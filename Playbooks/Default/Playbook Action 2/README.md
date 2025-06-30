# Playbook Action 2




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
|VirusTotalV3_Enrich IOC_1|Enrich IOCs using information from VirusTotal.|VirusTotalV3|Enrich IOC|
|VirusTotalV3_Download File_1|Download file from VirusTotal. Supported entities: Filehash. Note: this action requires a VT Enterprise token. Only MD5, SHA-1, SHA-256 hashes are supported.|VirusTotalV3|Download File|
|VirusTotalV3_Add Vote To Entity_1|Add a vote to entities in VirusTotal. Supported entities: File Hash, URL, Hostname, Domain, IP Address. Note: only MD5, SHA-1 and SHA-256 Hash types are supported|VirusTotalV3|Add Vote To Entity|

### Involved Blocks
|Name|Description|
|----|-----------|
|New Block 2|An embedded workflow that can receive inputs and return an output.|
