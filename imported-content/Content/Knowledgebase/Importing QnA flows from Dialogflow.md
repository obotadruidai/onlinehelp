<a id="ImportingQnAflowsfromDialogflowES"></a>

# Importing QnA flows from Dialogflow ES

DRUID QnA provides a streamlined way to import root level intents with no follow-up intents from Dialogflow Essentials (ES), putting at your disposal the Dialogflow data source (intents and responses).

In DRUID, the QnA is a special type of conversational flow designed to simplify the business user experience when creating simple conversations. They are comprised of training phrases (primary and alternate questions) and a single step of type Message that delivers the response to the user (answer).

> **IMPORTANT!**  DRUID does not import Dialogflow ES agent entities, parameters, triggers, etc., if you want to have the flows working similarly as in Dialogflow, additional configuration is required in DRUID.

<a id="Prerequisites"></a>

## Prerequisites

- You have a published AI Agent for which you created a solution.
- You have a Dialogflow ES agent which has only root level intents, no follow up intents.

![](../Resources/Images/Importing%20QnA%20flows%20from%20DialogFlow%20ES/Importing%20QnA%20flows%20from%20Dialogflow.png)

- The default language of the Dialogflow agent must match the AI Agent default language.

<a id="Step1ExportagentfromDialogflowES"></a>

## Step 1. Export agent from Dialogflow ES

1. Go to the [Dialogflow ES Console](https://dialogflow.cloud.google.com).
2. Select an agent.
3. Click the **Settings** icon  ![](../Resources/Images/Importing%20QnA%20flows%20from%20DialogFlow%20ES/Importing%20QnA%20flows%20from%20Dialogflow_1.png) next to your Dialogflow agent name.

![](../Resources/Images/Importing%20QnA%20flows%20from%20DialogFlow%20ES/Importing%20QnA%20flows%20from%20Dialogflow_2.png)

Click the **Export and Import** tab and click the **EXPORT AS ZIP** button.

![](../Resources/Images/Importing%20QnA%20flows%20from%20DialogFlow%20ES/Importing%20QnA%20flows%20from%20Dialogflow_3.png)

4. The zip archive is saved on your PC in the default Download folder.

<a id="Step2ImportQnAflowsinDRUID"></a>

## Step 2. Import QnA flows in DRUID

1. Log into Druid Portal.
2. From the selectors at the top of the page, select the AI Agent and solution.
3. On the main menu, click **QnA**.
4. Click the **Upload** button and select **DialogflowArchive**.

![](../Resources/Images/Importing%20QnA%20flows%20from%20DialogFlow%20ES/Importing%20QnA%20flows%20from%20Dialogflow_4.png)

The DialogFlowArchive pop-up appears.

![](../Resources/Images/Importing%20QnA%20flows%20from%20DialogFlow%20ES/Importing%20QnA%20flows%20from%20Dialogflow_5.png)

5. Browse for the archive exported from Dialogflow and click the **Upload** button.

If you meet all prerequisites, the QnAs will be imported successfully.

![](../Resources/Images/Importing%20QnA%20flows%20from%20DialogFlow%20ES/Importing%20QnA%20flows%20from%20Dialogflow_6.png)

> **NOTE:**
>
> - The root intents from dialog flow will be the DRUID’s QnAs primary questions while the intents training phrases will be DRUID alternate questions.
>
> ![](../Resources/Images/Importing%20QnA%20flows%20from%20DialogFlow%20ES/Importing%20QnA%20flows%20from%20Dialogflow_7.png)
>
> - If a Dialogflow intent has multiple responses and responses with multiple variants, DRUID will concatenate the 1st responses and ignore response variants.
>
> ![](../Resources/Images/Importing%20QnA%20flows%20from%20DialogFlow%20ES/Importing%20QnA%20flows%20from%20Dialogflow_8.png)
>
> - DRUID ignores entities, parameters, triggers, etc.

<a id="Step3TraintheAIAgent"></a>

## Step 3. Train the AI Agent

Go to the AI Agent settings. Click the **Details** tab, and then click the NLP section header. The NLP area expands. Scroll down to the Train area and click the **Train** button.

> **NOTE:** It might take a few minutes for the NLP training to complete, so you might need to wait for DRUID to finish training all AI Agent entities that have NLP enabled (NLP=true).
