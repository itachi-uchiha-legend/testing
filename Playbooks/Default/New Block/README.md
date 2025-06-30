# New Block
An embedded workflow that can receive inputs and return an output.



**Enabled:** True

**Version:** 1

**Type:** Block

**Priority:** 2

**Playbook Simulator:** False


##### Input Parameters
|Name|Default Value|
|----|-------------|


### Involved Steps (Unordered)
|Step Name|Description|Integration|Original Action|
|---------|-----------|-----------|---------------|
|VirusTotalV3_Add Comment To Entity_1|Add a comment to entities in VirusTotal. Supported entities: File Hash, URL, Hostname, Domain, IP Address. Note: only MD5, SHA-1 and SHA-256 Hash types are supported|VirusTotalV3|Add Comment To Entity|
|VirusTotalV3_Enrich Hash_1|Enrich Hash using information from VirusTotal. Supported entities: Filehash. Note: only MD5, SHA-1 and SHA-256 are supported.|VirusTotalV3|Enrich Hash|
|VirusTotalV3_Download File_1|Download file from VirusTotal. Supported entities: Filehash. Note: this action requires a VT Enterprise token. Only MD5, SHA-1, SHA-256 hashes are supported.|VirusTotalV3|Download File|
|VirusTotalV3_Add Vote To Entity_1|Add a vote to entities in VirusTotal. Supported entities: File Hash, URL, Hostname, Domain, IP Address. Note: only MD5, SHA-1 and SHA-256 Hash types are supported|VirusTotalV3|Add Vote To Entity|

