<a id="ImportandSetUptheSolution"></a>

# Import and Set Up the Solution

The KB Toolkit 2 solution provides tools and apps to support advanced testing scenarios, including multi-turn conversations and integration with Azure Cognitive Search and Embeddings. This section will walk you through the steps to import and configure the solution to ensure a smooth setup and operation.

<a id="Step1Importthesolution"></a>

## Step 1. Import the solution

1. Go to the Solutions Library, search for solution **KB Toolkit 2**.

![](../../../Resources/Images/KB%20Toolkit/import%20solution.png)

2. Import the solution following the instructions provided in section [Installing Solution Templates](../../Installing%20Solution%20Templates.md).
3. Wait until the import status shows as “Success.”
4. Once the import is successful, click **Save & Close**.

<a id="Step2Configuretheapps"></a>

## Step 2. Configure the apps

From the **Solution Contents** menu, select **Apps**. The solution includes the following apps:

![](../../../Resources/Images/KB%20Toolkit/apps.png)

| App name | Description | Mandatory |
| --- | --- | --- |
| gpt-agent | Acts as the primary testing agent. | Yes |
| KBToolkit-TargetBot | Handles tests for test cases with multi-turn conversation. | Yes |
| AzureCognitiveSearch | Facilitates tests leveraging Azure Cognitive Search capabilities. | No |
| EmbedingsAzure | Supports advanced testing using Azure Embeddings for exceptional test cases. | No |
| druid-kb2 | Manages connections between business objects and knowledge base (KB) data sources or their elements.  \*Setting up this app is necessary only if you want to enhance KB answers with additional KB metadata. For more information on how to configure the app and use KB Metadata, see [Enhance KB Answers with KB Metadata](../../../Knowledgebase/KB%20Metadata.md). | Yes\* |

<a id="Configurethegptagentapp"></a>

### Configure the gpt-agent app

To configure the **gpt-agent** app, you will need the **base URL** and **API key** for one of the following:

- DRUID’s OpenAI, if you are using the DRUID.LLM service.
- Your Azure OpenAI Chat Completion API.

#### Configuring the gpt-agent App for DRUID’s OpenAI

1. Navigate to **Administration** > **Druid Services** to retrieve the required details.
2. Copy the claim of the **Druid.LLM** resource.
3. Copy the corresponding token, which will serve as the API key.

![](../../../Resources/Images/KB%20Toolkit/druid%20details.png)

4. Go to **Solution Contents** > **Apps** and click on the **gpt-agent** app.
5. In the **Base URL** field, paste the URL you copied earlier.

![](../../../Resources/Images/KB%20Toolkit/druid%20url.png)

6. In the Variables table, set the **token** value to the copied token.

![](../../../Resources/Images/KB%20Toolkit/druid%20token.png)

7. Click **Save & Close** to save the configuration and exit the page.

#### App configuration when using your Azure OpenAI subscription

1. Go to **Solution Contents** > **Apps** and click on the **gpt-agent** app.
2. In the **Base URL** field, enter the base URL of your Azure OpenAI chat completion API in the following format: *https://{your-resource-name}.openai.azure.com/openai/deployments/{your\_model\_name}/chat/completions?api-version={api-version}**-preview*.

*Api version example*: api-version=2024-06-01

![](../../../Resources/Images/KB%20Toolkit/base%20url%20your%20azure.png)

3. In the Variables section, set the **key** value to your Azure OpenAI key.

![](../../../Resources/Images/KB%20Toolkit/your%20key.png)

4. Click **Save & Close** to save the configuration and exit the page.

<a id="ConfiguretheKBToolkitTargetBotapp"></a>

### Configure the KBToolkit-TargetBot app

To configure the **KBToolkit-TargetBot** app, follow these steps:

1. Get the connection details for the VoiceText channel, and the AI Agent id:

- Go to the AI Agent details page and click on the **Channels** tab.
- Click on the **VoiceText** channel.
- Copy the **AuthorizeURL** and **BotURL**.

![](../../../Resources/Images/KB%20Toolkit/voicetext%20channel.png)

- Copy the AI Agent id from the browser:

![](../../../Resources/Images/KB%20Toolkit/bot%20id.png)

2. Select the KB Toolkit solution, then go to **Solution Contents** > **Apps** and click on the **KBToolkit-TargetBot** app.
3. In the Variables table, enter the AuthorizeURL and BotURL values that you copied from the VoiceText channel. Also enter the BotId you got at step 1.

![](../../../Resources/Images/KB%20Toolkit/target%20bot%20variables.png)

<a id="Step3Publishtheintegrations"></a>

## Step 3. Publish the integrations

To ensure the apps are operational, you must publish the integrations. Click the **Publish** button to complete this step.

![](../../../Resources/Images/KB%20Toolkit/publish%20integrations.png)

Next, you need to create the KB Settings.

<a id="Step4TraintheAIAgent"></a>

## Step 4. Train the AI Agent

To train the AI Agent, go to **NLU** > **Configurations**. Click the **Intents** tab and click the **Train** button.

![](../../../Resources/Images/KB%20Toolkit/train%20the%20bot.png)
