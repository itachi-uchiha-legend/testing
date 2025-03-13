from __future__ import annotations

import re
import tempfile
import uuid
from typing import Any

from jinja2 import Template

from GitContentManager import GitContentManager
from GitManager import Git
from SiemplifyAction import SiemplifyAction
from SiemplifyApiClient import SiemplifyApiClient
from SiemplifyJob import SiemplifyJob
from SiemplifyLogger import SiemplifyLogger
from cache import Cache, Context, get_context_factory
from constants import (
    ALL_ENVIRONMENTS_IDENTIFIER,
    COMMIT_AUTHOR_REGEX,
    DEFAULT_AUTHOR,
    DEFAULT_USERNAME,
    IGNORED_INTEGRATIONS,
    INTEGRATION_NAME,
    ROOT_README,
    ScriptType,
    WorkflowTypes,
)
from definitions import Connector, File, Integration, Job, Mapping, Workflow


class MergeConflictError(Exception):
    """A merge conflict was discovered."""


class GitSyncManager:
    """GitSync main interface

    This class holds and orchestrates all GitSync components.

    Attributes:
        git_client: A Git instance for handling all git operations
        api: A SiemplifyApiClient instance for communicating with Siemplify
        content: A GitContentManager instance for reading or writing objects from the repository to a define structure
        logger: A logger instance
    """

    def __init__(
        self,
        siemplify: SiemplifyAction | SiemplifyJob,
        repo_url: str,
        branch: str,
        git_password: str,
        git_username: str = "None",
        git_author: str = DEFAULT_AUTHOR,
        smp_verify: bool = True,
        git_verify: bool = True,
    ):
        self.logger = siemplify.LOGGER
        self._siemplify = siemplify
        self._cache = {}
        self._wd = tempfile.TemporaryDirectory(dir=siemplify.RUN_FOLDER)
        self.api = SiemplifyApiClient(siemplify.API_ROOT, siemplify.api_key, smp_verify)
        self.git_client = Git(
            repo_url,
            branch,
            self._wd.name,
            git_password,
            git_username,
            git_author,
            git_verify,
            self.logger,
        )
        self.content = GitContentManager(self.git_client, self.api)

    def __del__(self):
        self.logger.info("Cleaning up")
        self._wd.cleanup()

    @classmethod
    def from_siemplify_object(
        cls, siemplify: SiemplifyAction | SiemplifyJob
    ) -> GitSyncManager:
        """Init an instance using the siemplify job object

        Args:
            siemplify: SiemplifyJob instance

        Returns: A GitSyncManager instance
        """

        def get_conf_param(name, **kwargs):
            return siemplify.extract_configuration_param(
                INTEGRATION_NAME, name, **kwargs
            )

        siemplify.LOGGER.info("================= Param Init =================")
        repo_url = siemplify.extract_job_param("Repo URL", print_value=True)
        if not repo_url:
            repo_url = get_conf_param("Repo URL", print_value=True)

        branch = siemplify.extract_job_param("Branch", print_value=True)
        if not branch:
            branch = get_conf_param("Branch", print_value=True)

        git_author = siemplify.extract_job_param("Commit Author", print_value=True)
        if not git_author:
            git_author = get_conf_param(
                "Commit Author", print_value=True, default_value=DEFAULT_AUTHOR
            )

        if not re.fullmatch(COMMIT_AUTHOR_REGEX, git_author):
            raise Exception(
                "Commit Author parameter must be in the following format: Name <example@gmail.com>"
            )

        git_password = get_conf_param("Git Password/Token/SSH Key")
        git_username = get_conf_param(
            "Git Username", print_value=True, default_value=DEFAULT_USERNAME
        )
        smp_verify = get_conf_param(
            "Siemplify Verify SSL", print_value=True, input_type=bool
        )
        git_verify = get_conf_param("Git Verify SSL", print_value=True, input_type=bool)
        return cls(
            siemplify,
            repo_url,
            branch,
            git_password,
            git_username,
            git_author,
            smp_verify,
            git_verify,
        )

    def install_integration(self, integration: Integration) -> None:
        """Install or update a custom or commercial integration.

        There are two different flows to install an integration,
        If the integration is custom, the entire zip (ide/exportPackage) is used when pushing, so we import it
        as a zip file (ide/importPackage)
        if the integration is commercial, only custom items are pushed, that means we iterate the items, install new
        items and update existing ones.

        Args:
            integration: An Integration object instance to install
        """
        if integration.identifier in IGNORED_INTEGRATIONS:
            return
        self.logger.info(f"Installing {integration.identifier}")
        if integration.isCustom:
            self.logger.info(
                f"{integration.identifier} is a custom integration - importing as zip"
            )
            self.api.import_package(
                integration.identifier, integration.get_zip_as_base64()
            )
        else:
            self.logger.info(
                f"{integration.identifier} is a commercial integration - Checking installation"
            )
            if not self.get_installed_integration_version(integration.identifier):
                self.logger.info(
                    f"{integration.identifier} is not installed - installing from the marketplace"
                )
                if not self.install_marketplace_integration(integration.identifier):
                    self.logger.warn(
                        f"Couldn't install integration {integration.identifier} from the marketplace"
                    )
                    return
            integration_cards = next(
                x
                for x in self.api.get_ide_cards()
                if x["identifier"] == integration.identifier
            )["cards"]
            for script in integration.get_all_items():
                item_card = next(
                    (
                        x
                        for x in integration_cards
                        if x["name"] == script["name"] and x["type"] == script["type"]
                    ),
                    None,
                )
                if item_card:
                    script["id"] = item_card["id"]
                    self.logger.info(
                        f"Updating {integration.identifier} - {script['name']}"
                    )
                else:
                    self.logger.info(
                        f"Adding {integration.identifier} - {script['name']}"
                    )
                script["script"] = integration.get_script(
                    script.get("name"), ScriptType(script.get("type"))
                )
                self.api.update_ide_item(script)

    def install_connector(self, connector: Connector) -> None:
        """Installs or update a connector instance

        If the integration of the connector doesn't exist, will attempt to install it from the marketplace or from the
        git repository,
        If the connector instance integration version doesn't match the installed integration, the update button on the
        connector will forcibly activate to update the definition

        Args:
            connector: A Connector object instance to install
        """
        installed_version = self.get_installed_integration_version(
            connector.integration
        )
        if not installed_version:
            self.logger.info(
                f"Connector {connector.name} integration ({connector.integration}) not installed"
            )
            # Integration not installed - try installing from repo, and if not install from marketplace
            integration = self.content.get_integration(connector.integration)
            if integration and integration.isCustom:
                self.logger.info("Custom integration found in repo, installing")
                # Integration found in repo
                self.install_integration(integration)
            else:
                # Try installing integration from marketplace
                self.logger.info(
                    "Trying to install connector integration from the marketplace"
                )
                if not self.install_marketplace_integration(connector.integration):
                    raise Exception(
                        f"Error installing connector {connector.name} - missing integration"
                    )
                self.logger.info(
                    "Connector integration successfully installed from the marketplace"
                )
        if connector.integration_version != installed_version:
            self.logger.warn(
                "Installed integration version doesn't match the connector integration version. Please upgrade the "
                "connector."
            )
            connector.raw_data["isUpdateAvailable"] = True
        if connector.environment not in self.api.get_environment_names():
            self.logger.warn(
                f"Connector is set to non-existing environment {connector.environment}. Using Default Environment "
                f"instead"
            )
        self.api.update_connector(connector.raw_data)

    def install_mappings(self, mappings: Mapping) -> None:
        """Install or update mappings definitions

        Args:
            mappings: A Mapping object instance to install
        """
        self.logger.info(f"Installing mappings for {mappings.integrationName}")
        for rule in mappings.rules:
            self.api.add_mapping_rules(rule["familyFields"])
            self.api.add_mapping_rules(rule["systemFields"])

        for record in mappings.records:
            self.api.set_mappings_visual_family(
                record.get("source"),
                record.get("product"),
                record.get("eventName"),
                record.get("familyName"),
            )

    def install_workflows(self, workflows: list[Workflow]) -> None:
        """Install or update playbooks and blocks

        Args:
            workflows: A list of playbook instances to install

        Raises:
            Exception: When a playbook environment doesn't exist
        """
        # Validate all playbook environments exist as environments or environment groups
        environments = (
            self.api.get_environment_names()
            + self.api.get_environment_group_names()
            + [ALL_ENVIRONMENTS_IDENTIFIER]
        )
        for p in workflows:
            if not all(x in environments for x in p.environments):
                raise Exception(
                    f"Playbook {p.name} is assigned to environment that doesn't exist - {p.environments[0]}"
                )

        # Remove duplicates and split by type
        workflows = list(set(workflows))
        siemplify_context: Context = get_context_factory(self._siemplify)
        cache: Cache[str, int] = Cache(siemplify_context)
        playbook_installer = WorkflowInstaller(self.api, self.logger, cache)
        blocks, playbooks = [], []
        for workflow in workflows:
            if workflow.type == WorkflowTypes.BLOCK:
                blocks.append(workflow)

            else:
                playbooks.append(workflow)

        # Save blocks first
        for block in blocks:
            playbook_installer.install_workflow(block)

        playbook_installer.refresh_cache_item("playbooks")

        for playbook in playbooks:
            playbook_installer.install_workflow(playbook)

    def install_job(self, job: Job) -> None:
        """Installs or updates a job instance

        Args:
            job: A Job object instance to install
        """
        if not self.get_installed_integration_version(job.integration):
            self.logger.warn(
                f"Error installing job {job.name} - Job integration ({job.integration}) is not installed"
            )
            return
        # Try to find and fix the jobDefinitionId field
        integration_cards = next(
            (x for x in self.api.get_ide_cards() if x["identifier"] == job.integration),
            {},
        ).get("cards", None)
        if integration_cards:
            job_def_id = next(
                (
                    x
                    for x in integration_cards
                    if x["type"] == 2 and x["name"] == job.name
                ),
                None,
            )
            if job_def_id:
                job.raw_data["jobDefinitionId"] = job_def_id.get("id")

        job_id = next((x for x in self.api.get_jobs() if x["name"] == job.name), None)
        if job_id:
            job.raw_data["id"] = job_id.get("id")
        self.api.add_job(job.raw_data)

    def generate_root_readme(self) -> str:
        """Generates the readme file contents for the root of the repository

        Contains all assets currently in the repository

        Returns: Readme file contents
        """

        def strip_new_lines(s: str):
            # Description might be None
            return s.replace("\n", "").strip() if s else s

        integrations = [
            {
                "name": integration.definition["DisplayName"],
                "description": strip_new_lines(integration.definition["Description"]),
            }
            for integration in self.content.get_integrations()
        ]

        playbooks = [
            {
                "name": playbook.name,
                "description": strip_new_lines(playbook.description),
            }
            for playbook in self.content.get_playbooks()
        ]

        connectors = [
            {
                "name": connector.name,
                "description": strip_new_lines(connector.description),
                "hasMappings": (
                    True if self.content.get_mapping(connector.integration) else False
                ),
            }
            for connector in self.content.get_connectors()
        ]

        jobs = [
            {"name": job.name, "description": strip_new_lines(job.description)}
            for job in self.content.get_jobs()
        ]

        visual_families = [
            {"name": vf.name, "description": strip_new_lines(vf.description)}
            for vf in self.content.get_visual_families()
        ]

        readme = Template(ROOT_README)
        return readme.render(
            connectors=connectors,
            integrations=integrations,
            jobs=jobs,
            visualFamilies=visual_families,
            playbooks=playbooks,
        )

    def update_readme(self, readme: str, base_path: str = "") -> None:
        """Creates or updates a readme file in basePath

        Valid base_path format:
        - "Integrations"
        - "Playbooks/PlaybookName/"

        Args:
            readme: The readme contents
            base_path: Base path in the repo to write the readme file. Writes to root by default.
        """
        if base_path and not base_path.endswith("/"):
            base_path += "/"
        self.git_client.update_objects([File(f"{base_path}README.md", readme)])

    def commit_and_push(self, message: str) -> None:
        """Commits all the changes and pushes the commit to the repo

        Args:
            message: The commit message
        """

        if self.content.metadata.get_setting_by_name("update_root_readme"):
            # Generate root readme
            root_readme = self.generate_root_readme()
            self.update_readme(root_readme)

        self.content.metadata.system_version = self.api.get_system_version()
        self.content.push_metadata()
        self.git_client.commit_and_push(message)

    @property
    def _marketplace_integrations(self) -> list[dict]:
        if "marketplace" not in self._cache:
            self._cache["marketplace"] = self.api.get_store_data()
        return self._cache.get("marketplace")

    def clear_cache(self) -> None:
        self._cache = {}

    def refresh_cache_item(self, item_name) -> None:
        if item_name in self._cache:
            del self._cache[item_name]

    def install_marketplace_integration(self, integration_name: str) -> bool:
        """Installs or update an integration from the marketplace.

        Args:
            integration_name: Name of the integration to install

        Returns: True if the integration was installed successfully, otherwise False
        """
        store_integration = next(
            (
                x
                for x in self._marketplace_integrations
                if x["identifier"] == integration_name
            ),
            None,
        )
        if not store_integration:
            self.logger.warn(
                f"Integration {integration_name} wasn't found in the marketplace"
            )
            return False
        try:
            self.api.install_integration(
                integration_name,
                store_integration["version"],
                store_integration["isCertified"],
            )
            self.logger.info(f"{integration_name} installed successfully")
            return True
        except Exception as e:
            self.logger.warn(f"Couldn't install {integration_name} - {e}")
            return False

    def get_installed_integration_version(self, integration_name: str) -> float:
        """Get currently installed integration version

        If the integration is not installed, 0.0 will be returned

        Args:
            integration_name: Name of the integration to check

        Returns: Integration version
        """
        return next(
            (
                x["installedVersion"]
                for x in self._marketplace_integrations
                if x["identifier"] == integration_name
            ),
            0.0,
        )


