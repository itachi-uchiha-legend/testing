
# CofenseTriage

With Cofense Triage, prioritize and remediate phishing threats faster. A culture of user-reporting is key to stopping phishing attacks, but your overburdened SOC team needs to prioritize what’s reported. Instead of slowing their efforts with time consuming manual processes—the numerous steps required to find and understand real indicators of threats—automate analysis with Cofense Triage and focus on making decisions to speed remediation.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|None|True|String|https://tap.phishmecloud.com|
|Client ID|None|True|String||
|Client Secret|None|True|Password|None|
|Verify SSL|None|False|Boolean|false|


#### Dependencies
| |
|-|
|requests-2.32.3-py3-none-any.whl|
|filelock-3.15.4-py3-none-any.whl|
|charset_normalizer-3.3.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl|
|chardet-5.2.0-py3-none-any.whl|
|tldextract-5.1.2-py3-none-any.whl|
|urllib3-2.2.2-py3-none-any.whl|
|TIPCommon-1.0.10-py3-none-any.whl|
|requests_file-2.1.0-py2.py3-none-any.whl|
|idna-3.7-py3-none-any.whl|
|certifi-2024.7.4-py3-none-any.whl|
|EnvironmentCommon-1.0.0-py3-none-any.whl|


## Actions
#### Add Tags To Report
Add tags to a report in Cofense Triage.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Report ID|Specify the id of the report to which you want to add tags.|True|String||
|Tags|Specify a comma-separated list of tags that need to be applied to the report.|True|String||



