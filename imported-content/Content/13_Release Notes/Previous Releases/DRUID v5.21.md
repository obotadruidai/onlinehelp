<a id="DRUID521"></a>

# DRUID 5.21

Deployment Dates

The table below lists the deployment date of DRUID v5.21 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| August 17, 2023 | August 31, 2023 | August 31, 2023 | August 31, 2023 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

<a id="Improvements"></a>

## Improvements

- **Calendar Views**.You can now move events to another day on a calendar view by using the drag and drop feature.
- **Generate new conversation context when expired**. Conversations can now be triggered by StartFlow / Alert flows to existing users even independent of the time elapsed from the last chat interaction (the limit of 24 hours / 5 days has been removed).
- **WhatsApp Meta: Guard validation on phone number**. When multiple AI Agents are connected to the same Meta account, WhatsApp will send messages to all AI Agents. DRUID provides you with a new option, **Phone number validation** you can use to ensure the phone number uniqueness per AI Agent.

![](../../Resources/Images/druid%205.21/number%20validation.png)

- **DRUID Data Services - Increased the Query limit to 50k or 100k records**. For hybrid and on premise DRUID deployments, you can now operate with larger data volumes when using the "Query entity" and "Query related entity" integration tasks.

<a id="BugFixes"></a>

## Bug Fixes

- Intent rephrase flow fixes:

- Triggering rephrase flow by it's own utterance no longer enters a loop (does not trigger the rephrase flow continuously).
- Hero card (last step, no input mapping): Intent.Text is now populated with the button value instead of the button label.
