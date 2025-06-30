from __future__ import annotations

from collections import namedtuple

import constants
import exceptions

import paramiko
from paramiko.ssh_exception import NoValidConnectionsError, SSHException


CommandResult = namedtuple("CommandResult",["output", "error", "exit_code"])


class CyberArkCredentialProviderManager:
    """CyberArk Credential Provider Manager"""
    def __init__(
        self,
        sdk_path: str = None,
        username: str = None,
        docker_gateway_ip: str = None,
        ssh_private_key_path: str = None,
        password: str = None,
    ) -> None:
        self.sdk_path: str = sdk_path
        self.username: str = username
        self.docker_gateway_ip: str = docker_gateway_ip
        self.ssh_private_key_path: str = ssh_private_key_path
        self.password: str = password
        self.client = paramiko.SSHClient()
        self._create_ssh_client()

    def _create_ssh_client(self) -> None:
        """Set up the ssh connection with the target host.

        Raises:
            CyberArkCredentialProviderNoValidConnectionsError: When no policy is set
            or general SSH connection error.
        """
        try:
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            if self.ssh_private_key_path:
                private_key = paramiko.RSAKey(filename=self.ssh_private_key_path)
                self.client.connect(
                    self.docker_gateway_ip,
                    username=self.username,
                    pkey=private_key
                )
            elif self.password:
                self.client.connect(
                    self.docker_gateway_ip,
                    username=self.username,
                    password=self.password
                )
            else:
                raise exceptions.CyberArkCredentialProviderNoValidConnectionsError(
                    "No valid authentication method provided. "
                    "Please provide either an SSH private key or a password."
                )
        except(
            NoValidConnectionsError,
            paramiko.BadHostKeyException,
            SSHException,
        ) as err:
            raise exceptions.CyberArkCredentialProviderNoValidConnectionsError(
                f"Unable to connect - {err}"
            ) from err

    def execute_command_on_server(self, command: str) -> CommandResult:
        """Executes a command on the SSH Server.
        Args:
            command(str): The command to execute on the server.

        Returns:
            CommandResult: A namedtuple with the following fields:
            output, error, exit_code.
        """
        _, stdout, stderr = self.client.exec_command(command)
        output: str = stdout.read().decode("utf-8")
        error: str = stderr.read().decode("utf-8")
        exit_code: int = stdout.channel.recv_exit_status()

        return CommandResult(output=output, error=error, exit_code=exit_code)

    def test_connectivity(self) -> CommandResult:
        """Tests the connectivity to the Integration.

        Returns:
            CommandResult: A namedtuple with the following fields:
            output, error, exit_code.
        """
        test_command: str = f"{self.sdk_path} {constants.TEST_COMMAND}"
        result: CommandResult = self.execute_command_on_server(command=test_command)
        self.client.close()

        return result

    def get_application_password(
        self,
        application_id: str = None,
        safe_name: str = None,
        folder_name: str = None,
        object_name: str = None,
        output_field: str = constants.PASSWORD_OUTPUT_FIELD
    ) -> CommandResult:
        """Retrieves the password for a specified application id from
        CyberArk Credential Provider.

        Args:
            application_id(str): The ID of the application.
            safe_name(str): The safe name of the vault.
            folder_name(str): The folder name of the vault.
            object_name(str): The object name of the vault.
            output_field(str): The output field. Defaults to "Password".

        Returns:
            CommandResult: A namedtuple with the following fields:
            output, error, exit_code.
        """
        command: str = (
            f"{self.sdk_path} GetPassword "
            f"-p AppDescs.AppID={application_id} "
            f'-p Query="Safe={safe_name};Object={object_name}" '
            f"-o {output_field}"
        )
        if folder_name:
            command: str = (
                f"{self.sdk_path} GetPassword "
                f"-p AppDescs.AppID={application_id} "
                f'-p Query="Safe={safe_name};'
                f"Folder={folder_name};"
                f'Object={object_name}" '
                f"-o {output_field}"
            )

        result: CommandResult = self.execute_command_on_server(command=command)
        self.client.close()

        return result

    def execute_custom_sdk_command(self, command: str) -> CommandResult:
        """Execute a custom command on CyberArk Credential Provider.

        Args:
            command(str): The custom command to execute.

        Returns:
            CommandResult: A namedtuple with the following fields:
            output, error, exit_code.
        """
        command = f"{self.sdk_path} {command}"
        result: CommandResult = self.execute_command_on_server(command=command)
        self.client.close()

        return result
