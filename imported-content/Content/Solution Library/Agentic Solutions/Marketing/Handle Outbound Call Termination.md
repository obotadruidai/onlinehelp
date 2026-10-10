---
title: Handle Outbound Call Termination
---

# Handle Outbound Call Termination

The solution automatically records the outcome of each call, whether the conversation ends normally or the contacted person hangs up before the AI Agent completes the interaction.

When a call ends, the solution updates the corresponding campaign activity with the following information:

* Status – The campaign activity status that reflects the call outcome (disposition).
* End Date – The date and time when the call ended.
* Summary – A summary of the conversation between the AI Agent and the contacted person.

### Normal Call Termination

When the AI Agent completes the conversation with the contacted person, it ends the call and automatically updates the corresponding campaign activity with the appropriate status, end date, and conversation summary.

### Early Call Termination

If the contacted person hangs up before the AI Agent completes the conversation, the early-temination-flow is triggered immediately.

This flow ensures that the campaign activity is updated even when the conversation ends unexpectedly. The activity captures the call status, end date, and a summary of the conversation up to the point of termination.

### View Call Outcomes

To review the information recorded for a completed call:

1. Open the Campaigns workspace and navigate to the corresponding RingCentral CX campaign.
2. Open the campaign activity you want to review.
3. On the Details tab, review the activity status.
4. On the Status tab, review the call details, including the end date and conversation summary.

This information helps campaign managers track call outcomes, review interactions, and monitor outbound campaign activity.

![](<../../../../.gitbook/assets/Handle Outbound Call Termination.png>)

![](<../../../../.gitbook/assets/Handle Outbound Call Termination_1_1887x859.png>)

If the contacted person hangs up first, the **early-temination-flow** flow is triggered immediately. This flow still captures the same details mentioned above, including the conversation summary and the status.
