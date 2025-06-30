from GitSyncManager import GitSyncManager
from SiemplifyJob import SiemplifyJob
from SiemplifyUtils import output_handler

SCRIPT_NAME = "Pull Simulated Cases"


@output_handler
def main():
    siemplify = SiemplifyJob()
    siemplify.script_name = SCRIPT_NAME

    case_names = list(
        [
            _f
            for _f in [
                x.strip()
                for x in siemplify.extract_job_param("Simulated Cases", " ").split(",")
            ]
            if _f
        ]
    )

    try:
        gitsync = GitSyncManager.from_siemplify_object(siemplify)

        for case_name in case_names:
            siemplify.LOGGER.info(f"Pulling {case_name}")
            case = gitsync.content.get_simulated_case(case_name)
            gitsync.api.import_simulated_case(case)
            siemplify.LOGGER.info(f"Successfully pulled simulated case: {case_name}")

    except Exception as e:
        siemplify.LOGGER.error(f"General error performing Job {SCRIPT_NAME}")
        siemplify.LOGGER.exception(e)
        raise

    siemplify.end_script()


if __name__ == "__main__":
    main()
