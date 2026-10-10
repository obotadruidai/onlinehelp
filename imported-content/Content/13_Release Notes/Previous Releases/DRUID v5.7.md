<a id="DRUID57"></a>

# DRUID 5.7

Deployment Dates

The table below lists the deployment date of DRUID v5.7 across Druid Clouds. To view the Druid Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| February 02, 2023 | February 16, 2023 | February 16, 2023 | February 16, 2023 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your Druid tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local Druid partner for more information.

**Required!** This release includes features that require upgrade of your Druid Connector Host to the latest version:

- Custom Code.

<a id="WhatsNew"></a>

## What's New

- **Custom Code**. This release introduces the business operations layer and enables you to implement business rules that always apply either to the flow engine, web views, forms, or external applications. Using the Custom Code integration task, you can perform data validations and raise errors when validation fails or do extensive calculations (e.g., forecast calculations).
> **NOTE:**  If you have a hybrid or on premise DRUID deployment and you want to use the business operations layer you should install DRUID Connector Host version 5.7.

Defining the business rules requires medium to extensive JavaScript knowledge. To streamline the authoring experience, DRUID provides you with a set of predefined code templates.

![](../../Resources/Images/Custom%20Code2/Custom%20Code.png)…<a id="kanchor3"></a>

For more information, see [Custom Code](../../7_Integrations/Custom%20Code.md).

- **Voice AudioCodes channel**. The Voice channel through VoiceAI Connect from AudioCodes enables you to deliver a seamless voice experience to the users talking to your DRUID AI Agents.

![](../../Resources/Images/Voice%20Audio%20Codes%20Channel/Voice%20Audio%20Codes%20Channel.png)

> **IMPORTANT!** This channel is in technology preview as a tenant feature.

This channel provides you with powerful benefits and extensive options to have full control over the conversations authoring. To mention a few:

- Capture a collection of Dual Tone Multi Frequency (DTMF) Digits.
- Provide users with a flawless conversation and avoid interrupting the conversation due to language change.
- Extensive configuration for handling AI Agent delays.
- Configure what happens on conversation disconnect.
- Let VoiceAI Connect know why the AI Agent disconnected a call.

With this new channel, DRUID introduces new features:

- A new system entity field, **[[ChatUser]].CalleePhoneNumber** that stores the AI Agent phone number.
- Two new conversation context entity fields: **[[ChatUser]].VoiceConversationTerminatedReason** and **[[ChatUser]].VoiceConversationTerminatedReasonCode** that store the reason for which the call is disconnected and its associated code.
- Three backchannel steps: **SetVoiceActivityParams**, **SetVoiceSessionParams** and **hangup**.
- New data is logged into the Conversation History which is useful for debugging purposes: all voice conversations begin with **“[Voice start event]”**. that helps you to measure the time from the moment when the call was initiated (AI Agent picks up the call) until the AI Agent says the first message, and **Speech-to-Text Confidence Score** shows the confidence level of the recognition received from the speech-to-text provider.

For more information, see [Voice AudioCodes Channel](../../Channels/Voice%20Audio%20Codes/Voice%20Audio%20Codes%20Channel.md).

- **Kanban views**. Kanban views allow you to work with the graphical visualization of your records. They are a good way to help you stay focused on finishing existing work before starting new work and ensuring that top priority work stays top priority, thus improving efficiency.

![](../../Resources/Images/CBA/kanban%20board.png)

For more information, see [Kanban Views](../../CBA/Kanban%20Views.md)

<a id="Improvements"></a>

## Improvements

- **WhatsApp channel templates** (for both Meta and Nexmo) have been extended to allow authors to add description to hero card buttons
  by for each button in the "buttons" array add the channelData object and set the "description" property.

![](../../Resources/Images/WhatsAppMeta/Multiple%20Cards.png)

For information on how to dd description for hero card buttons, see [WhatsApp Meta Message Templates](../../Channels/WhatsApp%20Integration/WhatsApp%20Meta%20Message%20Templates.md) or [WhatsApp Vonage Message Templates](../../Channels/WhatsApp%20Integration/WhatsApp%20Message%20Templates.md).

- Two new fields are now available in within the conversation context system entity [[ConversationInfo]]:
  **[[ConversationInfo]].CurrentFlow** and **[[ConversationInfo]].PreviousFlow** which store the FlowId, FlowName, FlowDescription and FlowCategory of the current and the previous flow. They provide you with a easy way to trigger back to the previous flow once a trigger flow step is executed.

![](../../Resources/Images/Flows/PREVIOUS%20FLOW.png)

For more information, see [Trigger Flow Steps Configuration](../../4_Flows/Trigger%20Flow%20Steps%20Configuration.md).

- The BF4 webchat widget has been adapted to Conversation time machine translation. When Conversation Time Translation is enabled on the AI Agent, the language selector on the webchat snippet is replaced with a World icon (non-selectable) because user can use other languages than the AI Agent languages. The webchat snippet automatically adapts to the new language code; therefore, if the user sends a voice message in a language different than the AI Agent languages, the voice message will be sent to the STT service in that language.

![](../../Resources/Images/voice%20channel/snippet.png)

For more information about Conversation Time Translation, see [Conversation Time Translation](../../2_AI%20Agents/Conversation%20Time%20Translation.md) and Building Multi-Language AI Agents Using SDL.

<a id="BugFixes"></a>

## Bug Fixes

- Fixed NER issue where InvariantDate field type was not always extracted.
