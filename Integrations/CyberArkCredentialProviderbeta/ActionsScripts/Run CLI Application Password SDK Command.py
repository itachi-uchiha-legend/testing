from typing import NoReturn

from TIPCommon.base.action import Action
from TIPCommon.extraction import extract_action_param

import constants
from CyberArkCredentialProviderManager import (
    CyberArkCredentialProviderManager,
    CommandResult,
)
import exceptions
import utils


class RunCLIApplicationPasswordSDKCommand(Action):

    def __init__(self) -> None:
        super().__init__(constants.RUN_CLI_APP_PASSWORD_SDK_COMMAND_SCRIPT_NAME)
        self.output_message = ""
        self.error_output_message = (
            "Error executing action "
            f'"{constants.RUN_CLI_APP_PASSWORD_SDK_COMMAND_SCRIPT_NAME}".'
        )

    def _extract_action_parameters(self) -> None:
        self.params.integration_parameters = utils.get_integration_parameters(
            self.soar_action
        )
        self.params.custom_sdk_command = extract_action_param(
            self.soar_action,
            param_name="clipasswordsdk Command",
            print_value=True,
            is_mandatory=True,
        )

    def _init_api_clients(self) -> CyberArkCredentialProviderManager:
        return utils.initialize_credential_provider_manager(self.soar_action)

    def _validate_params(self) -> None:
        utils.validate_ip_address(self.params.integration_parameters.docker_gateway_ip)

    def _perform_action(self, _) -> None:
        result: CommandResult = self.api_client.execute_custom_sdk_command(
            command=self.params.custom_sdk_command
        )

        if result.error:
            self.error_output_message = (
                "Error executing the following command: "
                f"{self.params.custom_sdk_command}. "
            )
            raise exceptions.CyberArkCredentialProviderSDKCommandError(result.error)

        self.output_message = (
            "Successfully executed the following CLI Application Password SDK command "
            f"{self.params.custom_sdk_command}."
        )
        self.soar_action.result.add_result_json({"result": result.output})


def main() -> NoReturn:
    RunCLIApplicationPasswordSDKCommand().run()


if __name__ == "__main__":
    main()
