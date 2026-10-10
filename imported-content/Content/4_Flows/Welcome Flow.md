---
layout:
  title:
    visible: false
---

<a id="WelcomeFlow"></a>

# Welcome Flow

The Welcome flow is the first flow DRUID executes for each new conversation. It provides the first response the AI Agent sends to the user who starts the chat.

To configure a Welcome flow, create a flow with a step of type Message and provide the initial message.

To set a Welcome flow on the AI Agent, go to AI Agent Details page, click the **Dialogue management** section and from the **Welcome** field, select your flow.

![](../Resources/Images/Bots/welcome%20flow.png)

To prevent the AI Agent app from triggering the Welcome flow (E.g., the user expands a new chat window for the same conversationId), set a **Trigger interval** in minutes. This value is valid at ConversationId level. The maximum value is 1440 minutes, whereas the default is 0 minutes, which means that the Welcome flow is always triggered by default.

When the AI Agent app triggers the Welcome flow, DRUID verifies the time stamp (value stored in **[[ChatUser]].LastWelcomeMessageAt**) when the AI Agent automatically triggered the Welcome flow and executes the flow again only after the Trigger interval threshold is reached.

A conversation with a AI Agent can be in one of the following statuses:

- **Idle** - The conversation is not linked with a particular flow.
- **Flow** - A returning user enters the conversation web page, the AI Agent automatically starts the **Welcome flow**.

## Related Topics

- [Configuring AI Agent Advanced Settings](../2_AI%20Agents/Configuring%20AI%20Agent%20Advanced%20Settings.md)
- [Conversation Lifecycle](Conversation%20Lifecycle.md)
- [Special Flows](Special%20Flows.md)
