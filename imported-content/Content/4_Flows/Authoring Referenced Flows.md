<a id="AuthoringReferencedFlows"></a>

# Authoring Referenced Flows

In the Druid AI Platform, a flow can reference (link) other flows, allowing you to build modular, reusable conversation structures. Referenced flows appear as expandable groups inside the Flow Diagram, so you can author them inline without navigating away from the current flow.

The reference flow functionality applies in the following use cases:

- Creating menus automatically transforms the menu options in virtual nodes. For each of the virtual nodes, DRUID tries to find a flow utterance that contains the button’s value. If the AI Agent finds such a flow it links this flow to the virtual node and DRUID groups it under the virtual node.
- Use trigger flow steps.

The Flow Diagram shows referenced flows as groups and you can expand inline the referenced flows and author them.

<a id="Creatingmenusandauthoringreferencedflows"></a>

## Creating menus and authoring referenced flows

To create a menu, create a step of type Hero, leave Input mapping empty and mark the step as being the last step (check Is last step). In the Metadata section of the step, add hero card options and save.

DRUID transforms the hero card options in virtual nodes (virtual steps).

![](../Resources/Images/Authoring%20Referenced%20Subflows/Authoring%20Referenced%20Flows.png)

For every button in the menu, the AI Agent takes the button value and tries to find flows that contain in the training phrases the button’s value.

If the AI Agent finds any flow, it will group the referenced flow under the virtual node. DRUID provides you with extensive options for managing a referenced flow. To view a flow grouped under a virtual node, click the expand icon on the virtual node.

![](../Resources/Images/Authoring%20Referenced%20Subflows/Authoring%20Referenced%20Flows_1.png)

The referenced flow and its steps display within the virtual node.

![](../Resources/Images/Authoring%20Referenced%20Subflows/Authoring%20Referenced%20Flows_2.png)

<a id="Choosereferenceflows"></a>

### Choose reference flows

If the AI Agent finds no referenced flow for a virtual node, you can create one by clicking **Choose reference subflow**.

![](../Resources/Images/Authoring%20Referenced%20Subflows/Authoring%20Referenced%20Flows_3.png)

The Create New Flow page appears, which allows you to create a new flow for the selected virtual node directly in the virtual node without navigating away from the menu. The page would have all the fields filled in with information from the current virtual node.

<a id="CreatingTriggerFlowsteps"></a>

## Creating Trigger Flow steps

The Trigger Flow step enables a AI Agent to redirect the conversational flow to another existing flow.

When you create a trigger flow step, the referenced flow (selected on the step in the Metadata section) is expanded within a group inside the trigger flow step. To view the referenced flow click the expand icon on the virtual node.

![](../Resources/Images/Authoring%20Referenced%20Subflows/Authoring%20Referenced%20Flows_4.png)

<a id="Authoringflowsinsidegroups"></a>

## Authoring flows inside groups

You can edit the referenced flows directly inside the virtual nodes or trigger flow steps as you would do with any other flow using the Flow Diagram options.

If you want to author a complex flow you can choose to open it in a new browser window by clicking the icon ![](../Resources/Images/Authoring%20Referenced%20Subflows/Authoring%20Referenced%20Flows_5.png).

## Related Topics

- [Flows](Flows.md)
- [Redirect to Another Step](Redirect%20to%20Another%20Step.md)
