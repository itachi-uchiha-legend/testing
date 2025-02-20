from io import BytesIO

from GitSyncManager import GitSyncManager
from SiemplifyJob import SiemplifyJob
from SiemplifyUtils import output_handler
from definitions import Integration


SCRIPT_NAME = "Push Integration"


@output_handler
def main():
    siemplify = SiemplifyJob()
    siemplify.script_name = SCRIPT_NAME

    push_allowlist = list(
        [
            _f
            for _f in [
                x.strip()
                for x in siemplify.extract_job_param("Push Whitelist", " ").split(",")
            ]
            if _f
        ]
    )
    commit_msg = siemplify.extract_job_param("Commit")
    readme_addon = siemplify.extract_job_param("Readme Addon", input_type=str)

    try:
        gitsync = GitSyncManager.from_siemplify_object(siemplify)

        integrations = [
            x for x in gitsync.api.get_ide_cards() if x["identifier"] in push_allowlist
        ]

        for integration in integrations:
            siemplify.LOGGER.info(f"Pushing Integration: {integration['identifier']}")
            integration_obj = Integration(
                integration,
                BytesIO(gitsync.api.export_package(integration["identifier"])),
            )
            if readme_addon:
                siemplify.LOGGER.info(
                    "Readme addon found - adding to GitSync metadata file (GitSync.json)"
                )
                gitsync.content.metadata.set_readme_addon(
                    "Integration", integration.identifier, readme_addon
                )
            gitsync.content.push_integration(integration_obj)

        gitsync.commit_and_push(commit_msg)

    except Exception as e:
        siemplify.LOGGER.error(f"General error performing Job {SCRIPT_NAME}")
        siemplify.LOGGER.exception(e)
        raise

    siemplify.end_script()


if __name__ == "__main__":
    main()
