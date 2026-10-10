---
title: "Vonage Voice"
---

<a id="VonageVoice"></a>


Vonage Voice is a cloud-based voice communication service provided by Vonage. It enables businesses to make and receive voice calls over the internet using Voice over IP (VoIP) technology.

Integrating AI Agents with Vonage Voice enhances customer interactions by enabling seamless voice-based conversations, automated call handling, and efficient call routing, improving support and engagement while reducing operational costs.

<a id="Prerequisites"></a>

## Prerequisites

- You built and published a AI Agent.
- You have a Vonage account.

<a id="IntegrateDruidwithVonageVoice"></a>

## Integrate Druid with Vonage Voice

To integrate Druid with Vonage Voice, follow these:

<a id="Step1GetthechannelURLsfromtheDruidPortal"></a>

### Step 1. Get the channel URLs from the Druid Portal

Go to the AI Agent details page and click on the **Channels** tab. Then, search for **Vonage, Voice** and click on the card. From the channel configuration modal, copy the **Answer URL**, **Event URL** and **Fallback URL**, as you’ll need them to configure your Vonage application.

![](../Resources/Images/Vonage%20Voice/channel%20urls.png)

<a id="Step2CreateandconfigureyourVonageapplicationforVoice"></a>

### Step 2. Create and configure your Vonage application for Voice

To integrate Vonage Voice with DRUID, you need to configure a Vonage application. This involves setting up a phone number for voice, adding channel URLs from the Druid Portal, and retrieving API private key. Follow the steps below to complete the setup:

