<a id="DRUID526"></a>

# DRUID 5.26

Deployment Dates

The table below lists the deployment date of DRUID v5.26 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| October 26, 2023 | November 23, 2023 | November 23, 2023 | November 23, 2023 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

<a id="Improvements"></a>

## Improvements

- **Global and Local scope available for SQL integrations**. With this release, the SQL connector becomes a tool you can use to implement very complex automations. A new field, **Scope** is available on integration tasks (on both the Request and Response tabs) that allows you to set a local context that is different from the global context set on the connector action (the entity set as Request / Response entity on the connector action).

Using the **Local** scope, you do all related queries directly inside the connector action instead of building a larger context outside the connector action via additional queries within the Flow Designer to put data inside the request entity and then send the data back to the connector action.

- **Technology preview! DRUID Data Services - DRUID custom query in the Query related entity task**. The DRUID Data Services Query related entity integration tasks now offer you with the option to interrogate other entities. The DRUID custom query supports a set of TSQL transactions (statements, functions, operators and clauses). For more information, see [Query Related Entity](../../7_Integrations/Druid%20Data%20Service%20Connector/Query_Related_Entity.md).
- **Entity Designer in tree view**. When editing an entity by clicking on it in the Entity designer in tree view, the entity fields, flows and integrations are now available in the entity editor.

![](../../Resources/Images/druid%205.26/entity%20editor%20tabs%20new.png)

- **Live Chat - Helpdesk agent**. You can provide your helpdesk agents with the option to preview and edit predefined messages before sending them in the chat by using the following syntax of the **sendMessage** JavaScript function: `sendMessage ("message/text",true)`, in backchannel steps on the client connected flow.

**Example: Previewing predefined messages**

```
<div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
    <a class="dropdown-item" onclick='sendMessage("Thank you for waiting! How may I help you?",true)'>Thank you for waiting</a>
    <a class="dropdown-item" onclick='sendMessage("Thank you for your time. To help us improve the quality of our services please give feedback. Have a nice day!",true)'>Ask feedback</a>
</div>
```

- **Web views: Recommend Automations and the Chat**. With this release, two features are available on web views that allow you to:

- Provide your business users with the possibility to trigger conversational flows on entity records directly from views by making available a set of recommended automations.

![](../../Resources/Images/druid%205.26/view%20automations.png)

For more information, see [Recommend automations on views](../../CBA/Recommend%20automations%20on%20views.md).

- Enable your business users to chat with the AI Agent directly from a web view.

![](../../Resources/Images/druid%205.26/chat%20on%20view.png)

For more information, see [Enable chat in views](../../CBA/Enable%20chat%20in%20views.md).

<a id="BugFixes"></a>

## Bug Fixes

- **Connector - Local scope**: Local scope set on a response that is a collection is now working inside a connector action that is not a collection.
- **Flow Designer**: Multiple Save on UiPath steps no longer causes children steps to disappear.
