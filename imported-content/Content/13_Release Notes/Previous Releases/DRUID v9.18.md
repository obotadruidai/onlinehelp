<a id="Druid918"></a>

# Druid 9.18

Deployment Dates

The table below lists the deployment date of Druid v9.18 across Druid Clouds. To view the DRUID Releases Calendar, see [Druid Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| March 12, 2026 | April 14, 2026 | April 14, 2026 | April 14, 2026 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your Druid tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local Druid partner for more information.

**Recommended!** This release includes features that require upgrade of your Druid Connector Host and Druid Data Service:

- Netopia Payments - Full Payment Transaction Details
- Data Service Performance Monitoring (Worst Calls)
- Custom Dashboards - Simplified Table Filtering
- Bug fixes

<a id="Improvements"></a>

## Improvements

- **Enforce SSO Login for All Portal Users**. Administrators can now enforce Single Sign-On (SSO) login for all Druid Portal users, ensuring that every user authenticates through the organization’s external identity provider.

This improvement helps you:

- Strengthen security by eliminating credential-based logins and reducing the risk of password attacks.
- Prevent unauthorized access from orphaned or unmanaged local accounts.
- Apply centralized identity policies, such as Multi-Factor Authentication (MFA) and corporate access controls.
- Reduce exposure to automated login attacks targeting the standard authentication endpoint.

![](../../Resources/Images/Enforce%20login%20with%20Single%20Sign%20On/Single%20Sign%20On%20Login%20Enforcement_1.png)

If needed, administrators can temporarily restore credential-based login using a generated Login key, for example if the external identity provider becomes unavailable.

![](../../Resources/Images/Enforce%20login%20with%20Single%20Sign%20On/Single%20Sign%20On%20Login%20Enforcement_2.png)

For more information, see [Enforce Login with Single Sign On](../../Governance%20%26%20Security/User%20Management/Enforce%20login%20with%20Single.md).

- **ElevenLabs - Full-Stack Voice Support (STT & TTS)**.
  Druid now supports ElevenLabs as a Speech-to-Text (STT) provider, complementing our existing Text-to-Speech integration. By adding STT capabilities, Druid users can now leverage the industry-standard ElevenLabs ecosystem for the entire voice loop—from crystal-clear voice recognition to world-class synthetic speech.  For more information, see Enable voice interactions in the Web channel.
> **NOTE:** To enable ElevenLabs STT, ensure your ElevenLabs API Key has Read permissions for the Speech-to-Text endpoint.

- **Improved intent classification with dedicated flow fields**. We improved how flow descriptions are used for intent classification:

- **Display Name (formerly Description)**. The **Description** field has been renamed to **Display Name**. This field is intended for user-facing text and may appear in the chat when the AI Agent asks users to choose between similar intents (used within the Intent-not-recognized flow).
> **IMPORTANT!** Existing values from the previous **Description** field were preserved. We **recommend reviewing** them to ensure the text is short, clear, and professional, as it might be visible to the users during chat interactions.

- **New Description LLM field**. A new **Description LLM** field is available for AI Agents that use [NLU intents classification with LLM](../../Conversational%20AI/NLU%20Intents%20Classification.md). This field provides additional context used by the LLM when identifying user intents. The LLM analyzes the following elements for classification:

- Flow Name
- Description LLM
- Training Phrases

> **Info:** Unlike the **Display Name**, content entered in the **Description LLM** field is strictly for backend processing and is **never visible** to the end user in the chat interface.

> **NOTE:** For AI Agents that already used LLM-based classification in previous Druid versions, existing content from the legacy **Description** field was automatically migrated to **Description LLM** to ensure classification continuity.

- **Netopia Payments - Full Payment Transaction Details**. With this release, Druid captures the complete transaction payload, giving you total visibility into every payment. Beyond simple success or failure, you can now access rich transaction details—such as bank issuer information, authorization codes, and currency data—directly within your conversational flows. This allows you to provide customers with detailed, real-time confirmation and more personalized service. For more information, see [Netopia Payments](../../7_Integrations/Netopia%20Payments.md).
- **Azure OpenAI LLM Resources – Support for OAuth Authentication**. You can now configure Azure OpenAI LLM resources in DRUID AI using OAuth authentication. This enhancement provides a more secure and flexible way to connect Druid to Azure-hosted LLM deployments.

Instead of relying on static API keys, OAuth uses token-based authentication managed through Microsoft Entra ID, enabling:

- **Improved Security**. Use short-lived access tokens rather than permanent keys.
- **Easier Governance**. Centrally manage and revoke access through Azure Service Principals without updating AI Agent configurations.
- **Compliance**. Meet enterprise security standards by eliminating the risk of hardcoded or exposed API keys.

For more information, see [Create LLM Resources](../../Governance%20%26%20Security/LLM%20Resource%20Management%20and%20Governance.md).

- **Data Service Performance Monitoring (Worst Calls)**. We have introduced a new WorstCalls section within the Druid Data Service settings to help you identify and optimize slow-running integrations. This monitoring tool is designed to give you immediate visibility into any Data Service integration that takes longer than 1 second to execute.

![](../../Resources/Images/Druid%20Data%20Service/worst%20calls%20rn.png)

Use these insights to determine if an integration requires logic improvements or if a Druid Data Service index should be added to the underlying entity to boost speed.

For more information, see [Analyze Data Service Performance (Worst Calls)](../../7_Integrations/Data%20Service/Druid_Data_Service.md#Analyze).

- **Workspaces - Chart Values Display**. Previously, chart values were only visible when hovering over a chart element (such as a bar or pie slice). You can now enable a persistent view to see values at a glance.

This feature allows users to compare data points and analyze trends more quickly without requiring manual interaction with every chart segment.

![](../../Resources/Images/Charts/chart%20values.png)

- **Custom Dashboards - Simplified Table Filtering**. We have significantly streamlined the process for filtering dashboard table records using the time interval selected on the dashboard. Authors no longer need to create dedicated web views or manually add search fields to entities.

![](../../Resources/Images/Custom%20Dashboards/filter%20views.png)

By enabling the **Apply Dashboard Date Filter** toggle and selecting a date-type field from the dropdown directly within any classic view configuration, you can instantly synchronize a table with the dashboard time range. This update removes the tedious setup of building custom filtering integrations, allowing you to reuse existing views while maintaining full filtering functionality.  For more information, see [Filtering table records on the dashboard](../../Data%20Analytics%20%26%20Insights/Track%20Business%20KPIs.md#Filterin).

- **SharePoint Data Sources - User permission-based content filtering**. You can now configure Knowledge Base search results to perform real-time SharePoint Online permissions checks, ensuring the AI Agent only provides information that the current user is authorized to access. For more information, see [User permission-based content filtering](../../Knowledgebase/User%20Permission-based%20Content%20Filtering.md).

<a id="BugFixes"></a>

## Bug Fixes

- **Telegram File Download**. Resolved an issue where the File Download flow step failed to render in the Telegram Channel. Files are now correctly delivered to the user instead of being skipped.
- **Telegram Hero Cards**. Fixed a bug preventing Hero Card buttons from triggering actions within Telegram conversations.
- **Outlook Email Body**. Improved the Outlook Channel integration to ensure the full email body is retrieved as plain text. Content is no longer truncated during the ingestion process.
- **MultichatV2 Cursor Focus**. Fixed a UI navigation issue in the Multichat agent portal. Previously, the input cursor would automatically jump back to the Agent Chat box after typing a single character in the Client Chat box. Focus now remains on the intended input field.
- **Connector Link Condition Errors**. Corrected a behavior where errors in Connector Action link conditions were failing silently. These errors are now properly logged, and the flow will no longer default to the success path if an evaluation error occurs.
- **Conversation History Filters**. Fixed a persistence issue where active filters in the Conversation History view were cleared after clicking the Refresh button. Applied filters now remain active across refreshes and navigation steps.
