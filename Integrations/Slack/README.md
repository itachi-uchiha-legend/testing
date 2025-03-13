<p align="center"><img src="./Resources/Slack.svg" 
     alt="Slack" width="200"/></p>

# Slack

Slack is where work flows. It's where the people you need, the information you share, and the tools you use come together to get things done.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Api Token|None|True|Password|None|
|Bolt Token|None|True|Password|None|
|Webhook Base URL|None|False|String||
|Verify SSL|None|False|Boolean|False|



## Actions
#### List Channels
Get a list of Slack channels based on the provided criteria. Note that action is not working on Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Max Channels to Return|Specify how many channels to return.|False|String|20|
|Type Filter|Specify what type of conversations to return. Example: public_channel,private_channel. Possible Values: public_channel, private_channel, mpim, im.|False|String|public_channel|
|Filter Key|Specify the key that needs to be used to filter channels.|False|List|Select One|
|Filter Value|Specify what value should be used in the filter. If “Equal“ is selected, action will try to find the exact match among results and if “Contains“ is selected, action will try to find results that contain that substring. If nothing is provided in this parameter, the filter will not be applied. Filtering logic is working based on the value  provided in the “Filter Key” parameter.|False|String||
|Filter Logic|Specify what filter logic should be applied. Filtering logic is working based on the value  provided in the “Filter Key” parameter.|False|List|Not Specified|



##### JSON Results
```json
[{"is_general": false, "name_normalized": "project_old", "is_channel": true, "creator": "U0136KZ0xxx", "is_member": true, "is_archived": false, "topic": {"last_set": 0, "value": "", "creator": ""}, "parent_conversation": null, "is_im": false, "is_ext_shared": false, "previous_names": ["project_new", "project"], "id": "C013ELA1xxx", "is_org_shared": false, "pending_connected_team_ids": [], "is_pending_ext_shared": false, "is_mpim": false, "is_group": false, "shared_team_ids": ["T013MJHSxxx"], "purpose": {"last_set": 1589444943, "value": "This *channel* is for working on a project. Hold meetings, share docs, and make decisions together with your team.", "creator": "U0136KZ0xxx"}, "is_private": false, "is_shared": false, "num_members": 4, "name": "project_old", "created": 1589444943, "pending_shared": [], "unlinked": 0}]
```



#### Get User Details By Id
Fetch Slack user account details. Note that action is not working on Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|User Id|Specify user account id to fetch details for. User ID can be found by running “List Users“ action.|True|String||



##### JSON Results
```json
{"profile": {"status_expiration": 0, "display_name": "", "status_emoji": "", "avatar_hash": "g2d62053d7f7", "title": "", "fields": null, "status_text_canonical": "", "skype": "", "real_name": "somerealname", "image_24": "https://secure.gravatar.com/avatar/2d62053d7f735bc096de59639eb8f350.jpg?s=24&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0022-24.png", "phone": "", "real_name_normalized": "realnamen", "image_512": "https://secure.gravatar.com/avatar/2d62053d7f735bc096de59639eb8f350.jpg?s=512&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0022-512.png", "display_name_normalized": "", "image_32": "https://secure.gravatar.com/avatar/2d62053d7f735bc096de59639eb8f350.jpg?s=32&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0022-32.png", "image_48": "https://secure.gravatar.com/avatar/2d62053d7f735bc096de59639eb8f350.jpg?s=48&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0022-48.png", "team": "TRALP6VNY", "image_72": "https://secure.gravatar.com/avatar/2d62053d7f735bc096de59639eb8f350.jpg?s=72&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0022-72.png", "status_text": "", "email": "example.user@example.com", "image_192": "https://secure.gravatar.com/avatar/2d62053d7f735bc096de59639eb8f350.jpg?s=192&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0022-192.png"}, "updated": 1575550598, "tz": "Europe/Europe", "name": "name", "deleted": false, "is_app_user": false, "is_bot": false, "tz_label": "Central European Summer Time", "real_name": "real_name", "is_primary_owner": true, "color": "9f69e7", "team_id": "TRALP6VNY", "is_admin": true, "is_ultra_restricted": false, "is_restricted": false, "tz_offset": 14400, "has_2fa": false, "id": "URALP6WRJ", "is_owner": true}
```



