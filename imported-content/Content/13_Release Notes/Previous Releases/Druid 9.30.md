---
title: "Druid 9.30"
---

<a id="Druid930"></a>


Deployment Dates

The table below lists the deployment date of Druid 9.30 across Druid Clouds. To view the Druid Releases Calendar, see [Druid Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| August 27, 2026 | September 24, 2026 | September 24, 2026 | September 24, 2026 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your Druid tenant, please contact [support@druidai.com](mailto:support@druidai.com) or your local Druid partner for more information.

**Recommended!** This release includes features that require upgrade of your Druid Connector Host:

- Druid Custom Queries - Support for `ROUND` function

<a id="WhatsNew"></a>

## What's New

- **Enhanced Chat Experience**. The webchat interface introduces a major design evolution centered around customizable **Light and Dark themes**, alongside full support for agentic reasoning and dynamic messaging workflows. Because webchat customization options depend directly on the selected theme, this update empowers authors to tailor the interface to their branding while minimizing visual noise and optimizing the overall conversation area. The cleaner, more intuitive layout provides users with a transparent and engaging conversational experience.

**Key features**

- **Light and Dark Themes**. Select between **Light** and **Dark** visual styles that serve as the foundation for webchat customization, offering enhanced readability and modern aesthetic appeal across diverse web environments.

![](../../Resources/Images/WebChat/Light%20Theme.png) ![](../../Resources/Images/WebChat/Dark%20Theme.png)

![](../../Resources/Images/WebChat/select%20theme.png)

- **Redesigned Chat Header**. A streamlined, cleaned header layout that reduces UI clutter while retaining essential navigation icons.
- **Relocated Voice Icon**. The voice input icon has been moved out of the top header and positioned below the user text input area, creating a cohesive typing and voice interaction flow that makes the experience more accessible and engaging.
- **Improved Input Area**. The gray text area and action bar (including attachments, emojis) and resizing capabilities have been cleaned up and optimized to ensure a smooth user experience.
- **Improved Hero Cards**. Updated hero card designs provide a cleaner layout and clearer action buttons, making structured options and recommendations easier to scan and interact with.

![](../../Resources/Images/WebChat/Light%20Theme%20-%20Hero%20Cards.png) ![](../../Resources/Images/WebChat/Dark%20Theme%20-%20Hero%20Cards.png)

- **Transparent Agentic Reasoning**. Visually clarifies intermediate execution steps, search status, and multi-step logic directly within the chat feed to reveal how an AI agent thinks and generates responses.

![](../../Resources/Images/WebChat/Light%20Theme%20-%20%20-%20Reasoning.png) ![](../../Resources/Images/WebChat/Dark%20Theme%20-%20Reasoning.png)

![](../../Resources/Images/WebChat/Light%20Theme%20-%20%20Informative%20Message.png) ![](../../Resources/Images/WebChat/Dark%20Theme%20-%20Informative%20Message.png)

{% hint style="info" %}
**Info:** Enabling agentic reasoning requires setting up specific parameters in the webchat customization.  For more information, see [Agentic Reasoning and Messaging](../../Channels/WebChat/WebChat_Common_Styling_and_Behavior_v4.md#Agentic).
{% endhint %}

- **Druid Voice – Speech-to-Speech (Technology Preview)**. Druid Voice Speech-to-Speech delivers a real-time, low-latency vocal interaction experience with response times under one second. Built for fluid, natural conversations, this technology preview introduces advanced capabilities designed for high-performance voice interactions:
  - **Flexible Speech Provider Selection**. Choose between **Druid** or **Google Gemini Live API** speech services depending on business needs.
  - **Low Latency**. Delivers instantaneous responses with sub-second latency for natural dialogue flow.
  - **Instant Barge-In Support**. Allows users to interrupt the AI agent mid-response, immediately halting output to adapt to new user input.
  - **Mid-Sentence Language Switching**. Seamlessly detects and transitions between supported languages during a single sentence without losing context.
  - **Multilingual Capabilities**. Fully supports [78 languages](https://ai.google.dev/gemini-api/docs/live-api/live-translate#supported-languages).

  Experience the speed yourself! [Speak with Nova](https://cmgbh04.na1.hubspotlinks.com/Ctc/W1+113/cMGbh04/VWWmxx3kkms3W57rNFQ6YrRjWW2L--MX5Tqv9jN2SX2503qn9qW95jsWP6lZ3nNW7X8bvk2wZpfnW3KlWj82BwbdxN8f8dhyWL-q0W8pClq36c2V7LW5pJtZF4gxZ6GW5lfLWm5sR657W27WBhC8vPdRxW1HdZ4g7x9gm3W79HNtG6M4GhJW2mV5jr79cylwW65_24z25JRVDW3Ctjdy7f_LZqW41Fln05VbmD2W35Rf_58B5dKhW8dHf1x7CR4mYW3JctPt1CnxzWW2FW1D-82y0GPW7vBmBr2MwsNqVLSLS544mRHrW68Y0Nd10rLLxW2RhWm_2zgQP_W2ccCV338Tyy9W3QFXyd84y8qhW8WTqZW5vFrRGW32rGVp7MyP5MW1Xs3g91S6MszW9cwRx62f973LW815THL3sgWjRW7J_syz5DZhXkW70jHL65BFlnnf1-yzJF04), our healthcare demo AI Agent, and feel sub-second voice interactions in action.
{% hint style="info" %}
**Info:** If you want to activate it on your tenant, reach out to your Druid sales representative.
{% endhint %}

- **Troubleshooting and Debugging with AI**. AI-assisted troubleshooting and debugging is now available within Conversation Transcript, Conversation Trace, and Flow Trace! The AI Authoring Agent automatically analyzes your system logs to provide immediate insights into runtime errors, dialog bottlenecks, and logic gaps. Beyond just identifying problems, the agent can suggest actions you should take to fix the errors, significantly reducing manual debugging effort and accelerating your authoring workflow.

![](../../Resources/Images/druid%209.30/debug%20with%20ai_1914x917.png)

For more information, see [Conversation Diagnostics Agent](../../2_AI%20Agents/Conversation%20Diagnostics%20Agent.md).

- **Becus 2 - Druid built-in LLM**. We are thrilled to announce Becus 2, the latest evolution of Druid native, built-in Large Language Model, reaching General Availability! Delivering frontier-class performance on par with GPT, Gemini, and Claude, Becus 2 introduces advanced reasoning and complex coding capabilities directly into the platform. This allows AI Agents to independently tackle multi-step logic and generate configurations autonomously, providing high-tier processing power while seamlessly maintaining enterprise data security and privacy.
{% hint style="info" %}
**NOTE:** Becus 2 is available in US environments. It will be available in EU environments starting with Druid 9.33.
{% endhint %}

<a id="Improvements"></a>

## Improvements

- **Voice AudioCodes Channel - Exception handling support**. AudioCodes-generated errors are now processed as native Druid exceptions. Authors can capture end-to-end voice exceptions by checking **[[ChatUser]].VoiceConversationTerminatedReason == "error"** within the [Voice Call Terminate Flow](../../4_Flows/Voice%20Call%20Terminate%20Flow.md) to trigger automated alerts or execute recovery steps (such as dynamic TTS provider switching).  For more information, see [Handle AudioCodes Exceptions](../../Channels/Voice%20Audio%20Codes/Voice%20Audio%20Codes%20Channel.md#Handle).
- **Druid Custom Queries- Support for** `ROUND` **function**. Custom queries now support the `ROUND()` function, allowing you to round numeric expressions and direct calculations to a specified number of decimal places. Additionally, you can now wrap aggregate functions (such as `AVG`, `SUM`, `MIN`, `MAX`, or `COUNT` inside `ROUND()` to easily format aggregated metrics directly within your query statements.  For more information, see [Functions](../../7_Integrations/Druid%20Data%20Service%20Connector/Filter%20using%20DRUID%20custom%20query.md#Function).
