---
title: "Authoring Flows and Voice Best Practices"
---

<a id="AuthoringFlowsandVoiceBestPractices"></a>


Druid provides authors with a simple way to configure flows for Voice channel by providing the Speak message in the Voice section on flow steps.

> **NOTE:** In the Voice channel, the **Speak message** has priority over the step message.

<a id="BestPractices"></a>

## Best Practices

To make the AI Agent voice sound more natural, follow these best practices:

- For multi-channel AI Agents do not customize voice messages per channel, instead check the steps message spelling and punctuation marks and correct the mistakes if any. Also properly use diacritics and accented characters.
- Provide short messages in the **Speak message** field on steps.
- Use properly the punctuation marks. This way you make it easier for the AI Agent to read using pauses and the pitch of the voice to make the message clear.
- For hero, thumbnail and choice steps, if you want the AI Agent to speak what’s in the cards, buttons, etc., provide the desired voice message in the **Speak message** field on these steps.

<a id="Transferringthecall"></a>

## Transferring the call

There are cases when the AI Agent cannot handle the call by itself, so it needs to escalate the call to a call center live agent. By default, once VoiceAI Connect performs the transfer, it immediately disconnects the call with the AI Agent, regardless of whether the transfer succeeded or not.

For the AI Agent to escalate the call to contact center live agent, add a backchannel step named **transfer**. You need to configure the backchannel step so that the AI Agent provides the **transferTarget** that is the URI to where the call should be transferred call to. Typically, the URI is a "tel" or "sip" URI. You can configure the backchannel step so that upon transfer the AI Agent provides additional SIP headers.

In **Input mapping** on the **transfer** backchannel flow step, provide the entity which stores the desired values. In the figure below, we created an example entity, [[VoiceParams]], which stores the values of the parameters associated with the transfer event.

![](../../Resources/Images/Voice%20Audio%20Codes%20Channel/transfer%20entity.png)

Make sure that the entity you provide in **Input mapping** contains fields named exactly as the parameters expected by VoiceAI Connect for the transfer event. For the complete list of transfer event parameters, see [VoiceAI Connect documentation](<https://techdocs.audiocodes.com/livehub/#LiveHub/byoc_Call Transfer.htm%23Trigger20call20transfer>).

> **NOTE:** Druid system entity fields storing the name of a SIP header (Name) will be automatically converted to lowercase (name) when sent over to VoiceAI Connect.

![](../../Resources/Images/Voice%20Audio%20Codes%20Channel/transfer%20entity%20params%201.png)

![](../../Resources/Images/Voice%20Audio%20Codes%20Channel/transfer%20entity%20params%202.png)

In the **SetVariables** section of the respective **transfer** backchannel step, set the **transferTarget** and the desired additional transfer parameters and SIP headers (if you want to send any).

![](../../Resources/Images/Voice%20Audio%20Codes%20Channel/transfer%20set%20variables.png)

> **Info:** When using the **Transfer** backchannel step, a "Connected with agent" event is now recorded in the Conversation History at the moment the transfer request is sent. This provides a clear audit trail of the routing action initiated by the AI Agent, as the contact center does not return a separate confirmation once an agent connects.

<a id="Disconnectingthecall"></a>

## Disconnecting the call

At any stage of the conversation, the AI Agent can disconnect the conversation. For the AI Agent to disconnect the call, add a backchannel step named **hangup**.

You can configure the backchannel step so that upon disconnect the AI Agent provides a textual reason that will be passed to the peer on the SIP Reason header and will appear in the CDR of the call. In addition, you can also configure the backchannel step to add SIP headers and their values, which will be included in the SIP BYE message.

To add the disconnect reason and additional SIP headers, on the **hangup** backchannel step, in Input mapping provide the entity which stores the desired values.

![](../../Resources/Images/Voice%20Audio%20Codes%20Channel/Voice%20Audio%20Codes%20Channel_5.png)

Make sure that the entity you provide in **Input mapping** contains fields named exactly as the parameters expected by VoiceAI Connect. For the complete list of hangup event parameters, see [VoiceAI Connect documentation](https://techdocs.audiocodes.com/voice-ai-connect/Default.htm#VAIG_Combined/hangup.htm?Highlight=HANGUP).

> **NOTE:** Druid system entity fields storing the name of a SIP header (Name) will be automatically converted to lowercase (name) when sent over to VoiceAI Connect.

![](../../Resources/Images/Voice%20Audio%20Codes%20Channel/Voice%20Audio%20Codes%20Channel_6.png)

In the **SetVariables** section of the **hangup** backchannel step, set the disconnect reason and/or additional SIP headers.

![](../../Resources/Images/Voice%20Audio%20Codes%20Channel/Voice%20Audio%20Codes%20Channel_7.png)

When the call disconnects, the following data is logged in the conversation context:

- **[[ChatUser]].VoiceConversationTerminatedReason** - The reason for which the call is disconnected. E.g., “Client Side”. The reason of the disconnect can be one of the following:

- **SocketInterrupted** – The connection was interrupted.
- **UserBecameSilent** – The user said nothing for 120 seconds.
- **CallTerminatedByCaller** – The user terminated the call.

- **[[ChatUser]].VoiceConversationTerminatedReasonCode** – The code (text) associated to the disconnect reason. E.g., “client-disconnected”.

<a id="AutomaticConversationEndedEvent"></a>

## Automatic Conversation Ended Event

> **Info:** This feature is available starting with Druid 9.27.

To ensure easy identification of call duration, the AudioCodes channel automatically saves the ActivityEnd event in the [[ChatActivityData]] to mark a conversation as completed in the system (End Time). This closure is triggered automatically by any of the following events:

- **Call Termination**. Triggers when a call hangs up. If a **Voice Termination Flow** is active, the closure is delayed until the flow completes executing under the same activity.
- **Hangup Backchannel Event**. Triggers when a hangup event is processed via the backchannel.
- **Transfer Backchannel Event**. Triggers immediately following the successful execution of a call transfer event.

![](../../Resources/Images/druid%209.27/end%20time.png)

![](../../Resources/Images/druid%209.27/conv%20insights%5D.png)