#### Build Block
Build a slack message block based on provided input criteria. Action creates a block with a webhook that can be later passed to the 'Send Interactive Message' to send a message with. Note that action is not working on Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Question|Specify the question text to add to the block.|True|String||
|Answers Buttons|Specify the answer buttons to add to the block.|True|String||
|Siemplify Base URL|Specify the Siemplify server base url to add to the block.|True|String||
|Case ID|Specify the Siemplify case id to add to the block.|True|String||
|Webhook Token UUID|Specify the Webhook token UUID to monitor for the user’s response.|True|String||



##### JSON Results
```json
{"result": "[{\"type\": \"section\", \"block_id\": \"f99958f1-c1f1-4fdb-bb8b-a382d952d5bd\", \"text\": {\"type\": \"mrkdwn\", \"text\": \"yes?\", \"verbatim\": false}},{\"type\": \"actions\", \"block_id\": \"2850e684-472a-472f-9a32-96294cbe9046\", \"elements\": [{\"type\": \"button\", \"text\": {\"type\": \"plain_text\", \"text\": \"y\"}, \"action_id\": \"y\", \"url\": \"https://webhook.site/token/47289ba5-277e-4ab9-9238-xx00000000xx?Answer=y\"}, {\"type\": \"button\", \"text\": {\"type\": \"plain_text\", \"text\": \"n\"}, \"action_id\": \"n\", \"url\": \"https://webhook.site/token/47289ba5-277e-4ab9-9238-xx00000000xx?Answer=n\"}, {\"type\": \"button\", \"text\": {\"type\": \"plain_text\", \"text\": \"View Case in Siemplify\"}, \"action_id\": \"View Case in Siemplify\", \"url\": \"https://something/main/cases/dynamic-view/1\"}]}]"}
```



#### Create Channel
Create a channel in Slack. Note that action is not working on Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Channel Name|Specify the name of the channel. Note: Channel names may only contain lowercase letters, numbers, hyphens, and underscores, and must be 80 characters or less.|True|String||
|User IDs|Specify the ids of the users that should be invited to the newly created channel. Example: U014JDHLW87, U08544ABC85. Parameter accepts multiple values as a comma separated list. Note: if both “User IDs” and “User Emails” are specified, action will only work with IDs.|False|String||
|Is Private|If enabled, action will create a private channel.|False|Boolean|False|
|User Emails|Specify the emails of users that should be invited to the newly created channel. Parameter accepts multiple values as a comma separated list. Note: if both “User IDs” and “User Emails” are specified, action will only work with IDs.|False|String||



##### JSON Results
```json
{"is_general": "False", "name_normalized": "12asd1237712318", "is_channel": "True", "creator": "U014J4NFQQG", "is_member": "True", "is_archived": "False", "topic": {"last_set": "0", "value": "", "creator": ""}, "parent_conversation": "None", "is_im": "False", "is_ext_shared": "False", "previous_names": [], "last_read": "0000000000.000000", "id": "C014S1G6DB4", "is_org_shared": "False", "pending_connected_team_ids": [], "is_pending_ext_shared": "False", "is_mpim": "False", "is_group": "False", "shared_team_ids": ["T013MJHSNCT"], "purpose": {"last_set": 0, "value": "", "creator": ""}, "is_private": "False", "is_shared": "False", "name": "12asd1237712318", "created": "1591194197", "pending_shared": [], "unlinked": 0, "priority": 0}
```



#### Wait For Reply
Wait for a thread reply to a message previously sent with a 'Send Message' or 'Send Advanced Message' actions. Note: action is async, please adjust the timeout for action in Siemplify IDE. Action is not running on Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Channel|Specify the channel name in which to track reply for the message. Note: if both Channel and Channel ID are specified, action will only work with ID.|False|String||
|Channel ID|Specify the id of the channel, in which to track reply for the message. Note: if both Channel and Channel ID are specified, action will only work with ID.|False|String||
|Message Timestamp|Specify the timestamp of the message to track. Timestamp can be found in the Send Message action json result as ts key.|True|String||
|Wait for Multiple Replies|If enabled, action should wait for multiple responses  until action timeout. Otherwise, action finishes running after getting first reply to the message.|False|Boolean|false|



