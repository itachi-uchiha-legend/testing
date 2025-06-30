<p align="center"><img src="./Resources/MicrosoftTeams.svg" 
     alt="MicrosoftTeams" width="200"/></p>

# MicrosoftTeams

Microsoft Teams is a platform that combines workplace chat, meetings, notes, and attachments
Quick Guide: you must first register your app at Microsoft App Registration Portal, Configure Microsoft Teams Integration, Run the action 'Get Authorization', Run the action 'Generate Token'.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Client ID|None|True|String||
|Secret ID|None|True|Password|None|
|Tenant|None|True|String||
|Refresh Token|None|True|Password|None|
|Redirect URL|None|False|String|http://localhost/|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Microsoft Teams server is valid.|False|Boolean|false|


#### Dependencies
| |
|-|
|idna-3.10-py3-none-any.whl|
|google_auth_httplib2-0.2.0-py2.py3-none-any.whl|
|google_auth-2.40.3-py2.py3-none-any.whl|
|httpcore-1.0.9-py3-none-any.whl|
|soupsieve-2.6-py3-none-any.whl|
|httplib2-0.22.0-py3-none-any.whl|
|googleapis_common_protos-1.70.0-py3-none-any.whl|
|protobuf-6.31.1-cp39-abi3-manylinux2014_x86_64.whl|
|anyio-4.9.0-py3-none-any.whl|
|requests-2.32.4-py3-none-any.whl|
|pyasn1-0.6.1-py3-none-any.whl|
|h11-0.16.0-py3-none-any.whl|
|sniffio-1.3.1-py3-none-any.whl|
|pyparsing-3.2.3-py3-none-any.whl|
|EnvironmentCommon-1.0.2-py2.py3-none-any.whl|
|TIPCommon-2.2.2-py2.py3-none-any.whl|
|pycryptodome-3.23.0-cp37-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|pyasn1_modules-0.4.2-py3-none-any.whl|
|typing_extensions-4.14.0-py3-none-any.whl|
|urllib3-2.4.0-py3-none-any.whl|
|charset_normalizer-3.4.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|proto_plus-1.26.1-py3-none-any.whl|
|beautifulsoup4-4.12.3-py3-none-any.whl|
|uritemplate-4.2.0-py3-none-any.whl|
|google_api_python_client-2.172.0-py3-none-any.whl|
|cachetools-5.5.2-py3-none-any.whl|
|httpx-0.28.1-py3-none-any.whl|
|rsa-4.9.1-py3-none-any.whl|
|certifi-2025.4.26-py3-none-any.whl|
|google_api_core-2.25.0-py3-none-any.whl|


## Actions
#### Create Chat
Create a user chat in Microsoft Teams. Supported entities: Username, Email Address (username that matches email regex). Note: chat will be created for each user.
Timeout - 600 Seconds



##### JSON Results
```json
[{"Entity":"test@example.com","EntityResult":{"@odata.context":"https://graph.microsoft.com/beta/$metadata#chats/$entity","id":"19:xxxxxxxx-ffdf-4ea2-83ad-0f26722a25cc_b786d3cf-e97d-4511-b61c-xxxxxxxxxxxx@xxx.xxx.spaces","topic":null,"createdDateTime":"2021-12-01T17:08:12.52Z","lastUpdatedDateTime":"2021-12-01T17:08:12.52Z","chatType":"oneOnOne","webUrl":"https://teams.microsoft.com/l/chat/19%xxxxxxxxxx-ffdf-4ea2-83ad-0f26722a25cc_b786d3cf-e97d-4511-b61c-xxxxxxxxxxxx%40xxx.xxx.spaces/0?tenantId=d48f52ca-5b1a-4708-8ed0-xxxxxxxxxxxx","tenantId":"d48f52ca-5b1a-4708-8ed0-xxxxxxxxxxxx","viewpoint":null,"onlineMeetingInfo":null}},{"Entity":"Test name","EntityResult":{"@odata.context":"https://graph.microsoft.com/beta/$metadata#chats/$entity","id":"19:xxxxxxxx-f255-4f9d-8220-bfeafdb91065_b786d3cf-e97d-4511-b61c-xxxxxxxxxxxx@xxx.xxx.spaces","topic":null,"createdDateTime":"2021-12-01T17:08:54.032Z","lastUpdatedDateTime":"2021-12-01T17:08:54.032Z","chatType":"oneOnOne","webUrl":"https://teams.microsoft.com/l/chat/19%xxxxxxxxxx-f255-4f9d-8220-bfeafdb91065_b786d3cf-e97d-4511-b61c-xxxxxxxxxxxx%40xxx.xxx.spaces/0?tenantId=d48f52ca-5b1a-4708-8ed0-xxxxxxxxxxxx","tenantId":"d48f52ca-5b1a-4708-8ed0-xxxxxxxxxxxx","viewpoint":null,"onlineMeetingInfo":null}}]
```



