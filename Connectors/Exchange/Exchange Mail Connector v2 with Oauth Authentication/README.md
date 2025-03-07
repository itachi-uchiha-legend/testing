# Exchange Mail Connector v2 with Oauth Authentication
Connector can be used to monitor specific mailboxes on Office 365 mail servers that require Oauth authentication. Get Authorization and Generate Token actions can be used to obtain refresh token that should be set in the connector. Note: Make sure to configure the integration first for the Oauth authentication.


Integration: Exchange

Integration Version: 107.0

Device Product Field: device_product

Event Name Field: event_name
### Parameters
|Name|Description|Is Mandatory|Value|
|----|-----------|------------|-----|
|Unread Emails Only|If checked, cases will be pulled only from unread emails|False|false|
|Mark Emails as Read|If checked, after the emails have been pulled they will be marked as read|False|false|
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return value unchanged. Used to allow the user to manipulate the environment field via regex logic. If regex pattern is null or empty, or the environment value is null, the final environment result is ""|False||
|Headers to add to events|Specify what headers from emails should be added to the events. Parameter accepts multiple values as a comma separated string. Provided values can be exact match or set as a regex.|False||
|Email exclude pattern|Regular expression to exclude specific emails from being ingested by the connector. Works with both subject and body part of email. Example is, to exclude mass mailing emails like news from being ingested.|False||
|Original Received Mail Prefix|Prefix to add to the extracted event keys (to, from,subject,…) from the original email received in the monitored mailbox.|False|orig|
|Attached Mail File Prefix|Prefix to add to the extracted event keys (to, from,subject,…) from the attached mail file received with the email in the monitored mailbox.|False|attach|
|Create a Separate Siemplify Alert per Attached Mail File?|If enabled, connector will create multiple alerts, 1 alert per attached mail file. This behavior can be useful when processing email with multiple mail files attached and Siemplify event mapping set to create entities from attached mail file.|False|false|
|Mail Server Address|Mail server IP address to connect to. If connecting to O365, server address should be set to outlook.office365.com|True|outlook.office365.com|
|Mail Address|Mail address to use for connector.|True|james.bond@siemplifycyarx.onmicrosoft.com|
|Client ID|For Office 365 Oauth authentication, Client (Application) ID of Azure Active Directory App that will be used for the integration.|True|93107771-ca33-4d31-8059-535c7481368a|
|Client Secret|For Office 365 Oauth authentication, secret can be provided for the auth flow.|False|***************|
|Tenant (Directory) ID|For Office 365 Oauth authentication, Azure Tenant (Directory) ID.|True|d48f52ca-5b1a-4708-8ed0-ebb98a26a46a|
|Refresh Token|For Office 365 Oauth authentication, refresh token that was obtained from running “Get Authorization” and “Generate Token” actions.|True|***************|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Exchange server is valid.|False|false|
|Folder to check for emails|Parameter can be used to specify email folder on the mailbox to search for the emails. Parameter should also accept comma separated list of folders to check the user response in multiple folders. Parameter is case sensitive. '/' separator can be used to specify a subfolder to search in, example: Inbox/Subfolder|True|a9|
|Use Delegated Access|If enabled, delegated access type will be used. Otherwise, impersonation access type is used. For details on impersonation/delegation and EWS, see the following link https://learn.microsoft.com/en-us/exchange/client-developer/exchange-web-services/impersonation-and-ews-in-exchange.|False|false|
|Offset Time In Days|Number of days before the first connector iteration to retrieve mails from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|True|5|
|Fetch Backwards Time Interval (minutes)|Time interval connector should use to fetch events from max hours backwards or connector last run timestamp. This parameter in minutes can be used to split max hours backwards on smaller segments and process them individually. Its recommended to adjust this value accordingly to the environment, for example 60 minutes or less.|False|0|
|Max Emails Per Cycle|Fetch x emails per connector cycle|True|10|
|Proxy Server Address|The address of the proxy server to use.|False|http://0.0.0.0:8866/|
|Proxy Username|The proxy username to authenticate with.|False||
|Proxy Password|The proxy password to authenticate with.|False||
|Extract urls from HTML email part?|Specify whether connector should additionally try to extract urls from html part of email. This will allow connector to extract complex urls, but urls from plain text part of email will not be extracted with this method. Extracted urls will be available in urls_from_html_part event field.|False|false|
|Disable Overflow|If enabled, the connector will ignore the overflow mechanism.|False|false|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False||
|Script Timeout (Seconds)|Timeout limit for the python process running the current script.|True|60|
|Attach Original EML|If checked, the original email will be attached to the case info as an eml file|False|false|
|Case Name Template|When provided, connector will add a new key called "custom_case_name" to the Siemplify Event. It can used to have a customer case name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Siemplify Event for placeholders. Only keys that have string value will be handled.|False||
|Alert Name Template|If provided, connector will use this value for Siemplify Alert Name. Please refer to the documentation portal for more details. You can provide placeholders in the following format: [name of the field]. Example: Phishing - [event_mailbox]. Note: connector will use first Siemplify Event for placeholders. Only keys that have string value will be handled. If nothing is provided or user provides an invalid template, connector will use the default alert name.|False||
|Email Padding Period (minutes)|Specify an optional time period in minutes connector should fetch emails for prior to the latest timestamp.|False|0|
|Base64 Encoded Private Key|Specify a base64 encoded private key that will be used to decrypt the email.|False||
|Base64 Encoded Certificate|Specify a base64 encoded certificate that will be used to decrypt the email.|False||
|Base64 Encoded CA certificate|Specify a base64 encoded trusted CA certificate for signature verification.|False||

