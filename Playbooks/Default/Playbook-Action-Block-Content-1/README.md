# Playbook-Action-Block-Content-1




**Enabled:** True

**Version:** 1

**Type:** Playbook

**Priority:** 2

**Playbook Simulator:** False


### Playbook Trigger
**Trigger Type:** All

**Conditions Operator:** And

##### Conditions
|Key|Operator|Value|
|---|--------|-----|
||Equals||


### Involved Steps (Unordered)
|Step Name|Description|Integration|Original Action|
|---------|-----------|-----------|---------------|
|VirusTotalV3_Ping_1|Test connectivity to the VirusTotal with parameters provided at the integration configuration page on the Marketplace tab.|VirusTotalV3|Ping|
|VirusTotalV3_Get Related URLs_1|Get related urls to the provided entities from VirusTotal. Note: this action requires a VT Enterprise token. Supported entities: IP, URL, Filehash, Hostname, Domain. Note: only MD5, SHA-1 and SHA-256 are supported.|VirusTotalV3|Get Related URLs|
|VirusTotalV3_Submit File_1|Submit a file and return results from VirusTotal.|VirusTotalV3|Submit File|
|VirusTotalV3_Get Domain Details_1|Get detailed information about the domain using information from VirusTotal. Supported entities: URL (entity extracts domain part), Hostname, Domain.|VirusTotalV3|Get Domain Details|
|VirusTotalV3_Search Graphs_1|Search graphs based on custom filters in VirusTotal.|VirusTotalV3|Search Graphs|

### Involved Blocks
|Name|Description|
|----|-----------|
|Block 4|An embedded workflow that can receive inputs and return an output.|
