
# SCCEnterprise

SCC Enterprise integration to set up the SCC Enterprise env

Python Version - 3


#### Dependencies
| |
|-|
|pycparser-2.22-py3-none-any.whl|
|packaging-24.2-py3-none-any.whl|
|pyOpenSSL-24.1.0-py3-none-any.whl|
|cachetools-5.5.0-py3-none-any.whl|
|importlib_metadata-8.5.0-py3-none-any.whl|
|Jinja2-3.1.2-py3-none-any.whl|
|pycryptodome-3.21.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|pyparsing-3.2.0-py3-none-any.whl|
|soupsieve-2.6-py3-none-any.whl|
|Markdown-3.7-py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|proto_plus-1.25.0-py3-none-any.whl|
|jaraco.classes-3.4.0-py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|google_auth_httplib2-0.2.0-py2.py3-none-any.whl|
|backports.tarfile-1.2.0-py3-none-any.whl|
|rsa-4.9-py3-none-any.whl|
|requests_oauthlib-2.0.0-py2.py3-none-any.whl|
|pillow-11.0.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|TIPCommon-2.2.4-py2.py3-none-any.whl|
|uritemplate-4.1.1-py2.py3-none-any.whl|
|h11-0.14.0-py3-none-any.whl|
|jaraco.functools-4.1.0-py3-none-any.whl|
|cffi-1.17.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|jaraco.context-6.0.1-py3-none-any.whl|
|requests_toolbelt-1.0.0-py2.py3-none-any.whl|
|google_auth-2.36.0-py2.py3-none-any.whl|
|keyring-25.5.0-py3-none-any.whl|
|protobuf-5.28.3-cp38-abi3-manylinux2014_x86_64.whl|
|certifi-2024.8.30-py3-none-any.whl|
|typing_extensions-4.12.2-py3-none-any.whl|
|pyasn1-0.6.1-py3-none-any.whl|
|httpx-0.27.2-py3-none-any.whl|
|pyasn1_modules-0.4.1-py3-none-any.whl|
|zipp-3.21.0-py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|defusedxml-0.7.1-py2.py3-none-any.whl|
|urllib3-1.26.15-py2.py3-none-any.whl|
|httpcore-1.0.6-py3-none-any.whl|
|cryptography-42.0.8-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|MarkupSafe-3.0.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|SecretStorage-3.3.3-py3-none-any.whl|
|google_api_core-2.23.0-py3-none-any.whl|
|jeepney-0.8.0-py3-none-any.whl|
|httplib2-0.22.0-py3-none-any.whl|
|anyio-4.6.2.post1-py3-none-any.whl|
|more_itertools-10.5.0-py3-none-any.whl|
|jira-3.2.0-py3-none-any.whl|
|oauthlib-3.2.2-py3-none-any.whl|
|beautifulsoup4-4.12.3-py3-none-any.whl|
|requests-2.28.2-py3-none-any.whl|
|idna-3.10-py3-none-any.whl|
|googleapis_common_protos-1.66.0-py2.py3-none-any.whl|
|google_api_python_client-2.152.0-py2.py3-none-any.whl|


## Actions
#### Add SCCE Tags
Add all of the SCCE metadata tags to the case.
Timeout - 600 Seconds



#### CloudEntityParser
Parse GCP related Entities from am existing alert's events data, and adds them to the alert.
Timeout - 600 Seconds



##### JSON Results
```json
{"created": {"/projects/xxxx/zones/us-central1-a/instances/xxx-xxxx": "DEPLOYMENT", "//compute.googleapis.com/projects/xxxx/zones/us-central1-a/instances/yyy-yyyy": "HOSTNAME", "//cloudresourcemanager.googleapis.com/projects/xxxx": "DEPLOYMENT"}}
```



#### Create SCC Enterprise Cloud Posture Ticket Type Jira
This action will create a new ticket type called SCC Enterprise Cloud Posture Ticket” in Jira. It’s a mandatory requirement for the “Sync SCC-Jira Tickets” job and “Posture Findings with Jira” playbook to work. Note: as a part of the process, action will create a new project SCC Enterprise Project” dedicated to SCC Enterprise.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|API root of the Jira instance.|True|String||
|Username|Username of the Jira account.|True|String||
|API Token|Password of the Jira account.|True|Password||
|Verify SSL|If enabled, verify the SSL certificate for the connection to Jira is valid.|False|Boolean|true|