class WorkflowInstaller:
    """Helper class for installing workflows"""

    def __init__(
        self,
        api: SiemplifyApiClient,
        logger: SiemplifyLogger,
        mod_time_cache: Cache[str, int],
    ) -> None:
        self.api: SiemplifyApiClient = api
        self.logger: SiemplifyLogger = logger
        self._mod_time_cache: Cache[str, int] = mod_time_cache
        self._cache: dict[str, Any] = {}

    def install_workflow(self, workflow: Workflow) -> None:
        """Save a playbook or block in the current platform

        Args:
            workflow: A Playbook object to install
        """
        if self._workflow_exists(workflow.name):
            self._update_workflow_if_needed(workflow)

        else:
            self.install_new_workflow(workflow)

    def _workflow_exists(self, __workflow_name: str, /) -> bool:
        """Check if a workflow exists (is installed) in the platform."""
        return __workflow_name in self._installed_playbooks

    def _update_workflow_if_needed(self, workflow: Workflow) -> None:
        if not self._workflow_was_modified(workflow):
            self.logger.info(f"Skipped update for unchanged workflow '{workflow.name}'")
            self._filter_and_save_context()
            return

        self._log_merge_conflicts(workflow)
        self.update_local_workflow(workflow)

    def _log_merge_conflicts(self, workflow: Workflow) -> None:
        if self._has_merge_conflicts(workflow):
            self.logger.warn(
                "Both the git playbook and local installed playbook were modified."
                "  Git version will override local changes!"
            )

    def _has_merge_conflicts(self, workflow: Workflow) -> bool:
        cached_time: int = self._mod_time_cache.get(workflow.name, -1)
        local_time: int = self._get_local_workflow_mod_time(workflow.name, -1)
        return min(local_time, workflow.modification_time) > cached_time

    def _workflow_was_modified(self, workflow: Workflow) -> bool:
        cached_time: int = self._mod_time_cache.get(workflow.name, -1)
        return workflow.modification_time > cached_time

    def update_local_workflow(self, workflow: Workflow) -> None:
        """Update an existing workflow in the platform."""
        self.logger.info(f"Updating existing workflow '{workflow.name}'")
        self._adjust_workflow_ids(workflow)
        self.api.save_playbook(workflow.raw_data)
        self._save_workflow_mod_time_to_context(workflow)
        self.logger.info(f"Workflow '{workflow.name}' was updated successfully")

    def _adjust_workflow_ids(self, workflow: Workflow) -> None:
        """Adjust workflow identifiers to match the existing workflow's
        (with the same name) identifiers.
        """
        playbook_id: str = self._installed_playbooks[workflow.name]["identifier"]
        local_playbook: dict[str, Any] = self.api.get_playbook(playbook_id)
        self._copy_ids_from_existing_workflow(workflow, local_playbook)
        self._process_steps(workflow, local_playbook)

    def install_new_workflow(self, workflow: Workflow) -> None:
        """Install a new workflow in the platform."""
        self.logger.info(f"Installing new workflow '{workflow.name}'")
        self._define_workflow_as_new(workflow)
        self._process_steps(workflow)
        self.api.save_playbook(workflow.raw_data)
        self._save_workflow_mod_time_to_context(workflow)
        self.logger.info(f"New workflow '{workflow.name}' was installed successfully")

    def _process_steps(
        self, workflow: Workflow, installed_workflow: dict = None
    ) -> None:
        """Iterate the playbook steps and assign the correct integration instances and block identifiers

        Args:
            workflow: Workflow to iterate steps
            installed_workflow: Optional current installed playbooks to copy identifiers
        """
        # A dict where the keys are the old step identifiers and values are the new step identifiers
        # Used for patching step relations
        identifier_mappings = {}
        # Flatten steps to include action containers
        old_steps = (
            self._flatten_playbook_steps(installed_workflow.get("steps"))
            if installed_workflow
            else None
        )
        for step in self._flatten_playbook_steps(workflow.raw_data.get("steps")):
            provider = step.get("actionProvider")
            step_type = step.get("type")

            step["workflowIdentifier"] = workflow.raw_data.get("identifier")
            # Take the step identifier if the same step instance name already exists.
            existing_step = (
                next(
                    (
                        x
                        for x in old_steps
                        if x.get("instanceName") == step.get("instanceName")
                    ),
                    None,
                )
                if old_steps
                else None
            )
            if existing_step:
                old_step_identifier = step.get("identifier")
                identifier_mappings[old_step_identifier] = existing_step.get(
                    "identifier"
                )
                step["identifier"] = existing_step.get("identifier")
                step["originalStepIdentifier"] = existing_step.get(
                    "originalStepIdentifier"
                )

                step_debug_data = step.get("debugData")
                if step_debug_data and step_debug_data.get("originalStepIdentifier"):
                    step_debug_data["originalStepIdentifier"] = existing_step.get(
                        "originalStepIdentifier"
                    )
                if step_debug_data and step_debug_data.get(
                    "originalWorkflowIdentifier"
                ):
                    step_debug_data["originalWorkflowIdentifier"] = (
                        installed_workflow.get("originalPlaybookIdentifier")
                    )

            if step_type == 0 and provider == "Scripts":  # Regular Action
                self._assign_integration_instance_to_step(
                    step, workflow.environments, existing_step
                )
            elif step_type == 5:  # Nested Workflow
                self._link_nested_block_step(step)

        for relation in workflow.raw_data.get("stepsRelations"):
            if relation.get("fromStep") in identifier_mappings:
                relation["fromStep"] = identifier_mappings.get(relation.get("fromStep"))
            if relation.get("toStep") in identifier_mappings:
                relation["toStep"] = identifier_mappings.get(relation.get("toStep"))

    def _save_workflow_mod_time_to_context(self, workflow: Workflow) -> None:
        self.refresh_cache_item("playbooks")
        new_mod_time: int = self._get_local_workflow_mod_time(workflow.name, -1)
        self._mod_time_cache[workflow.name] = new_mod_time
        self._filter_and_save_context()

    def _filter_and_save_context(self) -> None:
        self._mod_time_cache.filter_items(set(self._installed_playbooks))
        self._mod_time_cache.push_local_to_external()

    def _get_local_workflow_mod_time(
        self, __workflow_name: str, default: int | None = None, /
    ) -> int:
        playbook: dict[str, Any] = self._installed_playbooks[__workflow_name]
        return playbook.get("modificationTimeUnixTimeInMs", default)

    @property
    def _installed_playbooks(self) -> dict[str, dict[str, Any]]:
        """Currently installed playbooks and blocks"""
        if "playbooks" not in self._cache:
            self._cache["playbooks"] = {
                x.get("name"): x for x in self.api.get_playbooks()
            }
        return self._cache.get("playbooks")

    @property
    def _playbook_categories(self) -> dict:
        """Currently configured playbook categories"""
        if "categories" not in self._cache:
            self._cache["categories"] = {
                x.get("name"): x for x in self.api.get_playbook_categories()
            }
        return self._cache.get("categories")

    def refresh_cache_item(self, item_name) -> None:
        if item_name in self._cache:
            del self._cache[item_name]

    def _assign_integration_instance_to_step(
        self, step: dict, environments: list, existing_step: dict = None
    ) -> None:
        """Reconfigure an integration instance of a workflow step.

        If old_steps is supplied, It will first try to match the same step in the old playbook and assign
        the step to the same integration instance.
        Otherwise, If the playbook is assigned to only one environment (and not all environments), it will assign the
        first integration instance it finds.
        If the playbook is assigned to All Environments or more than one environment, The step will be set to
        dynamic mode, and assigned to the first shared instance, or None if it doesn't exist.

        Args:
            step: The step to reconfigure
            environments: Playbook assigned environments, for searching integration instances
            existing_step: Optional - if the step is already defined, take the integration instance from it instead
        """
        if existing_step:
            instance = self._get_step_parameter_by_name(
                existing_step, "IntegrationInstance"
            ).get("value")
            self._set_step_parameter_by_name(step, "IntegrationInstance", instance)
            fallback = self._get_step_parameter_by_name(
                existing_step, "FallbackIntegrationInstance"
            ).get("value")
            self._set_step_parameter_by_name(
                step, "FallbackIntegrationInstance", fallback
            )
            return
        # If the playbook is for one specific environment, choose the first integration instance from that environment
        # Otherwise, set the step to dynamic mode and set the first shared integration instance as fallback
        if len(environments) == 1 and environments[0] != ALL_ENVIRONMENTS_IDENTIFIER:
            integration_instances = self._find_integration_instances_for_step(
                step.get("integration"), environments[0]
            )
            if integration_instances:
                self._set_step_parameter_by_name(
                    step,
                    "IntegrationInstance",
                    integration_instances[0].get("identifier"),
                )
                self._set_step_parameter_by_name(
                    step, "FallbackIntegrationInstance", None
                )
        else:
            integration_instances = self._find_integration_instances_for_step(
                step.get("integration"), ALL_ENVIRONMENTS_IDENTIFIER
            )
            self._set_step_parameter_by_name(
                step, "IntegrationInstance", "AutomaticEnvironment"
            )
            if integration_instances:
                self._set_step_parameter_by_name(
                    step,
                    "FallbackIntegrationInstance",
                    integration_instances[0].get("identifier"),
                )
            else:
                self._set_step_parameter_by_name(
                    step, "FallbackIntegrationInstance", None
                )

    def _find_integration_instances_for_step(
        self, integration_name: str, environment: str
    ) -> list[dict]:
        """Find integration instances available for integration per environment

        Args:
            integration_name: The integration name to look for
            environment: The environment to fetch the integration instances

        Returns:
            A list of configured integration instances
        """
        cache_key = f"integration_instances_{environment}"
        if cache_key not in self._cache:
            self._cache[cache_key] = self.api.get_integrations_instances(environment)

        instances = self._cache.get(cache_key)
        instances.sort(key=lambda x: x.get("instanceName"))

        return [
            x
            for x in instances
            if x.get("integrationIdentifier") == integration_name
            and x.get("isConfigured")
        ]

    @staticmethod
    def _flatten_playbook_steps(steps: list) -> list[dict]:
        """Flatten playbook steps with parallel actions to one list

        Args:
            steps: The playbook steps to flatten

        Returns:
            Flattened list of steps
        """
        flat_steps = []
        for step in steps:
            if step.get("actionProvider") == "ParallelActionsContainer":
                flat_steps.extend(step.get("parallelActions"))
            flat_steps.append(step)
        return steps

    def _set_step_parameter_by_name(
        self, step: dict, parameter_name: str, parameter_value: str | None
    ):
        """Set the value of a step parameter

        Args:
            step: The step to reconfigure
            parameter_name: Name of the parameter to reconfigure
            parameter_value: New value of the parameter
        """
        self._get_step_parameter_by_name(step, parameter_name)[
            "value"
        ] = parameter_value

    @staticmethod
    def _get_step_parameter_by_name(step: dict, parameter_name: str) -> dict | None:
        """Get a workflow step parameter by name

        Args:
            step: The step to get the parameter from
            parameter_name: Name of the parameter

        Returns:
            The parameter dict instance, or None if not found
        """
        return next(
            (x for x in step.get("parameters") if x.get("name") == parameter_name), None
        )

    @staticmethod
    def _copy_ids_from_existing_workflow(workflow: Workflow, other: dict) -> None:
        """Reconfigure a workflow used another workflow ids

        Args:
            workflow: The workflow to copy the ids to
            other: A dict of the other workflow to copy the ids from
        """
        workflow.raw_data["id"] = other.get("id")
        workflow.raw_data["identifier"] = other.get("identifier")
        workflow.raw_data["originalPlaybookIdentifier"] = other.get(
            "originalPlaybookIdentifier"
        )
        workflow.raw_data["trigger"]["id"] = other.get("trigger").get("id")
        workflow.raw_data["trigger"]["identifier"] = other.get("trigger").get(
            "identifier"
        )
        workflow.raw_data["categoryName"] = other.get("categoryName")
        workflow.raw_data["categoryId"] = other.get("categoryId")

    def _define_workflow_as_new(self, workflow: Workflow) -> None:
        """Generate a new identifier and create the playbook category if it doesn't exist

        Args:
            workflow: A new workflow to reconfigure
        """
        workflow.raw_data["identifier"] = workflow.raw_data[
            "originalPlaybookIdentifier"
        ] = str(uuid.uuid4())
        workflow.raw_data["trigger"]["id"] = 0
        workflow.raw_data["trigger"]["identifier"] = str(uuid.uuid4())

        if workflow.category not in self._playbook_categories:
            category = self.api.create_playbook_category(workflow.category)
            self.refresh_cache_item("categories")
        else:
            category = self._playbook_categories.get(workflow.category)

        workflow.raw_data["categoryId"] = category.get("id")

    def _link_nested_block_step(self, step: dict) -> None:
        """Links a nested block step to the correct block that is stored on the system

        Args:
            step: A nested workflow step to reconfigure
        """
        if (
            step.get("name") in self._installed_playbooks
            and self._installed_playbooks[step.get("name")].get("playbookType")
            == WorkflowTypes.BLOCK.value
        ):
            nested_workflow_identifier = self._get_step_parameter_by_name(
                step, "NestedWorkflowIdentifier"
            )
            if nested_workflow_identifier:
                nested_workflow_identifier["value"] = self._installed_playbooks[
                    step.get("name")
                ].get("identifier")
