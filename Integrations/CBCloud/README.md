
# CBCloud

The VMware Carbon Black Cloud is a cloud-native endpoint protection platform (EPP) that combines the intelligent system hardening and behavioral prevention needed to keep emerging threats at bay, using a single lightweight agent, and an easy-to-use console.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|None|True|String||
|Organization Key|None|True|String||
|API ID|None|True|Password|None|
|API Secret Key|None|True|Password|None|
|Verify SSL|None|False|Boolean||


#### Dependencies
| |
|-|
|uritemplate-4.1.1-py2.py3-none-any.whl|
|google_auth_httplib2-0.2.0-py2.py3-none-any.whl|
|google_auth-2.32.0-py2.py3-none-any.whl|
|googleapis_common_protos-1.63.2-py2.py3-none-any.whl|
|arrow-1.3.0-py3-none-any.whl|
|httplib2-0.22.0-py3-none-any.whl|
|pycryptodome-3.20.0-cp35-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|protobuf-5.27.2-cp38-abi3-manylinux2014_x86_64.whl|
|google_api_python_client-2.137.0-py2.py3-none-any.whl|
|exceptiongroup-1.1.1-py3-none-any.whl|
|idna-3.8-py3-none-any.whl|
|proto_plus-1.24.0-py3-none-any.whl|
|httpx-0.24.1-py3-none-any.whl|
|certifi-2024.8.30-py3-none-any.whl|
|six-1.16.0-py2.py3-none-any.whl|
|types_python_dateutil-2.9.0.20240821-py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|pyasn1_modules-0.4.0-py3-none-any.whl|
|h11-0.14.0-py3-none-any.whl|
|cachetools-5.4.0-py3-none-any.whl|
|TIPCommon-2.2.0-py2.py3-none-any.whl|
|anyio-3.7.1-py3-none-any.whl|
|rsa-4.9-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|pyparsing-3.1.2-py3-none-any.whl|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|pyasn1-0.6.0-py2.py3-none-any.whl|
|EnvironmentCommon-1.0.1-py2.py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|google_api_core-2.19.1-py3-none-any.whl|
|httpcore-0.17.3-py3-none-any.whl|


## Actions
#### Enable Bypass Mode for Device
Create enable bypass mode task for device on VMware Carbon Black Cloud server based on Siemplify IP or Host Siemplify entities.
Timeout - 600 Seconds



#### Delete a Reputation Override
Delete a Reputation Override based on the provided reputation override id. Note that action is not working on Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Reputation Override ID|Specify a Reputation Override ID to delete.|True|String||



#### Create a Reputation Override for Certificate
Create a Reputation Override for the certificate. Note that action is not working on Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Certificate Authority|Specify the Certificate Authority that authorizes the validity of the certificate to add to reputation override.|False|String||
|Signed By|Specify the name of the signer to add to reputation override.|True|String||
|Description|Specify a description for the created reputation override.|False|String||
|Reputation Override List|Specify override list to create.|True|List|Not Specified|



##### JSON Results
```json
[{"id":"38472c5bff7f11eb86dc8fXXXXXXXXXX","created_by":"XXXXXXXXXX","create_time":"XXXX-XX-XXTXX:XX:XX.XXXZ","override_list":"WHITE_LIST","override_type":"CERT","description":"XXXXXX","source":"APP","source_ref":"None","signed_by":"XXXXXXX","certificate_authority":"XXXXXXXX"}]
```



#### Device Background Scan
Create a device background scan task on VMware Carbon Black Cloud server based on the Siemplify IP or Host Siemplify entities.
Timeout - 600 Seconds



#### Enrich Entities
Enrich Siemplify Host or IP entities based on the device information from the VMware Carbon Black Cloud.
Timeout - 600 Seconds



