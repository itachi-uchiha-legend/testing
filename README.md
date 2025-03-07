# GitSync

## Integrations
|Name|Description|
|----|-----------|
|Vmware Carbon Black Cloud|The VMware Carbon Black Cloud is a cloud-native endpoint protection platform (EPP) that combines the intelligent system hardening and behavioral prevention needed to keep emerging threats at bay, using a single lightweight agent, and an easy-to-use console.|
|Carbon Black Response|Highly scalable, real-time EDR with unparalleled visibility for top security operations centers and incident response teams|
|Exchange|Integration provides support for Microsoft Exchange 2010 - 2019 and Microsoft Office365 mail servers. Integration uses Exchange Web Services (EWS) for communication. Integration includes a series of actions to send out emails and work with received emails, along with a connector to monitor specific mailboxes and ingest emails from that mailboxes as alerts to Google SecOps for further analysis.|
|GitSyncBeta|Sync Google SecOps integrations, playbooks, and settings with a GitHub, BitBucket or GitLab instance|
|Google Chronicle|Google SecOps enables you to examine the aggregated security information for your enterprise going back for months or longer. Use Google SecOps to search across all of the domains accessed from within your enterprise. To enable the Google API client to communicate with the Backstory API you will need Google Developer Service Account Credential, https://developers.google.com/identity/protocols/OAuth2#serviceaccount.|
|Microsoft Graph Mail|Microsoft 365 and Office 365 deliver the power of cloud productivity to businesses of all sizes, helping save time, money, and free up valued resources. The Microsoft 365 and Office 365 plans combine the familiar Microsoft Office desktop suite with cloud-based versions of Microsoft's next-generation communications and collaboration services (including Office for the web, Microsoft Exchange Online, Microsoft Teams, and Microsoft SharePoint Online) to help users be productive from virtually anywhere through the Internet. This integration uses Microsoft Graph Mail API to communicate with Microsoft 365 and Office 365 services.|
|Microsoft Graph Mail Delegated|This integration version uses Delegated Authentication in Microsoft 365 and requires interactive login of the user on behalf of which integration should communicate with Microsoft 365. To configure this integration, provide all parameters except for Refresh Token, and save the integration configuration, then run “Get Authorization” and “Generate Token” actions to get the token and then provide it in integration configuration to finish the process. Microsoft 365 and Office 365 deliver the power of cloud productivity to businesses of all sizes, helping save time, money, and free up valued resources. The Microsoft 365 and Office 365 plans combine the familiar Microsoft Office desktop suite with cloud-based versions of Microsoft's next-generation communications and collaboration services (including Office for the web, Microsoft Exchange Online, Microsoft Teams, and Microsoft SharePoint Online) to help users be productive from virtually anywhere through the Internet. This integration uses Microsoft Graph Mail API to communicate with Microsoft 365 and Office 365 services.|
|Netskope|The Netskope Security Cloud helps the world’s largest organizations take full advantage of the cloud and web without sacrificing security.|
|Siemplify ThreatFuse|ThreatFuse combines best-in-class security orchestration, automation and response (SOAR) with a market-leading Threat Intelligence Platform (TIP) powered by Anomali, to make intelligence-driven security operations simple and accessible for organizations of all sizes.With robust integration out of the box, ThreatFuse ingrains threat-intelligence across the entire detection and response lifecycle. From enrichment with real-time threat indicators, through threat-hunting and intelligence sharing, security analysts can validate, investigate and respond to threats with unprecedented speed and precision.|
|Varonis Data Security Platform|Capture and search every important action at petabyte scale. Varonis creates a normalized record of every important action on your data—on-premises and in the cloud.|
|VirusTotalV3|VirusTotal was founded in 2004 as a free service that analyzes files and URLs for viruses, worms, trojans and other kinds of malicious content. Our goal is to make the internet a safer place through collaboration between members of the antivirus industry, researchers and end users of all kinds. Fortune 500 companies, governments and leading security companies are all part of the VirusTotal community, which has grown to over 500,000 registered users.This integration was created using the 3rd iteration of VT API.|


## Connectors
|Name|Description|Has Mappings|
|----|-----------|------------|
|VMware Carbon Black Cloud Alerts and Events Baseline Connector|Fetch Carbon Black Cloud Alerts and Events that reached specific baseline (were classified by default as Threat in Carbon Black Cloud)|False|
|Exchange Mail Connector v2 with Oauth Authentication|Connector can be used to monitor specific mailboxes on Office 365 mail servers that require Oauth authentication. Get Authorization and Generate Token actions can be used to obtain refresh token that should be set in the connector. Note: Make sure to configure the integration first for the Oauth authentication.|True|


## Playbooks
|Name|Description|
|----|-----------|
|New Playbook||
|New Playbook 1||


## Jobs
|Name|Description|
|----|-----------|
|Pull Content GitSyncBeta|Installs content from the repo.|
|Push Content GitSyncBeta|Push all content of this platform to git|
|Push Content GitSyncBeta1|Push all content of this platform to git|

