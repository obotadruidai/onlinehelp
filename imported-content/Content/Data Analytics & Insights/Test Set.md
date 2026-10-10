---
title: "Evaluate Test Phrases"
---

<a id="EvaluateTestPhrases"></a>


The sample of data used to provide an unbiased evaluation of a final trained model based on the selected train set. In general, the test set is well-curated. It contains carefully sampled data that spans the various classes that the model would face, when used in the real world.

The Test Set feature (**Test Set** tab) enables you train the AI Agent with test phrases that are similar to the AI Agent training phrases, creating a powerful ML model for your AI Agent.

![](../Resources/Images/Evaluating%20Bot%20Training%20Model/bot%20test%20set.png)

Similar to the Train Set, if there are parent flows with child intents, you can also evaluate the child models.

<a id="Importingtestdatainbulk"></a>

## Importing test data in bulk

The Test module of the DRUID Evaluation tool works with bulk sets of test phrases, using template based import / export of test phrases in Excel file format.

{% hint style="warning" %}
**IMPORTANT!** Bulk Import from excel file will REPLACE existing test set for that AI Agent and the language code! The import does not affect other languages on the same AI Agent.
{% endhint %}

<a id="Prerequisites"></a>

### Prerequisites

- Make sure to use only templates downloaded from DRUID platform, to avoid table structure misalignment. Download the Test phrases excel template by clicking **Test Set** button and then **Download**.
- Make sure that the utterances in the excel file are in the language you want to evaluate (using the Evaluation tool). Only ONE single language must be used per excel file. Create separate excel files for each different language you wish to test.

- After downloading the Excel template file, fill in the test phrase set as follows:

- In column B (Utterances) fill in the test phrases.
- In column C (Expected Intent Name) fill in the name of DRUID Flow which the respective test phrase is expected to match.
{% hint style="warning" %}
**IMPORTANT!**  The name provided in column C must be identical with the expected flow name, otherwise the corresponding phrase will not be uploaded.
{% endhint %}

{% hint style="info" %}
**NOTE:** Leaving a C cell empty means that the corresponding test phrase in column B is not expected to match any of the flows defined on the AI Agent, for the chosen language.
{% endhint %}

To import your test set from an excel file, click the **Test Set** button and then click **Upload**.

![](../Resources/Images/Evaluating%20Bot%20Training%20Model/Test%20Set.png)

Browse for the excel file and select it. Click the **Upload** button.

After uploading the test set excel file, this will be evaluated for data coherence. In case errors occur during file evaluation, these will be mentioned in column O (Import Status) of the SAME file you uploaded. The updated file will be available for download in the same pop-up window used to initially upload the file.

Click the **Evaluate** button to evaluate your test set.

![](../Resources/Images/Evaluating%20Bot%20Training%20Model/Test%20Set_1.png)

The Test Set page provides you with matching percentage for each test phrase.

<a id="Exportingtestset"></a>

## Exporting test set

To export a test data, click the **Test Set** button, then click **Download**. The excel file contains detailed information on all test phrases and their corresponding intents (flows).

![](../Resources/Images/Evaluating%20Bot%20Training%20Model/Test%20Set_2.png)

## Related Topics

- [Explainability and Utterances Annotation](../Governance%20%26%20Security/Explainability%20and%20Utterances%20Annotation.md)
