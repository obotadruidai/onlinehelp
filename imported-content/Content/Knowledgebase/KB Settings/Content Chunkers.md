---
layout:
  title:
    visible: false
---

<a id="ContentChunkers"></a>

# Content Chunkers

The Druid KB Engine supports two types of content chunking (article extraction) methods: **Basic** and **LLM**. These options help define how content is divided into chunks for processing, allowing you to customize the level of detail processed from documents.

![](../../Resources/Images/KB/content%20chunkers.png)

<a id="BasicContentChunking"></a>

## <a id="Basic"></a>Basic Content Chunking

This method extracts articles in chunks of 512 tokens (approximately 2,000 characters).

Use this option for simple content processing when you do not require deep semantic understanding. It is ideal for smaller, less complex documents or when speed is a priority over nuanced content interpretation.

To generate additional information for the extracted content using an LLM, turn on the **Enable Augmentation** toggle, then select the **Augmentation Strategy** to use. Augmentation strategies define the generative endpoint and prompt used to generate missing elements.

![](../../Resources/Images/druid%2010.1/enable%20aug.png)

> **Info:** Configure augmentation strategies in **Knowledge Base Settings** > **Advanced** > **Augmentation**. For more information, see [Augmentation.htm](Augmentation.md).

<a id="LLMContentChunking"></a>

## LLM Content Chunking

LLM chunking uses generative AI to perform smart content splitting, focusing on producing more meaningful and contextually relevant chunks. This approach leverages language models to identify and split key pieces of content, improving the relevance of each chunk.

> **Info:** LLM-based chunking is enabled by default to split content into contextually relevant chunks. If the default LLM resource is unavailable, an error is raised. In previous versions, Druid automatically falls back to an alternative model like Azure OpenAI GPT-4o-mini, if it’s configured. If no generative resource is activated on your tenant, Druid defaults to the basic (non-AI) chunking method. Resetting the settings restores LLM chunking using the available resource.

<a id="Addnewchunkers"></a>

## Add new chunkers

To add a new chunker:

1. Click **Add new**.
2. Select the chunker type.
3. Configure the chunker parameters (see details below).
4. Click **Save**.

<a id="ChunkerParameters"></a>

## Chunker Parameters

The table below describes the Chunker parameters.

| Parameter | Description |
| --- | --- |
| Caption | The display name of the content chunker in the UI. Use a descriptive name to distinguish between multiple configurations. |
| Type | Determines the chunking method:   - **Basic** – Splits content into fixed token-size chunks without AI interpretation. - **LLM** – Uses a generative AI model to split content into contextually meaningful chunks. |
| Generative Endpoint | **NOTE:** Available for LLM chunkers only.  Select the generative endpoint the chunker will use to process content. The available options correspond to the endpoints configured in the [Generative Endpoints](Generative%20Endpoints.md) section. |
| Max Tokens | **NOTE:** Available for Basic chunkers only.  Defines the maximum number of tokens per chunk. Controls output length to prevent excessively large chunks  **Info:** Max Tokens cannot exceed the remaining space in the **Model Context Window Size** after accounting for input tokens. |
| Max Lines | **NOTE:** Available for LLM chunkers only.  Limits the number of lines in each chunk, regardless of token count.. Structures the output into a fixed number of lines.  This parameter is specific to the generative model being used. For optimal performance, you should adjust these values based on the capabilities of the selected generative endpoint.  **Info:** If both **Max Tokens (per request)** (in the generative endpoint configuration) and **Max Lines** are set, the model generates up to **Max Tokens (per request)** but also stops at **Max Lines** — whichever limit is reached first.  *Example*: If you use a model with a token limit of 4,096, you might set Max Tokens (per request) to 2,000 and Max Lines to 30 to ensure each chunk is appropriately sized. |
| Keep Table Structure | This option, allows you to exclude tables from LLM chunking and process them with Druid’s proprietary chunking technology. Enabling this option is useful for maintaining the structure and readability of tables in the processed content, ensuring tables are handled more precisely than with LLM-based chunking.  **Info:**  If your documents include structured tables or data that need to be accurately retained, consider enabling this option for better results. |
| Prompt | **NOTE:** Available for LLM chunkers only.  Defines the instructions the model uses to interpret and process the chunking task. You can edit the prompt directly in the text field to customize how the LLM splits content.  The default prompt ensures article/paragraph titles are always extracted in the same language as the source document. If you use a custom prompt, you can add the following rules manually:     ``` - Detect the main language of the document once at the beginning. - All chapter titles MUST be written strictly in the same language as the document text. - Do not translate, do not switch languages, and do not mix languages in chapter titles. - If the document is entirely in English, every chapter title must also be in English. - If the document is entirely in another language, every chapter title must also be in that same language. - You are strictly forbidden to generate titles in a language different from the text. ``` |
