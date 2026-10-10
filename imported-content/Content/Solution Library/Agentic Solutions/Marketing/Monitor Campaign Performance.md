---
layout:
  title:
    visible: false
---

<a id="MonitorCampaignPerformance"></a>

# Monitor Campaign Performance

Each campaign activity status reflects the real-time state of a campaign activity as it progresses through the delivery and engagement lifecycle. Monitoring these statuses enables you to confirm successful delivery, track audience engagement, and quickly identify and troubleshoot any issues preventing a campaign activity from reaching its intended recipient. The table below describes each possible status value and the condition it represents.

| Status | Description |
| --- | --- |
| New | The campaign activity was created but not yet sent to the audience member. |
| Delivered | The campaign activity was delivered to the audience member. |
| Not Delivered | The delivery of the campaign activity to the audience member (by email or SMS) failed. |
| Initiated | The audience member started answering the survey questions. |
| Completed | The audience member completed the campaign survey. |
| Missing Contact | The campaign activity has no associated audience member. |
| Invalid Phone Number | The campaign activity has an invalid phone number. |
| Invalid Area Code | The campaign activity has an invalid phone area code. |
| Missing Phone Number | The campaign activity has no associated phone number. |
| Opted Out | The campaign activity has an associated contact contact who has opted out. |
| Pending | The campaign activity was queued for processing but not yet sent to the audience member. |
| Sent | The campaign activity is currently being sent to the audience member. |
| Queued | The campaign activity has been added to a delivery queue. |
| Survey Started | The audience member started answering the survey questions. |
| Not Interested | The audience member declined to receive the full campaign content. |
| No Answer | The outbound call went unanswered within the allotted time. |
| Busy | The outbound call failed to connect because the line was busy. |
| Declined | The recipient actively rejected the incoming call. |
| Unknown | The call concluded with a result that could not be classified. |
| Machine Detected | The call was answered by an automated system, such as voicemail or a fax machine. |

In addition to the status table, these values are aggregated numerically and visualized through an interactive engagement chart on the campaign form, giving you an at-a-glance view of totals for Delivered, Sent, Queued, Open, Undelivered, and Failed activities, along with a clear visual breakdown of each status category.

To view the engagement chart, navigate to the **Campaigns & Contacts** workspace and select the **Campaigns** section. Click the campaign you want to review, confirm you are on the Campaign information form, and then select the **Engagement** tab to display the chart.

![](../../../Resources/Images/Campaign%20Management/campaign%20pervformance.png)

The chart's total counts group multiple status values into higher-level categories, as summarized below.

| Count Fields | Included Statuses |
| --- | --- |
| Total Count | All campaign activity statuses, regardless of status (every activity ever created). |
| Sent | Sent, Delivered, Completed, Not Delivered, Initiated, and Survey Started. |
| Delivered | Delivered, Completed, Initiated, and Survey Started. |
| Undelivered | Not Delivered. |
| Failed | Invalid Phone Number. |
| Open | Initiated and Survey Started |
| Queued | Queued - activities that have been accepted for delivery but have not yet been dispatched to the audience member. |
