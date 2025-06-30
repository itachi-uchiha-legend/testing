# playbook action 1




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
|VirusTotalV3_Enrich Hash_1|Enrich Hash using information from VirusTotal. Supported entities: Filehash. Note: only MD5, SHA-1 and SHA-256 are supported.|VirusTotalV3|Enrich Hash|
|VirusTotalV3_Ping_1|Test connectivity to the VirusTotal with parameters provided at the integration configuration page on the Marketplace tab.|VirusTotalV3|Ping|
|VirusTotalV3_Get Graph Details_1|Get detailed information about graphs in VirusTotal.|VirusTotalV3|Get Graph Details|
|VirusTotalV3_Add Vote To Entity_1|Add a vote to entities in VirusTotal. Supported entities: File Hash, URL, Hostname, Domain, IP Address. Note: only MD5, SHA-1 and SHA-256 Hash types are supported|VirusTotalV3|Add Vote To Entity|
|VirusTotalV3_Get Related URLs_1|Get related urls to the provided entities from VirusTotal. Note: this action requires a VT Enterprise token. Supported entities: IP, URL, Filehash, Hostname, Domain. Note: only MD5, SHA-1 and SHA-256 are supported.|VirusTotalV3|Get Related URLs|
|VirusTotalV3_Enrich URL_1|Enrich URL using information from VirusTotal. Supported entities: URL.|VirusTotalV3|Enrich URL|

### Involved Blocks
|Name|Description|
|----|-----------|
|New Block 2|An embedded workflow that can receive inputs and return an output.|
|New Block 1|An embedded workflow that can receive inputs and return an output.|
