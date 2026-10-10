---
title: Execute Campaigns
---

# Execute Campaigns

Executing a campaign involves two distinct steps:

1. **Run Campaign**. Generates campaign activity records for every audience member.
2. **Send Campaign Activities**. Delivers the generated messages across selected channels (SMS, Email, Voice, or WhatsApp) to recipients.

### Step 1. Run campaign

To generate recipient activities for your campaign:

1. From the **Automations** dropdown, select **Run Now**.

![](<../../../../.gitbook/assets/Campaign Operations Automations_1.png>)

2. Monitor progress in the updates panel on the right side of the screen.

![](<../../../../.gitbook/assets/Campaign Operations Automations_2.png>)

3. When prompted “Do you want to send the message(s) now?”, select an option:

* **Yes**: Generates campaign activities with status New, sends messages immediately, and tracks recipient interaction statuses (e.g., Delivered, Initiated, Survey Started, Completed).
* **No**: Generates campaign activities with status New without delivering messages, allowing manual or scheduled delivery later.

4. Click the **Run History** tab to the list of activities.

![](<../../../../.gitbook/assets/Campaign Operations Automations_3.png>)

Each campaign activity records information about the channel, status, message received, and, for survey campaigns, the survey answers for every audience member interaction with the campaign.

![](<../../../../.gitbook/assets/Campaign Operations Automations_4.png>)

### Step 2. Send campaign activities

If you selected **No** when running the campaign, activities remain in New status until you send them.

#### Immediate Delivery

1. From the **Automations** dropdown menu, select **Send open activities** now.

![](<../../../../.gitbook/assets/Campaign Operations Automations_6.png>)

2. All activities with status **New** will deliver immediately via SMS, Email, Voice, or WhatsApp.

#### Scheduled Delivery

**Prerequisite**

* Ensure you have completed Step 1 with **No** selected when prompted “Do you want to send the message(s) now?”, leaving campaign activities in status **New**.

To deliver activities automatically at a specific date and time:

1. Select your campaign and on the campaign form, click the **Schedule Send** tab within the campaign form.
2. Set the desired delivery date and time.

![](<../../../../.gitbook/assets/scedule send tab on form.png>)

3. Go to **Solution Contents** > **Flows** and search for flow **alert-send-scheduled-activities**.
4. Click the **Flow Info** button, then click the **Scheduling** tab.

![](<../../../../.gitbook/assets/Campaign Operations Automations_7.png>)

5. Configure the schedule.

{% hint style="info" %}
**Info:** Set flow execution to run daily every 1 hour for optimal delivery accuracy.
{% endhint %}
