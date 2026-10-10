---
title: "DRUID 5.6"
---

<a id="DRUID56"></a>


Deployment Dates

The table below lists the deployment date of DRUID v5.6 across Druid Clouds. To view the Druid Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| January 19, 2023 | February 16, 2023 | February 16, 2023 | February 16, 2023 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your Druid tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local Druid partner for more information.

<a id="WhatsNew"></a>

## What's New

- **Search views**. To enhance the user-friendliness, the authors can add a search bar to the views list which is consumed from the **Data** tab defined on the entity or from Workspaces. The search view bar enables authors and workspace users to quickly search for specific views.

![](../../Resources/Images/CBA/SEARCH%20BAR.png)

![](../../Resources/Images/CBA/search%20in%20workspaces.png)

In this regard, this release introduces the following:

- Two types of views: **Table View** used for creating views and **Quick Search** used for creating a search view (a view that shows the search results).

![](../../Resources/Images/CBA/view%20type.png)

- The **Details** of the quick search view is shown when hovering the mouse over the search bar.

![](../../Resources/Images/CBA/search%20view%20details.png)

- Specific definition of the quick search view columns and view data via a dedicated query entity integration.

For more information, see [Add Search View Bar](../../CBA/Add%20Search%20View%20Bar.md).

<a id="Improvements"></a>

## Improvements

- Added multiple language support for the LiveChatPauseKeyword (“Pause”) in Live Chat functionality.

On the AI Agent details, Live Chat section, you can now provide the LiveChatPauseKeyword in all AI Agent additional languages. By default, the keyword is provided in English (en-US) and Romanian (ro). To add the LiveChatPauseKeyword on the AI Agent you can either provide keyword in additional AI Agent languages and the keyword is automatically added to the AI Agent or first add it on the AI Agent by clicking the plus icon and then provide the keyword in AI Agent additional languages.

![](../../Resources/Images/Live%20Chat/pause%20keyword%20button.png)

![](../../Resources/Images/Live%20Chat/pause%20keyword.png)

Whenever the agent pauses the conversation, the LiveChatPauseKeyword is sent in the chat in the conversation language, if keyword value was set in that language on the AI Agent, otherwise the value in EN is provided.

![](../../Resources/Images/Live%20Chat/pause%20in%20the%20chat.png)

<a id="BugFixes"></a>

## Bug Fixes

- Fixed solution export issue: in some cases, internal server error occurred.
