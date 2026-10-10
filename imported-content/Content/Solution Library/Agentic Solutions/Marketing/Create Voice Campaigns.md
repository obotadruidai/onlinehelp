<a id="CreateVoiceCampaigns"></a>

# Create Voice Campaigns

Voice campaigns initiate outbound automated voice calls to deliver spoken notification messages or run interactive voice conversations.

<a id="Prerequisites"></a>

## Prerequisites

Verify that target contact phone numbers and campaign audience filters are already configured. For more information, see [Prerequisites for All Campaigns except for RingCentral CX Campaigns](Build%20Campaigns.md#Prerequi).

<a id="Manualcampaigncreationprocedure"></a>

## Manual campaign creation procedure

1. Click **Campaigns** on the **Campaign & Contacts** workspace menu.
2. Make sure the form selected is the Campaign information form.

![](../../../Resources/Images/Campaign%20Management/Build%20Campaigns_26.png)

3. Click **New Campaign** at the top-right corner of the page. The campaign form appears by default on the **General** tab.
4. Add the campaign **Name** and select the campaign **Status** as **Active**.
5. From **Campaign Type** dropdown, select **Conversation** or **Surve**y.
6. Optionally, enter a **Description** and select the **Start** and **End date**.

![](../../../Resources/Images/Campaign%20Management/Build%20Campaigns_27.png)

7. Save the form, then click the **Campaign Details** tab.
8. Click the **+ New Record** icon in the Messages table.

![](../../../Resources/Images/Campaign%20Management/Build%20Campaigns_28.png)

The Campaign Step form appears by default on the **Details** tab. A campaign step defines a single message or interaction sent to the audience through a specific channel, together with its own audience segment and content. A campaign can include multiple campaign steps with different channels.

9. Configure the following mandatory fields:

- **Name**. Enter a descriptive campaign step title (e.g., Initial reach).
- **Channel**. Select Voice.
- **Audience**. Select the target audience segment (e.g., Summer\_Campaign).

![](../../../Resources/Images/Campaign%20Management/Build%20Campaigns_29.png)

10. Save the form.
11. Click the **Campaign Messages** tab and choose one of the message creation methods below:

- **Manual message entry**

1. Click the **Edit** icon displayed on the right side of the Message area.
2. Input the intro message that will be delivered through voice to each member of the campaign audience.

![](../../../Resources/Images/Campaign%20Management/Build%20Campaigns_30.png)

- **Conversational message generation**

1. Click the **Content Authoring Agent** automation button. The chat interface appears.

![](../../../Resources/Images/Campaign%20Management/Build%20Campaigns_31.png)

2. Follow the agent instructions to define message goals, context, and parameters to auto-generate the content.
3. Click the **Survey Script** tab and complete the conversation script. Make sure that you specify when the AI Agent should end the conversation.

**Example**

```
Topic: "Where would you like to travel?" — dream destinations, why they appeal, what the user would do there. Stay on this topic the whole conversation.
Tone: warm, casual, curious — a friendly chat, not a form. 1–3 sentences per turn, one open question per turn based on what the user just said.
Start: open directly with the topic, no greeting first. Example: "If you could go anywhere right now, where would you go?"
Flow: let it run naturally for about 4–8 user replies. Explore things like why the place appeals, what they'd do there, who they'd go with, what's stopping them — follow their lead, don't force all of them.
End when: user says they have to go / says bye / gives two short disengaged replies in a row ("idk", "yeah") / the topic has had a natural arc (~5–8 exchanges) with nothing new to explore.

How to end: one warm closing line first, no new question (e.g. "That sounds amazing — hope you get there someday! Take care."). If the user confirms (bye/thanks/silence on topic), close with a short goodbye. If they keep talking, drop the closing tone and continue. Never ask a question and say goodbye in the same turn.
```

![](../../../Resources/Images/Campaign%20Management/survey%20script.png)

12. Save and close the form. The message record is displayed in the **Campaign Details** > **Messages** view.
13. Save and close the Campaign Step form, then save and close the Campaign form.
