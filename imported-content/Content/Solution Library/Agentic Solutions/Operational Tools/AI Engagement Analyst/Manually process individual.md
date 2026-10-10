---
title: "Manually Process Individual Conversations"
---

<a id="ManuallyProcessIndividualConversations"></a>


While the AI Analyst typically processes data automatically, you can manually trigger the analysis for a specific record if it has not yet been processed.

To manually process a conversation:

1. On the workspace menu, click **ConversationInfo** and select the **All Conversations** view.
2. Click on the desired conversation record to open the **ConversationInfo** form.
3. Run the **Get transcript** automation. This action fetches the raw chat data from the Conversation History database and populates the **Details** tab.

![](../../../../Resources/Images/Conversation%20Toolkit%202/Manually%20process%20individual.png)

4. Click the **Reload** button on the form to display the conversation transcript text.

![](../../../../Resources/Images/Conversation%20Toolkit%202/Manually%20process%20individual_1.png)

5. Run the **Get Conversation Metrics** automation. This sends the transcript to the AI Analyst for evaluation.

![](../../../../Resources/Images/Conversation%20Toolkit%202/Manually%20process%20individual_2.png)

6. Click the **Reload** button again. The AI-generated metrics will now be visible.

![](../../../../Resources/Images/Conversation%20Toolkit%202/analysis%20complete.png)
