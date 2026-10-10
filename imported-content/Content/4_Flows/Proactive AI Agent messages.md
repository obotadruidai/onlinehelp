---
layout:
  title:
    visible: false
---

<a id="ProactiveAIAgentMessages"></a>

# Proactive AI Agent Messages

Proactive AI Agent Messages for Long-Running Integrations allows you to keep users informed and engaged when a flow step involving an integration takes longer than expected to complete. By configuring proactive AI Agent messages at the flow step level, you can automatically send updates to the user at defined intervals. This helps manage expectations and prevents potential timeouts, especially in voice channels.

> **NOTE:** This feature is available in DRUID 8.15 and higher.

<a id="Howproactivemessageswork"></a>

## How proactive messages work

When a flow step with an integration begins execution, a timer is initiated based on the Trigger time (seconds) you configure.

- **Single message**: If you set only one proactive message, it will be sent to the user when the trigger interval elapses. For example, if the trigger time is set to 3 seconds and the integration takes 10 seconds to complete, the message will be sent a single time — 3 seconds after the step starts executing.
- **Multiple messages**: If you configure multiple proactive messages, each message will be sent only once at its designated time. For instance, if you set a **Trigger time (seconds)** of 2 for the first message and 5 for the second, the first message will be sent after 2 seconds, and the second message will be sent after 5 seconds.

![](../Resources/Images/DRUID%208.15/proactive%20messages.png)

This functionality is available for both pre-actions and post-actions within a flow step.

<a id="AddingaProactiveAIAgentMessage"></a>

## Adding a Proactive AI Agent Message

To configure proactive messages for a flow step that contains an integration which may take some time to execute, follow these steps:

1. Navigate to the specific flow step you want to configure.
2. Click on the **Proactive AI Agent messages** section header.
3. Click the **Add new** button within this section.
4. Set the **Trigger time (seconds**) after which you want a proactive message to be sent. For the first message, this is the time interval trigger. For subsequent messages (if configuring multiple), this represents the time from the start of the step when that specific message should be sent.
5. In the **Message** field, enter the message you want to send to the user. If your AI Agent is multilingual, provide localized messages for each supported language.
> **Info:** Repeat steps 4 and 5 to add multiple proactive messages if desired.

6. Click **Save** on the flow step to apply your proactive message configuration.

By implementing proactive AI Agent messages, you can significantly improve the user experience by providing timely updates during longer processing times.
