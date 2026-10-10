---
layout:
  title:
    visible: false
---

<a id="Step3SetupOrchestratorVictorAdvancedProcessDataService"></a>

# Step 3: Set up Orchestrator Victor\_Advanced Process\_Data Service

Log in [https://cloud.uipath.com/](https://cloud.uipath.com/), go to your orchestrator tenant/Data Service and create four entities:

![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator.png)

For each entity, add the specific fields as described below.

![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_1.png)

> **NOTE:** For all fields type Text, set up the **Maximum Length** of 4000 characters.

<a id="Currency"></a>

## Currency

![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_2.png)

Click the **Data** tab and add the currencies as described below:

CODE: EUR

MasterId=1

CODE: RON

MasterId=2

![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_3.png)

<a id="FinancingType"></a>

## FinancingType

![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_4.png)

Click the **Data** tab and add the Financing Types data as described below:

![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_5.png)

Name: Refinance

Synonym: Refinance

NameEN: RefinanceEN

MasterId: 3

Name: Nevoi personale

Synonym: nevoi|nevoie|personal

NameEN: Personal Needs

MasterId: 2

Name: Investiții imobiliare

Synonym: teren|apartament|nvestitii|imobiliar|ipotecar

NameEN: Real Estate investments

MasterId: 1

<a id="LoanRequest"></a>

## LoanRequest

![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_6.png)

![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_7.png)

![](../../../Resources/Images/Step%202_Set%20up%20Orchestrator%20Victor_Unattended%20Next%20Best%20Deal%20Process/Step%202%20Set%20up%20Orchestrator_15.png)

![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_9.png)

![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_10.png)

Create new choice set LoanRequestStatus with the following details:

![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_11.png)

![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_12.png)

<a id="Product"></a>

## Product

![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_13.png)

Click the **Data** tab and add the Product Types data as described in the embedded Excel file.

![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_14.png)

Log in to your orchestrator account and click on the tenant used in the basic setup.

On the left on the navigation bar, click the folder you created when setting up the unattended process.

Click the **Queues** tab, click the **Add** icon and complete the fields for a new queue. We will use this queue for adding data to Data Service.

Write down the queue’s name, you will need it later.
![IMG_256](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator.jpg)

![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_15.png)

Open UiPath Studio.

![IMG_259](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_1_176x333.jpg)

Click **Open a Local Project**, browse for the **Add Loan Request Process** folder (from prerequisites) and choose the **project.json** file.
Right click on the process name and click **Open Project Folder**.
![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_16.png)

Open the **Framework** folder, then the **Config** folder. There are two json files.

Open **DruidConfig.json**. Complete all the fields in the file. Fill in the correct service account username or email address and password for a service account, which has enough permissions to create a flow.
![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_17.png)
Save a file.

Open **UiPathConfig.json**. Complete the folder name and the queue name you previously created and the save the file.
![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_18.png)
Switch to UiPath Studio.
Click **Manage Entities**.

![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_19.png)

Tick all checkboxes and click **Save**.

![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_20.png)

Click **Publish**.
![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_21.png)
Click **Next**, select **Publish to Orchestrator Tenant Process Feed** and click **Publish**.
![IMG_266](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_2.jpg)

In your folder, click **Automations** > **Processes** and click the **Add** icon.
![IMG_268](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_3.jpg)

Choose the published package, enter a Process name (optional) and click **CREATE**.
![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_22.png)

Click the **Triggers** tab and then click the **Add** icon.
![IMG_271](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_4.jpg)
Click the **Queue** button, enter a trigger name, select the queue and the process you created previously and click **ADD**.
![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_23.png)

Switch to the UiPath Assistant. Search for the process you created, click the three dots on the right and click **Install**.
![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_24.png)

In the Druid Portal, go to Victor Flows and search for the flow **add-loan-request-response**. Click on it and from the Details page, copy the **Flowid**.

Search for the flow **onboarding-create-instance**and click on it. The flow has only one flow step. Click on it and in the Set Variables section, change the response **[[Offer]].CallbackFlowid** with the flowId of **add-loan-request-response**.

![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_25.png)

Go to Victor Integration, search for the **add-loan-request** connector action and click on it. Click the **LoadOrchestratorData** button and connect to your loan request queue designed in the orchestrator.

![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_26.png)

Search for the **trigger-loan-request-workflow** connector action and click on it. Click the **LoadOrchestratorData** button and connect to the queue designed in the orchestrator.

![](../../../Resources/Images/Step%203_Set%20up%20Orchestrator%20Victor_Advanced%20Process_Data%20Service/Step%203%20Set%20up%20Orchestrator_27.png)
