---
title: Connector Designer
---


The Connector Designer enables authors to create complex automations. It allows you to define the integration steps (for a connector action), add integration tasks, set conditions on integration tasks, link tasks, etc.

![](<../../../.gitbook/assets/designer overview.png>)

{% hint style="info" %}
**NOTE:** The Connector Designer is available in technology preview in DRUID 5.12 and higher.
{% endhint %}

{% hint style="warning" %}
**IMPORTANT!** If you define a complex automation using the Connector Designer, do any subsequent changes using the Connector Designer; otherwise, the automation will break.
{% endhint %}

## Access the Connector Designer

To access the Connector Designer, in your connector action, click the **Connector steps** tab and the diagram icon.

![](../../../.gitbook/assets/access.png)

The Connector Designer appears.

![](<../../../.gitbook/assets/diagram (2).png>)

The Actions menu provides you with extensive options to edit and analyze the flow and the flow steps.

|                                             |                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![](../../../.gitbook/assets/Diagram_4.png) | **Settings**. Edit the selected integration task.                                                                                                                                                                                                                                                                                                                                                   |
| ![](../../../.gitbook/assets/Diagram_5.png) | **Info**. View and edit the current integration (connector action) details.                                                                                                                                                                                                                                                                                                                         |
| ![](../../../.gitbook/assets/audit.png)     | **Code**. Provides you with the JSON structure of the connector action and a comprehensive historical record of all changes made by authors to the integrations (**Audit trail** tab). For information on how to view the flow changes, see [Review flow changes.htm](https://druidai.gitbook.io/druid-ai-docs/ai-platform/build-ai-agents/authoring-tools/flows/review-flow-changes). **NOTE:** The Audit feature is available in technology preview in DRUID version 7.8. |
| ![](../../../.gitbook/assets/Diagram_9.png) | **Analytics**. View integration analytics.                                                                                                                                                                                                                                                                                                                                                          |

In the Connector Designer, all integration tasks are connected by strong links (![](<../../../.gitbook/assets/Bot Diagram_20.png>)). The last integration tasks is marked with **END**.

## Add integration tasks

On the connector (arrow), place the mouse over the add icon (![](<../../../.gitbook/assets/Flows Diagram_3.png>) ) and select the desired integration type you want to add. By default, you can select from the six most common integration tasks types. If you want to add other available integration tasks types, use the Connector Palette (![](<../../../.gitbook/assets/flow palette.png>)).

![](<../../../.gitbook/assets/add task.png>)

You can also use the Connector Palette to add integration tasks, except for the first one.

## Set conditions

On the connector (arrow), the place the mouse over the settings icon (![](<../../../.gitbook/assets/Flows Diagram_1.png>)) and click on it. The Update link condition editor appears on the right. Define which condition should be met for the next integration task to be executed. The green Settings icon (![](<../../../.gitbook/assets/Flows Diagram_5.png>)) on the connector indicates that a condition is defined on the integration task.

## Link two integration tasks

Linking integration tasks is useful when you want to jump on another existing integration task (up or down) when a given condition is met.

To link two integration tasks, place the cursor on the task you want to link, hover over the link icon and click **Link to Task**.

![](<../../../.gitbook/assets/link tasks.png>)

The LinkTask page appears. From the drop-down, select next task to be executed if the condition you define on this page is met.

![](../../../.gitbook/assets/nexttask.png)

## Use the Connector Palette

The Connector Palette simplifies AI Agent authoring. It displays all integration tasks defined on the AI Agent organized by category.

To access the Connector Palette, click the ![](<../../../.gitbook/assets/Flow Palette.png>) icon on the left side of the Connector Designer. You can also access the Connector Palette from the Connector Designer by hovering the mouse over the add icon (![](<../../../.gitbook/assets/Flows Diagram_3.png>)) and clicking the **Connector Palette** icon (![](<../../../.gitbook/assets/flow palette.png>)). When you add the first integration task, use the second option.

You use the Connector Palette using drag and drop functionality. Search for the desired integration task or navigate the Connector Palette until you find the desired task, drag and drop it in the working area as follows based on where you want to add the task:

* To add the task between two existing integration tasks, place the task on the line that connects the two tasks and when the line connecting the second step is highlighted, drop the task from the Connector Palette.

![](<../../../.gitbook/assets/Flow Palette_8.png>)

* To add as child integration task, place the cursor on the parent task and when it is highlighted, drop the integration tas from the Connector Palette.

![](<../../../.gitbook/assets/Flow Palette_9.png>)

To configure DRUID predefined integration tasks steps, in the working area, click on the desired task and use the right editor to configure the details.

## Related Topics

* [Using Connector Local Variables](../Use_connector_local_variables.md)
