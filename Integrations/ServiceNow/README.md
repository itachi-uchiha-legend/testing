<p align="center"><img src="./Resources/ServiceNow.svg" 
     alt="ServiceNow" width="200"/></p>

# ServiceNow

An incident ticketing integration exchanges ticket data between your ServiceNow instance and Google SecOps system.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root|API root of the ServiceNow instance.|True|String|https://{dev-instance}.service-now.com/api/now/v1/|
|Username|Username of the ServiceNow account. Note: "Username" and "Password" need to be provided together to authenticate to API via "password" flow.|False|String||
|Password|Password of the ServiceNow account. Note: "Username" and "Password" need to be provided together to authenticate to API via "password" flow.|False|Password|None|
|Incident Table|Default table that should be used across actions that work with incidents.|False|String|incident|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the ServiceNow server is valid.|False|Boolean|true|
|Client ID|Client ID of the ServiceNow account. Note: "Client ID" and "Client Secret" need to be provided together to authenticate to API via "client_credentials" flow. If "Refresh Token" is provided, then integration will use "refresh_token" flow.|False|String||
|Client Secret|Client Secret of the ServiceNow account. Note: "Client ID" and "Client Secret" need to be provided together to authenticate to API via "client_credentials" flow. If "Refresh Token" is provided, then integration will use "refresh_token" flow.|False|Password|None|
|Refresh Token|Refresh Token for the "refresh_token" flow. Note: "Client ID" and "Client Secret" need to be provided.|False|Password|None|
|Use Oauth Authentication|If enabled, integration will try to use "client_credentials" or "refresh_token" flow.|False|Boolean|false|



## Actions
#### Wait For Field Update

Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Table Name|Specify what table should be used to create a record. |True|String|None|
|Record Sys ID|Specify Sys ID of the needed record.|True|String|None|
|Field - Column name|Specify name of the column that is expected to be updated.|True|String|None|
|Field - Values|Specify values that are expected in the column. Example: In Progress,Resolved.|True|String|None|



##### JSON Results
```json
{"parent": "", "made_sla": "true", "caused_by": "", "watch_list": "", "upon_reject": "cancel", "sys_updated_on": "2020-11-22 17:40:35", "child_incidents": "0", "hold_reason": "", "approval_history": "", "skills": "", "number": "INC0010xxx", "resolved_by": "", "sys_updated_by": "Admin", "opened_by": {"link": "https://dev98xxx.service-now.com/api/now/v1/table/sys_user/6816f79cc0a8016401c5a33bxxxxxx", "value": "6816f79cc0a8016401c5a33bxxxxxx"}, "user_input": "", "sys_created_on": "2020-11-22 17:40:35", "sys_domain": {"link": "https://dev98xxx.service-now.com/api/now/v1/table/sys_user_group/global", "value": "global"}, "state": "1", "sys_created_by": "Admin", "knowledge": "false", "order": "", "calendar_stc": "", "closed_at": "", "cmdb_ci": "", "delivery_plan": "", "contract": "", "impact": "2", "active": "true", "work_notes_list": "", "business_service": "", "priority": "2", "sys_domain_path": "/", "rfc": "", "time_worked": "", "expected_start": "", "opened_at": "2020-11-22 17:40:35", "business_duration": "", "group_list": "", "work_end": "", "caller_id": {"link": "https://dev98xxx.service-now.com/api/now/v1/table/sys_user/6816f79cc0a8016401c5a33bxxxxx", "value": "6816f79cc0a8016401c5a33bxxxxx"}, "reopened_time": "", "resolved_at": "", "approval_set": "", "subcategory": "", "work_notes": "", "short_description": "short description", "close_code": "", "correlation_display": "", "delivery_task": "", "work_start": "", "assignment_group": "", "additional_assignee_list": "", "business_stc": "", "description": "", "calendar_duration": "", "close_notes": "", "notify": "1", "service_offering": "", "sys_class_name": "incident", "closed_by": "", "follow_up": "", "parent_incident": "", "sys_id": "aada0a4f2f6c2010c518532xxxxx", "contact_type": "", "reopened_by": "", "incident_state": "1", "urgency": "1", "problem_id": "", "company": "", "reassignment_count": "0", "activity_due": "", "assigned_to": "", "severity": "3", "comments": "", "approval": "not requested", "sla_due": "", "comments_and_work_notes": "", "due_date": "", "sys_mod_count": "0", "reopen_count": "0", "sys_tags": "", "escalation": "0", "upon_approval": "proceed", "correlation_id": "", "location": "", "category": "inquiry"}
```



#### Create Incident
Create a new incident in the ServiceNow system
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Short Description|Specify short description of the incident.|True|String||
|Impact|Specify impact of the incident. Possible values: 1 for High, 2 for Medium and 3 for Low.|True|String|1|
|Urgency|Specify urgency of the incident. Possible values: 1 for High, 2 for Medium and 3 for Low.|True|String|1|
|Category|Specify category of the incident.|False|String|network|
|Assignment group ID|Specify full name of the group that was assigned to the incident.|False|String||
|Assigned User ID|Specify full name or the username of the user that was assigned to the incident.|False|String||
|Description|Specify description of the incident.|False|Content||
|Custom Fields|Specify a comma-separated list of fields and values. Format: field_1:value_1,field_2:value_2. You can also specify a JSON object as input. Note: this parameter has priority and all of the fields will be overwritten with the value that is provided for this parameter. Example: {"field":"value"}|False|String||



##### JSON Results
```json
{"sys_tags": "", "user_input": "", "calendar_stc": "", "subcategory": "", "watch_list": "", "follow_up": "", "made_sla": "true", "sys_created_by": "admin", "sla_due": "", "number": "INC0010010", "group_list": "", "reassignment_count": "0", "assigned_to": "", "sys_mod_count": "0", "notify": "1", "resolved_by": "", "upon_reject": "cancel", "additional_assignee_list": "", "category": "inquiry", "closed_at": "", "parent_incident": "", "cmdb_ci": "", "contact_type": "", "impact": "3", "rfc": "", "expected_start": "", "knowledge": "false", "sys_updated_by": "admin", "caused_by": "", "comments": "", "closed_by": "", "priority": "3", "state": "1", "sys_id": "200f90ef2f311010f170c886f699b646", "opened_at": "2020-07-10 06:13:43", "child_incidents": "0", "work_notes": "", "delivery_task": "", "short_description": "test", "comments_and_work_notes": "", "time_worked": "", "upon_approval": "proceed", "company": "", "business_stc": "", "correlation_display": "", "sys_class_name": "incident", "delivery_plan": "", "escalation": "0", "description": "", "parent": "", "close_notes": "", "business_duration": "", "problem_id": "", "sys_updated_on": "2020-07-10 06:13:43", "approval_history": "", "approval_set": "", "business_service": "", "reopened_by": "", "calendar_duration": "", "caller_id": {"link": "https://dev92294.service-now.com/api/now/v1/table/sys_user/6816f79cc0a8016401c5a33be04be441", "value": "6816f79cc0a8016401c5a33be04be441"}, "active": "true", "approval": "not requested", "service_offering": "", "sys_domain_path": "/", "hold_reason": "", "activity_due": "", "severity": "3", "incident_state": "1", "resolved_at": "", "location": "", "due_date": "", "work_start": "", "work_end": "", "work_notes_list": "", "sys_created_on": "2020-07-10 06:13:43", "correlation_id": "", "contract": "", "reopened_time": "", "opened_by": {"link": "https://dev92294.service-now.com/api/now/v1/table/sys_user/6816f79cc0a8016401c5a33be04be441", "value": "6816f79cc0a8016401c5a33be04be441"}, "close_code": "", "assignment_group": "", "sys_domain": {"link": "https://dev92294.service-now.com/api/now/v1/table/sys_user_group/global", "value": "global"}, "order": "", "urgency": "1", "reopen_count": "0"}
```



