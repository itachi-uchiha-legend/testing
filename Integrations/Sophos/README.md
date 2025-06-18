<p align="center"><img src="./Resources/Sophos.svg" 
     alt="Sophos" width="200"/></p>

# Sophos

Secure cloud workloads, data, apps, and access from the latest advanced threats and vulnerabilities.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|None|True|String|https://api.central.sophos.com|
|Client ID|None|True|String||
|Client Secret|None|True|Password|None|
|SIEM API Root|None|False|String||
|API Key|None|False|Password|None|
|Base 64 Auth Payload|None|False|Password|None|
|Verify SSL|None|False|Boolean|True|



## Actions
#### Unisolate Endpoint
Unisolate endpoints in Sophos. Supported entities: IP Address, Hostname. Note: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Comment|Specify the comment explaining why the unisolation is needed.|True|String||



#### Isolate Endpoint
Isolate endpoints in Sophos. Supported entities: IP Address, Hostname. Note: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Comment|Specify the comment explaining why the isolation is needed.|True|String||



#### Add Entities To Allowlist
Add entities to allowlist in Sophos. Supported entities: Filehash. Note: Only SHA-256 hashes are supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Comment|Specify the comment explaining why the hash was sent to allowlist.|True|String||



##### JSON Results
```json

```



#### Get Events Log
Retrieve logs related to the endpoints in Sophos. Supported entities: IP Address, Hostname. Note: events are accessible from API only for 24 hours. Requires valid “SIEM API Root”, “API Key” and “Base 64 Auth Payload” provided in the integration configuration.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Timeframe|Specify how many hours backwards events should be retrieved. Note: if the user provides more than 24 hours, action will still use 24.|True|String|12|
|Max Events To Return|Specify how many events to return per entity. Maximum: 1000|False|String|50|



##### JSON Results
```json
[{"Entity":"entity_identifier","EntityResult":{"events":[{"when":"2021-08-25T12:11:59.959Z","appSha256":"72828XXXXXb483f07e05XXXXXXXXX6d29390c7a4bbf6dXXXXX335cfeeec","appCerts":[{"signer":"KnowBe4 Inc.","thumbprint":"20f1ffXXXXXXXbe14398a440ddd8c8ec63XXXXXXX96387b4142XXXXX9a50"}],"threat":"KnowBe4 Ransomware Simulator","created_at":"2021-08-25T12:12:11.432Z","source_info":{"ip":"172.30.201.180"},"customer_id":"dfb85412-XXXX-XXXX-XXXX-03523a0178b8","severity":"medium","endpoint_id":"5fc739f3-XXXX-XXXX-XXXX-d77902621e3b","endpoint_type":"computer","user_id":"61238d60XXXXXXe83de9f54","origin":"SAV","core_remedy_items":null,"source":"XXXXX-H00\\Admin","type":"Event::Endpoint::CorePuaDetection","name":"PUA detected: 'KnowBe4 Ransomware Simulator' at 'C:\\Users\\Admin\\Desktop\\SimulatorSetup.exe'","location":"XXXXX-H00","id":"18e3b4a6-XXXX-XXXX-XXXX-5d7a8f29c438","group":"PUA"}]}}]
```



#### Execute Alert Actions
Initiate action execution on the alert in Sophos. Use action "List Alert Actions" to get a list of available actions for the alert.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert ID|Specify the ID of the alert on which you want to execute the action.|True|String||
|Action|Specify an action that should be executed on the alert.|True|List|Acknowledge|
|Message|Specify a message explaining why the action was executed.|False|String||



#### Get Services Status
Retrieve information about services on endpoints in Sophos. Supported entities: IP Address, Hostname.
Timeout - 600 Seconds



##### JSON Results
```json
[{"Entity":"entity_identifier","EntityResult":{"services":{"status":"good","serviceDetails":[{"name":"HitmanPro.Alert service","status":"running"},{"name":"Sophos Anti-Virus","status":"running"},{"name":"Sophos Anti-Virus Status Reporter","status":"running"}]}}}]
```



