
# GitSyncBeta

Sync Google SecOps integrations, playbooks, and settings with a GitHub, BitBucket or GitLab instance

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Branch|Target branch|True|String||
|Git Password/Token/SSH Key|Git Password/Token/SSH Key (Base64). RSA and Ed25519 are supported.|True|Password|None|
|Git Username|Git Username|False|String||
|Commit Author|Commit Author. Must be in the following format: 'James Bond <james.bond@gmail.com>'|False|String||
|Siemplify Verify SSL|Siemplify Verify SSL|False|Boolean|true|
|Git Verify SSL|Git Verify SSL|False|Boolean|true|
|Repo URL|Repository URL. The URL must start with 'https' for HTTPS+Token or 'git@' for SSH+Cert.|True|String||


#### Dependencies
| |
|-|
|requests-2.32.3-py3-none-any.whl|
|certifi-2024.12.14-py3-none-any.whl|
|jinja2-3.1.5-py3-none-any.whl|
|cryptography-44.0.0-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|MarkupSafe-3.0.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|dulwich-0.22.7-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|cffi-1.17.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|pycparser-2.22-py3-none-any.whl|
|packaging-24.2-py3-none-any.whl|
|PyNaCl-1.5.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.manylinux_2_24_x86_64.whl|
|paramiko-3.5.0-py3-none-any.whl|
|bcrypt-4.2.1-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|urllib3-2.3.0-py3-none-any.whl|
|idna-3.10-py3-none-any.whl|
|charset_normalizer-3.4.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|


## Actions
#### Ping
Test connectivity to GitSync
Timeout - 600 Seconds



##### JSON Results
```json
None
```






## Jobs

#### Pull Content GitSyncBeta
Installs content from the repo.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Repo URL|False|String||
|Branch|False|String|None|
|Integrations|False|Boolean|true|
|Playbooks|False|Boolean|true|
|Jobs|False|Boolean|true|
|Connectors|False|Boolean|true|
|Integration Instances|False|Boolean|true|
|Visual Families|False|Boolean|true|
|Mappings|False|Boolean|true|
|Environments|False|Boolean|true|
|Dynamic Parameters|False|Boolean|true|
|Logo|False|Boolean|true|
|Case Tags|False|Boolean|true|
|Case Stages|False|Boolean|true|
|Case Title Settings|False|Boolean|true|
|Case Close Reasons|False|Boolean|true|
|Networks|False|Boolean|true|
|Domains|False|Boolean|true|
|Custom Lists|False|Boolean|true|
|Email Templates|False|Boolean|true|
|Blacklists|False|Boolean|true|
|SLA Records|False|Boolean|true|
|Simulated Cases|False|Boolean|true|

#### Pull Mappings GitSyncBeta
Imports mappings from the repo.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Repo URL|False|String|None|
|Branch|False|String|None|
|Source|True|String||

#### Pull Simulated Cases GitSyncBeta
Imports simulated cases from the repo.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Simulated Cases|True|String||
|Repo URL|False|String|None|
|Branch|False|String|None|

#### Push Content GitSyncBeta
Push all content of this platform to git

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Commit|True|String||
|Repo URL|False|String|None|
|Branch|False|String|None|
|Commit Author|False|String||
|Commit Passwords|False|Boolean|false|
|Integrations|False|Boolean|true|
|Playbooks|False|Boolean|true|
|Jobs|False|Boolean|true|
|Connectors|False|Boolean|true|
|Integration Instances|False|Boolean|true|
|Visual Families|False|Boolean|true|
|Mappings|False|Boolean|true|
|Environments|False|Boolean|true|
|Dynamic Parameters|False|Boolean|true|
|Logo|False|Boolean|true|
|Case Tags|False|Boolean|true|
|Case Stages|False|Boolean|true|
|Case Title Settings|False|Boolean|true|
|Case Close Reasons|False|Boolean|true|
|Networks|False|Boolean|true|
|Domains|False|Boolean|true|
|Custom Lists|False|Boolean|true|
|Email Templates|False|Boolean|true|
|Blacklists|False|Boolean|true|
|SLA Records|False|Boolean|true|
|Simulated Cases|False|Boolean|true|

#### Push Simulated Cases GitSyncBeta
Export simulate cases to the repo

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Commit|True|String||
|Repo URL|False|String|None|
|Branch|False|String|None|
|Commit Author|False|String||
|Simulated Cases|True|String||

#### Pull Integration GitSyncBeta
Install an integration or update an installed one.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Install Whitelist|True|String||
|Repo URL|False|String|None|
|Branch|False|String|None|

#### Pull Jobs GitSyncBeta
Imports a job from the repo.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Job Whitelist|True|String||
|Repo URL|False|String|None|
|Branch|False|String|None|

#### Push Integration GitSyncBeta
Push an integration to repo. This action will overwrite the entire folder.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Commit|True|String||
|Push Whitelist|True|String||
|Repo URL|False|String|None|
|Branch|False|String|None|
|Commit Author|False|String||
|Readme Addon|False|String||

#### Push Job GitSyncBeta
Export a job to the repo

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Commit|True|String||
|Repo URL|False|String|None|
|Branch|False|String|None|
|Commit Author|False|String||
|Job Whitelist|True|String||
|Readme Addon|False|String||

#### Pull Connector GitSyncBeta
Imports a connector from the repo.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Repo URL|False|String|None|
|Branch|False|String|None|
|Connector Name|True|String||
|Include Visual Families|False|Boolean|false|
|Include Mappings|False|Boolean|false|

#### Push Mappings GitSyncBeta
Exports mappings  to the repo.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Commit|True|String||
|Repo URL|False|String|None|
|Branch|False|String|None|
|Commit Author|False|String||
|Source|True|String||
|Readme Addon|False|String||

#### Push Playbook GitSyncBeta
Exports playbooks or blocks to the repo

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Branch|False|String|None|
|Commit|True|String||
|Repo URL|False|String|None|
|Commit Author|False|String||
|Folders Whitelist|False|String||
|Playbook Whitelist|False|String||
|Readme Addon|False|String||
|Include Playbook Blocks|False|Boolean|true|

#### Push Connectors GitSyncBeta
Exports a connector to the repo.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Connectors|True|String||
|Branch|False|String||
|Repo URL|False|String||
|Commit Author|False|String||
|Include Visual Families|False|Boolean|false|
|Include Mappings|False|Boolean|false|
|Readme Addon|False|String||
|Commit|True|String||

#### Pull Custom Family GitSyncBeta
Imports a custom family from the repo.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Repo URL|False|String|None|
|Branch|False|String|None|
|Family Name|True|String||

#### Pull Playbook GitSyncBeta
Pulls and Installs a playbook or block from the repo. NOTE: Please verify you're not overwriting existing playbooks

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Repo URL|False|String|None|
|Branch|False|String|None|
|Playbook Whitelist|True|String||
|Include Playbook Blocks|False|Boolean|true|

#### Push Custom Family GitSyncBeta
Exports a custom family to the repo.

|Name|IsMandatory|Type|DefaultValue|
|----|-----------|----|------------|
|Commit|True|String||
|Repo URL|False|String|None|
|Branch|False|String|None|
|Commit Author|False|String||
|Family Name|True|String||
|Readme Addon|False|String||



