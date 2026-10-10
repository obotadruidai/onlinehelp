---
title: "Troubleshooting Steps with Debug Messages"
---

<a id="TroubleshootingStepswithDebugMessages"></a>


When specific flow steps are not executed as expected or a conversation follows an unexpected path, you can use debug messages to gain valuable insights into the execution process. They help trace the conversation’s progression step by step.

By leveraging debug messages, you can efficiently troubleshoot and optimize flow steps while maintaining the conversation quality in production environments.

> **NOTE:** For hybrid Druid deployments, this feature requires you to upgrade your DRUID Connector Host to version 8.11 or later.

<a id="BenefitsofDebugMessages"></a>

## Benefits of Debug Messages

- **Enhanced debugging** – Gain visibility into conversation flow transitions.
- **Context awareness** – Understand the state and context at each step.
- **Non-intrusive** – Debug messages do not impact end-user conversations and are only visible in the Conversation Trace tool.
- **Production-safe** – Add debug messages in a live environment without affecting conversation quality.

<a id="HowtoUseDebugMessages"></a>

## How to Use Debug Messages

1. Identify the flow step where the conversation is not behaving as expected.
2. Add a debug message to that flow step. You can also include additional context in the message to capture relevant details.

![](../Resources/Images/druid%208.11/add%20debug%20message.png)

3. Monitor the Conversation Trace tool to view the debug messages and track how the conversation evolves.
4. Analyze the collected debug messages to identify issues and make necessary adjustments to the flow.

![](../Resources/Images/druid%208.11/debug%20message.png)

<a id="ImportantNotes"></a>

## Important Notes

- Debug messages are never visible to the end user.
- They are only logged in the Conversation History Trace tool for debugging purposes.
- You can safely add debug messages in production without disrupting the user experience.

## Related Topics

- [Conversation Trace](../Data%20Analytics%20%26%20Insights/History%20%26%20Logs/Conversation%20History%20V2/Conversation%20Trace.md)