#### Ping
Test connectivity to the Sophos with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### List Alert Actions
Retrieve actions that can be executed on the alert in Sophos.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert ID|Specify the ID of the alert for which you want to retrieve details.|True|String||



##### JSON Results
```json
{"allowedActions":["clearThreat"]}
```



#### Scan Endpoints
Initiate a scan on endpoints in Sophos. Supported entities: IP Address, Hostname.
Timeout - 600 Seconds



#### Add Entities To Blocklist
Add entities to blocklist in Sophos. Supported entities: Filehash. Note: Only SHA-256 hashes are supported.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Comment|Specify the comment explaining why the hash was sent to blocklist.|True|String||



##### JSON Results
```json

```



#### Enrich Entities
Enrich entities using information from Sophos. Supported entities: Hostname, IP Address, File hash.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Create Insights|If enabled, action will create an insight containing all of the retrieved information about the entity.|False|Boolean|true|



##### JSON Results
```json
[{"Entity":"Sophos-H01","EntityResult":{"id":"5fc739f3-dcab-4a1a-a4cc-d77902621e3b","type":"computer","tenant":{"id":"dfb85412-db6e-4289-b5a1-03523a0178b8"},"hostname":"Sophos-H01","health":{"overall":"suspicious","threats":{"status":"suspicious"},"services":{"status":"good","serviceDetails":[{"name":"HitmanPro.Alert service","status":"running"}]}},"os":{"isServer":false,"platform":"windows","name":"Windows 10 Enterprise Evaluation","majorVersion":10,"minorVersion":0,"build":19043},"ipv4Addresses":["172.30.xxx.xxx"],"macAddresses":["00:50:56:xxxxxxx"],"associatedPerson":{"name":"SOPHOS-H01\\Admin","viaLogin":"SOPHOS-H01\\Admin","id":"3d5b16cc-cc1c-4adc-97fb-b57adc9b16d8"},"tamperProtectionEnabled":true,"assignedProducts":[{"code":"endpointProtection","version":"10.8.11.1","status":"installed"},{"code":"interceptX","version":"2.0.22","status":"installed"},{"code":"coreAgent","version":"2.19.6","status":"installed"}],"lastSeenAt":"2021-09-09T11:02:22.259Z"}},{"Entity":"ca978112ca1bbdcafac231b39xxxxxxxxxxxx","EntityResult":{"id":"2c43575d-7b8c-4b8a-a65c-4248662ef369","createdAt":"2021-09-01T12:50:34.879Z","properties":{"sha256":"ca978112ca1bbdcafac231b39xxxxxxxxxxx"},"comment":"asdasda","type":"sha256"}}]
```









## Connectors
#### Sophos Central - Alerts Connector
Pull alerts from Sophos Central into Siemplify. Note: alerts are available to API only for 24 hours.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|Enter the source field name in order to retrieve the Product Field name.|True|String|Product Name|
|EventClassId|Enter the source field name in order to retrieve the Event Field name.|True|String|type|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|PythonProcessTimeout|Timeout limit for the python process running the current script.|True|Integer|180|
|API Root|API root of the Sophos instance.|True|String|https:/{{api root}}|
|API Key|Sophos API key.|False|Password||
|Base 64 Auth Payload|Sophos Base 64 Auth Payload. Note: "Basic" shouldn't be a part of it.|False|Password||
|Client ID|Sophos Client ID.|False|String||
|Client Secret|Sophos Client Secret.|False|Password||
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Sophos Central server is valid.|False|Boolean|true|
|Lowest Severity To Fetch|Severity that will be used to fetch alerts. If nothing is specified, action will ingest all alerts. Possible values: Low, Medium, High.|False|String||
|Max Hours Backwards|Number of hours before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires. Maximum is 24 hours.|False|Integer|1|
|Max Alerts To Fetch|How many alerts to process per one connector iteration. Maximum is 1000.|False|Integer|10|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|Boolean|false|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password||




