<a id="DRUID817"></a>

# DRUID 8.17

Deployment Dates

The table below lists the deployment date of DRUID v8.17 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| May 22, 2025 | June 5, 2025 | June 5, 2025 | June 5, 2025 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host

- GoogleLLM Connector

<a id="WhatsNew"></a>

## What's New

- **GoogleLLM Connector**. You can now securely connect your own Google Vertex AI service account using the new GoogleLLM Connector, enabling direct authentication and conversational AI powered by Google’s Large Language Models without using the DRUID Service Gateway or sharing credentials.

![](../../Resources/Images/druid%208.17/googlellm%20app.png)

> **NOTE:** To use the GoogleLLM Connector in hybrid and on-premises DRUID deployments, upgrade the DRUID Connector Host to version 8.17 or later.

For more information, see [Google LLM](../../7_Integrations/GoogleLLM.md).

<a id="Improvements"></a>

## Improvements

- **Agent Assist - UI improvements in Multichat**. We've refined the Agent Assist experience within the Multichat interface for smoother helpdesk agent workflows. For voice-enabled channels, the Agent Assist now appears automatically when an agent connects to a live chat. For non-voice channels, agents can easily access Agent Assist by clicking the AI Agent icon, and we've made it simple to copy and paste suggested responses directly into the chat, further streamlining how agents leverage AI assistance.

For more information, see [Agent Assist](../../Live%20Chat/Agent%20Assist.md).

- **Vonage Voice Channel – Call transfer**. You can now seamlessly transfer calls to a live agent in your Vonage Contact Center. When the AI Agent can't fully resolve a user's query, it can escalate the call to a human agent, ensuring a smooth handover and improved customer experience for complex interactions. For more information, see [Vonage Voice](../../Channels/Vonage_Voice.md).
- **Knowledge Base – Content chunker LLM instructions**. The Content chunker LLM instructions section now appears by default in the KB Advanced Settings. This allows authors to customize the default instructions sent to the LLM chunker.

![](../../Resources/Images/druid%208.17/content%20chunker%20prompt.png)

For more information, see [Content Chunkers](../../Knowledgebase/KB%20Settings/Content%20Chunkers.md).

- **Improved Solution selector**. The Solution drop-down selector has been redesigned for better usability. It now auto-sizes to display full solution names and includes a search function to help you quickly find a solution, especially useful when your AI Agent has many.

![](../../Resources/Images/druid%208.17/solution%20selector.png)

- **DRUID Vision**. Added support for the latest Romanian ID card format (New\_IdentityCard).

<a id="BugFixes"></a>

## Bug Fixes

- The **KBExtractURLContext** internal action now correctly extracts content from websites as expected.
