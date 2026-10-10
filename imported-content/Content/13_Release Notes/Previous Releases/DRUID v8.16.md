---
title: "DRUID 8.16"
---

<a id="DRUID816"></a>


Deployment Dates

The table below lists the deployment date of DRUID v8.16 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| May 8, 2025 | June 5, 2025 | June 5, 2025 | June 5, 2025 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

<a id="WhatsNew"></a>

## What's New

- **DRUID Multichat – Real-time response recommendations with Agent Assist**. This release introduces Agent Assist in Multichat, providing real-time, AI-powered response suggestions to helpdesk agents. Agent Assist analyzes customer messages—both written and voice—and recommends the most relevant replies based on your Knowledge Base. This new feature helps agents respond faster, handle more interactions efficiently, and deliver a better customer experience.

For more information, see [Agent Assist](../../Live%20Chat/Agent%20Assist.md).

<a id="Improvements"></a>

## Improvements

- **Azure Machine Translation – Support for custom dictionaries**. This release adds support for custom dictionaries in Azure Machine Translation. You can now define and manage term-based translation rules to ensure consistent, domain-specific translations. Custom dictionaries allow you to override default translations with preferred terminology, improving accuracy and aligning results with your organization's language style.

![](../../Resources/Images/druid%208.16/AZURE%20TRANSLATOR%20SETTINGS.png)

For more information, see [Using Machine Translation](../../2_AI%20Agents/Using%20Machine%20Translation.md).

- **Web Chat – Improved feedback reactions**. Feedback reactions in Web Chat have been streamlined. You no longer need to create dedicated feedback event flows to capture positive or negative user reactions. This release introduces three new system fields in the [[ChatActivityData]] system entity:

- FeedbackMessage (string) – captures the user's feedback text.
- FeedbackReaction (string) – records the reaction type (like/dislike).
- FeedbackRating (integer) – stores the rating value.

These fields are automatically populated when a user provides feedback, making it easier to track and analyze reactions without additional configuration. For more information, see [Feedback Reactions in Web Chat](../../Channels/WebChat/Configure%20Feedback%20Options%20in%20Web%20Chat.md).