#### List Channels
Get all channels details that exist in specific team
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Team Name|None|True|String||
|Max Channels To Return|Specify how many channels to return. Default: 50.|False|String|50|



##### JSON Results
```json
{}
```



#### Create Channel
Create a channel in Microsoft Teams.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Team Name|Specify the name of the team in which you need to create the channel.|True|String||
|Channel Name|Specify a unique name of the channel.|True|String||
|Channel Type|Specify the type of the channel that needs to be created. Standard channel is accessible to all members of the team, while private channel will require users to be added to it.|True|List|Standard|
|Description|Specify a description for the channel.|False|String||



##### JSON Results
```json
{"@odata.context": "https: //graph.microsoft.com/beta/$metadata#teams('947e8bdb-27b6-4ba4-9ee4-7cxxxxxxxxxx')/channels/$entity","id": "19:a04023d482da48e48518f5xxxxxxxxxx@thread.xxxxx","createdDateTime": "2021-11-22T15:13:02.0443425Z","displayName": "test name","description": "testing","isFavoriteByDefault": false,"email": "","webUrl": "https://teams.microsoft.com/l/channel/19%3aa04023d482da48e48518f5xxxxxxxxxx%40thread.xxxxx/test+name?groupId=ee820b05-6cb4-4496-b441-b6xxxxxxxxxx&tenantId=d48f52ca-5b1a-4708-8ed0-ebxxxxxxxxxx","membershipType": "standard","moderationSettings": {"userNewMessageRestriction": "everyone","replyRestriction": "everyone","allowNewMessageFromBots": true,"allowNewMessageFromConnectors": true}}
```



#### List Teams
Retrieve details of all teams
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Max Teams To Return|Specify how many teams to return. Default: 50.|False|String|50|



##### JSON Results
```json
[{"mailNickname": "Test", "classification": null, "deletedDateTime": null, "renewedDateTime": "2018-11-12T15:03:50Z", "onPremisesProvisioningErrors": [], "membershipRuleProcessingState": null, "preferredLanguage": null, "expirationDateTime": null, "id": "43b559d5-f63d-47dd-9e6c-b3470b6446ee", "theme": null, "preferredDataLocation": null, "mail": "john_doe@example.com", "membershipRule": null, "onPremisesLastSyncDateTime": null, "description": "Test", "securityEnabled": false, "proxyAddresses": ["SPO:SPO_eaf75319-582a-46cf-8812-9e787d757c4e@SPO_a4a936ec-735f-488a-bfc0-7665f87aab47", "SMTP:Test@tenant.onmicrosoft.com"], "visibility": "Public", "resourceProvisioningOptions": ["Team"], "displayName": "Test", "groupTypes": ["Unified"], "onPremisesSyncEnabled": null, "createdDateTime": "2018-11-12T15:03:50Z", "resourceBehaviorOptions": ["HideGroupInOutlook", "SubscribeMembersToCalendarEventsDisabled", "WelcomeEmailDisabled"], "onPremisesSecurityIdentifier": null, "mailEnabled": true}, {"mailNickname": "user", "classification": null, "deletedDateTime": null, "renewedDateTime": "2018-11-28T13:46:50Z", "onPremisesProvisioningErrors": [], "membershipRuleProcessingState": null, "preferredLanguage": null, "expirationDateTime": null, "id": "67149c85-7139-4062-bfae-059d18ee7e5d", "theme": null, "preferredDataLocation": null, "mail": "john_doe@example.com", "membershipRule": null, "onPremisesLastSyncDateTime": null, "description": "user", "securityEnabled": false, "proxyAddresses": ["SPO:SPO_781470a6-2db5-454d-a8e3-71752b3b829e@SPO_a4a936ec-735f-488a-bfc0-7665f87aab47", "SMTP:user@tenant.onmicrosoft.com"], "visibility": "Public", "resourceProvisioningOptions": ["Team"], "displayName": "user", "groupTypes": ["Unified"], "onPremisesSyncEnabled": null, "createdDateTime": "2018-11-28T13:46:50Z", "resourceBehaviorOptions": ["HideGroupInOutlook", "SubscribeMembersToCalendarEventsDisabled", "WelcomeEmailDisabled"], "onPremisesSecurityIdentifier": null, "mailEnabled": true}]
```



