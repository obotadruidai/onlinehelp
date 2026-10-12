---
title: Speech Resource Configuration
---


The **Configurations** tab allows you to fine-tune how ElevenLabs speech resources operate. You can manage settings for both Text-to-Speech (TTS) and Speech-to-Text (STT) services using inline JSON editors.

Before changing default resource configurations, we recommend you test the configurations in the [Playground](Playground.md#Playground).

## TTS Configuration

TTS configurations control voice generation parameters supported by ElevenLabs.

Select a voice profile and model, then define your properties inside the TTSConfiguration JSON editor. For more information on the supported parameters, see [ElevenLabs documentation](https://elevenlabs.io/docs/eleven-creative/playground/text-to-speech#voice-settings-1).

Default settings are visible in the non-editable ExampleConfiguration panel.

![](<../../.gitbook/assets/Speech Configuration.png>)

Click the **Save** button at the top-right corner of the page to save the configuration.

## STT Configuration

STT configurations control real-time transcription parameters and Voice Activity Detection (VAD) behaviors.

When configuring real-time Speech-to-Text (STT) resources, you can use the following parameters to adjust Voice Activity Detection (VAD) and transcription behavior:

| Parameter               | Range     | Default value | Description                                                                                                                                                           |
| ----------------------- | --------- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| vadSilenceThresholdSecs | 0.3 - 3.0 | 1.5           | Defines the duration of silence in seconds required before the VAD automatically commits a transcript segment.                                                        |
| vadThreshold            | 0.1 - 0.9 | 0.4           | Sets the sensitivity threshold for the VAD model to distinguish active speech from background noise. Lower values make transcription more sensitive to quieter input. |
| minSpeechDurationMs     | 50 - 2000 | 100           | Specifies the duration of speech in milliseconds required to be considered valid speech by VAD.                                                                       |
| minSilenceDurationMs    | 50 -2000  | 100           | Determines the minimum duration of silence in milliseconds required to be considered a speech break by VAD.                                                           |

Select a voice profile and model, then define your properties inside the **STTConfiguration** JSON editor.

![](<../../.gitbook/assets/Speech Configuration_1.png>)

Default JSON:

**Default JSON**

```
{
  "vadSilenceThresholdSecs": 1.5,
  "vadThreshold": 0.4,
  "minSpeechDurationMs": 100,
  "minSilenceDurationMs": 100
}
```
