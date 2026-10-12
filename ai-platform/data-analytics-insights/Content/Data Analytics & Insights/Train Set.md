---
title: Evaluate Train Phrases
---


The training model includes ALL training phrases defined on all flows associated with the respective AI Agent. The Train Set is the actual sample data used to train the AI Agent NLP model. The model uses the data to see and learn.

The Train Set feature (**Train Set** tab) enables you to:

* [Evaluate the AI Agent training model](<Train Set.md#Evaluating_the_bot_training_model>).
* [Evaluate the child models of a parent flow](<Train Set.md#Evaluate_child_models>).
* [Test a train phrase](<Train Set.md#Testing_utterance>).
* [View the evaluation details of a specific train phrase](<Train Set.md#Viewing_utterance_evaluation_details>).
* [Download the AI Agent train model logs](<Train Set.md#Downloading_bot_train_model_log>).

## Evaluate the AI Agent training model <a href="#evaluating_the_bot_training_model" id="evaluating_the_bot_training_model"></a>

{% hint style="info" %}
**NOTE:** The evaluation metrics are using trained data and there might be new settings not included. Check the last train date and train the AI Agent model by clicking the **Train** button.
{% endhint %}

The Train Set page provides you with information from the TrainLog file (with matching percentage for each training phrase). You can check the general metrics of the AI Agent training model and the general metrics per flow.

![](<../../.gitbook/assets/Train Set.png>)

## Test a train phrase (utterance) <a href="#testing_utterance" id="testing_utterance"></a>

To test a phrase, in the **Test** field, enter the phase, click on the **Test** button and select the language:

![](<../../.gitbook/assets/Train Set_1.png>)

If testing a phrase (intent) returns no matches found, you can further fine-tune the model using  [../Conversational%20AI/Natural%20Language%20Processing.md](https://druidai.gitbook.io/druid-ai-docs/build-ai-agents/authoring-tools/conversational-ai/natural-language-processing)[NLP](https://druidai.gitbook.io/druid-ai-docs/build-ai-agents/authoring-tools/conversational-ai/natural-language-processing) and [NER](https://druidai.gitbook.io/druid-ai-docs/build-ai-agents/authoring-tools/conversational-ai/named-entity-recognition-ner) settings.

## View utterance evaluation details <a href="#viewing_utterance_evaluation_details" id="viewing_utterance_evaluation_details"></a>

To view the evaluation details of a flow, in the table, click on the desired flow. Below the flow the utterances are listed together with their matching status, the top two matched flows (if DRUID matched the utterance on multiple flows or if the utterance was matched to a flow (or flows) other than the expected one) and their matching score.

![](<../../.gitbook/assets/Train Set_2.png>)

The color of the intents provides you with valuable information, as follows:

* Black. The system matches the utterance (training phrase) on a single, corresponding flow. However, you should check the score to see if the phrase is strong enough.
* Red. The system matches that utterance with other flow than the one it is defined on (wrong match).
* Orange. The system matches the utterance (training phrase) on multiple flows.

If you want to edit an utterance click the dots displayed inline with the utterance and click **Edit**.

![](<../../.gitbook/assets/Train Set_3.png>)

The Add to Train Set page appears that allows you to edit the utterance. You can also improve the train set by editing / deleting training phrases from the expected flow or from the top matched flows.

![](<../../.gitbook/assets/edit utterance.png>)

Edit the desired training phrase and click the **Train** button to train the AI Agent with the new training phrase.

![](<../../.gitbook/assets/train bot train set.png>)

{% hint style="info" %}
**Info:** If you selected **Enable auto train** on the AI Agent (AI Agent details page, NLP section, there is no need to click the **Train** button.
{% endhint %}

## Evaluate child models <a href="#evaluate_child_models" id="evaluate_child_models"></a>

For DRUID version 1.73 and higher you can evaluate the NLP sub-model of parent flows. To do so, identify the parent flow whose NLP sub-model you want to evaluate and in the Child Intent column, click the **Child model** icon. In line with the parent flow, two labels are displayed: Error (in red) and Accuracy (in green).

![](<../../.gitbook/assets/child model icon.png>)

The NLP model of the parent flow appears.

![](<../../.gitbook/assets/parent submodel.png>)

{% hint style="info" %}
**NOTE:** The [NLP parameters](https://druidai.gitbook.io/druid-ai-docs/build-ai-agents/authoring-tools/conversational-ai/setting-up-the-conversational-ai-druid-versions-prior-to-5.15) set on the AI Agent apply to the AI Agent model and to child models.
{% endhint %}

You can evaluate child models similar to evaluating AI Agent training phrases:

* Test the child model understanding.
* View the evaluation details of a specific train phrase.
* Understand why the NLP sub-model associated an utterance to a specific child intent.
* Add to Test set.

![](<../../.gitbook/assets/detailed child model.png>)

{% hint style="warning" %}
**IMPORTANT!** For child intents, if the TargetMatchScore (the target threshold for matching utterance) is not reached, DRUID does not trigger IntentNotRecognized.
{% endhint %}

To go back to the AI Agent model, at the top-left side of the Evaluation page (above the test child model understanding area), click **Back to AI Agent Model**.

## Download AI Agent train model logs <a href="#downloading_bot_train_model_log" id="downloading_bot_train_model_log"></a>

![](<../../.gitbook/assets/Train Set_5.png>)

* **Download** – Downloads the AI Agent training model in Excel format. It is the training model visualized in the Train Set page.  For information of the metrics you can find in the train set log, see [Train Status](<Train Status.md>).
* **DownloadTrainLog** - Downloads (in your default Download folder) a JSON file, which contains comprehensive training phrases data: status per training phrases, score for each utterance, etc.
* **DownloadTrainErrors** – Downloads (in your default Download folder) a JSON file, which contains the errors occurred (if any) during the last NLP model training.

## Related Topics

* [Annotation Tool](<Annotation/Annotation Tool.md>)
* [Explainability and Utterances Annotation](https://druidai.gitbook.io/druid-ai-docs/ai-governance-and-security/observability-and-explainability/explainability-and-utterances-annotation)
* [Setting Up the AI Agent Conversational AI (DRUID versions prior to 5.15)](https://druidai.gitbook.io/druid-ai-docs/build-ai-agents/authoring-tools/conversational-ai/setting-up-the-conversational-ai-druid-versions-prior-to-5.15)