##### JSON Results
```json
{"data": {"id": "13xxx", "type": "reports", "links": {"self": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx"}, "attributes": {"location": "Processed", "risk_score": 96, "from_address": null, "subject": "Test Phishing domain", "received_at": "2020-10-12T21:30:54.000Z", "reported_at": "2020-10-12T21:30:53.000Z", "raw_headers": "X-Triage-Noise-Reduction: state=0\r\nX-Triage-Noise-Reduction: score=79\r\nX-Triage-Noise-Reduction: verdict=clean\r\nDate: Mon, 12 Oct 2020 21:31:36 +0000\r\nMessage-ID: <5f84cb38575a0_2592acb1561f9d0321eb@ip-10-132-10-234.exxx.internal.mail>\r\nSubject: Test Phishing domain\r\nMime-Version: 1.0\r\nContent-Type: multipart/mixed;\r\n boundary=\"--==_mimepart_5f84cb385734c_2592acb1561f9d032089\";\r\n charset=UTF-8\r\nContent-Transfer-Encoding: 7bit", "text_body": "Testing<http://dsrihsddk.net/>\r\n\r\nThis is a poor reputation domain\r\n\r\n", "html_body": "<html xmlns:v=\"urn:schemas-microsoft-com:vml\" xmlns:o=\"urn:schemas-microsoft-com:office:office\" xmlns:w=\"urn:schemas-microsoft-com:office:word\" xmlns:m=\"http://schemas.microsoft.com/office/2004/12/omml\" xmlns=\"http://www.w3.org/TR/REC-html40\">\r\n<head>\r\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\r\n<meta name=\"Generator\" content=\"Microsoft Word 15 (filtered medium)\">\r\n<style><!--\r\n/* Font Definitions */\r\n@font-face\r\n\t{font-family:\"Cambria Math\";\r\n\tpanose-1:2 4 5 3 5 4 6 3 2 4;}\r\n@font-face\r\n\t{font-family:Calibri;\r\n\tpanose-1:2 15 5 2 2 2 4 3 2 4;}\r\n/* Style Definitions */\r\np.MsoNormal, li.MsoNormal, div.MsoNormal\r\n\t{margin:0in;\r\n\tfont-size:12.0pt;\r\n\tfont-family:\"Calibri\",sans-serif;}\r\na:link, span.MsoHyperlink\r\n\t{mso-style-priority:99;\r\n\tcolor:#0563C1;\r\n\ttext-decoration:underline;}\r\nspan.EmailStyle17\r\n\t{mso-style-type:personal-compose;\r\n\tfont-family:\"Calibri\",sans-serif;\r\n\tcolor:windowtext;}\r\n.MsoChpDefault\r\n\t{mso-style-type:export-only;\r\n\tfont-size:12.0pt;\r\n\tfont-family:\"Calibri\",sans-serif;}\r\n@page WordSection1\r\n\t{size:8.5in 11.0in;\r\n\tmargin:1.0in 1.0in 1.0in 1.0in;}\r\ndiv.WordSection1\r\n\t{page:WordSection1;}\r\n--></style>\r\n</head>\r\n<body lang=\"EN-US\" link=\"#0563C1\" vlink=\"#954F72\" style=\"word-wrap:break-word\">\r\n<div class=\"WordSection1\">\r\n<p class=\"MsoNormal\"><span style=\"font-size:11.0pt\"><a href=\"http://dsrihsddk.net/\">Testing</a><o:p></o:p></span></p>\r\n<p class=\"MsoNormal\"><span style=\"font-size:11.0pt\"><o:p>&nbsp;</o:p></span></p>\r\n<p class=\"MsoNormal\"><span style=\"font-size:11.0pt\">This is a poor reputation domain<o:p></o:p></span></p>\r\n<div>\r\n<p class=\"MsoNormal\"><span style=\"font-size:11.0pt\"><o:p>&nbsp;</o:p></span></p>\r\n</div>\r\n</div>\r\n</body>\r\n</html>\r\n", "md5": "81fe86fc9c244be978ab8b8392d3c986", "sha256": "146b857b2a147eeb9091571327452006438294aeb21069e38c6f25a811aa6c03", "match_priority": 1, "tags": ["asd"], "categorization_tags": [], "processed_at": "2020-11-20T14:50:04.237Z", "created_at": "2020-10-12T21:31:36.495Z", "updated_at": "2020-11-23T08:35:15.974Z"}, "relationships": {"assignee": {"links": {"self": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/relationships/assignee", "related": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/assignee"}, "data": null}, "category": {"links": {"self": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/relationships/category", "related": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/category"}, "data": {"type": "categories", "id": "3"}}, "cluster": {"links": {"self": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/relationships/cluster", "related": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/cluster"}, "data": {"type": "clusters", "id": "3915"}}, "reporter": {"links": {"self": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/relationships/reporter", "related": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/reporter"}, "data": {"type": "reporters", "id": "5331"}}, "attachment_payloads": {"links": {"self": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/relationships/attachment_payloads", "related": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/attachment_payloads"}}, "attachments": {"links": {"self": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/relationships/attachments", "related": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/attachments"}}, "headers": {"links": {"self": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/relationships/headers", "related": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/headers"}}, "hostnames": {"links": {"self": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/relationships/hostnames", "related": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/hostnames"}}, "urls": {"links": {"self": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/relationships/urls", "related": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/urls"}}, "rules": {"links": {"self": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/relationships/rules", "related": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/rules"}}, "threat_indicators": {"links": {"self": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/relationships/threat_indicators", "related": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/threat_indicators"}}}, "meta": {"risk_score_summary": {"integrations": 75, "vip": 5, "reporter": 15, "rules": 1}}}}
```



#### Categorize Report
Categorize a report in Cofense Triage.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Report ID|Specify the id of the report to which you want to add tags.|True|String||
|Category Name|Specify the name of the category that should be applied to the report. Available categories can be found in the “List Categories” action.|True|String||



