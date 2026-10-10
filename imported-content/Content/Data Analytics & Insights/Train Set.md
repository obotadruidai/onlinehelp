<a id="EvaluateTrainPhrases"></a>

# Evaluate Train Phrases

The training model includes ALL training phrases defined on all flows associated with the respective AI Agent. The Train Set is the actual sample data used to train the AI Agent NLP model. The model uses the data to see and learn.

The Train Set feature (**Train Set** tab) enables you to:

- [Evaluate the AI Agent training model](#Evaluating_the_bot_training_model).
- [Evaluate the child models of a parent flow](#Evaluate_child_models).
- [Test a train phrase](#Testing_utterance).
- [View the evaluation details of a specific train phrase](#Viewing_utterance_evaluation_details).
- [Download the AI Agent train model logs](#Downloading_bot_train_model_log).

<a id="EvaluatetheAIAgenttrainingmodel"></a>

## <a id="Evaluating_the_bot_training_model"></a>Evaluate the AI Agent training model

> **NOTE:** The evaluation metrics are using trained data and there might be new settings not included. Check the last train date and train the AI Agent model by clicking the **Train** button.

The Train Set page provides you with information from the TrainLog file (with matching percentage for each training phrase). You can check the general metrics of the AI Agent training model and the general metrics per flow.

![](../Resources/Images/Evaluating%20Bot%20Training%20Model/Train%20Set.png)

<a id="Testatrainphraseutterance"></a>

## <a id="Testing_utterance"></a>Test a train phrase (utterance)

To test a phrase, in the **Test** field, enter the phase, click on the **Test** button and select the language:

![](../Resources/Images/Evaluating%20Bot%20Training%20Model/Train%20Set_1.png)

If testing a phrase (intent) returns no matches found, you can further fine-tune the model using  [../Conversational%20AI/Natural%20Language%20Processing.md](../Conversational%20AI/Natural%20Language%20Processing.md)[NLP](../Conversational%20AI/Natural%20Language%20Processing.md) and [NER](../Conversational%20AI/Named%20Entity%20Recognition%20NER.md) settings.

<a id="Viewutteranceevaluationdetails"></a>

## <a id="Viewing_utterance_evaluation_details"></a>View utterance evaluation details

To view the evaluation details of a flow, in the table, click on the desired flow. Below the flow the utterances are listed together with their matching status, the top two matched flows (if DRUID matched the utterance on multiple flows or if the utterance was matched to a flow (or flows) other than the expected one) and their matching score.

![](../Resources/Images/Evaluating%20Bot%20Training%20Model/Train%20Set_2.png)

The color of the intents provides you with valuable information, as follows:

- Black. The system matches the utterance (training phrase) on a single, corresponding flow. However, you should check the score to see if the phrase is strong enough.
- Red. The system matches that utterance with other flow than the one it is defined on (wrong match).
- Orange. The system matches the utterance (training phrase) on multiple flows.

If you want to edit an utterance click the dots displayed inline with the utterance and click **Edit**.

![](../Resources/Images/Evaluating%20Bot%20Training%20Model/Train%20Set_3.png)

The Add to Train Set page appears that allows you to edit the utterance. You can also improve the train set by editing / deleting training phrases from the expected flow or from the top matched flows.

![](../Resources/Images/Evaluating%20Bot%20Training%20Model/edit%20utterance.png)

Edit the desired training phrase and click the **Train** button to train the AI Agent with the new training phrase.

![](../Resources/Images/Evaluating%20Bot%20Training%20Model/train%20bot%20train%20set.png)

> **Info:**  If you selected **Enable auto train** on the AI Agent (AI Agent details page, NLP section, there is no need to click the **Train** button.

<a id="Evaluatechildmodels"></a>

## <a id="Evaluate_child_models"></a>Evaluate child models

For DRUID version 1.73 and higher you can evaluate the NLP sub-model of parent flows. To do so, identify the parent flow whose NLP sub-model you want to evaluate and in the Child Intent column, click the **Child model** icon. In line with the parent flow, two labels are displayed: Error (in red) and Accuracy (in green).

![](../Resources/Images/Evaluating%20Bot%20Training%20Model/child%20model%20icon.png)

The NLP model of the parent flow appears.

![](../Resources/Images/Evaluating%20Bot%20Training%20Model/parent%20submodel.png)

> **NOTE:** The [NLP parameters](../Conversational%20AI/Setting%20Up%20the%20Conversational%20AI%20%28DRUID%20versions%20prior%20to%205.15%29.md) set on the AI Agent apply to the AI Agent model and to child models.

You can evaluate child models similar to evaluating AI Agent training phrases:

- Test the child model understanding.
- View the evaluation details of a specific train phrase.
- Understand why the NLP sub-model associated an utterance to a specific child intent.
- Add to Test set.

![](../Resources/Images/Evaluating%20Bot%20Training%20Model/detailed%20child%20model.png)

> **IMPORTANT!** For child intents, if the TargetMatchScore (the target threshold for matching utterance) is not reached, DRUID does not trigger IntentNotRecognized.

To go back to the AI Agent model, at the top-left side of the Evaluation page (above the test child model understanding area), click **Back to AI Agent Model**.

<a id="DownloadAIAgenttrainmodellogs"></a>

## <a id="Downloading_bot_train_model_log"></a>Download AI Agent train model logs

![](../Resources/Images/Evaluating%20Bot%20Training%20Model/Train%20Set_5.png)

- **Download** – Downloads the AI Agent training model in Excel format. It is the training model visualized in the Train Set page.  For information of the metrics you can find in the train set log, see [Train Status](Train%20Status.md).
- **DownloadTrainLog** - Downloads (in your default Download folder) a JSON file, which contains comprehensive training phrases data: status per training phrases, score for each utterance, etc.
- **DownloadTrainErrors** – Downloads (in your default Download folder) a JSON file, which contains the errors occurred (if any) during the last NLP model training.

## Related Topics

- [Annotation Tool](Annotation/Annotation%20Tool.md)
- [Explainability and Utterances Annotation](../Governance%20%26%20Security/Explainability%20and%20Utterances%20Annotation.md)
- [Setting Up the AI Agent Conversational AI (DRUID versions prior to 5.15)](../Conversational%20AI/Setting%20Up%20the%20Conversational%20AI%20%28DRUID%20versions%20prior%20to%205.15%29.md)
