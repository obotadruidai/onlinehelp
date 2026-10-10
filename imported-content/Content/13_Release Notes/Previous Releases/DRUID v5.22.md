---
title: "DRUID 5.22"
---

<a id="DRUID522"></a>


Deployment Dates

The table below lists the deployment date of DRUID v5.22 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| August 31, 2023 | September 28, 2023 | September 28, 2023 | September 28, 2023 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

<a id="WhatsNew"></a>

## What's New

- **Code Editor on forms** - The Code Editor is now available on web forms that allows you to perform automations on form load or save, on a specific field change or on a specific tab change. Using the Code Editor on forms eliminates the need to use the Custom Code integration task on form automations (create / update form).

![](../../Resources/Images/CBA/code%20editor.png)

For more information, see [Using the Code Editor on Forms](../../CBA/Trigger%20Events%20on%20Forms.md).

- **Filter columns on web views**. In addition to ascending / descending ordering the records in a view, extended filtering is now available in web views for columns which contain data of type string, integer and decimal.

  ![](../../Resources/Images/CBA/filetring%20rules.png)

  For more information, see [Filtering records in a view](../../CBA/Filtering%20records%20in%20a%20view.md).
- **[[QueryParams]] system entity - new parameters**. Two new parameters are now available in [[QueryParams]], PortalUserId and PortalUserToken which are taken from the AuthorizeAsync method. You can use them to create a link for web views and forms or another link from the Portal that requires PortalUserToken, instead of calling an authorize API.

<a id="Improvements"></a>

## Improvements

- **Flow Diagram improvements**. For a parent flow with a child flow that triggers the parent flow, if you expand the child flow and inside it you expand the step that triggers the parent flow, the parent flow is highlighted on the Flow Diagram and you can update it (add / delete update steps, conditions, etc.).

![](../../Resources/Images/druid%205.22/expanded%20flows.png)

- **Knowledgebase - unstructured data sources**. When crawling website content the artifacts regarding cookies are lo longer extracted. The extracted articles only contain the relevant text.

![](../../Resources/Images/druid%205.22/crawling.png)

<a id="BugFixes"></a>

## Bug Fixes

- Channels: Even if the Step Message is empty, the Hero/Thumbnail buttons are now rendered in the following channels: Instagram, WhatsApp Vonage and Sunshine Conversations apps.
- Disabling Exception Handler on a flow step now removes the exception step from the Flow diagram.
