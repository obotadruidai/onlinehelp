---
title: Campaign Automations
---


The campaign configuration page provides you with automations to improve efficiency. These automations are available only for **Notification**, **Survey**, and **Conversation campaigns**, and are located on the Campaign Information form.

![](<../../../../.gitbook/assets/Campaign Operations Automations.png>)

## Synchronize SMS Statuses

Status synchronization for the Twilio SMS channel occurs as soon as the message is sent. Once you click the automation **Run now** and click the **Send now** button in the chat panel, a series of delay messages display in the chat indicating that fetching and synchronization are in progress.

![](<../../../../.gitbook/assets/run and send now.png>)

It retrieves real-time status updates only for the activities sent during that specific run; activities from previous runs are not affected.

![](<../../../../.gitbook/assets/sms statuses.png>)

When the final message "All activities were successfully sent. Process is over." appears, refreshing the form will show the updated status. The status will change from Pending to one of the following: Delivered, Not Delivered, Queued, Sent, or Invalid Phone Number.

The **Synchronize SMS Statuses** automation, available in the automation dropdown on the campaign form, applies when not all statuses within a bulk send have been synchronized.

![](<../../../../.gitbook/assets/sync statuses.png>)

## Synchronize Outbound Call Statuses

For campaigns using the voice channel, synchronization occurs for each activity individually, once the call has ended, whether it completed or failed. These activities can return the following statuses: Initiated, Completed, No Answer, Busy, Declined, Unknown, or Machine Detected. Activities are sent as usual, and synchronization of these statuses happens automatically, no need to run another automation.

Outbound call activities can also result in other statuses, depending on how the call unfolds. If the call disconnects before authentication and the recipient indicates they do not have time to complete the survey but still wish to be contacted, the activity is marked **Not Interested**. Similarly, during authentication, if the recipient indicates they no longer wish to be contacted, the activity is marked **Opted Out**. If the recipient disconnects while the survey is in progress, the activity is marked **Survey Started**, and any unanswered questions are marked **Skipped**. Those are the result of the voice termination flow.

## Export campaign data to excel

You can export comprehensive details for any campaign into an Excel report by running the Export Campaign & Survey Details automation. For Conversation and Notification campaigns, this exports campaign activities, while Survey campaigns also include participant responses.

### Running the Export

1. Open the desired campaign form.
2. Click the **Automations** dropdown and select **Export Campaign & Survey Details**.
3.  A chat window will open, delivering a downloadable .xlsx file containing the complete dataset.

    ![](<../../../../.gitbook/assets/Campaign Data Export to Excel.png>)

### Excel File Structure

The generated workbook can contain up to five dedicated sheets depending on your campaign type:

* **General**: Contains summary information divided into two blocks—Campaign overview details and Campaign Steps breakdown.

![](<../../../../.gitbook/assets/Campaign Data Export to Excel_1.png>)

* **Dashboard**: Provides visual metrics and automated summary tables. For Survey campaigns, it includes engagement, completion, and status charts.

![](<../../../../.gitbook/assets/Campaign Data Export to Excel_2.png>)

For Conversation and Notification campaigns, it outlines status distribution and percentages via a dynamic pie chart.

![](<../../../../.gitbook/assets/Campaign Data Export to Excel_3.png>)

* **Campaign Activities**: A granular, row-by-row log of every campaign activity, displaying timestamps, contact details, call durations, call reasons, opt-out status, and conversation summaries.

![](<../../../../.gitbook/assets/Campaign Data Export to Excel_4.png>)

![](<../../../../.gitbook/assets/Campaign Data Export to Excel_5.png>)

* **Survey Responses (Survey campaigns only)**: Tracks individual response records, completion statuses, count of answered versus open questions, duration, and start/completion timestamps:

![](<../../../../.gitbook/assets/Campaign Data Export to Excel_6.png>)

* **Question Responses (Survey campaigns only)**: Itemizes individual answers given to every survey question, noting response text, numeric values, timestamps, and skipped items.

![](<../../../../.gitbook/assets/Campaign Data Export to Excel_7.png>)

## Import audience members

Importing audience members to a campaign using specific automation eliminates the manual effort required to manually add each audience member.

Trigger the **Import audience members** automation and follow the instructions provided by the AI Agent in the chat window.

[\<https://docs.druidai.com/docs/Content/Resources/Images/Agentic Campaign Management v2/import audience members.png>](../../../Solution%20Library/Agentic%20Solutions/Marketing/https:/docs.druidai.com/docs/Content/Resources/Images/Agentic%20Campaign%20Management%20v2/import%20audience%20members.png)![](<../../../../.gitbook/assets/Campaign Operations Automations_10.png>)

## Clone campaign

Use the **Copy/Clone Campaign** automation to replicate existing campaign settings and structures.

[\<https://docs.druidai.com/docs/Content/Resources/Images/Agentic Campaign Management v2/clone campaign.png>](../../../Solution%20Library/Agentic%20Solutions/Marketing/https:/docs.druidai.com/docs/Content/Resources/Images/Agentic%20Campaign%20Management%20v2/clone%20campaign.png)![](<../../../../.gitbook/assets/Campaign Operations Automations_11.png>)

The campaign clone doesn't have the status and the start and end dates set.

[\<https://docs.druidai.com/docs/Content/Resources/Images/Agentic Campaign Management v2/cloned campaign.png>](../../../Solution%20Library/Agentic%20Solutions/Marketing/https:/docs.druidai.com/docs/Content/Resources/Images/Agentic%20Campaign%20Management%20v2/cloned%20campaign.png)![](<../../../../.gitbook/assets/Campaign Operations Automations_12.png>)

## Delete open campaign activities

Use the **Delete open activities** for campaign to clear the campaign activities from the **Run History** of the selected campaign.

[\<https://docs.druidai.com/docs/Content/Resources/Images/Agentic Campaign Management v2/delete opne activ.png>](../../../Solution%20Library/Agentic%20Solutions/Marketing/https:/docs.druidai.com/docs/Content/Resources/Images/Agentic%20Campaign%20Management%20v2/delete%20opne%20activ.png)![](<../../../../.gitbook/assets/Campaign Operations Automations_13.png>)
