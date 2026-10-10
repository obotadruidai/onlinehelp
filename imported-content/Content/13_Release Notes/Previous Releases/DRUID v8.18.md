<a id="DRUID818"></a>

# DRUID 8.18

Deployment Dates

The table below lists the deployment date of DRUID v8.18 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| June 5, 2025 | July 3, 2025 | July 3, 2025 | July 3, 2025 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host:

- Authenticate Action - Text response mapping
- DRUID Data Service Connector: Delete Entity - Cascade Delete
- DRUID Services Connector - variable name in the Base URL
- REST Connector fix

<a id="WhatsNew"></a>

## What's New

- **Agent Flow for Advanced AI Capabilities (Technology Preview)**. We are excited to introduce the new Agent step, bringing advanced AI agent capabilities directly into your conversational flows. This powerful step leverages an agentic framework, enabling your AI Agent to reason, plan, and execute complex tasks by breaking down goals into manageable steps. AI Agents can now dynamically decide actions, converse with users to gather information, and utilize various tools (functions) to achieve objectives, making your AI Agents more adaptable and capable of handling complex, multi-turn interactions. This feature is ideal for scenarios requiring dynamic decision-making, complex information gathering, and seamless integration with external tools and APIs.

![](../../Resources/Images/Agent%20Step/Agent%20Step.png)

For more information, see [Agent Step](../../4_Flows/Agent%20Step.md).

- **VoiceText Channel - Enhanced responsiveness with Long Polling**. We're excited to announce the introduction of Long Polling for the VoiceText channel, significantly improving responsiveness and user experience in Contact Center voice integrations. While the VoiceText channel traditionally uses a synchronous request-response model, which is ideal for simpler conversations, it can sometimes introduce delays during complex interactions involving integrations or Proactive AI Agent messages. The new asynchronous long polling mechanism addresses this by allowing your Contact Center to receive AI Agent responses as soon as they're available, ensuring a more fluid and efficient conversation flow.

![](../../Resources/Images/druid%208.18/long%20polling.png)

For more information, see [VoiceText channel](../../Channels/Voice%20Text/Voice_Text_Integration.md).

- **DRUID Data Service Connector: Delete Entity - Cascade Delete**. We are pleased to announce the addition of Cascade Delete functionality within the Delete Entity integration tasks. This new feature allows you to automatically propagate delete operations to related child records (entity lists), ensuring data consistency and preventing orphaned data. When configuring a Delete Entity task, you can now select specific entity lists where the delete action should also be applied, streamlining data management and improving data integrity.

![](../../Resources/Images/druid%208.18/cascade%20delete.png)

For more information, see [Delete Entity](../../7_Integrations/Druid%20Data%20Service%20Connector/Delete_Entity.md).

- **Knowledge Base - Website data sources - Subdomain Crawling Support**. Website data sources now support crawling web pages from subdomains of the provided URL. This improvement removes the need to create separate data sources for each subdomain, streamlining setup and maintenance. You can enable subdomain crawling during data source creation or later from the data source details.

![](../../Resources/Images/druid%208.18/DS%20SUBDOMAINS.png)

![](../../Resources/Images/druid%208.18/DS%20DETAILS.png)

<a id="Improvements"></a>

## Improvements

- **Authenticate Action - Text response mapping**. The Authenticate action now supports mapping tokens returned as a simple string in the response body. If your authentication client returns the token directly as a string (e.g., "yourTokenString123") rather than within a JSON object, you can now map this response directly. When configuring the Authenticate action's response mapping, simply leave the Connector field name column empty to correctly capture the plain text token.

![](../../Resources/Images/druid%208.18/custom%20auth.png)

- **DRUID Services Connector - variable name in the Base URL**. You can now use URL variables (for example, @\_Druid.LLM\_URL) directly in the **Base URL** field of the app, making integration setup easier and more dynamic.

![](../../Resources/Images/druid%208.18/DRUID%20SERVICES.png)

For more information, see [DRUID Services](../../7_Integrations/DruidServices.md).

- **Live Chat – Reply to Previous Messages**. We’ve improved the user experience and UI when replying to previous messages in Live Chat. These updates make it easier to follow conversations and provide more context when responding to users.

![](../../Resources/Images/druid%208.18/reply1.png)

![](../../Resources/Images/druid%208.18/reply2.png)

![](../../Resources/Images/druid%208.18/reply%203.png)

- **Flows – Mark flows as special flows**. You can now mark flows as special flows from the Flow details panel by selecting a **Special flow type**. This enhancement improves the authoring experience by making it easier to identify and select the correct special flow in the Dialogue Management section of the AI Agent.

![](../../Resources/Images/druid%208.18/special%20flow%20type.png)

![](../../Resources/Images/druid%208.18/special%20welcome%20flow.png)

- **Knowledge Base - Default Chunker**. The default generative endpoint is now DRUID LLM, model Becus 1.0.

![](../../Resources/Images/druid%208.18/becus.png)

- **Web Forms – Icon support for fields**. You can now add a small icon next to a field name or its value in web forms. Choose from a predefined set of icons and customize their color to enhance visual clarity and user experience.

![](../../Resources/Images/druid%208.18/set%20icon.png)

![](../../Resources/Images/druid%208.18/next%20to%20field.png)

![](../../Resources/Images/druid%208.18/next%20to%20label.png)

- **Administration - Druid Services improvement**. Expired tokens are now hidden by default in **Administration** > **Druid Services**, making it easier to view active tokens. To see the full list, including expired tokens, toggle on **Show inactive tokens**.

![](../../Resources/Images/druid%208.18/hidden%20tokens.png)

<a id="BugFixes"></a>

## Bug Fixes

- **Telegram channel – inconsistent button display**. Fixed an issue where buttons from hero cards and choice prompts in the Telegram channel appeared differently and truncated text. All buttons now have a consistent appearance and support vertical display with up to two lines of text, improving readability and user experience.
- **REST Connector fix**. The REST Connector now correctly processes and maps emoji characters received in REST API responses, preventing previous display or parsing issues.
- **Views - Relations tab fix**. Fixed an issue where self-referencing entity fields in the **Relations** tab of the Views editor could be expanded infinitely. Fields now expand only as defined by the relationship configuration.
- **Web views fix**. Fixed an issue where filters based on boolean fields did not work correctly in web views. Boolean filters now apply as expected.
