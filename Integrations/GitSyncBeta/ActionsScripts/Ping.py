import re

from GitSyncManager import GitSyncManager
from SiemplifyAction import SiemplifyAction
from SiemplifyUtils import output_handler
from constants import COMMIT_AUTHOR_REGEX, DEFAULT_AUTHOR, DEFAULT_USERNAME


SCRIPT_NAME = "Ping"
INTEGRATION_NAME = "GitSync"


@output_handler
def main():
    siemplify = SiemplifyAction()
    siemplify.script_name = SCRIPT_NAME

    repo_url = siemplify.extract_configuration_param(INTEGRATION_NAME, "Repo URL")
    branch = siemplify.extract_configuration_param(INTEGRATION_NAME, "Branch")
    git_password = siemplify.extract_configuration_param(
        INTEGRATION_NAME, "Git Password/Token/SSH Key"
    )
    git_username = siemplify.extract_configuration_param(
        INTEGRATION_NAME, "Git Username", default_value=DEFAULT_USERNAME
    )
    git_author = siemplify.extract_configuration_param(
        INTEGRATION_NAME, "Commit Author", default_value=DEFAULT_AUTHOR
    )
    smp_verify = siemplify.extract_configuration_param(
        INTEGRATION_NAME, "Siemplify Verify SSL", input_type=bool
    )
    git_verify = siemplify.extract_configuration_param(
        INTEGRATION_NAME, "Git Verify SSL", input_type=bool
    )

    if not re.fullmatch(COMMIT_AUTHOR_REGEX, git_author):
        raise Exception(
            "Commit Author parameter must be in the following format: Name <example@gmail.com>"
        )

    try:
        gitsync = GitSyncManager(
            siemplify,
            repo_url,
            branch,
            git_password,
            git_username,
            git_author,
            smp_verify,
            git_verify,
        )
    except Exception as e:
        raise Exception(f"Couldn't connect to git\nError: {e}")

    try:
        gitsync.api.test_connectivity()
    except:
        raise Exception("Couldn't connect to Chronicle SOAR.")

    siemplify.end("True", True)


if __name__ == "__main__":
    main()
