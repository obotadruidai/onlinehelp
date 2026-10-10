---
title: "Create Marketing Campaigns"
---

<a id="CreateMarketingCampaigns"></a>


Marketing campaigns deliver promotional messages or advertisement notifications within active chat sessions following a configured period of user inactivity.

<a id="Prerequisites"></a>

## Prerequisites

Verify that target contact phone numbers and campaign audience filters are already configured. For more information, see [Prerequisites for All Campaigns except for RingCentral CX Campaigns](Build%20Campaigns.md#Prerequi).

<a id="Manualcampaigncreationprocedure"></a>

## Manual campaign creation procedure

1. Click **Campaigns** on the **Campaign & Contacts** workspace menu. Select the **Marketing Campaign Information** form.

![](../../../Resources/Images/Campaign%20Management/Build%20Campaigns_32.png)

2. Click **New Campaign** at the top-right corner of the page. The campaign form appears by default on the **General** tab.
3. Add the campaign **Name** select the campaign **Status** as **Active**.
4. From **Campaign Type** dropdown, select **Marketing**.
5. Enter a **Description** and select the **Start** and **End date**.
> **NOTE:** The **Description** is important for the LLM Agent to match an active campaign to the user interests, based on the questions that she asked in the chat.

![](../../../Resources/Images/Campaign%20Management/Build%20Campaigns_33.png)

6. Save the form, then click the **Campaign Details** tab.
7. Click the **+ New Record** icon in the Messages table.

![](../../../Resources/Images/Campaign%20Management/Build%20Campaigns_34.png)

8. The Campaign Step form appears by default on the **Details** tab. A campaign step defines a single message or interaction sent to the audience through a specific channel, together with its own audience segment and content. A campaign can include multiple campaign steps with different channels.
9. Configure the following mandatory fields:

- **Name**. Enter a descriptive campaign step title (e.g., Initial reach).
- **Channel**. Select **Web**.
- **Script**. Enter the script that you want the Marketing campaign to send.

**Example script**

```
Metallica returns to Bucharest, May 13, 2026
The rock band Metallica is coming back to Bucharest, performing at the National Arena on May 13, 2026.
Special guests will be Gojira and Knocked Loose. The concert is part of the global M72 tour.
Tickets go on sale to the general public starting Friday, May 30, at 10:00 AM.
```

![](../../../Resources/Images/Campaign%20Management/Build%20Campaigns_35.png)

10. Save and close the form. The record appears in the Messages section.

![](../../../Resources/Images/Campaign%20Management/Build%20Campaigns_36.png)

11. Save and close the Campaign Step form, then save and close the Campaign form.
12. Configure the campaign Agent's special flow to trigger on the End Conversation event, as shown below. Navigate to AI Agent **Settings**, click on **Dialogue Management** and search for **Inactivity end conversation flow**. Select the deliver-campaign-message flow. Save and close. Campaigns do not require **Run and Send**. A special flow, the campaign Agent, must be set to the End Conversation event:

![](../../../Resources/Images/Campaign%20Management/Build%20Campaigns_37.png)