##### JSON Results
```json
{"data": {"id": "13xxx", "type": "reports", "links": {"self": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx"}, "attributes": {"location": "Processed", "risk_score": 96, "from_address": null, "subject": "Test Phishing domain", "received_at": "2020-10-12T21:30:54.000Z", "reported_at": "2020-10-12T21:30:53.000Z", "raw_headers": "X-Triage-Noise-Reduction: state=0\r\nX-Triage-Noise-Reduction: score=79\r\nX-Triage-Noise-Reduction: verdict=clean\r\nDate: Mon, 12 Oct 2020 21:31:36 +0000\r\nMessage-ID: <5f84cb38575a0_2592acb1561f9d0321eb@ip-10-132-10-234.ec2.intexxxxl.mail>\r\nSubject: Test Phishing domain\r\nMime-Version: 1.0\r\nContent-Type: multipart/mixed;\r\n boundary=\"--==_mimepart_5f84cb385734c_2592acb1561f9d032089\";\r\n charset=UTF-8\r\nContent-Transfer-Encoding: 7bit", "text_body": "Testing<http://dsrihsddk.net/>\r\n\r\nThis is a poor reputation domain\r\n\r\n", "html_body": "<html xmlns:v=\"urn:schemas-microsoft-com:vml\" xmlns:o=\"urn:schemas-microsoft-com:office:office\" xmlns:w=\"urn:schemas-microsoft-com:office:word\" xmlns:m=\"http://schemas.microsoft.com/office/2004/12/omml\" xmlns=\"http://www.w3.org/TR/REC-html40\">\r\n<head>\r\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\">\r\n<meta name=\"Generator\" content=\"Microsoft Word 15 (filtered medium)\">\r\n<style><!--\r\n/* Font Definitions */\r\n@font-face\r\n\t{font-family:\"Cambria Math\";\r\n\tpanose-1:2 4 5 3 5 4 6 3 2 4;}\r\n@font-face\r\n\t{font-family:Calibri;\r\n\tpanose-1:2 15 5 2 2 2 4 3 2 4;}\r\n/* Style Definitions */\r\np.MsoNormal, li.MsoNormal, div.MsoNormal\r\n\t{margin:0in;\r\n\tfont-size:12.0pt;\r\n\tfont-family:\"Calibri\",sans-serif;}\r\na:link, span.MsoHyperlink\r\n\t{mso-style-priority:99;\r\n\tcolor:#0563C1;\r\n\ttext-decoration:underline;}\r\nspan.EmailStyle17\r\n\t{mso-style-type:personal-compose;\r\n\tfont-family:\"Calibri\",sans-serif;\r\n\tcolor:windowtext;}\r\n.MsoChpDefault\r\n\t{mso-style-type:export-only;\r\n\tfont-size:12.0pt;\r\n\tfont-family:\"Calibri\",sans-serif;}\r\n@page WordSection1\r\n\t{size:8.5in 11.0in;\r\n\tmargin:1.0in 1.0in 1.0in 1.0in;}\r\ndiv.WordSection1\r\n\t{page:WordSection1;}\r\n--></style>\r\n</head>\r\n<body lang=\"EN-US\" link=\"#0563C1\" vlink=\"#954F72\" style=\"word-wrap:break-word\">\r\n<div class=\"WordSection1\">\r\n<p class=\"MsoNormal\"><span style=\"font-size:11.0pt\"><a href=\"http://dsrihsddk.net/\">Testing</a><o:p></o:p></span></p>\r\n<p class=\"MsoNormal\"><span style=\"font-size:11.0pt\"><o:p>&nbsp;</o:p></span></p>\r\n<p class=\"MsoNormal\"><span style=\"font-size:11.0pt\">This is a poor reputation domain<o:p></o:p></span></p>\r\n<div>\r\n<p class=\"MsoNormal\"><span style=\"font-size:11.0pt\"><o:p>&nbsp;</o:p></span></p>\r\n</div>\r\n</div>\r\n</body>\r\n</html>\r\n", "md5": "81fe86fc9c244be978ab8b8392d3c986", "sha256": "146b857b2a147eeb9091571327452006438294aeb21069e38c6f25a811aa6c03", "match_priority": 1, "tags": [], "categorization_tags": [], "processed_at": "2020-11-23T08:39:53.143Z", "created_at": "2020-10-12T21:31:36.495Z", "updated_at": "2020-11-23T08:39:09.705Z"}, "relationships": {"assignee": {"links": {"self": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/relationships/assignee", "related": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/assignee"}, "data": null}, "category": {"links": {"self": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/relationships/category", "related": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/category"}, "data": {"type": "categories", "id": "1"}}, "cluster": {"links": {"self": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/relationships/cluster", "related": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/cluster"}, "data": {"type": "clusters", "id": "3915"}}, "reporter": {"links": {"self": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/relationships/reporter", "related": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/reporter"}, "data": {"type": "reporters", "id": "5331"}}, "attachment_payloads": {"links": {"self": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/relationships/attachment_payloads", "related": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/attachment_payloads"}}, "attachments": {"links": {"self": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/relationships/attachments", "related": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/attachments"}}, "headers": {"links": {"self": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/relationships/headers", "related": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/headers"}}, "hostnames": {"links": {"self": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/relationships/hostnames", "related": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/hostnames"}}, "urls": {"links": {"self": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/relationships/urls", "related": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/urls"}}, "rules": {"links": {"self": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/relationships/rules", "related": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/rules"}}, "threat_indicators": {"links": {"self": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/relationships/threat_indicators", "related": "https://tap.phishmecloud.com/api/public/v2/reports/13xxx/threat_indicators"}}}, "meta": {"risk_score_summary": {"integrations": 75, "vip": 5, "reporter": 15, "rules": 1}}}}
```



