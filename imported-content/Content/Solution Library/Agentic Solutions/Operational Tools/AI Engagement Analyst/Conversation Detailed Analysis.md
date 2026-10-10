---
title: "Conversation Detailed Analysis"
---

<a id="ConversationDetailedAnalysis"></a>


You can review individually each conversation.

Selecting a record from any drill-down view opens the **ConversationInfo** form, which provides the comprehensive results of the AI Analyst’s evaluation. This form serves as a deep-dive diagnostic tool, translating raw transcript data into structured insights that allow you to troubleshoot specific interactions, validate AI logic, and identify precise points for improvement in your dialogue flows.

The analysis results are organized into specialized tabs—**Insights**, **Live Chat**, **Details**, **Transcript**, and **Data & Events**—ensuring that all qualitative assessments, human agent performance metrics, and technical system data are easily accessible for audit and review.

<a id="Insights"></a>

## Insights

The **Insights** tab is the main evaluation hub. It explains **why** an interaction performed the way it did by showing the AI’s decision-making process.

This tab contains the core AI Analyst results, including narrative summaries, qualitative metrics, and the reasoning behind each assigned score.

![](../../../../Resources/Images/Conversation%20Toolkit%202/Conversation%20Detailed%20Analysis.png)

| Section | Field | Description |
| --- | --- | --- |
| SUMMARY | Sentiment / Clarity / Friction | High-level indicators of the interaction quality. |
|  | Resolution | The final success status (Pass, Partial Pass, Failed). |
|  | Outcome (L1 / L2) | The specific business goal identified, categorized by hierarchy level. |
|  | Outcome Explain | The AI-generated justification for the selected outcome category. |
| TRANSCRIPT SUMMARY | AI-generated summary | A concise, text-based recap of the entire conversation. |
|  | Language | The primary language detected in the transcript. |
|  | Waiting in Queue | Time spent by the user awaiting a human agent (seconds). |
|  | Agent Connected | Boolean indicating if the user successfully reached a human agent. |
|  | AgentDidntRespond | Flag indicating if an agent failed to reply to a user prompt. |
|  | Resolution Explain | A detailed technical justification for the final Resolution status. |
| SENTIMENT | Sentiment value and Explain | AI-generated reasoning for the detected emotional tone. |
| FRICTION | Friction | The friction value (e.g., High Friction). |
|  | Friction Intent | The specific user goal being pursued when the struggle occurred. |
|  | Friction Step | The exact flow step where friction was detected. |
|  | Friction Explain | The AI Analyst's detailed reason for the assigned friction level. |
| CLARITY | Clarity value and Explain | AI-generated reasoning for the assigned clarity score. |
| HUMAN REVIEW | Human Review |  |
|  | Human Explain | A field for users to provide comments after metrics review. |
| INTENTS | Name / IsPrimary | Lists the intents detected and identifies which was the main goal. |
|  | Completion | Status indicating if the specific intent was fully executed. |
|  | Completion Explain | Reasoning for why an intent was or was not completed. |
| DATA CAPTURED | Name / Value | Lists any specific variables or data entities (e.g., account numbers) collected during the chat. |

<a id="LiveChat"></a>

## Live Chat

This section provides performance data specifically for interactions involving human agents, when drilling down on the dashboards from the Live Conversation Toolkit workspace.

![](../../../../Resources/Images/Conversation%20Toolkit%202/Conversation%20Detailed%20Analysis_2.png)

| Category | Field | Description |
| --- | --- | --- |
| LIVE CHAT INTERACTION | Waiting in Queue | The duration the user spent in the queue before an agent joined. |
|  | Queue Name / Contact Center | The specific department and physical/Contact center handling the chat. |
|  | Agent Name | The name of the human staff member connected with the user. |
|  | Queue Start Time | Local timestamps for when the user entered the queue. |
|  | Agent Start Time | Local timestamps for when the agent first replied. |
|  | Duration with Agent | Total active time (seconds) spent in conversation with the human agent. |
|  | LivechatEndTime | The timestamp when the human-led portion of the session concluded. |
| CONTACT CENTER SCHEDULE | IsOutsideWorkingHours | Boolean flag indicates if the chat occurred outside working hours. |
|  | OutsideWorkingHoursExplain | AI logic explaining the reason for considering the call outside working hours. |

<a id="Details"></a>

## Details

While the Insights tab focuses on AI-generated qualitative analysis, the **Details** tab offers the underlying metadata and raw data from the ConversationInfo, verifying user authentication, and performing comprehensive audits of the conversation transcript.

![](../../../../Resources/Images/Conversation%20Toolkit%202/Conversation%20Detailed%20Analysis_3.png)

| Category | Field | Description |
| --- | --- | --- |
| GENERAL | Name | The user’s name for authenticated users, or **anonymous** for unauthenticated users. |
|  | UserPhone | The phone number provided by or associated with the user during the interaction. This field is redacted. |
|  | ConversationId | The unique system identifier for the entire chat session, used for cross-referencing with external logs. |
|  | ActivityId | A specific ID used to track individual interactions or events within the larger conversation. |
|  | StartedOn | The timestamp indicating the exact moment the user initiated the chat. |
|  | EndedOn | The timestamp indicating when the chat session was terminated. |
|  | Turns | The total message count exchanged between the user, the AI Agent, and any human agent involved. |
|  | Duration Total | The total length of the chat session from start to end, expressed in seconds. |
|  | IsAuthenticated | A Boolean flag indicating whether the user was logged into a verified account during the session. |
| REVIEW | Resolution | The final resolution status determined by the AI Analyst. |
| TRANSCRIPT | Language | The primary language detected by the system during interaction. |
|  | IsProcessed | A status flag confirming whether the AI Analyst has completed the processing and extraction of metrics for this session. |
|  | TranscriptTxt | The complete, unformatted text of the conversation, allowing for a line-by-line audit of the interaction. |

![](../../../../Resources/Images/Conversation%20Toolkit%202/Conversation%20Detailed%20Analysis_4.png)

<a id="DataEvents"></a>

## Data & Events

The **Data & Events** tab captures the technical footprint of the interaction. It provides context regarding the user's environment, their navigation on your website, and a chronological log of system events during user conversation with the AI Agent.

![](../../../../Resources/Images/Conversation%20Toolkit%202/Conversation%20Detailed%20Analysis_5.png)