##### JSON Results
```json
{"client_msg_id": "00000000-0000-0000-0000-000000000000", "type": "message", "text": "Yes", "user": "U0000000", "ts": "1578390603.001200", "team": "T0000000", "blocks": [{"type": "rich_text", "block_id": "2Bb=", "elements": [{"type": "rich_text_section", "elements": [{"type": "text", "text": "Example"}]}]}], "thread_ts": "1578390492.001100", "parent_user_id": "U0000000"}
```



#### Ping
Test connectivity to the Slack instance with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### Send Message
Send a message to a Slack channel or user. Note that action is not working on Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Channel|Specify the name of the Slack channel or the email address of the user to whom to send the message. Parameter accepts multiple values as a comma-separated string.|True|String||
|Message|Specify the message content to send.|True|String||



##### JSON Results
```json
[{"EntityResult": {"message": {"text": "Test message", "ts": "1594730989.000200", "bot_profile": {"updated": 1578312330, "name": "Test", "icons": {"image_36": "https://a.slack-edge.com/80588/img/plugins/app/bot_36.png", "image_48": "https://a.slack-edge.com/80588/img/plugins/app/bot_48.png", "image_72": "https://a.slack-edge.com/80588/img/plugins/app/service_72.png"}, "deleted": false, "app_id": "12345678", "team_id": "12345678", "id": "12345678"}, "user": "12345678", "team": "12345678", "type": "message", "bot_id": "12345678"}, "ok": true, "ts": "1594730989.000200", "channel": "12345678"}, "Entity": "test"}]
```



#### Upload File
Add files to Slack and share them with your teammates to help you collaborate. Uploaded files are stored, searchable, and shareable across your workspace. Note that action is not working on Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|File Name|Specify the name(title) that should be used to show in Slack for the uploaded file.|True|String||
|File Path|Specify the full file path on the Siemplify server for the file to upload.|True|String||
|Channel|Specify the name of the Slack channel or the email address of the user to whom to send the message.|True|String||



#### Send Advanced Message
Send an advanced message to a Slack channel or user. Action provides an ability to send 'simple' text messages and 'rich' Slack block messages with buttons, advanced formatting and more. Please see https://api.slack.com/block-kit for the block messages reference. Note that action is not working on Siemplify entities. This action can be used together with the 'Wait for Reply With Webhook' action to first send a 'block' message with a webhook to a user, and when later with 'Wait for Reply With Webhook' action check for a user's response.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Recipient|Specify the recipient to send a message to.|True|String||
|Recipient Type|Specify channel or user name (full name) to send message to. Optionally channel or user id can be specified, or email address of a user.|True|List|Name|
|Message|Specify the message content to send.|True|String||
|Message Type|Specify the message type to send.|True|List|Text|



##### JSON Results
```json
[{"Entity": "U043FPEMATG", "EntityResult": {"channel": "D044C3DUMB2", "message": {"bot_id": "B02D9QYM7P0", "type": "message", "text": "test msg", "user": "U02D1RPLVST", "ts": "1666008612.116169", "app_id": "A02DDGD942Z", "team": "T02CX3N6B0B", "bot_profile": {"id": "B02D9QYM7P0", "app_id": "A02DDGD942Z", "name": "test", "icons": {"image_36": "https://a.slack-edge.com/80588/img/plugins/app/bot_36.png", "image_48": "https://a.slack-edge.com/80588/img/plugins/app/bot_48.png", "image_72": "https://a.slack-edge.com/80588/img/plugins/app/service_72.png"}, "deleted": false, "updated": 1630908872, "team_id": "T02CX3N6B0B"}, "blocks": [{"type": "rich_text", "block_id": "RJvg", "elements": [{"type": "rich_text_section", "elements": [{"type": "text", "text": "test msg"}]}]}]}, "ts": "1666008612.116169", "ok": true}}]
```



#### Send Interactive Message
Send an interactive message to a channel or a user and when based on the provided Webhook UUID check a user's response. Action is similar to the 'Send Advanced Message' action, but it allows to send only 'block' content (not plain text messages) and also requires a webhook UUID to check a user's response to a webhook. Action is async, please adjust action timeout in IDE accordingly. Action is not working on Siemplify entities. Please configure the Slack app used in integration to allow interactive messages as described here - https://api.slack.com/legacy/interactive-messages#readying_app.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Recipient|Specify the recipient to send a message to.|True|String||
|Recipient Type|Specify channel or user name (full name) to send message to. Optionally channel or user id can be specified, or email address of a user.|True|List|Name|
|Message|Specify the message content to send.|True|String||
|Webhook Token UUID|Specify the Webhook token UUID to monitor for the user’s response.|True|String||



