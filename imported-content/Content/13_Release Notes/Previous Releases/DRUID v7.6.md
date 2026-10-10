---
layout:
  title:
    visible: false
---

<a id="DRUID76"></a>

# DRUID 7.6

Deployment Dates

The table below lists the deployment date of DRUID v7.6 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| April 11, 2024 | May 09, 2024 | May 09, 2024 | May 09, 2024 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

<a id="WhatsNew"></a>

## What's New

- **Two new field types, JArray and JObject, in technology preview**. These field types empower authors to use JSON array or JSON object data seamlessly from Data Service integrations and on flows (in the Set variables > Code Editor). This eliminates the need to align the AI Agent information model with the properties returned by the integrations or those provided in the Code Editor, thereby streamlining the authoring process.

<a id="Improvements"></a>

## Improvements

- **RingCentral channel: support for virtual agents**. RingCentral channel now supports integration with virtual agents. This release enables the seamless integration of a AI Agent with a RingCentral virtual agent without the need for a webhook.  For more information, see [RingCentral Channel](../../Channels/RingCentral/RingCentral_channel.md).
- **Solutions - a new metadata property: 'Tag'**. This property, now accessible within solutions (Solution Details), offers two distinct values: 'Solution' and 'BusinessApp'. The 'Solution' tag denotes solutions containing conversational flows, while the 'BusinessApp' tag signifies solutions solely comprising conversational business applications.

![](../../Resources/Images/druid%207.6/tag.png)

Setting this tag proves valuable for accurately categorizing solutions upon upload to the Solution Library.

![](../../Resources/Images/druid%207.6/solution%20category.png)

- **AI Agent special message for file uploads when 'Block File Upload' is set**. When a user attempts to upload a file in a chat where file uploads are blocked on the AI Agent, they will receive the message: "File transfer is not supported in this chat". You can customize this message easily on the AI Agent details page under Dialogue management > Special messages.

![](../../Resources/Images/druid%207.6/block%20file%20upload.png)

![](../../Resources/Images/druid%207.6/file%20upload%20cutomize%20message.png)

- **Live Chat and WhatsApp channels - taking over past conversations older than 24 hours**. Enhancements have been made to streamline agent interactions with past WhatsApp conversations older than 24 hours. Three key features have been added to enhance the agent experience:

- **Highlighting older conversations**: Past conversations older than 24 hours are now clearly marked with a "> 24h" label in orange, aiding agents in identifying them easily. This label is visible in both the advanced search result list and the conversation card within the agent's page left menu under 'Past' conversations.
- **Preventing message input**: To mitigate potential message loss, a feature has been implemented to block user input in the main conversation with the client if the last message in the chat is older than 24 hours. This ensures agents are aware of the conversation's status and prompts them to send a template message before proceeding with further interaction.
- **Storing user phone number**: With the context of conversations older than 24 hours deleted from the Conversation History, the phone number of users who interact with a helpdesk agent via live chat is now stored in [[HelpdeskClient]].PhoneNumber. Authors can update the flow for sending the WhatsApp Message Templates, facilitating efficient agent communication and support.

![](../../Resources/Images/druid%207.6/set%20variables.png)

![](../../Resources/Images/druid%207.6/sent%20template%20request.png)

- **Internal actions improvement**. We have improved internal actions by displaying their specific parameters in the UI, allowing authors to easily view and copy them. This enhancement enhances the authoring experience, providing greater convenience and efficiency.

![](../../Resources/Images/druid%207.6/internal%20actions.png)

- **Improved NLU Configurations - entities listing**. Entities are now listed in alphabetical order within NLU configurations. Additionally, entities utilizing Lexicon (with NLP enabled) are prioritized and displayed first in alphabetical order, providing users with a more organized and intuitive experience.

![](../../Resources/Images/druid%207.6/NLU%20CONFIG.png)

Step types are now ordered alphabetically.

![](../../Resources/Images/druid%207.6/ste%20type.png)

- **Improved clarity in Related Elements of an app**. The Related elements of an app are now more organized, allowing users to navigate directly to a specific integration by clicking its name. This enhancement streamlines the authoring experience, making it more efficient and intuitive.

![](../../Resources/Images/druid%207.6/all%20related%20integration.png)

![](../../Resources/Images/druid%207.6/selected%20integration%20in%20app.png)

- **Enhanced Workspace Logs - Connector task drill-down**. With this release, accessing detailed information about connector integrations in Workspace Logs is streamlined. Users can now simply click on a connector task name to view Connector steps, identify failed integration tasks marked with a red bar, and access error messages for resolving any misconfiguration efficiently.

![](../../Resources/Images/druid%207.6/select%20cnn%20integr%20task.png)

![](../../Resources/Images/druid%207.6/integr%20task.png)

![](../../Resources/Images/druid%207.6/correct%20error.png)

<a id="BugFixes"></a>

## Bug Fixes

- Charts with SQL integrations behind now properly send the 'Payload' property when performing operations.
- The calendar date picker no longer has missing text for quick filters.