#### Add Attachment
Add attachment to a table record in ServiceNow.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Table Name|Specify name of the table, where is located the record to which you want to add attachment.|True|String||
|Record Sys ID|Specify sys id of the record to which you want to add attachment.  |True|String||
|File Path|Specify a comma-separated list of absolute paths to the files that need to be attached.|True|String||
|Mode|Specify the mode for the action. If “Add New Attachment” is selected, action will add a new attachment, if it even has the same name. If “Overwrite Existing Attachment” is selected, action will remove other attachments with the same name and add a new attachment.|False|List|Add New Attachment|



##### JSON Results
```json
[{"result": {"sys_tags": "", "sys_updated_by": "admin", "hash": "c9d04c9565fc665c80681fb1d829938026871f66e14f501e08531df66938axxx", "content_type": "multipart/form-data", "chunk_size_bytes": "700000", "file_name": "Example.txt", "sys_updated_on": "2020-09-02 05:55:32", "sys_created_on": "2020-09-02 05:55:32", "image_width": "", "image_height": "", "state": "pending", "sys_mod_count": "0", "table_name": "sys_product_help", "sys_id": "30b0ea302f031010c518532a2799bxxx", "download_link": "https://devXXXX.service-now.com/api/now/attachment/30b0ea302f031010c518532a2799bxxx/file", "average_image_color": "", "size_bytes": "5", "table_sys_id": "003a3ef24ff1120031577d2ca310cxxx", "size_compressed": "25", "sys_created_by": "admin", "compressed": "true"}}]
```



#### Get CMDB Record Details
Get detailed CMDB records from the same class in ServiceNow.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Class Name|Specify name of the class, from where you want to list records. Example: cmdb_ci_appl.|True|String||
|Sys ID|Specify a comma-separated list of record sys ids for which you want to retrieve details.|True|String||
|Max Records To Return|Specify how many record relations per type to return.|False|String|50|



##### JSON Results
```json
[{"result": {"inbound_relations": [{"sys_id": "3b3d95297f701200bee45f19befa9xxx", "type": {"link": "https://devXXX.service-now.com/api/now/table/cmdb_rel_type/1a9cb166f1571100a92eb60da2bcexxx", "display_value": "Depends on::Used by", "value": "1a9cb166f1571100a92eb60da2bcexxx"}, "target": {"link": "https://dev98xxx.service-now.com/api/now/cmdb/instance/cmdb_ci/161441257f701200bee45f19befa9xxx", "display_value": "IP-Router-3", "value": "161441257f701200bee45f19befa9xxx"}}], "attributes": {"lease_id": "", "operational_status": "1", "change_control": "", "subcategory": "Cluster", "sys_tags": "", "sys_created_on": "2016-01-06 16:47:15", "gl_account": "", "dns_domain": "", "due": "", "asset_tag": "", "correlation_id": "", "managed_by": "", "cluster_id": "", "managed_by_group": "", "assigned_to": "", "duplicate_of": "", "install_status": "1", "cost_center": "", "location": "", "checked_in": "", "category": "Resource", "monitor": "false", "justification": "", "skip_sync": "false", "cluster_type": "", "sys_updated_by": "glide.maint", "sys_created_by": "glide.maint", "model_number": "", "comments": "", "environment": "", "attested_by": "", "cluster_status": "", "mac_address": "", "short_description": "", "serial_number": "", "attested": "false", "unverified": "false", "start_date": "", "fault_count": "0", "purchase_date": "", "cost": "", "model_id": "", "sys_class_name": "cmdb_ci_win_cluster", "warranty_expiration": "", "vendor": "", "asset": "", "discovery_source": "", "schedule": "", "checked_out": "", "company": "", "sys_updated_on": "2016-01-06 19:04:07", "supported_by": "", "department": "", "cost_cc": "USD", "sys_mod_count": "1", "sys_class_path": "/!!/!5/!$", "attributes": "", "invoice_number": "", "sys_domain_path": "/", "ip_address": "", "manufacturer": "", "assigned": "", "last_discovered": "", "maintenance_schedule": "", "name": "SAP-LB-Win-Cluster", "po_number": "", "sys_id": "103d30e17f701200bee45f19befa91db", "due_in": "", "install_date": "", "fqdn": "", "caption": "", "order_date": "", "can_print": "false", "attestation_score": "", "support_group": "", "assignment_group": "", "sys_domain": {"link": "https://dev98xxx.service-now.com/api/now/table/sys_user_group/global", "display_value": "global", "value": "global"}, "owned_by": "", "attested_date": "", "first_discovered": "", "cluster_version": "", "delivery_date": ""}, "outbound_relations": [{"sys_id": "56f3a7ad7f701200bee45f19befa910f", "type": {"link": "https://dev98xxx.service-now.com/api/now/table/cmdb_rel_type/55c913d3c0a8010e012d1563182d6xxx", "display_value": "Members::Member of", "value": "55c913d3c0a8010e012d1563182d6xxx"}, "target": {"link": "https://dev98xxx.service-now.com/api/now/cmdb/instance/cmdb_ci/95bdb0e17f701200bee45f19befa9127", "display_value": "SAP LB2", "value": "95bdb0e17f701200bee45f19befa9127"}}, {"sys_id": "e38367ad7f701200bee45f19befa91ab", "type": {"link": "https://dev98xxx.service-now.com/api/now/table/cmdb_rel_type/55c913d3c0a8010e012d1563182d6xxx", "display_value": "Members::Member of", "value": "55c913d3c0a8010e012d1563182d6xxx"}, "target": {"link": "https://dev98xxx.service-now.com/api/now/cmdb/instance/cmdb_ci/6c9d70e17f701200bee45f19befa91a1", "display_value": "SAP LB1", "value": "6c9d70e17f701200bee45f19befa91a1"}}]}}]
```



#### Wait For Comments
Wait for comments related to a specific table record in ServiceNow. Note: Action is running as async, please adjust script timeout value in Siemplify IDE for action as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Table Name|Specify the name of the table in which you want to wait for a comment or work note. Example: incident.|True|String||
|Record Sys ID|Specify the record ID in which you want to wait for a comment or work note.|True|String||
|Type|Specify for what type of object action needs to wait.|True|List|Comment|
|Wait Mode|Specify the wait mode for the action. If "Until Timeout" is selected, action will wait until and return all of the comments in that timeframe. If "Until First Message" is selected, action will wait until a new message appears after action execution. If "Until Specific Text" is selected, action will wait until there is a message that is equal to the string provided in the "Text" parameter. Note: "Text" parameter is mandatory, if "Until Specific Text" is provided.|True|List|Until Timeout|
|Text|Specify the text for which action needs to wait. Note: this parameter is only relevant, if "Until Specific Text" is selected for "Wait Mode" parameter.|False|String||



