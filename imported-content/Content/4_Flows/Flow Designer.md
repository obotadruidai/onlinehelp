<a id="FlowDesigner"></a>

# Flow Designer

The Flow Graphical Designer is a robust tool that simplifies flow design within the Druid AI Platform, enhancing efficiency for authors. It offers an intuitive interface for visualizing, creating, and updating flows.

<a id="AccessingtheFlowDesigner"></a>

## Accessing the Flow Designer

To access the Flow Designer, select the AI Agent and solution, then click **Flows** on the main menu. The Flow Designer appears within the context of the selected AI Agent and solution.

![](../Resources/Images/Flows/flow%20designer_no%20flows.png)

If no flows are defined for the selected AI Agent within the current solution, the Flow Designer list will be empty.

<a id="FlowDesignerOverview"></a>

## Flow Designer Overview

You have two options for viewing flows within the current solution:

|  |  |
| --- | --- |
| ![](../Resources/Images/Entities/list%20view.png) | **List View**: Displays all flows in alphabetical order.  ![](../Resources/Images/Flows/flow%20designer_no%20flows.png) |
| ![](../Resources/Images/Entities/diagram%20view.png) | **Diagram View**:Provides a graphical visualization of flows and their interconnections within the selected AI Agent. ![](../Resources/Images/Flows/flows%20in%20diagram%20view.png) |

<a id="Availablefunctionality"></a>

### Available functionality

|  |  |
| --- | --- |
| Test utterance | Analyzes user phrases and attempts to match them with existing conversations, displaying Confidence Percentage based on the current training dataset.  ![](../Resources/Images/Flows/test%20utterance.png) |
| Search flow | Allows searching for flows using both exact and partial flow names. |
| View flows within a category | Enables grouping flows into categories for easier navigation and management.  **NOTE:** Available only in list view. |
| Link / Unlink flows | Adds or removes flows from the current solution.  **NOTE:** Available only in list view. |
| Create a new flow | Adds new flows to the selected solution. |
| Edit / Delete a flow | Allows editing or deleting a flow from the selected solution. |
| Clone flows | Creates a copy of a specific flow for reuse. To clone a flow, click the **Clone** icon displayed inline with the flow and confirm. The cloned flow appears on the **Steps** tab. Click the **Details** tab to rename the flow and adjust its elements as needed.  **NOTE:** Available only in list view. |

<a id="AIAgentDiagramDesigner"></a>

## AI Agent Diagram Designer

- Enables authors to visualize AI Agent flows and the connections between them.
- Highlights inconsistency zones requiring attention from AI Agent authors.
- Provides insights into the primary conversation path and possible flow paths.

To access the AI Agent Diagram Designer, in Druid Portal, select the AI Agent, select solution and click **Flows**. The Flows page appears.

At the top-left corner of the page, click the icon ![](../Resources/Images/Flow%20Graphical%20Designer/Bot%20Diagram_1_38x39.png). Diagram Designer appears.

![](../Resources/Images/Flow%20Graphical%20Designer/Bot%20Diagram_2.png)

The nodes in the diagram represent the flows. By default, the Diagram Designer displays the most recently viewed selection on the **Toolbar**.

> **Info:** You can always go back to the flows list view by clicking the List view icon.

<a id="Toolbar"></a>

### Toolbar

The Toolbar offers options for viewing flow lists, flow steps, and adding/editing flow steps or child flows. Additionally, it provides features for flow layout adjustments and various actions such as testing, debugging, and analytics.

| Button | Description |
| --- | --- |
| ![](../Resources/Images/Flow%20Graphical%20Designer/Bot%20Diagram_4.png) | Highlights the Welcome flow and the primary conversation path. ![](../Resources/Images/Flow%20Graphical%20Designer/Bot%20Diagram_5.png) |
| ![](../Resources/Images/Flow%20Graphical%20Designer/Bot%20Diagram_6.png) | Displays flows in the current solution. |
| ![](../Resources/Images/Flow%20Graphical%20Designer/Bot%20Diagram_7.png) | Displays all AI Agent flows inside and outside the current solution. |
| ![](../Resources/Images/Flow%20Graphical%20Designer/Bot%20Diagram_8.png) | Hides the flows details (badges and names). ![](../Resources/Images/Flow%20Graphical%20Designer/hidden%20flow%20details.png) |
| ![](../Resources/Images/Flow%20Graphical%20Designer/Bot%20Diagram_9.png) | Displays the flows name. ![](../Resources/Images/Flow%20Graphical%20Designer/Bot%20Diagram_10.png) |
| ![](../Resources/Images/Flow%20Graphical%20Designer/Bot%20Diagram_11.png) | Displays in badges the number of child flows. ![](../Resources/Images/Flow%20Graphical%20Designer/child%20steps.png) |
| ![](../Resources/Images/Flow%20Graphical%20Designer/Bot%20Diagram_12.png) | Add a new flow. **NOTE:** From the AI Agent Diagram you can add new flows but you cannot add links between the flows. |
| ![](../Resources/Images/Flow%20Graphical%20Designer/Bot%20Diagram_13.png) | The slicer allows you to view more or less flows based on the number of association levels between the flows. Slice up for more and slice down for less. |

