<p align="center"><img src="./Resources/Jira.svg" 
     alt="Jira" width="200"/></p>

# Jira

Jira Software is part of a family of products designed to help teams of all types manage work. Originally, Jira was designed as a bug and issue tracker. But today, Jira has evolved into a powerful work management tool for all kinds of use cases, from requirements and test case management to agile software development. Jira will be the perfect fit for: requirements & test case management, agile teams, project management teams, software development teams, product management teams, task management, bug tracking and much more...

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Root|None|True|String|https://{jira_address}|
|Username|None|True|String|None|
|Api Token|None|True|Password|None|
|Verify SSL|None|False|Boolean|False|


#### Dependencies
| |
|-|
|cachetools-5.5.0-py3-none-any.whl|
|cryptography-43.0.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|rsa-4.9-py3-none-any.whl|
|requests-2.32.3-py3-none-any.whl|
|pycparser-2.22-py3-none-any.whl|
|cffi-1.17.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|pyasn1-0.6.0-py2.py3-none-any.whl|
|jira-3.8.0-py3-none-any.whl|
|google_auth-2.34.0-py2.py3-none-any.whl|
|packaging-24.1-py3-none-any.whl|
|SecretStorage-3.3.3-py3-none-any.whl|
|pyasn1_modules-0.4.0-py3-none-any.whl|
|jeepney-0.8.0-py3-none-any.whl|
|oauthlib-3.2.2-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|requests_toolbelt-1.0.0-py2.py3-none-any.whl|
|argparse-1.4.0-py2.py3-none-any.whl|
|typing_extensions-4.12.2-py3-none-any.whl|
|pillow-10.4.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|EnvironmentCommon-1.0.1-py2.py3-none-any.whl|
|idna-3.7-py3-none-any.whl|
|requests_oauthlib-2.0.0-py2.py3-none-any.whl|
|certifi-2024.7.4-py3-none-any.whl|
|pbr-6.0.0-py2.py3-none-any.whl|
|defusedxml-0.7.1-py2.py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|my_test_package-0.1.1.tar.gz|
|TIPCommon-1.1.2.2-py2.py3-none-any.whl|


## Actions
#### Copy of Ping
Test Connectivity
Timeout - 600 Seconds



##### JSON Results
```json
None
```



#### Add Comment
Add a comment to a issue
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Issue Key|The issue key of the issue, i.e: ABC-123|True|String||
|Comment|The comment content to add to the issue|True|String||



#### Assign Issue
Assign an issue to a specific user. (Jira username could be: name, mail, etc...). For new Jira Api, action will try to find a match for the assignee to assign an issue based on User email or displayName field.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Issue Key|The issue key of the issue|True|String||
|Assignee|The new assignee of the issue. Assignee can be jira username.|True|String||
|Jira Username|The Jira username of the initiator of the action. Note: If a username is not provided, action will not create a comment in the issue|False|String||



#### Create Alert Issue
Create an alert issue
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Project Key|The key of the project to create the issue in|True|String||
|Summary|The summary of the issue|True|String||
|Issue Type|The type of the issue|True|String||



##### JSON Results
```json
{"comment": {"total": 0, "startAt": 0, "comments": [], "maxResults": 0}, "creator": {"displayName": "user1", "name": "user1", "self": "", "avatarUrls": {"24x24": "", "16x16": "", "48x48": "", "32x32": ""}, "emailAddress": "john_doe@example.com", "key": "user1user", "active": true, "timeZone": "Asia/Jerusalem", "accountId": "0"}, "aggregatetimeestimate": null, "labels": ["Label1"], "aggregatetimespent": null, "watches": {"self": "", "watchCount": 1, "isWatching": false}, "assignee": {"displayName": "user2", "name": "user2", "self": "", "avatarUrls": {"24x24": "", "16x16": "", "48x48": "", "32x32": ""}, "emailAddress": "john_doe@example.com", "key": "user2", "active": true, "timeZone": "Asia/Jerusalem", "accountId": ""}, "lastViewed": "2019-01-22T10:14:02.910+0200", "issuelinks": [], "worklog": {"worklogs": [], "total": 0, "startAt": 0, "maxResults": 20}, "aggregateprogress": {"progress": 0, "total": 0}, "priority": {"iconUrl": "", "self": "", "name": "Medium", "id": "3"}, "votes": {"hasVoted": false, "self": "", "votes": 0}, "workratio": -1, "fixVersions": [], "environment": null, "timespent": null, "attachment": [{"mimeType": "binary/octet-stream", "created": "2018-06-19T15:23:07.369+0300", "self": "", "author": {"displayName": "user1", "name": "user1", "self": "", "avatarUrls": {"24x24": "", "16x16": "", "48x48": "", "32x32": ""}, "emailAddress": "john_doe@example.com", "key": "user1", "active": true, "timeZone": "Asia/Jerusalem", "accountId": "0"}, "filename": "file.rar", "content": "", "id": "0", "size": 0}], "progress": {"progress": 0, "total": 0}, "duedate": null, "status": {"statusCategory": {"name": "Done", "self": "", "id": 3, "key": "done", "colorName": "green"}, "description": "", "self": "", "iconUrl": "", "id": "0", "name": "DONE"}, "updated": "2018-09-18T10:02:06.347+0300", "subtasks": [], "description": "Create Enrich entites action using Insights API (IOC search)\n\nWrite connector for laerts\n\nIn a couple of days we will have access to an instance", "reporter": {"displayName": "user1", "name": "user1", "self": "", "avatarUrls": {"24x24": "", "16x16": "", "48x48": "", "32x32": ""}, "emailAddress": "john_doe@example.com", "key": "user1", "active": true, "timeZone": "Asia/Jerusalem", "accountId": "0"}, "timeoriginalestimate": null, "aggregatetimeoriginalestimate": null, "created": "2018-06-19T15:23:13.701+0300", "versions": [], "resolutiondate": "2018-09-18T10:02:06.340+0300", "summary": "Sample issue", "project": {"name": "Project 1", "self": "", "projectTypeKey": "software", "avatarUrls": {"24x24": "", "16x16": "", "48x48": "", "32x32": ""}, "key": "PR", "id": "0"}, "timetracking": {}, "components": [], "issuetype": {"name": "Task", "self": "", "iconUrl": "", "subtask": false, "avatarId": 10318, "id": "10002", "description": "A task that needs to be done."}, "security": null, "resolution": {"id": "10000", "self": "", "description": "Work has been completed on this issue.", "name": "Done"}, "timeestimate": null}
```



