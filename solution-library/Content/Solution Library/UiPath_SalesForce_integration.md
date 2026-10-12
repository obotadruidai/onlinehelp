---
title: UiPath Salesforce Integration
---


Use this solution template if you want to showcase the ticket management process in Salesforce for opening a new ticket, see your tickets list and close tickets by using Druid-UiPath unattended activities integration.

## Prerequisites

* Tenant Druid community or Druid subscription.
* UiPath Orchestrator subscription, Community or Enterprise edition.
* Salesforce account used for ticket management integration. You need to have a Salesforce instance. If you don't have one, go to [https://www.salesforce.com](https://www.salesforce.com/) and create your first Salesforce instance.

## Setting up the solution template

### Step 1. Install the solution from the Solutions Library

For information on how to install the solution, see [Installing Solution Templates](<Installing Solution Templates.md>).

### Step 2. Download the UiPath processes

[!\[\](../Resources/Images/Download.png)](https://druiddocs.file.core.windows.net/docs-shares/Salesforce.zip?st=2021-08-16T15%3A02%3A50Z\&se=2024-08-17T15%3A02%3A00Z\&sp=rl\&sv=2018-03-28\&sr=f\&sig=tuqUvraoIe2j32UvdUujziAfO9sho8Ao4j%2BFy4rfX38%3D)

The archive contains the following files:

* add-salesforce-ticket - used to showcase the creation of new tickets in Salesforce
* get-salesforce-tickets – used to get the list of open tickets
* close-salesforce-ticket – used to close a ticket in Salesforce

{% hint style="info" %}
**NOTE:** The **get-salesforce-tickets** process is using Druid-UiPath integration via queues while the other processes are using the integration via webhooks.
{% endhint %}

Unzip the files, you will need them during the processes setup.

### Step 3. Set up the UiPath processes

**Step 3.1. Create Orchestrator folder**

Go to the UiPath Orchestrator and create a new modern folder where you will add the Salesforce Ticket UiPath Processes.

**Step 3.2. Define the UiPath Assets for Salesforce**

Under the folder created at the previous step, click the **Assets** tab.

![](../../.gitbook/assets/assets.png)

Add the following UiPath assets:

* **Salesforce Consumer**
* **Type**: Credential
* **Username**: Your Salesforce Client Id
* **Password**: Your Salesforce Client Secret.
* **SalesForce Endpoint & Security Token**
* **Type**: Credential
* **Username**: The endpoint URL of your Salesforce instance.
* **Password**: Your Salesforce Security Token.
*   **Salesforce User\&Pass**

    * **Type**: Credential
    * **Username** & **Password**: Your Salesforce instance credentials.

    > **NOTE:** You must have admin privileges with your Salesforce instance credentials.

**Step 3.3. Publish the Salesforce Ticket UiPath Processes**

{% hint style="info" %}
**NOTE:** The UiPath setup for the UiPath processes **add-salesforce-ticket** and **close-salesforce-ticket** is done on the [Druid-Uipath integration via Webhooks](https://druidai.gitbook.io/druid-ai-docs/ai-platform/integrations/enterprise-connectors/uipath-connector/starting-uipath-unattended).
{% endhint %}

**3.3.1 For each of the following UiPath Processes: add-salesforce-ticket and close-salesforce-ticket, follow these steps:**

1. Go to the **Config.json** file and open it.
2. Set up the name of the folder where you will add the process.

![](<../../.gitbook/assets/Setting up the Add ServiceNow.png>) ![](<../../.gitbook/assets/Setting up the Add ServiceNow_1.png>)

3. Go to the **Main.xaml**, open it.
4. To publish the process in your orchestrator, click **Publish**.

**3.3.2 Publish the get-salesforce-tickets process**

{% hint style="info" %}
**NOTE:** The UiPath setup for the **get-salesforce-tickets** process is done on the [Druid-Uipath integration via Orchestrator queues](https://druidai.gitbook.io/druid-ai-docs/ai-platform/integrations/enterprise-connectors/uipath-connector/running-unattended-process-using-orchestrator-queues).
{% endhint %}

To publish this process, follow these steps:

1. Open UiPath Studio.
2. Click **Open a Local Project**. Browse for the > get-salesforce-tickets folder (from prerequisites) and choose the project.json file.
3. Right click on the process name and click Open Project Folder.
4. Open the **Framework** folder, then the **Config** folder. There are two json files.
5. Open DruidConfig.json. Complete all the fields as shown in the screenshot and save.

![](<../../.gitbook/assets/config json.png>)

6. Fill in the correct service account username or email address and the password for a service account, which has enough permissions to create a flow.
7. Open UiPathConfig.json. Complete the folder name and the queue name you previously created.

![](<../../.gitbook/assets/uipath json.png>)

8. Switch to UiPath Studio. Click **Publish**.

### Step 4: Set up Druid

1. In Druid, go to **Apps**, search for Salesforce UiPath and configure the connection string to your orchestrator following the procedure described in [Creating the UiPath Connection Strings](https://druidai.gitbook.io/druid-ai-docs/ai-platform/integrations/enterprise-connectors/uipath-connector/creating-the-uipath-connection-strings).
2. Go to **Integrations** and configure each UiPath integration following the integration procedure as listed below:

| UiPath Process          | Integration Procedure                                                                                                                      |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| add-salesforce-ticket   | [Starting UiPath Unattended Processes](https://druidai.gitbook.io/druid-ai-docs/ai-platform/integrations/enterprise-connectors/uipath-connector/starting-uipath-unattended)                                           |
| close-salesforce-ticket | [Starting UiPath Unattended Processes](https://druidai.gitbook.io/druid-ai-docs/ai-platform/integrations/enterprise-connectors/uipath-connector/starting-uipath-unattended)                                           |
| get-salesforce-tickets  | [Running Unattended Process using Orchestrator Queues](https://druidai.gitbook.io/druid-ai-docs/ai-platform/integrations/enterprise-connectors/uipath-connector/running-unattended-process-using-orchestrator-queues) |

3. Go to the Salesforce Flows, search for the **show-open-tickets-response** flow and copy the flow ID.
4. Search for the **show-open-tickets-trigger** flow and open it. It contains only one step.
5. Click the edit icon.
6. In the Set Variables section, modify the variable **\[Case]].FlowId** with the flowId taken from the **show-open-tickets-response** flow.
7. Save the step.
8. Open the AI Agent and type in the chat one of the following phrases:

| English (EN)                  | Romanian (RO)                   |
| ----------------------------- | ------------------------------- |
| I want to open a new ticket   | Vreau sa postez un nou incident |
| I want to see my tickets list | Arata-mi lista ticketelor       |
| Set up closing for my ticket  | Vreau sa inchid ticketul        |