#### Get Authorization
Run the action and browse to the received url
Timeout - 600 Seconds



#### Add Users To Channel
Add users to the private channel in Microsoft Teams. Supported entities: Username, Email Address (username that matches email regex). Note: only users that are a part of the same team can be added to the channel.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Team Name|Specify the name of the team in which you want to search for the channel.|True|String||
|Channel Name|Specify the name of the channel to which you want to add users.|True|String||



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Send Chat Message
Send a chat message in Microsoft Teams. Note: Action is running as async if “Wait For Reply” is enabled, please adjust script timeout value in Siemplify IDE for action as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Chat ID|Specify the ID of the chat to which you want to send a message.|True|String||
|Text|Specify the content of the message.|True|String||
|Wait For Reply|If enabled, action will wait until reply.|False|Boolean|true|



##### JSON Results
```json
{"id":"16340311xxxx","replyToId":"null","etag":"1634031165xxx","messageType":"message","createdDateTime":"2021-10-12T09:32:45.41Z","lastModifiedDateTime":"2021-10-12T09:32:45.41Z","lastEditedDateTime":"null","deletedDateTime":"null","subject":"null","summary":"null","chatId":"chat_id5@example","importance":"normal","locale":"en-us","webUrl":"null","channelIdentity":"null","policyViolation":"null","from":{"application":"null","device":"null","user":{"id":"b786d3cf-e97d-4511-b61c-0559e9sss","displayName":"asd","userIdentityType":"aadUser"}},"body":{"contentType":"text","content":"Test Text"}}
```



#### Generate Token
Get an access token using the authorization url received in the previous step
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Authorization URL|Use the authorization URL received in the previous step to request an access token.|True|String||



#### Send Message
Send Message to specific Channel
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Team Name|None|True|String||
|Channel Name|None|True|String||
|Message|None|True|String||



##### JSON Results
```json
[{"@odata.context":"https://graph.microsoft.com/beta/$metadata#teams('192c0699-fad2-4d02-88a2-84efd6369894')/channels('19%3Ae3acbb17a8754cae9df724f493b5342f%40thread.tacv2')/messages/$entity","id":"1601372154742","replyToId":null,"etag":"1601372154742","messageType":"message","createdDateTime":"2020-09-29T09:35:54.742Z","lastModifiedDateTime":"2020-09-29T09:35:54.742Z","lastEditedDateTime":null,"deletedDateTime":null,"subject":null,"summary":null,"chatId":null,"importance":"normal","locale":"en-us","webUrl":"https://teams.microsoft.com/l/message/19%3Ae3acbb17a8754cae9df724f493b5342f%40thread.tacv2/1601372154742?groupId=192c0699-fad2-4d02-88a2-84efd6369894&tenantId=d48f52ca-5b1a-4708-8ed0-ebb98a26a46a&createdTime=1601372154742&parentMessageId=1601372154742","policyViolation":null,"from":{"application":null,"device":null,"conversation":null,"user":{"id":"b786d3cf-e97d-4511-b61c-0559e9f4da75","displayName":"ג'יימס בונד","userIdentityType":"aadUser"}},"body":{"contentType":"text","content":"Hello there"},"channelIdentity":{"teamId":"192c0699-fad2-4d02-88a2-84efd6369894","channelId":"19:e3acbb17a8754cae9df724f493b5342f@thread.tacv2"},"attachments":[],"mentions":[],"reactions":[]}]
```



