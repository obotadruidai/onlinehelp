---
title: 'Step 2: Set up Orchestrator Victor\_Unattended Next Best Deal Process'
---

# Step 2: Set up Orchestrator Victor\_Unattended Next Best Deal Process

Go to [https://cloud.uipath.com](https://cloud.uipath.com/) and log in to your orchestrator account.

Click on the desired tenant (we will use SetupTenant).

![](<../../../../.gitbook/assets/Step 2 Set up Orchestrator.png>)

From the main menu, click Tenant. On the navigation bar, click the Machines tab and click the Add icon.

![](<../../../../.gitbook/assets/Step 1 Set up Orchestrator_4.png>)

Click Machine Template.

![](<../../../../.gitbook/assets/Step 2 Set up Orchestrator_2.png>)

The Add machine page appears. Enter a Template name, an unattended runtime license and click PROVISION.

![](<../../../../.gitbook/assets/Step 2 Set up Orchestrator_3.png>)

Click **Copy Machine Key to Clipboard**.

![](<../../../../.gitbook/assets/AI Center_53.png>)

Copy the extended URL (in our case, [https://cloud.uipath.com/Druidsoft1/SetupTenant/](https://cloud.uipath.com/Druidsoft1/SetupTenant/)).

Open the UiPath Assistant app.

Click on Preferences.

![](<../../../../.gitbook/assets/Step 2 Set up Orchestrator_5.png>)

From the main menu, click Orchestrator Settings. The Orchestrator Configuration page appears. From the Connection Type field, select Machine Key. The system automatically fills in the Machine Name field.

Paste the Machine Key and the Orchestrator URL (the ones you previously copied) and click Connect.

![](<../../../../.gitbook/assets/Step 2 Set up Orchestrator_6.png>)

The machine status changes to “Connected, Unlicensed”.

Go to Tenant, click Users, and search for your email address.

![](<../../../../.gitbook/assets/AI Center_57.png>)

Click the three dots on the right and click Edit. The Edit user page appears.

On the page menu, click Unattended Robot and tap on Automatically create an unattended robot for this user.

Open the command prompt app and type in “whoami”, copy the answer and paste it in the Domain\Username field.

![](<../../../../.gitbook/assets/AI Center_59.png>)

In the Password field, write the password of your Windows account for this machine and click UPDATE.

![](<../../../../.gitbook/assets/Step 2 Set up Orchestrator_9.png>)

You successfully created an UiPath Floating Unattended Robot!

On the navigation bar, click Folders, and then click New Folder.

![](<../../../../.gitbook/assets/Step 2 Set up Orchestrator_10.png>)

The New Folder page appears. Enter a folder Name and Description. Select Modern as Folder Type, select Tenant package feed as Process packages source and click CREATE.

![](<../../../../.gitbook/assets/Step 2 Set up Orchestrator_11.png>)

In the Tenant, click the Folders tab, select your folder, go to **Machine Templates** and click Manage Machine Templates.

![](<../../../../.gitbook/assets/Step 2 Set up Orchestrator_12.png>)

Select your Machine Template (the one you created) and click UPDATE.

![](<../../../../.gitbook/assets/AI Center_64.png>)

On the navigation bar, click the folder you created. Click the Queues tab, and then click the Add icon.

![](<../../../../.gitbook/assets/Step 2 Set up Orchestrator_14.png>)

The Create Queue page appears. Complete the required fields. Write down the queue’s name, you will need it later.

![](<../../../../.gitbook/assets/Step 2 Set up Orchestrator_15.png>)

Click Add. The queue appears in the Queues page.

Open UiPath Studio.

Click **Open a Local Project**. Browse for the Unattended Next Best Deal Process folder > next-best-deal-victor folder (from prerequisites) and choose the project.json file.

![](<../../../../.gitbook/assets/Step 2 Set up Orchestrator_17.png>)

Right click on the process name and click Open Project Folder.

![](<../../../../.gitbook/assets/Step 2 Set up Orchestrator_18.png>)

Open the Framework folder, then the Config folder. There are two json files.

Open DruidConfig.json. Complete all the fields as shown in the screenshot and save.

Fill in the correct service account username or email address and the password for a service account, which has enough permissions to create a flow.

![](<../../../../.gitbook/assets/Step 2 Set up Orchestrator_19.png>)

Open UiPathConfig.json. Complete the folder name and the queue name you previously created.

![](<../../../../.gitbook/assets/Step 2 Set up Orchestrator_20.png>)

Switch to UiPath Studio. Click **Publish**.

![](<../../../../.gitbook/assets/Step 2 Set up Orchestrator_21.png>)

Click **Next**, select **Publish to Orchestrator Tenant Process Feed** and click **Publish**.

![](<../../../../.gitbook/assets/Step 2 Set up Orchestrator_22.png>)

In your folder, on the navigation bar, click Automations > Processes and click the Add icon.

![](<../../../../.gitbook/assets/AI Center_75.png>)

Choose the published package, enter a Process name and click CREATE.

![](<../../../../.gitbook/assets/Step 2 Set up Orchestrator_24.png>)

Click the Triggers tab, and then and click the Add icon.

![](<../../../../.gitbook/assets/Step 2 Set up Orchestrator_25.png>)

Click the Queue button. The Create Trigger page appears. Enter a trigger Name, select the queue and the process you previously created.

![](<../../../../.gitbook/assets/Step 2 Set up Orchestrator_26.png>)

Click ADD.

Switch to the UiPath Assistant. Search for the process you created, click the three dots on the right and click Install.

![](<../../../../.gitbook/assets/Step 2 Set up Orchestrator_27.png>)

In the Druid Portal, go to Victor Flow sand search for \[SME] UiPathResponse. Double click on it, go to the flow details and copy the Flowid.

Search for the flow \[SME] Next\_Best\_Deal. Click on it. Go to the flow step Trigger-Uipath-Process, click Edit and in the Set Variables section, change the response \[\[Offer\[\[.CallbackFlowid with the flowId of the \[SME] UiPathResponse (the one copied previously).
