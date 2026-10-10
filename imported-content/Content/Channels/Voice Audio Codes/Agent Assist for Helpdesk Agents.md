---
title: "Agent Assist for Helpdesk Agents"
---

<a id="AgentAssistforHelpdeskAgents"></a>


Configure advanced agent assist capabilities and outbound campaign automation for your voice channel through AudioCodes Live Hub. This topic explains how to deploy Agent Assist to provide real-time response recommendations, map backend settings to preserve live-agent handoff transcripts in DRUID conversation history, and optimize outbound dialer flows with automated voicemail and machine detection.

<a id="RecommendResponsestoHelpdeskAgentswithAgentAssist"></a>

## Recommend Responses to Helpdesk Agents with Agent Assist

Agent Assist analyzes real-time voice interactions and suggests AI-powered responses to help AudioCodes helpdesk agents provide faster and more accurate support. It can use large language models (LLMs) to interpret client messages and recommend the most relevant replies from the Knowledge Base.

![](../../Resources/Images/Agent%20Assist/Recommending%20Responses%20to.png)

> **NOTE:** This feature requires Agent Assist setup to store AudioCodes helpdesk conversations in Conversation History.

When a client-AI Agent conversation is transferred to a helpdesk agent, Agent Assist activates automatically—if the Agent Assist special flow is configured. It processes each message in real time as follows:

- Captures the full conversation transcript by updating [[ConversationInfo]].AssistConversationItem[i], storing:

- The message in [[ConversationInfo]].AssistConversationItem.Message
- The message originator in [[ConversationInfo]].AssistConversationItem.Originator (**user** for client messages, **agent** for helpdesk agent messages).

- Searches the Knowledge Base using each client message to find relevant content.
- Triggers the Agent Assist special flow to generate a response suggestion based on the client’s message.
- Sends the suggested reply to the helpdesk agent.
- Prevents overlapping suggestions by ensuring only the latest client message triggers a response—after the previous Agent Assist flow has completed

<a id="SetupAgentAssistforresponserecommendations"></a>

### Set up Agent Assist for response recommendations

1. Open Solution Library, search for solution **Agent Assist + Live Chat**, and import it.
2. Go to AI Agent Details > General details > Dialogue Management.
3. Select **Use Knowledge Base**.
4. From the **Knowledge Base response flow** field, select **Agent assist flow**.

![](../../Resources/Images/Agent%20Assist/Recommending%20Responses%20to_1.png)

5. Go to **Apps** and configure the connection strings for the **GPT-azure.com** app.

![](../../Resources/Images/Agent%20Assist/Recommending%20Responses%20to_2.png)

6. Go to **Flows**, search for 'Agent assist flow', and click on the **Add Suggestion** step. The solution comes by default with Druid Data Service integration, saving the suggested responses to the Agent Assist workspace that comes with the solution.

![](../../Resources/Images/Agent%20Assist/Recommending%20Responses%20to_3.png)

You can remove this integration and configure an integration with the third-party tool your helpdesk agents use to handle client calls.

After setup, Agent Assist will automatically suggest responses, helping agents provide faster and more accurate support.

> **Info:** Agent Assist supports machine translation. Enable and configure the desired machine translation services on the AI Agent. For more information, see [Real-time Machine Translation in Live Chat](../../Live%20Chat/Real-time%20Machine%20Translation%20in%20Live%20Chat.md).

<a id="StoreAudioCodesHelpdeskConversationsinConversationHistory"></a>

## Store AudioCodes Helpdesk Conversations in Conversation History

To log conversations between AudioCodes helpdesk agents and users in the Conversation History, you must set up Agent Assist. Doing so provides valuable insights into user-agent interactions, helping you refine AI Agent responses, improve escalation flows, and enhance overall AI Agent performance.

To set up Agent Assist follow these steps:

1. In the Druid Portal go to your AI Agent settings. Click the **Channels** tab, then click **Voice, AudioCodes – VoiceAi Connect**. The channel info section expands.
2. Select **Allow assist AI Agent** and copy the **Assist AI Agent Druid url** and the **Token** as you will need them in the subsequent steps.
3. Log into [AudioCodes LiveHub](https://livehub.audiocodes.io/) and select **AI Agents** from the left menu.
4. On the AI Agents page, click the **Add new assist AI Agent** button.

![](../../Resources/Images/Voice%20Audio%20Codes%20Channel/add%20agent%20assist.png)

The Connect your AI Agent wizard appears.

5. Select **Druid** as AI Agent framework, then click **Next**.

![](../../Resources/Images/Voice%20Audio%20Codes%20Channel/select%20bot%20framework.png)

6. Enter the AI Agent details. In the **AI Agent URL** field, paste the **Assist AI Agent Druid url** you copied from DRUID. In the **Token** field, paste the token you copied from DRUID.

![](../../Resources/Images/Voice%20Audio%20Codes%20Channel/bot%20assist%20details.png)

7. Click the **Validate bot configuration** button. If the validation fails, check that you entered the correct AI Agent URL and token. If the validation passes, click **Next**.
8. Set the assist AI Agent settings and click **Create**.

![](../../Resources/Images/Voice%20Audio%20Codes%20Channel/bot%20assist%20settings.png)

9. Click **Routing** in the left menu. On the **Routing Rules** tab, search for the main bot you created for the AI Agent integration and click the **Edit** button. Do not search for the assist AI Agent you created.

![](../../Resources/Images/Voice%20Audio%20Codes%20Channel/routing%20rule.png)

The **Edit routing rule** page appears.

10. Tap on **Assist bot** and select the assist AI Agent you created previously from the drop-down, then click **Update**.

![](../../Resources/Images/Voice%20Audio%20Codes%20Channel/select%20assist%20bot%20in%20route.png)

> **NOTE:** Following the Live Hub 2.19 upgrade, Agent Assist behavior after a call transfer is no longer carried over automatically from the initial call routing rule. The default setting is now disabled. If you want Agent Assist to continue functioning after a call transfer, you must explicitly configure the same Assist Bot on the relevant Transfer routing rule within the AudioCodes Live Hub.

Agent Assist is now successfully set up, enabling the logging of AudioCodes agent-user interactions in the Conversation History.

<a id="SetupAgentAssistforOutboundCalls"></a>

## Set up Agent Assist for Outbound Calls

Agent Assist supports outbound calls initiated from AudioCodes, where the AI Agent calls the client, the client answers, and the conversation is then transferred to a helpdesk agent.

For outbound calls, you must enable outbound calling on the AI Agent connections and configure the call routing settings differently than for inbound calls.

In outbound call scenarios, the call direction is reversed compared to inbound calls:

1. The AI Agent initiates the call to the client (outbound).
2. The client answers.
3. The conversation is transferred to an agent.

This reversal affects how Agent Assist processes the conversation transcript. The system must correctly identify which messages originate from the client and which come from the agent to provide accurate response suggestions.

> **NOTE:** Agent Assist support for outbound calls is available only in DRUID version 9.9 and later.

<a id="Prerequisites"></a>

### Prerequisites

Before you configure Agent Assist for outbound calls, make sure the following requirements are met:

- The phone numbers used for outbound calling must be provided by AudioCodes.
- You must have an AudioCodes Live Hub Essential account.
- You must have approval from AudioCodes Support.

<a id="ConfigureAgentAssistforOutboundCalls"></a>

### Configure Agent Assist for Outbound Calls

To ensure Agent Assist works correctly with outbound calls:

1. Enable and configure outbound calling on your AI Agent connections.
2. Configure the outbound call routing rule in AudioCodes Live Hub.

For detailed steps on setting up outbound call routing, see the [AudioCodes Live Hub Outbound Call Documentation](<https://techdocs.audiocodes.com/livehub/#LiveHub/byoc_Outbound Call.htm%23Enable20outbound20calls>).

<a id="HandleOutboundCallVoicemailDetectionAudioCodesLiveHub"></a>

## <a id="Handling"></a>Handle Outbound Call Voicemail Detection (AudioCodes Live Hub)

> **NOTE:** This feature is available in Druid 9.23 and higher.

This feature allows outbound Live Hub call campaigns to detect when a client voicemail or answering machine answers the call, enabling the AI Agent to deliver a properly timed message after the voicemail greeting ends.

<a id="Step1EnableMachineDetectionintheAPICall"></a>

### Step 1. Enable Machine Detection in the API Call

To trigger voicemail detection on an outbound call, you must include the following property in the payload sent to the dialout Live Hub endpoint: **"machineDetection": "detect"**.

**Outbound API Call Example**

```
POST /api/v1/actions/dialout HTTP/1.1
Host: server.example.com
Content-Type: application/json;charset=UTF-8
Authorization: BEARER 223d0d870a364a4a

{
  "bot": "Bot1",
  "target": "tel:+123456789",
  "caller": "1-800-111-111",
  "notifyUrl": "https://my-app.example.com/call/454/notify",
  "machineDetection": "detect", 
  "voicemailEndTimeoutSec": 20, 
  "metadata": {
    "participantName": "Alice"
  }
}
```

<a id="Step2UpdatetheWelcomeFlow"></a>

### Step 2. Update the Welcome Flow

When a voicemail machine is detected, the system automatically sets a query parameter. Authors must update the Welcome flow to handle this scenario:

- **Condition to check**: [[QueryParams]].VoiceMailAnswer == true
- **Behavior**: Route the conversation to a dedicated path designed for leaving a voicemail message. This path executes after the voicemail greeting ends and the AI agent begins speaking.

> **NOTE:**  Due to the response speed of certain voicemail providers, the initial welcome flow may trigger after the voicemail message starts. This behavior is expected and cannot be prevented.