#### EnrichURL
Return information about the URL from Cofense Triage.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Risk Score Threshold|Specify, what should be the risk score threshold for Siemplify to label that URL as suspicious. Maximum is 100.|True|String|50|



##### JSON Results
```json
[{"Entity": "https://www.paypal.com/us", "EntityResult": {"id": "1", "type": "urls", "attributes": {"url": "https://www.paypal.com/us", "risk_score": null, "created_at": "2019-04-12T02:58:20.008Z", "updated_at": "2019-04-12T02:58:20.008Z"}}}]
```



#### Execute Playbook
Initiate a playbook execution in Cofense Triage.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Report ID|Specify the ID of the report on which you want to execute the playbook.|True|String||
|Playbook Name|Specify the name of the playbook that needs to be executed.|True|String||



#### Get Domain Details
Return information about the domain from Cofense Triage.
Timeout - 600 Seconds



##### JSON Results
```json
[{"Entity": "http://cie.org.mx/leather.php", "EntityResult": {"id": "1", "type": "hostnames", "attributes": {"hostname": "cie.org.mx", "risk_score": null, "created_at": "2019-04-12T02:58:19.893Z", "updated_at": "2019-04-12T02:58:19.974Z"}}}]
```



#### Get Report Headers
Return information about the header related to the report from Cofense Triage.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Report ID|Specify the id of the report for which you want to retrieve headers.|True|String||
|Max Headers To Return|Specify how many headers to return.|False|String|50|



##### JSON Results
```json
[{"id": "4", "type": "headers", "attributes": {"key": "Mime-Version", "value": "1.0", "created_at": "2020-11-03T16:43:33.767Z", "updated_at": "2020-11-03T16:43:33.767Z"}}, {"id": "11", "type": "headers", "attributes": {"key": "Content-Transfer-Encoding", "value": "7bit", "created_at": "2020-11-03T16:43:34.212Z", "updated_at": "2020-11-03T16:43:34.212Z"}}, {"id": "3870", "type": "headers", "attributes": {"key": "Date", "value": "Fri, 12 Apr 2019 02:58:17 +0000", "created_at": "2020-11-03T16:44:09.580Z", "updated_at": "2020-11-03T16:44:09.580Z"}}, {"id": "3872", "type": "headers", "attributes": {"key": "Message-ID", "value": "<5caffec95c40b_3aab3fe7ea52f32063487@ip-10-132-9-226.ec2.internal.mail>", "created_at": "2020-11-03T16:44:09.594Z", "updated_at": "2020-11-03T16:44:09.594Z"}}, {"id": "3874", "type": "headers", "attributes": {"key": "Subject", "value": "Your Ha.Oullette@example.com Checking/Savings security need to be updated.", "created_at": "2020-11-03T16:44:09.609Z", "updated_at": "2020-11-03T16:44:09.609Z"}}, {"id": "3876", "type": "headers", "attributes": {"key": "Content-Type", "value": "multipart/mixed; boundary=\"--==_mimepart_5caffec95c0fd_3aab3fe7ea52f320633d2\"; charset=UTF-8", "created_at": "2020-11-03T16:44:09.631Z", "updated_at": "2020-11-03T16:44:09.631Z"}}]
```



