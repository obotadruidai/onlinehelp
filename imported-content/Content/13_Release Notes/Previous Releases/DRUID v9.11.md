<a id="Druid911"></a>

# Druid 9.11

Deployment Dates

The table below lists the deployment date of DRUID v9.11 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| December 04, 2025 | December 18, 2025 | December 18, 2025 | December 18, 2025 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features and bug fixes that require upgrade of your Druid Connector Host and Druid Data Service:

- Druid Data Service – DATEDIFF Function in Custom Queries.
- Data Service - Web views and forms improvements
- Bug fixes

<a id="WhatsNew"></a>

## What's New

- **LLM Response Streaming (Technology Preview)**. We introduced LLM response streaming, which delivers model output token by token, significantly improving perceived speed and creating a more natural conversational flow. This feature is **currently optimized for voice interactions**, where early partial responses enhance responsiveness.

LLM streaming is available through the new internal action **LlmStreamer**, which replaces standard LLM integrations in your [Agent Steps](../../4_Flows/Agent%20Step.md) and Agent Builder configurations.

![](../../Resources/Images/druid%209.11/llm%20setramer%20action.png)

For more information, see [Use LLM Response Streaming for Voice Interactions](../../4_Flows/Use%20LLM%20Response%20Streaming%20for%20Voice%20Interactions.md).

<a id="Improvements"></a>

## Improvements

- **Centralized LLM Resources**. We added a new **LLM Resources** section under **Administration**. This feature provides a single, central place to configure and manage all your Large Language Model (LLM) service connections (API URLs and keys), enabling consistent reuse across features such as LLM NLU, machine translation, and response streaming.

![](../../Resources/Images/druid%209.11/llm%20resources%20page.png)

![](../../Resources/Images/druid%209.11/llm%20res%20details.png)

For more information, see [Create LLM Resources](../../Governance%20%26%20Security/LLM%20Resource%20Management%20and%20Governance.md).

- **Outlook channel**. The Outlook channel has been significantly updated to provide authors with more control over email conversation flow and email data manipulation:

- **Reply behavior**: Choose whether the AI Agent replies to the sender only or to all recipients.
- **Forwarding**: Forward the original email to specific recipients.
- **Move messages**: Automatically move emails from the Inbox to any Outlook folder.
- **Extended email metadata**: Access the email’s metadata for external views, forms, and Graph API integrations.

For more information, see [Outlook Channel](../../Channels/Outlook.md).

- **AI Agent model retraining indicator**. The “AI Agent model requires retrain” alert in the portal header is also triggered when:

- You add new training phrases in Prompt or Choice steps that use input mapping.

![](../../Resources/Images/druid%209.11/retrain%20bot%20model.png)

- You import a solution that includes flows with existing training phrases.

These updates help you quickly identify when your AI Agent model needs retraining after changes or imports.

- **KB - Video Transcript Extraction for Shared Drive and File Repository**. Video transcript extraction is now supported for Shared Drive and File Repository data sources.
> **NOTE:** In the File Repository data sources, you can upload video files with a maximum file size of 20 MB.

For more information, see [Extracting Data from Video Files](../../Knowledgebase/Extract%20Data%20from%20Video%20Files.md).

- **Druid Data Service – DATEDIFF Function in Custom Queries**. This new function enables users to calculate the difference between two date/time columns, returning the result in a specified time unit. This simplifies time-series analysis and reporting by allowing you to calculate and filter by key business durations directly in custom queries. This is helpful for analyzing order trends over time, identifying seasonal patterns, or creating monthly order distribution reports.  For more information, see [Filter Data Using DRUID Custom Query](../../7_Integrations/Druid%20Data%20Service%20Connector/Filter%20using%20DRUID%20custom%20query.md).
- **Data Service - Web views and forms**. This release introduces two improvements to web views and forms:

- **Set row height in views**. Choose between **Small,** **Medium**, or **High** row height options. The default is **Medium**.

![](../../Resources/Images/druid%209.11/set%20row%20height.png)

Medium row height

![](../../Resources/Images/druid%209.11/medium%20height.png)

Small row height

![](../../Resources/Images/druid%209.11/small%20height.png)

High row height

![](../../Resources/Images/druid%209.11/high%20height.png)

- **Boolean field default values**: Boolean-type fields are now set to False by default when no value is specified.

In forms

![](../../Resources/Images/druid%209.11/false%20default.png)

In web views

![](../../Resources/Images/druid%209.11/views%20boolean.png)

- **Dashboards - light widgets**. You can now display view names on dashboards for light widgets.

![](../../Resources/Images/druid%209.11/SELECT%20SHOW%20VIEW%20NAME.png)

![](../../Resources/Images/druid%209.11/widget%20name%20view.png)

<a id="BugFixes"></a>

## Bug Fixes

- **Data Service - Upsert Entity Response Count**. Fixed an issue where the updatedCount value in the Response task did not accurately reflect the number of records updated during an Upsert operation. The counter now correctly reports the actual number of records that were updated in the database.
- **Parent flows cloning**. Cloning a parent flow now correctly includes all associated child flows, preserving the full parent-child structure. Previously, only the parent flow was cloned, leaving child flows missing and requiring manual recreation.
- **Video Tag Rendering Fixed**. Fixed an issue where HTML `<video>` tags were not rendering in AI Agent flow steps. Videos now display correctly.
- **Currency Field Display in Web views**. Resolved an issue where the Currency type field was not displaying correctly at runtime in webviews. The field now shows the proper format and value.
- **Conversation Trace - Integration Error Messages**. Fixed error message positioning in conversation trace. Integration errors now display under their parent step for better context and easier debugging.

![](../../Resources/Images/druid%209.11/error%20messges.png)

- **Data Service - JArray & JObject Display**. Fixed an issue where fields of type JArray and JObject were displaying as "[object Object]" instead of showing their actual JSON content in web views and forms. These fields now correctly render their structured data in a readable format.

![](../../Resources/Images/druid%209.11/jarray%20fix.png)

- **Knowledge Base: Search by text**. Fixed issues where selecting a search result did not navigate to or highlight the correct Q&A pair in both structured and unstructured data sources, and optimized search processing to avoid redundant backend calls.
