---
layout:
  title:
    visible: false
---

<a id="ChatandVoiceAssistedChatInteractions"></a>

# Chat and Voice-Assisted Chat Interactions

The Voice-assisted chat interactions allows web users to speak their messages instead of manually typing. Similar to using a voice-assisted keyboard on a mobile device, users can tap a voice icon within the chat interface to speak their input. Users can switch effortlessly between typing and speaking.

Key characteristics of voice-assisted chat interactions include:

- **Text-only communication**. The channel remains purely text-based. Voice input is transcribed into text directly on the client side before being sent to the AI Agent, and responses are delivered as standard text.
- **Client-side transcription**. Speech-to-text processing happens directly in the user's browser, relying on native client-side speech recognition capabilities.

<a id="Howthechannelworks"></a>

## How the channel works

Once speech services are enabled, the interaction follows a streamlined flow:

1. Users click the microphone icon in the chat snippet to begin speaking.

![](../../Resources/Images/voice%20channel/Voice%20Channel.png)

2. The Speech-to-Text (STT) service processes the voice input in real-time, displaying a transcript in the input field.
3. Once the sentence is complete, the AI Agent processes the text and generates a response.
4. The response is displayed as text and simultaneously spoken back to the user via the Text-to-Speech (TTS) service.

![](../../Resources/Images/voice%20channel/Voice%20Channel_1.png)

<a id="EnablingVoiceassistedInteractions"></a>

## Enabling Voice-assisted Interactions

This section explains how to enable voice-assisted interactions.

<a id="Step1ConfigureSpeechProviders"></a>

### Step 1: Configure Speech Providers

Configure voice interactions directly within the WebChat channel settings:

1. In the Druid Portal, navigate to your AI Agent and select the **Channels** tab.
2. Search for 'webchat' and click on the **WebChat** card.

![](../../Resources/Images/voice%20channel/Voice%20Channel_2.png)

The channel configuration modal opens.

![](../../Resources/Images/voice%20channel/Voice%20Channel_3.png)

3. At the top of the modal, click the tab for the speech provider you wish to configure.
4. Configure the desired speech providers following the instructions in the subsequent sections.

> **Info:** To integrate a preferred speech provider not listed below, reach out to your Druid representative.

#### Setting up Druid-native speech

To use voice interactions with Druid-native speech services, you need the API key from your Druid representative.

> **NOTE:** Druid-native STT/TTS is available in technology preview in Druid 9.20.

Setup procedure:

1. In the channel configuration modal, click the **Druid** tab.
2. Enter the details you received from your Druid representative.
3. Map the languages your AI Agent supports to specific Druid languages in the configuration table.

1. In the table, click the plus icon (+) to add a row.
2. From the **Language** dropdown, select the AI Agent language (default or additional).
3. From the **Voice** dropdown, select the specific voice the AI Agent will use to respond. The model is automatically filled in after you select the voice.

![](../../Resources/Images/voice%20channel/Voice%20Channel_4.png)

4. Click the **Save** icon displayed inline.

Add the desired voice per AI Agent language as you prefer.

4. Click **Save** at the bottom of the page and close the modal.

#### Setting up Microsoft Cognitive Services

> **IMPORTANT!**  To use voice interactions with MS Cognitive Services in production environments, contact your Druid representative for the necessary keys.

1. In the channel configuration modal, click the **Microsoft Cognitive Services** tab.
2. Provide the **Key** and **Region** provided by Druid Support Team in the voice activation email.
> **Info:** For demo purposes, you can request a test key to [Druid Tech Support](mailto:support@druidai.com?subject=Voiceactivation%20-%20send%20me%20a%20test%20key).

3. Map the languages your AI Agent supports to specific voices in the configuration table.

1. In the table below the Voice channel details, click the plus icon (+) to add a row.
2. From the **Language** dropdown, select the AI Agent language (default or additional).
3. From the **Voice** dropdown, select the specific voice the AI Agent will use to respond.
4. Click the **Save** icon displayed inline.

4. Save the configuration.

#### Setting up Deepgram

> **IMPORTANT!**  You can use Deepgram as voice provider for Webchat in DRUID 9.1 and higher for Speech-To-Text (STT) only.

##### Prerequisites

