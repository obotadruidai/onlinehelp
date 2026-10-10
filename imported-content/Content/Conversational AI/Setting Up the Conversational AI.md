---
layout:
  title:
    visible: false
---

<a id="SettingUptheAIAgentConversationalAI"></a>

# Setting Up the AI Agent Conversational AI

To set up the AI Agent Conversational AI, select the AI Agent and from the **NLU** menu, click **Configurations**.The NLU Configuration page opens on the **General** tab.

Click the Providers section header. Based on the model you want to use, from the **Provider** drop-down, select the NLP provider:

- **DRUID (built-in)** - DRUID proprietary NLP is set by default.
  DRUID proprietary NLP technology focuses on interpreting the user's intent to provide information contextually based on their behavior and preferences.
- **NeuralSpace** - Use the NeuralSpace NLP.
- **None** - Use the Knowledge Base model. The AI Agent will predict only within the Knowledge Base.

![](../Resources/Images/NLU/select%20provider.png)

Click the **Save** button.

> **NOTE:** The settings in the NLP Configurations page will overwrite the settings done on the AI Agent details page.

<a id="UsingtheDRUIDNLP"></a>

## Using the DRUID NLP

DRUID NLP is comprised of all flows and QnAs. The default NLP interpreter is **Druid (built-in)**, DRUID proprietary NLP.

![](../Resources/Images/NLU/druid%20built%20in.png)

To optimize the NLP interpreter, you need to set the AI Agent NLP thresholds and parameters and optionally define additional stop words as described in teh follwoing sections.

<a id="SetThresholdsandNLPParameters"></a>

## Set Thresholds and NLP Parameters

Click on the **Intents** tab, then click the Thresholds and parameters section header. The section expands.

To set the thresholds for matching utterance, on the thresholds slider, slide the thresholds to the left / right.

![](../Resources/Images/NLU/entity%20thresholds.png)

The table below provides the description of the thresholds used for matching utterance.

| Entity threshold | Description |
| --- | --- |
| Min match score | The minimum threshold for matching utterance. A matching score below the minimum threshold does not trigger any flows.  Recommended value: **30**. |
| Target match score | The target threshold for matching utterance. A matching score above the target score threshold is a high match and the AI Agent will provide the user with the relevant flow.  A matching score between the **MinScoreThreshold** and the **TargetMatchScore** is a low match and the AI Agent will provide the user with a flow which might not be the most relevant one.  Recommended value: **60**. |

To fine-tune the AI Agent NLP training model, in the Parameters table, add special NLP parameters. For more information on these parameters, see [NLP Special Parameters](NLP%20Special%20Parameters.md). The NLP parameters for Stop Words removal appear in the parameters table by default.

To add a parameter in the table click the Add icon (![](../Resources/Images/NLU/add%20icon.png)). A new line appears in the table. From the drop-downs, select the parameter, select the value and click the save icon.

![](../Resources/Images/NLU/select%20parameter.png)

If you want to add NLP experimental parameters, tap on **Add experimental parameters** and in the table that appears, add the desired parameters. For more information on these parameters, see [NLP Special Parameters](NLP%20Special%20Parameters.md).

Test the NLP model. Write the phrase you want to test (the intent), then click on **Test** and choose the corresponding language. The Conversational AI will return the matching flow (as it would do during a conversation), together with the matching score for that intent. It is a feedback tool for improving the NLP model.

> **NOTE:** The testing functionality only works for trained models!

Train the NLP model by clicking the **Train** button The training model includes ALL training phrases defined on ALL flows associated with the respective AI Agent.

![](../Resources/Images/NLU/train%20model.png)

After training the NLP model, the following information is available in the Train area:

- **Train started on** - the date and time when the NLP model training started. It has the following format: YYYY-MM-DD HH:MM:SS.
- **Trained on** – the date and time when the model was last trained on. It has the following format: x days ago (YYYY-MM-DD HH:MM:SS).
- **Duration** - how much time it took DRUID to train the AI Agent NLP model. It has the following format: HH:MM:SS.
- **Status** – the status of the model training (Trained / Untrained).
- **Download train rrrors** – Downloads (in your default Download folder) a JSON file which contains the errors occurred (if any) during the last NLP model training.
- **Download train log** - Downloads (in your default Download folder) a JSON file which contains comprehensive training phrases data: status per training phrases, score for each utterance, etc.

<a id="Addstopwords"></a>

## Add stop words

Words that are filtered out before the natural language data (text) is processed. While AI Agents already have a [predefined list of stop words per language](StopWords/Druid_Default_StopWords.md) (the most common words used in a language), you can optimize the training model by manually adding new stop words.

For example, if you have a bidding AI Agent, you might want to exclude the word “bid” as the occurrence percentage for this word might be very high.

To add stop words, in the NLU Configurations page, **Intents** tab, click the **Stop words** section header. The section expands.

![](../Resources/Images/NLU/stop%20words%20section.png)

By default, the NLP parameters for stop words removed are set to true (the toggle buttons are on). To disable the stop words removal, toggle off these buttons and the specific NLP parameter(s) is automatically set to "false".