##### JSON Results
```json
[{"sys_id":"e5039e6097211110c8cb32xxxxxxxxxx","sys_created_on":"2022-08-23 05:27:43","name":"incident","element_id":"40a5d77b97411110c8cb32xxxxxxxxxx","sys_tags":"","value":"test comment","sys_created_by":"admin","element":"comments"},{"sys_id":"8e03da6097211110c8cb32xxxxxxxxxx","sys_created_on":"2022-08-23 05:27:46","name":"incident","element_id":"40a5d77b97411110c8cb32xxxxxxxxxx","sys_tags":"","value":"new comment","sys_created_by":"admin","element":"comments"}]
```



#### Add Comment
Add a comment to a ServiceNow incident
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Incident Number|Specify number of the incident. Format: INCxxxxxxx|True|String||
|Comment|Specify what comment to add to the incident.|True|Content||



#### Update Record
Update available records in different tables of Service Now.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Table Name|Specify what table should be used to update a record.|False|String|None|
|Object Json Data|Specify JSON data that is needed to update a record.|True|String|None|
|Record Sys ID|Specify Sys ID of the needed record.|True|String|None|



##### JSON Results
```json
{"sys_tags": "", "user_input": "", "calendar_stc": "", "subcategory": "", "watch_list": "", "follow_up": "", "made_sla": "true", "sys_created_by": "admin", "sla_due": "", "number": "INC0010021", "group_list": "", "reassignment_count": "0", "assigned_to": "", "sys_mod_count": "3", "notify": "1", "resolved_by": "", "upon_reject": "cancel", "additional_assignee_list": "", "category": "inquiry", "closed_at": "", "parent_incident": "", "cmdb_ci": "", "contact_type": "", "impact": "3", "rfc": "", "expected_start": "", "knowledge": "false", "sys_updated_by": "admin", "caused_by": "", "comments": "", "closed_by": "", "priority": "5", "state": "1", "sys_id": "19fcb4672fb11010f170c886f699b612", "opened_at": "2020-07-09 11:24:34", "child_incidents": "0", "work_notes": "", "delivery_task": "", "short_description": "", "comments_and_work_notes": "", "time_worked": "", "upon_approval": "proceed", "company": "", "business_stc": "", "correlation_display": "", "sys_class_name": "incident", "delivery_plan": "", "escalation": "0", "description": "", "parent": "", "close_notes": "", "business_duration": "", "problem_id": "", "sys_updated_on": "2020-07-10 09:59:41", "approval_history": "", "approval_set": "", "business_service": "", "reopened_by": "", "calendar_duration": "", "caller_id": "", "active": "true", "approval": "not requested", "service_offering": "", "sys_domain_path": "/", "hold_reason": "", "activity_due": "", "severity": "3", "incident_state": "1", "resolved_at": "", "location": "", "due_date": "", "work_start": "", "work_end": "", "work_notes_list": "", "sys_created_on": "2020-07-10 08:24:34", "correlation_id": "", "contract": "", "reopened_time": "", "opened_by": {"link": "https://dev92294.service-now.com/api/now/v1/table/sys_user/{link=https://dev92294.service-n", "value": "{link=https://dev92294.service-n"}, "close_code": "", "assignment_group": "", "sys_domain": {"link": "https://dev92294.service-now.com/api/now/v1/table/sys_user_group/{link=https://dev92294.service-n", "value": "{link=https://dev92294.service-n"}, "order": "", "urgency": "3", "reopen_count": "0"}
```



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Update Incident
Update incident information
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Incident Number|Specify number of the incident. Format: INCxxxxxxx|True|String||
|Short Description|Specify short description of the incident.|False|String||
|Impact|Specify impact of the incident. Possible values: 1 for High, 2 for Medium and 3 for Low.|False|String||
|Urgency|Specify urgency of the incident. Possible values: 1 for High, 2 for Medium and 3 for Low.|False|String||
|Category|Specify category of the incident.|False|String||
|Assignment group ID|Specify full name of the group that was assigned to the incident.|False|String||
|Assigned User ID|Specify email address or the username of the user that was assigned to the incident.|False|String||
|Description|Specify description of the incident.|False|String||
|Incident State|Status name or status id.|False|String||
|Custom Fields|Specify a comma-separated list of fields and values. Format: field_1:value_1,field_2:value_2. You can also specify a JSON object as input. Note: this parameter has priority and all of the fields will be overwritten with the value that is provided for this parameter. Example: {"field":"value"}|False|String||



##### JSON Results
```json
{"sys_tags": "", "user_input": "", "calendar_stc": "2102", "subcategory": "", "watch_list": "", "follow_up": "", "made_sla": "true", "sys_created_by": "admin", "sla_due": "", "number": "INC0010041", "group_list": "", "reassignment_count": "0", "assigned_to": "", "sys_mod_count": "10", "notify": "1", "resolved_by": {"link": "https://dev92294.service-now.com/api/now/v1/table/sys_user/6816f79cc0a8016401c5a33be04be441", "value": "6816f79cc0a8016401c5a33be04be441"}, "upon_reject": "cancel", "additional_assignee_list": "", "category": "inquiry", "closed_at": "2020-07-10 12:53:06", "parent_incident": "", "cmdb_ci": "", "contact_type": "", "impact": "1", "rfc": "", "expected_start": "", "knowledge": "false", "sys_updated_by": "admin", "caused_by": "", "comments": "", "closed_by": {"link": "https://dev92294.service-now.com/api/now/v1/table/sys_user/6816f79cc0a8016401c5a33be04be441", "value": "6816f79cc0a8016401c5a33be04be441"}, "priority": "1", "state": "7", "sys_id": "f562fd272f351010f170c886f699b669", "opened_at": "2020-07-10 12:18:04", "child_incidents": "0", "work_notes": "", "delivery_task": "", "short_description": "sdf", "comments_and_work_notes": "", "time_worked": "", "upon_approval": "proceed", "company": "", "business_stc": "0", "correlation_display": "", "sys_class_name": "incident", "delivery_plan": "", "escalation": "0", "description": "", "parent": "", "close_notes": "Closed by Caller", "business_duration": "1970-01-01 00:00:00", "problem_id": "", "sys_updated_on": "2020-07-10 13:13:57", "approval_history": "", "approval_set": "", "business_service": "", "reopened_by": "", "calendar_duration": "1970-01-01 00:35:02", "caller_id": {"link": "https://dev92294.service-now.com/api/now/v1/table/sys_user/6816f79cc0a8016401c5a33be04be441", "value": "6816f79cc0a8016401c5a33be04be441"}, "active": "false", "approval": "not requested", "service_offering": "", "sys_domain_path": "/", "hold_reason": "", "activity_due": "2020-07-10 14:33:28", "severity": "3", "incident_state": "7", "resolved_at": "2020-07-10 12:53:06", "location": "", "due_date": "", "work_start": "", "work_end": "", "work_notes_list": "", "sys_created_on": "2020-07-10 12:18:04", "correlation_id": "", "contract": "", "reopened_time": "", "opened_by": {"link": "https://dev92294.service-now.com/api/now/v1/table/sys_user/6816f79cc0a8016401c5a33be04be441", "value": "6816f79cc0a8016401c5a33be04be441"}, "close_code": "Closed/Resolved by Caller", "assignment_group": "", "sys_domain": {"link": "https://dev92294.service-now.com/api/now/v1/table/sys_user_group/global", "value": "global"}, "order": "", "urgency": "1", "reopen_count": "0"}
```



#### Get Child Incident Details
Retrieve information about child incidents based on the parent incident in ServiceNow.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Parent Incident Number|Specify a number of the incident for which you want to retrieve child incident details. Format: INCxxxxxxx|True|String||
|Max Child Incident To Return|Specify how many child incidents to return. Default: 50.|False|String|50|



