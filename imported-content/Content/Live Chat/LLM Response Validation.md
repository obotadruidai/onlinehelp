---
title: "LLM Response Validation"
---

<a id="LLMResponseValidation"></a>


Ensure your LLM-powered AI Agents provide accurate and reliable information by setting up a flow that allows human agents to review and validate all LLM-generated responses before they reach users.

> **NOTE:**  This feature requires Multi-chat configuration.

<a id="Howitworks"></a>

## How it works

When an LLM-generated response requires human validation, the system places it in the Waiting queue. A human agent reviews the response, makes any necessary corrections, and approves it before it’s sent to the user. This process ensures users receive accurate information without noticing human involvement.

> **NOTE:** LLM responses needing validation are never part of a live chat session; they remain in the Waiting queue, even during agent review.

<a id="EnablehumanreviewforLLMresponses"></a>

## Enable human review for LLM responses

To enable human agents to review LLM responses, go to your Knowledge Base response flow (the one you selected in **KB** > **Settings** > **Knowledge Base response flow** field) and configure it as follows:

1. Add a branch after the response compilation step.
2. Set the branch to execute when **[[Intent]].KBQnAItems[0].Score < 0.95**. Adjust the score threshold or condition as needed.
3. On this new branch, add an Action step and in the Post Actions section, select the internal action **ConnectToHelpdeskAgent**.
4. Click on the internal action and configure it using the following parameters:

```
{ 
    "ForBotResponseValidation":true, 
    "InfoToValidate":{ 
        "UserQuestion":"<[[Entity]].UserQuestion / @UserQuestion>", 
        "BotResponse":"<[[Entity]].BotResponse / @BotResponse >", 
        "MaxWaitTimeForAgentResponse":30 //in seconds 
    }, 
"ResponseEntity":"[[Entity]].AgentResponse" 
} 
```

The table below describes the specific internal action parameters:

| Parameter | Description |
| --- | --- |
| ForBotResponseValidation | Set to true to flag the response for validation. |
| UserQuestion | The entity that stores the user question. |
| BotResponse | The entity that stores the LLM response. |
| MaxWaitTimeForAgentResponse | Sets the maximum time (in seconds) for a human agent to review the LLM response.  **NOTE:**  The job for **MaxWaitTimeForAgentResponse** runs every 15 seconds. |
| ResponseEntity | The entity that stores the agent-validated response. |

![](../Resources/Images/Reviewing%20and%20Validating%20LLM%20Responses/Reviewing%20and%20Validating%20LLM.png)

5. In the Action step, under Set variables, set **[[ChatUser]].HelpdeskSubject** to a value that helps agents distinguish between live chat users and LLM responses awaiting review (e.g., "Validate GPT").

![](../Resources/Images/Reviewing%20and%20Validating%20LLM%20Responses/validateGPT.png)

6. You can further author the flow with two branches to send either the LLM-generated response or a custom message indicating that the system could not provide an immediate answer (e.g., when condition **[[ChatUser]].ConversationStatus == "QueueTimeOut"** is met).

By following these steps, you can ensure that all LLM-generated responses are thoroughly reviewed by human agents, providing users with a seamless and trustworthy conversational experience.

<a id="Handletimeouts"></a>

## Handle timeouts

If an AI Agent response is waiting for agent review and exceeds the **LiveChatQueueWaitingTimeoutMins**, the **live-chat-waiting-message-in-the-queue** flow will trigger.

To ensure the best user experience, modify this flow by adding a branch that executes when **[[HelpdeskClient]].BotValidationStatus = “timedout”**. This branch should send a message to the user, such as “It’s taking a little longer to answer this question. Please wait a bit more".

<a id="AgentsreviewingLLMresponses"></a>

## Agents reviewing LLM responses

When an LLM response is awaiting review, it appears in the Waiting queue under the Low Confidence section.

![](../Resources/Images/Reviewing%20and%20Validating%20LLM%20Responses/Reviewing%20and%20Validating%20LLM_1.png)

When an agent clicks on an LLM-generated response, the user question and the LLM response are displayed on the right.

![](../Resources/Images/Reviewing%20and%20Validating%20LLM%20Responses/Reviewing%20and%20Validating%20LLM_2.png)

The agent can then:

- Approve the LLM response.
- Make light edits to the LLM response.

![](../Resources/Images/Reviewing%20and%20Validating%20LLM%20Responses/Reviewing%20and%20Validating%20LLM_3.png)

- Initiate a live chat session with the user by clicking **Pickup** if the question is complex and requires more time.

Approving the response sends it to the user and removes the conversation from the Waiting queue.

If human agents do not approve an LLM-generated response or if the **MaxWaitTimeForAgentResponse** is reached, the LLM-generated response will be highlighted in gray in the Waiting queue when hovered over. Agents can remove it from the queue by clicking the **close** icon. This feature helps agents easily identify LLM-generated responses they may have missed.

![](../Resources/Images/Reviewing%20and%20Validating%20LLM%20Responses/missed%20response.png)

<a id="Timestampsavailablewithintheconversationcontext"></a>

## Timestamps available within the conversation context

When reviewing and validating LLM responses, the [[HelpdeskClient]] system entity includes fields that capture timestamps for specific actions taken by agents during the review process.

The following fields provide detailed tracking of agent activities, offering a more comprehensive view of the conversation context:

| [[HelpdeskClient]] field | Type | Description |
| --- | --- | --- |
| BotResponseValidationEdit | DateTime | Captures when the agent clicked the **Edit** icon to modify an LLM response. Useful for measuring how long the agent spent editing. The value is recorded in real time when the **Edit** icon is clicked. |
| BotResponseValidationFirstClick | DateTime | Captures when the agent first clicked on the LLM response pending review. |
| BotResponseValidationPickUp | DateTime | Captures when the agent initiated a live session with the user by clicking **Pickup** in the LLM response. |
| BotResponseValidationSave | DateTime | Captures when the agent approves an LLM response or saves and closes an edited response. The value is stored after the agent completes the task. |

> **Info:** These timestamps are also available within the conversation context when the **MaxWaitTimeForAgentResponse** timeout is reached.
