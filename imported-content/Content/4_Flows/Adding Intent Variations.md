---
title: "Adding Intent Variations"
---

<a id="AddingIntentVariations"></a>


**Intent variations** also referred to as child intents or child flows, enhance the AI Agent context awareness by offering additional functionality within the conversation. They are secondary flows triggered by intent matching while the user is engaged in a primary (parent) flow or immediately after the completion of a parent flow. Use child intents to address slight variations on the same topic without disrupting the flow of conversation.

<a id="HowDruidHandlesChildIntents"></a>

## How Druid Handles Child Intents

![](../Resources/Images/Child%20intents/Child%20Intents.png)

When an intent change occurs within a parent flow, AFTER the flow step training phrases validation, the flow engine attempts to match the new intent with the training phrases of configured child flows.

- If a match is found, the conversation seamlessly transitions to the identified child flow. After completing the child flow, the conversation continues based on the last step configuration of the child intent. For more information, see [Create Child Intents](#_Create_Child_Flows).
- If no match is found with any child flow's training phrases, the flow engine resorts to data validation and, if necessary, parent flow matching.

If a new intent arises immediately after the conclusion of a parent flow:

- The flow engine first attempts to match the intent with the child training models of the preceding parent flow.
- If no match is found, it further predicts against the AI Agent general model.

If another intent change occurs within a child flow

- The flow engine first attempts to match the intent with other child intents and then with other parent flows.
- Upon completion of the child flow(s), the conversation returns to the last input mapping step of the parent flow from which the child intent was triggered.

<a id="CharacteristicsofChildIntents"></a>

## Characteristics of Child Intents

- Child intents are flows related to a parent flow.
- Each child intent can only be associated with one parent flow.
- They are triggered while the conversation is inside a parent flow or immediately after its completion.
- Child intents inherit the roles of the parent flow.
- Two parent flows can have identical child intents (with identical utterances), but there is no relation between the child intents.
- Child intent share the SAME conversation context with all the other intents (parent or child); there is no concept of “child context”.
- Training phrases of child intents follow the same NER configuration parameters as parent flows.
- Child intent utterances contribute to the NLP sub-model of the parent flow.

<a id="CreateChildFlows"></a>

## <a id="_Create_Child_Flows"></a>Create Child Flows

Creating child intents is similar to creating flows; the only difference is that the conversation within a child intent should be minimal to address a simple task inside the main conversation context (in the context of the parent flow).

> **NOTE:**  You can create child intents only from the Flow Diagram.

To create a child intent:

1. Navigate to the desired parent flow in diagram view.
2. On the toolbar, click the **Add child flow** icon (![](../Resources/Images/Child%20intents/Child%20Intents_1_32x33.png)).  A new child intent appears inside the parent flow.

By default, the child intent name follows this naming convention: Child <number> [Parent] <the name of the parent flow>. To change the name of the child intent, click on the child flow and on the **Actions** menu, click **Info**, click the General section header and change the name.

3. Click on the child flow, on the Actions menu click **Info** and in the right-side Editor define the training phrases for NLU.

![](../Resources/Images/Child%20intents/Child%20Intents_3.png)

> **Info:** You can test the training phrases from authoring time by entering a phrase in the NLP child model section, clicking the **Test** button and selecting the language.
>
> ![Image](../Resources/Images/Child%20intents/Child%20Intents_4.png)
>
> The NLP child model section is also available on the parent flow step and you can test child intent(s) of the parent flow.

4. In the child intent node, click the drop-down arrow to expand it.
5. Define the child intent dialog following the procedure for defining dialogs. For more information, see [Defining the Dialog](Defining%20the%20Dialog.md).
> **NOTE:** The conversation within a child intent should be minimal; therefore, design the child intent to respond to a single task.

![](../Resources/Images/Child%20intents/Child%20Intents_5.png)

6. Optionally, you can decide what you want to happen after the child intent execution ends by evaluating the value of **[[Intent]].Caller** system entity field; when triggered from inside a parent flow, the conversation will ALWAYS return to the input requesting step of the parent flow, where child intent was triggered. When triggered immediately after the parent flow completed, the child intent does NOT automatically return to the parent flow; a dedicated configuration must be set up for this.

- When child flow is triggered from INSIDE the parent flow, **[[Intent]].Caller == “inflow”**
- When child flow is triggered AFTER the parent flow completed, **[[Intent]].Caller == “idle”**. In this case, a Trigger Flow step can be added at the end of the child flow, to redirect the conversation back to the beginning of the parent flow, or to any other parent flow (if needed).

The child intents are added to the Flows list under the Child intents category. In Flow diagram, you can see their parent flow.

![](../Resources/Images/Child%20intents/Child%20Intents_6.png)

The Flows list enables you to easily spot the parent and child flows, as follows:

- The flows which are parent flows have the “child” icon, together with the counter of child flows it contains (how many flows have that flow set as parent flow).
- Child flows will have a badge containing the text “Child flow: <parent flow name>”, where the parent flow name is a hyperlink to the parent flow.

![](../Resources/Images/Flows/child%20intents%20and%20parents.png)

> **Info:** On the parent flow, you can disable intent switch on steps prior to the one that will trigger child intents, to keep the user in the dialog without switching the intent.

<a id="ExampleBookingareservation"></a>

## Example: Booking a reservation

The user wants to make a holiday reservation and when the AI Agent asks to confirm the reservation, the user changes the destination or the period.

![](../Resources/Images/Child%20intents/Child%20Intents_8.png)

<a id="Changetheparentflowofachild"></a>

## Change the parent flow of a child

To move a child intent to another parent flow, go to the child intent details (General tab) and from the **Parent flow** field, select the new parent flow where you want to move the child intent.

Save the child intent.

<a id="Createidenticalchildintentsacrossparentflows"></a>

## Create identical child intents across parent flows

In complex conversational designs, you may require the same intent variation to be accessible across multiple parent flows. Instead of manually recreating the logic for each instance, the Druid AI Platform allows you to implement identical child intents that provide consistent context handling regardless of the current conversation path.

This approach ensures that common user requests—such as "Cancel," "Help," or "Go back"—behave predictably across different functional areas of the AI agent. By streamlining child intent management, you maintain a unified user experience and reduce the administrative overhead associated with flow designer updates.

Repeat the procedure below as many times as parent flows you want to have an identical child intent.

1. Go to the Flow list (list view), search for the desired child intent and click the **Clone** icon displayed in line with the flow.
   The child intent clone displays on the steps tab (in list view).
2. Click the **Details** tab, click the General section header, change the child intent name and from the **Parent flow** field, select the flow you want to be parent flow for the current child intent.
3. Save the child intent.

<a id="Transformflowsintochildintents"></a>

## Transform flows into child intents

authors who have existing flows that better fit into the child intents functionality (e.g., small talk that occurs inside a flow), can transform them into child intents.

> **IMPORTANT!**  Child intents provide additional context awareness (inside a parent flow). We do not recommend you to transform a large, complex parent flow into a child intent as this would introduce complexity and might break the dialog design.

All existing and newly created flows automatically have the **Parent flow** field set to none.

To transform a flow into a child intent, from the **Parent flow** field, select the desired parent flow and save the changes. The current flow becomes child intent for the selected parent flow.

> **IMPORTANT!** Any modification on the child flow’s utterance(s), or any transformation of a child flow into a parent flow, or viceversa, requires the AI Agent to be re-trained! The train action creates both AI Agent model and child model(s).

By leveraging child intents effectively, authors can enhance conversational dynamics and streamline flow management across various dialog scenarios.
