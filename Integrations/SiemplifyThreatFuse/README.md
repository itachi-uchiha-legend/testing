
# SiemplifyThreatFuse

ThreatFuse combines best-in-class security orchestration, automation and response (SOAR) with a market-leading Threat Intelligence Platform (TIP) powered by Anomali, to make intelligence-driven security operations simple and accessible for organizations of all sizes.With robust integration out of the box, ThreatFuse ingrains threat-intelligence across the entire detection and response lifecycle. From enrichment with real-time threat indicators, through threat-hunting and intelligence sharing, security analysts can validate, investigate and respond to threats with unprecedented speed and precision.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Web Root|None|True|String|https://siemplify.threatstream.com|
|API Root|None|True|String|https://api.threatstream.com|
|Email Address|None|True|String||
|API Key|None|True|Password|None|
|Verify SSL|None|False|Boolean||


#### Dependencies
| |
|-|
|requests-2.32.3-py3-none-any.whl|
|certifi-2024.8.30-py3-none-any.whl|
|python_dateutil-2.9.0.post0-py2.py3-none-any.whl|
|pandas-2.2.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|TIPCommon-1.0.10-py3-none-any.whl|
|pytz-2024.1-py2.py3-none-any.whl|
|charset_normalizer-3.3.2-py3-none-any.whl|
|idna-3.8-py3-none-any.whl|
|numpy-2.1.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|EnvironmentCommon-1.0.0-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|chardet-5.2.0-py3-none-any.whl|
|tzdata-2024.1-py2.py3-none-any.whl|
|six-1.16.0-py2.py3-none-any.whl|


## Actions
#### Enrich Entities
Retrieve information about IPs, URLs, hashes or User entities with Email regexes from Siemplify ThreatFuse. If multiple records are found for the same entity, action will enrich using the latest record.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Severity Threshold|Specify what should be the severity threshold for the entity, in order to mark it as suspicious. If multiple records are found for the same entity, action will take the highest severity out of all available records.|True|List|Low|
|Confidence Threshold|Specify what should be the confidence threshold for the entity, in order to mark it as suspicious. Note: Maximum is 100. If multiple records are found for the entity, action will take the average. Active records have priority.|True|String||
|Ignore False Positive Status|If enabled, action will ignore the false positive status and mark the entity as suspicious based on the "Severity Threshold" and "Confidence Threshold". If disabled, action will never label false positive entities as suspicious, regardless, if they pass the "Severity Threshold" and "Confidence Threshold" conditions or not.|False|Boolean|false|
|Add Threat Type To Case|If enabled, action will add threat types of the entity from all records as tags to the case. Example: apt|False|Boolean|false|
|Create Insight|If enabled, action will add an insight per processed entity.|False|Boolean|false|
|Only Suspicious Entity Insight|If enabled, action will create insight only for entities that exceeded the "Severity Threshold" and "Confidence Threshold".|False|Boolean|false|



##### JSON Results
```json
{"results": [{"Entity": "49.234.23.243", "EntityResult": [{"source_created": null, "status": "active", "itype": "bot_ip", "expiration_ts": "2021-02-08T10:23:40.950Z", "ip": "49.234.23.243", "is_editable": false, "feed_id": 17, "update_id": 9074259384, "value": "49.234.23.243", "is_public": true, "threat_type": "bot", "workgroups": [], "rdns": null, "confidence": 100, "uuid": "d3c13526-3af4-4045-a242-f7e5720a13d8", "retina_confidence": 100, "trusted_circle_ids": null, "id": 56278363173, "source": "Emerging Threats - Compromised", "owner_organization_id": 2, "import_session_id": null, "source_modified": null, "type": "ip", "sort": [1605003831850, "56278363173"], "description": null, "threatscore": 25, "latitude": 34.7725, "modified_ts": "2020-11-10T10:23:51.850Z", "org": "Tencent cloud computing", "asn": "", "created_ts": "2020-11-10T10:23:51.850Z", "tlp": null, "is_anonymous": false, "country": "CN", "source_reported_confidence": 75, "can_add_public_tags": false, "longitude": 113.7266, "subtype": null, "meta": {"detail2": "imported by user 668", "severity": "low"}, "resource_uri": "/api/v2/intelligence/56278363173/", "report_link": "https://siemplify.threatstream.com/detail/ip/49.234.23.243"}]}], "is_risky": true}
```



#### Get Related Associations
Retrieve entity related associations from Siemplify ThreatFuse. Configure the parameters below: choose the association types to return, specify Max Associations To Return. You can also choose to add retrieved associations as entities to the case.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Return Campaigns|If enabled, action will fetch related campaigns and details about them.|False|Boolean|True|
|Return Threat Bulletins|If enabled, action will fetch related threat bulletins and details about them.|False|Boolean|False|
|Return Actors|If enabled, action will fetch related actors and details about them.|False|Boolean|False|
|Return Attack Patterns|If enabled, action will fetch related attack patterns and details about them.|False|Boolean|False|
|Return Courses Of Action|If enabled, action will fetch related courses of action and details about them.|False|Boolean|False|
|Return Identities|If enabled, action will fetch related identities and details about them.|False|Boolean|False|
|Return Incidents|If enabled, action will fetch related incidents and details about them.|False|Boolean|False|
|Return Infrastructure|If enabled, action will fetch related infrastructure and details about them.|False|Boolean|False|
|Return Intrusion Sets|If enabled, action will fetch related intrusion sets and details about them.|False|Boolean|False|
|Return Malware|If enabled, action will fetch related malware and details about them.|False|Boolean|False|
|Return Signatures|If enabled, action will fetch related signatures and details about them.|False|Boolean|False|
|Return Tools|If enabled, action will fetch related tools and details about them.|False|Boolean|False|
|Return TTPs|If enabled, action will fetch related TTPs and details about them.|False|Boolean|False|
|Return Vulnerabilities|If enabled, action will fetch related vulnerabilities and details about them.|False|Boolean|True|
|Create Campaign Entity|If enabled, action will create an entity out of available “Campaign” associations.|False|Boolean|False|
|Create Actors Entity|If enabled, action will create an entity out of available “Actor” associations.|False|Boolean|False|
|Create Signature Entity|If enabled, action will create an entity out of available “Signature” associations.|False|Boolean|False|
|Create Vulnerability Entity|If enabled, action will create an entity out of available “Vulnerability” associations.|False|Boolean|False|
|Create Case Tag|If enabled, action will create case tags based on the results.|False|Boolean|True|
|Create Insight|If enabled, action will create an insight base on the results.|False|Boolean|True|
|Max Associations To Return|Specify how many associations to return per type. Default: 5|False|String|5|
|Max Statistics To Return|Specify how many top statistics results regarding IOCs to return. Note: action will at max process 1000 IOCs related to the association. If you provide "0", action will not try to fetch statistics information.|False|String|3|



