---
title: Enhancing KB Predictions
---


To maximize accuracy and ensure your AI Agent returns the most relevant responses, you can fine-tune prediction behavior at multiple levels. While global Knowledge Base settings apply broadly across all data sources, configuring Advanced Settings at the data source or node/leaf level provides granular control over extractors and trainable elements.

## Granular fine-tuning (data source vs. node/leaf level)

Overriding global settings allows you to adapt extraction and processing parameters to the unique structure of specific files, web paths, or repositories.

### Fine-tuning at the data source level

1. Navigate to the desired data source.
2. Click the **Advanced Settings** tab.

![](<../../.gitbook/assets/DS advanced settings.png>)

3. Modify advanced parameters as needed and save the settings.

### Fine-tuning at the node or leaf level

1. Go to your data source, **Extracted paragraphs**.
2. Choose the Split view.
3. In the tree explorer. click on the desired node, leaf.
4. On the right side, select the **Advanced Settings** tab.

![](<../../.gitbook/assets/leaf settings.png>)

5. Modify advanced parameters as needed and save the settings.

**IMPORTANT!** Modifying **Advanced Settings** at the data source or node level does not automatically trigger an update to the prediction engine. You must **Retrain the data source** for changes to take effect.

## Reset advanced settings

If you want to discard granular customizations made at the data source or node/leaf level and revert them back to your global configuration:

1. Navigate to **Knowledge Base** > **Knowledge Base Settings** > **KB Advanced Settings**.
2. On the left menu, select the specific setting category you want to restore (for example, File Extractors).
3. On the right side of the panel, click the **Reset** button.

![](<../../.gitbook/assets/reset settingsd.png>)

This action removes any local overrides for that setting, realigning all data sources, nodes, and leaves with your global Knowledge Base configuration.

## Enhance predictions with question & answer matching

By default, the Knowledge Base engine matches user queries strictly against the body content (answers) of extracted paragraphs. You can significantly boost retrieval accuracy by reformatting unstructured data into Question & Answer pairs and instructing the engine to evaluate predictions against both elements.

### Step 1: Structure your extracted paragraphs

Open your data source and navigate to the **Extracted paragraphs** tab. Edit your extracted paragraphs to ensure both the title and paragraph fields are populated with clear text. For more information, see [Review and Improve Extracted Paragraphs](<Review and Improve Extracted Paragraphs.md>).

### Step 2: Configure Trainable Elements

1. Navigate to **Knowledge Base** > **Knowledge Base Settings** > **KB Advanced Settings** (or go to the **Advanced Settings** tab of a specific data source).
2. Go to Embeddings > Trainable Elements.
3. Make sure that both **Question** and **Answer** toggles are on.

![](<../../.gitbook/assets/qna toggles.png>)

4. Save your changes.

### Step 3: Retrain the Knowledge Base

Train the KB or select to **Retrain all data sources**.

![](<../../.gitbook/assets/train or retrain.png>)

Once training completes, the KB Engine will evaluate incoming user utterances against both the Question and Answer fields during vector search, delivering higher confidence scores and more precise matches.