##### JSON Results
```json
[{"parent": "", "made_sla": "true", "caused_by": "", "watch_list": "", "upon_reject": "cancel", "sys_updated_on": "2020-11-25 18:34:40", "child_incidents": "0", "hold_reason": "", "approval_history": "", "skills": "", "number": "INC0010xxx", "resolved_by": "", "sys_updated_by": "admin", "opened_by": {"link": "https://dev98xxx.service-now.com/api/now/v1/table/sys_user/6816f79cc0a8016401c5a33xxxxx", "value": "6816f79cc0a8016401c5a33xxxxx"}, "user_input": "", "sys_created_on": "2020-11-25 18:34:40", "sys_domain": {"link": "https://dev98xxx.service-now.com/api/now/v1/table/sys_xxx_group/global", "value": "global"}, "state": "2", "sys_created_by": "user", "knowledge": "false", "order": "", "calendar_stc": "", "closed_at": "", "cmdb_ci": "", "delivery_plan": "", "contract": "", "impact": "3", "active": "true", "work_notes_list": "", "business_service": "", "priority": "4", "sys_domain_path": "/", "rfc": "", "time_worked": "", "expected_start": "", "opened_at": "2020-11-25 18:34:32", "business_duration": "", "group_list": "", "work_end": "", "caller_id": {"link": "https://dev98xxx.service-now.com/api/now/v1/table/sys_user/62826bf03710200044e0bfcxxxxx", "value": "62826bf03710200044e0bfcxxxxx"}, "reopened_time": "", "resolved_at": "", "approval_set": "", "subcategory": "", "work_notes": "", "short_description": "short description", "close_code": "", "correlation_display": "", "delivery_task": "", "work_start": "", "assignment_group": "", "additional_assignee_list": "", "business_stc": "", "description": "description", "calendar_duration": "", "close_notes": "", "notify": "1", "service_offering": "", "sys_class_name": "incident", "closed_by": "", "follow_up": "", "parent_incident": {"link": "https://dev98xxx.service-now.com/api/now/v1/table/incident/434773172f60a010c51853xxxxx", "value": "434773172f60a010c51853xxxxxx"}, "sys_id": "82f3350c2ff8e010c51853xxxxxx", "contact_type": "", "reopened_by": "", "incident_state": "2", "urgency": "2", "problem_id": "", "company": {"link": "https://dev98xxx.service-now.com/api/now/v1/table/core_company/227cdfb03710200044e0bfxxxxx", "value": "227cdfb03710200044e0bfxxxxx"}, "reassignment_count": "0", "activity_due": "", "assigned_to": "", "severity": "3", "comments": "", "approval": "not requested", "sla_due": "", "comments_and_work_notes": "", "due_date": "", "sys_mod_count": "0", "reopen_count": "0", "sys_tags": "", "escalation": "0", "upon_approval": "proceed", "correlation_id": "", "location": "", "category": "database"}]
```



#### Wait For Status Update
ServiceNow - Wait For Status Update
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Incident Number|Specify number of the incident. Format: INCxxxxxxx|True|String|None|
|Statuses|Specify what statuses of the incident are expected. Example: In Progress,Resolved.|True|String|None|



##### JSON Results
```json
{"parent": "", "made_sla": "true", "caused_by": "", "watch_list": "", "upon_reject": "Cancel all future Tasks", "sys_updated_on": "2020-11-22 09:51:20", "child_incidents": "0", "hold_reason": "", "approval_history": "", "skills": "", "number": "INC0010xxx", "resolved_by": {"display_value": "System Administrator", "link": "https://dev98xxx.service-now.com/api/now/v1/table/sys_user/6816f79cc0a8016401c5a33bxxxx"}, "sys_updated_by": "admin", "opened_by": {"display_value": "System Administrator", "link": "https://dev98xxx.service-now.com/api/now/v1/table/sys_user/6816f79cc0a8016401c5a33bxxxx"}, "user_input": "", "sys_created_on": "2020-11-22 09:40:35", "sys_domain": {"display_value": "global", "link": "https://dev98xxx.service-now.com/api/now/v1/table/sys_user_group/global"}, "state": "Resolved", "sys_created_by": "Admin", "knowledge": "false", "order": "", "calendar_stc": "645", "closed_at": "", "cmdb_ci": "", "delivery_plan": "", "contract": "", "impact": "2 - Medium", "active": "true", "work_notes_list": "", "business_service": "", "priority": "4 - Low", "sys_domain_path": "/", "rfc": "", "time_worked": "", "expected_start": "", "opened_at": "2020-11-22 09:40:35", "business_duration": "0 Seconds", "group_list": "", "work_end": "", "caller_id": {"display_value": "System Administrator", "link": "https://dev98xxx.service-now.com/api/now/v1/table/sys_user/6816f79cc0a8016401c5a33bxxxx"}, "reopened_time": "", "resolved_at": "2020-11-22 09:51:20", "approval_set": "", "subcategory": null, "work_notes": "", "short_description": "short description", "close_code": "Closed/Resolved by Caller", "correlation_display": "", "delivery_task": "", "work_start": "", "assignment_group": "", "additional_assignee_list": "", "business_stc": "0", "description": "", "calendar_duration": "10 Minutes", "close_notes": "Closed by Caller", "notify": "Do Not Notify", "service_offering": "", "sys_class_name": "Incident", "closed_by": "", "follow_up": "", "parent_incident": "", "sys_id": "aada0a4f2f6c2010c518532a27xxxx", "contact_type": null, "reopened_by": "", "incident_state": "Resolved", "urgency": "3 - Low", "problem_id": "", "company": "", "reassignment_count": "0", "activity_due": "UNKNOWN", "assigned_to": "", "severity": "3 - Low", "comments": "", "approval": "Not Yet Requested", "sla_due": "UNKNOWN", "comments_and_work_notes": "", "due_date": "", "sys_mod_count": "2", "reopen_count": "0", "sys_tags": "", "escalation": "Normal", "upon_approval": "Proceed to Next Task", "correlation_id": "", "location": "", "category": "Inquiry / Help"}
```



#### Get Incident
Retrieve information about a ServiceNow incident
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Incident Number|Specify number of the incident. Format: INCxxxxxxx|True|String||



##### JSON Results
```json
{"user_input": "", "sys_updated_by": "admin", "subcategory": "None", "watch_list": "", "due_date": "", "made_sla": "true", "caused_by": "", "number": "INC0010001", "group_list": "", "correlation_id": "", "sys_mod_count": "0", "notify": "Do Not Notify", "resolved_by": "", "upon_reject": "Cancel all future Tasks", "additional_assignee_list": "", "category": "Inquiry / Help", "closed_at": "", "sla_due": "UNKNOWN", "upon_approval": "Proceed to Next Task", "follow_up": "", "close_notes": "", "expected_start": "", "knowledge": "false", "calendar_stc": "", "sys_created_by": "admin", "comments": "", "problem_id": "", "priority": "5 - Planning", "state": "New", "sys_id": "bf939329db13230011d0ab7dca961908", "opened_at": "2019-01-29 07:15:41", "cmdb_ci": "", "delivery_task": "", "short_description": "da", "comments_and_work_notes": "", "order": "", "company": "", "child_incidents": "0", "sys_tags": "", "sys_class_name": "Incident", "delivery_plan": "", "description": "", "parent": "", "business_duration": "", "rfc": "", "reassignment_count": "0", "work_notes": "", "approval_history": "", "assignment_group": "", "work_start": "", "business_service": "", "resolved_at": "", "calendar_duration": "", "caller_id": {"link": "https://dev70256.service-now.com/api/now/v1/table/sys_user/6816f79cc0a8016401c5a33be04be441", "display_value": "System Administrator"}, "active": "true", "approval": "Not Yet Requested", "parent_incident": "", "time_worked": "", "closed_by": "", "sys_domain_path": "/", "severity": "3 - Low", "activity_due": "UNKNOWN", "incident_state": "New", "reopen_count": "0", "sys_updated_on": "2019-01-29 07:15:48", "impact": "3 - Low", "work_end": "", "hold_reason": "", "work_notes_list": "", "sys_created_on": "2019-01-29 07:15:48", "location": "", "escalation": "Normal", "contact_type": "None", "opened_by": {"link": "https://dev70256.service-now.com/api/now/v1/table/sys_user/6816f79cc0a8016401c5a33be04be441", "display_value": "System Administrator"}, "close_code": "None", "sys_domain": {"link": "https://dev70256.service-now.com/api/now/v1/table/sys_user_group/global", "display_value": "global"}, "assigned_to": "", "approval_set": "", "business_stc": "", "correlation_display": "", "urgency": "3 - Low"}
```



