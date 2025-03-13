from typing import NoReturn

from TIPCommon.base.action import Action

import constants
from CyberArkCredentialProviderManager import (
    CyberArkCredentialProviderManager,
    CommandResult,
)
import exceptions
import utils


class Ping(Action):
    def __init__(self) -> None:
        super().__init__(constants.PING_SCRIPT_NAME)
        self.output_message = ""
        self.error_output_message = (
            "Failed to connect to the CyberArk Credential Provider installation!"
        )

    def _extract_action_parameters(self) -> None:
        self.params.integration_parameters = utils.get_integration_parameters(
            self.soar_action
        )

    def _init_api_clients(self) -> CyberArkCredentialProviderManager:
        return utils.initialize_credential_provider_manager(self.soar_action)

    def _perform_action(self, _) -> None:
        result: CommandResult = self.api_client.test_connectivity()

        if result.exit_code != 0:
            raise exceptions.CyberArkCredentialProviderManagerError(
                f"{self.error_output_message}. Error is {result.error}"
            )
        self.output_message = (
            "Successfully connected to the CyberArk Credential Provider "
            "installation with the provided connection parameters!"
        )
        self.logger.info(self.output_message)
        self.logger.info("Starting action finalizing steps")


def main() -> NoReturn:
    Ping().run()


if __name__ == "__main__":
    main()
