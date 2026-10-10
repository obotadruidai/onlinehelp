<a id="CreateCustomVoices"></a>

# Create Custom Voices

> **IMPORTANT!** Creating voices incurs additional costs governed by your ElevenLabs subscription pricing. Druid does not charge extra for voice generation.

To create a custom voice, click the **Create Voice** button at the top-right corner of the page.

![](../Resources/Images/ElevenLabs%20Voices/Creating%20Custom%20Voices.png)

The voice creation editor offers three powerful creation methods:

- **Voice Design** - Design an entirely new voice from a text prompt.
- **Voice Clone** - Clone your voice with only 10 seconds of audio.
- **Voice Remix** - Transform existing voices with text prompts to create new voices.

The voice creation editor displays by default on **Voice Design**.

![](../Resources/Images/ElevenLabs%20Voices/Creating%20Custom%20Voices_1_815x168.png)

<a id="CreatevoiceswithVoiceDesign"></a>

## Create voices with Voice Design

Design an entirely new voice from scratch using a text prompt.

To create a new voice using Voice Design:

1. Click the **Voice Design** option at the top of the editor.
2. Type a detailed description of the desired voice into the **Prompt** field, covering traits like age, gender, accent, tone, and pacing.

   **Prompt example**

   ```
   A clear, articulate American female voice in her 30s to early 40s with a neutral accent. The tone is warm, professional, and reassuring, conveying calm confidence and deep knowledge. Pacing is measured and natural, with smooth transitions and an inviting warmth designed to make complex technical or product information sound simple and easy to digest.
   ```

   > **Info:** You can also reference the built-in suggested prompts for formatting inspiration. Click on **Suggested Prompts**, then click the desired prebuilt prompt and it will display in the **Prompt** field.
3. Optionally, you can configure the settings and customize the preview text.

- Adjust the **Loudness** and **Guidance Scale** sliders to set the desired output volume and adherence level.
- Customize preview text. By default, preview text is automatically generated. If you want to use your own text for preview, turn off the **Generate Preview Text** toggle and enter your own custom text to test the voice.
> **Info:**  For optimal results, use long and relevant preview text.

![](../Resources/Images/ElevenLabs%20Voices/Creating%20Custom%20Voices_2.png)

4. Click **Generate Voice**. Druid generates three voice variants based on your prompt.
5. Listen to the generated variants.

![](../Resources/Images/ElevenLabs%20Voices/Creating%20Custom%20Voices_3.png)

6. Select the preferred variant, then click **Select Voice**.

![](../Resources/Images/ElevenLabs%20Voices/Creating%20Custom%20Voices_4.png)

The Voice Design page appears. You can preview the selected voice here.

7. Enter a unique **Name** for the voice.
8. Provide a brief **Description** of the voice profile using a minimum of 20 characters.
9. You can also set additional parameters.
> **Info:** We recommend you select the **Gender** as well. This makes it easier to find the voice later when filtering created voices by gender.

![](../Resources/Images/ElevenLabs%20Voices/Creating%20Custom%20Voices_5.png)

10. Click **Save Voice**.

<a id="CreatevoiceswithVoiceClone"></a>

## Create voices with Voice Clone

Clone a speaker's voice using a short audio sample.

To create a voice with Voice Clone:

1. Click the **Voice Clone** option at the top of the editor.
2. Review quick tips. Read the on-screen recommendations beforehand to avoid noisy environments, check microphone quality, and maintain consistent equipment for the best results.
3. Provide the audio sample by using one of these two options:

- **Upload audio sample**. Upload an audio file in MP3 or WAV format (maximum file size of 1GB) that meets the minimum 10-second requirement.
- **Record voice**. Click **Record Voice** to capture the required audio directly. If multiple microphones are available on the device, a prompt will appear to select the desired one.

4. Keep the **Remove background noise** toggle enabled to clean up the audio sample.

![](../Resources/Images/ElevenLabs%20Voices/Creating%20Custom%20Voices_6.png)

5. Click **Generate Voice**. The Voice Clone page appears. You can preview the voice.
6. Enter a unique **Name** for the voice.
7. Enter a **Description** of at least 20 characters.
8. You can also set additional parameters.
> **Info:** We recommend you select the **Language** and **Gender**. This makes it easier to find the voice later when filtering created voices by language or gender.

9. Select the checkbox to confirm that you hold all necessary rights and consents to clone the voice sample, and that you agree to abide by the service's terms, policies, and privacy guidelines.

![](../Resources/Images/ElevenLabs%20Voices/Creating%20Custom%20Voices_7.png)

10. Click **Save Voice**.

<a id="CreatevoicesusingtheVoiceRemix"></a>

## Create voices using the Voice Remix

Transform your custom voice profiles using text prompts.

To create a new voice by remixing a voice you created:

1. Click the **Voice Remix** option at the top of the editor.

![](../Resources/Images/ElevenLabs%20Voices/Creating%20Custom%20Voices_8.png)

2. Select the voice reference you want to remix from the dropdown.
3. Type a description into the **Prompt** field to define the desired changes, or use the **Prompt Inspiration** categories (such as Accent, Age, Emotion, Pacing, Pitch, and Timbre) to quickly add descriptive tags.
4. Click on **Prompt Strength** and adjust the slider to control how much the prompt alters the reference voice, ranging from **Low** (for subtle clarity or tone changes) up to **Max** (for complete changes like gender).
5. Enter your custom text into the **Script** field to test how the transformed voice will sound. If you leave the field empty, a generated script is used.

![](../Resources/Images/ElevenLabs%20Voices/Creating%20Custom%20Voices_9.png)

6. Click **Generate Voice**. The system generates three variants based on the provided prompt. They display in the **Generated Results** section at the top of the editor.
7. Navigate through the three variants and listen to them. If none of the voice variants responds to your quality standards, generate more voices.

![](../Resources/Images/ElevenLabs%20Voices/Creating%20Custom%20Voices_10.png)

8. Select the preferred variant, then click Select Voice.

![](../Resources/Images/ElevenLabs%20Voices/Creating%20Custom%20Voices_11.png)

The Voice Remix page appears. You can preview the voice.

9. Enter a unique **Name** for the voice.
10. Enter a **Description** of at least 20 characters.
11. You can also set additional parameters.
> **Info:** We recommend you select the **Gender** as well. This makes it easier to find the voice later when filtering created voices by gender.

![](../Resources/Images/ElevenLabs%20Voices/Creating%20Custom%20Voices_12.png)

12. Click **Save Voice**.