1. Log in to the [Vonage Portal](https://dashboard.nexmo.com/).
2. In the **BUILD & MANAGE** menu, click **Applications**.
3. In Your applications page, click the **Create a new application** button.
4. Enter a name for your application.
5. In the Capabilities section, tap on **Voice**.
6. Enter the **Answer URL**, **Event URL** and **Fallback URL** you copied from the Druid Portal.

![](../Resources/Images/Vonage%20Voice/create%20app.png)

7. Click the **Generate new application** button to create the app.
8. Link the desired phone number you have for SMS & Voice. If you don't have one, buy it.
9. Note down the phone number and the Application ID, as you’ll need them to configure the channel in the Druid Portal.

![](../Resources/Images/Vonage%20Voice/link%20app%20no.png)

10. Go back to your app configuration page ( **BUILD & MANAGE** menu > **Applications**> your app).
11. Generate public and private key.

![](../Resources/Images/Vonage%20Voice/GENERATE%20KEY.png)

12. The private key is downloaded on your computer.

<a id="Step3ActivatetheVonageVoicechannelinDruid"></a>

### Step 3. Activate the Vonage Voice channel in Druid

To activate the Vonage Voice channel, follow these steps:

1. In the Druid Portal, navigate to the **Voice, Vonage** configuration section.
2. Enter the **Application ID** you copied from Vonage and the **Private Key** from the file you downloaded when generating the app private key in Vonage.
3. Click the **Publish** button to activate the channel.

![](../Resources/Images/Vonage%20Voice/channel%20activate.png)

After the channel’s activation, the following fields are available in Druid:

- **[[ChatUser]].ChannelId** = "vonage-voice"
- **[[ChatUser]].UserId** - Stores the user's phone number in international format.

<a id="Transferringthecalltoaliveagent"></a>

## Transferring the call to a live agent

There are cases when the AI Agent may be unable to fully resolve a user's request and needs to escalate the call to a human agent in a call center. This feature allows the AI Agent to seamlessly transfer the call.

To enable your AI Agent to escalate a call to a live agent, follow these steps:

1. Add a backchannel step named **transfer** to the conversation flow where escalation is required.
2. In the **Input mapping** section of the **transfer** backchannel flow step, you must provide an entity that stores the necessary transfer values. E.g., [[VoiceParams]].

![](../Resources/Images/druid%208.17/transfer_input%20mapping.png)

3. Ensure that the entity you provided in Input mapping contains a string field named **transferTarget**.
4. In the SetVariables section of the **transfer** backchannel step, set [[entity]].**transferTarget** to the specific value provided by your Vonage contact center administrator.
> **NOTE:** The format of **transferTarget** may vary depending on your Vonage contact center integration.

For demo purposes, you can set [[entity]].**transferTarget** to a phone number associated with an agent.

![](../Resources/Images/druid%208.17/transferTarget.png)

5. Save the step.

By default, once a transfer is initiated, the AI Agent immediately disconnects from the call, regardless of whether the transfer to the live agent is successful.

<a id="SendingcallparameterstoVonageVoice"></a>

## Sending call parameters to Vonage Voice

Enhance your call interactions by sending additional data to Vonage Voice when a call is initiated. This enables greater flexibility and integration with your call workflows.

To send relevant data when a call is initiated, in the **Advanced Parameters** JSON field, set the desired parameters. DRUID supports sending the following call parameters:

| Parameter | Description |
| --- | --- |
| druidLanguage | The AI Agent default language. |
| bargeIn | Set to `true` so this action is terminated when the user interacts with the application either with DTMF or ASR voice input. Use this feature to enable users to choose an option without having to listen to the whole message in your Interactive Voice Response (IVR). If you set `bargeIn` to `true` the next non-talk action in the NCCO stack must be an input action. The default value is `false`. |
| loop | The number of times text (the message to be synthesized in the call) is repeated before the call is closed. The default value is `1`. Set to `0` to loop infinitely. |
| level | The volume level that the speech is played. This can be any value between `-1` to `1`. Th default value is `0`. |
| language | The language (BCP-47 format) for the message you are sending. Possible values supported by Vonage Voice are listed in the [Text-To-Speech guide](https://developer.vonage.com/en/voice/voice-api/guides/text-to-speech#supported-languages). |
| style | The vocal style (vocal range, tessitura and timbre). The default value is `0`. Possible values are listed in the [Text-To-Speech guide](https://developer.vonage.com/en/voice/voice-api/guides/text-to-speech#premium-voices). |
| premium | Set to true to use the premium version of the specified style if available, otherwise the standard version will be used. The default value is `false`. You can find more information about Premium Voices in the [Text-To-Speech guide](https://developer.vonage.com/en/voice/voice-api/guides/text-to-speech#premium-voices). |
| endOnSilence | Controls how long the system will wait after user stops speaking to decide the input is completed. The default value is `2` (seconds). The range of possible values is between `0.4` seconds and `10` seconds. |
| startTimeout | Controls how long the system will wait for the user to start speaking. The range of possible values is between `1` second and `60` seconds. The default value is `60`. |
| maxDuration | Controls maximum speech duration (from the moment user starts speaking). The default value is `60` (seconds). The range of possible values is between `1` and `60` seconds. |
| sensitivity | Audio sensitivity used to differentiate noise from speech. An integer value where 10 represents low sensitivity and 100 maximum sensitivity. The default value is `90`. |

<a id="ForwardingvoicecallstoSIP"></a>

## Forwarding voice calls to SIP

This section explains how to configure DRUID to forward inbound calls received on your Vonage voice-enabled virtual number directly to a SIP (Session Initiation Protocol) endpoint. This allows you to seamlessly integrate your Vonage numbers with existing SIP-compatible systems.

When a call is received on your configured Vonage virtual number, DRUID can redirect the call to any SIP-compatible system. This includes VoIP phones, Private Branch Exchanges (PBXs), or dedicated SIP servers.

> **NOTE:** This feature is available in DRUID 9.1 and higher.

To set up call forwarding, follow these steps:

1. Tap on **Forward to SIP**.
2. In the **SIP URL** field, enter your SIP Uniform Resource Identifier (URI). This can be in one of two formats:

- IP Address: username@IP\_ADDRESS (e.g., 123@201.354.123.456)
- Domain: username@domain.com (e.g., 1234@sipdomain.com)
> **NOTE:** If you're unsure of your SIP URI, please consult your internal VoIP or PBX administrator, your SIP service provider, or refer to your SIP gateway's configuration interface.

![](../Resources/Images/druid%209.1/sip.png)

3. Click **Save** to apply your changes.

> **IMPORTANT!**  For successful call delivery, it is crucial that your receiving SIP endpoint is configured to accept incoming calls from the Druid forwarding URL. Copy the **Forward URL** and providing it to your VoIP/PBX administrator or SIP service provider. They will need to allow incoming calls from this specific Druid Forward URL on your SIP system.
>
> ![](../Resources/Images/druid%209.1/FORARD%20URL.png)