##### JSON Results
```json
[{ "tipreport": [{ "all_circles_visible": true, "assignee_org": null, "assignee_org_id": null, "assignee_org_name": null, "assignee_user": null, "assignee_user_id": null, "assignee_user_name": null, "attachments": [], "body": "###EmailBody\n<div><p>https://un...", "body_content_type": "markdown", "campaign": null, "can_add_public_tags": true, "circles": [], "created_ts": "2019-04-30T13:22:03.392703", "embedded_content_type": null, "embedded_content_url": null, "feed_id": 0, "id": "XXXXXX", "is_anonymous": false, "is_cloneable": "yes", "is_editable": true, "is_email": true, "is_public": true, "logo_s3_url": "https://ts-optic.s3.amazon", "modified_ts": "2019-05-01T12:29:34.310333", "name": "BehindtheScen", "original_source": null, "original_source_id": null, "owner_org": { "id": "XXXX", "name": "Fi34234dsy", "resource_uri": "/api/v1/userorganization/XXXX/" }, "owner_org_id": "XXXX", "owner_org_name": "FirstEnergy", "owner_user": { "avatar_s3_url": null, "can_share_intelligence": true, "email": "jccollins@firstenergycorp.com", "id": "XXXXX", "is_active": true, "is_readonly": false, "must_change_password": false, "name": "ChrisCollins", "nickname": "Nickname_unavailable", "organization": { "id": "XXXX", "name": "FirstEnergy", "resource_uri": "/api/v1/userorganization/XXXX/" }, "resource_uri": "/api/v1/user/XXXXX/" }, "owner_user_id": "XXXXX", "owner_user_name": "ChrisCollins", "parent": null, "private_status_id": null, "published_ts": "2019-04-30T13:27:31.699863", "resource_uri": "/api/v1/tipreport/305150/", "source": "https://XXXXXX/", "source_created": null, "source_modified": null, "starred_by_me": false, "starred_total_count": 0, "statistics": { "total": 306, "top_countries": [{ "name": "US", "count": 53 }, { "name": "HK", "count": 31 }, { "name": "JP", "count": 8 }], "top_types": [{ "name": "email", "count": 126 }, { "name": "domain", "count": 95 }, { "name": "ip", "count": 55 }], "top_sources": [{ "name": "Analyst", "count": 306 }], "top_severities": [{ "name": "low", "count": 211 }, { "name": "very-high", "count": 95 }], "top_threat_types": [{ "name": "malware", "count": 172 }, { "name": "adware", "count": 85 }, { "name": "apt", "count": 48 }], "top_orgs": [{ "name": "N/A", "count": 197 }, { "name": "Choopa, XXY", "count": 22 }, { "name": "ABC", "count": 20 }], "top_status": [{ "name": "inactive", "count": 258 }, { "name": "active", "count": 48 }] }, "status": "published", "tags": ["Delivery", "Weaponization", "Reconnaissance", "XXXXXXX", "e_test_tag"], "tags_v2": [{ "id": "XXX", "name": "e_test_tag" }], "threat_actor": null, "tlp": "green", "ttp": null, "uuid": null, "votes": { "me": null, "total": 0 }, "watched_by_me": false, "watched_total_count": 0, "workgroups": [], "description": "..." }], "campaign": [{ "activity_dates": [], "aliases": [{ "id": "XXX", "name": "XXXX", "resource_uri": "/api/v1/campaignalias/XXX/" }], "body_content_type": "richtext", "can_add_public_tags": true, "circles": [], "created_ts": "2019-11-18T14:52:48.148640", "description": "XXXXXX", "embedded_content_type": null, "embedded_content_url": null, "end_date": "2018-02-01T14:53:00.381000", "external_references": [], "feed_id": 0, "id": "XXXXXX", "intended_effects": [], "is_anonymous": true, "is_cloneable": "yes", "is_public": true, "modified_ts": "2020-04-13T15:48:06.XXXXXX", "name": "ThreeDollarsMalwareToDeliverNewOopsIETrojan", "objective": null, "organization": { "id": 0, "name": "Analyst", "title": "Analyst" }, "parent": null, "publication_status": "published", "published_ts": "2019-11-19T16:58:46.732375", "resource_uri": "/api/v1/campaign/XXXXX/", "source_created": null, "source_modified": null, "starred_by_me": false, "starred_total_count": 2, "start_date": "2018-01-08T14:53:00.608000", "statistics": { "total": 306, "top_countries": [{ "name": "US", "count": 53 }, { "name": "HK", "count": 31 }, { "name": "JP", "count": 8 }], "top_types": [{ "name": "email", "count": 126 }, { "name": "domain", "count": 95 }, { "name": "ip", "count": 55 }], "top_sources": [{ "name": "Analyst", "count": 306 }], "top_severities": [{ "name": "low", "count": 211 }, { "name": "very-high", "count": 95 }], "top_threat_types": [{ "name": "malware", "count": 172 }, { "name": "adware", "count": 85 }, { "name": "apt", "count": 48 }], "top_orgs": [{ "name": "N/A", "count": 197 }, { "name": "Choopa, XXY", "count": 22 }, { "name": "ABC", "count": 20 }], "top_status": [{ "name": "inactive", "count": 258 }, { "name": "active", "count": 48 }] }, "status": { "display_name": "Historic", "id": "X", "resource_uri": "/api/v1/XXXXXXX/X/" }, "status_desc": null, "tags": ["XXXXXXXXX", "XXXXX-Execution", "XXXXXXXXX"], "tags_v2": [{ "id": "gci", "name": "XXXXX-LateralMovement" }], "tlp": "XXXXX", "uuid": "XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXX", "victims": [{ "id": "X", "name": "FinancialServices", "resource_uri": "/api/v1/victimtype/X/", "value": "X" }, { "id": "XX", "name": "Insurance", "resource_uri": "/api/v1/victimtype/XX/", "value": "XX" }], "votes": { "me": null, "total": "X" }, "watched_by_me": false, "watched_total_count": "X", "workgroups": [], "body": "" }], "attackpattern": [{ "name": "Pattern1", "id": 1, "statistics": { "total": 306, "top_countries": [{ "name": "US", "count": 53 }, { "name": "HK", "count": 31 }, { "name": "JP", "count": 8 }], "top_types": [{ "name": "email", "count": 126 }, { "name": "domain", "count": 95 }, { "name": "ip", "count": 55 }], "top_sources": [{ "name": "Analyst", "count": 306 }], "top_severities": [{ "name": "low", "count": 211 }, { "name": "very-high", "count": 95 }], "top_threat_types": [{ "name": "malware", "count": 172 }, { "name": "adware", "count": 85 }, { "name": "apt", "count": 48 }], "top_orgs": [{ "name": "N/A", "count": 197 }, { "name": "Choopa, XXY", "count": 22 }, { "name": "ABC", "count": 20 }], "top_status": [{ "name": "inactive", "count": 258 }, { "name": "active", "count": 48 }] } }, { "name": "Pattern2", "id": 2, "statistics": { "total": 306, "top_countries": [{ "name": "US", "count": 53 }, { "name": "HK", "count": 31 }, { "name": "JP", "count": 8 }], "top_types": [{ "name": "email", "count": 126 }, { "name": "domain", "count": 95 }, { "name": "ip", "count": 55 }], "top_sources": [{ "name": "Analyst", "count": 306 }], "top_severities": [{ "name": "low", "count": 211 }, { "name": "very-high", "count": 95 }], "top_threat_types": [{ "name": "malware", "count": 172 }, { "name": "adware", "count": 85 }, { "name": "apt", "count": 48 }], "top_orgs": [{ "name": "N/A", "count": 197 }, { "name": "Choopa, XXY", "count": 22 }, { "name": "ABC", "count": 20 }], "top_status": [{ "name": "inactive", "count": 258 }, { "name": "active", "count": 48 }] } }], "courseofaction": [{ "name": "CourseofAction1", "id": 1, "statistics": { "total": 306, "top_countries": [{ "name": "US", "count": 53 }, { "name": "HK", "count": 31 }, { "name": "JP", "count": 8 }], "top_types": [{ "name": "email", "count": 126 }, { "name": "domain", "count": 95 }, { "name": "ip", "count": 55 }], "top_sources": [{ "name": "Analyst", "count": 306 }], "top_severities": [{ "name": "low", "count": 211 }, { "name": "very-high", "count": 95 }], "top_threat_types": [{ "name": "malware", "count": 172 }, { "name": "adware", "count": 85 }, { "name": "apt", "count": 48 }], "top_orgs": [{ "name": "N/A", "count": 197 }, { "name": "Choopa, XXY", "count": 22 }, { "name": "ABC", "count": 20 }], "top_status": [{ "name": "inactive", "count": 258 }, { "name": "active", "count": 48 }] } }, { "name": "CourseOfAction2", "id": 2, "statistics": { "total": 306, "top_countries": [{ "name": "US", "count": 53 }, { "name": "HK", "count": 31 }, { "name": "JP", "count": 8 }], "top_types": [{ "name": "email", "count": 126 }, { "name": "domain", "count": 95 }, { "name": "ip", "count": 55 }], "top_sources": [{ "name": "Analyst", "count": 306 }], "top_severities": [{ "name": "low", "count": 211 }, { "name": "very-high", "count": 95 }], "top_threat_types": [{ "name": "malware", "count": 172 }, { "name": "adware", "count": 85 }, { "name": "apt", "count": 48 }], "top_orgs": [{ "name": "N/A", "count": 197 }, { "name": "Choopa, XXY", "count": 22 }, { "name": "ABC", "count": 20 }], "top_status": [{ "name": "inactive", "count": 258 }, { "name": "active", "count": 48 }] } }], "identity": [{ "name": "Identity1", "id": 1, "statistics": { "total": 306, "top_countries": [{ "name": "US", "count": 53 }, { "name": "HK", "count": 31 }, { "name": "JP", "count": 8 }], "top_types": [{ "name": "email", "count": 126 }, { "name": "domain", "count": 95 }, { "name": "ip", "count": 55 }], "top_sources": [{ "name": "Analyst", "count": 306 }], "top_severities": [{ "name": "low", "count": 211 }, { "name": "very-high", "count": 95 }], "top_threat_types": [{ "name": "malware", "count": 172 }, { "name": "adware", "count": 85 }, { "name": "apt", "count": 48 }], "top_orgs": [{ "name": "N/A", "count": 197 }, { "name": "Choopa, XXY", "count": 22 }, { "name": "ABC", "count": 20 }], "top_status": [{ "name": "inactive", "count": 258 }, { "name": "active", "count": 48 }] } }, { "name": "Identity2", "id": 2, "statistics": { "total": 306, "top_countries": [{ "name": "US", "count": 53 }, { "name": "HK", "count": 31 }, { "name": "JP", "count": 8 }], "top_types": [{ "name": "email", "count": 126 }, { "name": "domain", "count": 95 }, { "name": "ip", "count": 55 }], "top_sources": [{ "name": "Analyst", "count": 306 }], "top_severities": [{ "name": "low", "count": 211 }, { "name": "very-high", "count": 95 }], "top_threat_types": [{ "name": "malware", "count": 172 }, { "name": "adware", "count": 85 }, { "name": "apt", "count": 48 }], "top_orgs": [{ "name": "N/A", "count": 197 }, { "name": "Choopa, XXY", "count": 22 }, { "name": "ABC", "count": 20 }], "top_status": [{ "name": "inactive", "count": 258 }, { "name": "active", "count": 48 }] } }], "infrastructure": [{ "name": "Infrustructure1", "id": 1, "statistics": { "total": 306, "top_countries": [{ "name": "US", "count": 53 }, { "name": "HK", "count": 31 }, { "name": "JP", "count": 8 }], "top_types": [{ "name": "email", "count": 126 }, { "name": "domain", "count": 95 }, { "name": "ip", "count": 55 }], "top_sources": [{ "name": "Analyst", "count": 306 }], "top_severities": [{ "name": "low", "count": 211 }, { "name": "very-high", "count": 95 }], "top_threat_types": [{ "name": "malware", "count": 172 }, { "name": "adware", "count": 85 }, { "name": "apt", "count": 48 }], "top_orgs": [{ "name": "N/A", "count": 197 }, { "name": "Choopa, XXY", "count": 22 }, { "name": "ABC", "count": 20 }], "top_status": [{ "name": "inactive", "count": 258 }, { "name": "active", "count": 48 }] } }, { "name": "Infrustructure2", "id": 2, "statistics": { "total": 306, "top_countries": [{ "name": "US", "count": 53 }, { "name": "HK", "count": 31 }, { "name": "JP", "count": 8 }], "top_types": [{ "name": "email", "count": 126 }, { "name": "domain", "count": 95 }, { "name": "ip", "count": 55 }], "top_sources": [{ "name": "Analyst", "count": 306 }], "top_severities": [{ "name": "low", "count": 211 }, { "name": "very-high", "count": 95 }], "top_threat_types": [{ "name": "malware", "count": 172 }, { "name": "adware", "count": 85 }, { "name": "apt", "count": 48 }], "top_orgs": [{ "name": "N/A", "count": 197 }, { "name": "Choopa, XXY", "count": 22 }, { "name": "ABC", "count": 20 }], "top_status": [{ "name": "inactive", "count": 258 }, { "name": "active", "count": 48 }] } }], "signature": [{ "assignee_user": null, "body_content_type": null, "can_add_public_tags": true, "circles": [], "created_ts": "2020-08-02T12:31:43.676937", "description": null, "embedded_content_type": null, "embedded_content_url": null, "feed_id": "XXXX", "id": "XXXXX", "is_anonymous": false, "is_cloneable": "yes", "is_public": true, "logo_s3_url": null, "modified_ts": "2020-08-02T12:32:25.129859", "name": "XXXXX", "organization": { "id": "XXXX", "name": "XXXXXXX", "resource_uri": "/api/v1/userorganization/XXXX/" }, "organization_id": "XXXX", "owner_user": { "email": "devops+q6cyber@threatstream.com", "id": "XXXXX", "name": "", "resource_uri": "/api/v1/user/XXXXX/" }, "owner_user_id": "XXXXX", "parent": null, "publication_status": "published", "published_ts": "2020-08-02T12:31:XXXXX", "resource_uri": "/api/v1/signature/XXXXX/", "s_type": { "display_name": "CarbonBlackQuery", "id": "XXXXX", "resource_uri": "/api/v1/signature_type/XXXXX/", "value": "XXXXX" }, "source_created": null, "source_modified": null, "starred_by_me": false, "starred_total_count": 0, "statistics": { "total": 306, "top_countries": [{ "name": "US", "count": 53 }, { "name": "HK", "count": 31 }, { "name": "JP", "count": 8 }], "top_types": [{ "name": "email", "count": 126 }, { "name": "domain", "count": 95 }, { "name": "ip", "count": 55 }], "top_sources": [{ "name": "Analyst", "count": 306 }], "top_severities": [{ "name": "low", "count": 211 }, { "name": "very-high", "count": 95 }], "top_threat_types": [{ "name": "malware", "count": 172 }, { "name": "adware", "count": 85 }, { "name": "apt", "count": 48 }], "top_orgs": [{ "name": "N/A", "count": 197 }, { "name": "Choopa, XXY", "count": 22 }, { "name": "ABC", "count": 20 }], "top_status": [{ "name": "inactive", "count": 258 }, { "name": "active", "count": 48 }] }, "tags": ["XXXXX", "XXXXX"], "tags_v2": [{ "id": "XXXXX", "name": "XXXXX" }, { "id": "XXXXX", "name": "XXXXX" }], "tlp": "white", "uuid": "XXXXX-XXXXX-XXXXX-XXXXX-XXXXX", "votes": { "me": null, "total": 0 }, "watched_by_me": false, "watched_total_count": 0, "workgroups": [] }], "actor": [{ "aliases": [{ "id": "XXXXXXX", "name": "XXXXXXXXXXXXXX(XXXXXXX)", "resource_uri": "/api/v1/XXXXXXX/XXXXXXX/" }], "assignee_user": null, "avatar_s3_url": null, "body_content_type": "XXXXXXX", "can_add_public_tags": "XXXXXXX", "circles": [], "created_ts": "2020-02-27T05:24:17.691123", "description": "XXXXXXX", "embedded_content_type": null, "embedded_content_url": null, "external_references": [], "feed_id": "XXXXXXX", "goals": null, "id": "XXXXXXX", "is_anonymous": false, "is_cloneable": "yes", "is_public": true, "is_team": false, "logo_s3_url": "https://ts-optic.s3.aXXXXXXX", "modified_ts": "2020-11-28T01:12:XXXXXXX", "motivations": [], "name": "XXXXXXX", "organization": { "id": "XXXXXXX", "name": "ThreatStream", "resource_uri": "/api/v1/userorganization/XXXXXXX/" }, "organization_id": "XXXXXXX", "owner_user": { "email": "devops+threatstream@threatstream.com", "id": "XXXXXXX", "name": "", "resource_uri": "/api/v1/user/XXXXXXX/" }, "owner_user_id": "XXXXXXX", "parent": null, "personal_motivations": null, "primary_motivation": null, "publication_status": "published", "published_ts": "2020-11-28T01:11:XX.XXXXXXX", "resource_level": null, "resource_uri": "/api/v1/actor/XXXXXXX/", "roles": null, "secondary_motivations": null, "soph_desc": null, "soph_type": null, "source_created": "2019-07-XXXXXXX:47:20", "source_modified": "2020-11-XXXXXXX:28:47", "starred_by_me": false, "starred_total_count": "XXXXXXX", "start_date": null, "statistics": { "total": 306, "top_countries": [{ "name": "US", "count": 53 }, { "name": "HK", "count": 31 }, { "name": "JP", "count": 8 }], "top_types": [{ "name": "email", "count": 126 }, { "name": "domain", "count": 95 }, { "name": "ip", "count": 55 }], "top_sources": [{ "name": "Analyst", "count": 306 }], "top_severities": [{ "name": "low", "count": 211 }, { "name": "very-high", "count": 95 }], "top_threat_types": [{ "name": "malware", "count": 172 }, { "name": "adware", "count": 85 }, { "name": "apt", "count": 48 }], "top_orgs": [{ "name": "N/A", "count": 197 }, { "name": "Choopa, XXY", "count": 22 }, { "name": "ABC", "count": 20 }], "top_status": [{ "name": "inactive", "count": 258 }, { "name": "active", "count": 48 }] }, "tags": ["CVE-XXXXXXX-XXXXXXX"], "tags_v2": [{ "id": "XXX", "name": "CVE-XXXX-XXXX" }], "threat_actor_types": null, "tlp": "red", "trackings": [], "types": [], "uuid": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXX", "victims": [], "votes": { "me": null, "total": "X" }, "watched_by_me": false, "watched_total_count": "X", "workgroups": [] }], "identity": [{ "name": "Identity1", "id": 1 }], "malware": [{ "aliases": [], "body_content_type": "richtext", "c2_port": [], "c2_protocol": [], "can_add_public_tags": true, "capabilities": [], "circles": [], "created_ts": "2020-11-27T08:18:XX.XXXXXX", "description": "XXXXX", "embedded_content_type": null, "embedded_content_url": null, "execution_platforms": ["windows"], "external_references": [], "feed_id": 0, "first_seen": "2020-04-XXXXX:17:00", "id": "XXXXXX", "implementation_languages": [], "is_anonymous": true, "is_cloneable": "yes", "is_family": true, "is_public": true, "kill_chain_phases": {}, "killchainstages": [], "last_seen": null, "malware_types": ["XXXXX-XXXX-XXX"], "modified_ts": "XXXXX-11-30T09:37:56.786908", "name": "XXXXXXXXX", "organization": { "id": "X", "name": "Analyst", "title": "Analyst" }, "parent": null, "publication_status": "published", "published_ts": "2020-11-27T08:19:XX.XXXXXX", "resource_uri": "/api/v1/malware/XXXXXXX/", "source_created": null, "source_modified": null, "starred_by_me": false, "starred_total_count": 0, "statistics": { "total": 306, "top_countries": [{ "name": "US", "count": 53 }, { "name": "HK", "count": 31 }, { "name": "JP", "count": 8 }], "top_types": [{ "name": "email", "count": 126 }, { "name": "domain", "count": 95 }, { "name": "ip", "count": 55 }], "top_sources": [{ "name": "Analyst", "count": 306 }], "top_severities": [{ "name": "low", "count": 211 }, { "name": "very-high", "count": 95 }], "top_threat_types": [{ "name": "malware", "count": 172 }, { "name": "adware", "count": 85 }, { "name": "apt", "count": 48 }], "top_orgs": [{ "name": "N/A", "count": 197 }, { "name": "Choopa, XXY", "count": 22 }, { "name": "ABC", "count": 20 }], "top_status": [{ "name": "inactive", "count": 258 }, { "name": "active", "count": 48 }] }, "tags": ["Rat", "CarbonSpider", "Kodiak", "Malware"], "tags_v2": [{ "id": "XXX", "name": "XXXXXXXXXXXX" }], "tlp": "amber", "uuid": "XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXX", "votes": { "me": "XXX", "total": "X" }, "watched_by_me": false, "watched_total_count": 0, "workgroups": [] }], "vulnerability": [{ "aliases": [], "assignee_user": null, "body_content_type": "richtext", "can_add_public_tags": true, "circles": [], "created_ts": "XXXX-05-21T10:16:XX.XXXXXX", "cvss2_score": 0.0, "cvss3_score": null, "description": "XXXXXXX", "embedded_content_type": null, "embedded_content_url": null, "external_references": [], "feed_id": "X", "id": "XXXXXX", "is_anonymous": false, "is_cloneable": "yes", "is_public": true, "is_system": false, "logo_s3_url": null, "modified_ts": "2020-10-28T10:57:14.XXXXXX", "name": "CVE-XXXX-XXXX", "organization": { "id": "XXXX", "name": "VerizonBusiness", "resource_uri": "/api/v1/userorganization/XXXX/" }, "organization_id": "XXXX", "owner_user": { "email": "durga.ramjali@intl.verizon.com", "id": "XXXX", "name": "DRamjali", "resource_uri": "/api/v1/user/XXXX/" }, "owner_user_id": "XXXX", "parent": null, "publication_status": "published", "published_ts": "2019-05-21T10:19:XXXXXXX", "resource_uri": "/api/v1/vulnerability/XXXXXX/", "source": "Custom", "source_created": null, "source_modified": null, "starred_by_me": false, "starred_total_count": 0, "statistics": { "total": 306, "top_countries": [{ "name": "US", "count": 53 }, { "name": "HK", "count": 31 }, { "name": "JP", "count": 8 }], "top_types": [{ "name": "email", "count": 126 }, { "name": "domain", "count": 95 }, { "name": "ip", "count": 55 }], "top_sources": [{ "name": "Analyst", "count": 306 }], "top_severities": [{ "name": "low", "count": 211 }, { "name": "very-high", "count": 95 }], "top_threat_types": [{ "name": "malware", "count": 172 }, { "name": "adware", "count": 85 }, { "name": "apt", "count": 48 }], "top_orgs": [{ "name": "N/A", "count": 197 }, { "name": "Choopa, XXY", "count": 22 }, { "name": "ABC", "count": 20 }], "top_status": [{ "name": "inactive", "count": 258 }, { "name": "active", "count": 48 }] }, "tags": ["TI(INV)"], "tags_v2": [{ "id": "XXX", "name": "TI(XXX)" }], "tlp": "white", "update_id": "XXXXXXXX", "uuid": null, "vendors": [], "votes": { "me": null, "total": 0 }, "watched_by_me": false, "watched_total_count": 0, "workgroups": [] }], "tipreport": [{ "all_circles_visible": true, "attachments": [], "body": "XXXXXX", "body_content_type": "richtext", "campaign": null, "can_add_public_tags": true, "circles": [], "created_ts": "2020-11-27T08:22:00.XXXXXX", "embedded_content_type": null, "embedded_content_url": null, "feed_id": 0, "id": "XXXXXX", "is_anonymous": true, "is_cloneable": "yes", "is_editable": true, "is_email": false, "is_public": true, "modified_ts": "XXXX-11-30T09:37:XX.XXXX", "name": "XXXXXXXXXX", "original_source": null, "original_source_id": null, "owner_org": { "id": 0, "name": "Analyst", "title": "Analyst" }, "parent": null, "private_status_id": null, "published_ts": "2020-11-27T08:23:XX.XXXXXX", "resource_uri": "/api/v1/tipreport/XXXXXXX/", "source_created": null, "source_modified": null, "starred_by_me": false, "starred_total_count": 0, "status": "published", "statistics": { "total": 306, "top_countries": [{ "name": "US", "count": 53 }, { "name": "HK", "count": 31 }, { "name": "JP", "count": 8 }], "top_types": [{ "name": "email", "count": 126 }, { "name": "domain", "count": 95 }, { "name": "ip", "count": 55 }], "top_sources": [{ "name": "Analyst", "count": 306 }], "top_severities": [{ "name": "low", "count": 211 }, { "name": "very-high", "count": 95 }], "top_threat_types": [{ "name": "malware", "count": 172 }, { "name": "adware", "count": 85 }, { "name": "apt", "count": 48 }], "top_orgs": [{ "name": "N/A", "count": 197 }, { "name": "Choopa, XXY", "count": 22 }, { "name": "ABC", "count": 20 }], "top_status": [{ "name": "inactive", "count": 258 }, { "name": "active", "count": 48 }] }, "tags": ["Malware"], "tags_v2": [{ "id": "XXX", "name": "XXXXXX" }], "threat_actor": null, "tlp": "amber", "ttp": null, "uuid": "XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXX", "votes": { "me": null, "total": 0 }, "watched_by_me": false, "watched_total_count": 0, "workgroups": [] }], "tool": [{ "aliases": [], "assignee_user": null, "body_content_type": "richtext", "can_add_public_tags": true, "circles": [], "created_ts": "XXXX-06-12T02:34:XX.XXXXXX", "description": "<spa", "embedded_content_type": null, "embedded_content_url": null, "external_references": [], "feed_id": "X", "id": "XX", "is_anonymous": false, "is_cloneable": "yes", "is_public": true, "kill_chain_phases": { "lockheed-martin": ["actions-on-objectives"] }, "killchainstages": ["actions-on-objectives"], "logo_s3_url": "https:", "modified_ts": "2020-06-19T05:08:XX.XXXXXX", "name": "Bloodhound", "organization": { "id": "3676", "name": "NationalAustraliaBank", "resource_uri": "/api/v1/userorganization/XXXX/" }, "organization_id": "XXXX", "owner_user": { "email": "jorell.magtibay@nab.com.au", "id": "XXXXX", "name": "JorellMagitbay", "resource_uri": "/api/v1/user/XXXXX/" }, "owner_user_id": "XXXXX", "parent": null, "publication_status": "published", "published_ts": "2020-06-12T04:25:XX.XXXXXX", "resource_uri": "/api/v1/tool/XX/", "source_created": null, "source_modified": null, "starred_by_me": false, "starred_total_count": 1, "statistics": { "total": 306, "top_countries": [{ "name": "US", "count": 53 }, { "name": "HK", "count": 31 }, { "name": "JP", "count": 8 }], "top_types": [{ "name": "email", "count": 126 }, { "name": "domain", "count": 95 }, { "name": "ip", "count": 55 }], "top_sources": [{ "name": "Analyst", "count": 306 }], "top_severities": [{ "name": "low", "count": 211 }, { "name": "very-high", "count": 95 }], "top_threat_types": [{ "name": "malware", "count": 172 }, { "name": "adware", "count": 85 }, { "name": "apt", "count": 48 }], "top_orgs": [{ "name": "N/A", "count": 197 }, { "name": "Choopa, XXY", "count": 22 }, { "name": "ABC", "count": 20 }], "top_status": [{ "name": "inactive", "count": 258 }, { "name": "active", "count": 48 }] }, "tags": [], "tags_v2": [], "tlp": "white", "tool_types": ["information-gathering"], "tool_version": null, "uuid": "XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXX", "votes": { "me": null, "total": "X" }, "watched_by_me": false, "watched_total_count": "X", "workgroups": [] }], "ttp": [{ "aliases": [], "assignee_user": null, "behavior_attackpatterns": [], "behavior_exploits": [], "behavior_malware": [], "body_content_type": "XXXXX", "can_add_public_tags": true, "children": [], "circles": [], "created_ts": "XXXX-09-04T01:59:48.XXXXX", "description": "<heade", "embedded_content_type": null, "embedded_content_url": null, "feed_id": 0, "id": "XXXXXXX", "is_anonymous": false, "is_category": false, "is_cloneable": "yes", "is_mitre": false, "is_public": true, "killchain_stages": [], "logo_s3_url": "XXXX", "modified_ts": "XXXX-09-04T02:30:23.XXXXXX", "name": "XXXXXX", "organization": { "id": "XXXX", "name": "XXXXXXXXXXXXXXXXXXX", "resource_uri": "/api/v1/userorganization/XXXX/" }, "organization_id": "XXX", "owner_user": { "email": "XXXXX.XXXX@XXX.XXX.XX", "id": "XXXXX", "name": "JorellMagitbay", "resource_uri": "/api/v1/user/18139/" }, "owner_user_id": "XXXXX", "parent": null, "publication_status": "published", "published_ts": "2019-09-04T02:30:23.173875", "resource_uri": "/api/v1/ttp/XXXXXXX/", "source_created": null, "source_modified": null, "starred_by_me": false, "starred_total_count": 0, "statistics": { "total": 306, "top_countries": [{ "name": "US", "count": 53 }, { "name": "HK", "count": 31 }, { "name": "JP", "count": 8 }], "top_types": [{ "name": "email", "count": 126 }, { "name": "domain", "count": 95 }, { "name": "ip", "count": 55 }], "top_sources": [{ "name": "Analyst", "count": 306 }], "top_severities": [{ "name": "low", "count": 211 }, { "name": "very-high", "count": 95 }], "top_threat_types": [{ "name": "malware", "count": 172 }, { "name": "adware", "count": 85 }, { "name": "apt", "count": 48 }], "top_orgs": [{ "name": "N/A", "count": 197 }, { "name": "Choopa, XXY", "count": 22 }, { "name": "ABC", "count": 20 }], "top_status": [{ "name": "inactive", "count": 258 }, { "name": "active", "count": 48 }] }, "tags": [], "tags_v2": [], "tlp": null, "uuid": null, "votes": { "me": null, "total": 0 }, "watched_by_me": false, "watched_total_count": 0, "workgroups": [] }] }]
```



