---
title: Druid Data Service Connector
---

# Druid Data Service Connector

Druid Data Service Connector enables authors to use (at a conversational level) Druid entity records that are stored in Druid Data Service. Using this connector is out of the box, as entity records are stored in Druid Data Service, there is no need to define connection strings. You create connector actions and define the Druid Data Service specific integration tasks, then call the integrations tasks on the flows as best suits your needs.

{% hint style="info" %}
**NOTE:** Instead of manually configuring integrations, you can use AI Authoring Agents to automate the process. By launching the Integrations Engineer from the Page Help icon on the Integrations page, you can describe your business requirements in natural language to automatically create or fine-tune Druid Data Service integration through guided chat interactions. For more information, see the [AI Authoring Agents](<../../2_AI Agents/AI Authoring Agents.md#Create2>).
{% endhint %}

### Step 1. Create connector action

Connector Action (Integration) only represents a host for a group of one or more integration tasks. DRUID Data Service integration is defined at task level, not at action (integration) level.

If a connector action (integration) has more tasks, the response data will be returned to the flow only after ALL tasks inside the action have run. Implicitly, data in the response entity might be altered by the execution of each task. Thus, at Connector Action (Integration) level, only the general information is saved, and used for describing and identifying the action.

Using the solution Connector Designer, you can define the integration actions and tasks:

1. From the main menu, click **Integrations**. The Connector Designer appears.
2. At the top-right corner of the page, click the **Create Connector Action** button. The Edit Connector Action page appears by default on the **ConnectorGeneral** tab.
3. Provide the connector action general details by setting up the parameters described in the table below.

| Parameter              | Description                                                                                                                                                                                                                                                                                              |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                   | The name of the action. The field is mandatory.                                                                                                                                                                                                                                                          |
| Description            | A brief description of the action that might be useful for other tenant admins. The field is mandatory.                                                                                                                                                                                                  |
| Category               | Define on the spot when creating the action. Useful when you want to find the actions in the Integrations list. The field is mandatory.                                                                                                                                                                  |
| Icon                   | Select the icon that best describes the integration. It helps you easily identify the integration action in the list of integrations. If no icon is selected, DRUID will show default icon. ![](<../../../.gitbook/assets/default icon.png>) **NOTE:** This field is available in DRUID 1.71 and higher. |
| Request Entity Name    | The entity used by the AI Agent to send data DRUID Data Service via the current action. On the request and response, DRUID will map all entity fields existing in the request entity set on the connector action.                                                                                        |
| Response Entity Name   | The entity that will be used by the AI Agent to receive data DRUID Data Service via the current action.                                                                                                                                                                                                  |
| Is Response Collection | Tick only if the expected response is a list of records. E.g., a list of holidays, whereas each holiday has its own data set. The response from the integration, in this case, will be saved in \[\[List]] instead of \[\[]]. E.g., \[\[HolidayList]].                                                   |
| Is Active              | Tick to activate the connector action. DRUID ignores inactive connector actions at runtime.                                                                                                                                                                                                              |

4. Click **Save** to save the settings and stay on page to add tasks, or click **Save & Close** to save and exit the page.

If you click Save, the **ConnectorSteps** tab appears and you can add DRUID Data Service specific integration tasks.

For more information, see subsequent sections.

You can add as many UiPath Data Service connector actions as best suit your integration needs.

{% hint style="info" %}
**NOTE:** A Connector Action represents a set of one or more integration tasks, which run sequentially and use the same request and response entities.
{% endhint %}

### Step 2. Add Druid Data Service integration tasks

After you saved the connector action, click the **ConnectorSteps** tab and the top-right corner of the page, click **Create Task**. On the drop-down, click **DRUID Data Service** and then click on the integration task you want to add.

![](<../../../.gitbook/assets/Druid Data Service Connector_5.png>)

For information on each integration task, see subsequent section in the Help.

Make sure that you publish the integrations.

On the request and response, DRUID will automatically return the schema of the request entity set on the connector action if the **Scope** is Global.

### Step 3. Use the integrations on flows as needed

Call the integration tasks on flow steps as best suits your needs.

### Related Topics

* [Debugging Integrations](<../Debugging Integrations.md>)
* [Post Actions](<../../4_Flows/Post Actions.md>)
* [Pre Actions](<../../4_Flows/Pre Actions.md>)