#### List CMDB Records
List CMDB records from the same class in ServiceNow.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Class Name|Specify name of the class, from where you want to list records. Example: cmdb_ci_appl.|True|String||
|Query Filter|Specify query filter for the results. Visit documentation to get more details. Example of the filter: sys_idLIKE1^sys_idSTARTSWITH0.|False|String||
|Max Records To Return|Specify how many records to return.|False|String|50|



##### JSON Results
```json
{"result": [{"sys_id": "02ece63e0b203200dc03650d37673xxx", "name": "AMSHumanCapital_development"}, {"sys_id": "0d62dfeb1394130068227f176144bxxx", "name": "ACME Citrix License server"}]}
```



#### Create Record
Create new records in different tables of Service Now.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Table Name|Specify what table should be used to create a record.|False|String|None|
|Object Json Data|Specify JSON data that is needed to create a record.|False|String|None|



##### JSON Results
```json
{"sys_tags": "", "user_input": "", "calendar_stc": "", "subcategory": "", "watch_list": "", "follow_up": "", "made_sla": "true", "sys_created_by": "admin", "sla_due": "", "number": "INC0010021", "group_list": "", "reassignment_count": "0", "assigned_to": "", "sys_mod_count": "0", "notify": "1", "resolved_by": "", "upon_reject": "cancel", "additional_assignee_list": "", "category": "inquiry", "closed_at": "", "parent_incident": "", "cmdb_ci": "", "contact_type": "", "impact": "3", "rfc": "", "expected_start": "", "knowledge": "false", "sys_updated_by": "admin", "caused_by": "", "comments": "", "closed_by": "", "priority": "5", "state": "1", "sys_id": "19fcb4672fb11010f170c886f699b612", "opened_at": "2020-07-10 08:24:34", "child_incidents": "0", "work_notes": "", "delivery_task": "", "short_description": "", "comments_and_work_notes": "", "time_worked": "", "upon_approval": "proceed", "company": "", "business_stc": "", "correlation_display": "", "sys_class_name": "incident", "delivery_plan": "", "escalation": "0", "description": "", "parent": "", "close_notes": "", "business_duration": "", "problem_id": "", "sys_updated_on": "2020-07-10 08:24:34", "approval_history": "", "approval_set": "", "business_service": "", "reopened_by": "", "calendar_duration": "", "caller_id": "", "active": "true", "approval": "not requested", "service_offering": "", "sys_domain_path": "/", "hold_reason": "", "activity_due": "", "severity": "3", "incident_state": "1", "resolved_at": "", "location": "", "due_date": "", "work_start": "", "work_end": "", "work_notes_list": "", "sys_created_on": "2020-07-10 08:24:34", "correlation_id": "", "contract": "", "reopened_time": "", "opened_by": {"link": "https://dev92294.service-now.com/api/now/v1/table/sys_user/6816f79cc0a8016401c5a33be04be441", "value": "6816f79cc0a8016401c5a33be04be441"}, "close_code": "", "assignment_group": "", "sys_domain": {"link": "https://dev92294.service-now.com/api/now/v1/table/sys_user_group/global", "value": "global"}, "order": "", "urgency": "3", "reopen_count": "0"}
```



#### Create Alert Incident
Create an incident related to a Siemplify alert
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Impact|Specify impact of the incident. Possible values: 1 for High, 2 for Medium and 3 for Low.|True|String|1|
|Urgency|Specify urgency of the incident. Possible values: 1 for High, 2 for Medium and 3 for Low.|True|String|1|
|Category|Specify category of the incident.|False|String|None|
|Assignment group ID|Specify full name of the group that was assigned to the incident.|False|String|None|
|Assigned User ID|Specify full name of the user that was assigned to the incident.|False|String|None|
|Description|Specify description of the incident.|False|Content|None|



##### JSON Results
```json
{"sys_tags": "", "user_input": "", "calendar_stc": "", "subcategory": "", "watch_list": "", "follow_up": "", "made_sla": "true", "sys_created_by": "admin", "sla_due": "", "number": "INC0010005", "group_list": "", "reassignment_count": "0", "assigned_to": "", "sys_mod_count": "0", "notify": "1", "resolved_by": "", "upon_reject": "cancel", "additional_assignee_list": "", "category": "inquiry", "closed_at": "", "parent_incident": "", "cmdb_ci": "", "contact_type": "", "impact": "1", "rfc": "", "expected_start": "", "knowledge": "false", "sys_updated_by": "admin", "caused_by": "", "comments": "", "closed_by": "", "priority": "1", "state": "1", "sys_id": "6131d0eb2f311010f170c886f699b61c", "opened_at": "2020-07-10 05:13:25", "child_incidents": "0", "work_notes": "", "delivery_task": "", "short_description": "4187b92c-7aaa-40ec-a032-833dd5a854e6", "comments_and_work_notes": "", "time_worked": "", "upon_approval": "proceed", "company": "", "business_stc": "", "correlation_display": "", "sys_class_name": "incident", "delivery_plan": "", "escalation": "0", "description": "", "parent": "", "close_notes": "", "business_duration": "", "problem_id": "", "sys_updated_on": "2020-07-10 05:13:25", "approval_history": "", "approval_set": "", "business_service": "", "reopened_by": "", "calendar_duration": "", "caller_id": {"link": "https://dev92294.service-now.com/api/now/v1/table/sys_user/6816f79cc0a8016401c5a33be04be441", "value": "6816f79cc0a8016401c5a33be04be441"}, "active": "true", "approval": "not requested", "service_offering": "", "sys_domain_path": "/", "hold_reason": "", "activity_due": "2020-07-10 07:13:25", "severity": "3", "incident_state": "1", "resolved_at": "", "location": "", "due_date": "", "work_start": "", "work_end": "", "work_notes_list": "", "sys_created_on": "2020-07-10 05:13:25", "correlation_id": "", "contract": "", "reopened_time": "", "opened_by": {"link": "https://dev92294.service-now.com/api/now/v1/table/sys_user/6816f79cc0a8016401c5a33be04be441", "value": "6816f79cc0a8016401c5a33be04be441"}, "close_code": "", "assignment_group": "", "sys_domain": {"link": "https://dev92294.service-now.com/api/now/v1/table/sys_user_group/global", "value": "global"}, "order": "", "urgency": "1", "reopen_count": "0"}
```



