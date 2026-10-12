---
title: Setting Up the Contract Termination UiPath Attended Process
---


Go to [https://cloud.uipath.com.](https://cloud.uipath.com)

Log in to your orchestrator account.

Download the UiPath Studio (if you don’t have it already).

![](<../../../../.gitbook/assets/Setting Up the Contract Termination.png>)

Install UiPath on your PC.

Click on the desired tenant (we will use SetupTenant).

![](<../../../../.gitbook/assets/Step 2 Set up Orchestrator.png>)

Go to Tenant(1), Machines(2) and click Add(3).

![](<../../../../.gitbook/assets/Setting Up the Contract Termination_2.png>)

Choose Standard Machine.

![](<../../../../.gitbook/assets/Setting Up the Contract Termination_3.png>)

Open the UiPath Assistant app.

Click on Preferences (1,2).

![](<../../../../.gitbook/assets/AI Center_54.png>)

Go to Orchestrator Settings(1), choose Machine Key(2) and copy the Machine Name(3).

![](<../../../../.gitbook/assets/AI Center_55.png>)

Switch back to Orchestrator, paste in the Name field(1), add an attended license(2) and click PROVISION.

![](<../../../../.gitbook/assets/Setting Up the Contract Termination_6.png>)

Click Copy Machine Key to Clipboard, store it and the extended URL (in our case, [https://cloud.uipath.com/Druidsoft1/SetupTenant/](https://cloud.uipath.com/Druidsoft1/SetupTenant/)).

![](<../../../../.gitbook/assets/Setting Up the Contract Termination_7.png>)

Switch to UiPath Assistant, paste the Machine Key and Orchestrator URL and click Connect .

![](<../../../../.gitbook/assets/Setting up the Read Currencies_8.png>)

After clicking Connect, the status should be “Connected, Licensed”.

Go to the Default(1) folder, click Robots(2) and Add(3).

![](<../../../../.gitbook/assets/Setting Up the Contract Termination_9.png>)

Add a Standard Robot.

![](<../../../../.gitbook/assets/Setting Up the Contract Termination_10.png>)

Choose your machine, enter a name, add a description, select the attended type, enter your Windows user password, and click CREATE.

![](<../../../../.gitbook/assets/Setting Up the Contract Termination_11.png>)

It should look like this:

![](<../../../../.gitbook/assets/Setting Up the Contract Termination_12.png>)

You have created an attended UiPath robot.

Unzip the **terminate-contract-victor zip** file (it contains the UiPath process).

Open UiPath Studio.

Click Open a Local Project and choose the project.json file from the unzipped folder

![](<../../../../.gitbook/assets/AI Center_68.png>)

Switch to UiPath Studio. Click **Publish**.

![](<../../../../.gitbook/assets/Setting Up the Contract Termination_14.png>)

Click **Next**, select **Publish to Orchestrator Tenant Process Feed** and click **Publish**.

![](<../../../../.gitbook/assets/Setting Up the Contract Termination_15.png>)

Go to **Automations** > **Processes** and click **Add**.

![](<../../../../.gitbook/assets/Setting Up the Contract Termination_16.png>)

Choose the published package, enter a Process name and choose your environment.

![](<../../../../.gitbook/assets/Setting Up the Contract Termination_17.png>)

Switch to UiPath Assistant. Find your process (the one waiting for install), click the three dots in its right and click **Install**.

## Related Topics

* [Integrating Using Robot.JS](https://docs.druidai.com/docs/Content/7_Integrations/UiPath/Integrating%20Using%20Robot.JS.htm)