##### JSON Results
```json
{"Assignee": {"self": "https://siemplify.atlassian.net/rest/api/2/user?accountId=123yyy123", "accountId": "123yyy123", "emailAddress": "xxx@google.com", "avatarUrls": {"48x48": "https://secure.gravatar.com/avatar/1dd32c1f758ff4e719d38b1aa96c5f3e?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FI-4.png", "24x24": "https://secure.gravatar.com/avatar/1dd32c1f758ff4e719d38b1aa96c5f3e?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FI-4.png", "16x16": "https://secure.gravatar.com/avatar/1dd32c1f758ff4e719d38b1aa96c5f3e?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FI-4.png", "32x32": "https://secure.gravatar.com/avatar/1dd32c1f758ff4e719d38b1aa96c5f3e?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FI-4.png"}, "displayName": "xxx", "active": true, "timeZone": "UTC", "accountType": "atlassian"}, "Reporter": {"self": "https://siemplify.atlassian.net/rest/api/2/user?accountId=123yyy123", "accountId": "123yyy123", "emailAddress": "xxx@google.com", "avatarUrls": {"48x48": "https://secure.gravatar.com/avatar/1dd32c1f758ff4e719d38b1aa96c5f3e?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FI-4.png", "24x24": "https://secure.gravatar.com/avatar/1dd32c1f758ff4e719d38b1aa96c5f3e?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FI-4.png", "16x16": "https://secure.gravatar.com/avatar/1dd32c1f758ff4e719d38b1aa96c5f3e?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FI-4.png", "32x32": "https://secure.gravatar.com/avatar/1dd32c1f758ff4e719d38b1aa96c5f3e?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FI-4.png"}, "displayName": "xxx", "active": true, "timeZone": "UTC", "accountType": "atlassian"}, "Summary": "Posture Test Ticket", "Description": "This is a test SCC Enterprise Cloud Posture Ticket generated with SCC Enterprise - Create SCC Enterprise Cloud Posture Ticket Type Jira action.", "Severity": {"self": "https://siemplify.atlassian.net/rest/api/2/customFieldOption/10042", "value": "Info", "id": "10042"}, "Cloud Environment": {"self": "https://siemplify.atlassian.net/rest/api/2/customFieldOption/10048", "value": "Other", "id": "10048"}, "Due date": "2024-01-02", "Issue Type": {"self": "https://siemplify.atlassian.net/rest/api/2/issuetype/10025", "id": "10025", "description": "This ticket type is used by SOAR to sync your SCC findings, SOAR cases and Jira issues.", "iconUrl": "https://siemplify.atlassian.net/rest/api/2/universal_avatar/view/type/issuetype/avatar/10300?size=medium", "name": "SCC Enterprise Cloud Posture Ticket Test", "subtask": false, "avatarId": 10300, "hierarchyLevel": 0}, "Project": {"self": "https://siemplify.atlassian.net/rest/api/2/project/10007", "id": "10007", "key": "SCC Enterprise", "name": "SCC Enterprise Project Test", "projectTypeKey": "software", "simplified": false, "avatarUrls": {"48x48": "https://siemplify.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10421", "24x24": "https://siemplify.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10421?size=small", "16x16": "https://siemplify.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10421?size=xsmall", "32x32": "https://siemplify.atlassian.net/rest/api/2/universal_avatar/view/type/project/avatar/10421?size=medium"}}, "statuscategorychangedate": "2024-01-16T16:23:46.640+0000", "Parent Type": null, "timespent": null, "Vulnerability Impact": null, "customfield_10030": null, "Finding Class": null, "customfield_10031": null, "customfield_10032": null, "fixVersions": [], "aggregatetimespent": null, "Affected Organization": null, "resolution": null, "customfield_10027": null, "customfield_10028": null, "customfield_10029": null, "resolutiondate": null, "workratio": -1, "watches": {"self": "https://siemplify.atlassian.net/rest/api/2/issue/SCCEnterprise-1/watchers", "watchCount": 1, "isWatching": true}, "lastViewed": null, "issuerestriction": {"issuerestrictions": {}, "shouldDisplay": false}, "created": "2024-01-16T16:23:46.258+0000", "Vulnerability Exploitation Activity": null, "customfield_10020": null, "customfield_10021": null, "Finding Count": null, "customfield_10022": null, "Priority": {"self": "https://siemplify.atlassian.net/rest/api/2/priority/4", "iconUrl": "https://siemplify.atlassian.net/images/icons/priorities/low.svg", "name": "Low", "id": "4"}, "Vulnerability Was Zero Day": null, "customfield_10023": null, "Vulnerability Observed in the Wild": null, "customfield_10024": null, "customfield_10025": null, "labels": [], "customfield_10016": null, "customfield_10017": null, "customfield_10018": {"hasEpicLinkFieldDependency": false, "showField": false, "nonEditableReason": {"reason": "PLUGIN_LICENSE_ERROR", "message": "The Parent Link is only available to Jira Premium users."}}, "customfield_10019": "0|i000on:", "aggregatetimeoriginalestimate": null, "timeestimate": null, "versions": [], "issuelinks": [], "updated": "2024-01-16T16:23:46.382+0000", "status": {"self": "https://siemplify.atlassian.net/rest/api/2/status/1", "description": "", "iconUrl": "https://siemplify.atlassian.net/images/icons/statuses/open.png", "name": "Open", "id": "1", "statusCategory": {"self": "https://siemplify.atlassian.net/rest/api/2/statuscategory/2", "id": 2, "key": "new", "colorName": "blue-gray", "name": "To Do"}}, "components": [], "timeoriginalestimate": null, "customfield_10010": null, "customfield_10014": null, "Source Link": null, "timetracking": {}, "customfield_10015": null, "customfield_10005": null, "customfield_10006": null, "customfield_10007": null, "security": null, "customfield_10008": null, "customfield_10009": null, "attachment": [], "aggregatetimeestimate": null, "creator": {"self": "https://siemplify.atlassian.net/rest/api/2/user?accountId=123yyy123", "accountId": "123yyy123", "emailAddress": "xxx@google.com", "avatarUrls": {"48x48": "https://secure.gravatar.com/avatar/1dd32c1f758ff4e719d38b1aa96c5f3e?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FI-4.png", "24x24": "https://secure.gravatar.com/avatar/1dd32c1f758ff4e719d38b1aa96c5f3e?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FI-4.png", "16x16": "https://secure.gravatar.com/avatar/1dd32c1f758ff4e719d38b1aa96c5f3e?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FI-4.png", "32x32": "https://secure.gravatar.com/avatar/1dd32c1f758ff4e719d38b1aa96c5f3e?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FI-4.png"}, "displayName": "xxx", "active": true, "timeZone": "UTC", "accountType": "atlassian"}, "Affected Azure Resource Group": null, "Affected Azure Subscription": null, "Finding Category": null, "subtasks": [], "Affected Resource Types": null, "Affected AWS Account": null, "Affected Projects": null, "aggregateprogress": {"progress": 0, "total": 0}, "customfield_10001": null, "customfield_10002": null, "customfield_10003": null, "customfield_10004": null, "environment": null, "progress": {"progress": 0, "total": 0}, "comment": {"comments": [], "self": "https://siemplify.atlassian.net/rest/api/2/issue/10114/comment", "maxResults": 0, "total": 0, "startAt": 0}, "votes": {"self": "https://siemplify.atlassian.net/rest/api/2/issue/SCCEnterprise-1/votes", "votes": 0, "hasVoted": false}, "worklog": {"startAt": 0, "maxResults": 20, "total": 0, "worklogs": []}, "expand": "renderedFields,names,schema,operations,editmeta,changelog,versionedRepresentations,customfield_10010.requestTypePractice", "id": "10114", "self": "https://siemplify.atlassian.net/rest/api/2/issue/10114", "key": "SCCEnterprise-1"}
```