#### List Users
Get all users details
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Max Users To Return|Specify how many users to return. Default: 50.|False|String|50|



##### JSON Results
```json
[{"isResourceAccount": null, "mailNickname": "admin", "surname": "test", "deletedDateTime": null, "assignedLicenses": [{"skuId": "16ddbbfc-09ea-4de2-b1d7-312db6112d70", "disabledPlans": []}], "userPrincipalName": "john_doe@example.com", "faxNumber": null, "consentProvidedForMinor": null, "userType": "Member", "officeLocation": null, "usageLocation": "IL", "city": null, "employeeId": null, "onPremisesImmutableId": null, "preferredLanguage": "en", "streetAddress": null, "id": "0cf5ab11-13fc-474c-abaf-cf2b69ee77a9", "state": null, "businessPhones": ["0542533879"], "postalCode": null, "mail": "john_doe@example.com", "onPremisesSamAccountName": null, "onPremisesLastSyncDateTime": null, "accountEnabled": true, "mobilePhone": null, "refreshTokensValidFromDateTime": "2018-11-12T13:26:42Z", "companyName": null, "deviceKeys": [], "jobTitle": null, "preferredDataLocation": null, "showInAddressList": null, "department": null, "proxyAddresses": ["SMTP:connectortest0@gmail.com"], "externalUserStateChangeDateTime": null, "onPremisesProvisioningErrors": [], "legalAgeGroupClassification": null, "onPremisesSyncEnabled": null, "onPremisesExtensionAttributes": {"extensionAttribute4": null, "extensionAttribute5": null, "extensionAttribute6": null, "extensionAttribute7": null, "extensionAttribute12": null, "extensionAttribute1": null, "extensionAttribute2": null, "extensionAttribute3": null, "extensionAttribute10": null, "extensionAttribute11": null, "extensionAttribute8": null, "extensionAttribute9": null, "extensionAttribute14": null, "extensionAttribute15": null, "extensionAttribute13": null}, "assignedPlans": [{"capabilityStatus": "Enabled", "servicePlanId": "617d9209-3b90-4879-96e6-838c42b2701d", "service": "MicrosoftCommunicationsOnline", "assignedDateTime": "2018-11-12T13:27:18Z"}, {"capabilityStatus": "Enabled", "servicePlanId": "902b47e5-dcb2-4fdc-858b-c63a90a2bdb9", "service": "SharePoint", "assignedDateTime": "2018-11-12T13:27:18Z"}, {"capabilityStatus": "Enabled", "servicePlanId": "4fa4026d-ce74-4962-a151-8e96d57ea8e4", "service": "TeamspaceAPI", "assignedDateTime": "2018-11-12T13:27:18Z"}], "passwordProfile": null, "passwordPolicies": null, "externalUserState": null, "otherMails": ["connectortest0@gmail.com"], "displayName": "connector test", "imAddresses": [], "provisionedPlans": [{"capabilityStatus": "Enabled", "provisioningStatus": "Success", "service": "SharePoint"}], "createdDateTime": "2018-11-12T13:26:42Z", "country": null, "onPremisesDistinguishedName": null, "onPremisesSecurityIdentifier": null, "onPremisesDomainName": null, "onPremisesUserPrincipalName": null, "givenName": "connector", "ageGroup": null}, {"isResourceAccount": null, "mailNickname": "usename.co#EXT#", "surname": null, "deletedDateTime": null, "assignedLicenses": [{"skuId": "16ddbbfc-09ea-4de2-b1d7-312db6112d70", "disabledPlans": []}], "userPrincipalName": "username@domain.com#EXT#@tenant.onmicrosoft.com", "faxNumber": null, "consentProvidedForMinor": null, "userType": "Member", "officeLocation": null, "usageLocation": "IL", "city": null, "employeeId": null, "onPremisesImmutableId": null, "preferredLanguage": null, "streetAddress": null, "id": "5e457a85-a705-4b65-8a9f-3a3d2ad7715c", "state": null, "businessPhones": [], "postalCode": null, "mail": "john_doe@example.com", "onPremisesSamAccountName": null, "onPremisesLastSyncDateTime": null, "accountEnabled": true, "mobilePhone": null, "refreshTokensValidFromDateTime": "2018-11-12T13:28:53Z", "companyName": null, "deviceKeys": [], "jobTitle": null, "preferredDataLocation": null, "showInAddressList": false, "department": null, "proxyAddresses": ["SMTP:username@domain.com"], "externalUserStateChangeDateTime": "2018-11-12T13:29:41Z", "onPremisesProvisioningErrors": [], "legalAgeGroupClassification": null, "onPremisesSyncEnabled": null, "onPremisesExtensionAttributes": {"extensionAttribute4": null, "extensionAttribute5": null, "extensionAttribute6": null, "extensionAttribute7": null, "extensionAttribute12": null, "extensionAttribute1": null, "extensionAttribute2": null, "extensionAttribute3": null, "extensionAttribute10": null, "extensionAttribute11": null, "extensionAttribute8": null, "extensionAttribute9": null, "extensionAttribute14": null, "extensionAttribute15": null, "extensionAttribute13": null}, "assignedPlans": [{"capabilityStatus": "Enabled", "servicePlanId": "617d9209-3b90-4879-96e6-838c42b2701d", "service": "MicrosoftCommunicationsOnline", "assignedDateTime": "2018-11-12T13:28:57Z"}, {"capabilityStatus": "Enabled", "servicePlanId": "902b47e5-dcb2-4fdc-858b-c63a90a2bdb9", "service": "SharePoint", "assignedDateTime": "2018-11-12T13:28:57Z"}, {"capabilityStatus": "Enabled", "servicePlanId": "4fa4026d-ce74-4962-a151-8e96d57ea8e4", "service": "TeamspaceAPI", "assignedDateTime": "2018-11-12T13:28:57Z"}], "passwordProfile": null, "passwordPolicies": null, "externalUserState": "Accepted", "otherMails": ["username@domaim.com"], "displayName": "username", "imAddresses": [], "provisionedPlans": [{"capabilityStatus": "Enabled", "provisioningStatus": "Success", "service": "SharePoint"}], "createdDateTime": "2018-11-12T13:28:53Z", "country": null, "onPremisesDistinguishedName": null, "onPremisesSecurityIdentifier": null, "onPremisesDomainName": null, "onPremisesUserPrincipalName": null, "givenName": null, "ageGroup": null}]
```