#### Get Related Domains
Retrieve entity related domains based on the associations in Siemplify ThreatFuse. Supported entities: Hash, URL, IP Address, Email Address (user entity that matches email regex), Threat Actor, CVE.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Confidence Threshold|Specify what should be the confidence threshold. Note: Maximum is 100.|True|String||
|Search Threat Bulletins|If enabled, action will search among threat bulletins.|False|Boolean|True|
|Search Actors|If enabled, action will search among actors.|False|Boolean|True|
|Search Attack Patterns|If enabled, action will search among attack patterns.|False|Boolean|True|
|Search Campaigns|If enabled, action will search among campaigns.|False|Boolean|True|
|Search Courses Of Action|If enabled, action will search among courses of action.|False|Boolean|True|
|Search Identities|If enabled, action will search among identities.|False|Boolean|True|
|Search Incidents|If enabled, action will search among incidents.|False|Boolean|True|
|Search Infrastructures|If enabled, action will search among infrastructures.|False|Boolean|True|
|Search Intrusion Sets|If enabled, action will search among intrusion sets.|False|Boolean|True|
|Search Malware|If enabled, action will search among malware.|False|Boolean|True|
|Search Signatures|If enabled, action will search among signatures.|False|Boolean|True|
|Search Tools|If enabled, action will search among tools.|False|Boolean|True|
|Search TTPs|If enabled, action will search among TTPs.|False|Boolean|True|
|Search Vulnerabilities|If enabled, action will search among vulnerabilities.|False|Boolean|True|
|Max Domains To Return|Specify how many domains to return. Default: 50.|False|String|50|



