---
layout:
  title:
    visible: false
---

<a id="SystemEntityUiPathEvent"></a>

# System Entity: [[UiPathEvent]]

The **[[UiPathEvent]]** system entity maps in the backend specific information sent by the Orchestrator to DRUID. It maps two types of information:

- **Generic Job Information** is mapped when the job starts. The Job is given an ID and the Event Type is “Pending”. If an error occurs when trying to start the job, than ErrorCode and ErrorMessage are mapped.

![](../../Resources/Images/Starting%20UiPath%20Unattended%20Processes/System%20Entity%20UiPathEvent.png)

- **Advanced job information**. This info is mapped after job completes (or fails to) executing the process. This data is generally used for advanced configurations, where details about the job run itself are required.

![](../../Resources/Images/Starting%20UiPath%20Unattended%20Processes/System%20Entity%20UiPathEvent_1.png)