If your AI Agent has multiple languages, you need to add stop word for each language. Select the language and enter the stop word in that language. After you add the stop words for all AI Agent languages, click the **Save** button.

![](../Resources/Images/NLU/add%20stop%20words.png)

You can download the predefined list of stop words per language by clicking on the link below the stop words defined per language.

<a id="SetEntityThresholds"></a>

## Set Entity Thresholds

Named Entity Recognition (NER) allows the AI Agent to extract entities directly from the user intent. The thresholds for

In the NLU Configurations page, click the **Entities** tab and on the entity thresholds slider, slide the thresholds to the left / right.

![](../Resources/Images/NLU/entity%20slider.png)

The table below provides the description of the thresholds used for matching entities.

| Entity threshold | Description |
| --- | --- |
| Entity min match score | The minimum threshold for matching NER entities. The AI Agent will match the appropriate indexed value based on the matching score in a similar way as for the MinScoreThreshold.  Recommended value: **30**. |
| Entity target match score | The target threshold for matching NER entities. The AI Agent will match the appropriate indexed value based on the matching score in a similar way as for the TargetMatchScore.  Recommended value: **60**. |

Click the **Save** button to save the settings.

<a id="Definekeywordsforsentimentanalysis"></a>

## Define keywords for sentiment analysis

Sentiment analysis is done based on the provided positive and negative keywords. Sentiment analysis is not done automatically. authors have to design their flow step(s) to capture user input and call the internal action **GetWeightedSentiment**, which will analyze the user input captured in Input mapping and return a score.

In the NLU Configurations page, click the **Sentiment** tab. Enter positive and negative words per AI Agent language and click the **Save** button to save the settings.

> **Info:** The current sentiment analysis feature is an intermediary version. Semantic NLU sentiment analysis will be available soon.

#### Enable language detection

DRUID is capable of detecting any language change in the conversation prior triggering the **Intent not found** flow, covering the cases when the user types something in another language than the default language of the AI Agent. It does not include the cases when the user changes the conversation language using the snippet's Language option.

> **NOTE:** The user can change the current language in conversation in either the idle state, or inside a flow. In the second situation, the current flow gets canceled.

To enable language detection, do the following steps:

1. In the NLU Configurations page, click on the Intents tab, click the **Dialogue management** section and select the **Language changed flow** to be triggered when language change is detected in the conversation.
   Save the settings.
2. Click on the **Language Detection** tab.
3. Tap on **Language Detection**. The **Threshold** field becomes editable.
4. In the **Threshold** field, enter a value (we recommend setting the threshold to 90). Whenever the threshold is reached, the selected **Language Changed Flow** will be triggered.
> **NOTE:** Only the texts that are detected in another language with a probability greater than the threshold will be taken into consideration.

![](../Resources/Images/NLU/language%20detection.png)

5. Save the AI Agent.

You can test user says to see the **Predicted language** and the **Confidence** (the score of the predicted language). This is particularly useful for debugging purposes to check why language detection was not done on user says or why the **Language changed flow** was not triggered.

![](../Resources/Images/druid%205.11/test%20predict%20language.png)

<a id="UsingtheNeuralSpaceNLP"></a>

## Using the NeuralSpace NLP

#### Prerequisite

- You should have an activated account on the [NeuralSpace Platform](https://platform.neuralspace.ai/#/auth/signup).

#### Set up the NeuralSpace NLP

In the NLU Configurations page, **General** tab, click the Providers section header and from the **Provider** drop-down, select **NeuralSpace**.

![](../Resources/Images/NLU/neuralspace%20provider.png)

Click on the **Intents** tab, then click the Thresholds and Parameters section header. In the Parameters table, add the parameters described in the table below.

| Parameter | Description |
| --- | --- |
| NeuralSpace.AuthorizationToken | The NeuralSpace Platform authentication token. To get the authentication token, log into the NeuralSpace Platform and click the **Copy Auth Token** button at the top-right corner of the Dashboard.  ![](../Resources/Images/AI/neuralspace%20token.png) |
| NeuralSpace.PlatformUrl | The URL of the NeuralSpace Platform if hosted on premises. The URL should be accessible from the Internet. |

Click the **Save** button to save the settings.

<a id="UsingtheKnowledgeBasemodel"></a>

## Using the Knowledge Base model

By default, when the Knowledge Base is used on the AI Agent , it will search through the Knowledge Base when the user input does not match with any of the existing flows.

To set the AI Agent to predict only within the Knowledge Base, in the NLU Configurations page, **General** tab, click the Providers section header and from the **Provider** drop-down, select **None**.

![](../Resources/Images/NLU/none%20provider.png)

Click the **Save** button, then click the **Intents** tab and the Dialogue management section header.

Scroll down and tap on **Use Knowledge Base**.

![](../Resources/Images/NLU/use%20kb%20model.png)

Click the **Save** button to save the settings.

## Related Topics

- [Defining the Intent](../4_Flows/Defining%20the%20Intent.md)
- [Knowledge Base](../Knowledgebase/Knowledgebase.md)
- [NLP Special Parameters](NLP%20Special%20Parameters.md)
