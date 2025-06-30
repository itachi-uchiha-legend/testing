import ipaddress

from TIPCommon.extraction import extract_configuration_param
from TIPCommon.types import ChronicleSOAR

import constants
from CyberArkCredentialProviderManager import CyberArkCredentialProviderManager
from datamodels import IntegrationParameters
import exceptions


def get_integration_parameters(soar_action: ChronicleSOAR) -> IntegrationParameters:
    """Extracts CyberArk Credential Provider integration configuration parameters.

    Args:
        soar_action: The ChronicleSOAR action object.

    Returns:
        IntegrationParameters: An IntegrationParameters object containing the
        extracted configuration parameters.
    """
    sdk_path: str = extract_configuration_param(
        soar_action,
        provider_name=constants.INTEGRATION_NAME,
        param_name="Path to clipasswordsdk",
        print_value=True,
    )
    username: str = extract_configuration_param(
        soar_action,
        provider_name=constants.INTEGRATION_NAME,
        param_name="Username for Credential Provider for Linux",
        print_value=True,
    )
    docker_gateway_ip: str = extract_configuration_param(
        soar_action,
        provider_name=constants.INTEGRATION_NAME,
        param_name="Docker Gateway IP Address",
        print_value=True,
    )
    ssh_private_key_path: str = extract_configuration_param(
        soar_action,
        provider_name=constants.INTEGRATION_NAME,
        param_name="SSH Private Key Path",
    )
    password: str = extract_configuration_param(
        soar_action,
        provider_name=constants.INTEGRATION_NAME,
        param_name="Password for Credential Provider for Linux",
    )
    integration_parameters: IntegrationParameters = IntegrationParameters(
        sdk_path=sdk_path,
        username=username,
        docker_gateway_ip=docker_gateway_ip,
        ssh_private_key_path=ssh_private_key_path,
        password=password,
    )

    return integration_parameters


def validate_ip_address(ip: str) -> None:
    """Validates whether an IP address is valid.

    Args:
        ip(str): The IP address to validate.

    Raises:
        CyberArkCredentialProviderValidationError: If the IP address is invalid.
    """
    try:
        ipaddress.ip_address(ip)
    except ValueError as e:
        raise exceptions.CyberArkCredentialProviderValidationError(
            f"Invalid Docker Gateway IP: {ip}. Please provide a valid IP address."
        ) from e


def initialize_credential_provider_manager(soar_action: ChronicleSOAR):
    """Initializes the CyberArk Credential Provider Manager.

    Args:
        soar_action: The ChronicleSOAR action object.

    Returns:
        CyberArkCredentialProviderManager: An instance of the 
        CyberArkCredentialProviderManager.
    """
    integration_parameters = get_integration_parameters(soar_action)
    return CyberArkCredentialProviderManager(
        sdk_path=integration_parameters.sdk_path,
        username=integration_parameters.username,
        docker_gateway_ip=integration_parameters.docker_gateway_ip,
        ssh_private_key_path=integration_parameters.ssh_private_key_path,
        password=integration_parameters.password,
    )
