---
title: Build Campaigns
---

# Build Campaigns

Campaign creation allows organizations to engage audiences across multiple channels using agentic automation or manual configuration workflows. Druid AI Platform supports four core campaign categories:

| Campaign Type | Description                                                                                                                 |
| ------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Notification  | Sends direct informational messages to contacts via SMS, Email, or Voice.                                                   |
| Conversation  | Initiates outbound automated voice calls to deliver spoken messages or run interactive voice conversations.                 |
| Survey        | Gathers user feedback, sentiment, and structured responses across preferred interaction channels.                           |
| Marketing     | Delivers promotional messages or advertisement notifications within active chat sessions after a period of user inactivity. |

Channels are the medium through which a campaign message is delivered to the audience. Druid AI Platform supports six channels:

| Channel         | Description                                                                                                                                | Campaign Types Supported        |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------- |
| Web             | Delivers interactive messages inside an active chat session, sent via the **Druid\_Sendgrid** connection.                                  | Marketing, Survey               |
| SMS             | Sends text messages directly to a contact's mobile phone number via the **Twilio** connection.                                             | Notification, Survey, Marketing |
| Voice           | Places automated outbound phone calls via the **Audiocodes** connection to deliver spoken messages or run interactive voice conversations. | Conversation, Survey            |
| Email           | Sends formatted messages to a contact's email address via the **Druid\_Sendgrid** connection.                                              | Notification                    |
| WhatsApp Vonage | Sends WhatsApp messages through the Vonage integration. Optional – for creating custom WhatsApp campaigns                                  | Notification, Survey, Marketing |
| WhatsApp Meta   | Sends WhatsApp messages through WhatsApp and the delivery provider is Meta. Optional – for creating custom WhatsApp campaigns              | Notification, Survey, Marketing |

You can create campaigns using either of the following two approaches:

* **Conversational creation** (agentic guided Workflow). Go to the **Campaign & Contacts** workspace. In the Campaign page, click **Campaign Authoring Agent**.

![](<../../../../.gitbook/assets/Build Campaigns.png>)

Provide the requested details in the chat interface that opens, and the agent will build the campaign for you.

![](<../../../../.gitbook/assets/Build Campaigns_1.png>)

* **Manual creation**. In the Campaigns page, click **New Campaign**.

![](<../../../../.gitbook/assets/Build Campaigns_2.png>)

Manually fill in the configuration form for your specific campaign type as detailed in the subsequent sections.

### Prerequisites for All Campaigns except for RingCentral CX Campaigns <a href="#prerequi" id="prerequi"></a>

Before creating any campaign (conversational or manual), perform these two mandatory steps:

#### Step 1: Add Contacts

Select the **Campaign & Contacts** workspace and click **Contacts** on the menu. Manually add target contacts.

