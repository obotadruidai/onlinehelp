---
layout:
  title:
    visible: false
---

<a id="KBGeneralSettings"></a>

# KB General Settings

The KB General Settings let you control how the Knowledge Base interacts with your AI Agent — from the embeddings model used to index your content, to the flows triggered when a match is found, to the score thresholds that determine what counts as a valid result.

To access these settings, go to the Knowledge Base page, click the Knowledge Base Settings tab, and select General from the left menu. The General settings appear by default.

![](../../Resources/Images/KB/general%20settings.png)

<a id="Embeddings"></a>

## Embeddings

Embeddings settings define how your content is transformed into vectors for semantic search. Changes here require retraining all data sources to take effect.

<a id="EmbeddingsProvider"></a>

### Embeddings Provider

Selects the service that generates vector embeddings for your Knowledge Base content.

Three providers are available:

- **Druid** (default). Uses a non-generative Large Language Model (LLM) maintained by DRUID. When selected, you can also choose an Embeddings Model (see below).
- **OpenAI**. Uses OpenAI's text embeddings. Requires entering the API key for your OpenAI account.
- **Microsoft Azure**. Uses Azure OpenAI embeddings. Requires entering the Azure OpenAI embeddings endpoint, deployment name and the API key (Password) for your Azure OpenAI account. Endpoint format: https://{your-resource-name}.openai.azure.com/openai/deployments/{deployment-id}/embeddings?api-version={api-version}.

> **NOTE:** Changing the Embeddings Provider requires a full retrain of all data sources.

<a id="EmbeddingsModel"></a>

### Embeddings Model

> **Info:** Available only when **Embeddings Provider** is set to **Druid**.

An embeddings model transforms text into a vector of numbers (an embedding) that captures semantic meaning, enabling similarity comparisons during search. The following models are available:

- **English**. Optimized for English text, captures semantic meaning in English language inputs.
- **English – score correction**. English embeddings with additional score correction to improve accuracy and relevance of similarity scores.
- **HigherEducation.v1.** Trained on higher education content in English only. Improves accuracy for university-specific queries.
- **MultiAspect**. Enhanced multilingual model with improved cross-language performance and score correction.
- **Multilingual**. Produces embeddings for multiple languages, enabling cross-lingual semantic understanding.
- **Multilingual – score correction**. Multilingual embeddings with score correction, enhancing precision of similarity scores across languages.
- **Paraphrase**. Specializes in identifying semantically similar phrases regardless of wording differences. Processes up to 125 tokens per paragraph. All other models support up to 512 tokens per paragraph.

> **NOTE:** Changing the Embeddings Model requires a full retrain of all data sources.

<a id="Configurations"></a>

## Configurations

Configuration settings control which flows your AI Agent uses when handling Knowledge Base results.

<a id="KnowledgeBaseResponseFlow"></a>

### Knowledge Base Response Flow

The flow the AI Agent executes when a matching answer is found in the Knowledge Base. Select the flow you have configured for delivering Knowledge Base responses (typically imported from the Solution Library).

This setting is required for the Knowledge Base to surface results in conversation.

<a id="IntentRephraseFlow"></a>

### Intent Rephrase Flow

Optional. If selected, the AI Agent runs this flow before searching the Knowledge Base. The flow uses an external service (for example, a GPT-based endpoint) to rephrase the user's input into a form better suited for your AI Agent model.

After the user sends a message, the AI Agent executes the **Intent Rephrase Flow** first, rephrases the utterance, and then uses the result — stored in **[[Intent]].Text** — to search the Knowledge Base.

> **IMPORTANT!** The **Intent Rephrase Flow** runs only when the user sends input while the conversation is in idle mode. Once the user is inside a flow, the **Intent Rephrase Flow** no longer executes and the input is not altered.

<a id="UseKnowledgeBase"></a>

### Use Knowledge Base

Toggle on to allow the AI Agent to search the Knowledge Base when the user's input does not match any existing flow.

When enabled, the AI Agent routes unmatched inputs to the Knowledge Base and uses the Knowledge Base Response Flow to deliver the result.

<a id="SearchInsideAnswers"></a>

### Search Inside Answers

Available for Structured Data sources only.

Toggle on to match user input against both questions and answers in structured data sources (Excel, CSV).

When off, the user's input is matched only against the question column in structured data sources.

<a id="SetResultsThreshold"></a>

### Set Results Threshold

The results threshold settings control the score range the Knowledge Base uses to decide whether a retrieved result is confident enough to return to the user.

<a id="UseAIAgentNLUThresholds"></a>

### Use AI Agent NLU Thresholds

When enabled, the Knowledge Base uses the same thresholds configured on the AI Agent (**NLU** menu > **Configurations** > **Intents** tab > **Thresholds and Parameters** section). This is the default for new AI Agents.

![](../../Resources/Images/KB/set%20slider.png)

Behavior for existing AI Agents depends on whether **Min score threshold** and **Target match score** have values:

- Both values are null. **Use** AI Agent **NLU Thresholds** is enabled, and the slider shows the NLU thresholds. The slider is disabled.
- One value is set. **Use** AI Agent**NLU Thresholds** is disabled. The slider is editable for the parameter that has a value. The empty parameter continues to use the AI Agent NLU threshold.
- Both values are set. **Use** AI Agent**NLU Thresholds** is disabled. Both slider handles are editable.

> **NOTE:** If you re-enable **Use AI Agent NLU Thresholds** after manually setting threshold values, the custom values on the slider will be lost.

To control how the KB evaluates and matches user input, disable **Use AI Agent NLU Thresholds** and adjust the **Min score threshold** and **Target match** score using the slider, ensuring that it aligns with your desired performance thresholds.

<a id="SearchBalance"></a>

## Search Balance

Controls how the Knowledge Base combines two search algorithms — keyword (Text) search and semantic (Vector) search — when retrieving results. You can also add the reranker to refine result quality after the initial retrieval.

The matching score for each result is calculated as:

**Matching Score = (Text Score × Text Weight) + (Vector Score × Vector Weight) + (Reranker Score × Reranker Weight)**

<a id="Vector"></a>

### Vector

The weight assigned to the semantic (Vector) search algorithm. Semantic search matches results based on meaning rather than exact keywords, generally returning more accurate results.

Recommended default: 80%

<a id="Text"></a>

### Text

The weight assigned to the keyword (Text) search algorithm. Keyword search matches exact words and phrases but may return more noise at higher weights.

Recommended default: 20%

<a id="Reranker"></a>

### Reranker

The weight assigned to the reranker, which performs an additional analysis pass on the initial results to improve ranking quality. Set to 0% (or leave null in the Score Calculator) if you do not want to use the reranker.

> **Info:** The values you set on the **Search Balance** slider are synchronized with the **Score Calculator** strategy in **Advanced Settings**. Any change in one is reflected in the other.

After configuring the General Settings, click **Save**.

For settings that affect embedding behavior (Embeddings Provider, Embeddings Model, or Search Inside Answers), use Retrain after saving to apply the changes across all data sources.
