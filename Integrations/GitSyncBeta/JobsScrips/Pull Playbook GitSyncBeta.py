from GitSyncManager import GitSyncManager
from SiemplifyJob import SiemplifyJob
from SiemplifyUtils import output_handler

SCRIPT_NAME = "Pull Playbook"


@output_handler
def main():
    siemplify = SiemplifyJob()
    siemplify.script_name = SCRIPT_NAME

    pull_whitelist = list(
        [
            _f
            for _f in [
                x.strip()
                for x in siemplify.extract_job_param("Playbook Whitelist", " ").split(
                    ","
                )
            ]
            if _f
        ]
    )
    include_blocks = siemplify.extract_job_param(
        "Include Playbook Blocks", input_type=bool
    )

    try:
        gitsync = GitSyncManager.from_siemplify_object(siemplify)

        playbooks = {}
        for playbook_name in pull_whitelist:
            siemplify.LOGGER.info(f"Pulling {playbook_name}")
            playbook = gitsync.content.get_playbook(playbook_name)
            if not playbook:
                siemplify.LOGGER.info(f"{playbook_name} not found in the repository")
                continue
            playbooks[playbook.name] = playbook
            if include_blocks:
                for block in playbook.get_involved_blocks():
                    if block.get("name") not in playbooks:
                        block = gitsync.content.get_playbook(block.get("name"))
                        if block:
                            playbooks[block.name] = block

        gitsync.install_workflows(list(playbooks.values()))

    except Exception as e:
        siemplify.LOGGER.error(f"General error performing Job {SCRIPT_NAME}")
        siemplify.LOGGER.exception(e)
        raise

    siemplify.end_script()


if __name__ == "__main__":
    main()