#### List Chats
List available chats in Teams.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Chat Type|Specify what type of chat should be returned.|False|List|All|
|Filter Key|Specify the key that needs to be used to filter chats.|False|List|Select One|
|Filter Logic|Specify what filter logic should be applied. Filtering logic is working based on the value  provided in the Filter Key parameter.|False|List|Not Specified|
|Filter Value|Specify what value should be used in the filter. If “Equal“ is selected, action will try to find the exact match among results and if “Contains“ is selected, action will try to find results that contain that substring. If nothing is provided in this parameter, the filter will not be applied. Filtering logic is working based on the value  provided in the “Filter Key” parameter.|False|String||
|Max Records To Return|Specify how many records to return. If nothing is provided, action will return 50 records.|False|String|50|



##### JSON Results
```json
[{"id":"19:testID@thread.v2","topic":null,"createdDateTime":"2021-10-19T12:49:55.135Z","lastUpdatedDateTime":"2021-10-19T12:49:55.135Z","chatType":"group","members@odata.context":"https://graph.microsoft.com/v1.0/$metadata#users('b786d3cf-e97d-4511-b61c-xxx')/chats('19%3AtestID%40thread.v2')/members","members":[{"@odata.type":"#microsoft.graph.aadUserConversationMember","id":"test_id","roles":["Owner"],"displayName":"test","visibleHistoryStartDateTime":"0001-01-01T00:00:00Z","userId":"b786d3cf-e97d-4511-b61c-xxx","email":"james.bond@email.com","tenantId":"d48f52ca-5b1a-4708-8ed0-xxxx"},{"@odata.type":"#microsoft.graph.aadUserConversationMember","id":"id example","roles":["Owner"],"displayName":"username","visibleHistoryStartDateTime":"0001-01-01T00:00:00Z","userId":"5af81bea-9c9f-4f9f-8745-xxx","email":null,"tenantId":"d48f52ca-5b1a-4708-8ed0-xxx"},{"@odata.type":"#microsoft.graph.aadUserConversationMember","id":"test id","roles":["Owner"],"displayName":"Test","visibleHistoryStartDateTime":"0001-01-01T00:00:00Z","userId":"cb786032-1ba9-439a-b714-xxxx","email":"TestUserAzure@email.com","tenantId":"d48f52ca-5b1a-4708-8ed0-xxxx"}]},{"id":"19:b786d3cf-e97d-4511-b61c-0559e9f4da75_xxxxx@domain","topic":null,"createdDateTime":"2021-10-13T11:24:15.696Z","lastUpdatedDateTime":"2021-10-13T11:24:15.696Z","chatType":"oneOnOne","members@odata.context":"https://graph.microsoft.com/v1.0/$metadata#users('b786d3cf-e97d-4511-b61c-xxxx')/chats('19%3Ab786d3cf-e97d-4511-b61c-yyyy-1ba9-439a-b714-xxxx%40domain')/members","members":[{"@odata.type":"#microsoft.graph.aadUserConversationMember","id":"xxxx","roles":["Owner"],"displayName":"\u05d2'\u05d9\u05d9\u05de\u05e1 \u05d1\u05d5\u05e0\u05d3","visibleHistoryStartDateTime":"0001-01-01T00:00:00Z","userId":"b786d3cf-e97d-4511-b61c-xxxx","email":"james.bond@email.com","tenantId":"d48f52ca-5b1a-4708-8ed0-xxxx"},{"@odata.type":"#microsoft.graph.aadUserConversationMember","id":"xxxx","roles":["Owner"],"displayName":"Test","visibleHistoryStartDateTime":"0001-01-01T00:00:00Z","userId":"cb786032-1ba9-439a-b714-xxxx","email":"TestUserAzure@email.com","tenantId":"d48f52ca-5b1a-4708-8ed0-xxxx"}]}]
```



