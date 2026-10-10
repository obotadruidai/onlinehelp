---
title: "Create SMS Campaigns"
---

<a id="CreateSMSCampaigns"></a>


SMS campaigns deliver direct text notification messages to contact mobile phone numbers.

<a id="Prerequisites"></a>

## Prerequisites

Verify that target contact phone numbers and campaign audience filters are already configured (for campaigns created with the Campaign Authoring Agent). For more information, see [Prerequisites for All Campaigns except for RingCentral CX Campaigns](Build%20Campaigns.md#Prerequi).

<a id="Manualcampaigncreationprocedure"></a>

## Manual campaign creation procedure

1. Click **Campaigns** on the **Campaign & Contacts** workspace menu
2. Make sure the form selected is the **Campaign information** form.

![](../../../Resources/Images/Campaign%20Management/Build%20Campaigns_13.png)

3. Click **New Campaign** at the top-right corner of the page. The campaign form appears by default on the **General** tab.
4. Enter the campaign **Name**  and select the campaign **Status** as **Active**.
5. From **Campaign Type** dropdown, select **Notification**.
6. Optionally, enter a **Description** and select the **Start** and **End date**.

![](../../../Resources/Images/Campaign%20Management/Build%20Campaigns_14.png)

7. Save the form, then click the **Campaign Details** tab.
8. Click the **+ New Record** icon in the Messages table.

![](../../../Resources/Images/Campaign%20Management/Build%20Campaigns_15.png)

The Campaign Step form appears by default on the Details tab. A campaign step defines a single message or interaction sent to the audience through a specific channel, together with its own audience segment and content. A campaign can include multiple campaign steps with different channels.

9. Configure the following mandatory fields:

- **Name**. Enter a descriptive campaign step title (e.g., Initial reach).
- **Channel**. Select SMS.
- **Audience**. Select the target audience segment (e.g., SMS\_Summer\_Campaign).

![](../../../Resources/Images/Campaign%20Management/Build%20Campaigns_16.png)

10. Save the form.
11. Click the Campaign Messages tab and choose one of the message creation methods below:

- **Manual message entry**

1. Click the **Edit** icon displayed on the right side of the Message area.
2. Input the message that will be delivered through SMS to each member of the campaign audience.

![](../../../Resources/Images/Campaign%20Management/Build%20Campaigns_17.png)

- **Conversational message generation**

1. Click the **Campaign Campaign Content** button.

![](../../../Resources/Images/Campaign%20Management/Build%20Campaigns_18.png)

2. The chat interface appears. Follow the agent instructions to define message goals, context, and parameters to auto-generate the content.

12. Save and close the form. The message record is displayed in the **Campaign Details** > **Messages** view.
13. Save and close the Campaign Step form, then save and close the Campaign form.

For information on how to send campaign activities, see [Campaign Automations](Campaign%20Automations.md#Send).
