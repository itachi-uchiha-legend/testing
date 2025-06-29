# Playbook_Action_Block_3




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
|VirusTotalV3_Get Related Domains_1|Get related domains to the provided entities from VirusTotal. Note: this action requires a VT Enterprise token. Supported entities: IP, URL, Filehash, Hostname, Domain. Note: only MD5, SHA-1 and SHA-256 are supported.|VirusTotalV3|Get Related Domains|
|VirusTotalV3_Get Related URLs_1|Get related urls to the provided entities from VirusTotal. Note: this action requires a VT Enterprise token. Supported entities: IP, URL, Filehash, Hostname, Domain. Note: only MD5, SHA-1 and SHA-256 are supported.|VirusTotalV3|Get Related URLs|

### Involved Blocks
|Name|Description|
|----|-----------|
|Block 3|An embedded workflow that can receive inputs and return an output.|
