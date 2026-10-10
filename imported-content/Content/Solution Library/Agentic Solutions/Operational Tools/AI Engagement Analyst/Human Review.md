---
title: "Human Review"
---

<a id="HumanReview"></a>


While the AI Analyst automatically extracts and evaluates metrics from your AI Agent and human-assisted interactions, the solution is built on a robust **four-eye principle**. This framework is a critical security and quality control measure, especially for AI-driven interactions, where human oversight ensures that automated decisions remain accurate, ethical, and aligned with organizational standards.

By enabling human supervisors to audit AI-generated insights, the platform provides a vital layer of governance. This allows the validation of automated data, the correction of edge-case anomalies, and the manual adjustment of scores to maintain the highest levels of data integrity in your analytics.

To begin the review process, select **Review Conversations** from the workspace menu. The page is organized into six functional tabs designed to prioritize your attention:

- **High Severity:** Aggregates interactions that have failed across all three pillars (High Friction, Negative Sentiment, and Negative Clarity). This is the primary tab for urgent troubleshooting.
- **High Friction:** Focuses exclusively on conversations where users encountered significant obstacles.
- **Negative Sentiment:** Isolates interactions where users expressed frustration or dissatisfaction.
- **Negative Clarity:** Highlights sessions where the dialogue was confusing, or the responses were ambiguous.
- **All Processed:** A complete repository of every conversation that has undergone AI analysis.
- **Not Processed:** Lists records awaiting analysis, including new conversations from history not yet sent to the AI Analyst and those currently assigned for analysis but not yet processed.

![](../../../../Resources/Images/Conversation%20Toolkit%202/Conversation%20Detailed%20Analysis_6.png)

The table below provides immediate context in the list view for the first five tabs, allowing you to filter and sort records before diving into the full record analysis.

| Column | Description |
| --- | --- |
| Started On | The exact date and time when the AI Analyst began processing the transcript. |
| Outcome | The business goal or category identified for the interaction. |
| Outcome L1 / L2 | The hierarchical classification of the outcome, from broad category (L1) to specific result (L2). |
| Resolution | The final success status of the interaction (Pass, Partial Pass, or Failed). |
| Clarity | The clarity level based on how easy the dialogue was for the user to follow. |
| Friction | The level of difficulty detected during the session. |
| Sentiment | The detected emotional tone of the user. |
| IsOutsideWorkingHours | A flag indicating if the chat occurred during contact center closed hours. |
| Waiting in Queue | The time (in seconds) the user waited for a human agent. |
| Agent Connected | A flag indicating if a human agent connected to the live chat session. |
| Agent Name | The name of the human agent who handled the live chat. |
| Queue Name | The specific support queue the user was routed to. |

<a id="Reviewingprocessedconversations"></a>

## Reviewing processed conversations

Failed conversations are escalated for Human review.

![](../../../../Resources/Images/Conversation%20Toolkit%202/Conversation%20Detailed%20Analysis_7.png)

The default **Review Conversations** dashboard proposes the following review workflow, from left to right:

1. High Severity. Are conversations with Sentiment = Negative and Friction = High.
2. High Friction. Friction = High.
3. Negative Sentiment.

As you progress from left to right you focus on special conversations that need your attention.

To review a processed conversation, click any record in the first five tabs. This opens the conversation detailed analysis (ConversationInfo form) where you can:

1. **Validate AI Logic:** Review the scores alongside the AI Analyst explanations. Use these justifications to determine if the AI Agent requires optimization (e.g., updating intents or dialogue flows).
2. **Manual Override:** If you identify an inaccurate assessment, you can change the metric score.
3. **Document Changes:** When overriding a score, you must provide justification in the **Human Review** section using the **Human Explain** field to maintain an audit trail.

![](../../../../Resources/Images/Conversation%20Toolkit%202/Conversation%20Detailed%20Analysis_8.png)

As you mark the conversation with **Human Review = Complete**, the record moves from the Pending review tables. You continue with the review process until you complete all pending reviews.

For detailed information on the information available on the form, see [Conversation Detailed Analysis](Conversation%20Detailed%20Analysis.md).