##### JSON Results
```json
[{"domains":["www.google.com"]}]
```



#### Get Related Email Addresses
Retrieve entity related email addresses based on the associations in Siemplify ThreatFuse. Supported entities: Hash, URL, IP Address, Email Address (user entity that matches email regex), Threat Actor, CVE.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Confidence Threshold|Specify what should be the confidence threshold. Note: Maximum is 100.|True|String||
|Search Observables|If enabled, action will search among observables.|False|Boolean|True|
|Search Threat Bulletins|If enabled, action will search among threat bulletins.|False|Boolean|True|
|Search Actors|If enabled, action will search among actors.|False|Boolean|True|
|Search Attack Patterns|If enabled, action will search among attack patterns.|False|Boolean|True|
|Search Campaigns|If enabled, action will search among campaigns.|False|Boolean|True|
|Search Courses Of Action|If enabled, action will search among courses of action.|False|Boolean|True|
|Search Identities|If enabled, action will search among identities.|False|Boolean|True|
|Search Incidents|If enabled, action will search among incidents.|False|Boolean|True|
|Search Infrastructures|If enabled, action will search among infrastructures.|False|Boolean|True|
|Search Intrusion Sets|If enabled, action will search among intrusion sets.|False|Boolean|True|
|Search Malware|If enabled, action will search among malware.|False|Boolean|True|
|Search Signatures|If enabled, action will search among signatures.|False|Boolean|True|
|Search Tools|If enabled, action will search among tools.|False|Boolean|True|
|Search TTPs|If enabled, action will search among TTPs.|False|Boolean|True|
|Search Vulnerabilities|If enabled, action will search among vulnerabilities.|False|Boolean|True|
|Max Email Addresses To Return|Specify how many email addresses to return. Default: 50.|False|String|50|



