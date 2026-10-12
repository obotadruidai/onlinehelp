---
title: Troubleshooting Steps with Debug Messages
---


When specific flow steps are not executed as expected or a conversation follows an unexpected path, you can use debug messages to gain valuable insights into the execution process. They help trace the conversation’s progression step by step.

By leveraging debug messages, you can efficiently troubleshoot and optimize flow steps while maintaining the conversation quality in production environments.

{% hint style="info" %}
**NOTE:** For hybrid Druid deployments, this feature requires you to upgrade your DRUID Connector Host to version 8.11 or later.
{% endhint %}

## Benefits of Debug Messages

* **Enhanced debugging** – Gain visibility into conversation flow transitions.
* **Context awareness** – Understand the state and context at each step.
* **Non-intrusive** – Debug messages do not impact end-user conversations and are only visible in the Conversation Trace tool.
* **Production-safe** – Add debug messages in a live environment without affecting conversation quality.

## How to Use Debug Messages

1. Identify the flow step where the conversation is not behaving as expected.
2. Add a debug message to that flow step. You can also include additional context in the message to capture relevant details.

![](<../../.gitbook/assets/add debug message.png>)

3. Monitor the Conversation Trace tool to view the debug messages and track how the conversation evolves.
4. Analyze the collected debug messages to identify issues and make necessary adjustments to the flow.

![](<../../.gitbook/assets/debug message.png>)

## Important Notes

* Debug messages are never visible to the end user.
* They are only logged in the Conversation History Trace tool for debugging purposes.
* You can safely add debug messages in production without disrupting the user experience.

## Related Topics

* [Conversation Trace](https://druidai.gitbook.io/druid-ai-docs/ai-platform/ai-governance-and-security/observability-and-explainability/conversation-trace)
