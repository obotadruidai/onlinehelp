---
layout:
  title:
    visible: false
---

<a id="InactivityEndConversationFlow"></a>

# Inactivity End Conversation Flow

The **Inactivity End Conversation Flow** helps manage conversations that are idle for a set period. You can define this timeout in the **Conversation timeout (min)** field, with a range of 0 to 1440 minutes. When the timeout period elapses, the selected **Inactivity End Conversation Flow** is triggered.

![](../Resources/Images/druid%207.13/inactivity%20end%20flow.png)

> **NOTE:**  If the user is in a live chat session, the system will disconnect them.

<a id="UseCases"></a>

## Use Cases

You can use this special flow to:

- Expire conversations for client-facing AI Agents on Direct Line by calling the internal action **ChangeConversation**. This action ends the old conversation, making it inaccessible.
- Request user feedback after a defined idle time.
