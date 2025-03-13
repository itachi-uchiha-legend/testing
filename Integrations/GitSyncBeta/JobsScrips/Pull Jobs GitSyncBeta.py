from GitSyncManager import GitSyncManager
from SiemplifyJob import SiemplifyJob
from SiemplifyUtils import output_handler

SCRIPT_NAME = "Pull Jobs"


@output_handler
def main():
    siemplify = SiemplifyJob()
    siemplify.script_name = SCRIPT_NAME

    job_names = list(
        [
            _f
            for _f in [
                x.strip()
                for x in siemplify.extract_job_param("Job Whitelist", " ").split(",")
            ]
            if _f
        ]
    )

    try:
        gitsync = GitSyncManager.from_siemplify_object(siemplify)

        for job in job_names:
            siemplify.LOGGER.info(f"Pulling {job}")
            job = gitsync.content.get_job(job)
            gitsync.install_job(job)
            siemplify.LOGGER.info(f"Successfully pulled Job {job.name}")

    except Exception as e:
        siemplify.LOGGER.error(f"General error performing Job {SCRIPT_NAME}")
        siemplify.LOGGER.exception(e)
        raise

    siemplify.end_script()


if __name__ == "__main__":
    main()
