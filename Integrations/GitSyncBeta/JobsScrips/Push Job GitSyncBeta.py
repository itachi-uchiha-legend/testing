from GitSyncManager import GitSyncManager
from SiemplifyJob import SiemplifyJob
from SiemplifyUtils import output_handler
from constants import IGNORED_JOBS, INTEGRATION_NAME
from definitions import Job

SCRIPT_NAME = "Push Job"


def create_root_readme(gitsync: GitSyncManager):
    jobs = []
    for job in gitsync.content.get_jobs():
        job.generate_readme(gitsync.content.metadata.get_readme_addon("Job", job.name))
        jobs.append(job)

    readme = "".join([x.readme for x in jobs])
    gitsync.update_readme(readme, "Jobs")


@output_handler
def main():
    siemplify = SiemplifyJob()
    siemplify.script_name = SCRIPT_NAME

    commit_msg = siemplify.extract_job_param("Commit")
    jobs = list(
        [
            _f
            for _f in [
                x.strip()
                for x in siemplify.extract_job_param("Job Whitelist", " ").split(",")
            ]
            if _f
        ]
    )
    readme_addon = siemplify.extract_job_param("Readme Addon", input_type=str)

    try:
        gitsync = GitSyncManager.from_siemplify_object(siemplify)

        for job in gitsync.api.get_jobs():
            if (
                job.get("name") in jobs
                and not job.get("name") in IGNORED_JOBS
                and job.get("integration") != INTEGRATION_NAME
            ):
                siemplify.LOGGER.info(f"Pushing {job['name']}")
                job = Job(job)
                if readme_addon:
                    siemplify.LOGGER.info(
                        "Readme addon found - adding to GitSync metadata file (GitSync.json)"
                    )
                    gitsync.content.metadata.set_readme_addon(
                        "Job", job.name, readme_addon
                    )
                gitsync.content.push_job(job)

        create_root_readme(gitsync)

        gitsync.commit_and_push(commit_msg)

    except Exception as e:
        siemplify.LOGGER.error(f"General error performing Job {SCRIPT_NAME}")
        siemplify.LOGGER.exception(e)
        raise


if __name__ == "__main__":
    main()
