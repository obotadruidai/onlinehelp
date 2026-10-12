---
title: Druid 9.24
---


Deployment Dates

The table below lists the deployment date of Druid v9.24 across Druid Clouds. To view the Druid Releases Calendar, see [Druid Releases](<../Druid AI Releases.md>).

| Druid Cloud Community \*.community.Druidplatform.com | Druid Cloud US \*.us.Druidplatform.com | Druid Cloud Australia \*au.Druidplatform.com | Druid Cloud West-Europe (PROD) \*.Druidplatform.com |
| ---------------------------------------------------- | -------------------------------------- | -------------------------------------------- | --------------------------------------------------- |
| June 04, 2026                                        | July 02, 2026                          | July 02, 2026                                | July 02, 2026                                       |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your Druid tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local Druid partner for more information.

**Recommended!** This release includes features that require upgrade of your Druid Connector Host :

* Basic Authentication for REST Apps

## Improvements

* **Basic Authentication for REST Apps**. REST Apps now support Basic Authentication, allowing authors to configure a username and password that are automatically Base64-encoded and included in the Authorization header of REST API requests.

![](<../../../.gitbook/assets/basic auth header.png>)

This enhancement simplifies integrations with APIs that require HTTP Basic Authentication and improves compatibility with authenticated endpoints and redirect-based authentication flows, reducing the need for custom authentication handling. For more information, see [Basic Authentication](https://druidai.gitbook.io/druid-ai-docs/integrations/enterprise-connectors/rest/rest-apps/basic-authentication).

* **Enhanced Conversation Transcript JSON Export**. We've enhanced conversation transcript exports to provide deeper visibility into customer interactions. When exporting conversation transcripts in JSON format using the **GetConversationTranscript** internal action, each message now includes an **OriginatorCode** that identifies whether it was sent by:
* A user interacting with the AI Agent
* The AI Agent itself
* A live agent
* A user interacting with a live agent

The existing **Originator** property remains unchanged, ensuring full backward compatibility with existing configurations.

**Conversation Transcript - JSON Output Example**

```
[
   {
        "Originator": "user",
        "Timestamp": "2026-06-02 09:24:30",
        "Message": "Can you please connect me to an agent?",
        "OriginatorCode": 0
   },
   {
        "Originator": "bot",
        "Timestamp": "2026-06-02 09:24:35",
        "Message": "You are now connected to a helpdesk agent.",
        "OriginatorCode": 1
   },
   {
        "Originator": "user",
        "Timestamp": "2026-06-02 09:25:05",
        "Message": "My washing machine is leaking water",
        "OriginatorCode": 4
   },
   {
        "Originator": "agent",
        "Timestamp": "2026-06-02 09:25:40",
        "Message": "Unplug it and then check and tighten hoses",
        "OriginatorCode": 3
   }
]
```

This improvement helps teams:

* Better analyze customer journeys across AI Agent and human-assisted interactions
* Build more accurate reporting and dashboards
* Send richer conversation data to CRMs, ticketing systems, and other external systems.

For more information, see [GetConversationTranscript](https://druidai.gitbook.io/druid-ai-docs/build-ai-agents/authoring-tools/flows/conversational-flows/internal-actions#GetConve) and [\[\[ConversationInfo\]\]](https://druidai.gitbook.io/druid-ai-docs/build-ai-agents/authoring-tools/ai-agent-informational-model/system-entities#\[\[Conver).

* **WebChat Voice Channel - Speechmatics Custom Dictionary Support**. You can now configure Custom Dictionary entries for the Speechmatics speech-to-text provider used in the WebChat Voice channel.

![](<../../../.gitbook/assets/speechmatics dictionary.png>)

Custom dictionaries help improve transcription accuracy for organization-specific terminology, including product names, brand names, acronyms, and technical vocabulary. You can also define alternative pronunciations for custom terms, helping Speechmatics recognize specialized words more reliably.

This enhancement improves transcript quality and helps ensure that business-specific terminology is captured correctly during voice interactions. For more information, see .

* **Improved Enforcement of Block User Input**. When **Block User Input** is enabled on a flow step, feedback reactions are now automatically hidden. This enhancement prevents feedback reactions from interfering with flow steps that are waiting for a specific user response, resulting in a more consistent and predictable user experience.

The change applies to **Hero Card**, **Choice**, **Thumbnail Card**, **Adaptive Card**, and **OAuth 2.0 Sign-In** steps.

* **Mistral (Voxtral) Support for Druid SIP**. Druid SIP now supports Mistral AI (Voxtral models) as speech provider for both Speech-to-Text (STT) and Text-to-Speech (TTS). This enhancement gives organizations additional flexibility when configuring voice interactions, enabling them to leverage Mistral's speech capabilities for real-time voice conversations while maintaining a seamless integration experience within Druid Voice.

## Bug Fixes

* **Telegram- Improved Rendering of Mathematical Expressions**. Fixed an issue in the Telegram channel where mathematical formulas could be displayed incorrectly due to character escaping, making expressions difficult to read and interpret. Mathematical formulas are now rendered correctly with the appropriate symbols and formatting, including division, multiplication, and percentage operators, improving readability and the overall user experience.
