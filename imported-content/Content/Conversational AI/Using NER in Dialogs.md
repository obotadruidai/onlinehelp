---
title: "Using NER in Dialogs"
---

<a id="UsingNERinDialogs"></a>


This section covers deterministic NER, which refers to simple entities, that is, flat data type, type other than Entity and Entity List.

<a id="Prerequisite"></a>

## Prerequisite

- You need to have at least one simple entity (entity type other than Entity and Entity List) defined in the system. The entity should have at least one field.

To use NER in dialogs, follow these steps:

<a id="Step1Setflowutterance"></a>

## Step 1. Set flow utterance

Go to the desired flow details, click **Training phrases** and provide at least five utterances with sample value for NER.

{% hint style="info" %}
**NOTE:** The flow engine expects to extract an entity the place where the sample value is located in the flow utterance.
{% endhint %}

{% hint style="info" %}
**Info:** To extract a location, organization or ask the AI Agent for info based on a date range, see [NER Best Practices](#NER_Best_Practices).
{% endhint %}

On the flow set as many utterances as you need providing the entity field.

<a id="Step2TraintheAIAgent"></a>

## Step 2. Train the AI Agent

Once you provide the desired flow utterance, you need to train the AI Agent. To do so, go to AI Agent details, NLP section and click the **Train** button.

From the moment the AI Agent extracts the information from the utterance, the value set in the entity is available in the flow context and you can further use this value in the flow based on your needs.

<a id="Step3Createflowsteps"></a>

## Step 3. Create flow steps

After you train the AI Agent for NLP, go back to the flow and add flow steps to accommodate your needs.

{% hint style="info" %}
**Info:** As there are situations where due to a low NLP model training, the AI Agent does not manage to extract the information from the utterance, we recommend you to add as flow first step, a step of type prompt and ask the user to provide the details again. In the **Input Mapping** field, enter the entity field, which will store the extracted information, and make sure to set on the flow the option **Skip if known**. If the AI Agent extracts the entity value from the flow utterance, it will skip this step.
{% endhint %}

Even from the moment the intent is identified, DRUID extracts the value and sets it in the entity, which you provided in the flow utterance. You can further use the entity on the flow.

<a id="NERBestPractices"></a>

## <a id="NER_Best_Practices"></a>NER Best Practices

<a id="DousetherightprepositiontoextractaLocationorOrganization"></a>

### Do use the right preposition to extract a Location or Organization

There are two main prepositions of location in English, i.e., " in" and "at". Each of these prepositions has a different meaning when used in a sentence. The NLP model is trained on a per-keyword basis, so it is good to know how to use these prepositions in training phrases to extract either a location or an organization.

To extract a Location or Organization from user says and store it in a specific entity field (either of type Location or Organization), in the training phrase on the flow, use the proper preposition in front of the entity field as follows:

- use "in" to extract a larger location like: a country, a city, a neighborhood, etc.
- use "at" to extract an organization / object that is located at an exact position like: City Hall, hotel name, hospital name, etc.

## Training phrases examples

The following example extracts location in **[[test\_location]].location\_name** (a field of type Location) and organization in **[[test\_organization]].test\_organization** (a field of type Organization).

![](../Resources/Images/Flows/special%20phrases.png)

<a id="Addingdaterangeintrainingphrases"></a>

### Adding date range in training phrases

{% hint style="info" %}
**NOTE:** This feature is available in DRUID version 5.0 and higher.
{% endhint %}

Provide complete training phrases with sample values for start date and end date. E.g.: "how many employees updated their personal data 01-01-2023 - 04-19-2023". In this example, the dates are sample values for the range (start date - end date).

{% hint style="info" %}
**NOTE:** Avoid using words that identity a range (e.g., until, between, etc.), otherwise the NLP Engine will fail extracting the date range.
{% endhint %}

Add target entity for the two sample values: [[Entity]].<start date field> - [[Entity]].<end date field>. To do that, select the date and click on the selection. In the pop-up that opens, click in the **Target Entity / Entity** field and select the desired entity / entity field (either the entity field that stores the start date or the one that stores the end date) and click **Save**.

The pop-up closes and the sample values are highlighted in blue and marked with the label Date.

Example:

![](../Resources/Images/Druid%205.12/end%20date.png)

![](../Resources/Images/Druid%205.12/date%20sample%20values.png)

{% hint style="info" %}
**NOTE:** Using sample values in training phrases is available in DRUID 5.12 and higher. This feature is backwards compatible, the training phrases with NER on flows and flow steps remain unchanged; however, we recommend you to update the training phrases with NER to provide sample values for entities.
{% endhint %}

Save the settings.

{% hint style="info" %}
**Info:** To see how the NLP engine extracts a date range from the user intent, go to **Evaluation** and test different input phrases. Example:

![](../Resources/Images/Flows/evaluate%20user%20input.png)
{% endhint %}

## Related Topics

- [Managing Entities](../5_Entities/Managing%20Entities.md)
- [Managing Entity Fields](../5_Entities/Managing%20Entity%20Fields.md)
