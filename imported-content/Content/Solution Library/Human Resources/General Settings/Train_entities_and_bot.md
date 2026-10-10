---
title: Training the Entities and the AI Agent
---

# Training the Entities and the AI Agent

We created Druid for enterprises and unlike other AI Agent platforms; its entities are business objects with attributes and references, similar to the UiPath Data Service entities.

### Train the Entities

In the AI Agent configuration page, click the **Entities** tab. Train the entities highlighted in the figure below by clicking the **Edit Schedule** icon displayed in line with each entity.

![](<../../../../.gitbook/assets/train entity.png>)

In the pop-up that appears, click the **Train** button.

![](<../../../../.gitbook/assets/train entity button.png>)

After a few seconds, the following train status message should appear in the pop-up:

![](<../../../../.gitbook/assets/trained entity message.png>)

{% hint style="info" %}
**NOTE:** If the train status message does not appear, you might want to check you have properly configured the corresponding Druid app.
{% endhint %}

After you successfully train the entities, click **Save** button.

Now you can train the AI Agent.

### Train the AI Agent

Click the **Details** tab, and then click the NLP section header. The NLP area expands. Scroll down to the Train area and click the **Train** button.

![](<../../../../.gitbook/assets/train bot.png>)

{% hint style="info" %}
**NOTE:** It might take a few minutes for the NLP training to complete, so you might need to wait for Druid to finish training all AI Agent entities that have NLP enabled (NLP=true).
{% endhint %}
