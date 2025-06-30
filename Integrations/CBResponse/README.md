<p align="center"><img src="./Resources/CBResponse.svg" 
     alt="CBResponse" width="200"/></p>

# CBResponse

Highly scalable, real-time EDR with unparalleled visibility for top security operations centers and incident response teams

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root|None|True|None|https://x.x.x.x|
|Api Key|None|True|Password|None|
|Version|None|True|String|6.3|
|CA Certificate File|CA certificate file to use with the verify_ssl option. Certificate file should be specified as a Base64-encoded string.|False|String||
|Verify SSL|None|False|Boolean|false|


#### Dependencies
| |
|-|
|requests-2.31.0-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|EnvironmentCommon-1.0.0-py3-none-any.whl|
|TIPCommon-1.0.11-py2.py3-none-any.whl|
|arrow-1.3.0-py3-none-any.whl|
|idna-3.7-py3-none-any.whl|
|zipp-3.18.1-py3-none-any.whl|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|six-1.16.0-py2.py3-none-any.whl|
|types_python_dateutil-2.9.0.20240316-py3-none-any.whl|
|certifi-2024.2.2-py3-none-any.whl|
|urllib3-2.2.1-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|


## Actions
#### Binary Free Query
List binaries by free query
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query|e.g. md5:* AND original_filename:<file-name>|True|String||



##### JSON Results
```json
[{"host_count": 3, "digsig_result": "Signed", "observed_filename": ["c:\\temp\\test.exe"], "product_version": "10.0.17134.1", "digsig_issuer": "Microsoft Windows Production PCA 2011", "legal_copyright": "\\u00a9 Microsoft Corporation. All rights reserved.", "digsig_sign_time": "2018-04-11T19:19:00Z", "orig_mod_len": 20888, "is_executable_image": true, "is_64bit": true, "digsig_subject": "Microsoft Windows", "digsig_publisher": "Microsoft Corporation", "group": ["Default Group"], "file_version": "10.0.17134.1 (WinBuild.160101.0800)", "company_name": "Microsoft Corporation", "internal_name": "test.exe", "product_name": "Microsoft\\u00ae Windows\\u00ae Operating System", "digsig_result_code": "0", "timestamp": "2018-12-30T03:55:55.376Z", "copied_mod_len": 20888, "server_added_timestamp": "2018-12-30T03:55:55.376Z", "digsig_prog_name": "Microsoft Windows", "md5": "098f6bcd4621d373cade4e832627b4f6", "endpoint": ["TEST1|15", "TEST2|16", "TEST3|17", "TEST4|18"], "watchlists": [{"wid": "3", "value": "2018-12-30T04:00:03.635Z"}], "signed": "Signed", "original_filename": "test.exe", "cb_version": 520, "os_type": "Windows", "file_desc": "COM Surrogate", "last_seen": "2019-02-21T15:27:33.231Z"}]
```



#### Block Hash
Block a hash
Timeout - 600 Seconds



#### Create Watchlist
Create a watchlist for processes (type = events) or for binaries (type = modules)
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Watchlist Name|Name of this watchlist|True|String|None|
|Query|The raw Carbon Black query that this watchlist matches|True|String|None|
|Watchlist Type|The type of watchlist. e.g. modules|True|String||



#### Download Binary
Download a binary
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": "TVqQAAMAAAAEAAAA//8AALgAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAA4fug4AtAnNIb", "Entity": "82A2C91219F140BB2A4FE34A7390B6C7"}]
```



#### Enrich Binary
Enrich hash with binary info from CB Response.
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": {"host_count": 1, "digsig_result": "Unsigned", "observed_filename": ["c:\\\\TEST_source\\\\main\\\\client\\\\wpf\\\\TEST.client\\\\bin\\\\release\\\\TEST.client.exe"], "product_version": "1.1.1.1", "legal_copyright": "TEST", "orig_mod_len": 4108800, "is_executable_image": "True", "is_64bit": "False", "group": ["Default Group"], "file_version": "1.1.1.1", "comments": "Flavor=Release", "company_name": "TEST", "internal_name": "TEST.Client.exe", "icon": "iVBORw0KGgoAAAANSUhEUg", "product_name": "(unknown)", "digsig_result_code": "2148204800", "timestamp": "2016-12-11T18:54:03.352Z", "copied_mod_len": 4108800, "server_added_timestamp": "2016-12-11T18:54:03.352Z", "md5": "098f6bcd4621d373cade4e832627b4f6", "endpoint": ["TEST|4"], "watchlists": [{"wid": "3", "value": "2016-12-11T19:00:03.232Z"}], "signed": "Unsigned", "original_filename": "TEST.Client.exe", "cb_version": 520, "os_type": "Windows", "file_desc": " ", "last_seen": "2016-12-11T19:00:04.178Z"}, "Entity": "098f6bcd4621d373cade4e832627b4f6"}]
```



