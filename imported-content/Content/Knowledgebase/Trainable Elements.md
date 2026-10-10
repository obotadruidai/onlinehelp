---
layout:
  title:
    visible: false
---

<a id="TrainableElements"></a>

# Trainable Elements

Trainable Elements define which parts of an article —question, title, short description, and/or answer— the KB Engine uses for predictions from unstructured data sources. These sources include structured documents added inside the data source.

Trainable Elements apply only to unstructured data sources, such as the web, File Repository, SharePoint, Shared Drive, and custom data sources.

You can choose one or multiple from the following options:

| Option | Description | Notes |
| --- | --- | --- |
| Question | Use the question and title for predictions. | Starting with Druid 7.10, new AI Agents use both the question and answer for predictions by default. Existing AI Agents continue to use only the answer ("trainableElements": null) until you update the setting. |
| Answer | Use the short description and answer for predictions. |  |
| Train generated summary | Applicable when using the LLM content chunker. When processing a document paragraph, the LLM generates a summary to be indexed, enhancing prediction accuracy. | Available starting with Druid version 9.12 at global and data source level and with 9.13 at node/leaf level. While these options may increase chunking execution time, they ensure higher quality matching at prediction time.  **IMPORTANT!** It requires setting the **SystemPromptGenerateSummary** to **true** (**Advanced Settings JSON** field under the **ContentChunkerLlmOptions** feature flag), otherwise the summary will not be generated.  To review generated questions and summaries, create a dedicated view and add it to a workspace. |
| Train generated questions | Applicable when using the LLM content chunker. When processing a document paragraph, the LLM generates the number of additional questions specified in the **Generated questions number for train** field |  |

You can apply these settings at three different levels of granularity:

- **Global level**: Go to Knowledge Base Settings > Advanced Settings > Trainable Elements. Changes here apply to all unstructured data sources in the KB.
- **Data source level**: Navigate to a specific data source and click the **Advanced Settings** tab. This allows you to prioritize questions for one source while using answers for another.
- **Node/Leaf level**: In the file explorer/tree, select a specific folder or file. Click the Advanced Settings tab on the right to override settings for just that specific piece of content.
