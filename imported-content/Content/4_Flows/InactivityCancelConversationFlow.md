---
title: "Inactivity Cancel Conversation Flow"
---

<a id="InactivityCancelConversationFlow"></a>


The **Inactivity Cancel Conversation Flow** allows you to customize the actions taken when a conversation is automatically canceled due to user inactivity.

To set it up, go to the AI Agent Details page, click on Dialogue Management, then select the desired **Inactivity Cancel Conversation Flow**. Then configure the **Flow Timeout (min)**, which defines the inactivity timeout period (between 0 and 15 minutes). Once the timeout is reached, the conversation will be canceled, and the selected flow will be triggered.

![](../Resources/Images/Alerts/inactivity%20cancel%20timeout.png)

> **NOTE:**  For DRUID version prior to 8.7, flow inactivity timeout is by default set to 15 mins for hybrid and full cloud installations, but is customizable for on-prem installations only (at application level, so the setting applies to all tenants and AI Agents).

<a id="Usecases"></a>

## Use cases

This special flow enables you to execute multiple actions when a conversation reaches out the 15 mins of inactivity threshold:

- Execute connector actions to save somewhere the fact that the conversation was canceled.
- Send a message or email to the chat user.
- Open a new conversation and ask the user to confirm the conversation cancel.
- Clear the conversation transcript from the chat widget (using ChangeConversation internal action and back channel step).
- Any other custom automations.

Whenever the AI Agent triggers the special flow **InactivityCancelConversationFlow**, DRUID stores specific details in system entity **[[InactivityDetails]]**. For more information, see [System Entities](../5_Entities/System%20Entities.md).

If no flow is selected for this special flow, the AI Agent will respond with the special message set for **InactivityCancelConversation**.

If the **InactivityCancelConversation** threshold is reached while the **InactivityCancelConversationFlow** is executed, then the AI Agent displays the special message **InactivityCancelConversation** and drops the conversation.

After the user is disconnected the [[ChatUser]].ConversationStatus is “Idle”.
