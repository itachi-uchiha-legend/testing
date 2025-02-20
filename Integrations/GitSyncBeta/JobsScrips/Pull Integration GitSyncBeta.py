from GitSyncManager import GitSyncManager
from SiemplifyJob import SiemplifyJob
from SiemplifyUtils import output_handler

SCRIPT_NAME = "Pull Integration"


@output_handler
def main():
    siemplify = SiemplifyJob()
    siemplify.script_name = SCRIPT_NAME

    pull_whitelist = list(
        [
            _f
            for _f in [
                x.strip()
                for x in siemplify.extract_job_param("Install Whitelist", " ").split(
                    ","
                )
            ]
            if _f
        ]
    )

    try:
        gitsync = GitSyncManager.from_siemplify_object(siemplify)

        for integration_name in pull_whitelist:
            siemplify.LOGGER.info(f"Pulling Integration: {integration_name}")
            integration = gitsync.content.get_integration(integration_name)
            if integration:
                siemplify.LOGGER.info(f"Installing {integration.identifier}")
                gitsync.install_integration(integration)
                siemplify.LOGGER.info(
                    f"Successfully installed {integration.identifier}"
                )
            else:
                siemplify.LOGGER.info(f"Couldn't find {integration_name} in the repo")

    except Exception as e:
        siemplify.LOGGER.error(f"General error performing Job {SCRIPT_NAME}")
        siemplify.LOGGER.exception(e)
        raise

    siemplify.end_script()


if __name__ == "__main__":
    main()