#### Get Report Reporters
Return information about the reporter related to the report from Cofense Triage.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Report ID|Specify the id of the report for which you want to retrieve reporters.|True|String||



##### JSON Results
```json
{"id": "1", "type": "reporters", "attributes": {"email": "ha.oullette@example.com", "reports_count": 3, "last_reported_at": "2016-02-18T00:24:45.000Z", "reputation_score": -5, "vip": false, "created_at": "2019-04-12T02:58:17.401Z", "updated_at": "2019-04-12T02:59:22.287Z"}}
```



#### Get Threat Indicator Details
Return information about the entities based on the threat indicator details from Cofense Triage. Note: Only MD5 and SHA256 hashes are supported.
Timeout - 600 Seconds



##### JSON Results
```json
[{"Entity": "f1364ab115332cb44b5d7bb734xxxx", "EntityResult": {"id": "1", "type": "threat_indicators", "attributes": {"threat_level": "Malicious", "threat_type": "MD5", "threat_value": "f1364ab115332cb44b5d7bb734xxxx", "threat_source": "Triage-UI", "created_at": "2019-06-06T18:55:38.107Z", "updated_at": "2020-11-03T16:41:19.972Z"}}}, {"Entity": "Subject:XXX Shipping Document invoice/bill of lading", "EntityResult": {"id": "3", "type": "threat_indicators", "attributes": {"threat_level": "Malicious", "threat_type": "Header", "threat_value": "Subject:DXXX Shipping Document invoice/bill of lading", "threat_source": "Triage-UI", "created_at": "2019-06-06T19:46:17.799Z", "updated_at": "2019-06-06T19:46:17.799Z"}}}]
```



#### List Categories
List available categories in Cofense Triage.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Names|Specify a comma-separated list of category names, This parameter is useful to check, whether a category with the specified name exists.|False|String||
|Lowest Score To Fetch|Specify what should be the lowest accepted score for the category. This parameter can work with negative values.|False|String||
|Only Malicious|If enabled, action will only return malicious categories.|False|Boolean|false|
|Only Archived|If enabled, action will only return archived categories.|False|Boolean|false|
|Only Non Archived|If enabled, action will return only non-archived categories.|False|Boolean|false|
|Only Non Malicious|If enabled, action will return only non-malicious categories.|False|Boolean|false|
|Max Categories To Return|Specify how many categories to return.|False|String||



