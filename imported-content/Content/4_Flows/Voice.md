---
layout:
  title:
    visible: false
---

<a id="Voice"></a>

# Voice

The Voice section is relevant when you are using voice on a flow and the flow has steps of type Choice, Thumbnail, or Hero, for which the system will not render the options using voice. In this case, you will provide the voice message as text, including all available options.

To see the Voice section, in the Flow Step Editor, click on the Voice section to expand it. The Voice section contains a **Speak message** field for each language configured on your AI Agent.

- In the first **Speak message** field, redact the voice message as text in the AI Agent default language.
- In the subsequent **Speak message** fields, enter the localized text of the redacted voice message in the AI Agent additional languages (if any).

<a id="UsingSSMLSpeechSynthesisMarkupLanguageforAdvancedVoiceText"></a>

## Using SSML (Speech Synthesis Markup Language) for Advanced Voice Text

The **Speak message** fields fully support Speech Synthesis Markup Language (SSML). When using a compatible Text-to-Speech (TTS) engine (such as Azure Speech Services), any SSML tags included in these fields are dynamically forwarded to the TTS service to fine-tune how your AI Agent sounds.

By leveraging SSML, you can control aspects of speech synthesis such as pitch, pronunciation, speaking rate, volume, and conversational styles (e.g., cheerful, empathetic).

> **Info:** SMML support is available starting with Druid 9.25.

When writing SSML inside a **Speak message** field, you must wrap your text in the standard `<speak>` root element and define the appropriate namespace attributes required by your provider.

Below are examples configured for Azure Speech Services:

<a id="Example1AdjustingRateandPitchProsody"></a>

### Example 1: Adjusting Rate and Pitch (Prosody)

Use the <prosody> tag to make the AI Agent speak slower, faster, or adjust its vocal pitch.

```
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
    <voice name="en-US-JennyNeural">
        Welcome back! <prosody rate="-10.00%" pitch="+5.00%">How can I help you today?</prosody>
    </voice>
</speak>
```

<a id="Example2AddingPausesBreak"></a>

### Example 2: Adding Pauses (Break)

Use the `<break>` tag to insert deliberate silences between options or sentences to make information easier to digest over the phone.

```
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-US">
    <voice name="en-US-JennyNeural">
        Please choose one of the following options. 
        For Technical Support, press 1. <break time="1s"/> 
        For Billing, press 2.
    </voice>
</speak>
```

<a id="Example3ChangingConversationalStylesExpressingEmotion"></a>

### Example 3: Changing Conversational Styles (Expressing Emotion)

If supported by your Azure Neural Voice profile, use the `<mstts:express-as>` tag to adjust the persona's speaking style (e.g., customer-service or empathetic).

```
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xmlns:mstts="http://www.w3.org/2001/mstts" xml:lang="en-US">
    <voice name="en-US-JennyNeural">
        <mstts:express-as style="customerservice">
            I understand your frustration, let me check that account for you right away.
        </mstts:express-as>
    </voice>
</speak>
```

> **NOTE:** Ensure that the `xml:lang` attribute and the `<voice name="...">` tag explicitly match the voice profile and region configured in your channel's Text-to-Speech settings. For an exhaustive breakdown of supported voice tags, styles, and advanced synthesis configurations, refer to the [Microsoft Azure SSML Documentation](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/speech-synthesis-markup).

## Related Topics

- [Common Flow Settings](Common%20Flow%20Settings.md)
