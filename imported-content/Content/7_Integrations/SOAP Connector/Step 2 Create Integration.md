---
layout:
  title:
    visible: false
---

<a id="Step2CreateIntegrationActions"></a>

# Step 2. Create Integration Actions

Connector Action (Integration) only represents a host for a group of one or more integration tasks. The integration technology/type (SQL, REST, SOAP, SMTP, etc.) is defined at task level, not at action (integration) level.

Example: If, at a certain point in the conversation flow, you need to send an email to the client, but the necessary data for that email comes from 2 different sources, you can create a single action which always performs the 3 operations, sequentially (getting email address from an SQL Database, then getting some HR data via a SOAP API call, and then sending this data to that email address using a SMTP call). From the flow designing point of view, you only place one integration action on the flow step.

If a connector action (integration) has more tasks, the response data will be returned to the flow only after ALL tasks inside the action have run. Implicitly, data in the response entity might be altered by the execution of each task. Also, tasks within the same action can be of different types (SQL, REST, SOAP, SMTP, etc.).

Thus, at Connector Action (Integration) level, only the general information is saved, and used for describing and identifying the action.

Using the solution’s Connector Designer, you can define the integration actions and tasks:

1. From the main menu, click **Integrations**. The Connector Designer appears.

![](../../Resources/Images/SOAP%20Connector/Step%202%20Create%20Integration.png)

2. At the top-right corner of the page, click the **Create Connector Action** button (![](../../Resources/Images/SOAP%20Connector/Step%202%20Create%20Integration_1.png)). The Edit Connector Action page appears by default on the **ConnectorGeneral** tab.
3. Provide the connector action general details by setting up the parameters described in the table below.

| Parameter | Description |
| --- | --- |
| Name | The name of the action. The field is mandatory. |
| Description | A brief description of the action that might be useful for other tenant admins. The field is mandatory. |
| Category | Define on the spot when creating the action. Useful when you want to find the actions in the Integrations list. The field is mandatory. |
| Icon | Select the icon that best describes the integration. It helps you easily identify the integration action in the list of integrations. If no icon is selected, DRUID will show default icon.  ![](../../Resources/Images/default%20icon.png)  **NOTE:** This field is available in DRUID 1.71 and higher. |
| Request Entity Name | The entity used by the AI Agent to send data to the external app via the current action. |
| Response Entity Name | The entity used by the AI Agent to receive data from the external app via the current action. |
| Is Response Collection | Tick only if the expected response is a list of records.  E.g., a list of holidays, whereas each holiday has its own data set. The response from the integration, in this case, will be saved in [[<ResponseEntity>List]] instead of [[<ResponseEntity>]]. E.g., [[HolidayList]]. |
| Is Active | Tick to activate the connector action. An inactive connector action will be ignored at runtime. |

![](../../Resources/Images/SOAP%20Connector/Step%202%20Create%20Integration_2.png)

4. Click **Save** to save the settings and stay on page to add tasks, or click **Save & Close** to save and exit the page.

If you click **Save**, the **ConnectorSteps** tab appears and you can define the SOAP integration tasks as best suits your needs.

You can add as many SOAP connector actions as best suit your integration needs.

> **NOTE:** A Connector Action represents a set of one or more integration tasks, which run sequentially and use the same request and response entities.
