---
title: "Setting up the Read Currencies UiPath Process"
---

<a id="SettinguptheReadCurrenciesUiPathProcess"></a>


<a id="Step1SetupUIPath"></a>

## Step 1: Set up UIPath

Go to [https://cloud.uipath.com.](https://cloud.uipath.com/Druidsoft1/portal_/home)

Log in to your orchestrator account.

Download the UiPath Studio.

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies.png)

Install UiPath on your computer.

Click on the desired tenant (we will use SetupTenant).

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_1.png)

Go to Tenant, click Machines and then Add.

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_2.png)

Choose Machine Template.

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_3.png)

Add a name and a description and click PROVISION.

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_4.png)

Copy the Machine Key and the extended URL (in our case, [https://cloud.uipath.com/Druidsoft1/SetupTenant/](https://cloud.uipath.com/Druidsoft1/SetupTenant/)), as you will need them later.

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_5.png)

Open the UiPath Assistant app.

Click on Preferences.

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_6.png)

Go to Orchestrator Settings and choose Machine Key. The Machine Name will be automatically filled in.

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_7.png)

Paste the Machine Key and Orchestrator URL (the ones you copied earlier) and click Connect.

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_8.png)

After clicking Connect, the status should be “Connected, Unlicensed” for now.

Go to Tenant, click Users, and search for your email address.

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_9.png)

Click the 3 dots on its right and select Edit.

Go to the Unattended Robot section and enable “Automatically create an unattended robot for this user”.

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_10.png)

Open the command prompt app and type in "whoami". Copy the answer and paste it in the Domain\Username field.

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_11.png)

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_12.png)

In the Password field, write the password of your Windows Credentials for this machine and click UPDATE.

You have created an UiPath Floating Unattended Robot.

Go to the Folders tab and click New Folder.

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_13.png)

Give the new folder a name, a description, select Modern as folder type and Tenant package feed as process packages source and click CREATE.

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_14.png)

In the Tenant > Folders tab, select your folder, go to Machine Templates and click Manage Machine Templates.

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_15.png)

Select your Machine Template (the one you created earlier) and click UPDATE.

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_16.png)

On the left navigation bar, click the folder you created. Go to Queues, click Add and complete the fields for a new queue. Store the queue’s name.

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_17.png)

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_18.png)

Unzip the read-currencies-victor file (it contains the UiPath project).

Open UiPath Studio.

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_19.png)

Click Open a Local Project and choose the project.json file from the unzipped folder.

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_20.png)

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_21.png)

Right click on the process name and click Open Project Folder.

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_22.png)

Open the Framework folder, then the Config folder. There are 2 json files.

Open DruidConfig.json. Complete all the fields as shown in the screenshot and save.

Fill in the correct service account username or email address and password for a service account, which has enough permissions to create a flow.

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_23.png)

Open UiPathConfig.json. Complete both fields and save. Make sure to add the correct folder name, and the correct queue name (the ones you created earlier), and save.

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_24.png)

Switch to UiPath Studio. Click Publish.

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_25.png)

Click Next, select Publish to Orchestrator Tenant Process Feed and click Publish.

In your folder, go to Automations, Processes and click Add.

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_26.png)

Choose the published package, enter a Process name and click CREATE.

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_27.png)

Go to Automations, Triggers and click Add.

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_28.png)

Click the big Queue button, give the trigger a name, select the queue you created for this specific process and click ADD.

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_29.png)

Switch to UiPath Assistant. Find the process “awaiting for install”, click the three dots in its right and click Install.

<a id="Step2SettingupDruid"></a>

## Step 2: Setting up Druid

1. Log into the Druid Portal and go to Flows.
2. Search for the **currency-exchange-rate-response** flow and click on it.
3. From the flow **Details** tab, copy the FlowId.
4. Go back to the flows list and search for the **currency-exchange-rate** flow.
5. Click on it and go to step **uipath-process**.
6. Change the response **[[Currency]].ResponseFlowId** with the flowId of currency-exchange-rate-response.

![](../../../Resources/Images/Setup%20read%20currency%20flow_OldUIPath/Setting%20up%20the%20Read%20Currencies_30.png)

## Related Topics

- [Running Unattended Process using Orchestrator Queues](../../../7_Integrations/UiPath/Running%20Unattended%20Process%20using%20Orchestrator%20Queues.md)