##### JSON Results
```json
{"Entity":"siemplify-xxxx","EntityResult":{"activation_code":"BMMC1T","activation_code_expiry_time":"2021-02-23T13:50:35.424Z","ad_group_id":0,"appliance_name":null,"appliance_uuid":null,"av_ave_version":"8.3.62.144","av_engine":"4.14.3.454-ave.8.3.62.144:avpack.8.5.0.92:vdf.8.18.24.126","av_last_scan_time":null,"av_master":false,"av_pack_version":"8.5.0.92","av_product_version":"4.14.3.454","av_status":["AV_ACTIVE","ONDEMAND_SCAN_DISABLED"],"av_update_servers":null,"av_vdf_version":"8.18.24.126","cluster_name":null,"current_sensor_policy_name":"default","datacenter_name":null,"deployment_type":"WORKLOAD","deregistered_time":null,"device_meta_data_item_list":[{"key_name":"OS_MAJOR_VERSION","key_value":"Windows 10","position":0},{"key_name":"SUBNET","key_value":"172.30.202","position":0}],"device_owner_id":"395xxxx","email":"xxxxx@siemplify.co","encoded_activation_code":"XZZEPCWxxxxx","esx_host_name":null,"esx_host_uuid":null,"first_name":"xxxxx","id":"4048xxxx","last_contact_time":"2021-06-08T09:18:26.503Z","last_device_policy_changed_time":"2021-05-30T12:28:27.850Z","last_device_policy_requested_time":"2021-05-30T12:28:53.989Z","last_external_ip_address":"185.180.xx.xx","last_internal_ip_address":"172.30.xx.xx","last_location":"OFFSITE","last_name":"xxxx","last_policy_updated_time":"2021-05-26T16:26:08.391Z","last_reported_time":"2021-06-08T09:17:23.947Z","last_reset_time":null,"last_shutdown_time":null,"linux_kernel_version":null,"login_user_name":"","mac_address":"005056a28d9a","middle_name":null,"name":"Siemplify-CBH10","organization_id":1105,"organization_name":"cb-internal-alliances.com","os":"WINDOWS","os_version":"Windows 10 x64","passive_mode":false,"policy_id":6525,"policy_name":"default","policy_override":true,"quarantined":false,"registered_time":"2021-02-16T13:52:38.909Z","scan_last_action_time":null,"scan_last_complete_time":null,"scan_status":null,"sensor_kit_type":"WINDOWS","sensor_out_of_date":true,"sensor_pending_update":false,"sensor_states":["ACTIVE","LIVE_RESPONSE_NOT_RUNNING","LIVE_RESPONSE_NOT_KILLED","LIVE_RESPONSE_ENABLED","SECURITY_CENTER_OPTLN_DISABLED"],"sensor_version":"3.6.0.1979","status":"REGISTERED","target_priority":"LOW","uninstall_code":"618KA4ZP","vcenter_host_url":null,"vcenter_name":null,"vcenter_uuid":null,"vdi_base_device":null,"virtual_machine":true,"virtualization_provider":"VMW_ESX","vm_ip":null,"vm_name":null,"vm_uuid":null,"vulnerability_score":0,"vulnerability_severity":null,"windows_platform":null}}
```



#### Quarantine Device
Create quarantine device task on the VMware Carbon Black Cloud server based on the Siemplify IP or Host Siemplify entities.
Timeout - 600 Seconds



##### JSON Results
```json
[{"Entity":"siemplify-xxxx","EntityResult":{"status":"done"}}]
```



#### Dismiss VMware Carbon Black Cloud Alert
Dismiss VMware Carbon Black Cloud alert. Note: action accepts alert id in format 27162661199ea9a043c11ea9a29a93652bc09fd, not in format that is shown in UI as DONAELUN.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert ID|Alert ID to dismiss on VMware Carbon Black Cloud server.|True|String||
|Reason for dismissal|VMware Carbon Black Cloud reason for alert dismissal.|True|List|No dismissal reason|
|Determination|Specify the determination to set for an alert.|True|List|None|
|Message for alert dismissal|Message to add to alert dismissal.|False|String|The alert has been dismissed by Siemplify|



#### Disable Bypass Mode for Device
Create disable bypass mode task for devices on the VMware Carbon Black Cloud server based on the Siemplify IP or Host Siemplify entities.
Timeout - 600 Seconds



#### Execute Entity Processes Search
Execute Carbon Black Cloud Process Search based on the Siemplify Entity. Action can be used to search information about processes stored in Carbon Black Cloud with action input parameters and following Siemplify entities: IP, Host, User, Hash, Process.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Start from Row|Specify from which row action should fetch data.|False|String|0|
|Max Rows to Return|Specify how many rows action should return.|False|String|50|
|Create Insight|If enabled, action will create a Siemplify insight based on process info from Carbon Black Cloud.|False|Boolean|false|



