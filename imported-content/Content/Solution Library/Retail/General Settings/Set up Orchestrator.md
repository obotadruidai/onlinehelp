---
title: Set up UiPath Data Service Process
---

# Set up UiPath Data Service Process

### Prerequisite

Download the **retail-case-workflow** UiPath process by clicking on the **Download** button below.

[!\[\](../../../Resources/Images/Download.png)](https://druiddocs.file.core.windows.net/docs-shares/retail-case-workflow.zip?st=2022-08-22T07%3A47%3A10Z\&se=2028-08-23T07%3A47%3A00Z\&sp=rl\&sv=2018-03-28\&sr=f\&sig=I2pxe3nIkloDoo2PjcdrRdEEg3oinbRSnZKIZKu1L8w%3D)

Unzip the file, you will need the it later during the process setup.

### Setting up UiPath Data Service Process

Log in [https://cloud.uipath.com/](https://cloud.uipath.com/), go to your orchestrator tenant/Data Service and click the **Create New Entity** button.

![](<../../../../.gitbook/assets/Step 3 Set up Orchestrator.png>)

Create the RetailCase entity with the following fields:

DisplayName:ClientId

NAME: **ClientId**

TYPE:Text

DisplayName:Description

NAME: **Description**

TYPE:Text

DisplayName:OrderNumber

NAME: **OrderNumber**

TYPE:Text

DisplayName:Subject

NAME: **Subject**

TYPE:Text

{% hint style="info" %}
**NOTE:** For all fields select the type **Text**and set up the Maximum Length of 4000 characters.
{% endhint %}

![](<../../../../.gitbook/assets/retail case entity.png>)

Switch to UiPath Studio and open **retail-case-workflow**.

Click **Manage Entities** and select **RetailCase** and **SystemUser**.

![](<../../../../.gitbook/assets/studio entities.png>)

Click **Publish**.

Click **Next**, select **Publish to Orchestrator Tenant Process Feed** and click **Publish**

Set up the **retail-case-workflow** UiPath process by following the [Starting UiPath Unattended Process](<../../../7_Integrations/UiPath/Starting UiPath Unattended.md>) procedure.

After you publish the process in the orchestrator and set up the webhooks, in the Druid Portal, go to **Integrations** and search for the **add-complain-add-case** integration. Load the input and output arguments (TicketNumber>\[\[Case]].TicketNumber) and map them as shown in the figure below:

![](../../../../.gitbook/assets/arguments.png)
