---
title: "Create Survey Campaign"
---

<a id="CreateSurveyCampaign"></a>


Survey campaigns gather user feedback, sentiment, and structured responses across preferred interaction channels.

<a id="Prerequisites"></a>

## Prerequisites

Verify that target contact phone numbers and campaign audience filters are already configured. For more information, see [Prerequisites for All Campaigns except for RingCentral CX Campaigns](Build%20Campaigns.md#Prerequi).

<a id="Manualcampaigncreationprocedure"></a>

## Manual campaign creation procedure

1. Click **Campaigns** on the **Campaign & Contacts** workspace menu.
2. Click **New Campaign** at the top-right corner of the page. The campaign form appears by default on the **General** tab.
3. Add the campaign **Name** select the campaign **Status** as **Active**.
4. From **Campaign Type** dropdown, select **Survey**.
5. Optionally, enter a **Description** and select the **Start** and **End date**.

![](../../../Resources/Images/Campaign%20Management/Build%20Campaigns_38.png)

6. Save the form, then click the **Campaign Details** tab.
7. Click the **+ New Record** icon in the Messages table.

![](../../../Resources/Images/Campaign%20Management/Build%20Campaigns_39.png)

The Campaign Step form appears by default on the **Details** tab. A campaign step defines a single message or interaction sent to the audience through a specific channel, together with its own audience segment and content. A campaign can include multiple campaign steps with different channels.

8. Configure the following mandatory fields:

- **Name**. Enter a descriptive campaign step title (e.g., Initial reach).
- **Channel**. Select your preferred delivery channel.
> **NOTE:** All channels support the Survey Campaign, except for Email. Email is only used to deliver the survey link.

- **Audience**. Select the target audience segment (e.g., Summer\_Campaign).

![](../../../Resources/Images/Campaign%20Management/Build%20Campaigns_40.png)

9. Save the form and click the **Survey Script** tab.
10. Click the **Edit** icon displayed on the right side of the Script area.
11. Enter the script as a story.

![](../../../Resources/Images/Campaign%20Management/Build%20Campaigns_41.png)

12. Save and close the form.
13. Save and close the Campaign Step form, then save and close the Campaign form.