##### JSON Results
```json
[{"EntityResult": {"results":[{"alert_category":["THREAT"],"alert_id":["19183229-XXXX-49a7-XXXX-87d0db243fcc","4dfc6aed-XXXX-41d1-XXXX-0de349d7a8b3"],"backend_timestamp":"2021-02-02T18:38:46.520Z","childproc_count":0,"crossproc_count":0,"device_external_ip":"161.47.37.87","device_group_id":0,"device_id":1111111,"device_installed_by":"sadiya@acalvio.com","device_internal_ip":"172.26.115.53","device_location":"UNKNOWN","device_name":"desktop1-win10","device_os":"WINDOWS","device_os_version":"Windows 10 x64","device_policy":"test","device_policy_id":12345,"device_target_priority":"HIGH","device_timestamp":"2020-08-19T16:31:20.887Z","document_guid":"sF1Ug1--SEyLWljQrWe8NA","event_threat_score":[6],"filemod_count":0,"ingress_time":1612291119946,"modload_count":0,"netconn_count":0,"org_id":"7DESJ9GN","parent_effective_reputation":"KNOWN_MALWARE","parent_guid":"7DESJ9GN-XXXXXXXX-000026d4-00000000-1d676428bd025e2","parent_hash":["86deb998e6b628755a104XXXXXX863d32752d6176fb1ef3b7c4ee08c1f25edbc"],"parent_name":"c:\\windows\\system32\\windowspowershell\\v1.o\\powershell.exe","parent_pid":9940,"parent_reputation":"KNOWN_MALWARE","process_cmdline":["powershell.exe -ep bypass"],"process_cmdline_length":[25],"process_effective_reputation":"COMPANY_BLACK_LIST","process_guid":"7DESJ9GN-XXXXXXXX-000005b8-00000000-1d676428bdf1285","process_hash":["908b64b1971a979cXXXXXXX4621945cba84854cb98d76367b791a6e22b5f6d53","cda48fc75952ad12d99e526d0b6bf70a"],"process_name":"c:\\windows\\system32\\windowspowershell\\v1.0\\powershell.exe","process_pid":[1464],"process_reputation":"COMPANY_BLACK_LIST","process_sha256":"908b64b1971a979cXXXXXXX4621945cba84854cb98d76367b791a6e22b5f6d53","process_start_time":"2020-08-19T16:05:24.057Z","process_username":["DESKTOP1-WIN10\\acalvio"],"regmod_count":0,"scriptload_count":0,"watchlist_hit":["BeCXz92RjiQxN1PnYlM6w:SdJksR9SsWuLCJNeBsNPw:10"]}],"num_found":1,"num_available":1,"approximate_unaggregated":6,"num_aggregated":6,"contacted":47,"completed":47}, "Entity": "EXAMPLE-HOST-001"}]
```



#### Ping
Test connectivity to the VMware Carbon Black Cloud
Timeout - 600 Seconds



#### Create a Reputation Override for SHA-256 Hash
Create a Reputation Override for the provided hash in SHA-256 format. Note: The SHA-256 hash can be provided either as a Siemplify FileHash (artifact) or as an action input parameter. If the hash is passed to action both as an entity and input parameter - action will be executed on the input parameter.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|SHA-256 Hash|Specify a SHA-256 hash value to create override for.|False|String||
|Filename|Specify a corresponding file name to add to reputation override.|True|String||
|Description|Specify a description for the created reputation override.|False|String||
|Reputation Override List|Specify override list to create.|True|List|Not Specified|



##### JSON Results
```json
[{"Entity":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","EntityResult":{"id":"2e41416fffa411eb83cf87XXXXXXXXXX","created_by":"XXXXXXXXXX","create_time":"XXXX-XX-XXTXX:XX:XX.XXXZ","override_list":"WHITE_LIST","override_type":"SHA256","description":"XXXX","source":"APP","source_ref":"XXXX","sha256_hash":"XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX","filename":"XXXX"}}]
```



#### List Host Vulnerabilities
List vulnerabilities found on the host in Сarbon Black Cloud. Supported entities: IP Address and Hostname.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Severity Filter|Specify the comma-separated list of severities for vulnerabilities. If nothing is provided, action will ingest all related vulnerabilities. Possible values: Critical, Important, Moderate, Low.|False|String||
|Max Vulnerabilities To Return|Specify how many vulnerabilities to return per host. If nothing is provided, action will process all of the related vulnerabilities.|False|String|100|