##### JSON Results
```json
[{"uuid": "10953f8e-7ef8-4bde-9e9b-212005e0e737", "type": "web", "token_id": "47289ba5-277e-4ab9-9238-eb31080530ca", "ip": "0000:a000000:ad80:000:20ea:653:fb97", "hostname": "webhook.site", "method": "GET", "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15", "content": "", "query": {"Answer": "yes"}, "headers": {"connection": ["close"], "accept-encoding": ["gzip, deflate, br"], "accept-language": ["en-US,en;q=0.9"], "user-agent": ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"], "cookie": ["_ga=GA"], "accept": ["text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"], "host": ["webhook.site"], "content-length": [""], "content-type": [""]}, "url": "https://webhook.site/47289ba5-277e-4ab9-9238-xx0000000xx?Answer=yes", "size": 0, "files": [], "created_at": "2022-10-14 19:45:40", "updated_at": "2022-10-14 19:45:40", "sorting": 1665776740032262, "custom_action_output": []}]
```



#### Get User Details
Get Slack user details based on provided input criteria. Note: that action is not working on Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Search By|Specify the parameter to search user details by.|True|List|Email|
|User Value|Specify the user value to search by.|True|String||



##### JSON Results
```json
{"id": "U043FPEMATG", "team_id": "T02CX3N6B0B", "name": "example.user", "deleted": false, "color": "3c989f", "real_name": "Example User", "tz": "Europe/Europe", "tz_label": "Central European Summer Time", "tz_offset": 7200, "profile": {"title": "", "phone": "", "skype": "", "real_name": "Example User", "real_name_normalized": "Example User", "display_name": "Example User", "display_name_normalized": "Example User", "fields": null, "status_text": "", "status_emoji": "", "status_emoji_display_info": [], "status_expiration": 0, "avatar_hash": "gc297456197c", "email": "example.user@example.com", "first_name": "Example", "last_name": "User", "image_24": "https://secure.gravatar.com/avatar/c297456197c0de7baa8c4b9a2398ecd1.jpg?s=24&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0011-24.png", "image_32": "https://secure.gravatar.com/avatar/c297456197c0de7baa8c4b9a2398ecd1.jpg?s=32&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0011-32.png", "image_48": "https://secure.gravatar.com/avatar/c297456197c0de7baa8c4b9a2398ecd1.jpg?s=48&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0011-48.png", "image_72": "https://secure.gravatar.com/avatar/c297456197c0de7baa8c4b9a2398ecd1.jpg?s=72&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0011-72.png", "image_192": "https://secure.gravatar.com/avatar/c297456197c0de7baa8c4b9a2398ecd1.jpg?s=192&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0011-192.png", "image_512": "https://secure.gravatar.com/avatar/c297456197c0de7baa8c4b9a2398ecd1.jpg?s=512&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0011-512.png", "status_text_canonical": "", "team": "T02CX3N6B0B"}, "is_admin": false, "is_owner": false, "is_primary_owner": false, "is_restricted": false, "is_ultra_restricted": false, "is_bot": false, "is_app_user": false, "updated": 1663939355, "is_email_confirmed": true, "who_can_share_contact_card": "EVERYONE"}
```



#### Rename Channel
Rename the specified Slack channel. Note that action is not working on Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Channel Name|Specify the name of the channel, which you want to rename. Note: if both “Channel Name” and “Channel ID” are specified, action will only work with ID. |False|String||
|Channel ID|Specify the id of the channel, which you want to rename. Note: if both “Channel Name” and “Channel ID” are specified, action will only work with ID. |False|String||
|New Name|Specify what should be a new name for the channel. Note: Channel names may only contain lowercase letters, numbers, hyphens, and underscores, and must be 80 characters or less.|True|String||