##### JSON Results
```json
{"data": [{"id": "1", "type": "categories", "links": {"self": "https://tap.phishmecloud.com/api/public/v2/categories/1"}, "attributes": {"name": "Non-Malicious", "score": -5, "malicious": false, "color": "#739d75", "archived": false, "created_at": "2019-04-11T08:24:49.787Z", "updated_at": "2019-11-12T19:15:37.849Z"}}, {"id": "2", "type": "categories", "links": {"self": "https://tap.phishmecloud.com/api/public/v2/categories/2"}, "attributes": {"name": "Spam", "score": 0, "malicious": false, "color": "#58899a", "archived": false, "created_at": "2019-04-11T08:24:49.791Z", "updated_at": "2019-11-12T19:15:37.854Z"}}, {"id": "3", "type": "categories", "links": {"self": "https://tap.phishmecloud.com/api/public/v2/categories/3"}, "attributes": {"name": "Crimeware", "score": 5, "malicious": true, "color": "#c6911f", "archived": false, "created_at": "2019-04-11T08:24:49.794Z", "updated_at": "2019-11-12T19:15:37.859Z"}}, {"id": "4", "type": "categories", "links": {"self": "https://tap.phishmecloud.com/api/public/v2/categories/4"}, "attributes": {"name": "Advanced Threats", "score": 10, "malicious": true, "color": "#a9052a", "archived": false, "created_at": "2019-04-11T08:24:49.797Z", "updated_at": "2019-11-12T19:15:37.864Z"}}, {"id": "5", "type": "categories", "links": {"self": "https://tap.phishmecloud.com/api/public/v2/categories/5"}, "attributes": {"name": "Phishing Simulation", "score": 10, "malicious": false, "color": "#4c024c", "archived": false, "created_at": "2019-04-11T08:24:53.792Z", "updated_at": "2019-11-12T19:15:37.843Z"}}, {"id": "6", "type": "categories", "links": {"self": "https://tap.phishmecloud.com/api/public/v2/categories/6"}, "attributes": {"name": "Test_Cat", "score": 99, "malicious": true, "color": "#db272f", "archived": false, "created_at": "2019-11-18T16:15:20.190Z", "updated_at": "2019-11-18T16:15:20.190Z"}}, {"id": "7", "type": "categories", "links": {"self": "https://tap.phishmecloud.com/api/public/v2/categories/7"}, "attributes": {"name": "Test_Test_Test", "score": 11, "malicious": true, "color": "#dbd336", "archived": false, "created_at": "2020-02-20T22:14:24.678Z", "updated_at": "2020-02-20T22:14:24.678Z"}}], "links": {"first": "https://tap.phishmecloud.com/api/public/v2/categories?fields%5Bcategories%5D=name%2Cscore%2Cmalicious%2Ccolor%2Carchived%2Ccreated_at%2Cupdated_at&page%5Bnumber%5D=1&page%5Bsize%5D=20", "last": "https://tap.phishmecloud.com/api/public/v2/categories?fields%5Bcategories%5D=name%2Cscore%2Cmalicious%2Ccolor%2Carchived%2Ccreated_at%2Cupdated_at&page%5Bnumber%5D=1&page%5Bsize%5D=20"}}
```



#### List Playbooks
List available playbooks in Cofense Triage.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Filter Key|Specify the key that needs to be used to filter playbooks.|False|List|Select One|
|Filter Logic|Specify what filter logic should be applied. Filtering logic is working based on the value provided in the "Filter Key" parameter. Note: "Equals" logic is case sensitive, while "Contains" is case insensitive.|False|List|Not Specified|
|Filter Value|Specify what value should be used in the filter. If "Equal" is selected, action will try to find the exact match among results and if "Contains" is selected, action will try to find results that contain that substring. If nothing is provided in this parameter, the filter will not be applied. Filtering logic is working based on the value provided in the "Filter Key" parameter.|False|String||
|Max Records To Return|Specify how many records to return. If nothing is provided, action will return 50 records. Maximum: 200.|False|String|50|



##### JSON Results
```json
[{"id":"xxx","type":"playbooks","links":{"self":"https://reltest6.phishmecloud.com/api/public/v2/playbooks/xxx"},"attributes":{"name":"SN_Test","description":"","active":true,"button_color":"#204d74","add_rule_tags_to_report_tags":true,"remove_existing_report_tags":false,"remove_existing_cluster_tags":false,"report_tags":["SN_Test"],"cluster_tags":["SN_Cluster_Test","test1"],"delete_report":false,"guid":"b443xxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx","created_at":"2021-05-28T01:29:22.080Z","updated_at":"2022-04-08T06:04:17.016Z"}}]
```



#### Ping
Test connectivity to the Cofense Triage with parameters provided at the integration configuration page on the Marketplace tab.
Timeout - 600 Seconds



#### Download Report Email
Download raw email related to the report from Cofense Triage.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Report ID|Specify the ID of the report, which contains the raw email that needs to be downloaded.|True|String||
|Download Folder|Specify the absolute path to the download folder. Note: Name will be constructed in the following way {report id}.eml.|True|String||
|Overwrite|If enabled, action will overwrite the file with the same name and filepath.|False|Boolean|true|
|Create Insight|If enabled, action will create an insight that contains raw email of the report.|False|Boolean|false|



