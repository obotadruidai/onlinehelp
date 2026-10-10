---
title: "DRUID 5.30"
---

<a id="DRUID530"></a>


Deployment Dates

The table below lists the deployment date of DRUID v5.30 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| December 21, 2023 | January 18, 2023 | January 18, 2023 | January 18, 2023 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

<a id="Improvements"></a>

## Improvements

- **Druid Conductor Evaluation logging enhancement**. This feature offers detailed insights into three key aspects The enhanced logging for Druid Conductor evaluation significantly improves the visibility of conversation history. Whether it's identifying flow-triggered messages, understanding knowledge base responses, or recognizing AI Agent child interactions, this feature empowers authors with a more comprehensive view of their interactions with Druid Conductor:
  - **Flow Triggered** - Easily identify messages where the conversation initiated a flow from the Druid Conductor. These messages only show the flow name in the AI Agent / Flow / KB column, making it simple to pinpoint where a conversation journey begins.
  - **Knowledge Base Response** - Messages with responses sourced from the Druid Conductor knowledge base are now clearly indicated with a specific book icon representing both the KB article and the Knowledge base data source.
  - **AI Agent Child Interaction** - Recognize messages involving interactions with the AI Agent child through by showing the child AI Agent name below the associated flow.

![](../../Resources/Images/druid%205.30/megabot%20evaluation.png)

- **Instagram channel - support added for story mention**. Mentioning an Instagram account linked to a AI Agent in a user's story triggers the Welcome flow. The event "story\_mention" is logged in a new system entity field, **[[ConversationInfo]].InstagramEvent**, providing authors with control over subsequent actions by evaluating the condition [[ConversationInfo]].InstagramEvent == "story\_mention" within the Welcome flow.
- **Enhanced Filtering for Flows, Entities, and Integrations**. You can now apply advanced filters to refine the list of QnA, Apps and Document Templates. These filters are tailored to each list and designed for intuitive use.

![](../../Resources/Images/druid%205.30/qna%20filter.png)

![](../../Resources/Images/druid%205.30/apps%20filter.png)

![](../../Resources/Images/druid%205.30/docs%20filter.png)

- **Extended search capabilities in the Flow Diagram**. Authors now also have the ability to locate the following flow elements within the flow diagram:

- Input mapping
- NER context
- Metadata attachments
- Is repeater
- Set variables
- Code extension
- Voice
