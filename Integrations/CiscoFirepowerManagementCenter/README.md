
# CiscoFirepowerManagementCenter

Cisco Firepower analyzes your network's vulnerabilities, prioritizes any attacks, and recommends protections so your security team can focus on strategic activities.

Python Version - 3
#### Parameters
|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|API Root|None|True|None|https://x.x.x.x/|
|Username|None|True|String||
|Password|None|True|Password|None|
|Verify SSL|None|False|Boolean||



## Actions
#### Unblock Address
Unblock address in Cisco Firepower
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Network Group Name|Network object name.|True|String|None|



#### Block URL
Block URL by assigning it to a URL group attached to a policy
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|URL Group Name|URL group object name.|True|String|None|



#### Unblock Port
Remove port from a group of blocked ports
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Port Group Name|Name of the port object group.|True|String||
|Port|Target port, e.g. 9856.|True|String|None|



#### Ping
Test Connectivity
Timeout - 600 Seconds



#### Block Port
Block port by assigning it to a port group attached to a policy
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Port Group Name|Name of the port object group.|True|String|None|
|Port|Port to block, e.g. 9856.|True|String|None|
|Port Protocol|Target port protocol, e.g. TCP.|True|String|None|



#### Block Address
Block IP address by assigning it to a network group attached to a policy
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Network Group Name|Network object name.|True|String|None|



#### Unblock URL
Remove URL from a groups of blocked URLs
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|URL Group Name|URL group object name.|True|String|None|



#### Get URL List By Name
Get list of URL fro specific group by it's name.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|URL Group Name|The name of the needed URL group.|True|String|None|



##### JSON Results
```json

```



#### Get Ports List By Name
Get list of blocked ports for specific group by it's name.
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Port Group Name|The name of the needed ports group.|True|String|None|



##### JSON Results
```json

```



#### Get Addresses List By Name
Get list of blocked addresses in a specific network group by it's name. 
Timeout - 600 Seconds


|Name|Description|IsMandatory|Type|DefaultValue|
|----|-----------|-----------|----|------------|
|Network Group Name|The name of the needed network group.|True|String|None|



##### JSON Results
```json

```









