---
title: Running Unattended Process using Orchestrator Queues
---


Triggering unattended robots will execute tasks and interact with applications independent of human interaction. They typically perform batch operations that do not require user intervention. For example, a batch of new client information is received in a spreadsheet and needs to be entered into multiple applications.

Unattended robots run in virtual environments and can automate any number of processes. The UiPath Orchestrator is responsible for remote execution, monitoring, scheduling and providing support for work queues.

You can integrate with the UiPath Orchestrator to trigger unattended robots (processes) from the AI Agent. The integration is asynchronous.

## How triggering an unattended process works

![](<../../../.gitbook/assets/trigger unattended process diagram_2.png>)

1. The AI Agent chats with the human and collects all the required information (Request Entity).
2. The AI Agent triggers the process. It sends the request to the robot passing the queue items to the UiPath queue.
3. The conversation with the human continues while the process is queued and executed in the back-office.
4. The robot will trigger the Callback flow and notify the AI Agent when the process completes.
5. The AI Agent will use the data stored in the Response Entity to respond to the user.

## How to trigger an unattended process from the AI Agents

To trigger an unattended process, follow these steps:

### Step 1: Create two flows.

Create two flows as follows: the **request flow** which will be triggered when chatting with the user and the **Callback flow** which will be triggered by the UiPath robot on process completion. At this point create the flows without defining the dialogs. For information on how to create a flow, see Creating a Flow.

{% hint style="info" %}
**Info:** Write down the ID of the Callback flow, you will need to provide it at Step 2 and Step 6.
{% endhint %}

### Step 2: Create the required entities.

Create the Request and Response entities. Define the AI Agent informational model by adding the business custom fields for both entities.

{% hint style="warning" %}
**IMPORTANT!** For the Callback flow to be triggered, make sure to add a field named **FlowId** to the Response Entity. This field will store the ID of the Callback flow.
{% endhint %}

For information on how to create entities, see [Creating Entities](https://druidai.gitbook.io/druid-ai-docs/build-ai-agents/authoring-tools/ai-agent-informational-model/managing-entities).

### Step 3: Create the UiPath connector.

Create the UiPath connection string. For information on how to do that, see [Creating the UiPath Connection Strings](<Creating the UiPath Connection Strings.md>).

### Step 4: Configure the flows.

Configure the request flow, defining the dialog. Make sure to add an Action step where you call the UiPath connector.

Configure the Callback flow. Make sure that you add an [Action step](https://druidai.gitbook.io/druid-ai-docs/build-ai-agents/authoring-tools/flows/conversational-flows/flow-steps/action-steps-configuration) where you call the UiPath connector and in the Set Variables section you set the **FlowId** field of the Response Entity to the ID of the Callback flow created at Step 1.

For information on how to configure flows, see [Configuring Flow Steps](https://druidai.gitbook.io/druid-ai-docs/build-ai-agents/authoring-tools/flows/conversational-flows/flow-steps/common-flow-settings).

### Step 5: Submit items to the UiPath queue.

Create a new queue item in a UiPath Orchestrator Queue with data mapped from DRUID Entities. For information on how to do that, see [Adding Item to UiPath Queue](<Adding Item to UiPath Queue.md>).

### Step 6: Use the integration data.

Once an item is placed in a UiPath Orchestrator Queue and its status is “New”, it is ready to be used by the UiPath process.

For information on how to use the AI Agent data in an UiPath process, see [Using UiPath Integration Data](<Using UiPath Integration Data.md>).

### Step 7: Trigger the Callback flow.

Handle the process completion by triggering the Callback flow. For information on how to do that, see [Triggering the Callback Flow](<Triggering the Callback Flow.md>).
