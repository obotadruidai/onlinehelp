---
title: Customer 360
---


This skill provides a smart way to scale exceptional sales representative experiences. It includes conversation flows that allow sales representatives to register new leads and clients into the database, search for a client, see and update client information.

| Functionality                      | Description                                                                                                                                    |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| Register a new client              | Conversational flows that allows the sales representative to register a new client / lead into the database.                                   |
| Update client information          | Once a client is registered into the system, the sales representative can always update any client information.                                |
| Search for a client / show Clients | Conversational flows that allow the sales representative to search for a specific client based on phone number, email address or company name. |

## Prerequisites

* Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
* You should have a AI Agent. For information on how to create an AI Agent, see [Creating AI Agents](https://druidai.gitbook.io/druid-ai-docs/build-ai-agents/authoring-tools/creating-ai-agents).
* SQL server connection.

## Configure the skill template

{% hint style="info" %}
**NOTE:** Customer 360 default language is set to EN-US and additional language is set to RO. If you want to add additional languages on Customer 360, make sure to add the language of choice as additional AI Agent language and add the according training phrases, synonyms and conditions.
{% endhint %}

To configure the AI Agent for Customer 360, in Druid Portal:

### Step 1: Set special flows

Click the Special Flows section header and select the following special flows:

| Special Flow   | Select                    |
| -------------- | ------------------------- |
| Welcome        | first-welcome-flow-360    |
| IntentNotFound | Intent-not-recognized-360 |

![](<../../../../.gitbook/assets/Customer 360_2.png>)

In production, you can configure these flows based on your needs.

### Step 2: Set the Connection Strings (Apps) Details

**Prerequisite**

* You need to have a Microsoft Azure SQL subscription. If you do not have one, register for a [12-month free-trial account](https://azure.microsoft.com/en-us/free/sql-database/).

To configure the SQL connector to your DB, from Customer 360 Apps, click **Customer\_360\_SQL**. The Edit Connector page appears.

Make the following settings:

| Setting             | Description                                                                                                                                  |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| ClientType          | Select SqlServer.                                                                                                                            |
| DataSource          | Enter the name of the SQL server.                                                                                                            |
| InitialCatalog      | Enter the name of the database used by the connection string, which is located on the server that you specified in the **DataSource** field. |
| UserID and Password | The credentials (user name and password) of your SQL Server account.                                                                         |

![](<../../../../.gitbook/assets/Customer 360.png>)

Click **Save and Close**.

{% hint style="warning" %}
**IMPORTANT!** In order for the AI Agent integration with the apps to be up and running, you need to publish the connector actions. To do so, from the main menu, click **Integrations** and click the **Publish** button.

<img src="../../../../.gitbook/assets/Customer 360_1.png" alt="" data-size="original">
{% endhint %}

### Step 3: Run Setup Flow

Open chat land AI Agent page and send the message “Setup Client360”. This command sets up all the DB tables needed in Customer 360.

Click **Done**. If the SQL connection strings are properly set, Customer 360 setup completes successfully.

### Step 4. Select AI Agent Framework Version 4 on the AI Agent

{% hint style="warning" %}
**IMPORTANT!** If bot framework version 4 is not available on your tenant, please contact [Druid Support](../../../Solution%20Library/Sales/Customer%20360/mailto:support@druidai.com) to activate it.
{% endhint %}

To allow the AI Agent display the Adaptive Card steps, go to the AI Agent details, click on the General section and from the **Bot Framework Version** field, select **v4**.

![](<../../../../.gitbook/assets/Customer 360_3.png>)

Save the AI Agent.

### Step 5. Train the AI Agent

Click the **Details** tab, and then click the NLP section header. The NLP area expands. Scroll down to the Train area and click the **Train** button.

{% hint style="info" %}
**NOTE:** It might take a few minutes for the NLP training to complete, so you might need to wait for Druid to finish training the AI Agent.
{% endhint %}

## See the AI Agent in action

{% hint style="info" %}
**NOTE:** The AI Agent is trained in two languages: RO and EN. If you want to switch between languages, just type the following commands in the snippet:

* “Romana te rog” if you want to switch from EN to RO.
* “English please” if you want to switch from RO to EN.
{% endhint %}

| Functionality                    | Intents (EN)                                                                                                                                                                                                                             | Intents (RO)                                                                                                                                                                                                                                                           |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Register a new client            | Register new client I want to register a new client I need to register a new client. Can you help me? How do I register a customer? How do I register a new client? Can you help me register a new client? help me register a new client | Înregistrați noul client Doresc să înregistrez un client nou Trebuie să înregistrez un client nou. Ma poti ajuta ? Cum înregistrez un client nou? Cum pot inregistra un client ? Ma puteti ajuta sa inregistrez un client nou? ajutați-mă să înregistrez un client nou |
| Update client information        | update data I need to update a customer data How can I update customer data? How do I update client data? I want to update data I need help to update a client data Help me update client data                                           | Actualizeaza date Trebuie să actualizez datele unui client Cum pot actualiza datele clienților? Cum actualizez datele clientului? Vreau să actualizez datele Am nevoie de ajutor pentru a actualiza datele unui client Ajută-mă să actualizez datele clientului        |
| Search for a client/show Clients | Show clients I want to see all the clients Show me the filtered customers Can I see the filtered clients? I need to search a specific client Can you help me search for a client?                                                        | Arata clientii Vreau să văd toți clienții Arată-mi clienții filtrati Pot vedea clienții filtrati? Trebuie să caut un anumit client Ma puteti ajuta sa caut un client?                                                                                                  |
