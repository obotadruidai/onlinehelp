---
title: Automatically Logging Out Helpdesk Agents
---

# Automatically Logging Out Helpdesk Agents

{% hint style="info" %}
**NOTE:** This feature is available in DRUID version 1.62 and higher.
{% endhint %}

Druid AI Platform provides authors with the tools for automatically logging out the helpdesk agents based on granular working schedules defined in the authoring portal.

DRUID provides you with extensive flexibility in terms of setting up the working schedule. For every helpdesk agent and queue you can define the working schedule. Based on this schedule, DRUID will automatically log out the agents who finished their working schedule if the following conditions are met:

* The agent’s working hours have ended.
* The agent has NO ongoing live chat sessions.
* The last live chat activity (Connect / Disconnect) for that agent is older than 15 minutes.

DRUID runs an automatic job every hour, which will automatically sign out the agent(s) who meet the criteria above. For every automatically signed out agent, DRUID will:

1. Log the chat activity event “AgentSignedOutAutomatically” in conversation history DB.
2. Set \[\[HelpdeskAgent]].Status = “SignedOutAutomatically”.
3. Set \[\[HelpdeskAgent]].SignOutTime = the date and time of the agent’s automatic sign out.
4. Trigger the SignOutHelpdeskAgent flow to run any automations that might be set on agent’s sign out.

{% hint style="info" %}
**Info:** Authors can use the new entity fields from \[\[HelpdeskAgent]] in the SignOutHelpdeskAgent flow to specifically report the reason of agent sign out event (in other systems than DRUID built in Chat Activity Data, like CRM or SQL database, etc).
{% endhint %}

{% hint style="warning" %}
**IMPORTANT!** As agents might not be in front of their computer when DRUID automatically signs them out, if there are integrations on the **SignOutHelpdeskAgent** flow, make sure that you place the integrations before all steps with input mapping (if any, hero, prompt, choice steps); otherwise, DRUID might not execute the integrations, as no one will answer to the input mapping steps.
{% endhint %}

{% hint style="info" %}
**NOTE:**

* For backwards compatibility, DRUID the working hours of all existing queues and agents is set by default to 24/7.
* AI Agents do not place users in the waiting queue outside queue’s working hours.
{% endhint %}

### Queues schedule versus agents schedule

|        | Queue's schedule                                                                                                                                                                                                            | Agent's schedule                                                                                                                                                                                                                                     |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Scope  | - Automatically provide schedule for all its agents (so authors won’t need to manually set working hours for each agent) - Protect the AI Agent from placing clients in the waiting queue outside the queue’s working hours | - Agents schedule is used for automatic log out only! - Avoid situations when agents remain logged in for a very long time, and not to automatically log-out the agents precisely when they meet the log-out criteria (1 hour hysteresis may occur). |
| Result | AI Agents do not place users in the waiting queue outside queue’s working hours.                                                                                                                                            | Agents can remain logged-in after their working hours end time is reached, if they are still engaged in long-running live chat conversations, or there are still many clients in the waiting queue and agents prefer connecting to all of them.      |

{% hint style="info" %}
**NOTE:**

* AI Agents do not place users in the waiting queue outside queue’s working hours, even if some of the agents inside that queue have an custom extended schedule.
* Agents can inherit one single queue’s schedule or can have their individual custom schedule. However, the automatic log-out of the agents is only performed according to each agent’s schedule, and not the queue’s schedule.
{% endhint %}

### Set working hours for a queue

You can set up working hours at a queue level and apply it to all agents or specific agents assigned to that queue.

To set the hours of operation for a queue:

1. Go to the **Live Chat Queues** and select the desired queue.

![](<../../.gitbook/assets/Automatically Logging Out.png>)

2. Click the **Working hours** tab.

![](<../../.gitbook/assets/Automatically Logging Out_1.png>)

{% hint style="info" %}
**NOTE:** By default, the working schedule for all queues is set to 24/7.
{% endhint %}

3. Select **Scheduled**. The scheduler appears on the page.

![](<../../.gitbook/assets/Automatically Logging Out_2.png>)

4. Select the **Queue timezone**.
5. Add day of week by clicking the **Add** button next to the day. By default, the daily working hours is from **08:00 AM** to **05:00 PM**.

You can either change the working hours and then click **Add**, or add the day of week with the default working hours and then edit it according to your needs.

![](<../../.gitbook/assets/Automatically Logging Out_3.png>)

![](<../../.gitbook/assets/Automatically Logging Out_4.png>)

{% hint style="info" %}
**Info:** You can add the same day of the week only if you set two different intervals for the working hours (e.g., day shift and night shift).
{% endhint %}

6. If helpdesk agents assigned to the queue will be offline during legal holidays or other specific days, add these days in the Legal holidays section. Select the day, enter a description and click **Add**.

![](<../../.gitbook/assets/Automatically Logging Out_5.png>)

Add as many holidays as you need.

{% hint style="info" %}
**NOTE:** The days you add in the Legal holidays section for a queue will be visible on all queues; however, by default they are inactive and have no effect on the working schedule.
{% endhint %}

7. To activate a holiday for the current queue, tick **Is Active**.

![](<../../.gitbook/assets/Automatically Logging Out_6.png>)