#### Send Message Reply
Send a reply to the channel message in Microsoft Teams.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Team Name|Specify the team to which you want to send the reply.|True|String||
|Channel Name|Specify the channel to which you want to send the reply.|True|String||
|Message ID|Specify the ID of the message to which you want to send the reply.|True|String||
|Content Type|Specify the content type for the message.|False|List|Text|
|Text|Specify the content of the message.|True|String||



##### JSON Results
```json
{"@odata.context":"https://graph.microsoft.com/v1.0/$metadata#teams('192c0699-fad2-4d02-88a2-84efd6369894')/channels('19%3A4649fcf41fa5417f9aa78a5840bea442%40thread.tacv2')/messages('1686652339690')/replies/$entity","id":"1686653341151","replyToId":"1686652339690","etag":"1686653341151","messageType":"message","createdDateTime":"2023-06-13T10:49:01.151Z","lastModifiedDateTime":"2023-06-13T10:49:01.151Z","lastEditedDateTime":null,"deletedDateTime":null,"subject":null,"summary":null,"chatId":null,"importance":"normal","locale":"en-us","webUrl":"https://teams.microsoft.com/l/message/19%3A4649fcf41fa5417f9aa78a5840bea442%40thread.tacv2/1686653341151?groupId=192c0699-fad2-4d02-88a2-84efd6369894&tenantId=d48f52ca-5b1a-4708-8ed0-ebb98a26a46a&createdTime=1686653341151&parentMessageId=1686652339690","policyViolation":null,"eventDetail":null,"from":{"application":null,"device":null,"user":{"@odata.type":"#microsoft.graph.teamworkUserIdentity","id":"b786d3cf-e97d-4511-b61c-0559e9f4da75","displayName":"ג'יימסבונד","userIdentityType":"aadUser"}},"body":{"contentType":"text","content":"Reply"},"channelIdentity":{"teamId":"192c0699-fad2-4d02-88a2-84efd6369894","channelId":"19:4649fcf41fa5417f9aa78a5840bea442@thread.tacv2"},"attachments":[],"mentions":[],"reactions":[]}
```



