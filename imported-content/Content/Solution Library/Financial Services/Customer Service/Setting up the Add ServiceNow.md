<a id="SettinguptheAddServiceNowTicketUiPathProcess"></a>

# Setting up the Add ServiceNow Ticket UiPath Process

<a id="Step1CreateOrchestratorfolder"></a>

## Step 1: Create Orchestrator folder

Go to the Orchestrator and create a new modern folder where you will add the Add ServiceNow Ticket UiPath Process.

<a id="Step2PublishtheAddServiceNowTicketUiPathProcess"></a>

## Step 2: Publish the Add ServiceNow Ticket UiPath Process

Unzip the **add-servicenow-ticket** file (it contains the Add ServiceNow Ticket UiPath Process) and go to the **Config.json** file.

Open the Config.json and setup up the name of the folder where you will add the process (the one from step 1).

![](../../../Resources/Images/Setting%20up%20the%20Add%20ServiceNow%20Ticket%20UiPath%20Process/Setting%20up%20the%20Add%20ServiceNow.png)![](../../../Resources/Images/Setting%20up%20the%20Add%20ServiceNow%20Ticket%20UiPath%20Process/Setting%20up%20the%20Add%20ServiceNow_1.png)

Go to the **Main.xaml**, open it.

![](../../../Resources/Images/Setting%20up%20the%20Add%20ServiceNow%20Ticket%20UiPath%20Process/Setting%20up%20the%20Add%20ServiceNow_2.png)

To publish this process in your orchestrator, click Publish.

![](../../../Resources/Images/Setting%20up%20the%20Add%20ServiceNow%20Ticket%20UiPath%20Process/Setting%20up%20the%20Add%20ServiceNow_3.png)

<a id="Step3Addnewprocessinorchestrator"></a>

## Step 3: Add new process in orchestrator

After the folder is created, click on it, go to **Automations** > **Processes**, and click **Add Process**.

![](../../../Resources/Images/Setting%20up%20the%20Add%20ServiceNow%20Ticket%20UiPath%20Process/Setting%20up%20the%20Add%20ServiceNow_4.png)

Select the Package name published from step 2, and click **Continue**.

![](../../../Resources/Images/Setting%20up%20the%20Add%20ServiceNow%20Ticket%20UiPath%20Process/Setting%20up%20the%20Add%20ServiceNow_5.png)

The process runs asynchronously, so you need to define what happens after the job completes. The process needs to call back Druid.

To do so, in Orchestrator, click **Tenant**, and from the top menu, click **Webhooks**.

![](../../../Resources/Images/Starting%20UiPath%20Unattended%20Processes/How%20to%20set%20up%20the%20UiPath%20Integration_16.png)

In the **URL** field, paste the value of the **Druid Endpoint URL** and in the **Secret** field, paste the value of the **Druid Endpoint Secret**.

Tick **Enabled**.

Select **Individual Events** as **Event Type**, select **Jobs** and from the list, select the first two jobs:

- **Job completed**. A job has completed successfully. The event is linked to the UiPath child flow step **After Job Complete (Success)**.
- **Job faulted**. A job has failed to finish execution (incl. app exceptions). The event is linked to the UiPath child flow step **After Job Complete (Error)**.

> **NOTE:**
>
> - We recommend you to select only these two types of events, as at this moment, the Druid AI Platform will ignore all other events. In new Druid versions, we will add support for more orchestrator events.
> - As the Orchestrator allows setting Webhooks on a tenant level, it will send all events on all processes existing in all folders on the tenant, including the ones that are not set up in Druid; however, Druid will ignore the events transmitted by the Orchestrator, which are not related to processes Druid started.

Click the **UPDATE** button to save the Webhook configuration.

Now your UiPath setup is completed.

<a id="Step4SetupDruid"></a>

## Step 4: Set up Druid

1. In Druid, go to Apps and create a new UiPath connection. For information on how to do that, see [Creating the UiPath Connection Strings](../../../7_Integrations/UiPath/Creating%20the%20UiPath%20Connection%20Strings.md).
> **NOTE:** The user used to obtain the UiPath Connector App credentials must have permission to run jobs on the corresponding Orchestrator Folder.

2. Go to integrations, on the connector action called **uipath-covid-claim-process**.
3. Click on the process and choose your process just published in UiPath.
4. Set up your connection code.
5. Select job type **Unattended**.

![](../../../Resources/Images/Setting%20up%20the%20Add%20ServiceNow%20Ticket%20UiPath%20Process/Setting%20up%20the%20Add%20ServiceNow_6.png)

6. Publish the connector.

## Related Topics

- [How to Set Up the UiPath Integration](../../../7_Integrations/UiPath/How%20to%20set%20up%20the%20UiPath%20Integration.md)
