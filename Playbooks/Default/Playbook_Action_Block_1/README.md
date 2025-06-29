# Playbook_Action_Block_1




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
|VirusTotalV3_Add Vote To Entity_1|Add a vote to entities in VirusTotal. Supported entities: File Hash, URL, Hostname, Domain, IP Address. Note: only MD5, SHA-1 and SHA-256 Hash types are supported|VirusTotalV3|Add Vote To Entity|
|VirusTotalV3_Get Related Domains_1|Get related domains to the provided entities from VirusTotal. Note: this action requires a VT Enterprise token. Supported entities: IP, URL, Filehash, Hostname, Domain. Note: only MD5, SHA-1 and SHA-256 are supported.|VirusTotalV3|Get Related Domains|
|VirusTotalV3_Enrich IP_1|Enrich IP using information from VirusTotal. Supported entities: IP address.|VirusTotalV3|Enrich IP|
|VirusTotalV3_Get Related Hashes_1|Get related hashes to the provided entities from VirusTotal. Note: this action requires a VT Enterprise token. Supported entities: IP, URL, Filehash, Hostname, Domain. Note: only MD5, SHA-1 and SHA-256 are supported.|VirusTotalV3|Get Related Hashes|

### Involved Blocks
|Name|Description|
|----|-----------|
|New Block|An embedded workflow that can receive inputs and return an output.|
