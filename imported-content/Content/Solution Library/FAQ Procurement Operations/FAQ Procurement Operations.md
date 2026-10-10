---
layout:
  title:
    visible: false
---

<a id="FAQProcurementOperations"></a>

# FAQ Procurement Operations

When talking about the procurement process, employees have lots of questions related to the stages of this process and its many procedures. This FAQ solution covers topics related to purchase requests, supplier selection process, auction, contracts signing and many more.

The solution provides answers to around 80 frequently asked questions related to the procurement process.

<a id="Prerequisites"></a>

## Prerequisites

- Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
- You should have a AI Agent. For information on how to create an AI Agent, see [Creating AI Agents](../../2_AI%20Agents/Creating%20AI%20Agents.md).

<a id="ConfiguringSolutionTemplate"></a>

## Configuring Solution Template

In Druid Portal, go to the Solution Library and from the Procurement category, download the solution.

To configure the solution template, follow these steps:

<a id="Step1Setspecialflows"></a>

### Step 1. Set special flows

> **NOTE:** Grocery default language is set to EN-US and additional language is set to RO. If you want to add additional languages on Grocery, make sure to add the language of choice as additional AI Agent language and add the according training phrases, synonyms and conditions.

Click the Special Flows section header and select the following special flows:

| Special Flow | Select |
| --- | --- |
| Welcome | welcome-flow-faq-procurement-bot |
| IntentNotFound | intent-not-recognized-faq-procurement-bot |

![](../../Resources/Images/Solutions%20Library/faq%20procurement%20flows.png)

In production, you can configure these flows based on your needs.

<a id="Step2TraintheAIAgent"></a>

### Step 2. Train the AI Agent

Click the **Details** tab, and then click the NLP section header. The NLP area expands. Scroll down to the Train area and click the **Train** button.

<a id="SeeFAQProcurementOperationsinAction"></a>

## See FAQ Procurement Operations in Action

> **NOTE:** The AI Agent is trained in two languages: RO and EN. If you want to switch between languages, just type the following commends in the chat:
>
> - “Romana te rog” if you want to switch from EN to RO.
> - “English please” if you want to switch from RO to EN.

The list below provides you with a list of things you can say to the AI Agent in either English or Romanian.

| English (EN) | Romanian (RO) |
| --- | --- |
| How to initiate a PR? | Cum se initiaza un PR? |
| What type of PR do I need to start the supplier selection process? | Ce tip de PR am nevoie pentru a incepe un proces de selectie? |
| Is the market screen the same as a vendor selection? | Market screen ul este acelasi ca o selectie a furnizorilor? |
| What are the criteria for selecting a vendor? | Care sunt criteriile pentru selectarea unui furnizor? |
| Which is the period for submitting the technical evaluation? | Care este perioada pentru a transmite evaluare tehnica? |
| All the suppliers will be evaluated by the same technical criteria? | Toti furnizorii urmeaza sa fie evaluati dupa aceleasi criterii tehnice? |
| Can I get in touch with the suppliers during the selection process? | Pot lua legatura cu furnizorii in timpul procesului de selectie |
| Can the Procurement Department reject the documents provided by the initiator / beneficiary? | Departamentul de achizitii poate respinge documentele furnizate de initiator/ beneficiar? |
| How long does it take to select a vendor? | Cat dureaza procesul de selectie a furnizorului? |
| How long does it take to have the contract reviewed? | Cat dureaza revizuirea contractului? |
| Who signs the contract with a supplier? | Cine are drept de semnatura pe contractul cu un furnizor? |