#### Create Issue
Create an issue in a project. (Jira username could be: name, mail, etc...). For new Jira Api, action will try to find a match for the assignee to assign an issue based on User email or displayName field.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Issue Type|The type of the issue|True|String||
|Project Key|The key of the project to create an issue in|True|String||
|Summary|The summary of the issue|True|String||
|Description|The description of the issue|False|String||
|Jira Username|The Jira username of the initiator of the action. Note: If a username is not provided, action will not create a comment in the issue|False|String||
|Assignee|The new assignee of the issue.|False|String||
|Components|The Components field of the issue. Parameter accepts multiple values as a comma separated string.|False|String||
|Labels|The Labels field of the issue. Parameter accepts multiple values as a comma separated string.|False|String||
|Custom Fields|Specify a JSON object containing all of the fields and values that will be used during issue creation. Note: this parameter has priority and all of the fields will be overwritten with the value that is provided for this parameter. Example: {"field":"value"}|False|String||



##### JSON Results
```json
{"comment": {"total": 0, "startAt": 0, "comments": [], "maxResults": 0}, "creator": {"displayName": "user1", "name": "user1", "self": "", "avatarUrls": {"24x24": "", "16x16": "", "48x48": "", "32x32": ""}, "emailAddress": "john_doe@example.com", "key": "user1user", "active": true, "timeZone": "Asia/Jerusalem", "accountId": "0"}, "aggregatetimeestimate": null, "labels": ["Label1"], "aggregatetimespent": null, "watches": {"self": "", "watchCount": 1, "isWatching": false}, "assignee": {"displayName": "user2", "name": "user2", "self": "", "avatarUrls": {"24x24": "", "16x16": "", "48x48": "", "32x32": ""}, "emailAddress": "john_doe@example.com", "key": "user2", "active": true, "timeZone": "Asia/Jerusalem", "accountId": ""}, "lastViewed": "2019-01-22T10:14:02.910+0200", "issuelinks": [], "worklog": {"worklogs": [], "total": 0, "startAt": 0, "maxResults": 20}, "aggregateprogress": {"progress": 0, "total": 0}, "priority": {"iconUrl": "", "self": "", "name": "Medium", "id": "3"}, "votes": {"hasVoted": false, "self": "", "votes": 0}, "workratio": -1, "fixVersions": [], "environment": null, "timespent": null, "attachment": [{"mimeType": "binary/octet-stream", "created": "2018-06-19T15:23:07.369+0300", "self": "", "author": {"displayName": "user1", "name": "user1", "self": "", "avatarUrls": {"24x24": "", "16x16": "", "48x48": "", "32x32": ""}, "emailAddress": "john_doe@example.com", "key": "user1", "active": true, "timeZone": "Asia/Jerusalem", "accountId": "0"}, "filename": "file.rar", "content": "", "id": "0", "size": 0}], "progress": {"progress": 0, "total": 0}, "duedate": null, "status": {"statusCategory": {"name": "Done", "self": "", "id": 3, "key": "done", "colorName": "green"}, "description": "", "self": "", "iconUrl": "", "id": "0", "name": "DONE"}, "updated": "2018-09-18T10:02:06.347+0300", "subtasks": [], "description": "Create Enrich entites action using Insights API (IOC search)\n\nWrite connector for laerts\n\nIn a couple of days we will have access to an instance", "reporter": {"displayName": "user1", "name": "user1", "self": "", "avatarUrls": {"24x24": "", "16x16": "", "48x48": "", "32x32": ""}, "emailAddress": "john_doe@example.com", "key": "user1", "active": true, "timeZone": "Asia/Jerusalem", "accountId": "0"}, "timeoriginalestimate": null, "aggregatetimeoriginalestimate": null, "created": "2018-06-19T15:23:13.701+0300", "versions": [], "resolutiondate": "2018-09-18T10:02:06.340+0300", "summary": "Sample issue", "project": {"name": "Project 1", "self": "", "projectTypeKey": "software", "avatarUrls": {"24x24": "", "16x16": "", "48x48": "", "32x32": ""}, "key": "PR", "id": "0"}, "timetracking": {}, "components": [], "issuetype": {"name": "Task", "self": "", "iconUrl": "", "subtask": false, "avatarId": 10318, "id": "10002", "description": "A task that needs to be done."}, "security": null, "resolution": {"id": "10000", "self": "", "description": "Work has been completed on this issue.", "name": "Done"}, "timeestimate": null}
```



