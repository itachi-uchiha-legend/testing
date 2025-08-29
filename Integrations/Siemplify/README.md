
# Siemplify

Google SecOps integration package includes all of Google SecOps's internal actions, jobs etc.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Monitors Mail Recipients|None|True|String|example@mail.com,example1@mail.com|
|Elastic Server Address|None|True|String|localhost|


#### Dependencies
| |
|-|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|cachetools-5.3.3-py3-none-any.whl|
|google_api_python_client-2.134.0-py2.py3-none-any.whl|
|h11-0.14.0-py3-none-any.whl|
|TIPCommon-2.2.9-py2.py3-none-any.whl|
|httpcore-1.0.5-py3-none-any.whl|
|pyasn1_modules-0.4.0-py3-none-any.whl|
|httplib2-0.22.0-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|pytz-2025.2-py2.py3-none-any.whl|
|certifi-2024.6.2-py3-none-any.whl|
|googleapis_common_protos-1.63.1-py2.py3-none-any.whl|
|anyio-4.4.0-py3-none-any.whl|
|google_auth-2.30.0-py2.py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|rsa-4.9-py3-none-any.whl|
|google_api_core-2.19.0-py3-none-any.whl|
|proto_plus-1.24.0-py3-none-any.whl|
|pyasn1-0.6.0-py2.py3-none-any.whl|
|protobuf-4.25.3-cp37-abi3-manylinux2014_x86_64.whl|
|pyparsing-3.1.2-py3-none-any.whl|
|pycryptodome-3.20.0-cp35-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|idna-3.7-py3-none-any.whl|
|psutil-5.9.8-cp36-abi3-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|google_auth_httplib2-0.2.0-py2.py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|uritemplate-4.1.1-py2.py3-none-any.whl|
|httpx-0.27.0-py3-none-any.whl|


## Actions
#### Get Similar Cases
Search for similar cases and return their Ids
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Rule Generator|Search for similar cases by the same Rule Generator. Note: All these search criteria are joined using logical 'AND' condition and will be used in the same search.|False|Boolean||
|Port|Search for similar cases by the same Port number. Note: All these search criteria are joined using logical 'AND' condition and will be used in the same search.|False|Boolean||
|Category Outcome|Search for similar cases by the same Category Outcome. Note: All these search criteria are joined using logical 'AND' condition and will be used in the same search.|False|Boolean||
|Entity Identifier|Search for similar cases containing the same Entity Identifier. Note: All these search criteria are joined using logical 'AND' condition and will be used in the same search.|False|Boolean||
|Days Back|Defines how many days back the search should look for similar cases.|True|String||
|Include Open Cases|Search open cases|False|Boolean|true|
|Include Closed Cases|Search closed cases|False|Boolean|true|



##### JSON Results
```json
{"stats": {"Is Incident": 0.0, "Malicious": 0.0, "Is Important": 0.0, "Status Open": 85.71428571428571}, "results": [{"status": "Open", "name": "Autoruns", "tags": [], "last modified": "2023-11-16 12:35:26.868000+00:00", "start time": "2020-04-14 06:50:05.048000+00:00", "matching_criteria": {"entities": true, "outcome": true, "ruleGenerator": true, "port": true}, "priority": "Informative", "assigned user": "@Tier1", "matched_entities": [{"type": "HOSTNAME", "isSuspicious": false, "entity": "TIP-LONGHOSTNAM"}, {"type": "FILENAME", "isSuspicious": false, "entity": "C:\\WINDOWS\\SYSTEM32\\WSQMCONS.EXE"}, {"type": "FILEHASH", "isSuspicious": false, "entity": "3198C8F020BC60931404167EEC51E2BF"}], "start time unix": 1586847005048, "id": 97}, {"status": "Closed", "name": "Newly Executed Applications", "tags": [], "last modified": "2023-11-22 12:51:49.046000+00:00", "start time": "2020-04-14 06:50:05.125000+00:00", "matching_criteria": {"entities": true, "outcome": true, "ruleGenerator": true, "port": true}, "priority": "Informative", "assigned user": "Siemplify Admin", "matched_entities": [{"type": "HOSTNAME", "isSuspicious": false, "entity": "TIP-LONGHOSTNAM"}], "start time unix": 1586847005125, "id": 103, "case_closure_details": {"case_closed_action_type": 1, "reason": "Maintenance", "root_cause": "Other"}}]}
```



