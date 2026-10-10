---
title: Configuring the Solution Template
---

# Configuring the Solution Template

To configure the solution template, follow these steps:

### Step 1. Install the solution from the Solutions Library

Go to the Solutions Library, search for solution Hospitality and import it following the instructions provided in section [Installing Solution Templates](<../Installing Solution Templates.md>).

Wait until the import status shows as “Success.”

![](<../../../.gitbook/assets/Configuring Skill Templates.png>)

Once the import is successful, click **Save & Close**.

### Step 2. Set up your Openai API Key

This solution template has only one app that requires setup, GPT-azure.com.

{% hint style="info" %}
**NOTE:** Charges apply to your Openai account according to the [Openai pricing policy](https://openai.com/pricing).
{% endhint %}

1. Go to [Openai](https://platform.openai.com/account/api-keys), log in and on the **User** menu, click **API Keys**.
2. In the API keys page, click the **Create new secret key** button.

![](<../../../.gitbook/assets/Configuring Skill Templates_1.png>)

A secret key is generated.

3. Copy the secret key as you will need it in DRUID.
4. In Druid Portal, on your AI Agent, select solution Hospitality and on the main menu, click **Apps**.
5. Click on the **GPT-azure.com** app. The app configuration page opens.
6. Scroll down to the Variables table and as value for the **key** variable, set up the secret key you copied from Openai. Save the key.

![](<../../../.gitbook/assets/Configuring Skill Templates_2.png>)

7. Scroll down and click **Save & Close**.
8. Click the **Publish** button at the top-right corner of the Apps page to publish the connectors.

![](<../../../.gitbook/assets/Configuring Skill Templates_3.png>)

### Step 3. Activate the AudioCodes channel

1. In the Druid Portal go to your AI Agent settings. Click the **Channels** tab, and then click **Voice, AudioCodes – VoiceAi Connect**. The channel info section expands.
2. Generate a token by clicking the **Generate** button.

![](<../../../.gitbook/assets/Configuring Skill Templates_4.png>)

3. Publish the channel.

![](<../../../.gitbook/assets/Configuring Skill Templates_5.png>)

For more information on how to set up the AudioCodes channel, see [Voice Audio Codes Channel](<../../Channels/Voice Audio Codes/Voice Audio Codes Channel.md>).

### Step 4. Activate the MS Teams channel

On the **Channels** tab, and click **Teams**. The Teams Channel Info section expands.

Activate the Teams channel. To do so, select the Microsoft Teams option that suits your company's Microsoft Office 365 version, agree to the Microsoft terms and statements and click the **Publish** button.

For more information about the Teams channel, see [MS Teams Integration](<../../Channels/MS Teams/MS Teams Integration.md>).

### Step 5. Set up the AI Agent special flows

Go to the AI Agent settings, Details page and click the **Dialog management** section header. The section expands. Select the following special flows:

| Special Flow          | Select                |
| --------------------- | --------------------- |
| Welcome flow          | first-welcome-flow    |
| Intent not found flow | Intent-not-recognized |

![](<../../../.gitbook/assets/Configuring Skill Templates_6.png>)

Scroll down and tap on **Use Knowledge Base**, then select the Knowledge base response flow that comes with the solution.

![](<../../../.gitbook/assets/Configuring Skill Templates_7.png>)

Scroll down and click **Save & Close**.

### Step 6. Train your AI Agent

From the **NLU** menu, click **Configurations** and then click the **Intents** tab. Click the **Train** button.

![](<../../../.gitbook/assets/Configuring Skill Templates_8.png>)

### Step 7. Add KB data sources

You can import your own knowledge base documents or use the provided examples:

* [FAQ – English](../../Solution%20Library/Hospitality/https:/druiddocs.file.core.windows.net/docs-shares/Hospitality/FAQ%20EN.xlsx)
* [FAQ – Portuguese](../../Solution%20Library/Hospitality/https:/druiddocs.file.core.windows.net/docs-shares/Hospitality/FAQ%20PT.xlsx).

For information on how to import files, see [File repository data sources](<../../Knowledgebase/File repository data sources.md>).
