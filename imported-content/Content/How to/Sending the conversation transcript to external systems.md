---
layout:
  title:
    visible: false
---

<a id="SendingtheConversationTranscripttoExternalSystems"></a>

# Sending the Conversation Transcript to External Systems

> **IMPORTANT!** The Conversation Transcript is now saved in [[ConversationInfo]].TranscriptTxt instead of [[ChatUser]].TranscriptTxt due to technical reasons. If you have a hybrid or on premise Druid deployment, install Druid Connector Host version 7.4 or above.

If you want to enable your agents to send conversation transcript to external systems through Druid connectors (email, CRM, etc.), follow these steps:

<a id="Step1Gettheconversationtranscriptwithintheconversationcontext"></a>

## Step 1. Get the conversation transcript within the conversation context

authors can bring the conversation transcript into the conversation context (in a DRUID entity). On the desired flow step, call the internal action **GetConversationTranscript**.

![](../Resources/Images/druid%207.4/get%20conv%20transcript.png)

If no parameter is set, the conversation from the current ActivityId will be saved.

> **NOTE:**  A chat activity represents a conversation session. A new chat activity is initiated (with a new ActivityId) whenever a user sends a message in chat after more than 1 hour from the last message in that chat, signaling the start of a new chat session. Additionally, a new chat activity is automatically initiated after the previous one is ended by the AI Agent author through the **EndChatActivity** internal action.

For Live Chat scenarios, when using the internal action without specified parameters, the conversation transcript will include the conversation of the user from the point where the chat activity began up to the moment when the action is invoked.

For details on parameters to filter the conversation transcript, see [Internal Actions](../4_Flows/Internal%20Actions.md).

<a id="Step2SetConversationInfoTranscriptTxtConversationInfoTranscriptJSONtoyourbusinessrequestentity"></a>

## Step 2. Set [[ConversationInfo]].TranscriptTxt/[[ConversationInfo]].TranscriptJSON to your business request entity

> **NOTE:** For DRUID versions prior to 7.4, there is no need to perform this step, as [[ChatUser]] is readily accessible in integrations. You can directly use[[ChatUser]].TranscriptTxt on the desired integration to send the conversation transcript to external systems.

Since [[ConversationInfo]] is inaccessible in integrations, you must save the conversation transcript in your request entity before the integration. Otherwise, you won't be able to map it in the integration.

Use the "Set variable" section on the flow step to set [[ConversationInfo]].TranscriptTxt or [[ConversationInfo]].TranscriptJSON to your business request entity.

![](../Resources/Images/druid%207.4/set%20variable.png)

<a id="Step3Usethetranscriptfileinintegrations"></a>

## Step 3. Use the transcript file in integrations

To send the conversation transcript to external systems, on the flow step, add the desired integration. In the mapping table, map the transcript to the business request entity set in the Set Variables section.

![](../Resources/Images/druid%207.4/map%20transcript.png)

> **NOTE:** For DRUID versions prior to 7.4, use **[[ChatUser]].TranscriptTxt** to send the conversation transcript to external systems.
