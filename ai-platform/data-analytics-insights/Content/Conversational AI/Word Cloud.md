---
title: Evaluate Words Used in Multiple Intents
---


The Druid Portal enables you to see for each AI Agent an image composed of words used in the training model.

The WordCloud page gives you an overview of the training model on a word level. The size of each word indicates its frequency throughout the entire NLP model / test phrase set.

This tool helps you identify the words that appear frequently and might affect the ML model:

1. On the AI Agent **NLU** menu, click **Evaluation**.
2. Click on the **WordCloud** tab.
3. Select the **Data Set** (Training Set or Test set).
4. From the **Model** field, select the model you want to evaluate (either the AI Agent model or a parent / child model).
5. Click the **Refresh** button and click the WordCloud section header.

![](<../../.gitbook/assets/Word Cloud.png>)

The bigger a word is in the image; the higher are the chances that it is a candidate for stop words.

Once you identify such words, you have two options:

* [Mark the words as stop words](<Word Cloud.md#Mark_the_words_as_stop_words>).
* [Change flow utterance](<Word Cloud.md#Change_flow_utterance>).

## Mark the words as stop words <a href="#mark_the_words_as_stop_words" id="mark_the_words_as_stop_words"></a>

To mark words as stop words, follow these steps:

1. On the **NLU** menu, click **Configurations**.
2. Click on the **Intents** tab, then click on the Stop words section header.
3. Enter the words identified in WordCloud.
4. Click the **Save** button to save the changes.
5. Click the **Train** button to train the AI Agent.

![](<../../.gitbook/assets/Word Cloud_1.png>)

If you go to **Evaluation** > **WordCloud** and do not select the **ShowStopWords** check box, the image will no longer show the words you’ve marked as stop words.

## Change flow utterance <a href="#change_flow_utterance" id="change_flow_utterance"></a>

Scroll-down to the Report section and check the word: on how many flows and utterances it appears.

![](<../../.gitbook/assets/Word Cloud_2.png>)

To view which flows contain the word, click on the word.

![](<../../.gitbook/assets/Word Cloud_3.png>)

To view the utterances that contain the word on a specific flow, click the arrow in front of the flow.

![](<../../.gitbook/assets/Word Cloud_4.png>)

If you want to edit a specific utterance, click on it. The Flow Details page appears by default on the Training Phrases.

![](<../../.gitbook/assets/Word Cloud_5.png>)

After you edit the flow utterance, click the **Train Set** tab and click the **Train** button to train the AI Agent with the new training phrase.

![](<../../.gitbook/assets/train bot train set.png>)

{% hint style="info" %}
**Info:** If you selected **Enable auto train** on the AI Agent (AI Agent details page, NLP section, there is no need to click the **Train** button.
{% endhint %}

## Related Topics

* [Defining the Intent](https://druidai.gitbook.io/druid-ai-docs/ai-platform/build-ai-agents/authoring-tools/flows/conversational-flows/defining-the-intent)
* [Setting Up the AI Agent Conversational AI (DRUID versions prior to 5.15)](https://druidai.gitbook.io/druid-ai-docs/ai-platform/build-ai-agents/authoring-tools/conversational-ai/setting-up-the-conversational-ai-druid-versions-prior-to-5.15)
