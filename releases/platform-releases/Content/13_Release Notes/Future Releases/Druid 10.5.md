---
title: "Druid 10.5"
---

<a id="Druid105"></a>


{% hint style="warning" %}
**IMPORTANT!** This topic describes functionality planned for a future Druid release. The information is provided for informational purposes only and reflects Druid current product direction. Nothing in this section constitutes a binding commitment to deliver any feature or functionality in a specific release or timeframe. As the market and user needs evolve, Druid reserves the right to update the list of features to ensure the most impactful features are delivered.
{% endhint %}

**Deployment Dates**

| **Druid Cloud Community**  \*.community.Druidplatform.com | **Druid Cloud US, Australia, West Europe (PROD)**  \*.us.Druidplatform.com  \*au.Druidplatform.com  \*.Druidplatform.com |
| --- | --- |
| December 03, 2026 | December 17, 2026 |

<a id="GranularPublishControls"></a>

## Granular Publish Controls

An enhancement to the platform publishing workflow that gives authoring teams precise control over exactly what goes live. Instead of a single, all-or-nothing publish action, authors can now review a detailed checklist breakdown of all pending changes, including specific integrations and individual asset updates.

When multiple authors work in the same environment, it can be difficult to track every active modification or prevent accidental deployments. This feature introduces a preview dropdown menu that lists all staged changes, allowing users to selectively deselect specific items before confirming the deployment. This ensures team collaboration remains seamless without the risk of publishing unfinished work or overwriting colleague updates.

<a id="NewEntityFieldTypePicklist"></a>

## New Entity Field Type: Picklist

We have expanded our entity configuration options with the addition of a new picklist field type, designed to significantly accelerate and streamline your data visualization workflows!

This new field type allows you to predefine specific values, custom labels, display ordering, and individual color-coding directly within the field metadata, delivering immediate benefits for charts and analytics:

- **Instant, Color-Coded Charts**. Because color mappings are defined directly at the field level, your charts automatically inherit the correct colors for every value. You no longer need to manually map colors every time you build a new bar chart, pie chart, or breakdown widget.
- **Uniform Dashboard Layouts** Display orders and visual treatments carry over consistently across all charts, ensuring your reports look professional, cohesive, and easy to interpret at a glance.
- **Seamless Solution Portability**. The field metadata is fully transportable with the solution, meaning your custom picklist configurations and chart settings move across environments effortlessly without requiring any manual reconfiguration.

<a id="AIAuthoringAgentsMoreIntegrations"></a>

## AI Authoring Agents – More Integrations

AI Authoring Agents now extend their orchestration capabilities to third-party systems, automatically generating the required connectivity to enterprise platforms such as Workday or Salesforce as part of the agentic skill creation pipeline, with no additional configuration steps required.

**What's new compared to version 9.23**: Agentic skill orchestration was previously scoped to Druid Data Services. Third-party system connectivity — now including enterprise platforms such as Workday or Salesforce — is fully handled by the AI Authoring Agents, leveraging the existing Druid connector framework under the hood, but making it entirely invisible to the author.

<a id="AlertsOrchestrationHub"></a>

## Alerts Orchestration Hub

We are excited to introduce a unified Alerts Orchestration Hub at the tenant level, providing administrators with a single place to monitor and manage all alerts. This feature eliminates complex navigation, allowing you to instantly view enabled statuses, track real-time runtime health, and review last-run timestamps alongside detailed error logs. This centralized hub directly answers critical operational questions at a glance:

- **Visibility**. Instantly identify which alerts are active for a specific AI Agent.
- **Status Tracking**. Verify if an alert is actively running or experiencing issues.
- **Quick Troubleshooting**. Immediately diagnose why an alert failed to trigger using the last-error details.