- You need a Deepgram API Key with Member Permissions. Refer to Deepgram documentation ([Token-Based Authentication](https://developers.deepgram.com/guides/fundamentals/token-based-authentication#why-do-i-get-a-forbidden-error)) for information on how to create a key with Member permissions.

##### Setup procedure

1. In the channel configuration modal, click the **Deepgram** tab.
2. Enter your Deepgram API Key.
3. Map the languages your AI Agent supports to specific Deepgram models in the configuration table.

1. In the table, click the plus icon (+) to add a row.
2. From the **Language** dropdown, select the AI Agent language (default or additional).
3. From the **Model** dropdown, select the specific Deepgram model the AI Agent will use to respond.
4. Click the **Save** icon displayed inline.

> **Info:** For Druid versions prior to 9.6, provide the Deepgram model (e.g., nova-2-medical). See [Deepgram documentation](https://developers.deepgram.com/docs/models-languages-overview) for the complete list of models available.

4. Save the configuration.

#### Setting up ElevenLabs

Druid supports ElevenLabs as a high-quality Text-to-Speech (TTS) and Speech-To-Text (STT) provider, enabling your AI Agent to communicate using specialized synthetic voices and custom voice clones.

> **NOTE:**  ElevenLabs is available as TTS provider starting with Druid 9.15 and as STT provider starting with Druid 9.18.

##### Prerequisites

- You need an ElevenLabs API Key. To get API key, go to [https://elevenlabs.io/app/developers/api-keys](https://elevenlabs.io/app/developers/api-keys) and copy the key ID.

![](../../Resources/Images/voice%20channel/Voice%20Channel_7.png)

- Make sure to grant the API Key Read permissions for the following endpoints:

- Voices
- Text to Speech
- Speech to Speech
- Speech to Text (for STT support)
- Sound Effects
- Audio Isolation

![](../../Resources/Images/voice%20channel/Voice%20Channel_8.png)

![](../../Resources/Images/voice%20channel/Voice%20Channel_9.png)

##### Setup procedure

1. In the channel configuration modal, click the **ElevenLabs** tab.
2. Enter your ElevenLabs API Key.
3. From the **Region** dropdown, select the residency region you want to use:

- **Global (US)** – Uses the global ElevenLabs API endpoint.
- **Europe (EU)** – Uses the EU residency API endpoint.
- **India (IN)** – Uses the India residency API endpoint.

The selected region determines which ElevenLabs API endpoint is used by the Web Chat Voice channel.

4. Map the languages your AI Agent supports to specific ElevenLabs languages in the configuration table.

1. In the table, click the plus icon (+) to add a row.
2. From the **Language** dropdown, select the AI Agent language (default or additional).
3. From the **Voice** dropdown, select the specific ElevenLabs voice the AI Agent will use to respond. The model is automatically filled in after you select the voice.
4. Click the **Save** icon displayed inline.

5. Click **Save** at the bottom of the page and close the modal.

#### Setting up Soniox

You can use Soniox as a Speech-To-Text (STT) provider for your AI Agent voice interactions. Its models natively support multiple languages and automatic language detection.

> **NOTE:** Soniox is available as a STT provider starting with Druid 9.19.

##### Prerequisites

- You need a API Key. To get your API key, sign in [https://console.soniox.com/signin/](https://console.soniox.com/signin/), go to your project > API Keys and copy the key ID.

![](../../Resources/Images/voice%20channel/Voice%20Channel_10.png)

##### Setup procedure

1. In the channel configuration modal, click the **Soniox** tab.
2. Enter your Soniox API Key and select the model.
3. Click **Save** at the bottom of the page and close the modal.

#### <a id="Setting"></a>Setting up Speechmatics

Speechmatics is a speech-to-text provider available in the Voice Channel. It enables real-time and batch transcription using advanced automatic speech recognition (ASR) technology. It supports multiple languages and delivers accurate results across different accents and audio conditions, making it suitable for voice interactions and transcription scenarios.

> **NOTE:** Speechmatics is available as a STT provider starting with Druid 9.20.

##### Prerequisites

- You need a Speechmatics API Key. To get your API key, follow [Speechmatrics documentation](https://apps.make.com/speechmatics#obtain-your-api-key-in-your-speechmatics-account).

##### Setup procedure

1. In the channel configuration modal, click the **Speechmatics** tab.
2. Enter your Speechmatics API Key.
3. **(Optional)** Configure a Custom Dictionary to improve recognition of organization-specific terminology.
   The Custom Dictionary allows you to define words or phrases that Speechmatics should recognize more accurately, such as product names, brand names, acronyms, or technical terms. Use the + button to add dictionary entries.

For each entry, configure the following fields:

| Field | Description |
| --- | --- |
| Word/Phrase | The word or phrase that should appear in the transcript. |
| Sounds Like | Optional pronunciation variants that help Speechmatics recognize the term. Multiple values can be provided as a comma-separated list. |

Save the dictionary entry and add as many as you want.

![](../../Resources/Images/druid%209.24/speechmatics%20dictionary.png)

> **Info:** Custom dictionary is available starting with Druid version 9.24.

4. Save the configuration and close the modal.

<a id="Step2EnableSpeechServices"></a>

### Step 2. Enable Speech Services

Once the speech provider details are entered, you must explicitly activate them for the channel:

1. In the WebChat configuration modal, click the **General** tab and scroll-down at the bottom of the modal.
2. Select the primary **Speech-to-Text Provider**. If you select a provider other than Azure, you should also select a **Fallback Speech-to-Text Provider**. The fallback speech provider will be used automatically if primary speech provider does not support the user’s language.
> **Info:** If Deepgram is set as the primary STT provider and Azure/ElevenLabs as fallback, and the user selects a language unsupported by Deepgram, the system falls back to Azure/ElevenLabs. Once the user changes the language back to one that Deepgram supports, the system will automatically switch back to Deepgram (the primary provider) for the remainder of the session.

3. Select the primary **Text-to-Speech Provider**. If you selected ElevenLabs or Druid, you should also select the **Fallback Text-to-Speech Provider**. The fallback provider will be used automatically if the primary one does not support the user’s language.

![](../../Resources/Images/voice%20channel/Voice%20Channel_12.png)

4. Click **Save** and close the modal.
