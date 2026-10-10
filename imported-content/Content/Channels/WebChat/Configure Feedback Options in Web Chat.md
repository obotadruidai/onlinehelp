---
title: "Feedback Reactions in Web Chat"
---

<a id="FeedbackReactionsinWebChat"></a>


Enable feedback options in web chat to capture user reactions to AI Agent responses. Users can provide positive or negative feedback using thumbs-up or thumbs-down emojis, helping you enhance AI Agent interactions and improve the user experience.

![](../../Resources/Images/WebChat/feedback%20reactions.png)

<a id="Howfeedbackworks"></a>

## How feedback works

When a user reacts to a AI Agent message, the system automatically triggers feedback collection in dedicated [[ChatActivityData]] system entity fields. A dedicated feedback flow that captures the feedback received is automatically triggered.

In Druid versions prior to 8.16, when a user reacts to a message sent by the AI Agent, the system triggers a feedback flow that captures and stores the reaction. The AI Agent saves this feedback in [[ChatActivityData]] for further analysis.

<a id="Benefitsofenablingfeedbackoptions"></a>

## Benefits of enabling feedback options

- Enhances user satisfaction – Users feel heard when they can react to responses.
- Provides actionable insights – Stored feedback allows you to analyze and optimize AI Agent performance.

<a id="Howtoenableconfigureandusefeedbackreceived"></a>

## How to enable, configure and use feedback received

<a id="Step1EnableFeedbackReactionsinWebChat"></a>

### Step 1. Enable Feedback Reactions in Web Chat

Follow these steps to enable feedback reactions:

1. Go to the AI Agent details page.
2. Click **Theme** and navigate to the Webchat snippet section.
3. Click **Customize webchat** and search for **Show Actions for AI Agent Messages (botActivitiesActionsEnabled)**.
4. Select the option to enable it.

![](../../Resources/Images/druid%208.10/show%20actions%20feedback.png)

5. Click on **Custom Handlers** and in the **Webchat Event Handlers (webChatEventHandler)** field, enter the following code:

```
(action, currentDruidState) => {
      if (action.type === 'DIRECT_LINE/INCOMING_ACTIVITY' && DruidWebchat_v2.isNewActivity(currentDruidState, action.payload.activity)) {
        if(action.payload.activity.type == "event" && action.payload.activity.name == "_positive_feedback_") {
                    DruidWebchat_v2.sendMessage("&#x1F44D");
        };
        if(action.payload.activity.type == "event" && action.payload.activity.name == "_negative_feedback_") {
                    DruidWebchat_v2.sendMessage("&#x1F44E");
        }        
      }
    }
```

![](../../Resources/Images/druid%208.10/custom%20handlers.png)

6. Click the **Save** button at the top right-corner of the pop-up.
7. Save the AI Agent.

<a id="Step2Configurefeedbackcollection"></a>

### Step 2. Configure feedback collection

To capture feedback received in the web chat, go to the **Solutions Library**, search for solution "Feedback received" and import it following the instructions provided in section [Installing Solution Templates](../../Solution%20Library/Installing%20Solution%20Templates.md).

Wait until the import status shows as “Success”.

The solution contains the flow that captures the received feedback.

![](../../Resources/Images/druid%208.10/feedback%20flow.png)

When a user reacts to a message sent by the AI Agent, the system automatically stores the feedback in the [[ChatActivityData]] entity using three dedicated fields:

- FeedbackBotMessage (string) – Stores the text of the message the user reacted to.
- FeedbackReaction (string) – Records the type of reaction (like or dislike).
- FeedbackRating (integer) – Stores the numeric rating value (**1** for thumbs-down and **5** for thumbs-up).

![](../../Resources/Images/druid%208.10/feedback%20in%20chat.png)

<a id="Step3Analyzecollectedfeedback"></a>

### Step 3. Analyze collected feedback

The "Feedback received" solution includes a workspace that allows you to view and analyze statistically the captured feedback.

To view feedback received, from the **Workspaces** menu, select **Intents**. On the workspace menu, click **Feedback**.

![](../../Resources/Images/druid%208.10/feedback%20workspace.png)

<a id="ConfigureandstorefeedbackreceivedinversionspriortoDruid816"></a>

## Configure and store feedback received in versions prior to Druid 8.16

In earlier versions, feedback collection requires additional setup:

1. Go to the solution entities, search for the [[ChatActivityData]] entity and add the following two fields:

- **FeedbackActivityId** – Stores the conversation Id and message hash of the rated message.
- **FeedbackBotMessage** – Stores the message the user reacted to.

2. Create a flow with the utterance **\_positive\_feedback\_**. To store the feedback in the Conversation History, add a message step (without step message) and include the internal action **SaveActivityData** in either the Pre Action or Post Action section.

![](../../Resources/Images/druid%208.10/flow%20uttenarnce.png)

When a user reacts with a thumbs-up emoji, the value stored in **[[ChatActivityData]].FeedbackFlows** is **5**.

3. Create a flow with the utterance **\_negative\_feedback\_**. To store the feedback in the Conversation History, add a message step (without step message) and include the internal action **SaveActivityData** in either the Pre Action or Post Action section.

![](../../Resources/Images/druid%208.10/negatiev%20feedback.png)

When a user reacts with a thumbs-down emoji, the value stored in **[[ChatActivityData]].FeedbackFlows** is **1**.

4. Create a web view on [[ChatActivityData]] with the following columns: FeedbackActivityId, FeedbackBotMessage and FeedbackFlows.
5. Add the view to a custom dashboard for analysis.