#### Wait For Reply
Action waits for the reply to a specified message. Note: You need to be a part of the desired team and channel. Note: Action is running as async, please adjust script timeout value in Chronicle SOAR IDE for action as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Team Name|Specify name of the team.|True|String||
|Channel Name|Specify name of the channel.|True|String||
|Message ID|Specify ID of the message that is expected to have a reply.|True|String||
|Expected Reply|Specify text of the expected reply. If this value is not provided, then action will stop execution on any reply.|False|String||
|Wait Method|Specify the wait method for the action. If "Check First Reply" is selected, action will either return the first reply or compare the first reply with expected value. If "Wait Till Timeout" is selected, action will either wait for the expected value until timeout is reached or return all of the messages that were sent during the timeout period.|False|List|Check First Reply|



##### JSON Results
```json
{"messages":[{"id":"1234567890123","replyToId":"1234567890122","etag":"1690955630010","messageType":"message","createdDateTime":"2023-08-02T05:53:50.09Z","lastModifiedDateTime":"2023-08-02T05:53:50.09Z","lastEditedDateTime":null,"deletedDateTime":null,"subject":null,"summary":null,"chatId":null,"importance":"normal","locale":"en-us","webUrl":"https://teams.microsoft.com/l/message/xyz","onBehalfOf":null,"policyViolation":null,"eventDetail":null,"from":{"application":null,"device":null,"user":{"@odata.type":"#microsoft.graph.teamworkUserIdentity","id":"test","displayName":"Testing","userIdentityType":"aadUser","tenantId":"testing"}},"body":{"contentType":"text","content":"Yes1"},"channelIdentity":{"teamId":"sampleValue","channelId":"channelValue"},"attachments":[],"mentions":[],"reactions":[]}]}
```



#### Get Team Details
Retrieve the properties of specific team
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Team Name|None|True|String||



##### JSON Results
```json
{}
```



#### Get User Details
Retrieve the properties and relationships of specific user
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Username|None|True|String||



##### JSON Results
```json
{"isResourceAccount": null, "mailNickname": "username.co#EXT#", "surname": null, "deletedDateTime": null, "assignedLicenses": [{"skuId": "16ddbbfc-09ea-4de2-b1d7-312db6112d70", "disabledPlans": []}], "userPrincipalName": "username.co#EXT#@tenant.onmicrosoft.com", "faxNumber": null, "consentProvidedForMinor": null, "userType": "Member", "officeLocation": null, "usageLocation": "IL", "city": null, "employeeId": null, "onPremisesImmutableId": null, "preferredLanguage": null, "streetAddress": null, "@odata.context": "https://graph.microsoft.com/beta/$metadata#users/$entity", "id": "5e457a85-a705-4b65-8a9f-3a3d2ad7715c", "state": null, "businessPhones": [], "postalCode": null, "mail": "john_doe@example.com", "onPremisesSamAccountName": null, "onPremisesLastSyncDateTime": null, "accountEnabled": true, "mobilePhone": null, "refreshTokensValidFromDateTime": "2018-11-12T13:28:53Z", "companyName": null, "deviceKeys": [], "jobTitle": null, "preferredDataLocation": null, "showInAddressList": false, "department": null, "proxyAddresses": ["SMTP:mail"], "externalUserStateChangeDateTime": "2018-11-12T13:29:41Z", "onPremisesProvisioningErrors": [], "legalAgeGroupClassification": null, "onPremisesSyncEnabled": null, "onPremisesExtensionAttributes": {"extensionAttribute4": null, "extensionAttribute5": null, "extensionAttribute6": null, "extensionAttribute7": null, "extensionAttribute12": null, "extensionAttribute1": null, "extensionAttribute2": null, "extensionAttribute3": null, "extensionAttribute10": null, "extensionAttribute11": null, "extensionAttribute8": null, "extensionAttribute9": null, "extensionAttribute14": null, "extensionAttribute15": null, "extensionAttribute13": null}, "assignedPlans": [{"capabilityStatus": "Enabled", "servicePlanId": "617d9209-3b90-4879-96e6-838c42b2701d", "service": "MicrosoftCommunicationsOnline", "assignedDateTime": "2018-11-12T13:28:57Z"}, {"capabilityStatus": "Enabled", "servicePlanId": "902b47e5-dcb2-4fdc-858b-c63a90a2bdb9", "service": "SharePoint", "assignedDateTime": "2018-11-12T13:28:57Z"}, {"capabilityStatus": "Enabled", "servicePlanId": "4fa4026d-ce74-4962-a151-8e96d57ea8e4", "service": "TeamspaceAPI", "assignedDateTime": "2018-11-12T13:28:57Z"}], "passwordProfile": null, "passwordPolicies": null, "externalUserState": "Accepted", "otherMails": ["mail"], "displayName": "name", "imAddresses": [], "provisionedPlans": [{"capabilityStatus": "Enabled", "provisioningStatus": "Success", "service": "SharePoint"}], "createdDateTime": "2018-11-12T13:28:53Z", "country": null, "onPremisesDistinguishedName": null, "onPremisesSecurityIdentifier": null, "onPremisesDomainName": null, "onPremisesUserPrincipalName": null, "givenName": null, "ageGroup": null}
```