#### Create Gemini Case Summary
Create a summary of the case using Gemini AI.
Timeout - 120 Seconds



##### JSON Results
```json
{  
"next_steps": [  
"Next step1",  
"Next step2",  
"Next step3",  
"Next step4",  
"Next step5",  
"Next step6",  
"Next step7"  
],  
"reasons": [  
"Reason1",  
"Reason2",  
"Reason3",  
"Reason4",  
"Reason5",  
"Reason6",  
"Reason7"  
],  
"summary": "This is some case summary"  
}  

```



#### Get Connector Context Value
Action gets a value stored under a specified key in the Siemplify database for a connector context. Action is not working on Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Connector Identifier|Specify connector identifier to list context keys for. Parameter works together with "Connector Identifier Filter Logic" parameter|True|String||
|Key Name|Optionally specify the key name to get context value for.|True|String||
|Create Case Wall Table|If enabled, the case wall table will be created as part of action results.|False|Boolean|true|



##### JSON Results
```json
{"Value": "example_value", "Key_Name": "example_key"}
```



#### Get Scope Context Value
Action gets a value stored under a specified key in the Siemplify database. Available scopes to get context values for: Alert, Case, Global. Action is not working on Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Context Scope|Specify the Siemplify context scope to return context keys for.|True|List|Not specified|
|Key Name|Optionally specify the key name to get context value for.|True|String||
|Create Case Wall Table|If enabled, the case wall table will be created as part of action results.|False|Boolean|true|



##### JSON Results
```json
{"Value": "example_value", "Key_Name": "example_key"}
```



