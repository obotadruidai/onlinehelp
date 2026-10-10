---
layout:
  title:
    visible: false
---

<a id="TrainingtheEntitiesandtheAIAgent"></a>

# Training the Entities and the AI Agent

We created Druid for enterprises and unlike other AI Agent platforms; its entities are business objects with attributes and references, similar to the UiPath Data Service entities.

<a id="TraintheEntities"></a>

## Train the Entities

In the AI Agent configuration page, click the **Entities** tab. Train the entities “Product” and “UiPathUser” by clicking the **Edit Schedule** icon displayed in line with each entity.

![](../../../Resources/Images/Retail/train%20entities.png)

In the pop-up that appears, click the **Train** button.

After a few seconds, the Status **Trained** should appear in the pop-up:

> **NOTE:**  If the train status message does not appear, you might want to check you have properly configured the corresponding Druid app.

After you successfully train the entities, click **Save** button.

Now you can train the AI Agent.

<a id="TraintheAIAgent"></a>

## Train the AI Agent

Click the **Details** tab, and then click the NLP section header. The NLP area expands. Scroll down to the Train area and click the **Train** button.

![](../../../Resources/Images/solution%20templates/Cristina/train%20bot.png)

> **NOTE:**  It might take a few minutes for the NLP training to complete, so you might need to wait for Druid to finish training all AI Agent entities that have NLP enabled (NLP=true).
