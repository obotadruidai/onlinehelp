---
layout:
  title:
    visible: false
---

<a id="Druid107"></a>

# Druid 10.7

> **IMPORTANT!** This topic describes functionality planned for a future Druid release. The information is provided for informational purposes only and reflects Druid current product direction. Nothing in this section constitutes a binding commitment to deliver any feature or functionality in a specific release or timeframe. As the market and user needs evolve, Druid reserves the right to update the list of features to ensure the most impactful features are delivered.

**Deployment Dates**

| **Druid Cloud Community**  \*.community.Druidplatform.com | **Druid Cloud US, Australia, West Europe (PROD)**  \*.us.Druidplatform.com  \*au.Druidplatform.com  \*.Druidplatform.com |
| --- | --- |
| December 29, 2026 | January 21, 2027 |

<a id="DocumentGPT"></a>

## Document GPT

This feature empowers business users to create ad-hoc knowledge bases within their workspace. By simply uploading project-specific documentation (e.g., acquisition records), users can immediately engage in natural language conversations with an AI Agent focused solely on that content. This provides a fast alternative to the admin-managed Knowledge Base in the Druid Portal.

<a id="DeveloperQueryConsole"></a>

## Developer Query Console

An interactive panel designed for engineers and developers to run ad hoc Druid queries directly within the platform.

Similar to industry-standard query and debugging consoles, this tool streamlines troubleshooting and accelerates data exploration—without requiring dedicated Druid integrations. Users can execute queries, inspect results, and diagnose issues in real time, all within their current working context.

<a id="AuditLogsforInternalActions"></a>

## Audit Logs for Internal Actions

When designing conversational flows, internal actions are powerful tools used within your flow steps as Pre-Actions or Post-Actions. However, because they previously executed without logging, diagnosing unexpected behavior or failures inside a flow step was difficult due to a lack of context regarding input variables, execution errors, or outputs.

Every internal action run now records its inputs, outputs, and explicit error details, helping you quickly pinpoint and resolve configuration issues.

<a id="DruidConductorAIAgentImportExport"></a>

## Druid Conductor AI Agent Import/Export

We are introducing a streamlined migration path for AI Agents. This feature extends the existing solution import/export capability — which focused on solution-level configurations — to cover AI Agents as a portable, self-contained artifact.

Authors can now export a fully configured AI Agent from one tenant and import it into another, eliminating the need for manual recreation. When importing a solution (such as ‘Appointment Management’), the entire AI Agent structure is automatically generated within the destination Druid Conductor.

This eliminates the manual effort of rebuilding and reconfiguring AI Agents across tenants, significantly streamlining cross-tenant deployment workflows.

<a id="SourceControlSolutionManagement"></a>

## Source Control – Solution Management

This release enhances Solution Management with improved governance and team productivity. Authors can publish solutions to a shared library, making them reusable across the organization, with usage tracking for visibility.

Platform and Managed solutions are enforced as read-only in destination tenants to prevent unintended changes. The new Push / Force Import capability enables updates across multiple tenants at once, simplifying large-scale deployments.

Support for AI Agent variables, flow variables, and version control ensures consistent and auditable solution management throughout the lifecycle.