#### Get Case Details
This action will get all the data from a case and return a JSON result.  The result includes comments, entity information, insights, playbooks that ran, alert information and events.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Case Id|The Case ID to query.  Optional. Will use current case if empty.|False|String||
|Fields to Return|Specify a comma-separated list of fields that need to be returned. If nothing is provided, all fields are returned. Getting nested values can be done using \"Nested Keys Delimiter\" value to chain nested keys and list indexes. For example, if the delimiter is \".\": key_1.nested_key_1.0.nested_key_2, key_2, key_3.1.nested_key_1|False|String||
|Nested Keys Delimiter|The delimiter to split nested keys. If missing or not provided fetching nested keys is not possible. Cannot be a comma (\",\")|False|String|.|



##### JSON Results
```json
{"id":7,"creationTimeUnixTimeInMs":1749547533606,"modificationTimeUnixTimeInMs":1750073142090,"name":"xxxxxx","isImportant":false,"isIncident":false,"startTimeUnixTimeInMs":1749547529741,"endTimeUnixTimeInMs":1749547529741,"assignedUser":"@Tier1","description":null,"isTestCase":false,"incidentId":null,"lastModifyingUserId":"xxxxxx","createTime":1749547533606,"updateTime":1750073142090,"alertCount":1,"type":"External","overflowCase":false,"status":"Opened","score":21.0,"involvedSuspiciousEntity":false,"workflowStatus":"Completed","source":"Server","products":[],"tasks":[],"displayName":"Phishing email detector","stage":"Triage","priority":"PriorityLow","important":false,"assignee":"@Tier1","incident":false,"environment":"Default Environment","relatedAlerts":[],"tags":["aaa"],"alertCards":[{"id":10,"creationTimeUnixTimeInMs":1749547533634,"modificationTimeUnixTimeInMs":1750073142082,"identifier":"xxxxxx","status":0,"name":"SUSPICIOUS PHISHING EMAIL","priority":40,"workflowsStatus":2,"slaExpirationUnixTime":1749547833634,"slaCriticalExpirationUnixTime":1749547773634,"startTime":1749547529741,"endTime":1749547529741,"alertGroupIdentifier":"xxxxxx","eventsCount":1,"title":"SUSPICIOUS PHISHING EMAIL","ruleGenerator":"Phishing email detector","deviceProduct":"Phishing email detector","deviceVendor":"Email server","playbookAttached":"New Playbook","playbookRunCount":1,"isManualAlert":false,"sla":{"slaExpirationTime":1749547833634,"criticalExpirationTime":1749547773634,"expirationStatus":0,"remainingTimeSinceLastPause":null},"fieldsGroups":[],"sourceUrl":null,"sourceRuleUrl":null,"siemAlertId":null,"relatedCases":[],"lastSourceUpdateUnixTimeInMs":null,"nestingDepth":0,"eventCount":1,"caseId":1,"createTime":1750684686624,"updateTime":1750684686949,"product":"Windows:AccessDisabledAccounts","displayName":"ACCESS DISABLED ACCOUNTS","vendor":"Microsoft","environment":"Default Environment","ticketId":"c4db60fa-b510-414a-a462-c3f215809f96","sourceSystemName":"Microsoft CASB","manual":false,"additionalProperties":"{\"Name\":\"Access Disabled Accounts\",\"Type\":\"ALERT\",\"EndTime\":\"1750684684139\",\"Alert_Id\":\"c4db60fa-b510-414a-a462-c3f215809f96\",\"TicketId\":\"c4db60fa-b510-414a-a462-c3f215809f96\",\"DisplayId\":\"c4db60fa-b510-414a-a462-c3f215809f96\",\"StartTime\":\"1750684684139\",\"IsArtifact\":\"False\",\"IsEnriched\":\"False\",\"IsTestCase\":\"False\",\"Description\":\"Access Disabled Accounts\",\"Environment\":\"Default Environment\",\"IsSuspicious\":\"False\",\"IsVulnerable\":\"False\",\"DataAccessScope\":null,\"IsInternalAsset\":\"False\",\"AlertBaseEventIds\":\"d85ca9a7-58a7-4329-b615-ebe3dcfc6fd1\",\"EstimatedStartTime\":\"1750684684139\"}","involvedRelations":[],"sourceIdentifier":"Simulation","playbookStatus":0}],"isOverflowCase":false,"isManualCase":false,"slaExpirationUnixTime":1749547833634,"slaCriticalExpirationUnixTime":1749547773634,"stageSlaExpirationUnixTimeInMs":null,"stageSlaCriticalExpirationUnixTimeInMs":null,"canOpenIncident":false,"sla":{"slaExpirationTime":1749547833634,"criticalExpirationTime":1749547773634,"expirationStatus":0,"remainingTimeSinceLastPause":null},"stageSla":{"slaExpirationTime":null,"criticalExpirationTime":null,"expirationStatus":2,"remainingTimeSinceLastPause":null},"relatedAlertTicketId":null,"relatedAlertCards":[],"activities":[{"id":"CaseInsightDatas16","creatorUserId":"Siemplify","activityId":16,"activityType":"CaseInsight","caseId":7,"createTime":1750068343993,"updateTime":1750068343993,"alertIdentifier":"xxxxx","activityDataJson":{"TriggeredBy":"Siemplify","EntityIdentifier":"YOUR NEW SALARY NOTIFICATION","EntityData":{"CaseId":7,"AlertIdentifier":"xxxxxxx","AlertStatus":0,"Identifier":"YOUR NEW SALARY NOTIFICATION","EntityType":"EMAILSUBJECT","IsInternal":true,"IsSuspicious":false,"IsArtifact":true,"IsPivot":false,"Environment":"Default Environment","FieldsGroups":[{"Order":0,"GroupName":"Default","IsIntegration":false,"IsHighlight":false,"Items":[{"OriginalName":"Network_Priority","Name":"Network_Priority","Value":"0"},{"OriginalName":"IsSuspicious","Name":"IsSuspicious","Value":"False"},{"OriginalName":"IsAttacker","Name":"IsAttacker","Value":"False"},{"OriginalName":"IsManuallyCreated","Name":"IsManuallyCreated","Value":"False"},{"OriginalName":"Environment","Name":"Environment","Value":"Default Environment"},{"OriginalName":"Alert_Id","Name":"Alert_Id","Value":"SUSPICIOUS PHISHING EMAIL_49010AE4-29EB-4C4B-8568-C91478531A7C"},{"OriginalName":"Type","Name":"Type","Value":"EMAILSUBJECT"},{"OriginalName":"IsArtifact","Name":"IsArtifact","Value":"True"},{"OriginalName":"IsEnriched","Name":"IsEnriched","Value":"False"},{"OriginalName":"IsTestCase","Name":"IsTestCase","Value":"False"},{"OriginalName":"IsVulnerable","Name":"IsVulnerable","Value":"False"},{"OriginalName":"IsInternalAsset","Name":"IsInternalAsset","Value":"False"},{"OriginalName":"OriginalIdentifier","Name":"OriginalIdentifier","Value":"Your New Salary Notification"}]},{"Order":0,"GroupName":"Entity","IsIntegration":false,"IsHighlight":false,"Items":[{"OriginalName":"IsPivot","Name":"Is Pivot","Value":"False"}]}],"HighlightedFieldsGroups":[],"IsManuallyCreated":false,"SourceUrl":null},"Title":"Entity insight","Content":"fd","Severity":0,"InsightType":1,"AdditionalDataType":null,"AdditionalData":null,"AdditionalDataTitle":null,"AlertIdentifiers":["SUSPICIOUS PHISHING EMAIL_49010AE4-29EB-4C4B-8568-C91478531A7C"],"EntityType":"EMAILSUBJECT","CreatorUserId":null,"CreatorFullName":null,"Id":16,"Type":6,"CaseId":7,"IsFavorite":false,"ModificationTimeUnixTimeInMs":1750068343993,"CreationTimeUnixTimeInMs":1750068343993,"AlertIdentifier":"SUSPICIOUS PHISHING EMAIL_49010AE4-29EB-4C4B-8568-C91478531A7C"},"favorite":false}],"totalSize":1,"moveEnvironment":{}}
```



#### Set Custom Fields
Preview. Set values for custom fields.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Scope|The scope to set for the custom fields.|True|List|Case|
|Custom Fields Data|The values to update for the custom fields. You can update multiple custom fields in a single action run.|True|String|{"Custom Field Name 1":"Custom Field Value 1","Custom Field Name 2":"Custom Field Value 2"}|
|Append Values|If selected, the action appends the inputs from the "Custom Fields Data" parameter to the existing values of the custom fields. If not selected, the action overwrites the existing values with the inputs from the "Custom Fields Data" parameter. Not selected by default.|False|Boolean|false|



##### JSON Results
```json
{"testfreetextfield": ["Custom Field Value 1", "Custom Field Value 2"], "testlistfieldCase": ["abc"]}
```



#### Wait For Custom Fields
Preview. Wait for custom fields values to continue playbook execution.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Scope|The scope to set for the custom fields.|True|List|Case|
|Custom Fields Data|The conditions that are required for the custom fields for the action to resume running a playbook. Configure the custom field names and their required values as a JSON object.If you set conditions for multiple fields, the action waits for all fields to match their respective conditions.The action behavior depends on the input that you provide.For the action to resume running a playbook with any value in a custom field, configure an empty string for the custom field as follows:{“Custom Field”: “”}For the action to resume running a playbook when the custom field equals to a specific value (“Value 1”), specify the value for the custom field as follows:{“Custom Field”: “Value 1”}|True|String|{
    "Custom Field Name 1": "Custom Field Value 1",
    "Custom Field Name 2": ""
}|



##### JSON Results
```json
{"testfreetextfield": ["Custom Field Value 1"], "testlistfieldCase": ["abc"]}
```



#### test action

Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|password|Testing|True|Password|Default password|



##### JSON Results
```json
{}
```



#### Add to Custom List
Add an Entity Identifier to a categorized Custom List, in order to perform future comparisons in other actions.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Category|Custom list category to be used.|True|String||



#### Add Entity Insight
Add an insight configurable message to each targeted entity
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Message|Message content to be added.|True|String||



#### Add General Insight
Add a general insight configurable message to the case
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Title|The title of the insight.|True|String||
|Message|The message that will be placed on the insight.|True|String||
|Triggered By|A description for the cause of this insight|False|String||



#### Add Tags To Similar Cases
Add tags to similar cases and return their Ids
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Rule Generator|Search for similar cases by the same Rule Generator. Note: All these search criteria are joined using logical 'AND' condition and will be used in the same search.|False|Boolean||
|Port|Search for similar cases by the same Port number. Note: All these search criteria are joined using logical 'AND' condition and will be used in the same search.|False|Boolean||
|Category Outcome|Search for similar cases by the same Category Outcome. Note: All these search criteria are joined using logical 'AND' condition and will be used in the same search.|False|Boolean||
|Entity Identifier|Search for similar cases containing the same Entity Identifier. Note: All these search criteria are joined using logical 'AND' condition and will be used in the same search.|False|Boolean||
|Days Back|Defines how many days back the search should look for similar cases.|True|String||
|Tags|Specify a comma-separated list of tags that you want to add to similar cases.|True|String||



#### Assign Case
Assign case to specific user or usergroup
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Assigned User|User or Usergroup to whom a case should be assigned.|True|Users||



#### Attach Playbook to Alert
Attach a specific playbook to an alert
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Playbook Name|Playbook, which should be attached to an alert.|True|Playbook Name||
|Allow Duplicates|If selected, action will allow the same playbook to be attached multiple times to the alert.|False|Boolean|true|



#### Case Comment
Add a comment to the case the current alert has been grouped to
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Comment|Comment to be added to the case.|True|String||



#### Case Tag
Add given tag to the case the current alert is grouped to
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Tag|Tag to be added to the case.|True|String||



#### Change Alert Priority
Automatically change the alert priority to the given input. Note: This action is compatible only with Siemplify version 5.6 and higher.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Alert Priority|Priority to which the alert should be moved to.|True|Priorities||



#### Change Case Stage
Change case stage to handling
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Stage|Stage to which the case should be moved to.|True|Stages||



#### Close Alert
Closes the current alert
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Reason|Alert closure reason.|True|Case Close Reason||
|Root Cause|Root cause of the alert closure.|True|Close Case Root Cause||
|Comment|Comment content.|True|String||
|Assign To User|User that the closed case will be assigned to.|False|Users|None|
|Tags|Comma separated tags values.|False|String|None|



#### Close Case
Closes the case the current alert has been grouped to
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Reason|Closure reason.|True|Case Close Reason||
|Root Cause|Root cause of the case closure.|True|Close Case Root Cause||
|Comment|Comment content.|True|String||



#### Create Entity
Creates an entity and adds to requested alert. Note - Please make sure to read our documentation regarding the differences in the delimiter’s behavior, between different Siemplify’s platform versions 5.6.0 inclusive and 5.6.2 exclusive, here: https://cloud.google.com/chronicle/docs/soar/marketplace-integrations/siemplify#create-entity
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Entities Identifies|Entity identifier or comma-separated list of identifiers (Example: value1,value2,value3).|True|String||
|Delimiter|Provide a delimiter character, with which the action will split the input it gets into a number of entities instead of a single one. If no value will be provided, action will not perform any splitting on the input, and it will be handled as a single entity. Note - Please make sure to read our documentation regarding the differences in the delimiter's behavior, between different Siemplify's platform versions 5.6.0 inclusive and 5.6.2 exclusive.|False|String|,|
|Entity Type|Siemplify entity type. Example: HOSTNAME / USERNAME / etc.|True|Entity Type||
|Is Internal|Mark if entities are part of an internal network.|False|Boolean||
|Is Suspicious|Mark if entities are suspicious.|False|Boolean||



#### Create Or Update Entity Properties
Create\Change properties for entities in an entity scope.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Entity Field|Field that has to be created or updated.|True|String||
|Field Value|Value that has to be set to the field.|True|String||



#### Get Custom Field Values
Get current values for the custom field based on the given scope.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Scope|The scope to Get the custom fields values from.|True|List|Case|



#### Instruction
Set an instruction for the analyst
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Instruction|Instruction content.|True|String||



#### Is In Custom List
Check whether an Entity Identifier is part of a predefined dynamic categorized Custom List
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Category|Custom list category.|True|String||



#### Mark As Important
Mark case as important
Timeout - 600 Seconds



#### Open Web Url
Generate a browser link
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Title|Title for URL.|True|String||
|URL|Target URL.|True|String||



#### Pause Alert SLA
Automatically pause the alert SLA
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Message|Pause Reason|False|String||



#### Pause Case SLA
Automatically pause the Case SLA.
Note: This action is only supported from Google SecOps SOAR version 6.3.34 and higher.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Message|Pause Reason|False|String||



#### Permitted Alert Time
Check case time according to a given time condition
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Timestamp Type|Type of timestamp that will be used for comparison.|False|List|Alert Start Time|
|Permitted Start Time|Start of the timeframe, when alerts are allowed. For example: 9:55:24|True|String||
|Permitted End Time|End of the timeframe, when alerts are allowed. For example: 17:23:21|True|String||
|Monday||False|Boolean||
|Tuesday||False|Boolean||
|Wednesday||False|Boolean||
|Thursday||False|Boolean||
|Friday||False|Boolean||
|Saturday||False|Boolean||
|Sunday||False|Boolean||
|Input Timezone|Timezone name. For example: UTC. This action also supports input with IANA zones (e.q. America/New_York). If the input is provided via zones, then action also supports daylight savings.|True|String||



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Raise Incident
Raise case incident (Note - Used to mark critical true positive cases)
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Soc Role|Role to which the case should be assigned.|False|Users|@SocManager|



#### Remove from Custom List
Remove an Entity Identifier from a categorized Custom List, in order to perform future comparisons in other actions.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Category|Custom list category to be used.|True|String||



#### Remove Tag
Remove tags from a case.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Tag|Specify the tag that needs to be removed. Comma seperated values.|True|String||



#### Resume Alert SLA
Automatically resume the alert SLA
Timeout - 600 Seconds



#### Resume Case SLA
Automatically Resume the Case SLA.
Note: This action is only supported from Google SecOps SOAR version 6.3.34 and higher.
Timeout - 600 Seconds



#### Run Remote
Run remote action via publisher
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Publisher Name|Publisher instance name to be used.|True|String||
|Remote Integration Name|Remote integration name to be used.|True|String||
|Remote Action Name|Remote action name to be used.|True|String||
|Remote Context Data|Remote action context data.|True|String|None|
|Remote Action Script|Remote action script content to be executed.|True|String|None|
|Agent ID|Action's target agent id.|True|String|None|
|Installed Integrations Shared Folder|Installed Integrations Shared Folder|True|String|None|
|Verify SSL|Enables\Disables SSL Verification between Siemplify's machine and the remote Publisher|False|Boolean|None|



#### Set Alert SLA
Set the SLA for an alert. This action has the highest priority and it will override the existing SLA defined for the specific alert.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|SLA Period|The period of time after which the SLA is in breach.|True|String|5|
|SLA Time Unit|Specify the unit for SLA Time.|True|List|Minutes|
|SLA Time To Critical Period|The period of time after which the SLA enters the critical period.|True|String|4|
|SLA Time To Critical Unit|Specify the unit for SLA Time To Critical.|True|List|Minutes|



#### Set Case SLA
Set the SLA for a case. This action has the highest priority and it will override the existing SLA defined for the specific case.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|SLA Period|The period of time after which the SLA is in breach.|True|String|5|
|SLA Time Unit|Specify the unit for SLA Time.|True|List|Minutes|
|SLA Time To Critical Period|The period of time after which the SLA enters the critical period.|True|String|4|
|SLA Time To Critical Unit|Specify the unit for SLA Time To Critical.|True|List|Minutes|



#### Change Priority
Automatically change case priority to the given input
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Priority|Priority, which should be set for the case.|True|Priorities||



#### Set Risk Score
Set risk score for a SOAR case. Note: This action is only supported from Chronicle SOAR version 6.3.6 and higher.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Risk Score|Specify risk score that needs to be set.|True|String||



#### Set Scope Context Value
Action sets a value for a key specified that is stored in the Siemplify database. Available scopes to get context values for: Alert, Case, Global. Action is not working on Siemplify entities. Note: Key Name parameter is case insensitive.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Context Scope|Specify the Siemplify context scope to return context keys for.|True|List|Not specified|
|Key Name|Specify the key name to set context value for.|True|String||
|Key Value|Specify the value to store under the specified key.|True|String||



#### TestSiemplifyProxy
Test connection to a given endpoint using proxy settings configured in Siemplify.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Endpoint URL|The endpoint to try to connect to|True|String||
|HTTP Method|The HTTP method to use when connecting to the endpoint|True|String|GET|
|Body|The body of the HTTP request|False|String|GET|
|Verify SSL|Whether to verify SSL certificate or not.|False|Boolean|true|



#### Update Case Description
Ability to set Case Description from playbooks.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Description|Specify what description should be set for the case.|True|String||






## Jobs

#### Actions Monitor
Notifies of all the actions, that have individually failed at least 3 times, in the last 3 hours

#### Cases Collector DB
Collect cases and connector logs from Publisher.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Publisher Id|True|Integer||
|Verify SSL|False|Boolean|False|

#### Cases Collector
Collect cases and connector logs from Publisher.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Publisher Id|True|Integer||
|Verify SSL|False|Boolean|False|

#### Delete Case Files History
Delete case files that are older than X days from Done and Error folders of the ETL

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Days|True|Integer|10|

#### Logs Collector
Collect the log records from Publisher agents and post them to Elasticsearch.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Publisher Id|True|Integer||
|Verify SSL|False|Boolean|False|

#### Measurement Monitor
Sends an email report of various system measurement to configured admins

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Additional Email Recipients|False|Integer|Insights@siemplify.co|
|Metrics Output Folder|False|Integer||
|Max CSV Files Count Retention|False|Integer|100|