<a id="AIAgentDiagramDesignerLegend"></a>

### AI Agent Diagram Designer Legend

Visual elements within the AI Agent Diagram Designer convey key information:

| Visual element | Description |
| --- | --- |
| ![](../Resources/Images/Flow%20Graphical%20Designer/Bot%20Diagram_14_31x29.png) | Identifies conversation entry points. The big green node indicates the Welcome flow. You can easily view it by clicking the **Home** button on the **Toolbar**. |
| ![](../Resources/Images/Flow%20Graphical%20Designer/Bot%20Diagram_15.png) | Indicates intermediary flows. |
| ![](../Resources/Images/Flow%20Graphical%20Designer/Bot%20Diagram_16_29x27.png) | Indicates AI Agent inconsistency zones. Indicates that the result of a menu flow is not found. The value of a button inside a menu flow does not correspond to a training phrase on any flows. The red endpoint indicates that you need to take action. To view what is missing and take the proper action, put the cursor on the red dotted line. ![](../Resources/Images/Flow%20Graphical%20Designer/Bot%20Diagram_17.png) Click on the red node. The Flows Diagram of the menu flow where you need to take action appears. Make corrections as indicated in the tooltip displayed on the red dotted line. |
| ![](../Resources/Images/Flow%20Graphical%20Designer/Bot%20Diagram_18.png) | Indicates that there are more links between the flow and its child flow(s). Example: the flow task-assign-to contains buttons which lead to the same flow, that is, my-tasks. ![](../Resources/Images/Flow%20Graphical%20Designer/Bot%20Diagram_19.png) |
| ![](../Resources/Images/Flow%20Graphical%20Designer/Bot%20Diagram_20.png) | Indicates that there is a strong link between two flows; that is, there is a trigger flow step defined on the first flow that triggers the execution of the second flow. |
| ![](../Resources/Images/Flow%20Graphical%20Designer/Bot%20Diagram_21.png) | Indicates that there is a soft link between the flows. Indicates the result of a menu flow (flow step of type hero card), where the hero card step does not have input mapping and Is last step. The Flow Designer executes the next flow based on the value put in the hero card button. If the button value corresponds to a training phrase of another flow, a soft link is created between the two flows. |
| ![](../Resources/Images/Flow%20Graphical%20Designer/Bot%20Diagram_22.png) | Indicates that the result of a menu flow is not found. The value of a button inside a menu flow does not correspond to a training phrase on any flows. |

<a id="Viewflowpaths"></a>

### View flow paths

When you click on a flow, the diagram shows the possible paths for the currently selected flow, that is, the links between the currently selected flow and subsequent flows. The bigger node indicates the currently selected flow.

*Example*: Clicking on the menu-loan-analyst node, you get an overview of the conversations dedicated to the loan analyst role.

![](../Resources/Images/Flow%20Graphical%20Designer/Bot%20Diagram_23.png)

<a id="FlowDiagramDesigner"></a>

## Flow Diagram Designer

- Allows users to define the flow structure.
- Facilitates addition of flow child steps and setting conditions on steps.
- Offers detailed visual information on flow step settings, including:

- Number of pre/post actions and variables defined on a flow step.
- Conditions set on a step.
- Identification of the first and last steps in the flow.

To view the Flow Diagram Designer of a specific flow, in the AI Agent Diagram Designer, click the node corresponding to the desired flow.

You can edit a flow by adding steps, editing step details, remove flow steps, add conditions on steps, etc. to best suit your AI Agent needs.

<a id="FlowDiagramToolbar"></a>

### Flow Diagram Toolbar

