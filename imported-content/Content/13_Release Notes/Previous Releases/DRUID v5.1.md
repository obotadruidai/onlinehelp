---
layout:
  title:
    visible: false
---

<a id="DRUID51"></a>

# DRUID 5.1

Deployment Dates

The table below lists the deployment date of DRUID v5.1 across Druid Clouds. To view the Druid Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| November 10, 2022 | November 24, 2022 | November 24, 2022 | November 24, 2022 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your Druid tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local Druid partner for more information.

<a id="WhatsNew"></a>

## What's New

- **Code extension** is a powerful feature that enables authors to make small adjustments to the flow steps definition. It is particularly useful in situations when the conversational flow steps behavior needs to align to more complex business rules that cannot be implemented at design time using the graphical Flow Designer.

![](../../Resources/Images/Flows/code%20extension.png)

> **IMPORTANT!** **DO NOT** use Code Extension to completely change the flow steps behavior; otherwise, the AI Agent diagram will no longer provide you with accurate information and you might get confused when analyzing the Conversation History and performing further debugging.

For more information, see [Code Extension](../../4_Flows/Code%20Extension.md).

- **Single Sign On Authentication via OpenID Connect**. You can now leverage the use of a unified authentication system(s) by enabling OpenID Connect authentication with an external Active Directory system. Once you set it up, all your users logging into the Druid Portal with their AD credentials will be automatically provisioned in DRUID at their first login. For information on how to set it up, see [Provisioning Portal Users and Single Sign On Authentication via OpenID Connect](../../Governance%20%26%20Security/User%20Management/Provisioning%20Portal%20Users.md).
- **Chat and Recommended automations available on web forms**. You can design forms to provide your business users with the possibility to chat with the AI Agent in the context of the current entity record and also trigger the execution of a specific conversational flow from a set of recommended automations available on the entity form.

![](../../Resources/Images/CBA/record%20context.png)

![](../../Resources/Images/CBA/automation%20selected.png)

For information on how to design forms to enable the two features for your business users, see [Create and Design Forms](../../CBA/Create%20and%20Design%20Forms.md) (sections *Enable chat in forms* and *Recommend automations on forms*).

- A new AI Agent setting is available at ConversationId level, **Trigger interval** which prevents the Welcome flow from being automatically triggered as long as the trigger time interval threshold is not reached. This is useful when a new chat window is expanded for the same ConversationId. By default, this setting is set to 0 mins, which means that the Welcome flow is always triggered.

![](../../Resources/Images/Bots/bot%20settings.png)

For more information, see [Setting the Welcome Flow](../../4_Flows/Welcome%20Flow.md).

<a id="Improvements"></a>

## Improvements

- Evaluation tool has an **improved Confidence buckets chart** in Conversation History. Besides the possibility to analyze the model classification scores, the authors can decide for each message if the classification was done right, or not and that decision is reflected in the Confidence buckets chart. For more information, see [Annotating Conversation History](../../Data%20Analytics%20%26%20Insights/Annotation/Annotating%20Conversation%20History.md).
- **File Upload steps**. Two new settings are now available on steps of type File Upload: **Allowed file types** and **Max allowed size (KB)**. Authors can use them to restrict users uploading in the chat only files with specific file extension(s) and / or files that have a maximum size.

![](../../Resources/Images/Flows/file%20uplaod%20restrictions.png)

When the flow step is executed, if the file restriction(s) validation fails, DRUID will raise exception [[SystemError]].ExceptionType == “UnsupportedFileType”, which for flow steps with input mapping you can further handle in the flow.

For more information, see [File Upload Steps Configuration](../../4_Flows/File%20Upload%20Steps%20Configuration.md).

- Flows list. This release provides a better overview on the parent and child flows in the Flows List, as follows:

- The flows which are parent flows (they have children associated to them) have the “child” icon, together with the counter of child flows it contains (how many flows have that flow set as parent flow).
- Child flows will have a badge containing the text “Child flow: <parent flow name>”, where the parent flow name is a hyperlink to the parent flow.

![](../../Resources/Images/Flows/child%20intents%20and%20parents.png)

For more information on child intents and parent flows, see [Child Intents](../../4_Flows/Adding%20Intent%20Variations.md).

- In Conversation History v2 grouped by conversations, the **User Name** changes from anonymous to authenticated user in situations when the user started the conversation as anonymous and while in the conversation was authenticated.
- Entity Designer - diagram view only. The entity's Details, Fields, Flows and Integrations are available in the right-side editor under separate tabs.

![](../../Resources/Images/Entities/entitty%20diagram%20view%20details.png)

<a id="BugFixes"></a>

## Bug Fixes

- Evaluation Screens: Accuracy score lines are wrongly placed.
- Uploading and downloading multiple file types didn't work on WhatsApp Meta:
  - Downloading: JSON, ODT, CSV.
  - Uploading: MP4.
- APPs: GetRelatedElements worked with "like" operator instead of "exact match"; if user had APPS with similar names, then integrations were wrongly displayed for the APP in the **Related Elements** tab.
- BF4 editor. Druid StyleSet Custom Style was not saved after save.
- ChangeConversation generated infinite reloading in BF4 Portal AI Agent Landpage.