[\<https://docs.druidai.com/docs/Content/Resources/Images/Agentic Campaign Management v2/Agentic Campaign Management\_6.png>](../../../Solution%20Library/Agentic%20Solutions/Marketing/https:/docs.druidai.com/docs/Content/Resources/Images/Agentic%20Campaign%20Management%20v2/Agentic%20Campaign%20Management_6.png)![](<../../../../.gitbook/assets/Build Campaigns_3.png>)

Ensure contact records contain valid communication details (such as phone numbers or email addresses) matching the intended delivery channel.

| Parameter      | Description                                                                                                                                                                | Mandatory                                              |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| Name           | The full display name of the contact.                                                                                                                                      |                                                        |
| Preferred name | The informal or custom name used for conversational engagement. Used in dynamic campaign message personalization (e.g., email or SMS salutations).                         |                                                        |
| First Name     | The contact given name. Used to populate personal greeting variables in automated marketing and notification campaigns.                                                    | Yes                                                    |
| Last Name      | The contact family name or surname. Essential for formal communications.                                                                                                   | Yes                                                    |
| Phone Number   | The phone number of the contact person. International E.164 standard format without spaces or special characters (for example, +12135550123).                              | Mandatory for notification campaigns via Voice or SMS. |
| Email          | The email address of the contact. Used to deliver notification campaigns through the Email channel and to populate personalized email content.                             | Mandatory for notification campaigns via Email.        |
| Country        | The primary country of residence or registration for the contact. Used for geographic segmentation, audience filtering, and compliance routing.                            |                                                        |
| LanguageCode   | The primary language and locale preference of the contact. Controls language localization for conversational interactions, voice synthesis, and dynamic message templates. |                                                        |

#### Step 2: Create Campaign Audience

Define the target recipient segment by creating a campaign audience filter. Select target contacts based on specific criteria or group tags to ensure accurate campaign targeting.

This section describes how to manually create audiences. You can also import audiences directly into the campaign, by using the Import audience members automation.

![](<../../../../.gitbook/assets/Build Campaigns_4.png>)

To build a list of contacts that will be targeted by the campaign, follow these steps:

1. On the workspace menu, click **Audiences**.
2. In the Audience page, click the **New Record** icon in the top-right corner. This opens the Audience creation page.
3. Enter the campaign audience **Name** and click the **Save** icon to save the new campaign audience.

[\<https://docs.druidai.com/docs/Content/Resources/Images/Agentic Campaign Management v2/Agentic Campaign Management\_7.png>](../../../Solution%20Library/Agentic%20Solutions/Marketing/https:/docs.druidai.com/docs/Content/Resources/Images/Agentic%20Campaign%20Management%20v2/Agentic%20Campaign%20Management_7.png)![](<../../../../.gitbook/assets/Build Campaigns_5.png>)

4. In the Members section, add the contacts who will be targeted by the campaign. To add a contact:
5. Click the **Add** icon at the top-right corner of the Members table. The Campaign Audience Member page appears.
6. From the **Contact** field, select the desired lead.
7. From the **Status** field, select **New**.

[\<https://docs.druidai.com/docs/Content/Resources/Images/Agentic Campaign Management v2/Agentic Campaign Management\_8.png>](../../../Solution%20Library/Agentic%20Solutions/Marketing/https:/docs.druidai.com/docs/Content/Resources/Images/Agentic%20Campaign%20Management%20v2/Agentic%20Campaign%20Management_8.png)![](<../../../../.gitbook/assets/Build Campaigns_6.png>)

4. Click **Save & new** if you want to add another lead or **Save & close** otherwise.
5. After you finish adding the desired leads to the campaign audience, click **Save & close** to save the campaign audience and exit the configuration page.

[\<https://docs.druidai.com/docs/Content/Resources/Images/Agentic Campaign Management v2/Agentic Campaign Management\_9.png>](../../../Solution%20Library/Agentic%20Solutions/Marketing/https:/docs.druidai.com/docs/Content/Resources/Images/Agentic%20Campaign%20Management%20v2/Agentic%20Campaign%20Management_9.png)![](<../../../../.gitbook/assets/Build Campaigns_7.png>)

Audience members have their own statuses that track their progress within a campaign. To send a campaign to an audience member, the member's status must be New, as detailed in the table below.

| Status    | Description                                                                                                       |
| --------- | ----------------------------------------------------------------------------------------------------------------- |
| New       | The audience member has been added to the campaign audience and is ready to be included in the next campaign run. |
| Sent      | A campaign activity has been sent to the audience member.                                                         |
| Initiated | The audience member has started interacting with the campaign (for example, answering the survey questions).      |
| Closed    | The audience member's interaction with the campaign has ended.                                                    |

#### Step 3: Create Message Templates (Optional)

Message templates are available for campaigns using the Email or Web channel. They provide a preconfigured message that can be personalized within each campaign where it is used.

**How to create Message Templates automatically**

To create a Message Template automatically, follow these steps:

1. Select the **Campaign & Contacts** workspace.
2. Click **Message Templates** on the workspace menu.
3. Click the **Message Template Authoring Agent** automation button at the top-right corner of the page.

![](<../../../../.gitbook/assets/Build Campaigns_8.png>)

4. A chat window opens, where you can describe the desired content for the template, including its purpose, tone of voice, color palette, and UX components.

![](<../../../../.gitbook/assets/Build Campaigns_9.png>)

5. Once the agent confirms that the template has been created, you can close the webchat window.

The new message template appears in the Email Template view, where you can review and edit it as needed.

![](<../../../../.gitbook/assets/Build Campaigns_10.png>)

**How to create Message Templates manually**

To create a Message Template manually, follow these steps:

1. Select the **Campaign & Contacts** workspace.
2. Click **Message Templates** on the workspace menu.
3. Click the **Add** icon at the top-right corner of the page.

![](<../../../../.gitbook/assets/Build Campaigns_11.png>)

4. Fill in the **Name**, **Description** and **Message** fields with the desired information.

{% hint style="info" %}
**NOTE:** The **Message** field accepts either natural language text or HTML code.
{% endhint %}

![](<../../../../.gitbook/assets/Build Campaigns_12.png>)

5. Click **Save & new** if you want to add another lead or **Save & close** otherwise.
