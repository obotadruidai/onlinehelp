---
title: UiPath Start My Day
---


Inspired by the [https://marketplace.uipath.com/listings/start-my-day](https://marketplace.uipath.com/listings/start-my-day) workflow, we added adjustments to the actual process in order to showcase the Druid-UiPath start my day workflow.

This solution template provides you with an [UiPath attended process](https://druidai.gitbook.io/druid-ai-docs/ai-platform/integrations/enterprise-connectors/uipath-connector/running-uipath-attended-processes) that opens the following applications:

* Acme. Open a new account here [https://acme-test.uipath.com/login](https://acme-test.uipath.com/login).
* SAP. Having an SAP subscription is optional.
* Druid tenant. By default, Druid opens the tenant [https://buildabotcitizen01.community.Druidplatform.com](https://buildabotcitizen01.community.druidplatform.com/).

{% hint style="info" %}
**Info:** We recommend you to set up your own Druid tenant.
{% endhint %}

## Setting up the solution

### Step 1: Install the solution template from the Solutions Library

For information on how to install the solution, see [Installing Solution Templates](<Installing Solution Templates.md>).

### Step 2: Set up the Process

**Step 2.1. Download the UiPath Process**

[!\[\](../Resources/Images/Download.png)](https://druiddocs.file.core.windows.net/docs-shares/start-my-day.zip?st=2021-08-16T13%3A17%3A03Z\&se=2024-08-17T13%3A17%3A00Z\&sp=rl\&sv=2018-03-28\&sr=f\&sig=7PUj%2FWO4FkAuwMqJfILypfuTPn%2B8OVM%2BKnMTPxS2rpQ%3D)

Unzip the file, you will need it at the next step.

**Step .2.2. Create Orchestrator folder**

Go to the UiPath Orchestrator and create a new modern folder where you will add the Start My Day Attended UiPath Process.

**Step 2.3. Define the UiPath Assets for Start My Day Attended**

The assets you define will store the credentials (username and password) used for starting the applications.

Under the folder created at the previous step, click the **Assets** tab.

![](../../.gitbook/assets/assets.png)

Add the following UiPath assets:

* **Cred\_ACME**
* **Type**: Credential
* **Username**& **Password**: your ACME login credentials.
* **Cred\_Druid**
* **Type**: Credential
* **Username**& **Password**: your Druid tenant login credentials.
* **Cred\_SAP**
  * **Type**: Credential
  * **Username**& **Password**: your SAP login credentials.

### Step 3: Publish the AREP\_StartMyDay UiPath Process

In the Orchestrator, go to your folder, click the **Automations** tab and at the top right corner of the page, click the **Add process** button. Set up the name **AREP\_StartMyDay**. Select the process published at [step 2.3](UiPath_start_my_day.md#Step_2.3.).

### Step 4: Set up Druid

1. In Druid, go to Apps, search for **UiPathStartMyDay** app and configure the UiPath connection string. For more information, see [Creating the UiPath Connection Strings](https://druidai.gitbook.io/druid-ai-docs/ai-platform/integrations/enterprise-connectors/uipath-connector/creating-the-uipath-connection-strings).
2. Go to the ServiceNow Flows, search for the **UiPath connection string** flow and copy the flow ID.
3. Search for the **my-open-tickets-trigger** flow and open it.
4. Go on the step **trigger-process** and load the process from your orchestrator.
5. Set up the in /out arguments as provided in the table below.

| Input argument | Druid entity               |
| -------------- | -------------------------- |
| in\_openSap    | \[\[StartMyDay]].OpenSap   |
| in\_openDruid  | \[\[StartMyDay]].OpenDruid |
| in\_openAcme   | \[\[StartMyDay]].OpenAcme  |

6. Save the step.
7. Open the AI Agent and run the flow that opens the Start My Day applications, by typing in the chat one of the following phrases:

| English (EN)               | Romanian (RO)                         |
| -------------------------- | ------------------------------------- |
| open my daily applications | deschide-mi aplicatiile pentru astazi |