The Toolbar offers options for viewing flow lists, flow steps, and adding/editing flow steps or child flows. Additionally, it provides features for flow layout adjustments and various actions such as testing, debugging, and analytics.

|  |  |
| --- | --- |
| ![](../Resources/Images/Flow%20Graphical%20Designer/tree%20diagram%20views.png) | Displays the flow steps in either list view or diagram view. |
| ![](../Resources/Images/Diagram/Diagram_1.png) | Displays the flow steps in either tree view or layered digraph view. The layered digraph view is available in Druid version 8.14 and higher. |
| ![](../Resources/Images/Flows/auto%20layout%20flow%20icon.png) | Automatically calculates all flow steps positions. If you select the Auto layout mode, all previous flow steps positions will be lost. |
| ![](../Resources/Images/Flows/manual%20layput%20flow%20icon.png) | Allows you to change the flow steps positions on the Flow Diagram. Click the **Manual layout** icon, change the position of the desired flow steps using drag and drop and click the **Save** icon next to the Manual layout icon. |
| ![](../Resources/Images/Flows/reload.png) | Reload the diagram. |
| ![](../Resources/Images/Diagram/Diagram_2.png) | Add a flow step. |
| ![](../Resources/Images/Diagram/Diagram_3.png) | Add a child flow to the current flow. |
| ![](../Resources/Images/Diagram/serach%20in%20diagram.png) | Search for the following elements within the Flow Diagram:   - Flow step names (e.g., get-step) - Messages (e.g., "Tell me your name", 'your name') - Connector action names (e.g., Case-UpdateStatus) - Link conditions - Child flows - Trigger flows - Hero steps   ![](../Resources/Images/Diagram/search%20flow%20element.png) |

<a id="Actionsmenu"></a>

### Actions menu

The Actions menu provides you with extensive options to edit and analyze the flow and the flow steps.

|  |  |
| --- | --- |
| ![](../Resources/Images/Diagram/Diagram_4.png) | **Settings**. Edit the selected flow step (node). |
| ![](../Resources/Images/Diagram/Diagram_5.png) | **Info**. View and edit the current flow details. |
| ![](../Resources/Images/Diagram/audit.png) | **Audit**. Provides you with the JSON structure of the flow and a comprehensive historical record of all changes made by authors to the flow (**Audit trail** tab). For information on how to view the flow changes, see [Review Flow Changes](Review%20flow%20changes.md).  **NOTE:** The Audit feature is available in technology preview in DRUID version 7.3. |
| ![](../Resources/Images/Diagram/Diagram_6.png) | **Webchat**. Test your flow. |
| ![](../Resources/Images/Diagram/Diagram_7_29x26.png) | **Entity Context Viewer**. View the entities (and their fields) used throughout the flow. You can also copy entity labels and add or delete entity fields as best suits your needs. For more information, see [Using Entity Context Viewer](Viewing%20and%20Managing%20Entities%20in%20a%20Flow.md). |
| ![](../Resources/Images/Diagram/Diagram_8.png) | **Debugging Tool**. View Conversation History on a flow and flow step level and debug any issues that occurred during the flow / flow step execution (if any). |
| ![](../Resources/Images/Diagram/Diagram_9.png) | **Analytics**. View flow and flow step analytics. |
| ![](../Resources/Images/Diagram/search%20action.png) | **Search**. Search elements within the Flow Diagram. |

In the Flow Diagram Designer, all steps are connected by strong links (![](../Resources/Images/Flow%20Graphical%20Designer/Bot%20Diagram_20.png)). The flow steps that are last steps (have the **Is last step?** selected) are marked with **END**.

On the connector (arrow), a gray dot displays. If you place the mouse over the icon, two options are available:

- Add condition ![](../Resources/Images/Flow%20Graphical%20Designer/Flows%20Diagram_2_29x27.png) - Allows you to set the next step to be executed only if a specific condition is met, following the logic the AI Agent uses to process user input. For more information on the logic the AI Agent uses to process user input, see [Conversation Lifecycle](Conversation%20Lifecycle.md).
- Add flow step ![](../Resources/Images/Flow%20Graphical%20Designer/Flows%20Diagram_3.png) - Allows you to add a parent step to the child step or access the Flow Palette (![](../Resources/Images/Diagram/flow%20palette.png)). If you add a parent step, the flow diagram layout is automatically resized to accommodate the new tree-like structure.

![](../Resources/Images/Flow%20Graphical%20Designer/Flows%20Diagram_4.png)