#### Create SCC Enterprise Cloud Posture Ticket Type SNOW
This action will create a new ticket type called "SCC Enterprise Cloud Posture Ticket" in ServiceNow. It’s a mandatory requirement for the "Sync SCC-ServiceNow Tickets" job and "Posture Findings with SNOW" playbook to work.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|API root of the ServiceNow instance.|True|String|https://{dev-instance}.service-now.com/api/now/v1/|
|Username|Username of the ServiceNow account.|True|String||
|Password|Password of the ServiceNow account.|True|Password||
|Verify SSL|If enabled, verify the SSL certificate for the connection to the ServiceNow is valid.|False|Boolean|true|
|Table Role|Specify the role that should be set to access the newly created table. If nothing is provided, action will create a new role "u_scc_enterprise_cloud_posture_ticket_user".|False|String|u_scc_enterprise_cloud_posture_ticket_user|



##### JSON Results
```json
{  
  "u_vulnerability_was_zero_day": "",  
  "u_due_date": "2023-10-26 14:51:39",  
  "u_chronicle_sec_ops_link": "",  
  "u_affected_projects": "",  
  "u_cloud_environment": "Google Cloud",  
  "sys_updated_on": "2023-11-09 14:51:39",  
  "u_overview": "",  
  "u_ticket_name": "Posture Test Ticket",  
  "u_affected_azure_subscription": "",  
  "u_priority": "Low",  
  "sys_id": "656c65db2f52311046dffe1df699b6e2",  
  "sys_updated_by": "admin",  
  "u_severity": "Info",  
  "sys_created_on": "2023-11-09 14:51:39",  
  "u_vulnerability_exploitation_activity": "",  
  "u_vulnerability_observed_in_the_wild": "",  
  "u_additional_comments": "",  
  "u_affected_organization": "",  
  "u_finding_count": "",  
  "u_status": "Open",  
  "u_finding_category": "",  
  "sys_created_by": "admin",  
  "u_assigned_to": {  
    "link": "https://dev69305.service-now.com/api/now/table/sys_user/6816f79cc0a8016401c5a33be04be441",  
    "value": "6816f79cc0a8016401c5a33be04be441"  
  },  
  "sys_mod_count": "0",  
  "u_finding_class": "",  
  "u_source_link": "",  
  "sys_tags": "",  
  "u_affected_resource_types": "",  
  "u_affected_azure_resource_group": "",  
  "u_affected_aws_account": "",  
  "u_comments": "",  
  "u_parent_type": "",  
  "u_vulnerability_impact": ""  
}
```



