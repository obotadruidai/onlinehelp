<a id="CreateRingCentralCXCampaigns"></a>

# Create RingCentral CX Campaigns

Voice campaigns initiate outbound automated voice calls to deliver spoken notification messages or run interactive voice conversations.

<a id="Prerequisites"></a>

## Prerequisites

- You must update your business app to version 10.1 or higher and perform additional configuration. For more information, see [RingCentral CX Data Provisioning & Configuration](RingCentral%20CX%20Data%20Provisioning.md#_RingCentral_CX_Data).
- You must set the call center system to Ring Central in your Campaign Settings so the RingCentral agent can load the correct statuses and dispositions.
- You must create an empty audience for RingCentral CX campaigns (**Campaign Managers - Campaign & Contacts** workspace > **Audiences**).

<a id="Manualcampaigncreationprocedure"></a>

## Manual campaign creation procedure

1. Go to **Campaign Managers - Campaign & Contacts** workspace > **Campaigns**.
2. Click the **Ring Central Campaigns** tab.
3. Click **New Campaign** at the top-right corner of the page. The campaign form appears by default on the **General** tab.
4. Add the campaign **Name** and select the campaign **Status** as **Active**.
5. From **Campaign Type** dropdown, select **Conversation**.
6. Optionally, enter a **Description**.
7. Select the **Start date**.

![](../../../Resources/Images/Ring%20central%20%2B%20excel%20export%20updates/Create%20RingCentral%20CX%20Campaigns_1.png)

8. Save the form, then click the **Campaign Details** tab.
9. Click the **+ New Record** icon in the Messages table.

![](../../../Resources/Images/Ring%20central%20%2B%20excel%20export%20updates/Create%20RingCentral%20CX%20Campaigns_1_1.png)

> **NOTE:**  The campaign should include exactly one campaign step configured with the Voice channel.

10. Configure the following mandatory fields:

- **Name**. Enter a descriptive campaign step title.
- **Channel**. Select **Voice**.
- **Audience**. Select the empty audience you created for RingCentral CX.

![](../../../Resources/Images/Ring%20central%20%2B%20excel%20export%20updates/Create%20RingCentral%20CX%20Campaigns_1_2.png)

11. Save the form.
12. Click the **Campaign Messages** tab , then click the **Edit** icon displayed on the right side of the Message area.
13. Provide a personalized introductory message using placeholders for the AI Agent to start the conversation.

![](../../../Resources/Images/Ring%20central%20%2B%20excel%20export%20updates/Create%20RingCentral%20CX%20Campaigns_1_3.png)

14. Click the **Conversation Script** tab and provide a conversation script to guide the AI Agent through the requirements specific to the campaign, such as scheduling appointments.

![](../../../Resources/Images/Ring%20central%20%2B%20excel%20export%20updates/Create%20RingCentral%20CX%20Campaigns_1_4.png)

15. Save and close the form. The message record is displayed in the Campaign Details > Messages view.
16. Save and close the Campaign Step form, then save and close the Campaign form.
