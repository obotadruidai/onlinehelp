---
title: Step 2. Create Integration Action
---


Connector Action (Integration) only represents a host for a group of one or more integration tasks. The integration technology/type (Azure Storage, SQL, REST, SOAP, SMTP, etc.) is defined at task level, not at action (integration) level.

**Example**: If, at a certain point in the conversation flow, you need to send an email to the client, but the necessary data for that email comes from 2 different sources, you can create a single action which always performs the 3 operations, sequentially (getting email address from an SQL Database, then getting some HR data via a REST API call, and then sending this data to that email address using a SMTP call). From the flow designing point of view, you only place one integration action on the flow step.

If a connector action (integration) has more tasks, the response data will be returned to the flow only after ALL tasks inside the action have run. Implicitly, data in the response entity might be altered by the execution of each task. Also, tasks within the same action can be of different types (Azure Storage, SQL, REST, SOAP, SMTP, etc.).

Thus, at Connector Action (Integration) level, only the general information is saved, and used for describing and identifying the action.

Using the solution’s Connector Designer, you can define the integration actions and tasks:

1. From the main menu, click **Integrations**. The Connector Designer appears.
2. At the top-right corner of the page, click the **Create Connector Action** button (![](<../../../.gitbook/assets/Step 2 Create Integration.png>)). The Edit Connector Action page appears by default on the **ConnectorGeneral** tab.
3. Provide the connector action general details by setting up the parameters described in the table below.

| Parameter              | Description                                                                                                                                                                                                                                                                                              |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                   | The name of the action. The field is mandatory.                                                                                                                                                                                                                                                          |
| Description            | A brief description of the action that might be useful for other tenant admins. The field is mandatory.                                                                                                                                                                                                  |
| Category               | Define on the spot when creating the action. Useful when you want to find the actions in the Integrations list. The field is mandatory.                                                                                                                                                                  |
| Icon                   | Select the icon that best describes the integration. It helps you easily identify the integration action in the list of integrations. If no icon is selected, DRUID will show default icon. ![](<../../../.gitbook/assets/default icon.png>) **NOTE:** This field is available in DRUID 1.71 and higher. |
| Request Entity Name    | The entity used by the AI Agent to send data to Azure Storage via the current action.                                                                                                                                                                                                                    |
| Response Entity Name   | The entity used by the AI Agent to receive the share URL from Azure Storage via the current action.                                                                                                                                                                                                      |
| Is Response Collection | Tick only if the expected response is a list of records. Leave unticked as the response is only a share URl.                                                                                                                                                                                             |
| Is Active              | Tick to activate the connector action. An inactive connector action will be ignored at runtime.                                                                                                                                                                                                          |

![](<../../../.gitbook/assets/Step 2 Create Integration_1.png>)

4. Click **Save** to save the settings and stay on page to add tasks, or click **Save & Close** to save and exit the page.

If you click **Save**, the **ConnectorSteps tab** appears.

You can add as many connector actions as best suit your integration needs.

{% hint style="info" %}
**NOTE:** A Connector Action represents a set of one or more integration tasks, which run sequentially and use the same request and response entities.
{% endhint %}
