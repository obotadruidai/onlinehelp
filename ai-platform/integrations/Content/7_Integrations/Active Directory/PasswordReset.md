---
title: "Putting Users in the \"Requires Password Reset\" State in Active Directory"
---

<a id="PuttingUsersintheRequiresPasswordResetStateinActiveDirectory"></a>


This section describes how to add and configure an AD integration task to put users in the state "requires password reset" in Active Directory. Upon the next login, users will be prompted to set a new password.

<a id="Step1Setthetaskgeneralparameters"></a>

## Step 1. Set the task general parameters

At the top-right corner of the Edit Connector Action page, **Connector steps** tab, click **Create task** and select **Active Directory > Reset Password**. The configuration page appears by default on the **General** tab.

Set the general parameters provided in the table below.

| Parameter | Description |
| --- | --- |
| Description | Provide a brief relevant description of the task. |
| Connection Code | Select the AD app. |

Save the configuration.

<a id="Step2Settherequest"></a>

## Step 2. Set the request

Click the **Request** tab and set the request details.

| Parameter | Description |
| --- | --- |
| User Distinguished Name | Enter the name of the field that stores the LDAP distinguished name of the user to unlock. This field is mandatory.  To properly fill in this field, type “[[“, choose your entity, type “.” after the closing brackets ]] and choose the correct entity field from the new drop-down that appears.  *Example: [[Employee]].AD\_UserDN* |
| Request entity | Read-only. Druid uses it to pass input data to the LDAP calls. This field is automatically fill-in with the request entity specified on the Connector Action set.  You refer this entity in all the Fields mapping on the **Request** tab. |
| CommandTimeout | Set the time in seconds to wait for the LDAP statement to execute. The default is 2000 milliseconds. |

Save the configuration. As the request is not expected an answer in Druid, the **Response** tab is not visible in Druid.

<a id="Step3Testtherequest"></a>

## Step 3. Test the request

The Druid AI Platform provides the possibility to test the configurations of the AD Task directly from authoring portal (without the need to place your newly created connector action in a flow and test it within a AI Agent conversation).

To test a request, click the **Test** tab. Click the **Request Entity** tab. The JSON field contains by default the name of the entity used by the AI Agent to send data to the AD app via the current action.

**Example**

```
{
    "$entityTypeName$": "Employee"
}
```

To test the task, you need to create an initial context, used for request (similar to when the task is called from a conversation, where Request Entity has data from conversational context). To do that, you’ll need to provide the request entity data in JSON format. Create the JSON object for a Druid entity in the following way:

- Mention the entity name in "$entityTypeName$" property. E.g., `"$entityTypeName$":"Employee"`.
- Add a new property for each field in Druid entity. E.g., `"EmployeeId":1234` or `"FirstName":"John"`.

**Example - Druid entity in Jobject format**

```
{
    "$entityTypeName$": "Employee",
    "EmployeeId":1234,
    "JobTitle":"LineManager",
    "EmploymentDate":"2020-01-20"
}
```

In case you need to map data from the **[[ChatUser]]** entity, as well, click the **Chat User** tab and in the JSON field, replace the values of the chat user details:

**Mapping data from [[ChatUser]]**

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

At the top-right corner of the page click the **Test** button. In the lower part the **Test** tab you will see the result of the test.

If the test is successful, you will see data in **Response Entity** tab (here you can see how would the response entity look like when the connector task will be called within a conversation).

You can also check the **Request Task** tab, to see the LDAP statement (with values) for this particular test.

If the test fails, you can navigate through the **Test Result** tabs to troubleshoot the misconfiguration.
