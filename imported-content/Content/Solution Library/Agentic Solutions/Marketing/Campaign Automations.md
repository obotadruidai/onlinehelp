---
layout:
  title:
    visible: false
---

<a id="CampaignAutomations"></a>

# Campaign Automations

The campaign configuration page provides you with automations to improve efficiency. These automations are available only for **Notification**, **Survey**, and **Conversation campaigns**, and are located on the Campaign Information form.

![](../../../Resources/Images/Campaign%20Management/Campaign%20Operations%20Automations.png)

<a id="SynchronizeSMSStatuses"></a>

## Synchronize SMS Statuses

Status synchronization for the Twilio SMS channel occurs as soon as the message is sent. Once you click the automation **Run now** and click the **Send now** button in the chat panel, a series of delay messages display in the chat indicating that fetching and synchronization are in progress.

![](../../../Resources/Images/Campaign%20Management/run%20and%20send%20now.png)

It retrieves real-time status updates only for the activities sent during that specific run; activities from previous runs are not affected.

![](../../../Resources/Images/Campaign%20Management/sms%20statuses.png)

When the final message "All activities were successfully sent. Process is over." appears, refreshing the form will show the updated status. The status will change from Pending to one of the following: Delivered, Not Delivered, Queued, Sent, or Invalid Phone Number.

The **Synchronize SMS Statuses** automation, available in the automation dropdown on the campaign form, applies when not all statuses within a bulk send have been synchronized.

![](../../../Resources/Images/Campaign%20Management/sync%20statuses.png)

<a id="SynchronizeOutboundCallStatuses"></a>

## Synchronize Outbound Call Statuses

For campaigns using the voice channel, synchronization occurs for each activity individually, once the call has ended, whether it completed or failed. These activities can return the following statuses: Initiated, Completed, No Answer, Busy, Declined, Unknown, or Machine Detected. Activities are sent as usual, and synchronization of these statuses happens automatically, no need to run another automation.

Outbound call activities can also result in other statuses, depending on how the call unfolds. If the call disconnects before authentication and the recipient indicates they do not have time to complete the survey but still wish to be contacted, the activity is marked **Not Interested**. Similarly, during authentication, if the recipient indicates they no longer wish to be contacted, the activity is marked **Opted Out**. If the recipient disconnects while the survey is in progress, the activity is marked **Survey Started**, and any unanswered questions are marked **Skipped**. Those are the result of the voice termination flow.

<a id="Exportcampaigndatatoexcel"></a>

## Export campaign data to excel

You can export comprehensive details for any campaign into an Excel report by running the Export Campaign & Survey Details automation. For Conversation and Notification campaigns, this exports campaign activities, while Survey campaigns also include participant responses.

<a id="RunningtheExport"></a>

### Running the Export

1. Open the desired campaign form.
2. Click the **Automations** dropdown and select **Export Campaign & Survey Details**.
3. A chat window will open, delivering a downloadable .xlsx file containing the complete dataset.

   ![](../../../Resources/Images/Campaign%20Data%20Export%20to%20Excel/Campaign%20Data%20Export%20to%20Excel.png)

<a id="ExcelFileStructure"></a>

### Excel File Structure

The generated workbook can contain up to five dedicated sheets depending on your campaign type:

- **General**: Contains summary information divided into two blocks—Campaign overview details and Campaign Steps breakdown.

![](../../../Resources/Images/Campaign%20Data%20Export%20to%20Excel/Campaign%20Data%20Export%20to%20Excel_1.png)

- **Dashboard**: Provides visual metrics and automated summary tables. For Survey campaigns, it includes engagement, completion, and status charts.

![](../../../Resources/Images/Campaign%20Data%20Export%20to%20Excel/Campaign%20Data%20Export%20to%20Excel_2.png)

For Conversation and Notification campaigns, it outlines status distribution and percentages via a dynamic pie chart.

![](../../../Resources/Images/Campaign%20Data%20Export%20to%20Excel/Campaign%20Data%20Export%20to%20Excel_3.png)

- **Campaign Activities**: A granular, row-by-row log of every campaign activity, displaying timestamps, contact details, call durations, call reasons, opt-out status, and conversation summaries.

![](../../../Resources/Images/Campaign%20Data%20Export%20to%20Excel/Campaign%20Data%20Export%20to%20Excel_4.png)

![](../../../Resources/Images/Campaign%20Data%20Export%20to%20Excel/Campaign%20Data%20Export%20to%20Excel_5.png)

- **Survey Responses (Survey campaigns only)**: Tracks individual response records, completion statuses, count of answered versus open questions, duration, and start/completion timestamps:

![](../../../Resources/Images/Campaign%20Data%20Export%20to%20Excel/Campaign%20Data%20Export%20to%20Excel_6.png)

- **Question Responses (Survey campaigns only)**: Itemizes individual answers given to every survey question, noting response text, numeric values, timestamps, and skipped items.

![](../../../Resources/Images/Campaign%20Data%20Export%20to%20Excel/Campaign%20Data%20Export%20to%20Excel_7.png)

<a id="Importaudiencemembers"></a>

## Import audience members

Importing audience members to a campaign using specific automation eliminates the manual effort required to manually add each audience member.

Trigger the **Import audience members** automation and follow the instructions provided by the AI Agent in the chat window.

[<https://docs.druidai.com/docs/Content/Resources/Images/Agentic Campaign Management v2/import audience members.png>](<https://docs.druidai.com/docs/Content/Resources/Images/Agentic Campaign Management v2/import audience members.png>)![](../../../Resources/Images/Campaign%20Management/Campaign%20Operations%20Automations_10.png)

<a id="Clonecampaign"></a>

## Clone campaign

Use the **Copy/Clone Campaign** automation to replicate existing campaign settings and structures.

[<https://docs.druidai.com/docs/Content/Resources/Images/Agentic Campaign Management v2/clone campaign.png>](<https://docs.druidai.com/docs/Content/Resources/Images/Agentic Campaign Management v2/clone campaign.png>)![](../../../Resources/Images/Campaign%20Management/Campaign%20Operations%20Automations_11.png)

The campaign clone doesn't have the status and the start and end dates set.

[<https://docs.druidai.com/docs/Content/Resources/Images/Agentic Campaign Management v2/cloned campaign.png>](<https://docs.druidai.com/docs/Content/Resources/Images/Agentic Campaign Management v2/cloned campaign.png>)![](../../../Resources/Images/Campaign%20Management/Campaign%20Operations%20Automations_12.png)

<a id="Deleteopencampaignactivities"></a>

## Delete open campaign activities

Use the **Delete open activities** for campaign to clear the campaign activities from the **Run History** of the selected campaign.

[<https://docs.druidai.com/docs/Content/Resources/Images/Agentic Campaign Management v2/delete opne activ.png>](<https://docs.druidai.com/docs/Content/Resources/Images/Agentic Campaign Management v2/delete opne activ.png>)![](../../../Resources/Images/Campaign%20Management/Campaign%20Operations%20Automations_13.png)
