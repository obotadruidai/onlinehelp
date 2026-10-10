---
layout:
  title:
    visible: false
---

<a id="ConfiguringtheSolutionTemplate"></a>

# Configuring the Solution Template

To configure the solution template, follow these steps:

<a id="Step1InstallthesolutionfromtheSolutionsLibrary"></a>

## Step 1. Install the solution from the Solutions Library

Go to the Solutions Library, search for solution Hospitality and import it following the instructions provided in section [Installing Solution Templates](../Installing%20Solution%20Templates.md).

Wait until the import status shows as “Success.”

![](../../Resources/Images/Hospitality/Configuring%20Skill%20Templates.png)

Once the import is successful, click **Save & Close**.

<a id="Step2SetupyourOpenaiAPIKey"></a>

## Step 2. Set up your Openai API Key

This solution template has only one app that requires setup, GPT-azure.com.

> **NOTE:**  Charges apply to your Openai account according to the [Openai pricing policy](https://openai.com/pricing).

1. Go to [Openai](https://platform.openai.com/account/api-keys), log in and on the **User** menu, click **API Keys**.
2. In the API keys page, click the **Create new secret key** button.

![](../../Resources/Images/Hospitality/Configuring%20Skill%20Templates_1.png)

A secret key is generated.

3. Copy the secret key as you will need it in DRUID.
4. In Druid Portal, on your AI Agent, select solution Hospitality and on the main menu, click **Apps**.
5. Click on the **GPT-azure.com** app. The app configuration page opens.
6. Scroll down to the Variables table and as value for the **key** variable, set up the secret key you copied from Openai. Save the key.

![](../../Resources/Images/Hospitality/Configuring%20Skill%20Templates_2.png)

7. Scroll down and click **Save & Close**.
8. Click the **Publish** button at the top-right corner of the Apps page to publish the connectors.

![](../../Resources/Images/Hospitality/Configuring%20Skill%20Templates_3.png)

<a id="Step3ActivatetheAudioCodeschannel"></a>

## Step 3. Activate the AudioCodes channel

1. In the Druid Portal go to your AI Agent settings. Click the **Channels** tab, and then click **Voice, AudioCodes – VoiceAi Connect**. The channel info section expands.
2. Generate a token by clicking the **Generate** button.

![](../../Resources/Images/Hospitality/Configuring%20Skill%20Templates_4.png)

3. Publish the channel.

![](../../Resources/Images/Hospitality/Configuring%20Skill%20Templates_5.png)

For more information on how to set up the AudioCodes channel, see [Voice Audio Codes Channel](../../Channels/Voice%20Audio%20Codes/Voice%20Audio%20Codes%20Channel.md).

<a id="Step4ActivatetheMSTeamschannel"></a>

## Step 4. Activate the MS Teams channel

On the **Channels** tab, and click **Teams**. The Teams Channel Info section expands.

Activate the Teams channel. To do so, select the Microsoft Teams option that suits your company's Microsoft Office 365 version, agree to the Microsoft terms and statements and click the **Publish** button.

For more information about the Teams channel, see [MS Teams Integration](../../Channels/MS%20Teams/MS%20Teams%20Integration.md).

<a id="Step5SetuptheAIAgentspecialflows"></a>

## Step 5. Set up the AI Agent special flows

Go to the AI Agent settings, Details page and click the **Dialog management** section header. The section expands. Select the following special flows:

| Special Flow | Select |
| --- | --- |
| Welcome flow | first-welcome-flow |
| Intent not found flow | Intent-not-recognized |

![](../../Resources/Images/Hospitality/Configuring%20Skill%20Templates_6.png)

Scroll down and tap on **Use Knowledge Base**, then select the Knowledge base response flow that comes with the solution.

![](../../Resources/Images/Hospitality/Configuring%20Skill%20Templates_7.png)

Scroll down and click **Save & Close**.

<a id="Step6TrainyourAIAgent"></a>

## Step 6. Train your AI Agent

From the **NLU** menu, click **Configurations** and then click the **Intents** tab. Click the **Train** button.

![](../../Resources/Images/Hospitality/Configuring%20Skill%20Templates_8.png)

<a id="Step7AddKBdatasources"></a>

## Step 7. Add KB data sources

You can import your own knowledge base documents or use the provided examples:

- [FAQ – English](<https://druiddocs.file.core.windows.net/docs-shares/Hospitality/FAQ EN.xlsx?sv=2023-01-03&st=2024-08-09T09%3A49%3A39Z&se=2030-08-10T09%3A49%3A00Z&sr=f&sp=r&sig=eTwp%2FfzM95a20r5JsVSsdi13u7uAZGGIXQNahe7Hiiw%3D>)
- [FAQ – Portuguese](<https://druiddocs.file.core.windows.net/docs-shares/Hospitality/FAQ PT.xlsx?sv=2023-01-03&st=2024-08-09T09%3A50%3A07Z&se=2030-08-10T09%3A50%3A00Z&sr=f&sp=r&sig=O71EGbNFXjDXMb6nykVEwdwRWyjdIOiZof%2Bc43D5FC8%3D>).

For information on how to import files, see [File repository data sources](../../Knowledgebase/File%20repository%20data%20sources.md).
