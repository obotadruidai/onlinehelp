---
title: "AudioCodes"
---


The Voice channel through VoiceAI Connect from AudioCodes enables you to deliver a seamless voice experience to the users talking to your DruidAI Agents.

VoiceAI Connect acts like a hub connecting different telephony systems (telephony channel, public telephony provider, contact center, enterprise communication platform, or any platform communicating via WebRTC) to the Druid bot framework and voice AI cognitive services.

{% hint style="info" %}
**Info:** Through AudioCodes, you can integrate DRUID with various telephony systems like: Genesys, Avaya, Cisco. For information on the list of available contact center solutions you can integrate DRUID with, see [SBC Interoperability List](https://www.audiocodes.com/partners/sbc-interoperability-list).
{% endhint %}

![](<../../../.gitbook/assets/Voice Audio Codes Channel.png>)

In a typical AI Agent deployment, VoiceAI Connect receives a phone call and connects it to your AI Agent.

## Prerequisites

* For Druid on premise deployments, make sure that you provide inbound access from the following messaging endpoint: DRUID.BotApp.

## Activate the Voice AudioCodes Channel

To activate the channel, follow these steps:

1. In the Druid Portal, go to AI Agent settings, and then click the **Channels** tab.
2. Click the **AudioCodes** card.

![](<../../../.gitbook/assets/channel card.png>)

The channel configuration modal appears.

![](<../../../.gitbook/assets/audiocodes modal.png>)

3. Generate the required security token. Click the **Generate** button to create the security token.
4. By default, the communication between DRUID and VoiceAi Connect is done via the WebSocket protocol. Clear the **Use web socket** checkbox only for special deployments where network restrictions may deny WebSocket communication.
5. In the **Reply timeout in seconds** field, enter the maximum time (in seconds) the AI Agent has to respond before the call is automatically disconnected. For more information, see [Handle Conversation Disconnect](<Voice Audio Codes Channel.md#_Handle_Conversation_Disconnect>).
6. In the **Language map** JSON field, provide a one-to-one mapping between the language codes used by the Speech-To-Text (STT) service provider (key on the left) and DRUID-specific language codes, that is, ISO 639-1(key on the right), providing the Text-to-speech voice DRUID will be using. For reference, consult the locales and voices supported for Text-to-speech provided by [Azure Cognitive Services](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support?tabs=tts).

Use the following format for the language codes mapping:

"\<STT Provider language code/locale>": "|"

For example:

```
{
  "ro-RO": "ro|ro-RO-AlinaNeural",
  "en-US": "en-US|en-US-AshleyNeural",
  "th-TH": "th-TH|th-TH-AcharaNeural"
}
```

{% hint style="info" %}
**NOTE:** To provide users with a flawless conversation and avoid interrupting the conversation due to language change as Druid takes for granted the language identified by the STT language detection, map all AI Agent languages: AI Agent default language, AI Agent additional languages (if any) and the languages used on the AI Agent at Conversation Time translation. For situations when you want to trigger the Language changed flow, you can activate Druid language detection on the AI Agent.
{% endhint %}

{% hint style="info" %}
**Info:** If the STT service provider has voice only en-UK and not for en-US, you can map “en-UK” to “en-US”.
{% endhint %}

7. Send the **token** and **DRUID URL** to your Druid representative and they will set up the connection between your AI Agent and VoiceAI Connect.

After the channel’s activation, the following fields are available in Druid:

* **\[\[ChatUser]].ChannelId** = “audiocodes”. It identifies the channel.
* **\[\[ChatUser]].Phone** – Stores the Calling Party phone number. (The initiator of the call).
* **\[\[ChatUser]].CalleePhoneNumber** – Stores the Called Party phone number. (The destination of the call).

Because the AI Agent can both receive and initiate calls, the values in thelast two fields shift depending on the direction:

Inbound Call (User calls AI Agent):

* **\[\[ChatUser]].Phone** stores the user phone number.
* **\[\[ChatUser]].CalleePhoneNumber** stores the AI Agent phone number.

Outbound Call (AI Agent calls User):

* **\[\[ChatUser]].Phone** stores the AI Agent phone number.
* **\[\[ChatUser]].CalleePhoneNumber** stores the user phone number.

## Handle Conversation Disconnect <a href="#handle_conversation_disconnect" id="handle_conversation_disconnect"></a>

A call disconnects if the AI Agent does not respond within the **Reply timeout in seconds** threshold set on the channel or if the user says nothing for 120 seconds.

You can configure what happens on conversation disconnect. Go to the AI Agent details, click the **Dialogue management** section header and from the **Voice call terminate flow** field, select the flow to be triggered on disconnect. If no such flow is set, the call disconnects.

When the call disconnects, the following data is logged in the conversation context:

* **\[\[ChatUser]].VoiceConversationTerminatedReason** - The reason for which the call is disconnected. E.g., “Client Side”. The reason of the disconnect can be one of the following:
* **SocketInterrupted** – The connection was interrupted.
* **UserBecameSilent** – The user said nothing for 120 seconds.
* **CallTerminatedByCaller** – The user terminated the call.
* **Error** – An error occurred on AudioCodes side.
* **\[\[ChatUser]].VoiceConversationTerminatedReasonCode** – The code (text) associated to the disconnect reason. E.g., “client-disconnected”.

## Handle AudioCodes Exceptions <a href="#handle" id="handle"></a>

{% hint style="info" %}
**Info:** This feature is available starting with Druid 9.30.
{% endhint %}

AudioCodes-specific errors are treated as exceptions within Druid. This allows flow authors to capture end-to-end errors directly during voice conversations, perform error recovery (such as changing the TTS provider for the current conversation), or send notifications to bot administrators.

To handle these exceptions:

1. Navigate to AI Agent details > **Dialogue management**.
2. Click to view the **Voice Call Terminate** flow.
3. Add a conditional branch with the following expression: **\[\[ChatUser]].VoiceConversationTerminatedReason == "error"**
4. Configure the desired exception handling steps (e.g., alert notifications or fallback TTS provider logic) inside this branch.

## Conversation History

All voice conversations begin with “\[Voice start event]”. This is particularly useful for debugging purposes to measure the time from the moment when the call was initiated (AI Agent picks up the call) until the AI Agent says the first message.

For this channel, Druid also logs in the Conversation History the **Speech-to-Text Confidence Score**, that is, the value representing the confidence level of the recognition received from the speech-to-text provider.

![](<../../../.gitbook/assets/Voice Audio Codes Channel_8.png>)

When the call disconnects due to an error, the disconnect reason logged in the Conversation History is “PlatformIntegrationError” (the message status is Platform Integration error).
