---
layout:
  title:
    visible: false
---

<a id="DRUID88"></a>

# DRUID 8.8

Deployment Dates

The table below lists the deployment date of DRUID v8.8 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| January 16, 2025 | February 13, 2025 | February 13, 2025 | February 13, 2025 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host:

- Custom Code improvement

<a id="Improvements"></a>

## Improvements

- **WhatsApp channels - receiving audio messages**. The AI Agent now supports processing voice messages in WhatsApp channels by leveraging the native Voice (MS Cognitive Service) channel.  For more information, see [WhatsApp Meta Channel](../../Channels/WhatsApp%20Integration/WhatsAppMeta%20Integration.md) or [WhatsApp Vonage Channel](../../Channels/WhatsApp%20Integration/WhatsApp%20Integration.md).
> **NOTE:** The AI Agent will respond to voice messages with text only.

- **NLU Evaluation - Tenant timezone in Conversation History export**. The Conversation History export now converts Date UTC to the tenant's timezone (if set) for improved accuracy.

![](../../Resources/Images/druid%208.8/evaluation%20timezoone.png)

- **Druid Conductor - Manual handling the Druid Conductor affinity**. This release introduces the ability to manually control which child AI Agent the Druid Conductor engages. You can now specify the child AI Agent using **[[ChatUser]].PredictTargetBot** during the Intent rephrase flow, eliminating the need for role usage on AI Agents or within the conversations. Additionally, you can restrict predictions to specific child AI Agents with **[[ChatUser]].RestrictedTargetBots**. To return to the default behavior, simply set these values to null.  For more information, see [Megabots](../../AI%20Agent%20Orhestration/Druid%20Conductor.md).
- **Custom Code - read and write txt and JSON files**. DRUID now supports reading content from TXT and JSON files, as well as generating new files in these formats. These files can be shared with users during a chat interaction or sent to third-party systems via API calls. This functionality is particularly useful for scenarios where data needs to be extracted from files or dynamically generated and forwarded to external systems.  For more information, see [Custom Code](../../7_Integrations/Custom%20Code.md).
