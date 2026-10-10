<a id="UsingMachineTranslation"></a>

# Using Machine Translation

AI Agents built on the Druid AI Platform can seamlessly handle conversations in over 100 languages by integrating with machine translation services like SDL Machine Translation Cloud, Azure Translator, or a chosen Large Language Model (LLM).

This functionality eliminates the need for manual translation of AI Agent content and conversation flows, saving effort when your agent encounters user queries in languages other than its default. You author the agent in one language (e.g., English), and the machine translation service automatically translates user input, messages, and even buttons in real time.

> **Info:** Machine translation services generate additional costs. Contact the [Druid Support Team](mailto:support@druidai.com) for more information.

<a id="TranslationOptionsConversationTimevsAuthoringTime"></a>

## Translation Options: Conversation Time vs. Authoring Time

By understanding the distinctions between Conversation Time Translation and Authoring Time Translation, users can effectively optimize translation costs and streamline localization efforts. Conversation Time Translation occurs during conversations when language changes are detected (the **[[ChatUser]].Language** is different from the AI Agent authoring languages), while Authoring Time Translation enables bulk translation of AI Agent flows during authoring, reducing translation expenses. Selecting both options allows dynamic switching between real-time machine translation and Druid NLP based on language changes during conversations.

Imagine that you have an agent authored in various languages hosted in an online shop and you need the agent to be always active. Using the conversation time translation in this scenario leads to high costs for having the messages translated in real-time; for each message translation, the agent calls the machine translation service. Translating the agent at authoring time is more cost-effective, enabling it to use NLP for the authoring languages instead of calling the machine translation service.

Understanding the two primary translation options can help you manage costs and efficiency:

| Feature | Conversation Time Translation | Authoring Time Translation (SDL only) |
| --- | --- | --- |
| When it Occurs | Real-time, during the chat, when a new language is detected. | Bulk translation of flows during the authoring process. |
| Provider | SDL, Azure, LLM, or eTranslation | SDL (all environments) or Azure Document Translation (hybrid/on-premise). |
| DRUID calls the Machine Translation Cloud service | Every time a message is written in the chat | When authoring the AI Agent (flows configuration) |
| Enables AI Agent translation in bulk | No | Yes |
| Translation Cost Structure | Per message | Per flow authored element |
| Customize message(s) translation | No | Yes |
| Voice AI Agents using machine translation | Yes | Yes |

> **Info:** Using Authoring Time Translation is typically more cost-effective for AI Agents with high traffic in specific languages. The translated content is stored, and the AI Agent uses its internal Natural Language Processing (NLP) for those languages instead of calling an external translation service for every message.

<a id="SetupmachinetranslationontheAIAgent"></a>

## Set up machine translation on the AI Agent

To enable and configure a translation provider:

1. Navigate to the AI Agent settings, **Details** tab.
2. Click the **Languages** section header.
3. Select **Enable Machine Translation**.

![](../Resources/Images/Bots/machine%20translation.png)

