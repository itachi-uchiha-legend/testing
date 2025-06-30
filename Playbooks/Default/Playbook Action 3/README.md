# Playbook Action 3




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
|VirusTotalV3_Download File_1|Download file from VirusTotal. Supported entities: Filehash. Note: this action requires a VT Enterprise token. Only MD5, SHA-1, SHA-256 hashes are supported.|VirusTotalV3|Download File|

### Involved Blocks
|Name|Description|
|----|-----------|
|New Block 3|An embedded workflow that can receive inputs and return an output.|