#### Delete Issue
Delete an issue
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Issue Key|The key of the issue to delete|True|String||



#### Download Attachments
Get an Issue key and download all attachments. If one of them is an EML file, download inside attachments as well
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Issue Key|The key of the issue|True|String||
|Download Path|Specify the path for the downloaded file. Note: if parameter 'Download Attachments to the Case Wall' is enabled, then this parameter is not mandatory.|False|String||
|Download Attachments to the Case Wall|If enabled, action download Jira issue attachmnets to the current Siemplify alert case wall.|False|Boolean|False|



##### JSON Results
```json
[  {  "download_path": "abc/File.eml",  "attachment_details": {  "self": "https://xxxx.atlassian.net/rest/api/2/attachment/10007",  "id": "10007",  "filename": "File.eml",  "author": {  "self": "https://xxxx.atlassian.net/rest/api/2/user?accountId=712020%3A2334c2cc-7387-42ac-9e5f-b0156b4469fa",  "accountId": "712020:2334c2cc-7387-42ac-9e5f-b0156b4469fa",  "emailAddress": "xxxx@google.com",  "avatarUrls": {  "48x48": "https://secure.gravatar.com/avatar/8111be18f7732b359b9c7d09e8459e45?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FRK-4.png",  "24x24": "https://secure.gravatar.com/avatar/8111be18f7732b359b9c7d09e8459e45?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FRK-4.png",  "16x16": "https://secure.gravatar.com/avatar/8111be18f7732b359b9c7d09e8459e45?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FRK-4.png",  "32x32": "https://secure.gravatar.com/avatar/8111be18f7732b359b9c7d09e8459e45?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FRK-4.png"  },  "displayName": "xxx yyy",  "active": true,  "timeZone": "Asia/Calcutta",  "accountType": "atlassian"  },  "created": "2023-05-25T20:27:09.066+0530",  "size": 12049140,  "mimeType": "message/rfc822",  "content": "https://xxxx.atlassian.net/rest/api/2/attachment/content/10007"  }  },  {  "download_path": "abc/Text_File_1.txt",  "attachment_details": {  "self": "https://xxxx.atlassian.net/rest/api/2/attachment/10005",  "id": "10005",  "filename": "Text_File_1.txt",  "author": {  "self": "https://xxxx.atlassian.net/rest/api/2/user?accountId=712020%3A2334c2cc-7387-42ac-9e5f-b0156b4469fa",  "accountId": "712020:2334c2cc-7387-42ac-9e5f-b0156b4469fa",  "emailAddress": "xxxx@google.com",  "avatarUrls": {  "48x48": "https://secure.gravatar.com/avatar/8111be18f7732b359b9c7d09e8459e45?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FRK-4.png",  "24x24": "https://secure.gravatar.com/avatar/8111be18f7732b359b9c7d09e8459e45?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FRK-4.png",  "16x16": "https://secure.gravatar.com/avatar/8111be18f7732b359b9c7d09e8459e45?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FRK-4.png",  "32x32": "https://secure.gravatar.com/avatar/8111be18f7732b359b9c7d09e8459e45?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FRK-4.png"  },  "displayName": "Rahul Kumbhar",  "active": true,  "timeZone": "Asia/Calcutta",  "accountType": "atlassian"  },  "created": "2023-05-16T11:48:24.141+0530",  "size": 43,  "mimeType": "text/plain",  "content": "https://xxxx.atlassian.net/rest/api/2/attachment/content/10005"  }  },  {  "download_path": "abc/Text_File.txt",  "attachment_details": {  "self": "https://xxxx.atlassian.net/rest/api/2/attachment/10004",  "id": "10004",  "filename": "Text_File.txt",  "author": {  "self": "https://xxxx.atlassian.net/rest/api/2/user?accountId=712020%3A2334c2cc-7387-42ac-9e5f-b0156b4469fa",  "accountId": "712020:2334c2cc-7387-42ac-9e5f-b0156b4469fa",  "emailAddress": "xxxx@google.com",  "avatarUrls": {  "48x48": "https://secure.gravatar.com/avatar/8111be18f7732b359b9c7d09e8459e45?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FRK-4.png",  "24x24": "https://secure.gravatar.com/avatar/8111be18f7732b359b9c7d09e8459e45?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FRK-4.png",  "16x16": "https://secure.gravatar.com/avatar/8111be18f7732b359b9c7d09e8459e45?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FRK-4.png",  "32x32": "https://secure.gravatar.com/avatar/8111be18f7732b359b9c7d09e8459e45?d=https%3A%2F%2Favatar-management--avatars.us-west-2.prod.public.atl-paas.net%2Finitials%2FRK-4.png"  },  "displayName": "Rahul Kumbhar",  "active": true,  "timeZone": "Asia/Calcutta",  "accountType": "atlassian"  },  "created": "2023-05-16T11:10:39.716+0530",  "size": 24,  "mimeType": "text/plain",  "content": "https://xxxx.atlassian.net/rest/api/2/attachment/content/10004"  }  } ]
```



#### Get Issues
Get issues details by keys. (separated by comma)
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Issue Keys|The keys of the issues to fetch. separated by comma|True|String||



