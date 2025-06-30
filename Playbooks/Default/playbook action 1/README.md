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
|VirusTotalV3_Get Graph Details_1|Get detailed information about graphs in VirusTotal.|VirusTotalV3|Get Graph Details|
|VirusTotalV3_Add Vote To Entity_1|Add a vote to entities in VirusTotal. Supported entities: File Hash, URL, Hostname, Domain, IP Address. Note: only MD5, SHA-1 and SHA-256 Hash types are supported|VirusTotalV3|Add Vote To Entity|
|VirusTotalV3_Enrich URL_1|Enrich URL using information from VirusTotal. Supported entities: URL.|VirusTotalV3|Enrich URL|

### Involved Blocks
|Name|Description|
|----|-----------|
|New Block 2|An embedded workflow that can receive inputs and return an output.|
|New Block 1|An embedded workflow that can receive inputs and return an output.|
