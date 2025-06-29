# Playbook_Block




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
|VirusTotalV3_Get Related IPs_1|Get related IPs to the provided entities from VirusTotal. Note: this action requires a VT Enterprise token. Supported entities: URL, Filehash, Hostname, Domain. Note: only MD5, SHA-1 and SHA-256 are supported.|VirusTotalV3|Get Related IPs|

### Involved Blocks
|Name|Description|
|----|-----------|
|Block 1|An embedded workflow that can receive inputs and return an output.|
|Block 2|An embedded workflow that can receive inputs and return an output.|