4. Turn on the toggle next to your desired translation provider: **Use LLM Translation**, **Azure translator (Cognitive Services)**, **SDL Machine Translation**, or **Use eTranslation**.
5. Provide the specific configuration details for the chosen provider. Refer to the subsequent sections for specific guidance.
6. Turn on the **Language Detection** toggle to provide the AI Agent to detect and adapt to user language changes in real time.
   For more information, see [Enable language change detection](#Enable_language_change_detection).
7. Click **Save** at the bottom of the page.

<a id="UseLLMmachinetranslation"></a>

## <a id="Use"></a>Use LLM machine translation

> **IMPORTANT!** LLM machine translation is available **only for conversation time translation**.

Before you start, make sure you have an LLM resource set up in the Druid Portal. For more information, see [Create LLM Resources](../Governance%20%26%20Security/LLM%20Resource%20Management%20and%20Governance.md).

To use LLM machine translation, follow these steps:

1. Turn on the **Use LLM Translation** toggle.

![](../Resources/Images/druid%209.1/llm%20translation.png)

2. From the **Endpoint Type** field, select one of the following options:

- **Druid** if you have an LLM subscription with Druid.
- **My resource** if you are using your own generative endpoint.

3. Select the **Model Name**. In the dropdown, you will see all your resources created in **Administration** > **LLM Resources**.

![](../Resources/Images/druid%209.11/llm%20translation.png)

4. The **Api Type** field appears dynamically in Druid 9.19 and higher when an Azure OpenAI model is selected (e.g., AzureOpenAi/gpt-4o-mini). Select one of the following:

- **Responses**: Recommended for Azure OpenAI models. This is the preferred API for Azure OpenAI models, enabling better performance and more intelligent interactions.
- **Chat Completions (Legacy)**: Use this for backward compatibility with existing configurations. Note that this endpoint is now considered legacy.

![](../Resources/Images/Bots/machien%20translation.png)

> **Info:** For other providers, the platform defaults to the standard completion settings compatible with those models.

5. For both prompts, click the **Set default** button. The default Druid prompts will be automatically filled in.
> **Info:** You can experiment with the prompts, provided their **JSON structure remains unchanged**. In an upcoming release, the prompts will become non-editable.

6. Click **Save**.

<a id="UseAzureTranslatorservices"></a>

## Use Azure Translator services

To use Azure Translator, turn on the **Azure translator (Cognitive Services)** toggle.

<a id="InitialConfiguration"></a>

### Initial Configuration

Provide the following details:

- **Azure translator region**: The Resource Region you set when creating your Azure Translator project.
- **Azure translator key**: The authentication key you receive after setting up your Azure Translator resource in the Azure portal.

<a id="UseCustomDictionaries"></a>

### Use Custom Dictionaries

Custom dictionaries enhance translation accuracy by providing user-defined translations for specific terminology, ensuring consistency with your branding.

> **NOTE:** Custom dictionaries are available in DRUID 8.16 and higher.

In your Azure Translator project, publish the models associated with your custom dictionaries. See the [Microsoft Custom Translator Quickstart](https://learn.microsoft.com/en-us/azure/ai-services/translator/custom-translator/quickstart) guide for instructions.

Copy the Category ID for each translation model.

![](../Resources/Images/druid%208.16/category_id.png)

In the **Azure Translator custom dictionaries** field, enter a JSON object that maps language pairs to their Category IDs:

- The key is a language pair (source and target codes) separated by a vertical bar (|).
- The value is the Category ID for the relevant translation model.

**Custom translations between English (United States) and Spanish**

```
{
  "en-US|es": "12d31552-1815-483b-b75c-8f40e7484d13-SOCIETY",
  "es|en-US": "12d31552-1815-483b-b75c-8f40e7484d13-HEALTHC"
}
```

![](../Resources/Images/druid%208.16/AZURE%20TRANSLATOR%20SETTINGS.png)

<a id="AzureTranslatorforConversationTimeTranslation"></a>

### Azure Translator for Conversation Time Translation

Turn on the **Conversation time** toggle to use Azure Translator for real-time translation during chat.

#### Cloud Deployment

1. Leave the **Specific languages** field empty.

![](../Resources/Images/Bot%20Advanced%20Settings/azure%20translator.png)

2. To use machine translation during conversations, turn on the **Language Detection** toggle to allow the AI Agent to detect and adapt to user language changes in real time.
   For more information, see [Enable language change detection](#Enable_language_change_detection).
3. Click **Save** The automatic machine translation service from Azure Translator will be activated.

#### On-Premise Deployment

If you use Azure Translator services in an on-premise container:

1. Select the **Use dedicated docker container** checkbox.
2. In the **Container address** field, enter the container's URL.

![](../Resources/Images/Bot%20Advanced%20Settings/conversation%20time_on%20prem%20Translator.png)

3. Leave the **Specific languages** field empty.
4. To use machine translation during conversations, turn on the **Language Detection** toggle to allow the AI Agent to detect and adapt to user language changes in real time.
   For more information, see [Enable language change detection](#Enable_language_change_detection).
5. Click **Save**.

<a id="AzureTranslatorforAuthoringtimetranslation"></a>

### Azure Translator for Authoring time translation

Authoring time translation uses the cloud-based Document Translation feature of Azure Translator. On-premise installations do not support this feature.

> **IMPORTANT!** Authoring time translation does not currently support the Azure Translator installed on premise; you should use the cloud Azure Translator service.

#### Hybrid Deployment (Cloud Service)

Use this option to configure your AI Agent to use the cloud-based Document Translation service for authoring time translation in a hybrid deployment.

##### Prerequisites

- You have an active [Azure account](https://azure.microsoft.com/free/cognitive-services/). If you don't have one, you can [create a free account](https://azure.microsoft.com/free/).
- You need to retrieve your Document Translation endpoint from the Azure portal.

![](../Resources/Images/druid%205.11/document%20translation%20endpoint.png)

For information on how to retrieve the Document Translation endpoint, see [Microsoft documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/translator/document-translation/quickstarts/get-started-with-rest-api?pivots=programming-language-csharp).

- Allow outbound calls from Druid to the Document Translation endpoint.

##### Configuration steps

1. Turn on the **Authoring time** toggle.
2. In the **Document translator endpoint** field, enter the custom domain endpoint of the Document Translation service from the Azure portal.

![](../Resources/Images/Bot%20Advanced%20Settings/azure%20cloud.png)

3. Click **Save**.

#### On-Premise Deployment (Dedicated Containers)

Use this option if you need to use dedicated Azure Blob Storage containers for file handling during translation.

##### Prerequisites

- You have an active [Azure account](https://azure.microsoft.com/free/cognitive-services/). If you don't have one, you can [create a free account](https://azure.microsoft.com/free/).
- You need to retrieve your Document Translation endpoint from the Azure portal.

![](../Resources/Images/druid%205.11/document%20translation%20endpoint.png)

- For information on how to retrieve the Document Translation endpoint, see [Microsoft documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/translator/document-translation/quickstarts/get-started-with-rest-api?pivots=programming-language-csharp).
- You have an Azure Blob Storage account. Create containers in your Azure Blob Storage account as follows:

- **Source container**. This container is where Druid uploads the files (authoring content) for translation.
- **Container for translation**. This container is where the Document Translation takes the files for translation.
- **Target container**. This container is where the Document Translation puts the translated files.
- **Delete container**. This container is where the translated files from the target container are put after deletion. After Druid picks up the translated files, the target container is cleaned up and the files are moved to the delete container.

- You also need to create Shared Access Signature (SAS) tokens for the four containers you created in Azure Blob Storage. When generating the SAS token, make sure that:

- Your source container has designated **read**, **add**, **create** and **write** access.
- Your container for translation has **read** and **list** access.
- Your target container has designated **write** and **list** access.
- Your delete container has designated **read**, **delete** and **list** access.

> **NOTE:** When you generate the Shared Access Signature (SAS) tokens for your containers, copy the URIs as you will need them in the Druid Portal.

- Allow outbound calls from Druid to the Document Translation endpoint and to Azure Blob Storage URIs.

##### Configuration steps

1. Turn on the **Authoring time** toggle.
2. In the **Document translator endpoint** field, enter the custom domain endpoint of the Document Translation service from the Azure portal.
3. Select the **Use dedicated blob containers** checkbox.
4. Enter the Shared Access Signature (SAS) token URIs for your containers in the corresponding fields:

| Field | Description |
| --- | --- |
| Private source container with SAS | The Shared Access Signature of the Source container in URI format. |
| Private destination container with SAS | The Shared Access Signature of the Delete container in URI format. |
| Public source container with SAS | The Shared Access Signature of the Container for translation in URI format. |
| Public destination container with SAS | The Shared Access Signature of the Target container in URI format. |

5. Click the **Save**.

<a id="UseSDLmachinetranslationservices"></a>

## Use SDL machine translation services

1. Turn on the **SDL Machine Translation** toggle.
2. Enter your **SDL Client Id** and **SDL Client Secret**. These are the credentials associated with your SDL account.
3. Choose your desired translation option by turning on the corresponding toggle: **Conversation time** or **Authoring time**.
4. Leave the **Specific languages** field empty.
5. To use machine translation during conversations (Conversation time), turn on the **Language Detection** toggle to allow the AI Agent to detect and adapt to user language changes in real time.
   For more information, see [Enable language change detection](#Enable_language_change_detection).

![](../Resources/Images/Bot%20Advanced%20Settings/sdl%20translator.png)

6. Click **Save**.

<a id="UseeTranslationservices"></a>

## Use eTranslation services

The eTranslation provider gives your AI Agent a specialized, high-quality translation service for real-time, domain-specific communication.

> **NOTE:** The eTranslation provider is available in DRUID 9.3 and higher, and is intended only for conversation time translation.

<a id="Prerequisites"></a>

### Prerequisites

- You have an eTranslation account.

<a id="Configurationsteps"></a>

### Configuration steps

1. Turn on the **Use eTranslation** toggle.
2. Enter the following details:

| Field | Description |
| --- | --- |
| User name | Enter the username provided to you by the eTranslation service administrator. |
| Password | Enter the password associated with the specified username. |
| Domain | Specify the domain (or topic) that best describes the type of content your AI Agent will be translating (e.g., 'Finance', 'General Text', etc.). Selecting the correct domain ensures that the translation model uses appropriate terminology, significantly improving translation quality. |
| Timeout | Specify the maximum time (in seconds) that Druid should wait for a response from the eTranslation service before considering the request a failure. This helps manage flow execution and prevents indefinite waiting times. |

3. Turn on the **Conversation time** toggle.
4. Leave the **Specific languages** field empty.

![](../Resources/Images/druid%209.9/translator%20service%20provider.png)

5. To use machine translation during conversations (Conversation time), turn on the **Language Detection** toggle to allow the AI Agent to detect and adapt to user language changes in real time.
   For more information, see [Enable language change detection](#Enable_language_change_detection).
6. Click **Save**.

<a id="EnableLanguageChangeDetection"></a>

## <a id="Enable_language_change_detection"></a>Enable Language Change Detection

Language change detection equips Druid with the ability to detect when a user starts speaking a language different from the AI Agent default language. This ensures seamless, multilingual communication and occurs before the **Intent not found flow** is triggered.

> **NOTE:**
>
> - Users can change the current language while the AI Agent is idle or within a flow. If the language changes inside an active flow, the flow is canceled.
> - This feature does not apply to cases where users manually change the conversation language using a snippet's **Language** option.

<a id="Prerequisites1"></a>

### Prerequisites

Before enabling detection, complete one of the following:

- Import the **Language detection flow** solution template from the **Solutions Library**.  For more information, see [Language changed flow](../4_Flows/Language%20changed%20flow.md).
- Define a flow to handle the actions triggered when a language change is detected.

<a id="Setuplanguagedetection"></a>

### Set up language detection

Follow these steps to set up language detection:

1. Go to the AI Agent details, **General** tab and click the **Dialogue management** section header.
2. From the **Language changed flow** field, select the flow that should be triggered when a language change is detected. If you imported the solution template, select **Language change**.
3. Click the **Languages** section header.
4. Turn on the **Language detection** toggle. The **Threshold** field becomes editable.
5. In the **Threshold** field, set a value (a threshold of 90 is recommended).
> **NOTE:** Only the texts that are detected in another language with a probability greater than the threshold will be taken into consideration.

![](../Resources/Images/Bot%20Advanced%20Settings/detect%20language.png)

6. Click **Save**.

<a id="Triggerconditions"></a>

### Trigger conditions

The selected **Language changed flow** triggers only when all the following conditions are met simultaneously:

- The detected language (**[[ChatUser]].DetectedLanguage**) is different from the current user language (**[[ChatUser]].Language**).
- The detected language confidence score (**[[ChatUser]].DetectedLanguage.Score**) is higher than the threshold set in the **NLP.Language.Detection.Threshold** parameter.
- The same new language has not been identified as a language change trigger in the last 15 minutes. This prevents continuous re-triggering due to brief or non-committal uses of foreign words.

> **Info:** Use the user says feature to test the **Predicted language** and **Confidence** score. This is useful for debugging to ensure accurate language detection and flow triggering.

## Related Topics

- [Configuring AI Agent Advanced Settings](Configuring%20AI%20Agent%20Advanced%20Settings.md)
