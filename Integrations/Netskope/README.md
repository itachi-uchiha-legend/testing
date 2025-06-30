<p align="center"><img src="./Resources/Netskope.svg" 
     alt="Netskope" width="200"/></p>

# Netskope

The Netskope Security Cloud helps the world’s largest organizations take full advantage of the cloud and web without sacrificing security.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root|None|True|String|https://{IP}|
|V1 Api Key|None|False|Password|None|
|V2 Api Key|None|False|Password|None|
|Verify SSL|None|False|Boolean|False|


#### Dependencies
| |
|-|
|certifi-2024.7.4-py3-none-any.whl|
|TIPCommon-1.0.10-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|idna-3.7-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|


## Actions
#### Download File
Download a quarantined file.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File ID|ID of a file, needed to identify a file.|True|String||
|Quarantine Profile ID|ID of a quarantine profile.|True|String||



#### Block File
Block a quarantined file.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File ID|ID of a file, needed to identify a file.|True|String||
|Quarantine Profile ID|ID of a quarantine profile.|True|String||



#### Ping
Test connectivity to Netskope.
Timeout - 600 Seconds



#### List Events
List events.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query|This acts as a filter for all the cloud app events in the events database.|False|String||
|Type|The type of the alert to filter by. Valid values: page | application | audit | infrastructure.|False|String||
|Time Period|Time period to search events at (milliseconds backwards). Valid Values: 3600 | 86400 | 604800 | 2592000.|False|String||
|Start Time|Restrict events to those that have timestamps greater than this (unixtime). Needed only if time period is not passed.|False|String||
|End Time|Restrict events to those that have timestamps less than this (unixtime). Needed only if time period is not passed.|False|String||
|Limit|Number of results to return. Default: 100.|False|String||



##### JSON Results
```json
[{"_category_id": "26", "_correlation_id": "6f96c5f3-3a05-4672-b5a5-40e871d966d8", "_creation_timestamp": 1739864350, "_ctg": ["26"], "_ef_received_at": 1739864349181, "_enriched_all": true, "_event_id": "9134ffd9-4ef1-4818-8c3b-1c592ee92a5a", "_forwarded_by": "msg-relayer", "_gef_src_dp": "US-SEA2", "_id": "b409336bf27717234f0e7df6", "_ingress_client_bytes": 10991, "_ingress_server_bytes": 50257, "_insertion_epoch_timestamp": 1739864352, "_nshostname": "dppool2-1-egress", "_raw_event_inserted_at": 1739864349508, "_service_identifier": "service-nsproxy", "_skip_geoip_lookup": "yes", "_src_epoch_now": 1739835368, "_src_gmt_offset": -28800, "access_method": "Client", "app": "Trend Micro Password Manager", "app_session_id": 6346025849381417210, "app_tags": ["Consumer"], "appcategory": "Security", "browser": "Chrome", "browser_session_id": 1876923647347754427, "browser_version": "132.0.0.0", "bypass_traffic": "no", "category": "Security", "cci": 65, "ccl": "medium", "client_bytes": 24464, "conn_duration": 30, "conn_endtime": 1739864273, "conn_starttime": 1739864243, "connection_id": 6368931229498758542, "count": 1, "device": "Windows Device", "domain": "docs.trendmicro.com", "dst_country": "US", "dst_latitude": 45.526, "dst_location": "Hillsboro", "dst_longitude": -122.9874, "dst_region": "Oregon", "dst_timezone": "America/Los_Angeles", "dst_zipcode": "97129", "dstip": "23.75.209.85", "dstport": 443, "hostname": "instance-ngcc1", "http_transaction_count": 15, "netskope_pop": "US-SEA2", "numbytes": 157866, "organization_unit": "", "os": "Windows Server 2016", "os_family": "Windows Server", "os_version": "Windows Server 10.0", "other_categories": ["Security"], "page": "docs.trendmicro.com/all/ent/de/v1.5/en-us/de_1.5_olh/ctm_ag/ctm1_ag_ch8/t_test_eicar_file.htm", "protocol": "HTTP/1.1", "req_cnt": 15, "resp_cnt": 15, "resp_content_len": 10731, "resp_content_type": "text/html", "server_bytes": 133402, "severity": "unknown", "site": "Trend Micro Password Manager", "src_country": "US", "src_latitude": 45.5999, "src_location": "The Dalles", "src_longitude": -121.1871, "src_region": "Oregon", "src_time": "Mon Feb 17 23:36:08 2025", "src_timezone": "America/Los_Angeles", "src_zipcode": "97058", "srcip": "34.82.190.203", "timestamp": 1739864243, "traffic_type": "CloudApp", "type": "connection", "ur_normalized": "dl-ngcc-engg@exabeamengineering2.onmicrosoft.com", "url": "docs.trendmicro.com/all/ent/de/v1.5/en-us/de_1.5_olh/ctm_ag/ctm1_ag_ch8/t_test_eicar_file.htm", "user": "DL-NGCC-ENGG@exabeamengineering2.onmicrosoft.com", "user_generated": "yes", "useragent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36", "userip": "10.70.0.19", "userkey": "DL-NGCC-ENGG@exabeamengineering2.onmicrosoft.com"}]
```



