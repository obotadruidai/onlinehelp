---
title: Trigger Flow
---


The Trigger Flow step allows a AI Agent to seamlessly redirect the conversation to another existing flow, making it a powerful tool for creating dynamic and interactive dialogues.

To add and configure a Trigger Flow step, follow these steps:

1. Open the desired flow in Flow Diagram view.
2. Expand the Flow Palette, then drag the **Trigger Flow** step from the Dialog category into the main flow window and drop it onto the step you want to link it to.
3. Select the step on the diagram, then click the **Settings** icon from the Actions menu.
4. Set the General parameters:

* **Name**: Enter a suggestive name that clearly indicates the purpose of this step. For example, "Go to Hero Card Flow" if the step triggers the Hero Card Flow.
* **Step Message**: If needed, you can enter a message that the AI Agent will display when this step is reached. However, for Trigger Flow steps, it’s common to leave this field empty, depending on the desired behavior.

5. Click on the Metadata section header and from the Subflow field, select the flow you want to trigger.

{% hint style="info" %}
**NOTE:** You can use 'Trigger flow' steps within parent flows to programmatically initiate child intents.

<img src="../../.gitbook/assets/trigger flow.png" alt="" data-size="original">
{% endhint %}

6. Click the Save button to save the flow step configuration.

## Triggering back to the previous flow

If you need to return to the previous flow after the Trigger Flow step is executed, use one of the following methods:

* Using \[\[ConversationInfo]].PreviousFlow.FlowId. Simply provide **\[\[ConversationInfo]].PreviousFlow.FlowId** in the **Input Mapping** to automatically trigger a return to the previous flow once the current step completes. This method is recommended. The completion of the current step execution triggers the previous flow.

![](<../../.gitbook/assets/PREVIOUS FLOW.png>)

* Input Mapping with Flow ID. You can manually input the ID of the previous flow or use a local variable that stores this ID.

{% hint style="warning" %}
**IMPORTANT!** We DO NOT this method because the flow IDs might change during solution imports, which could cause errors in your conversational flows.
{% endhint %}

By following these steps, you can effectively use the Trigger Flow step to optimize and streamline your AI Agent's conversational flows, creating a smoother and more engaging user experience.
