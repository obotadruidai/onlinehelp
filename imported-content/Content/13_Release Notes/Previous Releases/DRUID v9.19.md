---
layout:
  title:
    visible: false
---

<a id="Druid919"></a>

# Druid 9.19

Deployment Dates

The table below lists the deployment date of Druid v9.19 across Druid Clouds. To view the Druid Releases Calendar, see [Druid Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| March 26, 2026 | April 14, 2026 | April 14, 2026 | April 14, 2026 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your Druid tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local Druid partner for more information.

<a id="WhatsNew"></a>

## What's New

- **Enhanced Security – Druid Portal Access Control via IP Whitelisting**. To provide an additional layer of protection for enterprise environments, this release introduces Portal Login IP Whitelisting. Portal administrators can restrict access to the Druid Portal to specific authorized IPs or networks, such as corporate locations or secure VPN gateways. The restriction applies to all authentication methods, including standard user credentials and Single Sign-On (SSO), and supports both individual IP addresses and CIDR notation.

![](../../Resources/Images/DRUID%209.19/ip%20whitelisting.png)

> **NOTE:** For Druid Connector Host hybrid deployments, you **must** whitelist the IP address of the host machine to ensure uninterrupted service.

For more information, see [Enforce Druid Portal Access via IP Whitelisting](../../Governance%20%26%20Security/User%20Management/Enforce%20Druid%20Portal%20Access%20via%20IP%20Whitelisting.md).

- **Support for Azure OpenAI /Responses API**. We have introduced support for the `/Responses` API for Azure OpenAI models. This update allows the AI Agent to provide higher quality and more efficient responses.

For GPT OSS full on premise installation, the model can now be consumed across the entire Druid AI Platform. This ensures a consistent, high-performance LLM experience even in fully local environments.

Available capabilities include:

- Real-time response generation

![](../../Resources/Images/Flows/LLM%20STREAMER.png)

For more information, see [Use LLM Response Streaming for Voice Interactions](../../4_Flows/Use%20LLM%20Response%20Streaming%20for%20Voice%20Interactions.md).

- Enhanced intent recognition

![](../../Resources/Images/Conv%20AI/nluw%20iytth%20llm.png)

For more information, see [NLU Intents Classification with LLM](../../Conversational%20AI/NLU%20Intents%20Classification.md).

- KB Advanced settings - Generative Endpoints (LLM chunker)

![](../../Resources/Images/Bots/machien%20translation.png)

For more information, see [Generative Endpoints](../../Knowledgebase/KB%20Settings/Generative%20Endpoints.md#API).

- Machine Translation with LLM

![](../../Resources/Images/Bots/machien%20translation.png)

For more information, see [Using Machine Translation](../../2_AI%20Agents/Using%20Machine%20Translation.md#Use).

- **Soniox Speech-To-Text (STT) Support**. Elevate your voice-based AI Agents with our new Soniox STT integration. Complementing our existing list of STT providers, Soniox introduces semantic endpointing to intelligently detect when a user has finished speaking based on context rather than just silence. This integration ensures "human-parity" accuracy across 60+ languages and natively supports multilingual code-switching, allowing the AI Agent to follow conversations seamlessly even when users switch languages mid-sentence.

![](../../Resources/Images/voice%20channel/deepgram%20setup.png)

For more information, see Enable voice interactions in the Web channel.

<a id="Improvements"></a>

## Improvements

- **Enhanced Voice Message Logging**. Conversation History now records the exact message delivered to users in voice-based flows. For voice channels (such as Audiocodes and VoiceText), the system captures the content defined in the Speak field of the Voice section for each flow step. This update ensures the audit trail reflects what users actually hear, instead of the default message from the General section.
- **AudioCodes - Transfer Event Logging**. We have enhanced the visibility of handoffs in AudioCodes voice channel. When a conversation is transferred to a contact center queue via the **transfer** backchannel flow step, the platform now records a new ChatActivity event in the Conversation History. This improvement offers the following benefits:

- **Improved traceability**: A “Connected with agent” event is logged the moment the transfer request is successfully sent from Druid to the contact center.
- **Routing confirmation**: Since contact centers do not typically return a confirmation once a live agent actually picks up, this event serves as the definitive record that the routing action was initiated by the AI Agent.
- **Audit accuracy**: This update ensures that the Conversation History accurately reflects the transition from the AI Agent to the external queue, providing better data for session lifecycle tracking.

![](../../Resources/Images/DRUID%209.19/AUDIOCODES.png)

- **RingCentral – Location Sharing Support**. Authors can now use the Location flow step to request and receive geographical data from users interacting via RingCentral. With this update, AI Agents deployed on RingCentral can:

- Capture and store users' geographical location shared in the chat (stored in the [[GeoLocation]] system entity or a custom entity field).
- Share a specific location with users in the chat, rendered similar to a Google Maps preview.

For more information, see [Location steps](../../4_Flows/Location_Flow_Steps.md).

- **Outlook Channel – Conversation Management Enhancement**. Added a new configuration option to control how email threads are handled. A **Treat emails as separate conversations** toggle is now available in the Outlook channel settings. When enabled, each incoming email is processed as a new conversation, even if it belongs to an existing thread. This is useful for service desk scenarios where every email must be handled as an independent request or ticket.

![](../../Resources/Images/DRUID%209.19/outlook%20config.png)

- **Webhooks - External File Ingestion**. We have introduced the `/GenericIntegrationFileTransfer` endpoint to simplify how external systems send documents to Druid. By supporting multipart/form-data, this new endpoint provides a standardized way to upload files in Druid via integrations.  For more information, see [Uploading Files from External Systems to Druid](../../Webhooks/Uploading%20Files%20from%20External%20Systems%20to%20Druid.md).
- **Facebook Data Deletion Support**. We have introduced a new special flow to help organizations comply with Facebook's data privacy policies. When a user requests data deletion via Facebook, Druid can now automatically trigger a designated **Facebook data deletion flow**. This allows authors to programmatically anonymize or delete user data from the Conversation History and internal entities, ensuring full compliance with GDPR and platform-specific privacy requirements. For more information, see [Facebook Data Deletion Flow](../../4_Flows/Facebook%20Data%20Deletion%20Flow.md).
- **Microsoft Teams Channel – RBAC with Microsoft Entra ID Groups**. Starting with this release, you can configure the Teams channel to retrieve users’ security groups from Microsoft Entra ID (formerly Azure AD). This enables role-based access control for operational flows, allowing you to grant or restrict access based on the user’s organizational groups.

![](../../Resources/Images/MS%20Teams/2026-03-24_21-04-33.png)

For more information, see [Implement Role-Based Access Control via Microsoft Entra ID Groups](../../Channels/MS%20Teams/MS%20Teams%20Integration.md#Implemen).

- **Talkdesk Live Chat - File Transfer Support**. Starting with this release, file transfer between users and agents is supported for the Talkdesk integration. This allows both parties to exchange attachments seamlessly during a live chat session. To enable this functionality, you must add the following scopes to your Talkdesk OAuth Client:

- attachments:download
- attachments:read
- attachments:request
- attachments:write

![](../../Resources/Images/Talkdesk/attachment%20scopes.png)

For more information, see [Talkdesk Live Chat](../../Live%20Chat/Talkdesk%20Live%20Chat.md).

- **RingCentral CX- Conversation End Support**. Starting with this release, Druid supports the conversation end event for the RingCentral CX integration. This ensures that the session closes immediately when the conversation ends in RingCentral CX, rather than waiting for the **Live chat conversation idle timeout mins** threshold. To enable this functionality, you must create a webhook in RingCentral CX.

For more information, see [Step 3. Create conversation end webhook in RingCentral CX](../../Live%20Chat/RingCentral%20CX.md#Step).

- **AI Agent - Default Language Protection**. To ensure the integrity of your AI Agent configuration, once an AI Agent initial configuration is saved, the default language becomes read-only. This restriction prevents accidental changes that could break existing flows, intent recognition, or language-specific entity configurations.
> **Info:** Always verify the primary language of your AI Agent during the initial creation process. If a different default language is required for a new project, a new AI Agent must be created.

- **Knowledge Base - Support for Google MIME Types in All Data Sources**. Starting with this release, the Knowledge Base supports Google MIME type files across all data sources. Previously, Google native files (such as Google Docs, Google Sheets, and Google Slides) required conversion before they could be processed in the Knowledge Base. Druid now automatically supports these file formats, allowing you to upload Google file types directly to any data source.
- **KB File Extractors - OCR & Image Extraction**. We have introduced a new capability to convert visual content into searchable knowledge. For specific file types, authors can now enable OCR for pictures within the file extractor settings, **Use OCR for pictures** (Default: False).

When set to **True**, the extractor identifies images within the document and performs Optical Character Recognition (OCR) to convert them into text. This text is then indexed in the Knowledge Base, making the content of diagrams, screenshots, or scanned text fully searchable.

Supported Extractors:

- **DOC / DOCX**: Standard extractor.
- **HTML**: Standard extractor.
- **PDF**: Elpis and Daguerre extractors.

For more information, see [File Extractors](../../Knowledgebase/KB%20Settings/File%20Extractors.md).

<a id="BugFixes"></a>

## Bug Fixes

- **Outlook Channel – HTML Rendering Fix**. Fixed an issue where messages containing HTML were delivered as plain text in email responses. Messages sent through the Outlook channel now correctly render HTML content, ensuring users receive properly formatted emails.
