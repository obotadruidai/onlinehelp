---
layout:
  title:
    visible: false
---

<a id="Druid925"></a>

# Druid 9.25

Deployment Dates

The table below lists the deployment date of Druid 9.25 across Druid Clouds. To view the Druid Releases Calendar, see [Druid Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| June 18, 2026 | July 02, 2026 | July 02, 2026 | July 02, 2026 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your Druid tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local Druid partner for more information.

**Recommended!** This release includes features that require upgrade of your Druid Connector Host:

- REST Custom Authentication with JWT Assertion

<a id="WhatsNew"></a>

## What's New

- **Chart Authoring with AI**.
  We are excited to introduce AI-assisted chart authoring to streamline your visualization workflows! Available in this release, this capability transforms your visual data requirements into functional chart configurations through guided chat interactions. By leveraging conversational AI, you can significantly reduce manual configuration effort and accelerate the chart creation process.

Create chart from scratch

![](../../Resources/Images/AI%20Authoring%20Agents/chart%20druid%20help.png)

Fine-tune existing charts

![](../../Resources/Images/AI%20Authoring%20Agents/author%20with%20ai.png)

For more information, see [AI Authoring Agents](../../2_AI%20Agents/AI%20Authoring%20Agents.md).

<a id="Improvements"></a>

## Improvements

- **Druid SIP Improvements**. This release introduces significant enhancements to the Druid SIP, which connects external telephony systems to your voice-enabled AI Agents. These updates are designed to simplify your platform setup workflows and streamline authoring for live voice interactions.

- **Reorganized Configuration Layout**. The Druid SIP settings interface has been restructured into logical, intuitive tabs (General, Call Settings, and Speech). This makes managing your telephony trunk parameters faster and more organized.
- **Streamlined Allowed IPs Management**. Managing authorized signaling addresses from your telephony provider is now easier than ever. The updated interface introduces a clean, structured table configuration with dropdown menus for flexible matching types alongside direct inline editing and port mappings.

![](../../Resources/Images/Druid%20Voice/druid%20sip%20rn.png)

- **Language Detection for Speech-to-Text (STT)**. Voice recognition capabilities have been expanded. The Speech-to-Text configuration now supports automatic language detection modes (At Start or Continuous), allowing your voice AI Agent to intelligently track or adapt to the language spoken by the caller during the call.

![](../../Resources/Images/Druid%20Voice/langauge%20det%20mode.png)

- **Native Call Recording Support**. You can now capture and store raw audio recordings of voice interactions directly through the platform.

![](../../Resources/Images/Druid%20Voice/call%20settings.png)

- **Dedicated Voice Interaction improvement in the Conversation History**. You can now access detailed call transcripts, view precise caller/callee metadata and operational performance metrics, and access audio recordings—complete with interactive playback controls, visual audio waveforms, and direct download links.

![](../../Resources/Images/Druid%20Voice/voice%20conv%20transcript.png)

For more information, see [Configure Druid SIP Connectivity](../../Druid%20Voice/Configure%20Druid%20SIP%20Connectivity.md) and [Voice Conversation History](../../Druid%20Voice/Voice%20Conversation%20History.md).

- **Speech Synthesis Markup Language (SSML) Support for Voice-Enabled Flows**. We have expanded the capabilities of the Voice settings within flow steps to give authors total control over how AI Agents sound during voice interactions. The **Speak message** fields on flow steps now natively accept and forward SSML strings directly to your configured Text-to-Speech (TTS) engine (such as Azure Speech Services or AudioCodes channels).

Instead of relying on rigid, flat text conversions, conversation authors can now leverage xml-based SSML tags directly inside flow steps to explicitly manipulate:

- **Prosody & pacing**. Adjust vocal pitch, volume levels, and precise speaking speed (e.g., slowing down when reciting account digits).
- **Natural pausing**. Inject deliberate silence gaps between distinct options to improve caller comprehension on phone menus.
- **Emotional expressions**. Apply distinct speaking styles (such as cheerful, empathetic, or customer-service personas) supported by your neural voice provider to better match the context of the user interaction.

For more information, see [Voice](../../4_Flows/Voice.md).

- **Outlook Channel-Specific Inactivity Management**. Managing long-form, asynchronous conversations over email requires a much different pacing than instant live chat. We have introduced independent, channel-level conversation lifecycles and inactivity timeouts for the Outlook channel to give you complete control over email-driven interactions. For more information, see [Outlook](../../Channels/Outlook.md).

![](../../Resources/Images/druid%209.25/outlook.png)

- **Code Extension - Programmatic Business Exception Handling**. We have introduced the `Context.RaiseError()` method to the Code Extension to unify business logic validations with technical exception paths within the Flow Engine. By programmatically triggering an exception when custom business rules fail, the method eliminates the need for complex, branched visual routing in the Flow Designer. Instead, it automatically intercepts the failure and dynamically routes the conversation down your existing exception configuration—either directly following the step-level **Error Handler** path or falling back to the **Exception flow** configured in the AI Agent Dialogue Management settings. For more information, see [Context.RaiseError](../../4_Flows/Code%20Extension.md#Context.).
- **REST Custom Authentication - Custom Code**.
  Added support for Custom Code in the **Authenticate Client connector action**. You can use the Custom Code task to perform advanced processing directly before triggering the **Authenticate Client** integration task—such as Server-to-Server authentication with JWT Assertion by locally generating a signed, short-lived cryptographic assertion using custom claims, RSA signatures, or custom JWT headers, storing the assertion in a context variable, and passing it to the authentication endpoint. For more information, see [Advanced Dynamic Authentication](../../7_Integrations/REST/Advanced%20Dynamic%20Authentication.md) and [JWT Assertion Authentication Examples via Custom Code](../../7_Integrations/REST/JWT%20Assertion%20Authentication%20Examples%20via%20Custom%20Code.md).
- **Improved [[SystemError]] Message**. Enhanced the **[[SystemError]].Message** field to include both the primary error message and any additional error details returned by the system. This provides AI Agent authors with more complete diagnostic information, making troubleshooting and automated exception handling easier and more accurate. For more information, see [\[\[SystemError\]\]](../../5_Entities/System%20Entities.md#%5B%5BSystem).
- Druid Conductor **Explainability**. We are excited to extend Explainability to the Druid Conductor level. Previously available only for individual AI Agents, Explainability now provides a centralized, end-to-end view of how the orchestration layer interprets, routes, and processes user requests.

![](../../Resources/Images/Annotation%20Tool/conductor%20explain.png)

For more information, see [Explainability and Utterances Annotation](../../Governance%20%26%20Security/Explainability%20and%20Utterances%20Annotation.md#ExplainabilityatDruidConductorLevel).

- **Knowledge Base - New Standard PDF Extractor**. Starting with this release, the advanced PDF extraction engine previously available as **Elpis** is the new **Standard** and is automatically selected for all newly created Knowledge Bases. This change simplifies extractor selection while ensuring users benefit from improved document parsing capabilities, including support for multimedia-rich PDFs, image extraction, and more accurate processing of complex document structures. The previous Standard extractor remains available as **Standard (Deprecated)** to ensure backward compatibility with existing configurations. For more information, see [File Extractors](../../Knowledgebase/KB%20Settings/File%20Extractors.md#PDF%20Extractors).

![](../../Resources/Images/druid%209.25/pdf%20extractors.png)

> **Info:** Existing Knowledge Bases retain their current PDF extractor configuration. To view the updated extractor names in the PDF extractor drop-down, reset the Knowledge Base advanced settings.

- **Enhanced Advanced Data Editor for Charts**. To give authors more control and visibility when customizing charts, we have redesigned the advanced chart editor experience. The JSON field formerly known as the **Advanced Editor** has been renamed to the **Advanced data editor** and upgraded from a single JSON field to a dual-pane interface:

- **Default Query** (Readonly): Displays the current chart data query for easy reference.
- **Custom Query** (Editable): Select **Custom Query** and input your own custom code. This allows you to tailor chart configurations and advanced behaviors exactly to your preferences. For advanced customization, you can directly implement standard Chart.js configurations and documentation samples.

![](../../Resources/Images/Charts/advanced%20data%20editor.png)
