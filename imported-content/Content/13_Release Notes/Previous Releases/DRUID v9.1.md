<a id="Druid91"></a>

# Druid 9.1

Deployment Dates

The table below lists the deployment date of DRUID v9.1 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| July 17, 2025 | July 31, 2025 | July 31, 2025 | July 31, 2025 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host:

- Conversation History – Improved logging for translated messages
- Custom code improvements
- Druid Services Apps – Concatenated Base URL support
- SAML-based SSO authentication

<a id="WhatsNew"></a>

## What's New

- **Multilingual AI Agents – Real-Time Translation with LLM**. You can now use LLM to translate user messages in real time during conversations. This enables smoother multilingual AI Agent interactions and improves understanding across languages.
> **NOTE:** LLM machine translation is available **only for conversation time translation**.

![](../../Resources/Images/druid%209.1/llm%20translation.png)

For more information, see [Using Machine Translation](../../2_AI%20Agents/Using%20Machine%20Translation.md).

- **Webchat and Multichat - Deepgram STT Support**.DRUID now supports speech-to-text (STT) for the Webchat and Multichat using any available Deepgram model, giving you the flexibility to choose the best fit for your use case. This includes specialized models like Nova-2 Medical, which is optimized for clinical conversations and medical terminology—ideal for healthcare environments such as telemedicine and patient consultations. You can select the Deepgram model that best aligns with your domain and transcription accuracy needs.

![](../../Resources/Images/druid%209.1/DEEPGRAM.png)

![](../../Resources/Images/druid%209.1/stt%20deepgram.png)

For information how to set it up, see the Voice Channel.

- **SAML-based SSO authentication**. You can now integrate DRUID with external identity providers using the SAML protocol for Single Sign-On (SSO). This enables secure user authentication through your organization’s existing identity management system.

For more information, see [SSO Authentication with the SAML Protocol](../../7_Integrations/SamlAuth/SSO%20Authentication%20with%20SAML.md).

<a id="Improvements"></a>

## Improvements

- **Vonage Voice Channel improvements**. This release introduces two new improvements to the Vonage Voice channel:

- **SIP Forwarding Support**. Starting with this release, the Vonage Voice channel supports forwarding incoming voice calls to a Session Initiation Protocol (SIP) endpoint. This enhancement enables more flexible call routing and better integration with your existing telephony infrastructure.

![](../../Resources/Images/druid%209.1/sip.png)

For more information, see [Vonage Voice](../../Channels/Vonage_Voice.md).

- **Sending Call Parameters**. We've introduced the ability to send call parameters to Vonage Voice when a call is initiated. This enhancement provides greater control and allows you to integrate additional relevant data directly into your Vonage call flows, leading to more dynamic and tailored interactions.

![](../../Resources/Images/druid%209.1/vonage%20voice%20oparams.png)

For more information, see [Vonage Voice](../../Channels/Vonage_Voice.md).

- **New LLM Provider: Mesolitica MaLLaM**. You can now use MaLLaM as a large language model (LLM) provider for the Knowledge Base and NLU intent classification with LLM. MaLLaM is a state-of-the-art Malay language model developed by Mesolitica, offering improved accuracy for intent detection in Malaysian dialects and contexts.

![](../../Resources/Images/druid%209.1/mallaam.png)

![](../../Resources/Images/druid%209.1/kb%20mesolitica.png)

- **Conversation History – Improved logging for translated messages**. Translated messages are now clearly identified in the conversation history, Flow Log. You can easily see which messages were translated, along with the source and target languages used.
> **NOTE:** Improved logging for translated messages requires Connector Host upgrade to version 9.1.

![](../../Resources/Images/druid%209.1/translated%20messages.png)

- **Custom Code – `toLocaleString()` method support**. DRUID Custom Code does not natively support JavaScript’s toLocaleString() method. To provide equivalent functionality, we’ve introduced a new utility method:

DateTimeUtils.StringifyDate(date, format)

You can use this method in your Custom Code to convert date objects into localized string formats. The format parameter allows you to control the output structure based on your regional or display preferences.

![](../../Resources/Images/druid%209.1/TOlOCALEsTRING.png)

For more information, see [Custom Code](../../7_Integrations/Custom%20Code.md).

- **Custom Code - New utility methods: Base64 Encoding and Decoding**. You can now use `StringUtils.Base64Encode()` and `StringUtils.Base64Decode()` in Custom Code to safely encode and decode data. These methods are useful for handling sensitive information in headers, URLs, or other request parts.

![](../../Resources/Images/druid%209.1/base64%20encode.png)

![](../../Resources/Images/druid%209.1/decodeBase64.png)

For more information, see [Custom Code](../../7_Integrations/Custom%20Code.md).

- **Druid Services Apps – Concatenated Base URL support**. You can now dynamically construct the Base URL in a Druid Services app by concatenating a variable that holds the DRUID service URL (e.g., @\_Druid.LLM\_URL) with the API path (e.g., chat/completions).

For example: **@\_Druid.LLM\_URLchat/completions**

![](../../Resources/Images/druid%209.1/BASE%20URL.png)

This enhancement simplifies integrations by allowing flexible, variable-based URL construction—eliminating the need to manually enter or update the full request path.

![](../../Resources/Images/druid%209.1/integration%20url.png)

- **DRUID LLM Resources: gpt-4.1 model**. DRUID now supports the gpt-4.1 model from Azure OpenAI as a configurable LLM resource. To enable this resource for your tenant, please contact [DRUID Support](<mailto:support@druidai.com?subject=DRUID LLM resource: activate gpt-4.1>).
> **NOTE:** Using the gpt-4.1 model will incur additional costs.

- **Knowledge Base - Video Processing (technology preview)**. With this release, DRUID supports video processing to allow data extraction from video content for the following data sources: SharePoint, Custom Data Sources and Website with videos directly hosted (embedded third-party videos like YouTube are not supported).  For more information, see [Extracting Data from Video Files](../../Knowledgebase/Extract%20Data%20from%20Video%20Files.md).
> **NOTE:** This is a tenant feature and requires **Druid Knowledge Base Multimedia Extractor** activation on your tenant. For activation, reach out to [DRUID Support](<mailto:support@druidai.com?subject=Druid KB Multimedia Extractor activation request>).

- **Web Forms – Manual Date Entry**. With this release, you can manually enter dates in Date fields on web forms, offering an alternative to using the date selector. Use the date format set in the Platform; otherwise, DRUID will consider the date invalid.

![](../../Resources/Images/druid%209.1/date%20entry.png)

- **Calendar Views – Event Series Color**. You can now set event series colors based on the colors defined on entity. For example, assign different colors to case statuses, and display cases on the calendar view with colors matching their status.

![](../../Resources/Images/druid%209.1/case%20status.png)

![](../../Resources/Images/druid%209.1/calendar%20view.png)

![](../../Resources/Images/druid%209.1/calendat%20status.png)

<a id="BugFixes"></a>

## Bug Fixes

- **Solution Export/Import**: Fixed an issue where the Limit Intent switch configured on flow steps was not properly retained during solution export/import. The setting is now correctly preserved.
- **Views – Forms – Charts**: Resolved a bug that prevented users from unlinking an entry from a solution.
- **Knowledge Base – article focus**: Fixed an issue where navigating to an article from the bottom of the Search/Predict page didn’t bring the highlighted article into focus.
- **Knowledge Base – File Extractor**: Fixed a bug where the file extractor was not displayed for child nodes in the web interface.
