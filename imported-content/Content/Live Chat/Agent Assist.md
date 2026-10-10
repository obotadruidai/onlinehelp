---
title: "Agent Assist"
---

<a id="AgentAssist"></a>


Agent Assist helps helpdesk agents respond faster and more accurately by analyzing both written and real-time voice interactions. It can use large language models (LLMs) to understand client messages and suggest the most relevant replies from your Knowledge Base.

Agents can also ask Agent Assist specific questions to get quick, AI-powered answers.

![](../Resources/Images/Agent%20Assist/agent%20assist.png)

{% hint style="info" %}
**NOTE:** This feature is available as a technology preview in Multichat starting with DRUID 8.16.
{% endhint %}

<a id="HowItWorks"></a>

### How It Works

When a client-AI Agent conversation is transferred to a live agent in DRUID Live Chat, Agent Assist activates automatically—if the Agent Assist special flow is configured. It processes each message in real time as follows:

- Captures the full conversation transcript by updating [[ConversationInfo]].AssistConversationItem[i], storing:

- The message in [[ConversationInfo]].AssistConversationItem.Message
- The message originator in [[ConversationInfo]].AssistConversationItem.Originator (**user** for client messages, **agent** for helpdesk agent messages).

- Searches the Knowledge Base using each client message to find relevant content.
- Triggers the Agent Assist special flow to generate a response suggestion based on the client’s message.
- Sends the suggested reply to the helpdesk agent.
- Prevents overlapping suggestions by ensuring only the latest client message triggers a response—after the previous Agent Assist flow has completed.

<a id="SetupAgentAssistforresponserecommendations"></a>

### Set up Agent Assist for response recommendations

1. Open Solution Library, search for solution **Agent Assist + Live Chat**, and import it.
2. Go to AI Agent Details > General details > Dialogue Management.
3. Select **Use Knowledge Base**.
4. From the **Knowledge Base response flow** field, select **Agent assist flow**.

![](../Resources/Images/Agent%20Assist/Recommending%20Responses%20to_1.png)

5. Go to **Apps** and configure the connection strings for the **GPT-azure.com** app.

![](../Resources/Images/Agent%20Assist/Recommending%20Responses%20to_2.png)

The solution comes by default with Druid Data Service integration, saving the suggested responses to the Agent Assist workspace that comes with the solution.

![](../Resources/Images/Agent%20Assist/Recommending%20Responses%20to_3.png)

After setup, Agent Assist will automatically suggest responses, helping agents provide faster and more accurate support.

{% hint style="info" %}
**Info:** Agent Assist supports machine translation. Enable and configure the desired machine translation services on the AI Agent. For more information, see [Real-time Machine Translation in Live Chat](Real-time%20Machine%20Translation%20in%20Live%20Chat.md).
{% endhint %}

<a id="AgentAssistusageconsiderationsforMultichat"></a>

## Agent Assist usage considerations for Multichat

When using Agent Assist within the Multichat interface, its behavior differs slightly based on whether the channel has voice enabled or not.

For channels with voice enabled:

- The Agent Assist will appear automatically on the left side of the Multichat screen as soon as the helpdesk agent connects in a live chat session with a client.
- The helpdesk agent cannot manually type messages directly into the chat interface when Agent Assist is active in this configuration.

![](../Resources/Images/druid%208.17/agent%20assist%20voice%20_1.png)

For channels without voice enabled:

- The Backchannel events will appear by default on the left side of the Multichat screen once the helpdesk agent connects in a live chat session with a client. To open the Agent Assist, helpdesk agents need to click on the dedicated AI Agent icon.

![](../Resources/Images/druid%208.17/click%20AA.png)

- You can easily copy the last suggested response from Agent Assist by clicking the **Copy** icon located below the response.

![](../Resources/Images/druid%208.17/copy%20response.png)

To paste the copied response into the chat, the helpdesk agent just needs to click in the 'Type your message' field, press **CTRL+V**, and either click 'Send' or press **ENTER**.

![](../Resources/Images/druid%208.17/paste%20response.png)

<a id="Triggerpostcallactionsintheassistantconversation"></a>

## Trigger post-call actions in the assistant conversation

You can configure the Voice Call Terminate Flow to also run in the assistant conversation (the internal chat between the helpdesk agent and the assistant AI Agent), enabling you to define tailored post-call automation for agent-side actions after a voice call ends.

For more information, see [Voice Call Terminate Flow](../4_Flows/Voice%20Call%20Terminate%20Flow.md).

<a id="Accessthefullconversationtranscript"></a>

## Access the full conversation transcript

{% hint style="info" %}
**NOTE:** This feature is available in DRUID 9.2 and higher.
{% endhint %}

When Agent Assist is enabled, you can generate a complete transcript that includes both the client-side and assistant conversations. This provides full visibility into the entire interaction—useful for auditing, support analysis, or CRM integration.

For configuration details, see the [Internal Actions](../4_Flows/Internal%20Actions.md), GetConversationTranscript.
