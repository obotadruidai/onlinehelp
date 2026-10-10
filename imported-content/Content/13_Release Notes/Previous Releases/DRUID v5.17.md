---
title: "DRUID 5.17"
---

<a id="DRUID517"></a>


Deployment Dates

The table below lists the deployment date of DRUID v5.17 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| June 23, 2023 | July 06, 2023 | July 06, 2023 | July 06, 2023 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

<a id="WhatsNew"></a>

## What's New

- **Block chat users for Live Chat**. With this release authors can provide helpdesk agents with the possibility to block chat users who are disrespectful, offensive or have incorrect behavior. Helpdesk agents can block users from being placed in the waiting queue for a specific period. The way users are unblocked depends on the user type (authenticated or anonymous). For more information, see [Block Chat Users](../../Live%20Chat/Block%20Chat%20Users.md).

With this feature, the following are available:

- The **HelpdeskClient.IsBlockedForLiveChat** internal action authors can use in the Live chat agent disconnected flow to blocks users for a specific period. For more information, see the [Internal Actions](../../4_Flows/Internal%20Actions.md).
- New fields available in [[ChatActivityData] that store information related to authenticated users who have been blocked for Live Chat: **[[ChatActivityData].LiveChatBlockedUntil**, **[[ChatActivityData].LiveChatBlockedReason**, **[[ChatActivityData].LiveChatBlockedAt** and **[[ChatActivityData].LiveChatBlockedByAgentName**. For more information, see [System Entities](../../5_Entities/System%20Entities.md).
- A new context entity field, **[[ConversationInfo]].LiveChatBlockedUntil** that stores the time until the anonymous user is blocked for Live Chat. You can use this field (set to null or in the past) to author flow paths for unblocking anonymous users. For more information, see [System Entities](../../5_Entities/System%20Entities.md).

<a id="Improvements"></a>

## Improvements

- **Live Chat - Automatic allocation of clients to agents improvement**. The **Max number of sessions for automatic allocation** has been moved from AI Agent level to queue level. For more information, see [Automatically Allocating Clients to Agents](../../Live%20Chat/Automatically%20Allocating%20Clients%20to%20Agents.md).
- **Voice AudioCodes channel - added support for the "config" event**. With this release you can set parameters for the entire call (session parameters) using the "config" event.
> **NOTE:** We strongly recommend you to use the "config" event with priority against **SetVoiceSessionParams**.

For more information, see [Voice Audio Codes Channel](../../Channels/Voice%20Audio%20Codes/Voice%20Audio%20Codes%20Channel.md).

- **A new way of authoring the Intent not found flow**. If there is a single match or multiple matches, predict in the Knowledge Base Engine and decide using conditions if you want the AI Agent to reply the user only with the matches from the AI Agent model, only the matches from the Knowledge Base or both. For more information, see [Intent Not Recognized Flow](../../4_Flows/Intent%20Not%20Recognized%20Flow.md).
- **[[Intent]].KBQnAItems[].URL** entity field is now available and stores the URL specific to the unstructured data source of the identified article.
- **DRUID Data Service version** is now available in **All Settings** > **Connector Heartbeat** > **Instances** tab if the Data Service feature has been activated on your tenant. Particularly useful for DRUID on premise deployments as you can check the Data Service version against the Connector version.

![](../../Resources/Images/druid%205.17/DS%20version.png)

- **Query Related Entity - Filtering improvement**. The auto-complete of the Field Name to be filtered has been replaced with a drop-down that lists all the fields of the selected related entity.

![](../../Resources/Images/druid%205.17/query%20related%20entity.png)

- **NLU.NER.IndexBasedEntityExtractorV2 parameter improvements**. The **.IndexBasedEntityExtractorV2**algorithm was improved to search for more possible candidates from the entire user says inside the Lexicon. If the CRF algorithm extracts entities with a score under the EntityMinSingleThreshold, than the fallback algorithm searches within the Lexicon (entity index) the already matched words to ensure a higher matching score. The search will be done on the left and on the right of the matched word with a maximum offset of 3 words.
  If the algorithm finds better matches in the Lexicon, they will be added or replaced based on the matching score.
- **New Lexicon (entity index) type: Inverted**. To use an optimized algorithm that performs an extended and quick search inside the Lexicon increasing the number of candidates to a user says, set the NER parameter **NLU.NER.EntityIndexType** to **Inverted**.
> **NOTE:** We strongly recommend you to use this value, as it will become the default value in the next DRUID releases.

<a id="BugFixes"></a>

## Bug Fixes

- Saving a solution during import caused the import to remain in status "Pending".
- UiPath Unattended or attended Processes no callback - Fixed the issue when some UiPath callbacks were not triggering DRUID conversations (only for the new integration with StartUiPathJob, not with AddItemToUiPathQueue).