##### JSON Results
```json
[{"issuetype":{"self":"https://xxx.xx.xx.xx:xxx/rest/api/2/issuetype/10004","id":"10004","description":"","iconUrl":"https://xxx.xx.xx.xx:xxx/secure/viewavatar?size=xsmall&avatarId=10303&avatarType=issuetype","name":"Bogue","subtask":false,"avatarId":10303},"components":[],"timespent":null,"timeoriginalestimate":null,"description":null,"project":{"self":"https://xxx.xx.xx.xx:xxx/rest/api/2/project/10000","id":"10000","key":"TES","name":"test-project1","projectTypeKey":"software","avatarUrls":{"48x48":"https://xxx.xx.xx.xx:xxx/secure/projectavatar?avatarId=10324","24x24":"https://xxx.xx.xx.xx:xxx/secure/projectavatar?size=small&avatarId=10324","16x16":"https://xxx.xx.xx.xx:xxx/secure/projectavatar?size=xsmall&avatarId=10324","32x32":"https://xxx.xx.xx.xx:xxx/secure/projectavatar?size=medium&avatarId=10324"}},"fixVersions":[],"aggregatetimespent":null,"resolution":{"self":"https://xxx.xx.xx.xx:xxx/rest/api/2/resolution/10000","id":"10000","description":"Ce ticket a été traité.","name":"Terminé"},"timetracking":{},"archiveddate":null,"attachment":[],"aggregatetimeestimate":null,"resolutiondate":"2021-11-11T12:06:31.519+0000","workratio":-1,"summary":"New summary","lastViewed":"2021-11-11T08:23:31.008+0000","watches":{"self":"https://xxx.xx.xx.xx:xxx/rest/api/2/issue/TES-65/watchers","watchCount":1,"isWatching":true},"creator":{"self":"https://xxx.xx.xx.xx:xxx/rest/api/2/user?username=admin","name":"admin","key":"xxxxx","emailAddress":"admin@siemplifylab.local","avatarUrls":{"48x48":"https://www.gravatar.com/avatar/29b93653324514469f10298493b25289?d=mm&s=48","24x24":"https://www.gravatar.com/avatar/29b93653324514469f10298493b25289?d=mm&s=24","16x16":"https://www.gravatar.com/avatar/29b93653324514469f10298493b25289?d=mm&s=16","32x32":"https://www.gravatar.com/avatar/29b93653324514469f10298493b25289?d=mm&s=32"},"displayName":"admin@siemplifylab.local","active":true,"timeZone":"Asia/Jerusalem"},"subtasks":[],"created":"2021-08-31T12:15:22.089+0000","reporter":{"self":"https://xxx.xx.xx.xx:xxx/rest/api/2/user?username=admin","name":"admin","key":"xxxxx","emailAddress":"admin@siemplifylab.local","avatarUrls":{"48x48":"https://www.gravatar.com/avatar/29b93653324514469f10298493b25289?d=mm&s=48","24x24":"https://www.gravatar.com/avatar/29b93653324514469f10298493b25289?d=mm&s=24","16x16":"https://www.gravatar.com/avatar/29b93653324514469f10298493b25289?d=mm&s=16","32x32":"https://www.gravatar.com/avatar/29b93653324514469f10298493b25289?d=mm&s=32"},"displayName":"admin@siemplifylab.local","active":true,"timeZone":"Asia/Jerusalem"},"customfield_10000":"{summaryBean=com.atlassian.jira.plugin.devstatus.rest.SummaryBean@19c9f82a[summary={pullrequest=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@3da0a0a[overall=PullRequestOverallBean{stateCount=0, state='OPEN', details=PullRequestOverallDetails{openCount=0, mergedCount=0, declinedCount=0}},byInstanceType={}], build=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@369dd644[overall=com.atlassian.jira.plugin.devstatus.summary.beans.BuildOverallBean@65c400c7[failedBuildCount=0,successfulBuildCount=0,unknownBuildCount=0,count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], review=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@73d51b7d[overall=com.atlassian.jira.plugin.devstatus.summary.beans.ReviewsOverallBean@83b0ad3[stateCount=0,state=<null>,dueDate=<null>,overDue=false,count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], deployment-environment=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@50ccd266[overall=com.atlassian.jira.plugin.devstatus.summary.beans.DeploymentOverallBean@15cb3280[topEnvironments=[],showProjects=false,successfulCount=0,count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], repository=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@4e9ecdb7[overall=com.atlassian.jira.plugin.devstatus.summary.beans.CommitOverallBean@1e233b25[count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}], branch=com.atlassian.jira.plugin.devstatus.rest.SummaryItemBean@28ca9565[overall=com.atlassian.jira.plugin.devstatus.summary.beans.BranchOverallBean@64d9fdce[count=0,lastUpdated=<null>,lastUpdatedTimestamp=<null>],byInstanceType={}]},errors=[],configErrors=[]], devSummaryJson={\"cachedValue\":{\"errors\":[],\"configErrors\":[],\"summary\":{\"pullrequest\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"stateCount\":0,\"state\":\"OPEN\",\"details\":{\"openCount\":0,\"mergedCount\":0,\"declinedCount\":0,\"total\":0},\"open\":true},\"byInstanceType\":{}},\"build\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"failedBuildCount\":0,\"successfulBuildCount\":0,\"unknownBuildCount\":0},\"byInstanceType\":{}},\"review\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"stateCount\":0,\"state\":null,\"dueDate\":null,\"overDue\":false,\"completed\":false},\"byInstanceType\":{}},\"deployment-environment\":{\"overall\":{\"count\":0,\"lastUpdated\":null,\"topEnvironments\":[],\"showProjects\":false,\"successfulCount\":0},\"byInstanceType\":{}},\"repository\":{\"overall\":{\"count\":0,\"lastUpdated\":null},\"byInstanceType\":{}},\"branch\":{\"overall\":{\"count\":0,\"lastUpdated\":null},\"byInstanceType\":{}}}},\"isStale\":false}}","aggregateprogress":{"progress":0,"total":0},"priority":{"self":"https://xxx.xx.xx.xx:xxx/rest/api/2/priority/3","iconUrl":"https://xxx.xx.xx.xx:xxx/images/icons/priorities/medium.svg","name":"Medium","id":"3"},"customfield_10100":"0|i000ev:","customfield_10101":null,"customfield_10102":null,"labels":[],"environment":null,"timeestimate":null,"aggregatetimeoriginalestimate":null,"versions":[],"duedate":null,"progress":{"progress":0,"total":0},"comment":{"comments":[{"self":"https://xxx.xx.xx.xx:xxx/rest/api/2/issue/10129/comment/10263","id":"10263","author":{"self":"https://xxx.xx.xx.xx:xxx/rest/api/2/user?username=admin","name":"admin","key":"xxxxx","emailAddress":"admin@siemplifylab.local","avatarUrls":{"48x48":"https://www.gravatar.com/avatar/29b93653324514469f10298493b25289?d=mm&s=48","24x24":"https://www.gravatar.com/avatar/29b93653324514469f10298493b25289?d=mm&s=24","16x16":"https://www.gravatar.com/avatar/29b93653324514469f10298493b25289?d=mm&s=16","32x32":"https://www.gravatar.com/avatar/29b93653324514469f10298493b25289?d=mm&s=32"},"displayName":"admin@siemplifylab.local","active":true,"timeZone":"Asia/Jerusalem"},"body":"[~vasil.daskalov@siemplify.co] assigned issue TES-65 to vasil.daskalov@siemplify.co.","updateAuthor":{"self":"https://xxx.xx.xx.xx:xxx/rest/api/2/user?username=admin","name":"admin","key":"xxxxx","emailAddress":"admin@siemplifylab.local","avatarUrls":{"48x48":"https://www.gravatar.com/avatar/29b93653324514469f10298493b25289?d=mm&s=48","24x24":"https://www.gravatar.com/avatar/29b93653324514469f10298493b25289?d=mm&s=24","16x16":"https://www.gravatar.com/avatar/29b93653324514469f10298493b25289?d=mm&s=16","32x32":"https://www.gravatar.com/avatar/29b93653324514469f10298493b25289?d=mm&s=32"},"displayName":"admin@siemplifylab.local","active":true,"timeZone":"Asia/Jerusalem"},"created":"2021-11-08T14:10:06.738+0000","updated":"2021-11-08T14:10:06.738+0000"}],"maxResults":3,"total":3,"startAt":0},"issuelinks":[{"id":"10002","self":"https://xxx.xx.xx.xx:xxx/rest/api/2/issueLink/10002","type":{"id":"10000","name":"Blocks","inward":"is blocked by","outward":"blocks","self":"https://xxx.xx.xx.xx:xxx/rest/api/2/issueLinkType/10000"},"inwardIssue":{"id":"10127","key":"xxxx","self":"https://xxx.xx.xx.xx:xxx/rest/api/2/issue/10127","fields":{"summary":"Narek test","status":{"self":"https://xxx.xx.xx.xx:xxx/rest/api/2/status/10002","description":"","iconUrl":"https://xxx.xx.xx.xx:xxx/","name":"Fini","id":"10002","statusCategory":{"self":"https://xxx.xx.xx.xx:xxx/rest/api/2/statuscategory/3","id":3,"key":"done","colorName":"green","name":"Terminé"}},"priority":{"self":"https://xxx.xx.xx.xx:xxx/rest/api/2/priority/3","iconUrl":"https://xxx.xx.xx.xx:xxx/images/icons/priorities/medium.svg","name":"Medium","id":"3"},"issuetype":{"self":"https://xxx.xx.xx.xx:xxx/rest/api/2/issuetype/10004","id":"10004","description":"","iconUrl":"https://xxx.xx.xx.xx:xxx/secure/viewavatar?size=xsmall&avatarId=10303&avatarType=issuetype","name":"Bogue","subtask":false,"avatarId":10303}}}}],"votes":{"self":"https://xxx.xx.xx.xx:xxx/rest/api/2/issue/TES-65/votes","votes":0,"hasVoted":false},"worklog":{"startAt":0,"maxResults":20,"total":0,"worklogs":[]},"assignee":{"self":"https://xxx.xx.xx.xx:xxx/rest/api/2/user?username=token","name":"token","key":"xxxxx","emailAddress":"vasil.daskalov@siemplify.co","avatarUrls":{"48x48":"https://www.gravatar.com/avatar/458b9d1a2cbd7ba6d9de93877657db52?d=mm&s=48","24x24":"https://www.gravatar.com/avatar/458b9d1a2cbd7ba6d9de93877657db52?d=mm&s=24","16x16":"https://www.gravatar.com/avatar/458b9d1a2cbd7ba6d9de93877657db52?d=mm&s=16","32x32":"https://www.gravatar.com/avatar/458b9d1a2cbd7ba6d9de93877657db52?d=mm&s=32"},"displayName":"Vasil Daskalov","active":true,"timeZone":"Etc/UTC"},"archivedby":null,"updated":"2021-11-11T13:16:50.552+0000","status":{"self":"https://xxx.xx.xx.xx:xxx/rest/api/2/status/10002","description":"","iconUrl":"https://xxx.xx.xx.xx:xxx/","name":"Fini","id":"10002","statusCategory":{"self":"https://xxx.xx.xx.xx:xxx/rest/api/2/statuscategory/3","id":3,"key":"done","colorName":"green","name":"Terminé"}}}]
```