#### Add Parent Incident
Add the parent incident for the incidents in ServiceNow.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Parent Incident Number|Parent incident number. All of the incidents in the “Child Incident Numbers” parameter will be added as children for the parent incident. Configure this parameter in the following format: INCxxxxxxx|True|String||
|Child Incident Numbers|Comma-separated list of numbers that are related to the incident and used as children for the parent incident. Configure this parameter in the following format: INCxxxxxxx|True|String||



##### JSON Results
```json
{"result":[{"parent":"","made_sla":"true","caused_by":"","watch_list":"","upon_reject":"cancel","sys_updated_on":"2024-03-05 11:43:21","child_incidents":"0","hold_reason":"","origin_table":"","task_effective_number":"INC0000000","approval_history":"","number":"INC0000000","resolved_by":{"link":"https://dev000000.service-now.com/api/now/table/sys_user/5137xxxxxxxxxxx","value":"5137xxxxxxxxxxx"},"sys_updated_by":"admin","opened_by":{"link":"https://dev000000.service-now.com/api/now/table/sys_user/681xxxxxxxx","value":"681xxxxxxxxx"},"user_input":"","sys_created_on":"2016-12-12 15:19:57","sys_domain":{"link":"https://dev000000.service-now.com/api/now/table/sys_user_group/global","value":"global"},"state":"7","route_reason":"","sys_created_by":"employee","knowledge":"false","order":"","calendar_stc":"000000","closed_at":"2016-12-14 02:46:44","cmdb_ci":{"link":"https://dev000000.service-now.com/api/now/table/cmdb_ci/109xxxxxxxxxx","value":"109xxxxxxxxxx"},"delivery_plan":"","contract":"","impact":"2","active":"false","work_notes_list":"","business_service":{"link":"https://dev000000.service-now.com/api/now/table/cmdb_ci_service/27dxxxxxxxxxxxx","value":"27dxxxxxxxxxx"},"business_impact":"","priority":"3","sys_domain_path":"/","rfc":"","time_worked":"","expected_start":"","opened_at":"2016-12-12 15:19:57","business_duration":"1970-01-01 08:00:00","group_list":"","work_end":"","caller_id":{"link":"https://dev000000.service-now.com/api/now/table/sys_user/681xxxxxxxxxx","value":"681xxxxxxxxxx"},"reopened_time":"","resolved_at":"2016-12-13 21:43:14","approval_set":"","subcategory":"email","work_notes":"","universal_request":"","short_description":"Unable to connect to email","close_code":"Solved (Permanently)","correlation_display":"","delivery_task":"","work_start":"","assignment_group":{"link":"https://dev000000.service-now.com/api/now/table/sys_user_group/287xxxxxxxxxxx","value":"287xxxxxxxxx"},"additional_assignee_list":"","business_stc":"28800","cause":"","description":"I am unable to connect to the email server. It appears to be down.","origin_id":"","calendar_duration":"1970-01-02 04:23:17","close_notes":"This incident is resolved.","notify":"1","service_offering":"","sys_class_name":"incident","closed_by":{"link":"https://dev000000.service-now.com/api/now/table/sys_user/681xxxxxxxxxxx","value":"681xxxxxxxxxx"},"follow_up":"","parent_incident":{"link":"https://dev000000.service-now.com/api/now/table/incident/46cxxxxxxxxxxx","value":"46cxxxxxxxxxx"},"sys_id":"1c7xxxxxxxxxx","contact_type":"self-service","reopened_by":"","incident_state":"7","urgency":"2","problem_id":"","company":{"link":"https://dev000000.service-now.com/api/now/table/core_company/31bxxxxxxxxxxxxxxxxxxx","value":"31bxxxxxxxxxxxxxxxxx"},"reassignment_count":"2","activity_due":"2016-12-13 01:26:36","assigned_to":{"link":"https://dev000000.service-now.com/api/now/table/sys_user/513xxxxxxxxxxxxxxxxxx","value":"513xxxxxxxxxxxxxxxxxx"},"severity":"3","comments":"","approval":"not requested","sla_due":"","comments_and_work_notes":"","due_date":"","sys_mod_count":"16","reopen_count":"0","sys_tags":"","escalation":"0","upon_approval":"proceed","correlation_id":"","location":"","category":"inquiry"}]}
```



#### List Record Comments
List comments related to a specific table record in ServiceNow.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Table Name|Specify the name of the table for which you want to list comments or work notes. Example: incident.|True|String||
|Record Sys ID|Specify the record ID for which you want to list comments or work notes.|True|String||
|Type|Specify whether comment or work note should be listed.|True|List|Comment|
|Max Results To Return|Specify how many results to return. Default: 50.|False|String|50|



##### JSON Results
```json
[{"sys_id":"43551xxxxxxxxxxxxx","sys_created_on":"2021-09-03 10:29:48","name":"incident","element_id":"552c4xxxxxxxxxxxxx","sys_tags":"","value":"test","sys_created_by":"admin","element":"comments"}]
```



#### Add Comment And Wait For Reply
Wait for new comment to be added to the given incident. Action result is the content of the new comments
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Incident Number|Specify number of the incident. Format: INCxxxxxxx|True|String|None|
|Comment|Specify what comment to add to the incident.|True|Content||



#### Get User Details
Retrieve information about the user by the sys_id or email in ServiceNow.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|User Sys IDs|Specify a comma-separated list of sys_ids of the users for which you want to retrieve details. Example: sys_id_1,sys_id_2|False|String||
|Emails|Specify a comma-separated list of emails of the users for which you want to retrieve details. Example: email1@example.com,email2@example.com|False|String||



##### JSON Results
```json
[{"calendar_integration": "1", "country": "", "last_position_update": "", "user_password": "bkpu23xxxx", "last_login_time": "", "source": "", "sys_updated_on": "2020-08-29 02:42:45", "building": "", "web_service_access_only": "false", "notification": "1", "enable_multifactor_authn": "false", "sys_updated_by": "developer.xxxx@snc", "sys_created_on": "2005-05-02 19:28:40", "agent_status": "", "sys_domain": {"link": "https://dev98xxx.service-now.com/api/now/v1/table/xxxx/global", "value": "global"}, "state": "", "vip": "false", "sys_created_by": "glide.maint", "longitude": "", "zip": "", "home_phone": "", "time_format": "", "last_login": "", "default_perspective": "", "geolocation_tracked": "false", "active": "true", "sys_domain_path": "/", "cost_center": {"link": "https://dev98xxx.service-now.com/api/now/v1/table/cmn_cost_xxx/d9d07bddc0a80a647cf93xxxxxx", "value": "d9d07bddc0a80a647cf93xxxxxx"}, "phone": "", "name": "Don Goodliffe", "employee_number": "", "password_needs_reset": "false", "gender": "Male", "city": "", "failed_attempts": "", "user_name": "don.goodlxxxx", "latitude": "", "roles": "itil", "title": "", "sys_class_name": "sys_user", "sys_id": "9ee1b13dc6112271007f9xxxxx", "internal_integration_user": "false", "ldap_server": "", "mobile_phone": "", "street": "", "company": {"link": "https://dev98xxx.service-now.com/api/now/v1/table/core_company/31bea3d53790200044e0bfxxxxx", "value": "31bea3d53790200044e0bfxxxx"}, "department": {"link": "https://dev98xxx.service-now.com/api/now/v1/table/cmn_department/221f3db5c6112284009fxxxxx", "value": "221f3db5c6112284009fxxxxx"}, "first_name": "Don", "email": "don.goodxxxx@example.com", "introduction": "", "preferred_language": "", "manager": "", "business_criticality": "3", "locked_out": "false", "sys_mod_count": "10", "last_name": "Goodliffe", "photo": "", "avatar": "de0f78383730310042106710xxxxx", "middle_name": "", "sys_tags": "", "time_zone": "", "schedule": "", "on_schedule": "", "date_format": "", "location": {"link": "https://dev98xxx.service-now.com/api/now/v1/table/cmn_location/f90ad9120a0a0b9100514xxxx", "value": "f90ad9120a0a0b9100514xxxxx"}}]
```



