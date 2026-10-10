---
title: FAQ Car Rental
---

# FAQ Car Rental

This FAQ solution provides conversational flows that will assist the customer 24/7 in finding the right answer to questions related to rental conditions, payments, insurance policies required for car rental and many more.

### Prerequisites

* Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
* You should have a AI Agent. For information on how to create an AI Agent, see [Creating AI Agents](<../../../2_AI Agents/Creating AI Agents.md>).

### Download solution

In the Druid Portal, go to the Solution Library and from the "Automotive" category, download the **FAQ Car Rental** solution.

### Configuring the solution template

To configure the AI Agent for FAQ Car Rental, in Druid Portal, you need to:

#### Step 1: Configure the AI Agent

{% hint style="info" %}
**NOTE:** FAQ Car Rental default language is set to EN-US and additional language is set to RO. If you want to add additional languages on Healthcare, make sure to add the language of choice as additional AI Agent language and add the according training phrases, synonyms and conditions.
{% endhint %}

To configure the AI Agent for FAQ Car Rental, you need to set special flows.

**Set special flows**

Click the Special Flows section header and select the following special flows:

| Special Flow   | Select                      |
| -------------- | --------------------------- |
| Welcome        | welcome-flow-faq-car-rental |
| IntentNotFound | Intent-not-recognized       |

![](<../../../../.gitbook/assets/faq flows.png>)

In production, you can configure these flows based on your needs.

#### Step 2. Train the AI Agent

Click the **Details** tab, and then click the NLP section header. The NLP area expands. Scroll down to the Train area and click the **Train** button.

![](<../../../../.gitbook/assets/train bot.png>)

{% hint style="info" %}
**NOTE:** It might take a few minutes for the NLP training to complete, so you might need to wait for Druid to finish training all AI Agent entities that have NLP enabled (NLP=true).
{% endhint %}

### See FAQ Car Rental in Action

{% hint style="info" %}
**NOTE:** The AI Agent is trained in two languages: RO and EN. If you want to switch between languages, just type the following commends in the chat:

* “Romana te rog” if you want to switch from EN to RO.
* “English please” if you want to switch from RO to EN.
{% endhint %}

The list below provides you with an extensive list of things you can say to the AI Agent in either English or Romanian.

|                                                                                 |                                                                                  |
| ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| Intents                                                                         |                                                                                  |
| English (EN)                                                                    | Romanian (RO)                                                                    |
| Will I need my passport to pick up a car?                                       | Am nevoie de pasaport cand vin sa preiau masina?                                 |
| What is the maximum period of rental?                                           | Care este perioada maxima pentru care pot inchiria o masina?                     |
| Can I rent a car if I do not have a credit card?                                | Pot inchiria o masina daca nu am un card de credit?                              |
| Do I get a refund if I return my car early?                                     | O sa imi rambursati diferenta de bani daca returnez masina mai devreme?          |
| What is Theft Protection (TP)?                                                  | Ce este protectia impotriva furtului (TP)?                                       |
| What happens if I get a speeding ticket or other fines during my rental period? | Ce se intampla daca iau o amenda de viteza in timp ce merg cu masina inchiriata? |
| How old do I need to be to rent a car?                                          | Ce varsta trebuie sa am pentru a putea inchiria o masina?                        |
| Can I book a one-way car rental?                                                | Pot rezerva o închiriere de mașini într-un singur sens?                          |
| What is CDW?                                                                    | Ce inseamna CDW?                                                                 |
| Is a car rental deposit required?                                               | Este necesar un depozit bancar cand inchiriezi masina?                           |
| Do I need to refuel the vehicle before returning?                               | Trebuie sa realimentez masina inainte de a o returna?                            |
| What is your pet policy?                                                        | Care este politica dvs. pentru animalele de companie?                            |