#### Enrich Process
Enrich process entity with data from CB Response
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": [{"modload_count": 28, "sensor_id": 14, "filtering_known_dlls": "False", "process_md5": "098f6bcd4621d373cade4e832627b4f6", "parent_unique_id": "0000000e-0000-13d4-01d4-a04566d108ba-00000001", "emet_count": 0, "cmdline": "\\\\??\\\\C:\\\\Windows\\\\system32\\\\conhost.exe 0xffffffff -ForceV1", "last_update": "2018-12-30T13:41:43.904Z", "id": "0000000e-0000-1310-01d4-a04566d29849", "parent_name": "python.exe", "parent_md5": "000000000000000000000000000000", "group": "Default Group", "hostname": "TEST", "filemod_count": 0, "start": "2018-12-30T13:41:43.885Z", "emet_config": "", "netconn_count": 0, "interface_ip": 167772456, "process_pid": 4880, "username": "TEST\\\\Admin", "terminated": "True", "process_name": "conhost.exe", "comms_ip": 167772456, "path": "c:\\\\windows\\\\system32\\\\conhost.exe", "regmod_count": 0, "parent_pid": 5076, "crossproc_count": 1, "current_segment": 0, "segment_id": 1, "host_type": "server", "processblock_count": 0, "os_type": "windows", "childproc_count": 0, "unique_id": "0000000e-0000-1310-01d4-a04566d29849-00000001"}], "Entity": "process.exe"}]
```



#### Get FileMod Data For Process
Get filemod data for a process by its id
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Process ID|process unique id|True|String||
|Segment Id|e.g. 1|True|String||



##### JSON Results
```json
{"process": {"process_md5": "098f6bcd4621d373cade4e832627b4f6", "sensor_id": 2, "group": "Default Group", "segment_id": 1, "process_name": "taskhost.exe", "start": "2013-09-19T22:07:07Z", "regmod_complete": ["2|2013-09-19 22:07:07.000000|\\\\registry\\\\user\\\\s-1-5-19\\\\software\\\\microsoft\\\\sqmclient\\\\reliability\\\\adaptivesqm\\\\manifestinfo\\\\version", "2|2013-09-19 22:09:07.000000|\\\\registry\\\\machine\\\\software\\\\microsoft\\\\reliability analysis\\\\rac\\\\wmilasttime"], "cmdline": "taskhost.exe $(arg0)", "filemod_complete": ["2|2013-09-19 22:07:07.000000|c:\\\\programdata\\\\microsoft\\\\rac\\\\statedata\\\\racmetadata.dat|", "2|2013-09-19 22:07:07.000000|c:\\\\programdata\\\\microsoft\\\\rac\\\\temp\\\\sql4475.tmp|"], "parent_id": "5856845119039539348", "modload_complete": ["2013-09-19 22:07:07.000000|517110bd83835338c037269e603db55d|c:\\\\windows\\\\system32\\\\taskhost.exe", "2013-09-19 22:07:07.000000|3556d5a8bf2cc508bdab51dec38d7c61|c:\\\\windows\\\\system32\\\\ntdll.dll"], "id": "2032659773721368929", "path": "c:\\\\windows\\\\system32\\\\taskhost.exe", "os_type": "windows", "last_update": "2013-09-19T22:09:07Z", "hostname": "TEST"}, "elapsed": 0.0126001834869}
```



#### Get License
Get the current license from CB Response
Timeout - 600 Seconds



#### Get Process Tree Data
Get process tree data for process by id (JSON)
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Process ID|process unique id|True|String||
|Segment Id|e.g. 1|True|String||



##### JSON Results
```json
{"process": {"process_md5": "098f6bcd4621d373cade4e832627b4f6", "sensor_id": 2, "group": "Default Group", "segment_id": 1, "process_name": "taskhost.exe", "last_update": "2013-09-19T22:09:07Z", "cmdline": "taskhost.exe $(arg0)", "start": "2013-09-19T22:07:07Z", "parent_id": "5856845119039539348", "id": "2032659773721368929", "path": "c:\\\\windows\\\\system32\\\\taskhost.exe", "os_type": "windows", "hostname": "TEST"}, "siblings": [{"process_md5": "098f6bcd4621d373cade4e832627b4f6", "sensor_id": 2, "group": "Default Group", "segment_id": 1, "process_name": "svchost.exe", "last_update": "2013-09-19T22:34:49Z", "start": "2013-09-10T04:10:07Z", "parent_id": "5856845119039539348", "id": "5286285292765095481", "path": "c:\\\\windows\\\\system32\\\\svchost.exe", "os_type": "windows", "hostname": "TEST"}], "children": [], "parent": {"process_md5": "098f6bcd4621d373cade4e832627b4f6", "sensor_id": 2, "group": "Default Group", "segment_id": 1, "process_name": "services.exe", "last_update": "2013-09-19T22:09:07Z", "start": "2013-09-10T04:09:51Z", "parent_id": "4245649408199694328", "id": "5856845119039539348", "path": "c:\\\\windows\\\\system32\\\\services.exe", "os_type": "windows", "hostname": "TEST"}}
```



#### Get System Info
Get  system information for a sensor from CB Response and enrich  entity
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": {"systemvolume_total_size": "479127379968", "computer_name": "TEST", "os_environment_display_string": "Windows 10 Professional, 64-bit", "systemvolume_free_size": "319940304896", "physical_memory_size": "17058787328", "emet_version": "", "emet_dump_flags": "", "clock_delta": "10840", "supports_cblr": "True", "id": 11, "is_isolating": "False", "emet_process_count": 0, "build_id": 2, "uptime": "1640459", "computer_dns_name": "TEST.COMPANY.LOCAL", "emet_report_setting": " (Locally configured)", "last_update": "2018-06-25 13:27:47.442521+03:00", "parity_host_id": "0", "power_state": 0, "network_isolation_enabled": "False", "uninstalled": "None", "next_checkin_time": "2018-06-25 13:28:13.089904+03:00", "status": "Offline", "num_eventlog_bytes": "13771", "sensor_health_message": "Elevated memory usage", "build_version_string": "1.1.1.1", "computer_sid": "S-1-5-21-2809203804-286580391-3190870472", "node_id": 0, "event_log_flush_time": "None", "emet_exploit_action": " (Locally configured)", "emet_telemetry_path": "", "license_expiration": "1990-01-01 00:00:00+02:00", "supports_isolation": "True", "emet_is_gpo": "False", "supports_2nd_gen_modloads": "False", "network_adapters": "1.1.1.1,d4258bf480fd|", "sensor_health_status": 90, "registration_time": "2018-03-01 08:12:47.420579+02:00", "restart_queued": "False", "notes": "None", "num_storefiles_bytes": "0", "os_environment_id": 5, "cookie": 292474955, "shard_id": 0, "boot_id": "20", "last_checkin_time": "2018-06-25 13:27:43.091387+03:00", "os_type": 1, "group_id": 1, "display": "True", "sensor_uptime": "3", "uninstall": "False"}, "Entity": "TEST"}]
```



