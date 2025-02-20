from GitSyncManager import GitSyncManager
from SiemplifyJob import SiemplifyJob
from SiemplifyUtils import output_handler

SCRIPT_NAME = "Pull Custom Family"


@output_handler
def main():
    siemplify = SiemplifyJob()
    siemplify.script_name = SCRIPT_NAME

    family_name = siemplify.extract_job_param("Family Name")

    try:
        gitsync = GitSyncManager.from_siemplify_object(siemplify)

        siemplify.LOGGER.info(f"Pulling {family_name}")
        family = gitsync.content.get_visual_family(family_name)
        if family:
            gitsync.api.add_custom_family(family.raw_data)
            siemplify.LOGGER.info(f"Successfully pulled {family_name}")
        else:
            siemplify.LOGGER.info(f"Family {family_name} not found")

    except Exception as e:
        siemplify.LOGGER.error(f"General error performing Job {SCRIPT_NAME}")
        siemplify.LOGGER.exception(e)
        raise

    siemplify.end_script()


if __name__ == "__main__":
    main()