##### JSON Results
```json
[{"Entity":"10.0.xx.xx","EntityResult":{"statistics":{"total":2,"severity":{"critical":0,"important":0,"moderate":0,"low":2}},"details":[{"os_product_id":"22_14xxxxx","category":"APP","os_info":{"os_type":"WINDOWS","os_name":"Microsoft Windows 10 Enterprise","os_version":"10.0.18362","os_arch":"64-bit"},"product_info":{"vendor":"Google LLC","product":"Google Chrome","version":"96.0.4664.110","release":null,"arch":""},"vuln_info":{"cve_id":"CVE-xxxx-xxxx","cve_description":"test","risk_meter_score":1.1,"severity":"LOW","fixed_by":null,"solution":null,"created_at":"2009-01-20T16:30:00Z","nvd_link":"https://nvd.nist.gov/vuln/detail/CVE-xxxx-xxxx","cvss_access_complexity":null,"cvss_access_vector":null,"cvss_authentication":null,"cvss_availability_impact":null,"cvss_confidentiality_impact":null,"cvss_integrity_impact":null,"easily_exploitable":null,"malware_exploitable":null,"active_internet_breach":null,"cvss_exploit_subscore":null,"cvss_impact_subscore":null,"cvss_vector":null,"cvss_v3_exploit_subscore":null,"cvss_v3_impact_subscore":null,"cvss_v3_vector":null,"cvss_score":null,"cvss_v3_score":null},"device_count":1,"affected_assets":null},{"os_product_id":"2xxx","category":"OS","os_info":{"os_type":"WINDOWS","os_name":"Microsoft Windows 10 Enterprise","os_version":"10.0.18362","os_arch":"64-bit"},"product_info":{"vendor":null,"product":null,"version":null,"release":null,"arch":null},"vuln_info":{"cve_id":"CVE-xxxx-xxxx","cve_description":"test","risk_meter_score":1.2,"severity":"LOW","fixed_by":"KB50xxxxx","solution":null,"created_at":"2020-02-11T22:15:00Z","nvd_link":"https://nvd.nist.gov/vuln/detail/CVE-xxxx-xxxx","cvss_access_complexity":null,"cvss_access_vector":null,"cvss_authentication":null,"cvss_availability_impact":null,"cvss_confidentiality_impact":null,"cvss_integrity_impact":null,"easily_exploitable":null,"malware_exploitable":null,"active_internet_breach":null,"cvss_exploit_subscore":null,"cvss_impact_subscore":null,"cvss_vector":null,"cvss_v3_exploit_subscore":null,"cvss_v3_impact_subscore":null,"cvss_v3_vector":null,"cvss_score":null,"cvss_v3_score":null},"device_count":1,"affected_assets":null}]}},{"Entity":"test","EntityResult":{"statistics":{"total":2,"severity":{"critical":0,"important":0,"moderate":0,"low":2}},"details":[{"os_product_id":"9xx","category":"OS","os_info":{"os_type":"WINDOWS","os_name":"Microsoft Windows 10 Enterprise","os_version":"10.0.15063","os_arch":"64-bit"},"product_info":{"vendor":null,"product":null,"version":null,"release":null,"arch":null},"vuln_info":{"cve_id":"CVE-xxxx-xxxx","cve_description":"test","risk_meter_score":1,"severity":"LOW","fixed_by":"KB45xxxxx","solution":null,"created_at":"2017-06-15T01:29:00Z","nvd_link":"https://nvd.nist.gov/vuln/detail/CVE-xxxx-xxxx","cvss_access_complexity":null,"cvss_access_vector":null,"cvss_authentication":null,"cvss_availability_impact":null,"cvss_confidentiality_impact":null,"cvss_integrity_impact":null,"easily_exploitable":null,"malware_exploitable":null,"active_internet_breach":null,"cvss_exploit_subscore":null,"cvss_impact_subscore":null,"cvss_vector":null,"cvss_v3_exploit_subscore":null,"cvss_v3_impact_subscore":null,"cvss_v3_vector":null,"cvss_score":null,"cvss_v3_score":null},"device_count":1,"affected_assets":null},{"os_product_id":"9xx","category":"OS","os_info":{"os_type":"WINDOWS","os_name":"Microsoft Windows 10 Enterprise","os_version":"10.0.15063","os_arch":"64-bit"},"product_info":{"vendor":null,"product":null,"version":null,"release":null,"arch":null},"vuln_info":{"cve_id":"CVE-xxxx-xxxx","cve_description":"test","risk_meter_score":1,"severity":"LOW","fixed_by":"KB45xxxxx","solution":null,"created_at":"2017-10-13T13:29:00Z","nvd_link":"https://nvd.nist.gov/vuln/detail/CVE-xxxx-xxxx","cvss_access_complexity":null,"cvss_access_vector":null,"cvss_authentication":null,"cvss_availability_impact":null,"cvss_confidentiality_impact":null,"cvss_integrity_impact":null,"easily_exploitable":null,"malware_exploitable":null,"active_internet_breach":null,"cvss_exploit_subscore":null,"cvss_impact_subscore":null,"cvss_vector":null,"cvss_v3_exploit_subscore":null,"cvss_v3_impact_subscore":null,"cvss_v3_vector":null,"cvss_score":null,"cvss_v3_score":null},"device_count":1,"affected_assets":null}]}}]
```



