---
layout:
  title:
    visible: false
---

<a id="AuditingMetricsConfigurationChanges"></a>

# Auditing Metrics Configuration Changes

for solution admins

The audit logging mechanism provides solution admins with a transparent historical record of the metrics and metric options configuration changes within the solution. Whenever a user modifies either the name or the description of a metric or a metric option, the system automatically generates an audit record.

By tracking these modifications, this feature allows solution admins to compare current values against previous states, and helps teams maintain data consistency across reporting dashboards. If an operational discrepancy or unauthorized change occurs, the log offers the precise historical context needed to review changes and restore settings back to a verified baseline state.

To facilitate manual corrections, the audit log displays the original system values first, followed by all subsequent updates in chronological order. This sequential layout enables authors to review the initial system values and manually update the record back to those baseline settings should their custom updates not work as intended.

<a id="AccessingtheAuditLog"></a>

## Accessing the Audit Log

Follow these steps to review the configuration history for Metrics or Metric Options:

1. Switch to the **Conversation Toolkit Admin** workspace.
2. From the workspace menu, select **Metrics** or **Metric Options** depending on the element you wish to investigate.
3. Click on the targeted item row within the data grid to open the configuration slide-out panel.
4. Switch from the **Details** tab to the **Audit** tab.

In the Audit area, review the configuration, which highlights the initial system tracking followed by subsequent updates.

Metric Audit

![](../../../../Resources/Images/AI%20Engagement%20Analyst/metric%20audit.png)

Metric Options Audit

![](../../../../Resources/Images/AI%20Engagement%20Analyst/metric%20options%20audit.png)
