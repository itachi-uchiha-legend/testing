from GitSyncManager import GitSyncManager
from SiemplifyJob import SiemplifyJob
from SiemplifyUtils import output_handler

SCRIPT_NAME = "Push Simulated Cases"


@output_handler
def main():
    siemplify = SiemplifyJob()
    siemplify.script_name = SCRIPT_NAME

    commit_msg = siemplify.extract_job_param("Commit")
    cases = list(
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

        for case_name in gitsync.api.get_simulated_cases():
            if case_name in cases:
                siemplify.LOGGER.info(f"Pushing simulated case {case_name}")
                gitsync.content.push_simulated_case(
                    case_name, gitsync.api.export_simulated_case(case_name)
                )

        gitsync.commit_and_push(commit_msg)

    except Exception as e:
        siemplify.LOGGER.error(f"General error performing Job {SCRIPT_NAME}")
        siemplify.LOGGER.exception(e)
        raise


if __name__ == "__main__":
    main()