#### Create a Reputation Override for IT Tool
Create a Reputation Override for the specific IT Tool based on a file name and path. Note: The file name can be provided either as a Siemplify File (artifact) or as an action input parameter. If the file name is passed to action both as an entity and input parameter - action will be executed on the input parameter. File name will be appended to the File Path parameter to get the resulting path to add to the override.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File Name|Specify a corresponding file name to add to reputation override.|False|String||
|File Path|Specify a file path where corresponding IT Tool is stored on disk to add to reputation override. Example format: C:\TMP\ |True|String||
|Description|Specify a description for the created reputation to override.|False|String||
|Reputation Override List|Specify override list to create.|True|List|Not Specified|
|Include Child Processes|If enabled, include IT Tool's child processes on approved list|False|Boolean|False|



##### JSON Results
```json
[{"Entity":"XXXX","EntityResult":{"id":"d544346dff7711eba71965XXXXXXXXXX","created_by":"XXXXXXXXXX","create_time":"20XX-XX-XXTXX:XX:XX.XXXZ","override_list":"WHITE_LIST","override_type":"IT_TOOL","description":"None","source":"APP","source_ref":"None","path":"/var/log/XXX","include_child_processes":false}}]
```



#### Unquarantine Device
Create unquarantine device task on the VMware Carbon Black Cloud server based on the Siemplify IP or Host Siemplify entities.
Timeout - 600 Seconds



#### List Reputation Overrides
List reputation overrides configured in VMware Carbon Black Cloud. Note that action is not working on Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Reputation Override List|Specify override list action should return.|False|List|Not Specified|
|Reputation Override Type|Specify override type action should return.|False|List|Not Specified|
|Start from Row|Specify from which row action should fetch data.|False|String|0|
|Max Rows to Return|Specify how many rows action should return.|False|String|50|
|Rows Sort Order|Specify sort order for the returned rows. Rows are sorted based on "create_time" value.|False|List|ASC|



##### JSON Results
```json
{"results":[{"id":"bea48f4a9d4211eb9f49a5XXXXXXXXXX","created_by":"XXXXXXXXXX","create_time":"XXXX-XX-XXTXX:XX:XX.XXXZ","override_list":"BLACK_LIST","override_type":"SHA256","description":"XXXXXXXXX","source":"APP","source_ref":"None","sha256_hash":"5ebf807272af0775f15ece08fdce4a6ddc2a08f70864bcf65bae63XXXXXXXXXX","filename":"XXXXXXXXXXXXXXX.XXX"}]}
```



#### Update a Policy for Device by Policy ID
Change a policy on VMware Carbon Black Cloud sensor on a host. The action scope is IP or Host entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Policy ID|Specify a policy to associate with the VMware Carbon Black Cloud sensor.|True|String||









