---
title: AI Agent Audit Trail
---


The AI Agent Audit Trail gives you a complete historical record of all changes made to flows, integrations and apps in the current AI Agent. This feature helps you track modifications, identify who made them, and ensure accountability for updates. You can also compare different versions to review changes in detail, making it easier to maintain and troubleshoot your AI Agent.

{% hint style="info" %}
**NOTE:** Logging apps changes in the Audit Trail is available in DRUID 9.9 and higher.
{% endhint %}

To access the AI AgentAudit Trail, from the **History & Logs** menu, click **Audit Trail**.

![](<../../../.gitbook/assets/historical changes.png>)

## Viewing Changes

By default, the audit trail page displays all changes made today. You can filter the changes by:

* **Date range**: Select a specific time period to view changes made during that time.
* **Type**: Filter changes by either **Flow** or **Integration**.

![](<../../../.gitbook/assets/filtering (1).png>)

## Reviewing Changes

To view changes for a specific flow or integration, click the desired item in the list.

![](<../../../.gitbook/assets/all operations.png>)

The audit trail for the selected record appears on the right, listing all changes made to the item, including the operation performed (added, modified, deleted), timestamp, and the person who made the change.

## Comparing Versions

To compare different versions, click the **Compare** icon (![](<../../../.gitbook/assets/compare icon.png>)) at the top-right corner of the page. The current version appears on the right, and the previous version appears on the left.

![](<../../../.gitbook/assets/compare flow versions.png>)

Green indicates changes in the version you selected to compare, while red highlights changes in the version you are comparing it with.

You can compare the currently selected version with any previous version by selecting the desired log entry from the **Compare with** drop-down.

![](<../../../.gitbook/assets/compare with new log.png>)

{% hint style="info" %}
**Info:** If a flow / integration has been updated and later deleted, clicking the modified record in the audit trail may result in an error, as it no longer exists.
{% endhint %}

To exit the comparison view, click the **Back** icon or the **Compare** icon again.

![](<../../../.gitbook/assets/exit comparison.png>)
