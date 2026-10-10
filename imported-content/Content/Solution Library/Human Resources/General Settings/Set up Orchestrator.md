---
layout:
  title:
    visible: false
---

<a id="SetupUiPathDataServiceProcess"></a>

# Set up UiPath Data Service Process

<a id="Prerequisite"></a>

## Prerequisite

Download the **employment-workflow** UiPath process by clicking on the **Download** button below.

[!\[\](../../../Resources/Images/Download.png)](https://druiddocs.file.core.windows.net/docs-shares/CristinaHR/employment-workflow.zip?st=2021-04-26T07%3A50%3A01Z&se=2022-03-31T07%3A50%3A00Z&sp=rl&sv=2018-03-28&sr=f&sig=6RpjJetGWdD68a3zlwEZlEtmHDEMLfK7HqTs5QLBqy4%3D)

Unzip the file, you will need the it later during the process setup.

<a id="SettingupUiPathDataServiceProcess"></a>

## Setting up UiPath Data Service Process

Log in [https://cloud.uipath.com/](https://cloud.uipath.com/), go to your orchestrator tenant/Data Service and create the Offer entity:

![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator.png)

Add the fields as shown in the figures below:

![](../../../Resources/Images/solution%20templates/Cristina/ofefr%20entity%201.png)

![](../../../Resources/Images/solution%20templates/Cristina/offer%20entity%202.png)

Log in to your orchestrator account and click on the tenant used in the basic setup.

On the left on the navigation bar, click the folder you created when setting up the unattended process.

Click the **Queues** tab, click the **Add** icon and complete the fields for a new queue. We will use this queue for adding data to Data Service.

Write down the queue’s name, you will need it later.
![](../../../Resources/Images/solution%20templates/Cristina/queue.png)

Open UiPath Studio.

Click **Open a Local Project**, browse for the **Employment Workflow Process** folder (from prerequisites) and choose the **project.json** file.

Right click on the process name and click **Open Project Folder**.

![](../../../Resources/Images/solution%20templates/Cristina/employment%20workflow%20folder.png)

Open the **Framework** folder, then the **Config** folder. There are two json files.

Open **DruidConfig.json**. Complete all the fields in the file. Fill in the correct service account username or email address and password for a service account, which has enough permissions to create a flow.
![](../../../Resources/Images/solution%20templates/Cristina/druid%20config%20json.png)

Open **UiPathConfig.json**. Complete the correct folder name (the one you created for the unattended process), and the queue name you created for the UiPath Action Center.

![](../../../Resources/Images/solution%20templates/Cristina/uipath%20config.png)

Save the file.

Switch to UiPath Studio.

Click **Manage Entities** and choose **Offer**.

![](../../../Resources/Images/solution%20templates/Cristina/manage%20entities.png)

Click **Save** and then click **Publish**.

![](../../../Resources/Images/solution%20templates/Cristina/publish.png)

In your folder, click **Automations** > **Processes** and click the **Add** icon.

Choose the published package, enter a Process name (optional) and click **CREATE**.

![](../../../Resources/Images/solution%20templates/Cristina/create%20process.png)

Click the **Triggers** tab and click the **Add** icon.

![](../../../Resources/Images/solution%20templates/Cristina/add%20trigger.png)

Click the **Queue** button, enter a trigger name, select the queue and the process you created previously and click **ADD**.

![](../../../Resources/Images/solution%20templates/Cristina/trigger%20process.png)

Switch to the UiPath Assistant. Search for the process you created, click the three dots on the right and click **Install**.

Go to your folder and click **Action Catalogs** and add "**Level 1: Manager**" action.

![](../../../Resources/Images/solution%20templates/Cristina/action%20catalogs.png)

In the Druid Portal, go to the connector **save-employee-offer-dataservice** and load orchestrator data (click the **LoadOrchestratorData** button). Choose the queue name that you just created.

![](../../../Resources/Images/solution%20templates/Cristina/druid%20connector%20setting.png)
