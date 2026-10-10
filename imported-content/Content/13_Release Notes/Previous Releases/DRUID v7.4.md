---
layout:
  title:
    visible: false
---

<a id="DRUID74"></a>

# DRUID 7.4

Deployment Dates

The table below lists the deployment date of DRUID v7.4 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| March 14, 2024 | April 11, 2024 (part of 7.5) | April 11, 2024 (part of 7.5) | April 11, 2024 (part of 7.5) |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host:

- connector bug fixes.

<a id="Improvements"></a>

## Improvements

- **GetConversationTranscript Internal Action - enhancement**. In this release, we've transitioned the storage location of the conversation transcript to **[[ConversationInfo]].TranscriptTxt** from [[ChatUser]].Transcript.Txt due to technical reasons. For more information, see [Internal Actions](../../4_Flows/Internal%20Actions.md).
> **IMPORTANT!** When configuring CNN integration mappings, please be aware that [[ConversationInfo]] is not directly accessible like [[ChatUser]]. To ensure seamless integration, it's recommended to perform a SetVariable action beforehand, setting [[ConversationInfo].TranscriptTxt to your business request entity. **This update requires adjustments in configurations for transmitting conversation transcripts to external systems.** For more information, see [Sending the conversation transcript to external systems](../../How%20to/Sending%20the%20conversation%20transcript%20to%20external%20systems.md).

- **Knowledge Base - File Repository (Final Version)**. In this release, the File Repository feature reaches its final version, offering enhanced functionality and usability for managing your File Repository data sources. Key highlights:

- Users can fully harness the capabilities of a File Repository data source.
- Users can upload multiple files to the same data source and efficiently organize them into folders for better management.
- Gain full control over data source extraction and maintenance processes.
- Users can seamlessly maintain both the file repository structure and its content.

![](../../Resources/Images/druid%207.4/file%20repo.png)

For more information, see [Knowledge Base](../../Knowledgebase/Knowledgebase.md).

- **Adaptive Cards Manipulation**. This release allows seamless manipulation of adaptive cards to dynamically adapt to changing contexts using the Code Extension feature.  For more information, see [Adaptive Cards Steps](../../4_Flows/Adaptive%20Cards%20Steps.md).
- **Extended Control over NER**. This release grants you full access to all entity candidates discovered by the Flow Engine, allowing you to seamlessly incorporate them into the entity index, search them within an external database (if available), or perform additional flow authoring tailored to your specific requirements. For more information, see [Manipulating NER Candidates](../../Conversational%20AI/Control%20NER%20Candidates.md).
- **Intent rephrase flow improvements**. This release introduces user says pipeline execution changes for Intent rephrase. The "Intent rephrase flow" is triggered just before the Conversation Engine predicts to other parent flows or against the Knowledge Base, ensuring more accurate and optimized interactions. For more information, see [Intent rephrase flow](../../4_Flows/Intent%20rephrase%20flow.md).
- **Enhanced Solution References: Displaying Full Entity Path**. We've enhanced the Solution References feature to offer authors more comprehensive insights. Now, when linking an entity to a solution and the entity includes a field of type entity referencing another entity, the Parent Name column within Solution References will present the complete entity path. This path will be displayed in the format of "linked entity -> entity field referencing the entity in the 'Name' column".

![](../../Resources/Images/druid%207.4/solution%20references.png)

- **Viber channel - sending the welcome message**. Now, in the Viber channel, when a user initiates a conversation with the AI Agent, the Welcome flow will be automatically triggered. Regardless of the user's subscription status to the AI Agent channel, the welcome message will be promptly sent to the user, ensuring a seamless and engaging interaction experience.
- **Improved Automation Capabilities for Web Views and Forms**. In this release, we've enhanced the automation functionality for web views and forms. Now, business users have the capability to trigger specific integrations directly from web views and forms, expanding their control beyond conversational flows. This enhancement offers increased flexibility and efficiency in managing your processes. For more information see, [Recommend automations on views](../../CBA/Recommend%20automations%20on%20views.md) and [Recommend automations on forms](../../CBA/Recommend%20automations%20on%20forms.md).
- **Connector Diagram - Exit icon.** In this release, we've introduced a dedicated **Exit** icon within the Connector Diagram. It allows authors to seamlessly transition from the Connector Diagram to the list view, enhancing navigation efficiency within the interface.

![](../../Resources/Images/druid%207.4/exit%20cnn%20diagram.png)

- **Improved web forms improvement**. In this release, we've enhanced web forms by introducing the ability to add Kanban views. Now, users can seamlessly integrate Kanban views directly into web forms.

![](../../Resources/Images/druid%207.4/kanban%20on%20forms.png)

![](../../Resources/Images/druid%207.4/kanban%20on%20forms2.png)

<a id="BugFixes"></a>

## Bug Fixes

- **DRUID Data Service**. Dynamic Query with aggregation and functions is now properly returning values.
- **CNN - custom code**. the system now automatically converts IDs stored as strings to GUIDs. This bug fix streamlines data handling processes, ensuring seamless integration and compatibility within the CNN custom code functionality.
