---
title: "Creating Integration Actions"
---

<a id="CreatingIntegrationActions"></a>


Connector Action (Integration) only represents a host for a group of one or more integration tasks. The UiPath Data Service integration is defined at task level, not at action (integration) level.

If a connector action (integration) has more tasks, the response data will be returned to the flow only after ALL tasks inside the action have run. Implicitly, data in the response entity might be altered by the execution of each task. Also, tasks within the same action can be of different types (SQL, REST, SOAP, SMTP, etc.).

Thus, at Connector Action (Integration) level, only the general information is saved, and used for describing and identifying the action.

Using the solution’s Connector Designer, you can define the integration actions and tasks:

1. From the main menu, click **Integrations**. The Connector Designer appears.
2. At the top-right corner of the page, click the **Create Connector Action** button (![](../../Resources/Images/UiPath%20Data%20Service%20Connector/Creating%20Integration%20Actions.png)). The Edit Connector Action page appears by default on the **ConnectorGeneral** tab.
3. Provide the connector action general details by setting up the parameters described in the table below.

| Parameter | Description |
| --- | --- |
| Name | The name of the action. The field is mandatory. |
| Description | A brief description of the action that might be useful for other tenant admins. The field is mandatory. |
| Category | Define on the spot when creating the action. Useful when you want to find the actions in the Integrations list. The field is mandatory. |
| Request Entity Name | The entity used by the AI Agent to send data to the external app via the current action. |
| Response Entity Name | The entity which will be used by the AI Agent to receive data from the external app via the current action.  For more information on how to map UiPath Data Service entities to Druid entities, see [Loading UiPath Entity Schema and Mapping Fields](Loading%20UiPath%20Entity%20Schema.md). |
| Is Response Collection | Tick only if the expected response is a list of records.  E.g., a list of holidays, whereas each holiday has its own data set. The response from the integration, in this case, will be saved in [[<ResponseEntity>List]] instead of [[<ResponseEntity>]]. E.g., [[HolidayList]]. |
| Is Active | Tick to activate the connector action. Druid ignores inactive connector actions at runtime. |

![](../../Resources/Images/UiPath%20Data%20Service%20Connector/Creating%20Integration%20Actions_1.png)

4. Click **Save** to save the settings and stay on page to add tasks, or click **Save & Close** to save and exit the page.

If you click **Save**, the **ConnectorSteps** tab appears and you can add UiPath Data Service specific integration tasks.

For more information, see subsequent sections.

![](../../Resources/Images/UiPath%20Data%20Service%20Connector/Creating%20Integration%20Actions_2.png)

You can add as many UiPath Data Service connector actions as best suit your integration needs.

{% hint style="info" %}
**NOTE:** A Connector Action represents a set of one or more integration tasks, which run sequentially and use the same request and response entities.
{% endhint %}
