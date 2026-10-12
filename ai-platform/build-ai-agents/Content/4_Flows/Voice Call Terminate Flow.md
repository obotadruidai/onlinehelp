---
title: Voice Call Terminate Flow
---


The **Voice Call Terminate Flow** is triggered when a telephony voice call ends. You can use it to update call statuses in external systems, such as a CRM or ticketing platform, or to perform post-call automations (e.g., send follow-up messages, update records, log events).

## Configure the Voice Call Terminate Flow

You can choose which flow should be triggered when a voice conversation ends.

{% hint style="info" %}
**NOTE:** If a Voice Termination Flow is configured, Druid automatically logs the ActivityEnd event in \[\[ChatActivityData]] at the END of this flow. This ensures that any post-call processing runs under the same activity before the session officially closes. Do not manually trigger or send a duplicate call ending activity from within your custom **Voice Termination Flow**, as Druid handles this automatically to prevent duplicate records.
{% endhint %}

To configure the Voice Call Terminate Flow:

1. Go to your AI Agent details.
2. In the Dialogue Management section, locate the **Voice Call Terminate Flow** field.
3. Select the flow you want to trigger when the voice conversation disconnects.
4. Save the AI Agent.

## Trigger the flow in the assistant conversation

If Agent Assist is enabled and a **Voice Call Terminate Flow** is configured, the flow can be triggered in both the client-side and assistant-side conversations. When the **Trigger on assist conversation also** option is enabled, the flow runs twice:

* Once in the main conversation (with the user).
* Once in the assistant conversation (between the helpdesk agent and the assistant AI Agent).

{% hint style="warning" %}
**IMPORTANT!** To avoid running the same actions twice, update your flow with conditional logic before enabling the **Trigger on assist conversation also** option.
{% endhint %}

To prepare your **Voice Call Terminate** flow:

1. Add a branch condition that checks if `IsCommandChannel = true`.

![](<../../.gitbook/assets/vocie term condition.png>)

2. In this branch, define actions that should run only in the assistant conversation.

To enable the flow for the assistant conversation:

1. Go to your AI Agent details.
2. In the Dialogue Management section, locate the **Voice Call Terminate Flow** field.
3. Select the flow you want to trigger when the voice conversation disconnects.
4. Tap on **Trigger on assist conversation also**.

![](<../../.gitbook/assets/voice term.png>)

5. Save the AI Agent.

## Related Topics

* [Agent Assist](https://druidai.gitbook.io/druid-ai-docs/live-chat/agent-assist)
