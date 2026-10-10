---
title: "Testing Settings"
---

<a id="TestingSettings"></a>


The Druid AI Platform provides the possibility to test the configurations of the SQL Task directly from authoring portal (without the need to place your newly created connector action in a flow and test it within a AI Agent conversation).

To test a request, click the **Test** tab. Click the **RequestEntity** tab. The JSON field contains by default the name of the entity used by the AI Agent to send data to the SQL app via the current action.

For example:

**Request entity - Example**

```
{
    "$entityTypeName$": "LeaveRequest"
}
```

In order to test the task, you need to create an initial context, used for request (similar to when the task is called from a conversation, where Request Entity has data from conversational context). To do that, you’ll need to provide the request entity data in JSON format. Create the JSON object for a Druid entity in the following way:

- Mention the entity name in "$entityTypeName$" property. E.g., `"$entityTypeName$":"Employee"`.
- Add a new property for each field in Druid entity. E.g., `"EmployeeId":1234` or `"FirstName":"John"`.

Example of a Druid entity in Jobject format:

**Druid entity in Jobject format - Example**

```
{
    "$entityTypeName$": "Employee",
    "EmployeeId":1234,
    "JobTitle":"LineManager",
    "EmploymentDate":"2020-01-20"
}
```

In case you need to map data from the **[[ChatUser]]** entity, as well, click the **ChatUser** tab and in the JSON field, replace the values of the chat user details:

**Maping data from the [[ChatUser]] entity - Example**

```
{
    "$entityTypeName$": "ChatUser",
    "Id": "00000000-0000-0000-0000-000000000000",
    "TenantId": 0,
    "TenantUserId": "00000000-0000-0000-0000-000000000000",
    "IsAnonymous": false,
    "IsAuthenticated": false,
    "BotId": "00000000-0000-0000-0000-000000000000",
    "IsConnectedAsHelpdeskAgent": false,
    "IsAwaitingHelpdeskAgent": false,
    "IsConnectedToHelpdeskAgent": false,
    "ConversationStatus": "None",
    "WasAuthenticated": false,
    "ClientTimeStamp": "0001-01-01T00:00:00Z",
    "ServerTimeStamp": "0001-01-01T00:00:00Z",
    "IsCommandChannel": false
}
```

At the top-right corner of the page click the **Test** button. In the lower part the Test tab you will see the result of the test.

If the test is successful, you will see data in **ResponseEntity** tab (here you can see how would the response entity look like when the connector task will be called within a conversation).

![](../../Resources/Images/SQL%20Connector/Testing%20Settings.png)

You can also check the **Request Task** tab, to see the SQL statement (with values) for this particular test.

> **NOTE:** For SQL connector tasks, the response task will not return any values in the user interface.

![](../../Resources/Images/SQL%20Connector/Testing%20Settings_1.png)

If the test fails, you can navigate through the **Test Result** tabs to troubleshoot misconfiguration.

![](../../Resources/Images/SQL%20Connector/Testing%20Settings_2.png)
