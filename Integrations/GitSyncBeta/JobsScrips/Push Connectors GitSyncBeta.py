from GitSyncManager import GitSyncManager
from SiemplifyJob import SiemplifyJob
from SiemplifyUtils import output_handler
from definitions import Connector, Mapping, VisualFamily


SCRIPT_NAME = "Push Connector"


@output_handler
def main():
    siemplify = SiemplifyJob()
    siemplify.script_name = SCRIPT_NAME

    commit_msg = siemplify.extract_job_param("Commit")
    connector_names = list(
        [
            _f
            for _f in [
                x.strip()
                for x in siemplify.extract_job_param("Connectors", " ").split(",")
            ]
            if _f
        ]
    )
    include_vf = siemplify.extract_job_param("Include Visual Families", input_type=bool)
    include_mappings = siemplify.extract_job_param("Include Mappings", input_type=bool)
    readme_addon = siemplify.extract_job_param("Readme Addon", input_type=str)

    try:
        gitsync = GitSyncManager.from_siemplify_object(siemplify)

        for connector in gitsync.api.get_connectors():
            if connector.get("displayName") in connector_names:
                siemplify.LOGGER.info(f"Pushing {connector.get('displayName')}")
                if readme_addon:
                    siemplify.LOGGER.info(
                        "Readme addon found - adding to GitSync metadata file (GitSync.json)"
                    )
                    gitsync.content.metadata.set_readme_addon(
                        "Connector", connector.get("displayName"), readme_addon
                    )

                gitsync.content.push_connector(Connector(connector))
                siemplify.LOGGER.info(
                    f"Successfully pushed {connector.get('displayName')}"
                )

                if include_mappings or include_vf:
                    integration_name = connector.get("integration")
                    records = [
                        x
                        for x in gitsync.api.get_ontology_records()
                        if x.get("source") == integration_name
                    ]
                    visual_families = set([x.get("familyName") for x in records])
                    if include_mappings:
                        rules = []
                        for record in records:
                            record["exampleEventFields"] = []  # remove event assets
                            rule = gitsync.api.get_mapping_rules(
                                record["source"], record["product"], record["eventName"]
                            )
                            for r in rule["familyFields"] + rule["systemFields"]:
                                # remove bad rules with no source
                                if (
                                    r["mappingRule"]["source"]
                                    and r["mappingRule"]["source"].lower()
                                    == integration_name.lower()
                                ):
                                    rules.append(rule)
                                    break
                        if not records and not rules:
                            siemplify.LOGGER.info(
                                f"{integration_name} mappings don't exist. Skipping"
                            )
                        else:
                            siemplify.LOGGER.info(
                                f"Pushing {integration_name} mappings"
                            )
                            gitsync.content.push_mapping(
                                Mapping(integration_name, records, rules)
                            )

                    if include_vf:
                        for visualFamily in gitsync.api.get_custom_families():
                            if visualFamily["family"] in visual_families:
                                siemplify.LOGGER.info(
                                    f"Pushing Visual Family - {visualFamily['family']}"
                                )
                                gitsync.content.push_visual_family(
                                    VisualFamily(
                                        gitsync.api.get_custom_family(
                                            visualFamily["id"]
                                        )
                                    )
                                )

        gitsync.commit_and_push(commit_msg)

    except Exception as e:
        siemplify.LOGGER.error(f"General error performing Job {SCRIPT_NAME}")
        siemplify.LOGGER.exception(e)
        raise


if __name__ == "__main__":
    main()