#### Add Comment To Record
Add a comment to a specific table record in ServiceNow. Note: Action is running as async if "Wait For Reply" is enabled, please adjust script timeout value in Siemplify IDE for action as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Table Name|Specify the name of the table to which you want to add a comment or work note. Example: incident.|True|String||
|Type|Specify whether comment or work note should be added to the record.|True|List|Comment|
|Record Sys ID|Specify the record ID to which you want to add a comment or work note.|True|String||
|Text|Specify the content of the comment or work note.|True|String||
|Wait For Reply|If enabled, action will wait for reply. Note: action will track comments, if comments are sent and work notes, if work notes are sent.|False|Boolean|false|



##### JSON Results
```json
{"sys_id":"e58d380b07a63010ff23f6xxxxxxxxxx","sys_created_on":"2021-09-16 18:19:28","name":"incident","element_id":"57af7aec73d42300272866xxxxxxxxxx","sys_tags":"","value":"test reply","sys_created_by":"admin","element":"comments"}
```



#### Close Incident
Close a ServiceNow incident
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Incident Number|Specify number of the incident. Format: INCxxxxxxx|True|String||
|Close Reason|Specify the reason, why incident was closed.|True|String||
|Resolution Code|Specify the resolution code for the incident.|True|List|Solution provided|
|Close Notes|Specify the close notes for the incident.|True|String||



#### Get Oauth Token
Get an Oauth refresh token for ServiceNow. Requires: Username, Password, Client ID and Client Secret to be provided in the configuration tab.
Timeout - 600 Seconds



##### JSON Results
```json
{"access_token":"xxxxxxxxxxxxxxxxxx","refresh_token":"xxxxxxxxxxxxxxxxxx","scope":"useraccount","token_type":"Bearer","expires_in":1799}
```



#### Get Record Details
Retrieve information about specific table records in ServiceNow.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Table Name|Specify name of the table, where you want to search for the record. Example: incident.|True|String||
|Record Sys ID|Specify the record ID for which you want to retrieve details.|True|String||
|Fields|Specify a comma-separated list of fields that should be returned for that record. If nothing is specified, action will return the default fields for that record. Example: field_1,field_2.|False|String||



##### JSON Results
```json
{"parent": "", "made_sla": "true", "caused_by": "", "watch_list": "", "upon_reject": "cancel", "sys_updated_on": "2020-11-25 19:36:47", "child_incidents": "0", "hold_reason": "", "approval_history": "", "skills": "", "number": "INC0010xxx", "resolved_by": "", "sys_updated_by": "user.user", "opened_by": {"link": "https://dev98xxx.service-now.com/api/now/v1/table/sys_user/62826bf03710200044e0bfcxxxxx", "value": "62826bf03710200044e0bfxxxxx"}, "user_input": "", "sys_created_on": "2020-11-25 19:36:47", "sys_domain": {"link": "https://dev98xxx.service-now.com/api/now/v1/table/sys_user_group/global", "value": "global"}, "state": "1", "sys_created_by": "user", "knowledge": "false", "order": "", "calendar_stc": "", "closed_at": "", "cmdb_ci": "", "delivery_plan": "", "contract": "", "impact": "3", "active": "true", "work_notes_list": "", "business_service": "", "priority": "5", "sys_domain_path": "/", "rfc": "", "time_worked": "", "expected_start": "", "opened_at": "2020-11-25 19:36:47", "business_duration": "", "group_list": "", "work_end": "", "caller_id": {"link": "https://dev98xxx.service-now.com/api/now/v1/table/sys_user/62826bf03710200044e0bfxxxxx", "value": "62826bf03710200044e0bfxxxxx"}, "reopened_time": "", "resolved_at": "", "approval_set": "", "subcategory": "", "work_notes": "", "short_description": "test 10", "close_code": "", "correlation_display": "", "delivery_task": "", "work_start": "", "assignment_group": "", "additional_assignee_list": "", "business_stc": "", "description": "test 10", "calendar_duration": "", "close_notes": "", "notify": "1", "service_offering": "", "sys_class_name": "incident", "closed_by": "", "follow_up": "", "parent_incident": "", "sys_id": "ee224a842f3ce010c518532a279xxxx", "contact_type": "self-service", "reopened_by": "", "incident_state": "1", "urgency": "3", "problem_id": "", "company": {"link": "https://dev98xxx.service-now.com/api/now/v1/table/core_company/227cdfb03710200044e0bfxxxxx", "value": "227cdfb03710200044e0bfxxxxx"}, "reassignment_count": "0", "activity_due": "", "assigned_to": "", "severity": "3", "comments": "", "approval": "not requested", "sla_due": "", "comments_and_work_notes": "", "due_date": "", "sys_mod_count": "0", "reopen_count": "0", "sys_tags": "", "escalation": "0", "upon_approval": "proceed", "correlation_id": "", "location": "", "category": "inquiry"}
```



#### List Records Related To User
List records from a table related to a user in ServiceNow.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Table Name|Specify name of the table, where you want to search for related records. Example: incident.|True|String||
|Usernames|Specify a comma-separated list of usernames for which you want to retrieve related records.|True|String||
|Max Days Backwards|Specify how many days backwards to fetch related records.|True|String|1|
|Max Records To Return|Specify how many records to return per user. Default: 50|False|String|50|



##### JSON Results
```json
[{"Entity": "username", "EntityResult": [{"parent": "", "made_sla": "true", "caused_by": "", "watch_list": "", "upon_reject": "cancel", "sys_updated_on": "2020-11-24 12:56:02", "child_incidents": "0", "hold_reason": "", "approval_history": "", "skills": "", "number": "INC0010xxx", "resolved_by": "", "sys_updated_by": "Admin", "opened_by": {"link": "https://dev98xxx.service-now.com/api/now/v1/table/sys_user/6816f79cc0a8016401c5a33xxxx", "value": "6816f79cc0a8016401c5a33xxxx"}, "user_input": "", "sys_created_on": "2020-11-24 12:56:02", "sys_domain": {"link": "https://dev98xxx.service-now.com/api/now/v1/table/sys_user_group/global", "value": "global"}, "state": "1", "sys_created_by": "Admin", "knowledge": "false", "order": "", "calendar_stc": "", "closed_at": "", "cmdb_ci": "", "delivery_plan": "", "contract": "", "impact": "3", "active": "true", "work_notes_list": "", "business_service": "", "priority": "5", "sys_domain_path": "/", "rfc": "", "time_worked": "", "expected_start": "", "opened_at": "2020-11-24 12:56:02", "business_duration": "", "group_list": "", "work_end": "", "caller_id": "", "reopened_time": "", "resolved_at": "", "approval_set": "", "subcategory": "", "work_notes": "", "short_description": "", "close_code": "", "correlation_display": "", "delivery_task": "", "work_start": "", "assignment_group": "", "additional_assignee_list": "", "business_stc": "", "description": "", "calendar_duration": "", "close_notes": "", "notify": "1", "service_offering": "", "sys_class_name": "incident", "closed_by": "", "follow_up": "", "parent_incident": "", "sys_id": "b5ec5be72fa8a010c518532axxxxx", "contact_type": "", "reopened_by": "", "incident_state": "1", "urgency": "3", "problem_id": "", "company": "", "reassignment_count": "0", "activity_due": "", "assigned_to": "", "severity": "3", "comments": "", "approval": "not requested", "sla_due": "", "comments_and_work_notes": "", "due_date": "", "sys_mod_count": "0", "reopen_count": "0", "sys_tags": "", "escalation": "0", "upon_approval": "proceed", "correlation_id": "", "location": "", "category": "inquiry"}]}]
```