##### JSON Results
```json
{"absolute_file_path": "/tmp/test/13507.eml"}
```



#### Download Report Preview
Download image preview from the email related to the report from Cofense Triage.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Report ID|Specify the ID of the report, which contains the raw email that needs to be downloaded.|True|String||
|Download Folder|Specify the absolute path to the download folder. Note: Name will be constructed in the following way {report id}.eml.|True|String||
|Overwrite|If enabled, action will overwrite the file with the same name and filepath.|False|Boolean|true|
|Image Format|Specify the format of the image.|True|List|PNG|
|Create Insight|If enabled, action will create an insight that contains raw email of the report.|False|Boolean|false|



##### JSON Results
```json
{"absolute_file_path": "/tmp/test/13507.eml"}
```



#### List Reports Related To Threat Indicators
List reports related to threat indicators in Cofense Triage.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Create Case Wall Table|If enabled, action will create a case wall table with information about reports,|False|Boolean|false|
|Max Reports To Return|Specify how many reports to return.|False|String|100|



##### JSON Results
```json
[{"id": "string", "type": "string", "links": {"self": "string"}, "attributes": {"location": "string", "risk_score": null, "from_address": null, "subject": "string", "received_at": "string", "reported_at": "string", "raw_headers": "string", "md5": "string", "sha256": "string", "match_priority": "string", "tags": [], "categorization_tags": [], "processed_at": null, "created_at": "string", "updated_at": "string"}, "meta": {"risk_score_summary": null}}]
```









## Connectors
#### Cofense Triage - Reports Connector
Pull reports from Cofense Triage.

|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|DeviceProductField|Enter the source field name in order to retrieve the Product Field name.|True|String|Product Name|
|EventClassId|Enter the source field name in order to retrieve the Event Field name.|True|String|attributes_location|
|Environment Field Name|Describes the name of the field where the environment name is stored. If the environment field isn't found, the environment is the default environment.|False|String||
|Environment Regex Pattern|A regex pattern to run on the value found in the "Environment Field Name" field. Default is .* to catch all and return the value unchanged. Used to allow the user to manipulate the environment field via regex logic. If the regex pattern is null or empty, or the environment value is null, the final environment result is the default environment.|False|String|.*|
|PythonProcessTimeout|Timeout limit for the python process running the current script.|True|Integer|180|
|API Root|API Root of the Cofense Triage instance.|True|String|https://tap.phishmecloud.com|
|Client ID|Client ID of the Cofense Triage account.|True|String||
|Client Secret|Client Secret of the Cofense Triage account.|True|Password||
|Lowest Risk Score To Fetch|Lowest risk score that will be used to fetch emails. Maximum is 100.|True|Integer|0|
|Fetch Max Hours Backwards|Number of hours before the first connector iteration to retrieve emails from. This parameter applies to the initial connector iteration after you enable the connector for the first time, or used as a fallback value in cases where connector's last run timestamp expires.|False|Integer|1|
|Padding Time|Padding Period in hours specifies a minimum time interval that will be used by connector to check for unfinished reports.|False|Integer|0|
|Max Reports To Fetch|How many reports to process per one connector iteration.|False|Integer|10|
|Use whitelist as a blacklist|If enabled, whitelist will be used as a blacklist.|False|Boolean|false|
|Verify SSL|If enabled, verify the SSL certificate for the connection to the Cofense Triage server is valid.|False|Boolean|false|
|Report Location|Comma-separated list of locations from where to ingest reports. Only reports from the provided locations will be ingested. If nothing is specified, the connector will ingest reports from all locations. Possible values: Inbox,Reconnaissance,Processed|False|String|Inbox,Reconnaissance|
|Proxy Server Address|The address of the proxy server to use.|False|String||
|Proxy Username|The proxy username to authenticate with.|False|String||
|Proxy Password|The proxy password to authenticate with.|False|Password||




