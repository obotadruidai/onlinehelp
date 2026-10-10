---
title: "Annotating Conversation History"
---

<a id="AnnotatingConversationHistory"></a>


Using the Annotation Tool you can annotate messages one by one or in bulk.

<a id="Annotateamessage"></a>

## Annotate a message

To annotate a message, click the ![](../../Resources/Images/Annotation%20Tool/Annotating%20Conversation%20History.png) icon displayed at the right side of the message you want to annotate and select the desired annotation action.

![](../../Resources/Images/Annotation%20Tool/Annotating%20Conversation%20History_1.png)

For information on the annotation actions, see [Annotation actions](#_Annotation_actions).

<a id="Annotatemessagesinbulk"></a>

## Annotate messages in bulk

To annotate messages in bulk, select all or specific messages from the table and from the top of the table click the button corresponding to the action you want to perform on the selected messages.

> **Info:** Prior to annotating messages in bulk, you might find it useful to filter the messages by accuracy type clicking the appropriate bar on the Confidence buckets.

![](../../Resources/Images/Annotation%20Tool/Annotating%20Conversation%20History_2.png)

> **NOTE:** You cannot perform the annotation action of type Add to in bulk if the messages belong to different flows; the **Add to** buttons are non-clickable.

![](../../Resources/Images/Annotation%20Tool/Annotating%20Conversation%20History_3.png)

The tool provides the authors with three types of actions: Add to sets, Change status to and specific Actions. The next section describes the annotation actions.

<a id="Annotationactions"></a>

## <a id="_Annotation_actions"></a>Annotation actions

> **Info:** In DRUID version 1.52 or higher, the icon ![](../../Resources/Images/Annotation%20Tool/icon.png) marks the messages on which an annotation action was performed.

The table below lists the annotation actions available, their description and the new message status.

| Annotation action | Description | Message status after annotation action |
| --- | --- | --- |
| Add to Train Set on an existing flow | Add the selected message(s) as utterance for the specified flow to the Train Set.  ![](../../Resources/Images/Annotation%20Tool/Annotating%20Conversation%20History_4.png)  **NOTE:** This is available for false and multiple match training phrases.  To remove messages hover the mouse over the desired message and click the **Delete** icon displayed inline. You can also add new training phrases to top matching flows displayed. | Complete [update flow train] |
| Add to Train Set on a new flow | Add the selected message(s) as utterance for a new flow to the Train Set. | Complete [new flow] |
| Add to Test Set on an existing flow | Add the selected message(s) as utterance for the specified flow to the Test Set. | Complete [update flow test] |
| Add to Test Set on a new flow | Add the selected message(s) as utterance for a new flow to the Test Set. | Complete [new flow] |
| Change status to Disregard | The selected message(s) will be disregarded. It no longer appears in the Conversation History.  To view the list of messages you have chosen to disregard, you can filter by the Status Disregard.  ![](../../Resources/Images/Annotation%20Tool/Annotating%20Conversation%20History_8.png) | Disregard |
| Change status to Draft | Marks the message(s) as draft; the annotation actions you performed on the message(s) are reverted to default. | Draft |
| Change Status to Out of scope | Marks the message as being out of scope for the current solution.  **NOTE:** This status is available for DRUID version 1.52 or higher. | Out of scope |
| Annotate | Add comment or select the desired expected flow for that message(s).  **NOTE:** This action is available for DRUID version 1.52 or higher. | If you annotate a phrase into a flow the model should have matched in the first place, the phrase status changes to **False Match**.  **NOTE:** This status is available in DRUID 5.5 and higher. |

> **NOTE:** For DRUID version 1.52 or higher, the Annotation Tool provides you with the possibility to view the conversation history the message is part of (click the ![](../../Resources/Images/Annotation%20Tool/Annotating%20Conversation%20History.png) icon displayed at the right side of the message and select **ViewConversation**) and gain valuable insights that might help you properly annotate messages (change status, add comments, select expected flow).

<a id="AddingcommentsandselectingexpectedflowsAnnotateaction"></a>

## Adding comments and selecting expected flows (Annotate action)

The Annotation Tool allows authors to add comments to specific messages or select the desired expected flow for that message. This is particularly useful for messages with status Draft and Out of Scope.

> **NOTE:**  This feature is available in DRUID version 1.52 or higher.

To add a comment to a message or select an expected flow for a specific message, click the ![](../../Resources/Images/Annotation%20Tool/Annotating%20Conversation%20History.png) icon displayed at the right side of the message and select the **Annotate** action.

A pop-up appears.

If you want to set a specific flow to be executed for the selected message / utterance, from the **Expected Flow** drop-down, select the desired flow and click **Save**.

If you want to add a comment for the selected message, in the **Comment** field, type your comment and click **Save**.

![](../../Resources/Images/Annotation%20Tool/add%20comment.png)

The comment will display above the last annotation action performed on the message.

![](../../Resources/Images/Annotation%20Tool/comment%20added.png)

<a id="GeneralruleswhenaddingaphrasefromConversationHistorytoaflow"></a>

## General rules when adding a phrase from Conversation History to a flow

When you add a phrase from the Conversation History to a flow, make sure that:

- The extra phrase does not exceed the 100th phrase on the intent you want to add it into (if you want to add it, delete something else).
- The extra phrase does not contain typos – some of the typos entered by the users will be caught by the default NLP spelling correction algorithm (**NLU.NER.SpellingCorrection.Enabled**).
- The extra phrase is correctly written with diacritics (when using the semantic model).
- The sentence is not a multi-sentence. Currently, training supports only one sentence at a time, and the multi-sentence parameter (**NLU.NER.SpellingCorrection.Enabled**) is considered only at predict time - when a user writes two or more sentences in the same message, each of them will be matched separately into an intent.

<a id="Annotationactionsreflectedinconfidencebuckets"></a>

## Annotation actions reflected in confidence buckets

In DRUID version 1.51 and higher, when authors decide for specific messages if the classification was done right, or not by using annotation actions, their decision is reflected in the Confidence buckets chart. For example:

- The author decides that a match was made erroneously with a probability of 95% and annotates that message into another flow, the match will be a bad match (in red) on the green bar.

![](../../Resources/Images/Annotation%20Tool/sample%201.png)

- If a message that has nothing to do with the model and it really shouldn't is matched with a probability under the lower threshold and the user can change it's state to Out of Scope; it will be not counted as a bad match anymore, but as a good match on the red bar.

![](../../Resources/Images/Annotation%20Tool/bad%20annotation.png)

The table below provides an overview of the matching score coloring on the Confidence buckets chart based on author's actions.

| Initial color | Annotation action | New color | Description |
| --- | --- | --- | --- |
| Red | Annotate | Red |  |
|  | Disregard | Red |  |
|  | OutOfScope | Green | The model did not match anything, because it should not have known that message anyway. |
| Yellow | Annotate | Red | The model did a wrong match. |
|  | Disregard | Yellow |  |
|  | OutOfScope | Red | The model did a wrong match, it shouldn't have known how to answer. |
| Green | Annotate | Red | The model did a wrong match. |
|  | Disregard | Green |  |
|  | OutOfScope | Red | The model did a wrong match, it shouldn't have known how to answer. |
| Gray | Annotate | N/A |  |
|  | Disregard | Gray |  |
|  | OutOfScope | N/A |  |

## Related Topics

- [Explainability and Utterances Annotation](../../Governance%20%26%20Security/Explainability%20and%20Utterances%20Annotation.md)
