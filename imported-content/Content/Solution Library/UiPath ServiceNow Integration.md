---
title: "UiPath ServiceNow Integration"
---

<a id="UiPathServiceNowIntegration"></a>


Use this solution if you want to showcase Druid-UiPath ServiceNow integration.

<a id="Step1DownloadtheUiPathProcesses"></a>

## Step 1: Download the UiPath Processes

[!\[\](../Resources/Images/Download.png)](https://druiddocs.file.core.windows.net/docs-shares/ServiceNow_UiPath_Processes.zip?st=2021-07-13T06%3A08%3A59Z&se=2023-07-14T06%3A08%3A00Z&sp=rl&sv=2018-03-28&sr=f&sig=kQLLAWggSw6l6AMI%2B9CQ08VdRs0Mt3CtAkjUMooHP7I%3D)

The archive contains the following files:

- **add-servicenow-ticket.zip** - used to showcase the creation of new tickets in ServiceNow.
- **close-servicenow-ticket.zip** - used to showcase the closing of a ticket in ServiceNow.
- **get-servicenow-tickets.zip**
- **servicenow-instance-awakening.zip** - used to awaken the ServiceNow instance from UiPath.
- **update-servicenow-ticket.zip** - used to showcase the updating process of a ticket in ServiceNow.

Unzip all files, you will need them during the processes setup.

<a id="Step2SetuptheProcesses"></a>

## Step 2: Set up the Processes

<a id="Prerequisites"></a>

### Prerequisites

- You need to have a ServiceNow instance. If you don't have one, go to [https://developer.servicenow.com](https://developer.servicenow.com/), get a free subscription and create your first instance ServiceNow instance.

<a id="Step1CreateOrchestratorfolder"></a>

### Step 1: Create Orchestrator folder

Go to the UiPath Orchestrator and create a new modern folder where you will add the ServiceNow Ticket UiPath Processes.

<a id="Step2DefinetheUiPathAssetsforServiceNow"></a>

### Step 2: Define the UiPath Assets for ServiceNow

Under the folder created at Step 1, click the **Assets** tab.

![](../Resources/Images/Solutions%20Library/assets.png)

Add the following UiPath assets:

- **ServiceNow Awakening Credentials**

- **Type**: Credential
- **Username**& **Password**: your ServiceNow login credentials.

![](../Resources/Images/Solutions%20Library/awakening%20service%20now%20credentials.png)

- **ServiceNow Client**

- **Type**: Credential
- **Username**: your ServiceNow Client Id
- **Password**: your ServiceNow Client Secret

![](../Resources/Images/Solutions%20Library/service%20now%20client.png)

- **ServiceNow Endpoint**

  - **Type:** Text
  - **Text**: The endpoint URL of your ServiceNow instance. You usually receive the endpoint URL after you create your ServiceNow instance.

  ![](../Resources/Images/Solutions%20Library/service%20now%20endpoint.png)
- **ServiceNow User&Pass**

- **Type**: Credential
- **Username**& **Password**: your ServiceNow instance credentials.
> **NOTE:** You must have admin rights with your ServiceNow instance credentials.

![](../Resources/Images/Solutions%20Library/service%20now%20instance%20credentials.png)

<a id="Step3PublishtheServiceNowTicketUiPathProcesses"></a>

### Step 3: Publish the ServiceNow Ticket UiPath Processes

> **NOTE:** The UiPath setup for the UiPath processes mentioned in step 3.1 is done on the [Druid-Uipath integration via Webhooks](../7_Integrations/UiPath/Starting%20UiPath%20Unattended.md).

##### 3.1 For each of the following ServiceNow Ticket UiPath Processes: add-servicenow-ticket, close-servicenow-ticket, servicenow-instance-awakening and update-servicenow-ticket, follow these steps:

1. Go to the **Config.json** file and open it.
2. Set up the name of the folder where you will add the process.

![](../Resources/Images/Setting%20up%20the%20Add%20ServiceNow%20Ticket%20UiPath%20Process/Setting%20up%20the%20Add%20ServiceNow.png)![](../Resources/Images/Setting%20up%20the%20Add%20ServiceNow%20Ticket%20UiPath%20Process/Setting%20up%20the%20Add%20ServiceNow_1.png)

3. Go to the **Main.xaml**, open it.
4. To publish the process in your orchestrator, click **Publish**.

##### 3.2 Publish the get-servicenow-tickets process

> **NOTE:** The UiPath setup for the **get-service-now-tickets** process is done on the [Druid-Uipath integration via Orchestrator queues](../7_Integrations/UiPath/Running%20Unattended%20Process%20using%20Orchestrator%20Queues.md).

To publish this process, follow these steps:

1. Open UiPath Studio.
2. Click **Open a Local Project**. Browse for the > get-servicenow-tickets folder (from prerequisites) and choose the project.json file.
3. Right click on the process name and click Open Project Folder.
4. Open the **Framework** folder, then the **Config** folder. There are two json files.
5. Open DruidConfig.json. Complete all the fields as shown in the screenshot and save.

![](../Resources/Images/Retail/config%20json.png)

6. Fill in the correct service account username or email address and the password for a service account, which has enough permissions to create a flow.
7. Open UiPathConfig.json. Complete the folder name and the queue name you previously created.

![](../Resources/Images/Retail/uipath%20json.png)

8. Switch to UiPath Studio. Click **Publish**.

<a id="Step4SetupDruid"></a>

### Step 4: Set up Druid

1. In Druid, go to **Apps**, search for ServiceNow UiPath and configure the connection string to your orchestrator following the procedure described in
   [Creating the UiPath Connection Strings](../7_Integrations/UiPath/Creating%20the%20UiPath%20Connection%20Strings.md).
2. Go to **Integrations** and configure each UiPath integration following the integration procedure as listed below:

| UiPath Process | Integration Procedure |
| --- | --- |
| add-servicenow-ticket | [Starting UiPath Unattended Processes](../7_Integrations/UiPath/Starting%20UiPath%20Unattended.md) |
| close-servicenow-ticket | [Starting UiPath Unattended Processes](../7_Integrations/UiPath/Starting%20UiPath%20Unattended.md) |
| get-servicenow-tickets | [Running Unattended Process using Orchestrator Queues](../7_Integrations/UiPath/Running%20Unattended%20Process%20using%20Orchestrator%20Queues.md) |
| servicenow-instance-awakening | [Starting UiPath Unattended Processes](../7_Integrations/UiPath/Starting%20UiPath%20Unattended.md) |
| update-servicenow-ticket | [Starting UiPath Unattended Processes](../7_Integrations/UiPath/Starting%20UiPath%20Unattended.md) |

3. Go to the ServiceNow Flows, search for the **my-open-tickets-response** flow and copy the flow ID.
4. Search for the **my-open-tickets-trigger** flow and open it. It contains only one step.
5. Click the edit icon.
6. In the Set Variables section, modify the variable **[Case]].FlowId** with the flowId taken from the **my-open-tickets-response** flow.
7. Save the step.
8. Open the AI Agent and run the flow that awakes the ServiceNow instance, by typing in the chat "setup-servicenow".
