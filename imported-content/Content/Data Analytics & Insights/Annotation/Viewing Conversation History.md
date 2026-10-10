---
title: "Viewing Conversation History"
---

<a id="ViewingConversationHistory"></a>

<a id="_Viewing_and_Annotating"></a>
<a id="_Viewing_Conversation_History"></a>

To access the Annotation Tool for a specific AI Agent, select the AI Agent and the solution. From the main menu, click **Evaluation** and the **Conversation History** tab.

The Conversation History page contains the following elements:

- Filtering options: filter by date and by annotation status. For more information on annotation statuses, see [Annotation statuses](#Annotation_statuses).
- Trend chart – a multiple line chart that shows the number of messages (per accuracy score) sent daily within the selected date range. The Legend below the chart indicates the accuracy score coloring.
- Confidence buckets – a bar chart that shows the number of messages sent per accuracy score ranges. The chart also displays the NLP thresholds set on the AI Agent.

![](../../Resources/Images/Annotation%20Tool/Viewing%20Conversation%20History.png)

- The list of messages in the conversation history sent within the selected date range and filtered based on your selection (if any).

<a id="Viewingthemessageswithinspecificconfidencebuckets"></a>

## Viewing the messages within specific confidence buckets

Scrolling over the different bars in the Confidence buckets chart, displays a tooltip that shows the accuracy score and the number of messages with that score.

![](../../Resources/Images/Annotation%20Tool/Viewing%20Conversation%20History_1.png)

To view the messages with a specific accuracy score, click on the bar corresponding to the desired score. The list of messages with the selected accuracy score will be listed in the table below the charts. The fact that you have chosen to view messages with a specific score is marked by a black line around the selected bar on the Confidence buckets chart.

![](../../Resources/Images/Annotation%20Tool/Viewing%20Conversation%20History_2.png)

To undo the confidence bucket filtering, click on the selected bar again.

<a id="Annotationstatuses"></a>

## <a id="Annotation_statuses"></a>Annotation statuses

You can filter the conversation history (the charts and list of messages sent during the conversation) based on different annotation statuses.

By default, all message related information is shown regardless their annotation status.

![](../../Resources/Images/Annotation%20Tool/Viewing%20Conversation%20History_3.png)

The table below provides description of these statuses.

| Annotation status | Description |
| --- | --- |
| Draft | Indicates that there is no annotation action taken on the message or the annotation actions have been reverted to default. |
| Disregard | Indicates that you have chosen to disregard the message. It no longer appears in the Conversation History.  **NOTE:** Starting with DRUID version 1.47, all messages in the conversation history with an accuracy score of 100% get by default the status "Disregard". This feature is available for DRUID Connectors version 1.47 or above. In you have a hybrid or on premise DRUID deployment, install DRUID Connector Host version 1.47 or above. |
| Complete [new flow] | Indicates that you added the message as training phrase of a new flow (a new flow to the train set or test set). |
| Complete [update flow train] | Indicates that you added the message as training phrase of a flow to the AI Agent train set. |
| Complete [update flow test] | Indicates that you added the message as training phrase of a flow to the AI Agent test set. |
| Out of scope | Indicates that the message is out of scope for the current solution.  **NOTE:** This status is available for DRUID version 1.52 or higher. |

If you filter by a specific status and later you decide to analyze all messages, from the **Statuses** drop-down, select **Please select an option**.
