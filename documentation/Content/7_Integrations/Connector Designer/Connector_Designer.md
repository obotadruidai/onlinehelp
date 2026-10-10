<a id="ConnectorDesigner"></a>

# Connector Designer

The Connector Designer enables authors to create complex automations. It allows you to define the integration steps (for a connector action), add integration tasks, set conditions on integration tasks, link tasks, etc.

![](../../Resources/Images/CNN%20Designer/designer%20overview.png)

> **NOTE:** The Connector Designer is available in technology preview in DRUID 5.12 and higher.

> **IMPORTANT!** If you define a complex automation using the Connector Designer, do any subsequent changes using the Connector Designer; otherwise, the automation will break.

<a id="AccesstheConnectorDesigner"></a>

## Access the Connector Designer

To access the Connector Designer, in your connector action, click the **Connector steps** tab and the diagram icon.

![](../../Resources/Images/CNN%20Designer/access.png)

The Connector Designer appears.

![](../../Resources/Images/CNN%20Designer/diagram.png)

The Actions menu provides you with extensive options to edit and analyze the flow and the flow steps.

|  |  |
| --- | --- |
| ![](../../Resources/Images/Diagram/Diagram_4.png) | **Settings**. Edit the selected integration task. |
| ![](../../Resources/Images/Diagram/Diagram_5.png) | **Info**. View and edit the current integration (connector action) details. |
| ![](../../Resources/Images/Diagram/audit.png) | **Code**. Provides you with the JSON structure of the connector action and a comprehensive historical record of all changes made by authors to the integrations (**Audit trail** tab). For information on how to view the flow changes, see [Review flow changes.htm](../../4_Flows/Review%20flow%20changes.md).  **NOTE:** The Audit feature is available in technology preview in DRUID version 7.8. |
| ![](../../Resources/Images/Diagram/Diagram_9.png) | **Analytics**. View integration analytics. |

In the Connector Designer, all integration tasks are connected by strong links (![](../../Resources/Images/Flow%20Graphical%20Designer/Bot%20Diagram_20.png)). The last integration tasks is marked with **END**.

<a id="Addintegrationtasks"></a>

## Add integration tasks

On the connector (arrow), place the mouse over the add icon (![](../../Resources/Images/Flow%20Graphical%20Designer/Flows%20Diagram_3.png) ) and select the desired integration type you want to add. By default, you can select from the six most common integration tasks types. If you want to add other available integration tasks types, use the Connector Palette (![](../../Resources/Images/Diagram/flow%20palette.png)).

![](../../Resources/Images/CNN%20Designer/add%20task.png)

You can also use the Connector Palette to add integration tasks, except for the first one.

<a id="Setconditions"></a>

## Set conditions

On the connector (arrow), the place the mouse over the settings icon (![](../../Resources/Images/Flow%20Graphical%20Designer/Flows%20Diagram_1.png)) and click on it. The Update link condition editor appears on the right. Define which condition should be met for the next integration task to be executed. The green Settings icon (![](../../Resources/Images/Flow%20Graphical%20Designer/Flows%20Diagram_5.png)) on the connector indicates that a condition is defined on the integration task.

<a id="Linktwointegrationtasks"></a>

## Link two integration tasks

Linking integration tasks is useful when you want to jump on another existing integration task (up or down) when a given condition is met.

To link two integration tasks, place the cursor on the task you want to link, hover over the link icon and click **Link to Task**.

![](../../Resources/Images/CNN%20Designer/link%20tasks.png)

The LinkTask page appears. From the drop-down, select next task to be executed if the condition you define on this page is met.

![](../../Resources/Images/CNN%20Designer/nexttask.png)

<a id="UsetheConnectorPalette"></a>

## Use the Connector Palette

The Connector Palette simplifies AI Agent authoring. It displays all integration tasks defined on the AI Agent organized by category.

To access the Connector Palette, click the ![](../../Resources/Images/Flow%20Palette_v2_oana/Flow%20Palette.png) icon on the left side of the Connector Designer. You can also access the Connector Palette from the Connector Designer by hovering the mouse over the add icon (![](../../Resources/Images/Flow%20Graphical%20Designer/Flows%20Diagram_3.png)) and clicking the **Connector Palette** icon (![](../../Resources/Images/Diagram/flow%20palette.png)). When you add the first integration task, use the second option.

You use the Connector Palette using drag and drop functionality. Search for the desired integration task or navigate the Connector Palette until you find the desired task, drag and drop it in the working area as follows based on where you want to add the task:

- To add the task between two existing integration tasks, place the task on the line that connects the two tasks and when the line connecting the second step is highlighted, drop the task from the Connector Palette.

![](../../Resources/Images/Flow%20Palette_v2_oana/Flow%20Palette_8.png)

- To add as child integration task, place the cursor on the parent task and when it is highlighted, drop the integration tas from the Connector Palette.

![](../../Resources/Images/Flow%20Palette_v2_oana/Flow%20Palette_9.png)

To configure DRUID predefined integration tasks steps, in the working area, click on the desired task and use the right editor to configure the details.

## Related Topics

- [Using Connector Local Variables](../Use_connector_local_variables.md)
