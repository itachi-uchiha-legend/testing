class CyberArkCredentialProviderManagerError(Exception):
    """General Error For CyberArk Credential Provider"""


class CyberArkCredentialProviderSDKCommandError(Exception):
    """CLI Application Password SDK Command Error For CyberArk Credential Provider"""


class CyberArkCredentialProviderNotFoundError(CyberArkCredentialProviderManagerError):
    """Not Found Error For CyberArk Credential Provider"""


class CyberArkCredentialProviderValidationError(CyberArkCredentialProviderManagerError):
    """Validation Error For CyberArk Credential Provider"""


class CyberArkCredentialProviderNoValidConnectionsError(
    CyberArkCredentialProviderManagerError
):
    """No Valid Connections Error For CyberArk Credential Provider"""