#### Link Issues
Link multiple issues in Jira.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Inward Issue ID|Specify the inward issue id. For example, if the relation type is “Blocks”, then in the UI you would see this issue with relation "blocks".|True|String||
|Outward Issue IDs|Specify a comma-separated list of outward issue ids. For example, if the relation type is “Blocks”, then in the UI you would see this issue with relation "blocked by".|True|String||
|Relation Type|Specify the relation type that will be used to link multiple issues. A list of all available relation types are available in the action "List Relation Types".|True|String|Blocks|



#### List Issues
Search for issues
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Project Names|The names of the projects to search in, comma separated|False|String||
|Summary|The summary to filter by|False|String||
|Description|The description to filter by|False|String||
|Issue Types|The issue types to filter by|False|String||
|Priorities|The priority to filter by|False|String||
|Created From|The earliest creation date to filter by. Format: YYYY/MM/DD. If not provided, filter will not be used.|False|String|YYYY/MM/DD|
|Updated From|The earliest update date to filter by. Format: YYYY/MM/DD. If not provided, filter will not be used.|False|String|YYYY/MM/DD|
|Assignees|The name of the assignees to filter by, comma separated|False|String||
|Reporter|The name of the reporters to filter by, comma separated|False|String||
|Statuses|The statuses to filter by, comma separated|False|String||



