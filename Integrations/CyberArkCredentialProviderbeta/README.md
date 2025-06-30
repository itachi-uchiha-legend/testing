
# CyberArkCredentialProviderbeta

CyberArk’s Secrets Manager Credential Providers, part of the Privileged Access Security solution, is used to eliminate hard coded application credentials embedded in applications, scripts or configuration files, and allows these highly-sensitive passwords to be centrally stored, logged and managed within the Vault.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Path to clipasswordsdk|If you run CyberArk Credential Provider on Linux, enter the full path for the CLI Application Password SDK to retrieve credentials.|True|String|/opt/CARKaim/sdk/clipasswordsdk|
|Username for Credential Provider for Linux|If you run CyberArk Credential Provider on Linux and use Docker for the Google SecOps remote agent, enter the username for the remote agent to authenticate on a Linux host with installed Credential Provider.|True|String|secopsuser|
|Docker Gateway IP Address|If you run CyberArk Credential Provider on Linux and use Docker for the Google SecOps remote agent, enter the Docker gateway IP address for Credential Provider on Linux.|True|String|172.17.0.1|
|SSH Private Key Path|If you run CyberArk Credential Provider on Linux and use Docker for the Google SecOps remote agent,  it is recommended to use ssh key authentication and enter the full path for the Secure Shell (SSH) private key to authenticate on a Linux host with installed Credential Provider.|False|Password|None|
|Password for Credential Provider for Linux|If you run CyberArk Credential Provider on Linux and use Docker for the Google SecOps remote agent, specify the password to authenticate on a Linux host with installed Credential Provider.|False|Password|None|


#### Dependencies
| |
|-|
|rsa-4.9-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|httplib2-0.22.0-py3-none-any.whl|
|proto_plus-1.26.0-py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|pycparser-2.22-py3-none-any.whl|
|google_auth_httplib2-0.2.0-py2.py3-none-any.whl|
|PyNaCl-1.5.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_24_x86_64.whl|
|protobuf-5.29.3-cp38-abi3-manylinux2014_x86_64.whl|
|urllib3-2.3.0-py3-none-any.whl|
|pyasn1_modules-0.4.1-py3-none-any.whl|
|bcrypt-4.2.1-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|TIPCommon-2.0.10-py2.py3-none-any.whl|
|httpcore-1.0.7-py3-none-any.whl|
|idna-3.10-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|anyio-4.8.0-py3-none-any.whl|
|googleapis_common_protos-1.67.0-py2.py3-none-any.whl|
|certifi-2025.1.31-py3-none-any.whl|
|cachetools-5.5.1-py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|charset_normalizer-3.4.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|h11-0.14.0-py3-none-any.whl|
|google_api_python_client-2.161.0-py2.py3-none-any.whl|
|httpx-0.28.1-py3-none-any.whl|
|google_auth-2.38.0-py2.py3-none-any.whl|
|pyparsing-3.2.1-py3-none-any.whl|
|typing_extensions-4.12.2-py3-none-any.whl|
|pycryptodome-3.21.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|paramiko-3.5.1-py3-none-any.whl|
|cffi-1.17.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|google_api_core-2.24.1-py3-none-any.whl|
|cryptography-44.0.1-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|uritemplate-4.1.1-py2.py3-none-any.whl|
|pyasn1-0.6.1-py3-none-any.whl|


## Actions
#### Get Application Password Value
Use the Get Application Password Value to retrieve the application password value from CyberArk Credential Provider. Note: This action doesn't run on Google SecOps entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Output|The output fields. This parameter accepts multiple values as a comma-separated string.|True|String|Password|
|Application|The application ID to retrieve the password value.|True|String||
|Safe Name|The CyberArk Vault Safe name to retrieve the password value.|True|String||
|Folder Name|The CyberArk Vault folder name to retrieve the password value.|False|String||
|Object Name|The CyberArk Vault Object name to retrieve the password value.|True|String||



##### JSON Results
```json
{"result": "\"XXXX\""}
```



#### Ping
Use the Ping action to test the connectivity to Credential Provider. This action doesn’t run on Google SecOps entities.
Timeout - 600 Seconds



#### Run CLI Application Password SDK Command
Use the Run CLI Application Password SDK Command action to retrieve the application password from Credential Provider. 
This action doesn’t run on Google SecOps entities.

Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|clipasswordsdk Command|The command for the CLI Application Password SDK to run. The example of the command is as follows: GetPassword -p AppDescs.AppID=testappid2 -p Query="Safe=test;Object=testobject" -o Password.|True|String||



##### JSON Results
```json
{"result": "\"XXXX\""}
```