{% hint style="info" %}
**Info:** If you want to activate all holidays for the current queue, tick the **Is Active** column header.
{% endhint %}

![](<../../.gitbook/assets/Automatically Logging Out_7.png>)

8. Click **Save & Close** if you want to save the working schedule and exit the page, or **Save** to save and stay on the page.

{% hint style="info" %}
**NOTE:** If some of the agents assigned to the queue have other working hours defined (either individually or set on another queue they’re assigned to) a warning appears. To associate the current's queue working hours to some/all of them, select the desired agents and click **Continue**.
{% endhint %}

![](<../../.gitbook/assets/Automatically Logging Out_8.png>)

9. Click **Save & Close** to save the working schedule and exit the page.

{% hint style="info" %}
**Info:** You can see which agent(s) has the working schedule of the current queue or a different schedule. In the queue details page, click the **Agents** tab and see the icon displayed in the **Custom working** hours column. The grey icon (![](<../../.gitbook/assets/Automatically Logging Out_9.png>)) indicates that the agent has the current’s queue working hours while the orange icon (![](<../../.gitbook/assets/Automatically Logging Out_10.png>)) indicates that the agent has a different working schedule.
{% endhint %}

![](<../../.gitbook/assets/Automatically Logging Out_11.png>)

{% hint style="info" %}
**NOTE:** Setting up the working hours for a queue will propagate the schedule to all agents defined on that queue, except the ones who are assigned to other queues or have a custom schedule. Setting up the working hours for each agent is only required for exceptional cases.
{% endhint %}

{% hint style="warning" %}
**IMPORTANT!** AI Agents do not place users in the waiting queue outside queue’s working hours, even if some of the agents inside that queue have an custom extended schedule.
{% endhint %}

To handle this event in the conversation flow, authors can evaluate the value of **\[\[HelpdeskClient]].IsOutsideWorkingHours** (of type Boolean), which is set by the **ConnectToHelpdeskAgent** internal action, together with the value “false” in **@InternalActionResult**.

Ex: If @InternalActionResult == false.toString()

&#x20;   Then if \[HelpdeskClient]].IsOutsideWorkingHours == true

&#x20;       Send message to user: “Sorry, you are trying to reach out outside the working hours.”

### Set working hours for a helpdesk agent

You can set up specific working hours for each of your agents to make sure each shift is properly staffed or in case some agents work part-time or do extra working hours.

Follow these steps to set working hours for an agent:

1. Go to the **Live Chat Agents** and select the agent whose working hours you want to modify (by clicking Actions > Edit). The Edit agent page appears.

![](<../../.gitbook/assets/Automatically Logging Out_12.png>)

2. Click the **Working hours** tab.

{% hint style="info" %}
**NOTE:** By default, the agent’s working schedule is 24/7 if not likewise set on the queue the agent is assigned to; in this case, the agent working hours are inherited from that queue.
{% endhint %}

![](<../../.gitbook/assets/Automatically Logging Out_13.png>)

![](<../../.gitbook/assets/Automatically Logging Out_14.png>)

If the agent is not assigned to a queue yet, the working schedule is empty.

![](<../../.gitbook/assets/Automatically Logging Out_15.png>)

3. Tick on **Custom working hours**.
4. Select the **Queue timezone**. The default queue timezone is the tenant timezone.
5. Add day of week by clicking the **Add** button next to the day. By default, the daily working hours is from **08:00 AM** to **05:00 PM**.

You can either change the working hours and then click **Add**, or add the day of week with the default working hours and then edit it according to the agent’s working hours (e.g., part-time, night shift).

![](<../../.gitbook/assets/Automatically Logging Out_16.png>)

6. If the helpdesk agents will be offline during legal holidays or other specific days (e.g., birthday), add these days in the Legal holidays section. Select the day, enter a description and click **Add**.

![](<../../.gitbook/assets/Automatically Logging Out_17.png>)

{% hint style="info" %}
**NOTE:** The days you add in the Legal holidays section will be available on all queues; however, by default they are inactive and have no effect on the working schedule.
{% endhint %}

7. To activate a holiday for the current agent, tick **Is Active**.

![](<../../.gitbook/assets/Automatically Logging Out_18.png>)

{% hint style="info" %}
**Info:** If you want to activate all holidays for the current agent, tick the Is Active column header.
{% endhint %}

![](<../../.gitbook/assets/Automatically Logging Out_19.png>)

8. Click **Save & Close** if you want to save the working schedule and exit the page, or **Save** to save and stay on the page.

{% hint style="info" %}
**NOTE:** If the agent is assigned to a queue that has working schedule set, a warning appears when saving the agent’s custom working hours. To save the agent’s custom working schedule, click **Continue**. To associate the queue’s working schedule, select the agent from the list and click **Continue**. Click **Save & Close** to save the working schedule and exit the page.
{% endhint %}

![](<../../.gitbook/assets/Automatically Logging Out_20.png>)

The icon displayed in the **Custom working hours** column on the Live Chat Agents page indicates if the agent has a custom working schedule (![](<../../.gitbook/assets/Automatically Logging Out_21.png>)) or the working schedule of set on a queue (![](<../../.gitbook/assets/Automatically Logging Out_22.png>)).

![](<../../.gitbook/assets/Automatically Logging Out_23.png>)
