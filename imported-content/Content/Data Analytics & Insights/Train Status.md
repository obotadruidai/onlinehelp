---
layout:
  title:
    visible: false
---

<a id="TrainStatus"></a>

# Train Status

The Train Log contains comprehensive validation metrics:

- Self-validation Classification Metrics
- Cross Validation Classification Metrics

To view the train status, download the train log and check the metrics.

<a id="SelfvalidationClassificationMetrics"></a>

## Self-validation Classification Metrics

The Druid Portal performs the self-validation with the full train set to evaluate and get the training model’s accuracy metrics.

![](../Resources/Images/Evaluating%20Bot%20Training%20Model/general%20metrics.png)

The table below describes the self-validation general metrics.

| Metric | Description |
| --- | --- |
| Accuracy (A) | The accuracy counts the phrases correctly identified, as count and as percent in total number of tests.  In the **Train Set** tab, each train phrase is used for testing. In **Test Set** tab, each test phrase is used for testing.  **NOTE:**  You might also consider **True Match Single** and **True Match Second** as positive tests because at run time the AI Agent will present the user the intents found and ask for confirmation.  Accuracy = True Match / Count All |
| Error (E) | The Error counts the phrases for which the intent was not identified (Unknown) or was false identified (different from the known expected).  In the **Train Set** tab, the expected intent is the intent where the phrases is set. For the Test Set tab, the authors provide the expected intent for each train phrase. |
| True match (TM) | The True Match counts all the phrases where the expected intent is the expected one. The higher the value, the better. In **Train Set**, the expected intent is the flow to which the phrase belongs.  In **Test Set**, the authors provide the expected intent together with the phrase. |
| True match single | The True Match counts all the phrases where there is a single intent identified and is the expected one. The higher the value, the better. In **Train Set**, the expected intent is the flow to which the phrase belongs.  In **Test Set**, the authors provide the expected intent together with the phrase. |
| True match first (TP1) | There might be more intents identified for a phrase, with different confidence scores. The True Match Single counts the phrases for which there are multiple intents identified, and the expected intent has the highest score. |
| True match second (TP2) | There might be more intents identified for a phrase, with different confidence scores. The True Match Single counts the phrases for which there are multiple intents identified, and the expected intent has the second highest score. |
| False match (FM) | The False Match counts all phrases where an identified intent is different from the expected one. The lower the value, the better. In **Train Set**, the expected intent is the flow to which the phrase belongs.  In **Test Set**, the authors provide the expected intent together with the phrase. |
| True unknown (TU) | The True Unknown counts all the phrases with no intent identified and this was expected. **NOTE:** This metric applies only in **Test Set**. |
| False unknown (FU) | False Unknown counts the phrases where the expected intent is not found. In the **Train Set**, you should have **False Unknown = 0**.  In the **Test Set**, you can specify for each phrase the expected intent or leave empty when you expect not to find an intent. It is a good practice to include in your Test Set phrases where you do not expect an intent.  Unknown intents are counted as False Unknown or True Unknown, based on the above rule. |
| Count All | The number of phrases included in the test. For the **Train Set** counts all training phrases from all the flows.  In **Test Set**, it counts all the test phrases. |

<a id="CrossValidationClassificationMetrics"></a>

## Cross Validation Classification Metrics

The Druid Portal performs the cross validation with a part of the train set to evaluate and get the training model’s accuracy metrics.

The table below describes the cross-validation metrics.

| Metric | Description |
| --- | --- |
| Micro accuracy average | The micro-average is the fraction of instances predicted correctly across all classes. It can be more useful than macro-average if class imbalance is suspected (i.e. one class has many more instances than the rest). |
| Micro accuracies standard deviation |  |
| Micro accuracies confidence interval 95 |  |
| Macro accuracy average | The average accuracy at the class level. The accuracy for each class is computed and the macro-accuracy is the average of these accuracies. It gives the same weight to each class regardless the number of class instances contained in the data set. |
| Macro accuracies standard deviation |  |
| Macro accuracies confidence interval 95 |  |
| Log loss average | Measures the performance of a classifier with respect to how much the predicted probabilities diverge from the true class label. A lower value indicates a better model. The perfect model predicts a probability of 1 for the true class and will have a log-loss of 0. |
| Log loss standard deviation |  |
| Log loss confidence interval 95 |  |
| Log loss reduction average | The relative log-loss or reduction in information gain (a.k.a. RIG). It gives a measure of how much a model improves on a model that gives random predictions. A log-loss reduction closer to 1 indicates a better model. |
| Log loss reduction standard deviation |  |
| Log loss reduction confidence interval 95 |  |
