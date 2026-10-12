---
title: Create Email Campaigns
---


Email campaigns send rich or plain-text notification messages directly to contact email addresses.

## Prerequisites

Verify that target contact phone numbers and campaign audience filters are already configured. For more information, see [Prerequisites for All Campaigns except for RingCentral CX Campaigns](<Build Campaigns.md#Prerequi>).

## Manual campaign creation procedure

1. Click **Campaigns** on the **Campaign & Contacts** workspace menu.
2. Make sure the form selected is the Campaign information form.

![](<../../../../.gitbook/assets/Build Campaigns_19.png>)

3. Click **New Campaign** at the top-right corner of the page. The campaign form appears by default on the **General** tab.
4. Add the campaign **Name** and select the campaign **Status** as **Active**.
5. From **Campaign Type** dropdown, select **Notification**.
6. Optionally, enter a **Description** and select the **Start** and **End date**.

![](<../../../../.gitbook/assets/Build Campaigns_20.png>)

7. Save the form, then click the **Campaign Details** tab.
8. Click the **+ New Record** icon in the Messages table.

![](<../../../../.gitbook/assets/Build Campaigns_21.png>)

The Campaign Step form appears by default on the **Details** tab. A campaign step defines a single message or interaction sent to the audience through a specific channel, together with its own audience segment and content. A campaign can include multiple campaign steps with different channels.

9. Configure the following mandatory fields:

* **Name**. Enter a descriptive campaign step title (e.g., Initial reach).
* **Channel**. Select Email.
* **Audience**. Select the target audience segment (e.g., Summer\_Campaign).

![](<../../../../.gitbook/assets/Build Campaigns_22.png>)

10. Save the form.
11. Click the **Campaign Messages** tab, then choose whether to enter a custom message or use a message template.

* For a **custom message**, fill in the following details:
* Email **Subject.Message**. Click the **Edit** icon displayed on the right side of the Message area, then enter the email body in HTML format.Template. Leave this field empty.

![](<../../../../.gitbook/assets/Build Campaigns_23.png>)

* For a **message template**, fill in the following details:
* **Email Subject**.
* **Template**. Select one of the existing message templates. Leave the **Message** field empty. Once the **Save** button is clicked, this field should fill automatically with the message from the template.

![](<../../../../.gitbook/assets/Build Campaigns_24.png>)

12. Save and close the form. The message record is displayed in the **Campaign Details** > **Messages** view
13. You create a new message or customize an existing one as you desire by clicking the **Generate Campaign Content** automation button, which opens a chat window where you can discuss with the agent to adjust the message content.

![](<../../../../.gitbook/assets/Build Campaigns_25.png>)

14. Save and close the Campaign Step form, then save and close the Campaign form.