##### JSON Results
```json
[{"emails":["XWZNR1L@gmail.com"]}]
```



#### Get Related Hashes
Retrieve entity related hashes based on the associations in Siemplify ThreatFuse. Supported entities: Hash, URL, IP Address, Email Address (user entity that matches email regex), Threat Actor, CVE.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Confidence Threshold|Specify what should be the confidence threshold. Note: Maximum is 100.|True|String||
|Search Threat Bulletins|If enabled, action will search among threat bulletins.|False|Boolean|True|
|Search Actors|If enabled, action will search among actors.|False|Boolean|True|
|Search Attack Patterns|If enabled, action will search among attack patterns.|False|Boolean|True|
|Search Campaigns|If enabled, action will search among campaigns.|False|Boolean|True|
|Search Courses Of Action|If enabled, action will search among courses of action.|False|Boolean|True|
|Search Identities|If enabled, action will search among identities.|False|Boolean|True|
|Search Incidents|If enabled, action will search among incidents.|False|Boolean|True|
|Search Infrastructures|If enabled, action will search among infrastructures.|False|Boolean|True|
|Search Intrusion Sets|If enabled, action will search among intrusion sets.|False|Boolean|True|
|Search Malware|If enabled, action will search among malware.|False|Boolean|True|
|Search Signatures|If enabled, action will search among signatures.|False|Boolean|True|
|Search Tools|If enabled, action will search among tools.|False|Boolean|True|
|Search TTPs|If enabled, action will search among TTPs.|False|Boolean|True|
|Search Vulnerabilities|If enabled, action will search among vulnerabilities.|False|Boolean|True|
|Max Hashes To Return|Specify how many hashes to return. Default: 50.|False|String|50|