##### JSON Results
```json
{"is_general": false, "name_normalized": "piskovisko_new1", "is_channel": true, "creator": "U0136KZ0XXX", "is_member": true, "is_archived": false, "topic": {"last_set": 0, "value": "", "creator": ""}, "parent_conversation": null, "is_im": false, "is_ext_shared": false, "previous_names": ["piskovisko_new1", "piskovisko_new", "piskovisko4445", "piskovisko4", "piskovisko4", "piskovisko3", "piskovisko3", "piskovisko3", "piskovisko3", "piskovisko2"], "last_read": "1604669453.001200", "id": "C01EWBPXXXX", "is_org_shared": false, "pending_connected_team_ids": [], "is_pending_ext_shared": false, "is_mpim": false, "is_group": false, "shared_team_ids": ["T013MJHSXXX"], "purpose": {"last_set": 0, "value": "", "creator": ""}, "is_private": false, "is_shared": false, "name": "piskovisko_new1", "created": 1604668934, "pending_shared": [], "unlinked": 0}
```



#### Wait For Reply With Webhook
Wait for a User reply to a message sent with a webhook - action periodically check the provided webhook to see if the User had provided any reply to it. Action can be used with the 'Send Advanced Message' action, if the block message with webhook was sent, to check if the user's response was provided to the webhook. Note: action is async, please adjust the timeout for action in Siemplify IDE. Action is not running on Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Webhook Token UUID|Specify the Webhook token UUID to monitor for the user’s response.|True|String||



##### JSON Results
```json
{"uuid": "10953f8e-7ef8-4bde-9e9b-212005e0e737", "type": "web", "token_id": "47289ba5-277e-4ab9-9238-eb31080530ca", "ip": "0000:a000000:ad80:000:20ea:653:fb97", "hostname": "webhook.site", "method": "GET", "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15", "content": "", "query": {"Answer": "yes"}, "headers": {"connection": ["close"], "accept-encoding": ["gzip, deflate, br"], "accept-language": ["en-US,en;q=0.9"], "user-agent": ["Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15"], "cookie": ["_ga=GA"], "accept": ["text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"], "host": ["webhook.site"], "content-length": [""], "content-type": [""]}, "url": "https://webhook.site/47289ba5-277e-4ab9-9238-xx0000000xx?Answer=yes", "size": 0, "files": [], "created_at": "2022-10-14 19:45:40", "updated_at": "2022-10-14 19:45:40", "sorting": 1665776740032262, "custom_action_output": []}
```



#### List Users
Get a list of Slack users based on the provided criteria. Note that action is not working on Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Max Records to Return|Specify how many user accounts to return.|False|String|20|
|Filter Key|Specify the key that needs to be used to filter user accounts.|False|List|Select One|
|Filter Value|Specify what value should be used in the filter. If “Equal“ is selected, action will try to find the exact match among results and if “Contains“ is selected, action will try to find results that contain that substring. If nothing is provided in this parameter, the filter will not be applied. Filtering logic is working based on the value  provided in the “Filter Key” parameter.|False|String||
|Filter Logic|Specify what filter logic should be applied. Filtering logic is working based on the value  provided in the “Filter Key” parameter.|False|List|Not Specified|