#### Hosts By Process
Get hosts that are related to a particular process
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": [{"systemvolume_total_size": "160534884352", "computer_name": "COMPUTER", "os_environment_display_string": "Windows 10 Server Server Standard (Evaluation), 64-bit", "systemvolume_free_size": "120903110656", "physical_memory_size": "8589463552", "emet_version": "", "emet_dump_flags": "", "clock_delta": "7348", "supports_cblr": "True", "id": 14, "is_isolating": "False", "emet_process_count": 0, "build_id": 2, "uptime": "5888902", "computer_dns_name": "COMPUTER", "emet_report_setting": " (Locally configured)", "last_update": "2019-01-07 11:07:17.187979+02:00", "parity_host_id": "0", "power_state": 0, "network_isolation_enabled": "False", "uninstalled": "None", "next_checkin_time": "2019-01-07 11:07:44.348203+02:00", "status": "Offline", "num_eventlog_bytes": "34800", "sensor_health_message": "Healthy", "build_version_string": "1.1.1.1", "computer_sid": "S-1-5-21-405201704-2854221227-856099807", "node_id": 0, "event_log_flush_time": "None", "emet_exploit_action": " (Locally configured)", "emet_telemetry_path": "", "license_expiration": "1990-01-01 00:00:00+02:00", "supports_isolation": "True", "emet_is_gpo": "False", "supports_2nd_gen_modloads": "False", "network_adapters": "1.1.1.1,005056111111|", "sensor_health_status": 100, "registration_time": "2018-12-22 02:46:33.629175+02:00", "restart_queued": "False", "notes": "None", "num_storefiles_bytes": "0", "os_environment_id": 8, "cookie": 1164577502, "shard_id": 0, "boot_id": "1", "last_checkin_time": "2019-01-07 11:07:14.349477+02:00", "os_type": 1, "group_id": 1, "display": "True", "sensor_uptime": "1412441", "uninstall": "False"}], "Entity": "python.exe"}]
```



#### Isolate Host
Isolate an endpoint from the network
Timeout - 600 Seconds



#### Kill Process
Kill a process on a particular host
Timeout - 600 Seconds



#### List Processes
List processes that are related to given entities
Timeout - 600 Seconds



##### JSON Results
```json
[{"EntityResult": [{"modload_count": 63, "sensor_id": 14, "filtering_known_dlls": "False", "process_md5": "00eb8baca58a0dd0106d67db566d6ea4", "parent_unique_id": "0000000e-0000-1038-01d4-86754f9f6962-00000001", "emet_count": 0, "cmdline": "python.exe C:\\\\HOST_Server\\\\z31fmfzn.vzo.py", "last_update": "2018-12-30T13:39:55.642Z", "id": "0000000e-0000-1788-01d4-a04519d6ceaf", "parent_name": "HOST.server.pythonexecution.windowsservice.exe", "parent_md5": "000000000000000000000000000000", "group": "Default Group", "hostname": "HOST", "filemod_count": 7, "start": "2018-12-30T13:39:34.728Z", "emet_config": "", "netconn_count": 2, "interface_ip": 167772456, "process_pid": 6024, "username": "HOST\\\\Admin", "terminated": "True", "process_name": "python.exe", "comms_ip": 167772456, "path": "c:\\\\python27\\\\python.exe", "regmod_count": 0, "parent_pid": 4152, "crossproc_count": 1, "current_segment": 0, "segment_id": 1, "host_type": "server", "processblock_count": 0, "os_type": "windows", "childproc_count": 1, "unique_id": "0000000e-0000-1788-01d4-a04519d6ceaf-00000001"}], "Entity": "HOST"}]
```



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Process Free Query
List processes by free query
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query|e.g. process_name:python.exe|True|String||



##### JSON Results
```json
[{"process_md5": "00eb8baca58a0dd0106d67db566d6ea4", "sensor_id": 14, "filtering_known_dlls": "False", "modload_count": 63, "parent_unique_id": "0000000e-0000-1038-01d4-86754f9f6962-00000001", "emet_count": 0, "group": "Default Group", "cmdline": "python.exe C:\\\\bin\\\\\\\\z31fmfzn.vzo.py", "last_update": "2018-12-30T13:39:55.642Z", "id": "0000000e-0000-1788-01d4-a04519d6ceaf", "parent_name": "HOST.server.pythonexecution.windowsservice.exe", "parent_md5": "000000000000000000000000000000", "parent_pid": 4152, "hostname": "HOST", "filemod_count": 7, "start": "2018-12-30T13:39:34.728Z", "emet_config": "", "netconn_count": 2, "interface_ip": 167772456, "process_pid": 6024, "username": "HOST\\\\Admin", "terminated": "True", "process_name": "python.exe", "comms_ip": 167772456, "path": "c:\\\\python27\\\\python.exe", "regmod_count": 0, "crossproc_count": 1, "current_segment": 0, "segment_id": 1, "host_type": "server", "processblock_count": 0, "os_type": "windows", "childproc_count": 1, "unique_id": "0000000e-0000-1788-01d4-a04519d6ceaf-00000001"}]
```



#### Resolve Alert
Resolve an alert. Note: Carbon Black Response REST-API returns a successful answer even if the alert that you tried to resolve doesn’t exist.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert ID|The id of the alert to resolve|True|String||



#### Unblock Hash
Unblock a hash
Timeout - 600 Seconds



#### Unisolate Host
Rejoin an endpoint to the network
Timeout - 600 Seconds









## Connectors
#### Carbon Black Response Connector


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|The field name used to determine the device product|True|String|device_product|
|EventClassId|The field name used to determine the event name (sub-type)|False|String|name|
|PythonProcessTimeout|The timeout limit (in seconds) for the python process running current script|True|String|60|
|Api Root|https://x.x.x.x|True|String|None|
|Api Key||True|Password|None|
|Version|CB server version, default 6.3 will be used|True|String|6.3|
|Alerts Count Limit|Limit the number of alerts in every cycle. e.g. 20.|True|Integer|20|
|Max Days Backwards|Number of days before the first connector iteration to retrieve incidents from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|True|Integer|3|
|Environment Field Name|The name of the environment's field.|False|String|None|
|List Type|Can be whitelist or blacklist.|False|String|None|
|List Operator|Can be 'exact', 'start with', 'ends with' or 'contains'.|False|String|None|
|List Fields|List of fields, comma separated.|False|String|None|
|CA Certificate File|CA certificate file to use with the verify_ssl option. Certificate file should be specified as a Base64-encoded string.|False|String||
|Verify SSL|Whether to verify ssl certificate on connection or not|False|Boolean|false|
|Proxy Server Address|The address of the proxy server to use.|False|String|None|
|Proxy Username|The proxy username to authenticate with.|False|String|None|
|Proxy Password|The proxy password to authenticate with.|False|Password|None|




