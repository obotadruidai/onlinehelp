---
title: 'Step 4: Set up Orchestrator Victor\_Advanced Process\_Action Center'
---

# Step 4: Set up Orchestrator Victor\_Advanced Process\_Action Center

Go to [https://cloud.uipath.com/](https://cloud.uipath.com/) and log in to your orchestrator account and click on the tenant used in the basic setup.

From the main menu, click the folder you created when setting up the unattended process.

Click the Queues tab.

![IMG\_256](<../../../../.gitbook/assets/Step 4 Set up Orchestrator.jpg>)

Click the Add icon. The Create Queue page appears. Complete the required fields. You will use this queue for adding data to the UiPath Action Center. Write down the queue name.

![](<../../../../.gitbook/assets/Step 4 Set up Orchestrator.png>)

Open UiPath Studio.

![IMG\_259](<../../../../.gitbook/assets/Step 4 Set up Orchestrator_1_176x333.jpg>)

Click Open a Local Project, browse to the Loan Request Workflow Process folder (from the prerequisites) and choose the project.json file.

Right click on the process name and click Open Project Folder.

![](<../../../../.gitbook/assets/Step 4 Set up Orchestrator_1.png>)

Open the Framework folder, then the Config folder. There are two json files.

Open DruidConfig.json. Complete all the fields. Fill in the correct service account username or email address and password for a service account, which has enough permissions to create a flow.

![](<../../../../.gitbook/assets/Step 4 Set up Orchestrator_2.png>)

Open UiPathConfig.json. Complete the correct folder name (the one you created for the unattended process), and the queue name you created for the UiPath Action Center.

![](<../../../../.gitbook/assets/Step 4 Set up Orchestrator_3.png>)

Save the file.

Switch to UiPath Studio. Click Manage Entities.

![](<../../../../.gitbook/assets/Step 4 Set up Orchestrator_4.png>)

Tick all checkboxes.

![](<../../../../.gitbook/assets/Step 4 Set up Orchestrator_5.png>)

Click Save.

Click Publish.

![](<../../../../.gitbook/assets/Step 4 Set up Orchestrator_6.png>)

Click Next, select Publish to Orchestrator Tenant Process Feed and click Publish.

![IMG\_266](<../../../../.gitbook/assets/Step 4 Set up Orchestrator_2.jpg>)

In your folder, click Automations > Processes and click the Add icon.

![IMG\_268](<../../../../.gitbook/assets/Step 4 Set up Orchestrator_3.jpg>)

Choose the published package, enter a Process name (optional) and click CREATE.

![](<../../../../.gitbook/assets/Step 4 Set up Orchestrator_7.png>)

Click the Triggers tab and click the Add icon. ![IMG\_271](<../../../../.gitbook/assets/Step 4 Set up Orchestrator_4.jpg>) Click the Queue button, enter a trigger name, select the queue and the process you previously created and click ADD. ![](<../../../../.gitbook/assets/Step 4 Set up Orchestrator_8.png>)

Switch to UiPath Assistant. Search for the process you created, click the three dots on the right and click Install.

![](<../../../../.gitbook/assets/Step 4 Set up Orchestrator_9.png>)

Go to your folder and click Action Catalogs.

![](<../../../../.gitbook/assets/Step 4 Set up Orchestrator_10.png>)

Add the following Action Catalogs:

![](<../../../../.gitbook/assets/Step 4 Set up Orchestrator_11.png>)
