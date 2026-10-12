---
title: Sending the Conversation Transcript to External Systems
---


{% hint style="warning" %}
**IMPORTANT!** The Conversation Transcript is now saved in \[\[ConversationInfo]].TranscriptTxt instead of \[\[ChatUser]].TranscriptTxt due to technical reasons. If you have a hybrid or on premise Druid deployment, install Druid Connector Host version 7.4 or above.
{% endhint %}

If you want to enable your agents to send conversation transcript to external systems through Druid connectors (email, CRM, etc.), follow these steps:

## Step 1. Get the conversation transcript within the conversation context

authors can bring the conversation transcript into the conversation context (in a DRUID entity). On the desired flow step, call the internal action **GetConversationTranscript**.

![](<../../.gitbook/assets/get conv transcript.png>)

If no parameter is set, the conversation from the current ActivityId will be saved.

{% hint style="info" %}
**NOTE:** A chat activity represents a conversation session. A new chat activity is initiated (with a new ActivityId) whenever a user sends a message in chat after more than 1 hour from the last message in that chat, signaling the start of a new chat session. Additionally, a new chat activity is automatically initiated after the previous one is ended by the AI Agent author through the **EndChatActivity** internal action.
{% endhint %}

For Live Chat scenarios, when using the internal action without specified parameters, the conversation transcript will include the conversation of the user from the point where the chat activity began up to the moment when the action is invoked.

For details on parameters to filter the conversation transcript, see [Internal Actions](https://druidai.gitbook.io/druid-ai-docs/build-ai-agents/authoring-tools/flows/conversational-flows/internal-actions).

## Step 2. Set \[\[ConversationInfo]].TranscriptTxt/\[\[ConversationInfo]].TranscriptJSON to your business request entity

{% hint style="info" %}
**NOTE:** For DRUID versions prior to 7.4, there is no need to perform this step, as \[\[ChatUser]] is readily accessible in integrations. You can directly use\[\[ChatUser]].TranscriptTxt on the desired integration to send the conversation transcript to external systems.
{% endhint %}

Since \[\[ConversationInfo]] is inaccessible in integrations, you must save the conversation transcript in your request entity before the integration. Otherwise, you won't be able to map it in the integration.

Use the "Set variable" section on the flow step to set \[\[ConversationInfo]].TranscriptTxt or \[\[ConversationInfo]].TranscriptJSON to your business request entity.

![](<../../.gitbook/assets/set variable (2).png>)

## Step 3. Use the transcript file in integrations

To send the conversation transcript to external systems, on the flow step, add the desired integration. In the mapping table, map the transcript to the business request entity set in the Set Variables section.

![](<../../.gitbook/assets/map transcript.png>)

{% hint style="info" %}
**NOTE:** For DRUID versions prior to 7.4, use **\[\[ChatUser]].TranscriptTxt** to send the conversation transcript to external systems.
{% endhint %}
