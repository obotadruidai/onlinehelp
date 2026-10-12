---
title: Druid Portal Cookies Policy
---


A cookie is a small file that is downloaded to your computer when you access specific web pages. Cookies allow a web page to store and retrieve information about the users browsing or their machines. Based on the information the cookies contain, you can use them to recognize users and allow them efficiently surf the web pages.

## What types of cookies does DRUID use?

{% hint style="warning" %}
**IMPORTANT!** AI Agent widgets never store user personal data and neither sensitive data in their cookies.
{% endhint %}

Cookies used by Druid AI Agents fall under these two categories:

* **Business cookies**. These cookies are created by the webchat widget and store the conversation identifier and widget expand / collapse state only.
* **Authoring portal cookies**. These are technical cookies set by the Druid Portal. These cookies are exempt from configuration.

The table below provides detailed information about the cookies Druid AI Agents widgets use.

| Cookie                       | Purpose                                                                                                                                                                  | Cookie type                | Can be customized | Notes                                                                                                                                                                                                                                                                                                                                                         |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| druidConversationToken       | Stores the ConversationId used by the webchat widget to resume a conversation by loading the chat history.                                                               | Business (webchat snippet) | YES               | The cookie is functional. AI Agents can operate without it, but this will affect the user experience. Without this cookie, any page refresh will start a new conversation. The cookie is strictly necessary for maintaining the continuity of the user’s session. Without it, any page refresh will start a new conversation, disrupting the user experience. |
| druidWebChatIsOpened         | Keeps the webchat widget open or closed when navigating through sub-pages of the web page hosting the AI Agent.                                                          | Business (webchat snippet) |                   |                                                                                                                                                                                                                                                                                                                                                               |
| druidConversationLanguage    | Used by bot framework version 4 webchat widget to keep the conversation language set in the chat widget.                                                                 | Business (webchat snippet) | NO                |                                                                                                                                                                                                                                                                                                                                                               |
| ARRAffinity                  | Load-balancing cookie to route the request made through a web browser to the same server in any browsing session. **NOTE:** The cookie is deprecated starting DRUID 7.0. | Authoring Portal           | NO                |                                                                                                                                                                                                                                                                                                                                                               |
| ARRAffinitySameSite          | Load-balancing cookie to route the request made through a web browser to the same server in any browsing session. **NOTE:** The cookie is deprecated starting DRUID 7.0. | Authoring Portal           |                   |                                                                                                                                                                                                                                                                                                                                                               |
| Abp.AuthToken                | Keeps the authentication token and state, so that authors can use multiple browser tabs under the same account.                                                          | Authoring Portal           | NO                | The cookie is strictly necessary for maintaining author authentication. Without it, any button click will log out the author.                                                                                                                                                                                                                                 |
| Abp.TenantId                 | Keeps the ID of the Druid Authoring tenant.                                                                                                                              | Authoring Portal           | NO                | The cookie is strictly necessary for maintaining the ID of the Druid Authoring tenant.                                                                                                                                                                                                                                                                        |
| Abp.Localization.CultureName | Keeps the authoring language set in the Druid Portal.                                                                                                                    | Authoring Portal           | NO                |                                                                                                                                                                                                                                                                                                                                                               |
| ai\_user                     | Technical cookie, used for platform metrics. **NOTE:** The cookie is deprecated starting DRUID 7.0.                                                                      | Authoring Portal           | NO                |                                                                                                                                                                                                                                                                                                                                                               |

## How to modify the configuration of cookies

By default, AI Agent widgets cookies are created in a way that allows the cookies to be read across sub-domains by setting the "cookieDomain" attribute in the cookie options. Druid derives the proper domain value by parsing the host site's domain and extracting it.

_Bot framework 4_

![](<../.gitbook/assets/Druid Portal Cookies Policy_1.png>)

You are able to manage the preferences of the session cookies from the AI Agent details, Theme section, webchat snippet:

*   If you are using bot framework v3, click the **Edit Parameters** button and change the value (true / false) of the following parameters based on your preferences: “conversationTokenEnabled” and / or “druidWebChatIsOpenedEnabled”. By default, these settings and the associated cookies are enabled (their value is true).

    ![](<../.gitbook/assets/Druid Portal Cookies Policy_2.png>)
* If you are using bot framework v4, click the **Customize webchat** button. The Customize Your Webchat UI editor appears. On the editor menu, click **General**, and then click **Cookies** to expand the cookies section. By default, these cookie settings “conversationTokenEnabled” and “druidWebChatIsOpenedEnabled” are enabled. To disable them based on your preferences, untick the setting for the desired cookie(s).

![](<../.gitbook/assets/Druid Portal Cookies Policy_3.png>)

## Changes to this policy

DRUID S.A. reserves the right to change these guidelines at any time.
