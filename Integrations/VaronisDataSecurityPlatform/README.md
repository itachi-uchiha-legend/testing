
# VaronisDataSecurityPlatform

Capture and search every important action at petabyte scale. Varonis creates a normalized record of every important action on your data—on-premises and in the cloud.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|None|True|String|https://{ip address}:{port}|
|Username|None|True|String||
|Password|None|True|Password|None|
|Verify SSL|None|False|Boolean|false|


#### Dependencies
| |
|-|
|charset_normalizer-3.3.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|requests-2.32.3-py3-none-any.whl|
|idna-3.7-py3-none-any.whl|
|pyOpenSSL-24.2.1-py3-none-any.whl|
|cffi-1.17.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|chardet-5.2.0-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|TIPCommon-1.0.12-py2.py3-none-any.whl|
|cryptography-43.0.0-cp39-abi3-manylinux_2_28_x86_64.whl|
|requests_ntlm-1.3.0-py3-none-any.whl|
|pycparser-2.22-py3-none-any.whl|
|pyspnego-0.11.1-py3-none-any.whl|
|certifi-2024.7.4-py3-none-any.whl|
|EnvironmentCommon-1.0.1-py2.py3-none-any.whl|


## Actions
#### Update Alert
Update status of alerts ingested from the Varonis Data Security Platform connector with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert GUID|Specify alert GUID for the update. This action can run on multiple alerts. Multiple alerts can be specified as a comma-separated string.|True|String||
|Alert Status|Specify the alert status to update to.|True|List|Select One|
|Closing Reason|Specify the closing reason for the alert. When the alert status is changed to "closed", closing reason must be specified.|False|List|Not Provided|



#### Ping
Test connectivity to the Varonis Data Security Platform with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds









## Connectors
#### Varonis Data Security Platform Alerts Connector
Connector can be used to fetch alerts from the Varonis Data Security Platform. The connector dynamic list can be used to filter specific alerts for ingestion based on the Varonis Data Security Platform alert name.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|A framework parameter that must be set for every connector. Describes the name of the event field where the product name is stored.|True|String|device_product|
|EventClassId|A framework parameter that must be set for every connector. Describes the name of the event field where the event name is stored.|True|String|Type|
|Environment Field Name|Describes the name of the event field where the environment name is stored.If the environment field isn't found, the environment is "".|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field.Default is .* to catch all and return value unchanged.Used to allow the user to manipulate the environment field through regex logicIf the regex pattern is null or empty, or the environment value is null, the final environment result is "".|False|String|.*|
|PythonProcessTimeout|Timeout limit for the python process running the connector.|True|Integer|300|
|API Root|Specify the API URL for the target Varonis Data Security Platform instance.|True|String|https://{ip address}:{port}|
|Username|Specify the username to connect with.|True|String||
|Password|Specify the password to connect with.|True|Password||
|Verify SSL|If enabled, the certificate configured for the API root is validated.|False|Boolean|false|
|Max Days Backwards|Number of days before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|True|Integer|3|
|Max Alerts per Cycle|Fetch X alerts per connector cycle.|True|Integer|10|
|Max Events per Varonis alert|Maximum number of events that the connector fetches for the Data Security Platform alert.|True|Integer|25|
|Status|Data Security Platform alert statuses to fetch.|True|String|Open, Under Investigation, Closed|
|Severity|Data Security Platform alert severities to fetch.|True|String|Low, Medium, High|
|Disable Overflow|If enabled, the connector ignores the Chronicle SOAR overflow mechanism when creating alerts.|False|Boolean|false|
|Use Dynamic List as BlockList|If enabled, the connector uses alert names specified in the Dynamic list as a BlockList. It ingests only alerts that don't match Dynamic List.|False|Boolean|false|
|Alert Name Template|If provided, the connector uses this value for Chronicle SOAR Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Varonis alert - [name]. Note: The connector first uses CSOAR Event for placeholders. Only keys that have string value are handled. If nothing is provided or the user provides an invalid template, the connector uses the default alert name - [name].|False|String|[Name]|
|Rule Generator Template|If provided, the connector uses this value for Chronicle SOAR Rule Generator Value. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Varonis alert - [name]. Note: The connector first uses Chronicle SOAR Event for placeholders. Only keys that have string value are handled. If nothing is provided or the user provides an invalid template, the connector uses the default rule generator - [name].|False|String|[Name]|
|Proxy Server Address|Proxy server to use for connection to the mail server.|False|String||
|Proxy Username|Proxy server username|False|String||
|Proxy Password|Proxy server password|False|Password||




