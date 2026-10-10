---
layout:
  title:
    visible: false
---

<a id="ExecuteCampaign"></a>

# Execute Campaign

Campaigns can be executed automatically on a defined schedule or triggered manually on demand.

<a id="RunningtheCampaignManually"></a>

## Running the Campaign Manually

1. Navigate to the **Campaign & Contacts** workspace and click **Campaign** on the workspace menu.
2. Click on the **Lead Generation** record.
3. Click **Run Campaign.**

![](../../../../../Resources/Images/Lead%20Generation%20Skill/Execute%20Campaign.png)

Manual execution triggers the standard audience filter to build the target list. To prevent redundant outreach:

- Leads who completed a full conversation are automatically excluded from future runs.
- Leads with incomplete calls or surveys enter a 7-day suppression period before they can be contacted again.

<a id="RunningtheCampaignAutomatically"></a>

## Running the Campaign Automatically

Automated execution relies on a background trigger to automatically build audiences and launch calls at fixed intervals.

To configure the execution schedule:

1. Navigate to **Solution Content** > **Flows** and select the **Alerts** category.
2. Search for **alert-lead-generation** and click on it.
3. Click the **Info** icon in the action bar to access flow details.
4. Select the **Scheduling** tab and click **Schedule**.
5. Check **Is scheduler** enabled.

![](../../../../../Resources/Images/Lead%20Generation%20Skill/Execute%20Campaign_1.png)

6. Define the preferred cadence.
> **Info:** A weekly schedule during peak application periods is recommended.