## Connectors
#### VMware Carbon Black Cloud Alerts and Events Baseline Connector
Fetch Carbon Black Cloud Alerts and Events that reached specific baseline (were classified by default as Threat in Carbon Black Cloud)

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|The field name used to determine the device product|True|String|ProductName|
|EventClassId|The field name used to determine the event name (sub-type)|False|String|event_type|
|PythonProcessTimeout|The timeout limit (in seconds) for the python process running current script|True|String|180|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is ""|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is ""|False|Integer|.*|
|API Root|Vmware Carbon Black Cloud API Root URL|True|String||
|Organization Key|Vmware Carbon Black Cloud Organization Key, Eg. 7DDDD9DD|True|String||
|API ID|Vmware Carbon Black Cloud API ID (Custom API Key ID)|True|Password||
|API Secret Key|Vmware Carbon Black Cloud API Secret Key (Custom API Secret Key)|True|Password||
|Verify SSL|Verify SSL certificates for HTTPS requests to Microsoft Azure.|False|Boolean|false|
|Max Alerts Per Cycle|How many alerts should be processed during one connector run.|True|Integer|100|
|Offset Time In Hours|Number of hours before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|True|Integer|24|
|Minimum Severity to Fetch|Minimum severity of Carbon Black Cloud alert to be ingested to Siemplify, for example, 4 or 7|False|Integer||
|What Alert Field to use for Name field|What Carbon Black Cloud alert field should be used for the Siemplify Alert Name field. Possible values are: type, policy_name|True|String|type|
|What Alert Field to use for Rule Generator|What Carbon Black Cloud alert field should be used for the Siemplify Alert Rule Generator field. Possible values are: type, policy_name|True|String|type|
|Alert Reputation to Ingest|What Carbon Black Cloud alert reputation alert can have to be ingested. Parameter accepts multiple values as a comma separated string. If "N/A" is provided, connector will ingest alerts without reputation.|False|String||
|Watchlist Name Filter|If provided, for CB Cloud alerts with the type “Watchlist“ ingest only that were triggered by the respective whatchlist. Parameter accepts multiple values as a comma separated string. If nothing is specified - ingest everything regardless of watchlist name.|False|String||
|Events Limit to Ingest per Alert|Specify how many events can be ingested per single CB Cloud alert.|True|Integer|25|
|Proxy Server Address|Proxy server to use for connection.|False|IP||
|Proxy Server Username|Proxy server username|False|String||
|Proxy Server Password|Proxy server password|False|Password||
|Alerts Backlog Timer|Time frame in minutes for which connector should try to fetch again the alerts from backlog it previously failed to process.|True|Integer|60|
|Max Backlog Alerts per Cycle|How many alerts  connector should try to fetch from the backlog during one connector run.|True|Integer|10|
|Alert Name Template|If specified, connector will use this value from the CB Cloud API response for alert data for Siemplify Alert Name. You can provide placeholders in the following format: [name of the field]. Example: CBCLOUD Alert - [reason]. Note: the maximum length for the field is 256 characters. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False|String||
|Rule Generator Template|If specified, connector will use this value from the CB Cloud API response for alert data for Siemplify Rule Generator. You can provide placeholders in the following format: [name of the field]. Example: CBCLOUD - [reason]. Note: the maximum length for the field is 256 characters. If nothing is provided or user provides an invalid template, connector will use the default rule generator value.|False|String||


#### VMware Carbon Black Cloud Alerts Connector
Siemplify VMware Carbon Black Cloud Alerts Connector should be used to ingest alerts from Carbon Black Cloud (Platform) instances. Note that this connector is deprecated and not recommended to use. Consider switching to "VMware Carbon Black Cloud Alerts and Events Baseline Connector" or "VMware Carbon Black Cloud Alerts and Events Tracking Connector"

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|The field name used to determine the device product|True|String|ProductName|
|EventClassId|The field name used to determine the event name (sub-type)|False|String|type|
|PythonProcessTimeout|The timeout limit (in seconds) for the python process running current script|True|String|300|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is ""|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is ""|False|Integer|.*|
|API Root|Vmware Carbon Black Cloud API Root URL|True|String||
|Organization Key|Vmware Carbon Black Cloud Organization Key|True|String|None|
|API ID|Vmware Carbon Black Cloud API ID (Custom API Key ID)|True|Password|None|
|API Secret Key|Vmware Carbon Black Cloud API Secret Key (Custom API Secret Key)|True|Password|None|
|Verify SSL|Verify SSL certificates for HTTPS requests to Microsoft Azure.|False|Boolean|false|
|Max Alerts Per Cycle|How many alerts should be processed during one connector run.|True|Integer|10|
|Offset Time In Hours|Number of hours before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|True|Integer|24|
|Minimum Severity to Fetch|Minimum severity of Carbon Black Cloud alert to be ingested to Siemplify|False|Integer||
|What Alert Field to use for Name field|What Carbon Black Cloud alert field should be used for the Siemplify Alert Name field. Possible values are: type, policy_name|True|String|type|
|What Alert Field to use for Rule Generator|What Carbon Black Cloud alert field should be used for the Siemplify Alert Rule Generator field. Possible values are: type, policy_name|True|String|type|
|Proxy Server Address|Proxy server to use for connection.|False|IP||
|Proxy Server Username|Proxy server username|False|String||
|Proxy Server Password|Proxy server password|False|Password||