#### List Clients
List clients.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query|This acts as a filter on all the entries in the database.|False|String||
|Limit|Number of results to return. Default: 25.|False|String||



##### JSON Results
```json
[{"client_install_time": 1532040251, "users": [{"heartbeat_status_since": 1532040385, "user_added_time": 1532040167, "last_event": {"status": "Enabled", "timestamp": 1548578307, "event": "Tunnel Up", "actor": "System"}, "device_classification_status": "Not Configured", "username": "john_doe@example.com", "user_source": "Manual", "userkey": "00000", "_id": "00000", "heartbeat_status": "Active"}], "last_event": {"status": "Enabled", "timestamp": 1548578307, "event": "Tunnel Up", "actor": "System"}, "host_info": {"device_model": "VMware Virtual Platform", "os": "Windows", "hostname": "host000", "device_make": "VMware, Inc.", "os_version": "10.0"}, "client_version": "1.1.1.1", "_id": "device000", "device_id": "device000"}]
```



#### List Alerts
List alerts.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Query|This acts as a filter for all the cloud app events in the alerts database.|False|String||
|Type|The type of the alert to filter by. Valid values: anomaly | 'Compromised Credential' | policy | 'Legal Hold' | malsite | Malware | DLP | watchlist | quarantine | Remediation.|False|String||
|Time Period|Time period to search alerts at (milliseconds backwards). Valid Values: 3600 | 86400 | 604800 | 2592000.|False|String||
|Start Time|Restrict alerts to those that have timestamps greater than this (unixtime). Needed only if time period is not passed.|False|String||
|End Time|Restrict alerts to those that have timestamps less than this (unixtime). Needed only if time period is not passed.|False|String||
|Is Acknowledged|Whether to get only acknowledged alerts.|False|Boolean||
|Limit|Number of results to return. Default: 100.|False|String||



##### JSON Results
```json
[{"_correlation_id": "4618d275-542f-4dc3-8c42-d939e3791e4f", "_creation_timestamp": 1739856958, "_ef_received_at": 1739856954869, "_enriched": true, "_enriched_all": true, "_event_id": "e3510e5b-2c4f-44f6-aabe-2d0b854db038", "_forwarded_by": "msg-relayer", "_gef_src_dp": "US-SEA2", "_id": "c97712537738b9583a9e133c", "_insertion_epoch_timestamp": 1739856963, "_raw_event_inserted_at": 1739856955181, "_service_identifier": "service-npa", "_skip_geoip_lookup": "yes", "access_method": "Client", "acked": "false", "action": "block", "alert": "yes", "alert_name": "eicar", "alert_type": "policy", "app": "[eicar]", "appcategory": "n/a", "category": "n/a", "cci": 0, "ccl": "unknown", "client_bytes": 0, "client_packets": 0, "count": 1, "custom_classification_id": -2, "device": "Windows", "device_classification_status": "unmanaged", "dsthost": "secure.eicar.org", "dstip": "", "dstport": 443, "end_time": "2025-02-18T05:33:57+00:00", "hostname": "instance-ngcc1", "ip_protocol": "TCP", "netskope_device_id": "8251E21F-2223-73F5-D308-70FF560EE4C2", "netskope_pop": "US-SEA2", "network_session_id": "10311492756218252835", "num_sessions": 1, "numbytes": 0, "organization_unit": "", "os": "Windows", "os_version": "10.0(1607)", "other_categories": [], "policy": "eicar", "protocol": "Http", "protocol_port": "TCP:443", "publisher_cn": "", "publisher_name": "", "reason": "Dropped connection based on policy", "server_bytes": 0, "server_packets": 0, "session_duration": 0, "site": "secure.eicar.org", "srcip": "", "srcport": 20017, "start_time": "2025-02-18T05:33:54+00:00", "timestamp": 1739856954, "total_packets": 0, "traffic_type": "PrivateApp", "tunnel_id": "24173", "tunnel_type": "NPA", "tunnel_up_time": 0, "type": "network", "ur_normalized": "dl-ngcc-engg@exabeamengineering2.onmicrosoft.com", "user": "dl-ngcc-engg@exabeamengineering2.onmicrosoft.com", "userip": "", "userkey": "dl-ngcc-engg@exabeamengineering2.onmicrosoft.com"}]
```



#### List Quarantined Files
List quarantined files.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Start Time|Restrict events to those that have timestamps greater than this (unixtime). Needed only if time period is not passed.|False|String||
|End Time|Restrict events to those that have timestamps less than this (unixtime). Needed only if time period is not passed.|False|String||



##### JSON Results
```json
{}
```



#### Allow File
Allow a quarantined file.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File ID|ID of a file, needed to identify a file.|True|String||
|Quarantine Profile ID|ID of a quarantine profile.|True|String||









