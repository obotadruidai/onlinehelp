---
title: "Druid 9.2"
---

<a id="Druid92"></a>


Deployment Dates

The table below lists the deployment date of DRUID v9.2 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| July 31, 2025 | August 28, 2025 | August 28, 2025 | August 28, 2025 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

<a id="Improvements"></a>

## Improvements

- **Agent Assist – Trigger the Voice Call Terminate Flow in assistant conversations**. You can now configure the **Voice Call Terminate Flow** to also trigger in the assistant conversation — the internal conversation between the helpdesk agent and the assistant AI Agent — when Agent Assist is enabled.
{% hint style="info" %}
**NOTE:** To avoid running the same actions twice, update your flow to include a branch condition that checks if `IsCommandChannel = true` and define logic specific to the assistant conversation.
{% endhint %}

For more information, see [Voice Call Terminate Flow](https://druidai.gitbook.io/druid-ai-docs/ai-platform/build-ai-agents/authoring-tools/flows/special-flows/voice-call-terminate-flow).

- **Conversation Transcript – Include assistant conversation**. You can now generate a complete transcript that includes both the main conversation (with the end user) and the assistant conversation (between the agent and the assistant AI Agent). When enabled, the transcript merges and intercalates messages from both conversations in chronological order, providing a unified view of the interaction.

To support this enhancement, the **GetConversationTranscript** internal action includes two new parameters:

- **IncludeAssistedConversation** – Set to **true** to include messages from the assistant conversation.
- **ExportType** – Set to "text" or "Json" to define the output format of the transcript.

This feature is useful for auditing, customer support analysis, and CRM integration.

For more information, see [Internal Actions](https://druidai.gitbook.io/druid-ai-docs/ai-platform/build-ai-agents/authoring-tools/flows/conversational-flows/internal-actions).

- **Website Data Sources – Improved deletion of untrained elements**. When deleting data source nodes or web pages that have not been trained, they are now automatically removed from the data source. These elements are no longer marked for deletion and left pending training. This streamlines data management and reduces unnecessary processing.

<a id="BugFixes"></a>

## Bug Fixes

- **Proactive AI Agent messages not clickable in Debugging mode**. Proactive messages in Debugging mode can now be clicked to highlight the corresponding path in the flow, just like other messages.