#### Lock Playbook
This action will enforce only one playbook being executed for given Posture case.
Timeout - 600 Seconds



##### JSON Results
```json
{}
```



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Prepare Description
Prepare description for ITSM ticket.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Output||False|List|HTML|



##### JSON Results
```json
{"description": "<!DOCTYPE html>\n<html lang=\"en\">\nEscaped HTML\n</html>", "unescaped_description": "<!DOCTYPE html> <html lang=\"en\">Unescaped HTML</html>"}
```



#### Set SCC-FINDINGS-STATE Context Value
Set "SCC-FINDINGS-STATE" context value that is used by the "Sync SCC Data" job, action "Prepare Description" and ITSM jobs.
Timeout - 600 Seconds



##### JSON Results
```json
[  
  {  
    "finding_id": "organizations/000000000001/sources/18312063075767669755/findings/50bf0151aaeee97ad43aff66330466b9",  
    "status": "ACTIVE",  
    "aps_score": 6.0,  
    "resource_name": "//compute.googleapis.com/projects/sample-project/zones/us-central1-a/instances/xxx"  
  },  
  {  
    "finding_id": "organizations/000000000001/sources/18312063075767669755/findings/20200250613386afb0e795b02faa86b8",  
    "status": "ACTIVE",  
    "aps_score": null,  
    "resource_name": "//compute.googleapis.com/projects/sample-project/zones/us-central1-a/instances/xxx"  
  },  
  {  
    "finding_id": "organizations/000000000001/sources/18312063075767669755/findings/4e41c11fa3002aa6593c9e2b2950ecc1",  
    "status": "INACTIVE",  
    "aps_score": 1.0,  
    "resource_name": "//compute.googleapis.com/projects/sample-project/zones/us-central1-a/instances/xxx"  
  }  
]
```