##### JSON Results
```json
[{"SHA1_hashes":["e7700ed03ee64a634527be5944d5e063fd9f1734","10bc38d0a421011a56875db8636e34748a2107f1"],"all_hashes":["ak285ed63a42f22dae616a341ef61dab66b6b65217df02k491966c778be5f138","1ff4c79bffeaa6fc865ad3d8de1b7aac2939862b246cae0a93cf5937d827f5be","e7700ed03ee64a634527be5944d5e063fd9f1734","10bc38d0a421011a56875db8636e34748a2107f1","4781c65762016dbb1e624418e6asw21b","1ababw3014df8594a61e0645422db960"],"MD5_hashes":["4781c65762016dbb1e624418e6asw21b","1ababw3014df8594a61e0645422db960"],"SHA256_hashes":["ak285ed63a42f22dae616a341ef61dab66b6b65217df02k491966c778be5f138","1ff4c79bffeaa6fc865ad3d8de1b7aac2939862b246cae0a93cf5937d827f5be"]}]
```



#### Get Related IPs
Retrieve entity related IP addresses based on the associations in Siemplify ThreatFuse. Supported entities: Hash, URL, IP Address, Email Address (user entity that matches email regex), Threat Actor, CVE.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Confidence Threshold|Specify what should be the confidence threshold. Note: Maximum is 100.|True|String||
|Search Observables|If enabled, action will search among observables.|False|Boolean|True|
|Search Threat Bulletins|If enabled, action will search among threat bulletins.|False|Boolean|True|
|Search Actors|If enabled, action will search among actors.|False|Boolean|True|
|Search Attack Patterns|If enabled, action will search among attack patterns.|False|Boolean|True|
|Search Campaigns|If enabled, action will search among campaigns.|False|Boolean|True|
|Search Courses Of Action|If enabled, action will search among courses of action.|False|Boolean|True|
|Search Identities|If enabled, action will search among identities.|False|Boolean|True|
|Search Incidents|If enabled, action will search among incidents.|False|Boolean|True|
|Search Infrastructures|If enabled, action will search among infrastructures.|False|Boolean|True|
|Search Intrusion Sets|If enabled, action will search among intrusion sets.|False|Boolean|True|
|Search Malware|If enabled, action will search among malware.|False|Boolean|True|
|Search Signatures|If enabled, action will search among signatures.|False|Boolean|True|
|Search Tools|If enabled, action will search among tools.|False|Boolean|True|
|Search TTPs|If enabled, action will search among TTPs.|False|Boolean|True|
|Search Vulnerabilities|If enabled, action will search among vulnerabilities.|False|Boolean|True|
|Max IPs To Return|Specify how many IPs to return. Default: 50.|False|String|50|



