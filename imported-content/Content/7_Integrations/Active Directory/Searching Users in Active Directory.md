---
title: Searching Users in Active Directory
---

# Searching Users in Active Directory

This section describes how to add and configure an AD integration task to search user(s) in Active Directory.

### Step 1. Set the task general parameters

At the top-right corner of the Edit Connector Action page, **Connector steps** tab, click on the **Create Task** button and select **Active Directory** > **Search**. The task configuration page appears by default on the **General** tab.

Set the general parameters provided in the table below.

| Parameter      | Description                                       |
| -------------- | ------------------------------------------------- |
| Description    | Provide a brief relevant description of the task. |
| ConnectionCode | Select the AD app.                                |

![](<../../../.gitbook/assets/task details.png>)

Save the task general settings.

### Step 2. Set the request

Click the **Request** tab and set the request details.

| Parameter       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Search base     | The path to the AD folder. For faster LDAP queries, we recommend you to further filter the AD zone.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| LDAP Query      | Write down the LDAP Statement you wish to run on AD. For more information on the LDAP syntax, see [Active Directory: LDAP Syntax Filters](https://social.technet.microsoft.com/wiki/contents/articles/5392.active-directory-ldap-syntax-filters.aspx#Special_Characters). Example: LDAP statement for searching for all users with FirstName = \[\[ChatUser]].FirstName: `(&(objectCategory=person)(objectClass=user)(givenName=$firstName))` **NOTE:** In the LDAP statement, use a **transport variable** preceded by the special character “$”, when mentioned in the LDAP statement. |
| Request entity  | Read-only. Druid uses it to pass input data to the LDAP calls. This field is automatically fill-in with the request entity specified on the Connector Action set. You refer this entity in all the Fields mapping on the **Request** tab.                                                                                                                                                                                                                                                                                                                                                |
| Command timeout | Set the time in seconds to wait for the LDAP statement to execute. The default is 2000 milliseconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

#### Mapping request fields

In the Request parameters section, map the request parameters / variables you used in the LDAP statement with the conversation context available in the Request Entity.

Add a new line in the mapping table. In the **Connector field name** column, write the name of the “transport” variable (without $), and in the **Druid entity field name** column, select the corresponding Druid entity field (where the request data is stored).

In order to properly fill in the **Druid entity field name** field, type “\[\[“, choose the Request entity from the drop-down, type “.” after the closing brackets ]] and choose the correct entity field from the new drop-down that appears. Click the **Save** icon displayed inline.

{% hint style="info" %}
**NOTE:** \[\[ChatUser]] entity is always available to all Connector Tasks. Therefore, you can map data both from your Request Entity and from \[\[ChatUser]], in the same mapping table.
{% endhint %}

Save the configuration. Now you need to set up the response as well.

### Step 3. Set the response

Once you have set up the request settings, you need to set up the response as well. To do so, click the **Response** tab and set the response parameters as described in this section.

| Parameter                     | Description                                                                                                                                                                                                                            |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Responseentity                | The entity used by the AI Agent to receive data from AD and pass it into the conversation context. This field automatically fills in with the Response Entity set on the selected AD Connector Action set.                             |
| Response entity is collection | This field is automatically ticked if the Response Entity set on the selected AD Connector Action is expected to be a list of records. The response from the integration, in this case, will be saved in \[\[List]] instead of \[\[]]. |
| ProjectResultToEntityPath     | Use it when you want to map to the response directly to an Entity List type field. Example: retrieving the list of users from a certain group.                                                                                         |

#### Mapping response fields

Add a new line in the mapping section. In the **Connector field name** column, write the name of the element from AD.

In the **Druid entity field name** column, select the corresponding Druid entity field.

In order to properly fill in the **Connector field name** field, type “\[\[“, choose the Request entity from the drop-down, type “.” after the closing brackets ]] and choose the correct entity field from the new drop-down that appears.

Click the **Save** icon displayed inline. Click **Save** to save the settings and stay on page, or click **Save & Close** to save and exit the page.

Now the connector action is ready to be published.

### Step 4. Test the request

The Druid AI Platform provides the possibility to test the configurations of the AD Task directly from authoring portal (without the need to place your newly created connector action in a flow and test it within a AI Agent conversation).

To test a request, click the **Test** tab. Click the **Request entity** tab. The JSON field contains by default the name of the entity used by the AI Agent to send data to the AD app via the current action.

**Example**

```
{
    "$entityTypeName$": "Employee"
}
```

In order to test the task, you need to create an initial context, used for request (similar to when the task is called from a conversation, where Request Entity has data from conversational context). To do that, you’ll need to provide the request entity data in JSON format. Create the JSON object for a Druid entity in the following way:

* Mention the entity name in "$entityTypeName$" property. E.g., `"$entityTypeName$":"Employee"`.
* Add a new property for each field in Druid entity. E.g., `"EmployeeId":1234` or `"FirstName":"John"`.

Example of a Druid entity in Jobject format:

**Example - Druid entity in Jobject format**

```
{
    "$entityTypeName$": "Employee",
    "EmployeeId":1234,
    "JobTitle":"LineManager",
    "EmploymentDate":"2020-01-20"
}
```

In case you need to map data from the **\[\[ChatUser]]** entity, as well, click the **Chat user** tab and in the JSON field, replace the values of the chat user details:

**Mapping data from \[\[ChatUser]]**

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

If the test is successful, you will see data in **Response entity** tab (here you can see how would the response entity look like when the connector task will be called within a conversation).

You can also check the **Request task** tab, to see the LDAP statement (with values) for this particular test.

If the test fails, you can navigate through the **Test result** tabs to troubleshoot misconfiguration.