## Jobs

#### Sync SCC Data
This job will synchronize Google Security Command Center based cases created by the "Urgent Posture Findings Connector".

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Environment Name|True|String|Default Environment|
|API Root|True|String|https://securitycenter.googleapis.com|
|Organization ID|True|String||
|Location ID|False|String|global|
|PubSub Project ID|False|String||
|Quota Project ID|False|String||
|User Service Account|False|Password||
|Workload Identity Email|False|String||
|Max Hours Backwards|True|Integer|24|
|Verify SSL|False|Boolean|true|

#### Sync SCC-Jira Tickets
This job will synchronize tickets in the Jira and Chronicle SOAR case. As a part of synchronization the job will work with comments and status of Chronicle SOAR cases.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Environment|True|String|Default Environment|
|API Root|True|String|https://{jira_address}|
|Username|True|String||
|API Token|True|Password||
|Max Hours Backwards|True|Integer|24|
|Verify SSL|False|Boolean|true|

#### Sync SCC-ServiceNow Tickets
This job will synchronize tickets in the ServiceNow and Chronicle SOAR case. As a part of synchronization the job will work with comments and status of Chronicle SOAR cases.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Environment|True|String|Default Environment|
|Time Format|True|String|%Y-%m-%d %H:%M:%S|
|API Root|True|String|https://{dev-instance}.service-now.com/api/now/v1/|
|Username|True|String||
|Password|True|Password||
|Max Hours Backwards|True|String|24|
|Verify SSL|False|Boolean|true|



## Connectors
#### SCC Enterprise - Urgent Posture Findings Connector
Pull information about urgent posture findings in Google Security Command Center.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|Enter the source field name in order to retrieve the Product Field name.|True|String|findingClass|
|EventClassId|Enter the source field name in order to retrieve the Event Field name.|True|String|category|
|Environment Field Name|Describes the name of the field where the environment name is stored.If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field.Default is .* to catch all and return the value unchanged.Used to allow the user to manipulate the environment field via regex logic.If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|PythonProcessTimeout|Timeout limit for the python process running the current script.|True|Integer|60|
|API Root|API root of the Google Security Command Center instance.|True|String|https://securitycenter.googleapis.com|
|Organization ID|ID of the organization that should be used in Google Security Command Center integration.|True|String||
|Location ID|ID of the location that should be used in Google Security Command Center integration. Defaults to ‘global’|False|String|global|
|PubSub Project ID|ID of the project that will be used in the integration to host the Pub/Sub Topic and Subscription connection.|False|String||
|Quota Project ID|ID of your Google Cloud project for Google Cloud API usage and billing. If no value is provided, the project ID defined in your Google Cloud service account is used. For this parameter to work, make sure to grant the “Service Usage Consumer” IAM role to your Google Cloud service account.|False|String||
|User Service Account|Service Account that is used for authentication. If both this and "Workload Identity Email" not provided, the default Service Account of the SecOps Instance will be used to authenticate.|False|Password||
|Workload Identity Email|A Service Account Client Email to replace the usage of "User's Service Account", which will be used for Impersonation. Note that the SOAR Service Account must be granted the "Service Account Token Creator" IAM role on the User Service Account. If both this and "User's Service Account" not provided, the default Service Account of the SecOps Instance will be used to authenticate.|False|String||
|Owner Tag Name|Name of the tag that contains information about the owner of the finding.|False|String|Owner Name|
|Fallback Owner|Email address of the owner of the alerts created by this connector.|True|String||
|Group By GCP Project|If enabled, the connector will group findings by project.|False|Boolean|true|
|Group By AWS Account|If enabled, the connector will group findings by AWS account.|False|Boolean|true|
|Group By Azure Subscription|If enabled, the connector will group findings by Azure subscription.|False|Boolean|true|
|Group By Severity|If enabled, the connector will group findings by severity.|False|Boolean|true|
|Group By Asset Type|If enabled, the connector will group findings by asset type.|False|Boolean|true|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Google Security Command Center server is valid.|False|Boolean|true|
|Disable Overflow|If enabled, the connector will disable the overflow mechanism.|False|Boolean|true|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password||