#### Download Attachments
Download attachments related to a table record in ServiceNow.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Table Name|Specify name of the table, where the record from which you want to download attachments is located. Example: incident.|True|String||
|Record Sys ID|Specify sys id of the record from which you want to download attachment.|True|String||
|Download Folder Path|Specify the absolute folder path, where you want to store the downloaded attachments.|True|String||
|Overwrite|If enabled, action will overwrite files with the same name.|False|Boolean|false|



##### JSON Results
```json
[{"size_bytes": "62192", "file_name": "image_xxx.png", "sys_mod_count": "3", "average_image_color": "#251f30", "image_width": "1049", "sys_updated_on": "2020-11-23 12:11:54", "sys_tags": "", "table_name": "incident", "sys_id": "a539ce1b2f2c6010c518532axxxx", "image_height": "611", "sys_updated_by": "admin", "download_link": "https://dev98xxx.service-now.com/api/now/v1//attachment/a539ce1b2f2c6010c518532axxxx/file", "content_type": "image/png", "sys_created_on": "2020-11-23 12:11:54", "size_compressed": "55526", "compressed": "true", "state": "available", "table_sys_id": "0043fde92fd02010c518532axxxx", "chunk_size_bytes": "700000", "hash": "ffe386b22c572b14134533da96c9dd44be89bb8da785a16b073faxxxx", "sys_created_by": "admin", "absolute_file_path": "/opt/siemplify/siemplify_xxxx/xxxxx"}, {"size_bytes": "26625", "file_name": "image (2).png", "sys_mod_count": "3", "average_image_color": "#251f30", "image_width": "805", "sys_updated_on": "2020-11-23 12:11:54", "sys_tags": "", "table_name": "incident", "sys_id": "7539ce1b2f2c6010c518532axxxx", "image_height": "599", "sys_updated_by": "admin", "download_link": "https://dev98xxx.service-now.com/api/now/v1//attachment/7539ce1b2f2c6010c518532axxxx/file", "content_type": "image/png", "sys_created_on": "2020-11-23 12:11:54", "size_compressed": "20733", "compressed": "true", "state": "available", "table_sys_id": "0043fde92fd02010c518532axxx", "chunk_size_bytes": "700000", "hash": "640ac979019cb2fd968aa16fc7d1bce16b0c980e3995a8360axxxx", "sys_created_by": "admin", "absolute_file_path": "/opt/siemplify/siemplify_xxxx/xxx"}]
```






## Jobs

#### Sync Table Record Comments
This job will synchronize comments in ServiceNow table records and Siemplify cases.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Api Root|True|String|https://{dev-instance}.service-now.com/api/now/v1/|
|Username|True|String||
|Password|True|Password||
|Verify SSL|False|Boolean|true|
|Client ID|False|String||
|Client Secret|False|Password||
|Refresh Token|False|Password||
|Use Oauth Authentication|False|Boolean|false|
|Table Name|True|String||

#### Sync Incidents Job
This job will synchronize incidents fields and attachments that are related to case/alerts in ServiceNow. For the job to work, you need to have the "ServiceNow Incident Sync" tag added to the case and "TICKET_ID" context value added to either Case or Alert depending on the parameter "Sync Level". Example of the "TICKET_ID": "INC0000050,INC0000051".

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|API Root|True|String|https://{dev-instance}.service-now.com/api/now/v1/|
|Username|True|String||
|Password|True|Password||
|Sync Level|True|String|Case|
|Max Hours Backwards|True|Integer|24|
|Verify SSL|False|Boolean|true|

#### Sync Closed Incidents
This job will synchronize closed ServiceNow incidents and Siemplify alerts.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Api Root|True|String|https://{dev-instance}.service-now.com/api/now/v1/|
|Username|True|String||
|Password|True|Password||
|Verify SSL|False|Boolean|true|
|Client ID|False|String||
|Client Secret|False|Password||
|Refresh Token|False|Password||
|Use Oauth Authentication|False|Boolean|false|
|Max Hours Backwards|False|Integer|24|
|Table Name|True|String||

#### Sync Table Record Comments By Tag
This job will synchronize comments in ServiceNow table records and Siemplify cases. Additionally, in order for the job to work, it’s required for the case to have 2 tags. First tag should be "ServiceNow {table name}", for example, "ServiceNow incident" and the second should be with the prefix "ServiceNow TicketId: {TICKET_ID}". Example of the "TICKET_ID": "INC0000050,INC0000051".

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|API Root|True|String|https://{dev-instance}.service-now.com/api/now/v1/|
|Username|True|String||
|Password|True|Password||
|Table Name|True|String||
|Verify SSL|False|Boolean|true|



## Connectors
#### ServiceNow Connector
Fetching incidents from ServiceNow to Siemplify

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|The field name used to determine the device product|True|String|Product Name|
|EventClassId|The field name used to determine the event name (sub-type)|False|String|sys_class_name|
|PythonProcessTimeout|The timeout limit (in seconds) for the python process running current script|True|String|60|
|Rule Generator|The field name used to determine the rule generator.|False|String||
|Api Root|https://{dev-instance}.service-now.com/api/now/v1/|True|String||
|Incident Table|This parameter is defining what API root ServiceNow integration is going to use for actions that revolve around incidents. By default the integration uses the “table/incident” path. |False|String|incident|
|Username||True|String||
|Password||True|Password||
|Verify SSL|If enabled, verify the SSL certificate for the connection to the ServiceNow server is valid.|False|Boolean|true|
|Client ID|Client ID of Service Now application. Required for Oauth authentication.|False|String||
|Client Secret|Client Secret of Service Now application. Required for Oauth authentication.|False|Password||
|Refresh Token|Refresh token for Service Now application. Required for Oauth authentication.|False|Password||
|Use Oauth Authentication|If enabled, integration will use Oauth authentication. Parameters “Client ID“, “Client Secret“ and “Refresh Token“ are mandatory.|False|Boolean|false|
|Days Backwards|Fetch incidents from 'x' days backwards. e.g. 3|False|Integer|5|
|Max Incidents Per Cycle|Fetch max 'x' incidents. e.g. 10|False|Integer|10|
|Server Time Zone|The timezone configured in the server, ex. UTC, Asia/Jerusalem etc.|False|String|UTC|
|Environments Whitelist|The environments (domains) to ingest into Siemplify, comma separated list (env1,env2)|False|String||
|Table Name|The table to fetch from. e.g. incident|False|String||
|Event Name|The name of the event in Siemplify. e.g. ServiceNowEvent|False|String||
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password||
|Get User Information|If enabled, connector will additionally retrieve information about the users related to the incident.|False|Boolean|false|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|Boolean|false|