##### JSON Results
```json
[{"ips":["100.0.0.1"]}]
```



#### Get Related URLs
Retrieve entity related urls based on the associations in Siemplify ThreatFuse. Supported entities: Hash, URL, IP Address, Email Address (user entity that matches email regex), Threat Actor, CVE.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Confidence Threshold|Specify what should be the confidence threshold. Note: Maximum is 100.|True|String||
|Search Threat Bulletins|If enabled, action will search among threat bulletins.|False|Boolean|True|
|Search Actors|If enabled, action will search among actors.|False|Boolean|True|
|Search Attack Patterns|If enabled, action will search among attack patterns.|False|Boolean|True|
|Search Campaigns|If enabled, action will search among campaigns.|False|Boolean|True|
|Search Courses Of Action|If enabled, action will search among courses of action.|False|Boolean|True|
|Search Identities|If enabled, action will search among identities.|False|Boolean|True|
|Search Incidents|If enabled, action will search among incidents.|False|Boolean|True|
|Search Infrastructures|If enabled, action will search among infrastructures.|False|Boolean|True|
|Search Intrusion Sets|If enabled, action will search among intrusion sets.|False|Boolean|True|
|Search Malware|If enabled, action will search among malware.|False|Boolean|True|
|Search Signatures|If enabled, action will search among signatures.|False|Boolean|True|
|Search Tools|If enabled, action will search among tools.|False|Boolean|True|
|Search TTPs|If enabled, action will search among TTPs.|False|Boolean|True|
|Search Vulnerabilities|If enabled, action will search among vulnerabilities.|False|Boolean|True|
|Max URLs To Return|Specify how many hashes to return. Default: 50.|False|String|50|



