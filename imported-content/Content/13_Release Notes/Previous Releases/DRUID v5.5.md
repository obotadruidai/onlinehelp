---
layout:
  title:
    visible: false
---

<a id="DRUID55"></a>

# DRUID 5.5

Deployment Dates

The table below lists the deployment date of DRUID v5.5 across Druid Clouds. To view the Druid Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| January 05, 2023 | January 19, 2023 | January 19, 2023 | January 19, 2023 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your Druid tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local Druid partner for more information.

<a id="WhatsNew"></a>

## What's New

- **Salesforce Live Chat**. A new Live Chat provider, Salesforce is now available in DRUID, which allows you to integrate Salesforce Live Chat and AI Agents.

![](../../Resources/Images/Live%20Chat/SALESFORCE%20PROVIDER.png)

For more information, see [Salesforce Live Chat](../../Live%20Chat/Salesforce%20Live%20Chat.md).

<a id="Improvements"></a>

## Improvements

- For hero, choice and thumbnail steps, you can now customize the label of the **Options** button shown in WhatsApp channel. For more information, see [WhatsApp Meta Message Templates](../../Channels/WhatsApp%20Integration/WhatsApp%20Meta%20Message%20Templates.md).
- DRUID supports uploading a new file extension, **.vcf**, the standard file format for storing contact information for a person or business.
- In entity configuration page, two new entity details are available: **Plural Name** and **IconURL** which have effect on the workspaces menu when the entity is added as workspace link.

![](../../Resources/Images/release%205.5/entity%20details.png)

- **Annotation tool**. A new status is now available in the Conversation History, **False Match**. When the user annotates a phrase into a flow (the flow in which the model should have matched in the first place) its status changes to "False Match".

![](../../Resources/Images/release%205.5/false%20match.png)

When reviewing the quality of the model, the user also has the possibility to manually change the status of a phrase to "False Match".

![](../../Resources/Images/release%205.5/false%20macth%20manual.png)

- This release introduces a new style guide for notification status.

![](../../Resources/Images/release%205.5/notific%20status.png)

- When an error occurs on solution import, the reason for import failure now appears in the UI, you no longer have to download the error log file (JSON file) for details.

<a id="BugFixes"></a>

## Bug Fixes

- On flow steps and code editor, the Save button is disabled after click until the save action completes in the backend.
