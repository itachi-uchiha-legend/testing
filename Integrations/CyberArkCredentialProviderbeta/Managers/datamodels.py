import dataclasses


@dataclasses.dataclass(slots=True)
class IntegrationParameters:
    """Data class to hold the integration parameters for CyberArk Credential Provider.

    Attributes:
        sdk_path (str): The path to the clipasswordsdk.
        username (str): The username for the Credential Provider for Linux.
        docker_gateway_ip (str): The Docker Gateway IP Address.
        ssh_private_key_path (str): The path to the SSH private key.
        password (str): The password for the Credential Provider for Linux.
    """
    sdk_path: str
    username: str
    docker_gateway_ip: str
    ssh_private_key_path: str
    password: str