##### JSON Results
```json
["PR-123", "PR-124"]
```



#### List Relation Types
List available relation types in Jira.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Filter Key|Specify the key that needs to be used to filter {item type}.|False|List|Select One|
|Filter Logic|Specify what filter logic should be applied. Filtering logic is working based on the value provided in the "Filter Key" parameter.|False|List|Not Specified|
|Filter Value|Specify what value should be used in the filter. If "Equal" is selected, action will try to find the exact match among results and if "Contains" is selected, action will try to find results that contain that substring. If nothing is provided in this parameter, the filter will not be applied. Filtering logic is working based on the value  provided in the "Filter Key" parameter.|False|String||
|Max Records To Return|Specify how many records to return. If nothing is provided, action will return 50 records.|False|String|50|



##### JSON Results
```json
[{"id":"10xxx","name":"Blocks","inward":"is blocked by","outward":"blocks","self":"https://172.30.xxx.xx:84xx/rest/api/2/issueLinkType/10xxx"},{"id":"10xxx","name":"Cloners","inward":"is cloned by","outward":"clones","self":"https://172.30.xxx.xx:84xx/rest/api/2/issueLinkType/10xxx"}]
```



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Search Users
Search users in Jira. Note: Providing User Email Addresses will result in more accurate results.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|User Email Addresses|Specify a comma-separated list of email addresses for which you want to return the users.|False|String||
|User Names|Specify a comma-separated list of user display names for which you want to return the users.|False|String||
|Project|Specify the name of the project in which you need to search for the email addresses. If provided, only Project Assignable Users will be returned. |False|String||



