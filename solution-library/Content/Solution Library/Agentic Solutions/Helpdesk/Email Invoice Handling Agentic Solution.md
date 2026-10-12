---
title: Email Invoice Handling Agentic Solution
---


This intelligent solution automatically processes emails sent to a specified email address, extracting structured invoice data from both the email body and attachments (PDFs and image files). For each invoice received, it creates a case containing the following details:

* Customer and supplier information
* Invoice details: total amount, VAT, purchase order, cost center, due date, and more
* Case type and priority
* Summary and translation: summary and body translated into English

Once saved in the back-end, an agent can respond to the ticket in English (or another chosen language), and the response will be sent back to the user in the language of the original email.

## Prerequisites

* Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
* You should have a AI Agent. For information on how to create an AI Agent, see [Creating AI Agents](https://druidai.gitbook.io/druid-ai-docs/ai-platform/build-ai-agents/authoring-tools/creating-ai-agents).
* Email service.

## Configuring the Skill Template

To configure the skill template, follow these steps:

### Step 1. Install the solution from the Solutions Library

Go to the Solutions Library, search for solution "Email Invoice Handling Agentic Solution" and import it following the instructions provided in section [Installing Solution Templates](<../../Installing Solution Templates.md>).

Wait until the import status shows as “Success”.

### Step 2. Activate Email channel

After importing the solution, navigate to AI Agent Settings. Click the **Channels** tab, and activate the Email channel by following the instructions described in [Email Channel](https://druidai.gitbook.io/druid-ai-docs/channels/web-and-email/email-integration).

### Step 3. Set up the AI Agent special flows

Go to the AI Agent settings, Details page and click the Dialog management section header. The section expands. Select the following special flow:

| Special Flow         | Select            |
| -------------------- | ----------------- |
| Intent rephrase flow | 00\_rephrase-flow |

Scroll down and click **Save & Close**.

### Step 4. Configure the apps connection

1. Go to **Solution Contents** > **Apps**.
2. Search for each of the following apps one by one. Click on the app, and edit its settings as described below:

* **DRUID-LLM**. To configure this app connection, follow these steps:

1. Go to **Administration** > **Druid Services**.
2. Copy the claims and token corresponding to the DRUID.LLM resource you want to use — you’ll need them to configure the app connection.

![](<../../../../.gitbook/assets/druid llm.png>)

{% hint style="info" %}
**NOTE:** If the DRUID.LLM resource does not appear, contact your sales representative to activate DRUID-dedicated resources for one of the following providers on your tenant: Azure OpenAI, Mistral, or Google.
{% endhint %}

3. Go to Solution > Apps and select the **DRUID-LLM** app.
4. In the **Base URL** field, paste the claims value you copied at step b.
5. In the Variables table, enter the token you copied at step b as the key.
6. Click **Save** to complete the configuration.

* **SendGrid**: Enter your SendGrid API key or set up a new SMTP connection to send emails. After entering the SendGrid key, click **Save & Close**.

![](<../../../../.gitbook/assets/Case Handling_app3.png>)

3. Once the apps are configured, click **Publish**.

### Step 5. Run setup flow

Open the AI Agent and in the chat, type “set-prompts” to start the flow that adds custom GPT prompts to the Prompt View, which can be adjusted to meet specific business needs.

The solution is now ready to be used.

## How to use the solution

To create the first invoice case, send an email with an invoice attachment (PDF or image format) to the email address you used when activating the Email channel. The AI Agent will process both the email body and any attachments, then create a case in the **InvoiceCase** view.

To generate an Excel report of all invoices, go to the **Invoice Cases** workspace and in the workspace menu, click **InvoiceCases**. Click the **Automations** icon at the top of the view and select **Download Invoice Cases**.

![](<../../../../.gitbook/assets/download invoices.png>)

To reply to a case, follow these steps:

1. In the InvoiceCase view, click the case you want to respond to. The case form opens.
2. At the top of the view, click the **Automations** icon, then select **Respond to Email**.

![](<../../../../.gitbook/assets/select respond email.png>)

The chat form appears on the right.

![](<../../../../.gitbook/assets/reply email.png>)

3. Enter your reply and click **Send**.

![](<../../../../.gitbook/assets/send email.png>)
