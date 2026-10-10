---
layout:
  title:
    visible: false
---

<a id="SpeechResourceManagementandGovernance"></a>

# Speech Resource Management and Governance

Druid Speech Resource Management enables system administrators to centrally configure, govern, and manage Speech-to-Text (STT) and Text-to-Speech (TTS) integration services across the platform. Rather than binding speech services directly within individual channel configurations, speech resources can be defined at the tenant level under **Administration** and reused across Druid Voice channels.

> **Info:** This feature is available starting with Druid version 9.31. Centralized speech resource management is currently supported for the Druid SIP channel.

![](../Resources/Images/Speech%20resources/speech%20resources.png)

<a id="SupportedVendorsandRequirements"></a>

## Supported Vendors and Requirements

Each speech vendor requires specific information to connect successfully. Use this quick reference table to find out what you need to prepare before setting up your connection:

| Vendor | Authentication | Required parameters |
| --- | --- | --- |
| Azure | API Key | ModelId, VoiceId, region.  Take your region identifier from the [Microsoft documentation](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/regions?tabs=geographies).  Take the voice identifier from the [Microsoft documentation](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support#text-to-speech?tabs=tts). |
| Deepgram | API key | ModelId, VoiceId. - For the list of available voice models and voice name, see [Deepgram documentation](https://developers.deepgram.com/docs/tts-models#language-support). |
| Druid Voice | The connection details you received from Druid. | ModelId, VoiceId |
| ElevenLabs | API Key | For STT, use as ModelId **scribe\_v2\_realtime**  For TTS, use as ModelId any of the following models:   - eleven\_v4 - eleven\_v4\_turbo - eleven\_v3 - eleven\_v3\_conversational - eleven\_multilingual\_v2 - eleven\_flash\_v2\_5 - eleven\_turbo\_v2\_5 - eleven\_turbo\_v2 - eleven\_flash\_v2   VoiceId is required only for TTS. Starting with Druid 10.1, you can retrieve the voice ID for an ElevenLabs resource by following these steps:   1. Save your ElevenLabs TTS resource. 2. In the Speech Resources page, click the **Preview** icon next to the resource you just added. 3. Click the **Created** tab if you want to retrieve the voice ID of a custom-created voice, or click **Saved** if you want the voice ID of a voice saved from the ElevenLabs Library. 4. Click the **Actions** icon and select **Copy voice ID**.  ![](../Resources/Images/ElevenLabs%20Voices/copy%20voice%20id.png) 5. Return to the Speech Resources page, open your ElevenLabs TTS resource, paste the copied voice ID into the Parameters table, and save the resource. |
| Mistral | API Key | ModelId  VoiceId - a valid voice ID from your Mistral account. The selected voice determines the characteristics of the synthesized audio, such as accent, tone, and speaking style.  **Info:** To obtain a voice ID, create or select a voice in your Mistral account and copy its identifier from the [Mistral Voices API](https://docs.mistral.ai/studio-api/audio/text_to_speech/speech) or voice management interface. |
| Munsit | API Key | ModelId, VoiceId, region |
| Soniox | Access Secret | ModelId, VoiceId of the chosen [Soniox voice](https://soniox.com/docs/tts/concepts/voices#supported-voices). |

<a id="Addspeechresources"></a>

## Add speech resources

To establish a governed connection to a speech provider, follow these steps:

1. Go to **Administration** > **Speech Resources**.

![](../Resources/Images/Speech%20resources/speech%20resources.png)

2. Click the **Create Speech Resource** button. The Speech Resource Details modal appears.

![](../Resources/Images/Speech%20resources/speech%20modal.png)

3. Configure the speech resource:

1. **Provider**: Select the speech provider from the dropdown.
2. **Resource Type**: Select the speech resource type:

- **STT**: Speech-to-Text (Voice Recognition / Transcription).
- **TTS**: Text-to-Speech (Voice Synthesis).
- **STT\_TTS**: Combined Speech-to-Text and Text-to-Speech capability.

> **IMPORTANT!** For the ElevenLabs provider, you cannot create a single resource record with the **STT\_TTS** resource type because ElevenLabs requires different Model ID parameters for Speech-to-Text versus Text-to-Speech services. You must add dedicated, separate ElevenLabs resources for TTS and STT respectively.

3. **API Url**: Type or paste the web address endpoint provided by your vendor. For some providers, this field is automatically filled in.
4. **Disable Ssl Validation**: Keep this set to **No**. Only change this to **Yes** if explicitly instructed by your internal IT support team.
5. Enter the specific security credentials (API Key) provided by your AI vendor and set the required vendor-specific parameters. The platform automatically masks the credentials into dots to protect your security.

4. Check the **Active** box to turn the model connection on and make it available for use.
5. Click **Save & Close**.
