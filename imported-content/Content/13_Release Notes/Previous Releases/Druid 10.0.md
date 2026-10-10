---
title: Druid 10.0
---

# Druid 10.0

Deployment Dates

The table below lists the deployment date of Druid 10.0 across Druid Clouds. To view the Druid Releases Calendar, see [Druid Releases](<../Druid AI Releases.md>).

| Druid Cloud Community \*.community.Druidplatform.com | Druid Cloud US \*.us.Druidplatform.com | Druid Cloud Australia \*au.Druidplatform.com | Druid Cloud West-Europe (PROD) \*.Druidplatform.com |
| ---------------------------------------------------- | -------------------------------------- | -------------------------------------------- | --------------------------------------------------- |
| September 24, 2026                                   | October 22, 2026                       | October 22, 2026                             | October 22, 2026                                    |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your Druid tenant, please contact [support@druidai.com](mailto:support@druidai.com) or your local Druid partner for more information.

### Improvements

* **Druid SIP Call Routing & Bridge Transfers**. Druid SIP now supports bridge transfers, allowing it to route active voice calls directly to an external SIP server or telephony system using outbound SIP INVITE requests. Rather than issuing a SIP REFER back to the Voice Gateway, Druid SIP acts as a bridge between the caller and the destination. For more information, see [Direct Routing to SIP Server / Telephony System (Bridge Transfer)](<../../Druid Voice/Transfer Calls.md#Direct>).
* **Set Variables - `thisStep` manipulation through advanced coding**. Authors can now access and manipulate the current step's execution lifecycle directly during variable assignment. This is particularly valuable for agentic flows, where LLM tool arguments need runtime validation before an integration executes. For more information, see [Control the current flow step using thisStep](<../../4_Flows/Set Variables.md#Control>).
* **Bulk Flow Category Renaming**. You can now rename flow categories directly from the Categories panel in the Flows section. Previously, updating a category name required manually editing the category field across every individual flow. Authors can now click the **Edit** icon in the Categories sidebar, rename one or more categories simultaneously, and click **Save**. The updated category names automatically propagate to all assigned flows.

![](<../../../.gitbook/assets/edit category.png>)

![](<../../../.gitbook/assets/rename category.png>)

![](<../../../.gitbook/assets/rename4d categories.png>)

* **Bulk Flow Enablement**. Expanding on the bulk flow disable feature introduced in Druid 9.29, this release introduces bulk flow enablement directly from the Flows page. You can select multiple disabled flows from the list and enable them simultaneously in a single action. This streamlines flow administration, making it faster to restore, test, or activate groups of flows across your bot application without updating each flow individually.

![](<../../../.gitbook/assets/enable in bulk.png>)

* **KB - PDF table extraction improvement**. We improved PDF table extraction for multi-page tables. This enhancement will become visible after performing a new extraction on PDF files.

### Bug Fixes

* **Audit Trail - Flow Restore Fix**. Resolved an issue where restoring a flow to a previous version from Audit Trail could inadvertently delete other referenced flows created after that version. Restoring a flow now updates only the selected flow definition and safely removes invalid references without affecting or deleting other existing flows.
* **Trace - Conversation History Fix**. Resolved an issue where conversation trace history failed to display flow predictions after an AI Agent intervened to collect clarifying details during rephrase. Trace history now accurately records and displays predicted flows regardless of AI Agent clarification steps.
* **KB - Chunking LLM Retry Mechanism**. Fixed an issue where temporary LLM resource delays caused chunking operations to fail due to Gateway Timeout errors. The system now automatically retries slow LLM requests during initial chunking and fallback processes before applying standard failure handling.