#### VMware Carbon Black Cloud Alerts and Events Tracking Connector
Fetch Carbon Black Cloud Alerts and Events as Events are added to Carbon Black Cloud Alerts. Connector can create multiple Siemplify alerts for single Carbon Black Cloud Alert, if Cloud Alert was updated with new events after initial ingestion by Siemplify.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|The field name used to determine the device product|True|String|ProductName|
|EventClassId|The field name used to determine the event name (sub-type)|False|String|event_type|
|PythonProcessTimeout|The timeout limit (in seconds) for the python process running current script|True|String|180|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is ""|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is ""|False|Integer|.*|
|API Root|Vmware Carbon Black Cloud API Root URL|True|String||
|Organization Key|Vmware Carbon Black Cloud Organization Key, Eg. 7DDDD9DD|True|String||
|API ID|Vmware Carbon Black Cloud API ID (Custom API Key ID)|True|Password||
|API Secret Key|Vmware Carbon Black Cloud API Secret Key (Custom API Secret Key)|True|Password||
|Verify SSL|Verify SSL certificates for HTTPS requests to Microsoft Azure.|False|Boolean|false|
|Max Alerts Per Cycle|How many alerts should be processed during one connector run.|True|Integer|100|
|Offset Time In Hours|Number of hours before the first connector iteration to retrieve alerts from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|True|Integer|24|
|Minimum Severity to Fetch|Minimum severity of Carbon Black Cloud alert to be ingested to Siemplify, for example, 4 or 7|False|Integer||
|What Alert Field to use for Name field|What Carbon Black Cloud alert field should be used for the Siemplify Alert Name field. Possible values are: type, policy_name|True|String|type|
|What Alert Field to use for Rule Generator|What Carbon Black Cloud alert field should be used for the Siemplify Alert Rule Generator field. Possible values are: type, policy_name|True|String|type|
|Alert Reputation to Ingest|What Carbon Black Cloud alert reputation alert can have to be ingested. Parameter accepts multiple values as a comma separated string. If "N/A" is provided, connector will ingest alerts without reputation.|False|String||
|Events Padding Period (hours)|Specify how many hours connector should track new events for already ingested alert.|True|Integer|24|
|Events Limit to Ingest per Alert|Specify how many events can be ingested per single CB Cloud alert per Connector iteration.|True|Integer|25|
|Total Limit of Events per Alert|Specify a total number of events connector should get per single CB Cloud alert. If this limit is reached, no new events will be fetched for alert. In order to not limit the total number of events, please leave this parameter empty.|False|Integer|100|
|Max Backlog Alerts per Cycle|How many alerts connector should try to fetch from the backlog during one connector run.|True|Integer|10|
|Alerts Backlog Timer|Time frame in minutes for which connector should try to fetch again the alerts from backlog it previously failed to process.|True|Integer|60|
|Proxy Server Address|Proxy server to use for connection.|False|IP||
|Proxy Server Username|Proxy server username|False|String||
|Proxy Server Password|Proxy server password|False|Password||
|Watchlist Name Filter|If provided, for CB Cloud alerts with the type “Watchlist“ ingest only that were triggered by the respective whatchlist. Parameter accepts multiple values as a comma separated string. If nothing is specified - ingest everything regardless of watchlist name.|False|String||
|Alert Name Template|If specified, connector will use this value from the CB Cloud API response for alert data for Siemplify Alert Name. You can provide placeholders in the following format: [name of the field]. Example: CBCLOUD Alert - [reason]. Note: the maximum length for the field is 256 characters. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False|String||
|Rule Generator Template|If specified, connector will use this value from the CB Cloud API response for alert data for Siemplify Rule Generator. You can provide placeholders in the following format: [name of the field]. Example: CBCLOUD - [reason]. Note: the maximum length for the field is 256 characters. If nothing is provided or user provides an invalid template, connector will use the default rule generator value.|False|String||




