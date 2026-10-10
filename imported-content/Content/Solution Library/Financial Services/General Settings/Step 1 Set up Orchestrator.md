---
title: 'Step 1: Set up Orchestrator Victor\_Attended Next Best Deal Process'
---

# Step 1: Set up Orchestrator Victor\_Attended Next Best Deal Process

Go to [https://cloud.uipath.com.](https://cloud.uipath.com)

Log in to your orchestrator account. Download UiPath Studio (if you don’t have it already) by going to the resource center and choosing the Stable Community Edition.

![](<../../../../.gitbook/assets/Step 1 Set up Orchestrator.png>)

![](<../../../../.gitbook/assets/Step 1 Set up Orchestrator_1.png>)

Install UiPath on your PC. Don’t launch it yet, close the Get Started window when it pops up.

![](<../../../../.gitbook/assets/Step 1 Set up Orchestrator_2.png>)

Click on the desired tenant (we will use SetupTenant).

![](<../../../../.gitbook/assets/Step 1 Set up Orchestrator_3.png>)

From the main menu, click Tenant. On the navigation bar, click Machines and click Add.

![](<../../../../.gitbook/assets/Step 1 Set up Orchestrator_4.png>)

Click Machine Template.

![](<../../../../.gitbook/assets/Step 1 Set up Orchestrator_5.png>)

The Add machine page appears. Enter a Template name and click PROVISION.

![](<../../../../.gitbook/assets/Step 1 Set up Orchestrator_6.png>)

The machine is successfully created. Copy the machine key.

![](<../../../../.gitbook/assets/Step 1 Set up Orchestrator_7.png>)

Open the UiPath Assistant app.

Click on **Preferences**.

![](<../../../../.gitbook/assets/Step 1 Set up Orchestrator_8.png>)

From the menu, click Orchestrator Settings. The Orchestrator Configuration appears. From the Connection Type field, select Machine Key and paste the orchestrator URL (_https://cloud.uipath.com/\*account name\*/\*tenant name\*_ and the machine key (the one you copied after provisioning the machine).

![](<../../../../.gitbook/assets/Step 1 Set up Orchestrator_9.png>)

Click Connect. The status changes to “Connected, Unlicensed”.

Go to Users and find your user. Click the three dots on the right and click Edit.

>

![](<../../../../.gitbook/assets/Step 1 Set up Orchestrator_10.png>)

The Edit selected user page appears.

Tap on Automatically create an attended robot for this user.

Select StudioPro as License Type.

![](<../../../../.gitbook/assets/Step 1 Set up Orchestrator_11.png>)

To find your domain\username open the command prompt, type in “whoami” and copy the response.

![](<../../../../.gitbook/assets/Step 1 Set up Orchestrator_12.png>)

Open UiPath Studio.

Click **Open a Local Project**, browse for the **Attended Next Best Deal Process** folder (from the prerequisites) and choose the project.json file.

![](<../../../../.gitbook/assets/Step 1 Set up Orchestrator_14.png>)

Click **Publish**.

![](<../../../../.gitbook/assets/Step 1 Set up Orchestrator_15.png>)

The Publish Process wizard appears. Click Next. Select Publish to Orchestrator Tenant Process Feed and click Publish.

![](<../../../../.gitbook/assets/Step 1 Set up Orchestrator_16.png>)

Switch to UiPath Orchestrator. Go to a modern folder on which you have rights (we’ll be using the Shared folder). Click the Automations tab and click the Add icon.

![](<../../../../.gitbook/assets/Step 1 Set up Orchestrator_17.png>)

The Add Process page appears.

From the Package Name field, select the published package. The other fields will automatically fill in.

![](<../../../../.gitbook/assets/Step 1 Set up Orchestrator_18.png>)

Click CREATE. Switch to the UiPath Assistant. Find the local-Next-Best-Deal and click install .

![](<../../../../.gitbook/assets/Step 1 Set up Orchestrator_19.png>)
