<a id="AdvancedCallParametersandSessionEvents"></a>

# Advanced Call Parameters and Session Events

Configure advanced backend communication between the Druid AI Agent and AudioCodes VoiceAI Connect using backchannel flow steps. This topic explains how to pass real-time events, modify activity parameters, and declare global session attributes via JSON objects to control overall call behavior, timeouts, and system actions.

<a id="SendingeventstoVoiceAIConnect"></a>

## Sending events to VoiceAI Connect

You can send events (playUrl, transfer, hangup, etc.) from Druid to VoiceAI Connect by using Druid Backchannel Flow Steps to generate any supported VoiceAi Connect event.

![](../../Resources/Images/Voice%20Audio%20Codes%20Channel/audio%20codes%20events.png)

In Input mapping on the backchannel step, provide the entity that stores activity parameters of that event.

<a id="Setsessionparametersusingtheconfigevent"></a>

## Set session parameters using the "config" event

> **NOTE:** Use the "config" event with priority against the SetVoiceSessionParams.

To set the parameters for the entire call (session parameters), at the beginning of the call, on the welcome flow, add a backchannel step named **config** and in **Input mapping** provide the entity which stores the timeouts and actions you want to set.

On the flow step, click the **Metadata** section, tap on **Advanced Editing** and in the JSON field add the "sessionParams" object and set the desired parameters.

For information on the **config** event and general parameters for the **config** event, see VoiceAI Connect documentation, section [General AI Agents parameters](https://techdocs.audiocodes.com/voice-ai-connect/#VAIG_Combined/parameters.htm#General) and [Changing call settings](https://techdocs.audiocodes.com/voice-ai-connect/#VAIG_Combined/changing-call-setting.htm).

If later on you decide to update some session parameters, use a backchannel step called **SetVoiceSessionParams** and in **Input mapping** provide the entity which stores the timeouts and actions you want to address and in the Metadata section add the object specific to the action you want to perform and provide the parameters.

If you want to send some metadata during the call, use **Send metadata** event that corresponds to an Info SIP event.

<a id="HandlingAIAgentDelay"></a>

## Handling AI Agent Delay

Handling AI Agent delays is particularly useful when the AI Agent executes an integration which might take longer to complete.

By setting timeouts, you can configure the following actions to address situations when the AI Agent takes time to respond to a message sent to it:

- Play a textual prompt to the user
- Play an audio file to the user
- Disconnect the call
- Resume speech recognition (so the call will not remain hanging).

To handle not delay, add a backchannel step called **SetVoiceSessionParams**. In **Input mapping** provide the entity which stores the timeouts and actions you want to address.

Make sure that the entity you provide in Input mapping contains fields named exactly as the parameters expected by VoiceAI Connect. For the complete list of parameters, see [VoiceAI Connect documentation](https://techdocs.audiocodes.com/voice-ai-connect/#VAIG_Combined/handle-bot-delay.htm?Highlight=resumerecognit).

In the **SetVariables** section of the backchannel step, configure the timeouts and define the actions based on your needs.

<a id="Modifyingcallparameters"></a>

## Modifying call parameters

Any backchannel type flow step is sent as event to VoiceAI Connect (transfer, hangup, etc.). In the **activityParams** property of that specific VoiceAi Connect event, Druid sends the JSON object of the entity specified in **Input mapping** on the backchannel step.

If you want to modify activity parameters without sending a specific event to AudioCodes’ VoiceAI Connect (detect language change on conversation activity), you need to use a backchannel step called **SetVoiceActivityParams**. In the **activityParams** property, Druid sends the JSON object of the entity specified in **Input mapping** on the backchannel step.

If you want to modify session parameters (handle AI Agent delay, detect language change on session level, etc.), you need to use a backchannel step called **SetVoiceSessionParams**. In the **sessionParams** property, Druid sends the JSON object of the entity specified in **Input mapping** on the backchannel step.

<a id="StoreincomingSIPheadersinQueryParams"></a>

## Store incoming SIP headers in [[QueryParams]]

Storing incoming custom SIP headers (metadata sent by the contact center solution together with initiation call event) can be particularly useful for companies when running outbound dialing campaigns, whereby the dialer automatically initiates calls with potential customers.

AudioCodes VoiceAI Connect can pass custom SIP headers from incoming phone calls directly to Druid using the `sipHeadersToBot` configuration parameter. When this option is enabled in VoiceAI Connect, selected incoming SIP headers (for example, custom carrier headers or PBX routing data) are forwarded during the call initialization handshake. Druid captures these headers and makes them available within the system entity **[[QueryParams]]**.

By default, **[[ChatUser]].Phone** stores the user’s phone number and **[[ChatUser]].CalleePhoneNumber** stores the AI Agent phone number.

> **NOTE:** You need to create dedicated fields in the [[QueryParams]] system entity that have the same name as the incoming SIP header keys. You can store additional incoming custom SIP headers in dedicated fields in the **[[QueryParams]]** system entity. For that, you need to create dedicated fields that have the same name as the incoming SIP header keys.

For more information about configuring header forwarding on the AudioCodes side, see [VoiceAI Connect documentation](https://techdocs.audiocodes.com/voice-ai-connect/#VAIG_Combined/sending-any-SIP-header-to-bot.htm).

<a id="StorecallinitiationmetadatadialoutMetadata"></a>

## Store call initiation metadata (dialoutMetadata)

When an outbound call (dialout) is initiated via AudioCodes VoiceAI Connect, custom parameters and user metadata passed in the `dialoutMetadata` object are received during the session start event.

Druid automatically stores this initiation payload inside the following system entity field: **[[QueryParams]].dialoutMetadata**.

> **IMPORTANT!** Although [[QueryParams]] is a built-in system entity, the **[[QueryParams].dialoutMetadata** field is not created by default. You must manually create the **dialoutMetadata** field (string) inside the [[QueryParams]] system entity before attempting to store, read, or parse this payload in conversation flows.

Because this parameter carries structured JSON data (such as participant details, CRM identifiers, or custom session parameters), Druid saves `dialoutMetadata` as a stringified JSON.

**Example event payload**

```
{
  "type": "event",
  "name": "start",
  "parameters": {
    "callee": "+123456789",
    "caller": "1-800-111-111",
    "dialoutMetadata": {
      "participantName": "Alice"
    }
  }
}
```
