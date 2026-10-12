---
title: "TTS and STT Vendors"
---

<a id="TTSandSTTVendors"></a>


Druid provides a flexible, speech provider agnostic architecture, allowing you to integrate with the industry's leading Text-to-Speech (TTS) and Speech-to-Text (STT) engines. This commitment to an open ecosystem ensures you can select the best-performing voice models for your specific language, region, or industry requirements.

As the conversational AI landscape evolves, we regularly extend this list to include emerging technologies and specialized providers.

<a id="DruidSIP"></a>

## Druid SIP

The following table outlines the supported voice service providers for Druid SIP integrations, highlighting availability across both cloud and on-premises deployments.

| Provider | Cloud TTS | Cloud STT | On premises TTS | On premises STT |
| --- | --- | --- | --- | --- |
| Druid | yes | yes | no | no |
| Azure | yes | yes | yes | yes |
| ElevenLabs | yes | yes | yes | yes |
| Soniox | yes | yes | yes | yes |
| Deepgram | yes | yes | no | yes |
| Mistral AI (Voxtral speech model) | yes | yes | yes | yes |
| Munsit\* | yes | yes | yes | yes |

{% hint style="info" %}
**Info:** Support for Munsit speech services is available starting with Druid 9.31.
{% endhint %}

<a id="SpeechSynthesisMarkupLanguageSSMLSupport"></a>

### Speech Synthesis Markup Language (SSML) Support

Speech Synthesis Markup Language (SSML) is supported for Druid SIP; however, tag execution is dependent on your underlying telephony Text-to-Speech (TTS) provider:

| Provider | SSML Support Level | Notes |
| --- | --- | --- |
| Druid | Not Supported | - |
| Azure | Full Support | Processes the complete range of standard SSML tags. |
| ElevenLabs | Partial Support | Supports basic SSML tags. Advanced formatting (such as pitch, reading style, and intonation) is not supported. |
| Soniox | Not Supported | - |
| Deepgram | Not Supported | - |
| Mistral AI (Voxtral speech model) | Not Supported | - |

<a id="WebChatVoiceChannel"></a>

## WebChat Voice Channel

For web-based interactions, the WebChat Voice Channel supports a diverse range of providers to ensure low-latency and high-accuracy speech processing.

| Provider | Cloud TTS | Cloud STT | On premises TTS | On premises STT |
| --- | --- | --- | --- | --- |
| Druid | yes | yes | no | no |
| Microsoft | yes | yes | yes | yes |
| ElevenLabs | yes | yes | yes | yes |
| Deepgram | no | yes | no | yes |
| Soniox | no | yes | no | yes |
| Speechmatics | no | yes | no | yes |