#### Delete Channel
Delete a channel in Microsoft Teams.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Team Name|Specify the name of the team in which you need to delete the channel.|True|String||
|Channel Name|Specify a name of the channel that needs to be deleted.|True|String||



#### Remove Users From Channel
Remove users from the private channel in Microsoft Teams. Supported entities: Username, Email Address (username that matches email regex).
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Team Name|Specify the name of the team in which you want to search for the channel.|True|String||
|Channel Name|Specify a name of the channel in which you want to remove users.|True|String||



#### Send User Message
Send a chat message to the user in Microsoft Teams. Supported entities: Username, Email Address (username that matches email regex). Note: Action is running as async if “Wait For Reply” is enabled, please adjust script timeout value in Siemplify IDE for action as needed.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|User Identifiers|Specify a comma-separated list of user identifiers to whom you want to send a message.|False|String||
|Text|Specify the content of the message.|True|String||
|Wait For Reply|If enabled, action will wait until replies from all entities are available.|False|Boolean|true|
|Content Type|Specify the content type for the message.|False|List|Text|
|User Selection|Specify what selection should be used for users. If "From Entities & User Identifiers" is selected, then action will search in both relevant entities and values provided in the "User Identifiers" parameters. If "From Entities" is provided, action will only work with relevant entities and ignore values provided in the "User Identifiers". If "From User Identifiers" is selected, then action will only work with values from "User Identifiers" and "User Identifiers" parameter becomes mandatory.|False|List|From Entities & User Identifiers|



##### JSON Results
```json
[{"Entity":"Test Entity","EntityResult":{"id":"1634205451439","replyToId":null,"etag":"1634205451439","messageType":"message","createdDateTime":"2021-10-14T09:57:31.439Z","lastModifiedDateTime":"2021-10-14T09:57:31.439Z","lastEditedDateTime":null,"deletedDateTime":null,"subject":null,"summary":null,"chatId":"chat ID","importance":"normal","locale":"en-us","webUrl":null,"channelIdentity":null,"policyViolation":null,"from":{"application":null,"device":null,"user":{"id":"user_id","displayName":"","userIdentityType":""}},"body":{"contentType":"text","content":"Message"},"attachments":[],"mentions":[],"reactions":[]}}]
```






## Jobs

#### Refresh Token Renewal Job
Token renewal job should be used to periodically update the refresh token configured for the integration. By default, the refresh token expires every 90 days, making integration unusable upon expiration. It is recommended to run this job every 7 or 14 days to make sure that refresh token will be up to date.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Integration Environments|False|String||