##### JSON Results
```json
[{"profile": {"status_text": "", "display_name": "", "status_emoji": "", "title": "", "status_text_canonical": "", "team": "TRALP6VNY", "real_name": "somerealname", "image_24": "https://secure.gravatar.com/avatar/2d62053d7f735bc096de59639eb8f350.jpg?s=24&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0022-24.png", "phone": "", "real_name_normalized": "somerealnamen", "image_512": "https://secure.gravatar.com/avatar/2d62053d7f735bc096de59639eb8f350.jpg?s=512&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0022-512.png", "image_72": "https://secure.gravatar.com/avatar/2d62053d7f735bc096de59639eb8f350.jpg?s=72&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0022-72.png", "image_32": "https://secure.gravatar.com/avatar/2d62053d7f735bc096de59639eb8f350.jpg?s=32&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0022-32.png", "image_48": "https://secure.gravatar.com/avatar/2d62053d7f735bc096de59639eb8f350.jpg?s=48&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0022-48.png", "skype": "", "avatar_hash": "g2d62053d7f7", "display_name_normalized": "", "status_expiration": 0, "email": "example.user@example.com", "image_192": "https://secure.gravatar.com/avatar/2d62053d7f735bc096de59639eb8f350.jpg?s=192&d=https%3A%2F%2Fa.slack-edge.com%2Fdf10d%2Fimg%2Favatars%2Fava_0022-192.png"}, "updated": 1575550598, "tz": "Europe/Europe", "name": "name", "deleted": false, "is_app_user": false, "is_bot": false, "tz_label": "Central European Summer Time", "real_name": "realname", "color": "9f69e7", "team_id": "TRALP6VNY", "is_admin": true, "is_ultra_restricted": false, "is_restricted": false, "is_owner": true, "tz_offset": 14400, "has_2fa": false, "id": "URALP6WRJ", "is_primary_owner": true}, {"profile": {"last_name": "", "status_emoji": "", "display_name_normalized": "Slackbot", "image_32": "https://a.slack-edge.com/80588/img/slackbot_32.png", "skype": "", "image_72": "https://a.slack-edge.com/80588/img/slackbot_72.png", "status_expiration": 0, "image_192": "https://a.slack-edge.com/80588/marketing/img/avatars/slackbot/avatar-slackbot.png", "first_name": "slackbot", "display_name": "Slackbot", "title": "", "real_name_normalized": "Slackbot", "always_active": true, "status_text_canonical": "", "image_24": "https://a.slack-edge.com/80588/img/slackbot_24.png", "phone": "", "image_48": "https://a.slack-edge.com/80588/img/slackbot_48.png", "fields": null, "real_name": "Slackbot", "image_512": "https://a.slack-edge.com/80588/img/slackbot_512.png", "team": "TRALP6VNY", "avatar_hash": "sv41d8cd98f0", "status_text": ""}, "updated": 0, "tz": null, "name": "slackbot", "deleted": false, "is_app_user": false, "is_bot": false, "tz_label": "Pacific Standard Time", "real_name": "Slackbot", "color": "757575", "team_id": "TRALP6VNY", "is_admin": false, "is_ultra_restricted": false, "is_restricted": false, "is_owner": false, "tz_offset": -28800, "id": "USLACKBOT", "is_primary_owner": false}]
```



#### Get Channel Or User Conversation History
Get conversation history for a user or a channel based on provided input criteria. Action works with either channel or user id, which could be searched with either 'List Channels' or 'List User' actions. Note that action is not working on Siemplify entities.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Channel or User ID|Specify the channel or user id to fetch the conversation history for.|True|String||
|Time Frame|Specify a time frame for the results. If Custom is selected, you also need to provide Start Time.|False|List|Last Hour|
|Start Time|Specify the start time for the results. This parameter is mandatory, if Custom is selected for the Time Frame parameter. 'Format: ISO 8601. Example: 2021-08-05T05:18:42Z'|False|String||
|End Time|Specify the end time for the results. 'Format: ISO 8601. Example: 2021-08-05T05:18:42Z'. If nothing is provided and Custom is selected for the Time Frame parameter then this parameter will use current time.|False|String||
|Max Records to Return|Specify how many records to return. If nothing is provided, action will return 20 records.|False|String|20|



##### JSON Results
```json
[{"bot_id": "B02D9QYM7P0", "type": "message", "text": "test", "user": "U02D1RPLVST", "ts": "1665988448.627219", "app_id": "A02DDGD942Z", "team": "T02CX3N6B0B", "bot_profile": {"id": "B02D9QYM7P0", "deleted": false, "name": "Siemplify-test", "updated": 1630908872, "app_id": "A02DDGD942Z", "icons": {"image_36": "https://a.slack-edge.com/80588/img/plugins/app/bot_36.png", "image_48": "https://a.slack-edge.com/80588/img/plugins/app/bot_48.png", "image_72": "https://a.slack-edge.com/80588/img/plugins/app/service_72.png"}, "team_id": "T02CX3N6B0B"}, "blocks": [{"type": "rich_text", "block_id": "JbVUf", "elements": [{"type": "rich_text_section", "elements": [{"type": "text", "text": "test"}]}]}]}]
```



#### Ask Question
Ask question in Slack. Note: this action will be deprecated in the future integration's versions and replaced with actions providing enhanced functionality.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Channel|Target channel.|True|String||
|Question|Question content.|True|String||









