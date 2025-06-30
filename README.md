# GitSync

## Integrations
|Name|Description|
|----|-----------|
|Vmware Carbon Black Cloud|The VMware Carbon Black Cloud is a cloud-native endpoint protection platform (EPP) that combines the intelligent system hardening and behavioral prevention needed to keep emerging threats at bay, using a single lightweight agent, and an easy-to-use console.|
|Carbon Black Response|Highly scalable, real-time EDR with unparalleled visibility for top security operations centers and incident response teams|
|Cisco Firepower Management Center|Cisco Firepower analyzes your network's vulnerabilities, prioritizes any attacks, and recommends protections so your security team can focus on strategic activities.|
|Cofense Triage|With Cofense Triage, prioritize and remediate phishing threats faster. A culture of user-reporting is key to stopping phishing attacks, but your overburdened SOC team needs to prioritize what’s reported. Instead of slowing their efforts with time consuming manual processes—the numerous steps required to find and understand real indicators of threats—automate analysis with Cofense Triage and focus on making decisions to speed remediation.|
|CrowdStrike Falcon|CrowdStrike Falcon is the leader in next-generation endpoint protection, threat intelligence and incident response through cloud-based endpoint protection.|
|CyberX|The most widely-deployed ICS, SCADA & IIoT security platform that continuously reduces OT network risk via ICS threat monitoring & asset discovery.|
|CyberArk Credential Provider|CyberArk’s Secrets Manager Credential Providers, part of the Privileged Access Security solution, is used to eliminate hard coded application credentials embedded in applications, scripts or configuration files, and allows these highly-sensitive passwords to be centrally stored, logged and managed within the Vault.|
|EmailUtilities|A set of utility actions to assist with working with emails.  Includes actions to parse EMLs and analyze email headers.|
|Exchange|Integration provides support for Microsoft Exchange 2010 - 2019 and Microsoft Office365 mail servers. Integration uses Exchange Web Services (EWS) for communication. Integration includes a series of actions to send out emails and work with received emails, along with a connector to monitor specific mailboxes and ingest emails from that mailboxes as alerts to Google SecOps for further analysis.|
|GitSyncBeta|Sync Google SecOps integrations, playbooks, and settings with a GitHub, BitBucket or GitLab instance|
|Google Chronicle|Google SecOps enables you to examine the aggregated security information for your enterprise going back for months or longer. Use Google SecOps to search across all of the domains accessed from within your enterprise. To enable the Google API client to communicate with the Backstory API you will need Google Developer Service Account Credential, https://developers.google.com/identity/protocols/OAuth2#serviceaccount.|
|Jira|Jira Software is part of a family of products designed to help teams of all types manage work. Originally, Jira was designed as a bug and issue tracker. But today, Jira has evolved into a powerful work management tool for all kinds of use cases, from requirements and test case management to agile software development. Jira will be the perfect fit for: requirements & test case management, agile teams, project management teams, software development teams, product management teams, task management, bug tracking and much more...|
|Microsoft Graph Mail|Microsoft 365 and Office 365 deliver the power of cloud productivity to businesses of all sizes, helping save time, money, and free up valued resources. The Microsoft 365 and Office 365 plans combine the familiar Microsoft Office desktop suite with cloud-based versions of Microsoft's next-generation communications and collaboration services (including Office for the web, Microsoft Exchange Online, Microsoft Teams, and Microsoft SharePoint Online) to help users be productive from virtually anywhere through the Internet. This integration uses Microsoft Graph Mail API to communicate with Microsoft 365 and Office 365 services.|
|Microsoft Graph Mail Delegated|This integration version uses Delegated Authentication in Microsoft 365 and requires interactive login of the user on behalf of which integration should communicate with Microsoft 365. To configure this integration, provide all parameters except for Refresh Token, and save the integration configuration, then run “Get Authorization” and “Generate Token” actions to get the token and then provide it in integration configuration to finish the process. Microsoft 365 and Office 365 deliver the power of cloud productivity to businesses of all sizes, helping save time, money, and free up valued resources. The Microsoft 365 and Office 365 plans combine the familiar Microsoft Office desktop suite with cloud-based versions of Microsoft's next-generation communications and collaboration services (including Office for the web, Microsoft Exchange Online, Microsoft Teams, and Microsoft SharePoint Online) to help users be productive from virtually anywhere through the Internet. This integration uses Microsoft Graph Mail API to communicate with Microsoft 365 and Office 365 services.|
|Microsoft Teams|Microsoft Teams is a platform that combines workplace chat, meetings, notes, and attachmentsQuick Guide: you must first register your app at Microsoft App Registration Portal, Configure Microsoft Teams Integration, Run the action 'Get Authorization', Run the action 'Generate Token'.|
|Netskope|The Netskope Security Cloud helps the world’s largest organizations take full advantage of the cloud and web without sacrificing security.|
|Parsing Form Requests||
|SCC Enterprise|SCC Enterprise integration to set up the SCC Enterprise env|
|ServiceNow|An incident ticketing integration exchanges ticket data between your ServiceNow instance and Google SecOps system.|
|Slack|Slack is where work flows. It's where the people you need, the information you share, and the tools you use come together to get things done.|
|Sophos|Secure cloud workloads, data, apps, and access from the latest advanced threats and vulnerabilities.|
|Tools|A set of utility actions for data manipulation and common platform tasks to power up playbook capabilities.|
|VirusTotalV3|VirusTotal was founded in 2004 as a free service that analyzes files and URLs for viruses, worms, trojans and other kinds of malicious content. Our goal is to make the internet a safer place through collaboration between members of the antivirus industry, researchers and end users of all kinds. Fortune 500 companies, governments and leading security companies are all part of the VirusTotal community, which has grown to over 500,000 registered users.This integration was created using the 3rd iteration of VT API.|


## Playbooks
|Name|Description|
|----|-----------|
|New Block|An embedded workflow that can receive inputs and return an output.|
|New Block 2|An embedded workflow that can receive inputs and return an output.|
|Playbook Action 2||
|Playbook_Action_Block_1||


## Jobs
|Name|Description|
|----|-----------|
|Pull Content GitSyncBeta|Installs content from the repo.|
|Push Content GitSyncBeta|Push all content of this platform to git|
|Push Content GitSyncBeta1|Push all content of this platform to git|
|Sync SCC-Jira Tickets|This job will synchronize tickets in the Jira and Chronicle SOAR case. As a part of synchronization the job will work with comments and status of Chronicle SOAR cases.|

