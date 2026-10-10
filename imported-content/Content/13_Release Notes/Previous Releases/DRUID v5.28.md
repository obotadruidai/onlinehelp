---
title: "DRUID 5.28"
---

<a id="DRUID528"></a>


Deployment Dates

The table below lists the deployment date of DRUID v5.28 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| November 23, 2023 | December 21, 2023 | December 21, 2023 | December 21, 2023 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

<a id="WhatsNew"></a>

## What's New

- **DRUID Data Service installation**. DRUID Data Service installation is now available via the DRUID Connector Host Installer.

![](../../Resources/Images/Druid%20Data%20Service%20Installation/DS%20install.png)

For more information, see Druid Data Service Installation.

<a id="Improvements"></a>

## Improvements

- **Druid Conductor**. This release enhances your ability to manage and analyze interactions within the Druid Conductor-orchestrated AI Agent ecosystem:

- **Visibility in the Conversation History**. All conversations from a Druid Conductor with response from a child AI Agent are accessible in the Conversation History of the corresponding child AI Agent. To focus solely on conversations initiated by the Druid Conductor, you can filter the child AI Agent's conversation history. Simply choose the Druid Conductor from the **Orchestrated AI Agents** filter and click **Refresh**.
- **Debugging Druid Conductor-Triggered Conversations**. In the conversation history of a child AI Agent, efficient debugging of Druid Conductor-triggered conversations is possible using either the conversation transcript or the message details. For more information about the Conversation History, see [Conversation History](../../Data%20Analytics%20%26%20Insights/History%20%26%20Logs/Conversation%20History%20V2/Conversation%20History.md).
- **AI Agent Type Identification**. On the AI Agents page (found in the **All Settings** menu under **AI Agents**), which displays all the AI Agents within your tenant, each AI Agent is labeled as either a Druid Conductor, an Orchestrated AI Agent, or none (if the label is absent).

![](../../Resources/Images/druid%205.28/mega%20and%20child%20bots.png)

- **Filtering Druid Conductor Conversation History by Child AI Agent Flows.** A new capability allows you to filter the conversation history of a Druid Conductor based on the flows executed by its orchestrated AI Agents. To utilize this feature, from the **Orchestrated AI Agents** filter, choose the specific child AI Agent, then further refine your search by selecting the desired flow from the **Flow** filter.

![](../../Resources/Images/druid%205.28/filter%20megabot%20by%20flow.png)

- **Search capabilities in the Flow Diagram**.This release introduces an advanced search functionality within the Flow Diagram that significantly enhances the user experience. Users now have the ability to search for various flow elements, facilitating quick and precise identification of elements within the flow diagram.

![](../../Resources/Images/druid%205.28/Search%20flow%20elements.png)

**Searchable Flow Elements**. Use the search feature to locate specific elements within the flow diagram, including:

- Flow step names (e.g., get-step)
- Messages (e.g., "Tell me your name", 'your name')
- Connector action names (e.g., Case-UpdateStatus)
- Link conditions

*Example: Searching for the flow step that contains a specific connector action name*

![](../../Resources/Images/druid%205.28/search%20cnn%20action.png)

**Comprehensive Search Scope**. The Flow Engine extends its search capabilities to encompass:

- Child flows
- Trigger flows
- Hero steps

- **Land AI Agent page integration with telephony systems**. You can now instruct the telephony system to initiate a new conversation upon opening the DRUID Land AI Agent page by incorporating the system parameter `reset-conversation=true` into the URL of the DRUID Land AI Agent Page. By adhering to the following URL format, you ensure that your agents seamlessly navigate between telephony calls and chat interactions on the DRUID Land AI Agent page, providing an enhanced and contextually rich experience for users:

`*druidplatform.com/app/main/landingpage/``<landbot page id>``/?``<query params>``&reset-conversation=true`

For more information, see [Integrate Land AI Agent Page with Telephony Systems](../../How%20to/Land%20bot%20page.md).

- **DRUID Vision: New RO living permit**. The DRUID API engine can also seamlessly perform OCR (Optical Character Recognition) and extract data from the latest Romanian living permits. For more information, see [Romanian Live Permit OCR](../../Druid%20AI%20Services/Romanian%20Live%20Permit%20OCR.md).

<a id="BugFixes"></a>

## Bug Fixes

- **Druid Conductor ROI KPIs**. The ROI metrics configured on child AI Agents are now available on the Druid Conductor Summary Dashboard, tab **Automations**.