##### JSON Results
```json
[  
    {  
        "Entity": "User Display Name 1",  
        "EntityResult": {  
            "_resource": "user?accountId={0}",  
            "_options": {  
                "server": "https://{...}/atlassian.net",  
                "auth_url": "/rest/auth/1/session",  
                "context_path": "/",  
                "rest_path": "api",  
                "rest_api_version": "2",  
                "agile_rest_path": "agile",  
                "agile_rest_api_version": "1.0",  
                "verify": false,  
                "resilient": true,  
                "async": false,  
                "async_workers": 5,  
                "client_cert": null,  
                "check_update": false,  
                "delay_reload": 0,  
                "headers": {  
                    "Cache-Control": "no-cache",  
                    "Content-Type": "application/json",  
                    "X-Atlassian-Token": "no-check"  
                }  
            },  
            "_session": "<jira.resilientsession.ResilientSession object>",  
            "_base_url": "{server}/rest/{rest_path}/{rest_api_version}/{path}",  
            "raw": {  
                "self": "https://{...}.atlassian.net/rest/api/2/user?accountId={account_id}",  
                "accountId": "{account_id}",  
                "accountType": "atlassian",  
                "emailAddress": "user@domain.com",  
                "avatarUrls": {  
                    "48x48": "https://secure.gravatar.com/avatar/{id}?d=...png",  
                    "24x24": "https://secure.gravatar.com/avatar/{id}?d=...png",  
                    "16x16": "https://secure.gravatar.com/avatar/{id}?d=...png",  
                    "32x32": "https://secure.gravatar.com/avatar/{id}?d=...png"  
                },  
                "displayName": "User Display Name 1",  
                "active": true,  
                "timeZone": "Europe/Berlin",  
                "locale": "en_US"  
            },  
            "self": "https://{...}.atlassian.net/rest/api/2/user?accountId={account_id}",  
            "accountId": "{account_id}",  
            "accountType": "atlassian",  
            "emailAddress": "user@domain.com",  
            "avatarUrls": "<jira.resources.PropertyHolder object at 0x7bb39ae03470>",  
            "displayName": "User Display Name 1",  
            "active": true,  
            "timeZone": "Europe/Berlin",  
            "locale": "en_US"  
        }  
    },  
    {  
        "Entity": "User Display Name 2",  
        "EntityResult": {  
            "_resource": "user?accountId={0}",  
            "_options": {  
                "server": "https://{...}.atlassian.net",  
                "auth_url": "/rest/auth/1/session",  
                "context_path": "/",  
                "rest_path": "api",  
                "rest_api_version": "2",  
                "agile_rest_path": "agile",  
                "agile_rest_api_version": "1.0",  
                "verify": false,  
                "resilient": true,  
                "async": false,  
                "async_workers": 5,  
                "client_cert": null,  
                "check_update": false,  
                "delay_reload": 0,  
                "headers": {  
                    "Cache-Control": "no-cache",  
                    "Content-Type": "application/json",  
                    "X-Atlassian-Token": "no-check"  
                }  
            },  
            "_session": "<jira.resilientsession.ResilientSession object at 0x7bb39addbe48>",  
            "_base_url": "{server}/rest/{rest_path}/{rest_api_version}/{path}",  
            "raw": {  
                "self": "https://{...}.atlassian.net/rest/api/2/user?accountId={account_id}",  
                "accountId": "{account_id}",  
                "accountType": "atlassian",  
                "emailAddress": "user@domain.com",  
                "avatarUrls": {  
                    "48x48": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/{account_id}/{id}/48",  
                    "24x24": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/{account_id}/{id}/24",  
                    "16x16": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/{account_id}/{id}/16",  
                    "32x32": "https://avatar-management--avatars.us-west-2.prod.public.atl-paas.net/{account_id}/{id}/32"  
                },  
                "displayName": "User Display Name 2",  
                "active": true,  
                "timeZone": "Europe/Berlin",  
                "locale": "en_US"  
            },  
            "self": "https://{...}.atlassian.net/rest/api/2/user?accountId={account_id}",  
            "accountId": "{account_id}",  
            "accountType": "atlassian",  
            "emailAddress": "user@domain.com",  
            "avatarUrls": "<jira.resources.PropertyHolder object>",  
            "displayName": "User Display Name 2",  
            "active": true,  
            "timeZone": "Europe/Berlin",  
            "locale": "en_US"  
        }  
    }  
]
```



#### Upload Attachment
Add an attachment to an issue.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Issue Key|The key of the issue|True|String||
|File Paths|The paths of the files to upload, comma separated|True|String||
|Mode|Specify the mode for the action. If "Add New Attachment" is selected, action will add a new attachment, if it even has the same name. If "Overwrite Existing Attachment" is selected, action will remove other attachments with the same name and add a new attachment.|False|List|Add New Attachment|



#### Update Issue
Update an issue. For new Jira Api, action will try to find a match for the assignee to assign an issue based on User email or displayName field.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Issue Key|The key of the issue to update|True|String||
|Status|Specify the relevant transition name, to transition this issue to the new desired status.|False|String|Done|
|Summary|The new summary of the issue|False|String||
|Description|The new description of the issue|False|String||
|Issue Type|The new type of the issue|False|String||
|Jira Username|The JIRA username of the action initiator. Note: If a username is not provided, action will not create a comment in the issue|False|String||
|Assignee|The new assignee of the issue.|False|String||
|Components|The Components field of the issue. Parameter accepts multiple values as a comma separated string.|False|String||
|Labels|The Labels field of the issue. Parameter accepts multiple values as a comma separated string.|False|String||
|Custom Fields|Specify a JSON object containing all of the fields and values that will be updated for the issue. Note: this parameter has priority and all of the fields will be overwritten with the value that is provided for this parameter. Example: {"field":"value"}|False|String||