##### JSON Results
```json
[{"urls":["https://www.google.com/url?q=http:/wzFgw"]}]
```



#### Ping
Test connectivity to the Siemplify ThreatFuse with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### Submit Observables
Submit an observable to Siemplify ThreatFuse based on IP, URL, Hash or User entities with Email regexes from Siemplify ThreatFuse. Note: requires 'Org admin', 'Create Anomali Community Intel' and 'Approve Intel' permissions.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Classification|Specify the classification of the observable.|True|List|Private|
|Threat Type|Specify the threat type of the observables.|True|List|APT|
|Source|Specify the intelligence source for the observable.|False|String|Siemplify|
|Expiration Date|Specify the expiration date in days for the observable. If nothing is specified here, action will create an observable that will never expire.|False|String||
|Trusted Circle IDs|Specify the comma-separated list of trusted circle ids. Observables will be shared with those trusted circles.|False|String||
|TLP|Specify the TLP for your observables.|False|List|Select One|
|Confidence|Specify what should be the confidence for the observable. Note: this parameter will only work, if you create observables in your organization and requires 'Override System Confidence' to be enabled.|False|String||
|Override System Confidence|If enabled, created observables will have the confidence specified in the 'Confidence' parameter. Note: you can't share observables in trusted circles and publicly, when this parameter is enabled.|False|Boolean|False|
|Anonymous Submission|If enabled, action will make an anonymous submission.|False|Boolean|False|
|Tags|Specify a comma-separated list of tags that you want to add to observable.|False|String||



##### JSON Results
```json
[{"approved_jobs":[{"id":"XXXXXXX","entity":"104.10.182.103"}],"jobs_with_excluded_entities":[{"id":"XXXXXXX","entity":"10.0.0.28"},{"id":"XXXXXXX","entity":"HTTP://MARKOSSOLOMON.COM/F1Q7QX.PHP"},{"id":"XXXXXXX","entity":"100.0.0.10"}]}]
```









## Connectors
#### Siemplify ThreatFuse - Observables Connector
Pull observables from Siemplify ThreatFuse. Note: Source names are used in the whitelist.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password||
|DeviceProductField|Enter the source field name in order to retrieve the Product Field name.|True|String|Product Name|
|EventClassId|Enter the source field name in order to retrieve the Event Field name.|True|String|type|
|Script Timeout (Seconds)|Timeout limit for the python process running the current script.|True|Integer|300|
|API Root|API root of the Siemplify ThreatFuse instance.|True|String|https://api.threatstream.com|
|Email Address|Email address of the Siemplify ThreatFuse account.|True|String||
|API Key|API Key of the Siemplify ThreatFuse account.|True|Password||
|Lowest Severity To Fetch|Lowest severity that will be used to fetch observables. Possible values: Low, Medium, High, Very-High|True|String|High|
|Lowest Confidence To Fetch|Lowest confidence that will be used to fetch observables. Maximum is 100.|True|Integer|50|
|Source Feed Filter|Comma-separated list of feed ids that should be used to ingest observables. Example: 515,4129|False|String||
|Observable Type Filter|Comma-separated list of observable types that should be  ingested. Example: url, domain. Possible values: url, domain, email, hash, ip, ipv6|False|String|url, domain, email, hash, ip, ipv6|
|Observable Status Filter|Comma-separated list of observable status that should be used to ingest new data. Example: active, inactive. Possible values: active, inactive, falsepos|False|String|active|
|Threat Type Filter|Comma-separated list of threat types that should be used to ingest observables. Example: аdware, anomalous, anonymization, apt. Possible values: аdware, anomalous, anonymization, apt,bot,brute, c2,compromised, crypto,data_leakage, ddos, dyn_dns, exfil, exploit, fraud, hack_tool, i2p, informational, malware, p2p, parked, phish, scan, sinkhole, spam, suppress, suspicious, tor, vps|False|String||
|Trusted Circle Filter|Comma-separated list of trusted circle ids that should be used to ingest observables. Example: 146,147|False|String||
|Tag Name Filter|Comma-separated list of tag names associated with observables that should be used with ingestion. Example: Microsoft Credentials, Phishing|False|String||
|Source Feed Grouping|If enabled, the connector will group observables from the same source under the same Siemplify Alert.|False|Boolean|false|
|Fetch Max Days Backwards|Number of days before the first connector iteration to retrieve findings from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|Integer|1|
|Max Observables Per Alert|How many observables should be a part of one Siemplify Alert. Maximum is 200.|False|Integer|100|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|Boolean|false|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Siemplify ThreatFuse server is valid.|False|Boolean|false|
|Proxy Server Address|The address of the proxy server to use.|False|String||




