---
title: "Knowledge Base Schedule"
---

<a id="KnowledgeBaseSchedule"></a>


The Knowledge Base Schedule allows authors to schedule crawling, extraction, and training actions at a data source level to occur automatically.

> **NOTE:** The Schedule is available only for unstructured data sources. The KB Schedule is a tenant feature. If you want activate it on your tenant, reach out to [DRUID Support](<mailto:support@druidai.com?subject=Activate KB Schedule on my tenant>).

> **IMPORTANT!** For hybrid deployments, you must upgrade the KB Agent.

<a id="SetupaschedulefromtheKnowledgeBasepage"></a>

## Set up a schedule from the Knowledge Base page

1. Go to the Knowledge Base and click the **Schedules** tab. The Schedules page displays all schedules set up for the different unstructured data sources.
> **NOTE:**  You can set only one schedule per data source.

2. Click the **New Schedule** button. The New Schedule modal appears.
3. Choose the desired unstructured data source.

![](../Resources/Images/Knowledge%20Base%20Schedule/Knowledge%20Base%20Schedule.png)

4. Select **Next**. The schedule configuration appears.

By default, the schedule is disabled. Select the toggle next to the data source name to enable it.

5. Toggle on the actions to schedule. The following actions are available for scheduling: Crawl, Extract, and Train.

![](../Resources/Images/druid%209.7/kb%20level%20sched%20actions.png)

> **NOTE:** For File Repository data sources, the only available actions you can schedule are Extract and Train. The Crawl action is disabled.

When you toggle on Crawl and Extract, additional action-specific parameters become available.

You can toggle on the following action combinations:

- Crawl, Extract, and Train
- Crawl and Extract
- Extract and Train
- Each action individually (Crawl / Extract / Train)

> **NOTE:** Toggling on any other action combination than the ones listed above will cause an error when you save the schedule.

6. Select the **Start date**.
7. By default, the **No end date** toggle is turned on, which means the scheduler runs indefinitely. If you want the scheduler to stop on a specific date, turn off the **No end date** toggle, and then select the desired **End date**.

![](../Resources/Images/druid%209.7/start%20date.png)

8. Configure the occurrence, frequency, and interval.

![](../Resources/Images/druid%209.7/start%20date.png)

9. Click **Save** to save the schedule.

The selected actions will be performed on the data source based on the schedule.

<a id="SetupaschedulefromtheDataSource"></a>

## Set up a schedule from the Data Source

1. Go to your data source and click the **Schedule** tab. The Schedule configuration page appears.

![](../Resources/Images/Knowledge%20Base%20Schedule/Knowledge%20Base%20Schedule_3.png)

2. By default, the schedule is disabled. Select the toggle next to the data source name to enable it.
3. Toggle on the actions to schedule. The following actions are available for scheduling: Crawl, Extract, and Train.

![](../Resources/Images/druid%209.7/toggle%20schedule%20actions.png)

> **NOTE:** For File Repository data sources, the only available actions you can schedule are Extract and Train. The Crawl action is disabled.

When you toggle on Crawl and Extract, additional action-specific parameters become available.

You can toggle on the following action combinations:

- Crawl, Extract, and Train
- Crawl and Extract
- Extract and Train
- Each action individually (Crawl / Extract / Train)

> **NOTE:** Toggling on any other action combination than the ones listed above will cause an error when you save the schedule.

4. Select the **Start date**.
5. By default, the **No end date** toggle is turned on, which means the scheduler runs indefinitely. If you want the scheduler to stop on a specific date, turn off the **No end date** toggle, and then select the desired **End date**.
6. Configure the occurrence, frequency, and interval.
7. Click **Save** to save the schedule.

The selected actions will be performed on the data source based on the schedule.

<a id="Rulesforperformingscheduledactions"></a>

## Rules for performing scheduled actions

Each action will notify the next action set that can start. If all slots for an action are in use (for example, two crawls are running in parallel), the next one will wait in a queue and will start when one of the first two finishes. The same applies to extraction. If more than one training action is set to start in the same interval, they will accumulate.

<a id="ScheduleStatuses"></a>

## Schedule Statuses

A schedule can have one of the following statuses:

- **Disabled**: The schedule has been set up but has not been enabled.
- **Active**: The schedule has been set up and has been enabled.
- **Finished**: The schedule occurrence has been reached.

<a id="Updatedisableordeleteaschedule"></a>

## Update, disable or delete a schedule

Because you can set only one schedule per data source, if you need to set up a different schedule, go to the schedule configuration page and modify it based on your needs.

You can delete a schedule if you want. However, if you want to keep the configuration but stop automatically performing the actions, we recommend disabling it instead. This ensures that you can easily adjust the schedule and enable it in the future.