##### JSON Results
```json
{"comment": {"total": 0, "startAt": 0, "comments": [], "maxResults": 0}, "creator": {"displayName": "user1", "name": "user1", "self": "", "avatarUrls": {"24x24": "", "16x16": "", "48x48": "", "32x32": ""}, "emailAddress": "john_doe@example.com", "key": "user1user", "active": true, "timeZone": "Asia/Jerusalem", "accountId": "0"}, "aggregatetimeestimate": null, "labels": ["Label1"], "aggregatetimespent": null, "watches": {"self": "", "watchCount": 1, "isWatching": false}, "assignee": {"displayName": "user2", "name": "user2", "self": "", "avatarUrls": {"24x24": "", "16x16": "", "48x48": "", "32x32": ""}, "emailAddress": "john_doe@example.com", "key": "user2", "active": true, "timeZone": "Asia/Jerusalem", "accountId": ""}, "lastViewed": "2019-01-22T10:14:02.910+0200", "issuelinks": [], "worklog": {"worklogs": [], "total": 0, "startAt": 0, "maxResults": 20}, "aggregateprogress": {"progress": 0, "total": 0}, "priority": {"iconUrl": "", "self": "", "name": "Medium", "id": "3"}, "votes": {"hasVoted": false, "self": "", "votes": 0}, "workratio": -1, "fixVersions": [], "environment": null, "timespent": null, "attachment": [{"mimeType": "binary/octet-stream", "created": "2018-06-19T15:23:07.369+0300", "self": "", "author": {"displayName": "user1", "name": "user1", "self": "", "avatarUrls": {"24x24": "", "16x16": "", "48x48": "", "32x32": ""}, "emailAddress": "john_doe@example.com", "key": "user1", "active": true, "timeZone": "Asia/Jerusalem", "accountId": "0"}, "filename": "file.rar", "content": "", "id": "0", "size": 0}], "progress": {"progress": 0, "total": 0}, "duedate": null, "status": {"statusCategory": {"name": "Done", "self": "", "id": 3, "key": "done", "colorName": "green"}, "description": "", "self": "", "iconUrl": "", "id": "0", "name": "DONE"}, "updated": "2018-09-18T10:02:06.347+0300", "subtasks": [], "description": "Create Enrich entites action using Insights API (IOC search)\n\nWrite connector for laerts\n\nIn a couple of days we will have access to an instance", "reporter": {"displayName": "user1", "name": "user1", "self": "", "avatarUrls": {"24x24": "", "16x16": "", "48x48": "", "32x32": ""}, "emailAddress": "john_doe@example.com", "key": "user1", "active": true, "timeZone": "Asia/Jerusalem", "accountId": "0"}, "timeoriginalestimate": null, "aggregatetimeoriginalestimate": null, "created": "2018-06-19T15:23:13.701+0300", "versions": [], "resolutiondate": "2018-09-18T10:02:06.340+0300", "summary": "Sample issue", "project": {"name": "Project 1", "self": "", "projectTypeKey": "software", "avatarUrls": {"24x24": "", "16x16": "", "48x48": "", "32x32": ""}, "key": "PR", "id": "0"}, "timetracking": {}, "components": [], "issuetype": {"name": "Task", "self": "", "iconUrl": "", "subtask": false, "avatarId": 10318, "id": "10002", "description": "A task that needs to be done."}, "security": null, "resolution": {"id": "10000", "self": "", "description": "Work has been completed on this issue.", "name": "Done"}, "timeestimate": null}
```






## Jobs

#### Tits Sync Comments
Sync comments between Siemplify alert’s case and corresponding Jira ticket. Sync mechanism works in both ways, Siemplify → Jira and Jira → Siemplify

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|API Root|True|String|https://{jira_address}|
|Username|True|String||
|API Token|True|Password||
|Environment|False|String||
|Project Names|False|String|project names separated by comma|
|Days Backwards|False|String|1|
|Siemplify Comment Prefix|True|String|SIEMPLIFY:|
|Jira Comment Prefix|True|String|Jira Comment Sync Job:|

#### Tits Sync Closure
Close tickets in Jira if corresponding Siemplify alerts were closed.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|API Root|True|String|https://{jira_address}|
|Username|True|String||
|API Token|True|Password||
|Environment|False|String||
|Project Names|True|String|project names separated by comma|
|Days Backwards|True|String|1|

#### Copy of Sync Comments
Sync comments between Siemplify alert’s case and corresponding Jira ticket. Sync mechanism works in both ways, Siemplify → Jira and Jira → Siemplify

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|API Root|True|String|https://{jira_address}|
|Username|True|String||
|API Token|True|Password||
|Environment|False|String||
|Project Names|False|String|project names separated by comma|
|Days Backwards|False|String|1|
|Siemplify Comment Prefix|True|String|SIEMPLIFY:|
|Jira Comment Prefix|True|String|Jira Comment Sync Job:|

#### Sync Closure
Close tickets in Jira if corresponding Google SecOps alerts were closed.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|API Root|True|String|https://{jira_address}|
|Username|True|String||
|API Token|True|Password||
|Environment|False|String||
|Project Names|True|String|project names separated by comma|
|Days Backwards|True|String|1|

#### Sync Comments
Sync comments between Google SecOps alert's case and corresponding Jira ticket. Sync mechanism works in both ways, Google SecOps → Jira and Jira → Google SecOps

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|API Root|True|String|https://{jira_address}|
|Username|True|String||
|API Token|True|Password||
|Environment|False|String||
|Project Names|False|String|project names separated by comma|
|Days Backwards|False|String|1|
|Siemplify Comment Prefix|True|String|Google SecOps:|
|Jira Comment Prefix|True|String|Jira Comment Sync Job:|



## Connectors
#### Jira Connector
Fetch issues from Jira to Siemplify

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Token||True|Password||
|DeviceProductField|The field name used to determine the device product|True|String|device_product|
|EventClassId|The field name used to determine the event name (sub-type)|False|String|issuetype_name|
|PythonProcessTimeout|The timeout limit (in seconds) for the python process running current script|True|String|180|
|Api Root|The API root of the JIRA instance|True|String|https://{jira_address}|
|Username||True|String||
|Use Jira Project as Environment|Use Jira project as environment else use Environment Field Name as environment.|False|Boolean|true|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|Days Backwards|Max number of days backwards to pull alerts from|False|Integer|5|
|Max Tickets Per Cycle|Max tickets to fetch and process in one connector cycle|False|Integer|10|
|Verify SSL|If enabled, verify the SSL certificate for the connection to Jira server is valid.|False|Boolean|false|
|Project Names|Project names separated by comma|False|String||
|Issue Statuses|Issue statuses separated by comma|False|String||
|Assignees|Users full names separated by comma|False|String||
|Issue Types|Issue types separated by comma|False|String||
|Issue Priorities|Issue priorities separated by comma|False|String||
|Issue Components|Issue components separated by comma|False|String||
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password||




