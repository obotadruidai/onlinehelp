---
title: How to Set Up the UiPath Integration
---


Using the Flow Designer, you can easily set up this UiPath integration by adding a flow step of type UiPath and configuring it as best suits you needs. You can either create a new flow or add a new step to an existing flow.

{% hint style="info" %}
**Info:** You can also use classic DRUID Designers to create / edit the flow, connector action and integration task.
{% endhint %}

## Step 1. Add UiPath flow step

To add a flow step that will trigger an UiPath unattended robot, you have two options:

* Using the Flow Palette. From section **Integration - UiPath**, drag the **Start unattended process** integration and drop it within the flow where you want DRUID to trigger the unattended robot.

![](<../../../.gitbook/assets/select start unattended task.png>)

DRUID will automatically create (for this step) a connector action (named -) and a task (named "StartUiPathUnattendedJob"), which you can configure to accommodate your UiPath integration.

* Using the Flow Designer in list view . Add a new flow step and edit it as follows: in the General section, from the **Type** field, select **UiPath** and from the **Technology** field, select **Automation: unattended**. If you want to add a connector action and an integration task on the step after save, tap on **Automatically add unattended integration to this step (after Save)**.

![](<../../../.gitbook/assets/uipaths tep list view.png>)

When you add a flow step of type UiPath to a flow, the flow step automatically has four child steps, providing you with all possible flow exits:

* **Request successful**. DRUID successfully sends the “Start a job” request to the Orchestrator.
* **Error sending the request**. An error occurred while DRUID tried sending the request to the Orchestrator.
* **After job completes successfully**. The job executed the process and completed successfully.
* **After job completes with error**. An error occurred during the job execution.

![](<../../../.gitbook/assets/start unattended step.png>)

The conditions set on child steps are read-only making the flow configuration simple.

With this new UiPath flow step; there is no need to create a different, dedicated callback flow because the Druid AI Platform knows to resume the flow to the corresponding exit endpoint: either job completes successfully or the job completes with errors.

The events following process job completion can be designed in the same flow from where the process is initiated. After the job completes, the conversation will begin in the same flow, but not from its first step, but directly from one of the two “After job completes…” steps.

This conversation can be initiated either to the same AI Agent user which started the UiPath process (tap on the **Use current user for callback** option), or to a certain user, specified on the dedicated field on the UiPath step (when the option is disabled). In that field, provide the MasterId of the required user in one of the following formats:

* “” (directly a string)
* @ (DRUID local variable)
* \[\[]]. (DRUID entity field of type string).

## Step 2: Add connector action

{% hint style="info" %}
**NOTE:** If you added the **Start unattended process** integration from the Flow Palette or a new UiPath step with Technology **Automation: unattended** and **Automatically add unattended integration to this step (after Save)** tap on, the step automatically contains a connector action named -. Click on it and skip step 1 and step 2 below.
{% endhint %}

1. Click on the flow step of type UiPath. Click on the Post Actions section header. The section expands.
2. Click the **Add new** button (![](<../../../.gitbook/assets/How to set up the UiPath Integration_2.png>)). A new connector action appears in the Post Actions section and the right-side editor appears allowing you to configure the connector action.
3. In the Connector Action editor, provide the mandatory information (**Name**, **Description** and **Category**), select the entity which will be both request and response entity and mark the action as being active (tick **Is Active** option).

![](<../../../.gitbook/assets/edit connector action.png>)

4. Optionally, from the **Icon** field, select the icon that best describes the integration. It helps you easily identify the integration action in the list of integrations. If no icon is selected, DRUID default icon per selected app type will be shown in the apps list.

{% hint style="info" %}
**NOTE:** The **Icon** field is available in DRUID 1.71 and higher.
{% endhint %}

5. To save the configuration, at the top-right corner of the right-editor, click the **Save** icon (![](<../../../.gitbook/assets/How to set up the UiPath Integration_5.png>)).

## Step 3: Add integration task

{% hint style="warning" %}
**IMPORTANT!** You cannot add more than one connector action with a “Start UiPath Unattended Process” integration task.
{% endhint %}

{% hint style="info" %}
**NOTE:** If you added the **Start unattended process** integration from the Flow Palette or a new UiPath step with Technology **Automation: unattended** and tap on **Automatically add unattended integration to this step (after Save)**, the step automatically contains a task named "StartUiPathUnattendedJob". Click on it and skip step 1 and step 2 below.
{% endhint %}

1. In the Post Actions section, below the connector action, click the **Add task** icon (![](<../../../.gitbook/assets/How to set up the UiPath Integration_6.png>)). A drop-down appears.
2. Scroll down and select **Start UiPath Unattended Process**.

![](<../../../.gitbook/assets/How to set up the UiPath Integration_8.png>)

A new integration task appears in the Post Actions section, below the connector action and the right-side editor appears allowing you to configure the integration task. By default, the **Request** tab displays.

![](<../../../.gitbook/assets/How to set up the UiPath Integration_9.png>)

Unlike other UiPath integrations, the Start UiPath Unattended Process integration task allows you to set both the request and response, as DRUID will communicate with the UiPath robots via the Orchestrator.

3. Provide a suggestive **Description** for the integration task.
4. From the **ConnectionCode** field, select the Uipath connector app. You can use the same connector app for both adding an item to queue and starting unattended UiPath processes.
5. The **Process** field lists all active processes in the Orchestrator folder associated to the connector app (connector app specified in the ConnectorCode field). Select the desired process you want to start.
6. Select the **Job priority** to control which job has precedence over other competing jobs. A job can have one of the following priorities: **Normal**, **Low** and **High**.
7. Select the **Job type**. Note that the list of job types is the one provided by the Orchestrator based on the user allocated in the Orchestrator for the DRUID integration and the configuration of your tenant, robots and folders.

{% hint style="info" %}
**NOTE:** This field appears only if you’re connected to an Orchestrator modern folder.
{% endhint %}

8. The **Execution target** options depend on the type of Orchestrator folder is associated to the UiPath connector app, as follows:

*   For Orchestrator modern folders, the **Execution target** field automatically fills in with **Allocate dynamically**, which means that the Orchestrator automatically allocates the job on the available robot(s).

    > **IMPORTANT!** From DRUID you can start a process only once. If you want to run the process several times, then go through the flow again.
*   For Orchestrator default / classic folders, two Execution targets are available: **Specific robots** and **Allocate dynamically**.

    Figure: Modern Orchestrator Folder

    ![](<../../../.gitbook/assets/How to set up the UiPath Integration_10.png>)

    Figure: Classic Orchestrator Folder

    ![](<../../../.gitbook/assets/How to set up the UiPath Integration_11.png>)

    If you have a classic folder and you want to select a specific robot to execute your process, from the **Execution target** field, select **Specific robots**. From the **Robot** field, select the desired robot.

    > **NOTE:**
    >
    > * The **Robot** field lists the robots that are active. In order for a process to be executed at job runtime, the specified robot needs to be available.
    > * Please note that at design time (that is, the time when you configure the integration task, the robot might be active but not available; at job start time (that is, the time when the job executes the process on the specified robot) the robot needs to be available.

9. Click the **Load arguments** button. The input arguments of the UiPath process are loaded and appear in the Process input arguments table.

![](<../../../.gitbook/assets/How to set up the UiPath Integration_12.png>)

10. Map the Process input parameters to DRUID entity fields.

{% hint style="info" %}
**NOTE:** Starting with DRUID version 1.47, you can transfer complex data such as data collections (Entity List), unique set of data (Entity) or the entire content of a DRUID entity between DRUID and UiPath. For information on how to map complex data, see [Transferring Complex Data Type through the Start Unattended Job Integration](<Transferring Complex Data.md>).
{% endhint %}

![](<../../../.gitbook/assets/How to set up the UiPath Integration_13.png>)

11. Click the **Response** tab and click the **Load arguments** button. The process output arguments are loaded and appear in the Process output arguments table.
12. Map the Process output parameters to DRUID entity fields.

{% hint style="info" %}
**NOTE:** Starting with DRUID version 1.47, you can transfer complex data such as data collections (Entity List), unique set of data (Entity) or the entire content of a DRUID entity between DRUID and UiPath. For information on how to map complex data, see [Transferring Complex Data Type through the Start Unattended Job Integration](<Transferring Complex Data.md>).
{% endhint %}

{% hint style="info" %}
**NOTE:** Input and Output arguments table cannot be edited; therefore, no argument can be added or deleted, you can only use the arguments definition of the UiPath process itself.
{% endhint %}

![](<../../../.gitbook/assets/How to set up the UiPath Integration_14.png>)

13. To save the integration task, at the top-right corner of the right-editor, click the **Save** icon (![](<../../../.gitbook/assets/How to set up the UiPath Integration_5.png>)).

{% hint style="info" %}
**Info:** Write-down or save to a document the values provided in the fields **DRUID Endpoint URL** and **DRUID Endpoint Secret**, as you will need them later. You can also get these details from the connector app page.
{% endhint %}

## Step 4. Publish the integrations

You can either publish integrations one by one at creation time by clicking the **Publish** icon (![](<../../../.gitbook/assets/publish icon.png>)) at the top right-corner of the editor or publish or publish the integrations in bulk. To do so, on the main menu, click **Integrations** and at the top-right corner of the Integrations page, click the **Publish** button (![](<../../../.gitbook/assets/publish button_61x32.png>)).

## Step 5. Set webhooks to connect Orchestrator events to DRUID

The process runs asynchronously, so you need to define what happens after the job completes. The process needs to call back DRUID.

To do so, in Orchestrator, click **Tenant** and from the top menu, click **Webhooks**.

![](<../../../.gitbook/assets/How to set up the UiPath Integration_16.png>)

In the **URL** field, paste the value of the **DRUID Endpoint URL** and in the **Secret** field, paste the value of the **DRUID Endpoint Secret**.

For DRUID hybrid deployments, when you have both the Orchestrator and DRUID Connector Host installed on premise, and orchestrator webhook cannot make calls outside internal network, in the webhook URL field type the URL in the following format: _http://localhost:5008/Druidendpoints/{\*\*catchAll}_.

Where:

* Localhost is the address of the machine where the DRUID Connector Host is installed and can be accessed from another machine within the intranet.
* {\*\*catchAll} is the DRUID endpoint. To take this endpoint, in the Druid Portal, go to your UiPath connector app and from the DRUID Endpoint URL copy only the endpoint.

![](<../../../.gitbook/assets/endpoint druid.png>)

{% hint style="info" %}
**NOTE:**

* Only DRUID Connector Host version 1.52 or above exposes a local endpoint to receive calls from the on premise UiPath Orchestrator.
* Make sure that UiPath Orchestrator has access to DRUID Connector Host machine, on port 5008.
{% endhint %}

Tick **Enabled**.

Select **Individual Events** as **Event Type**, select **Jobs** and from the list, select the first two jobs:

* **Job completed**. A job has completed successfully. The event is linked to the UiPath child flow step **After Job Complete (Success)**.
* **Job faulted**. A job has failed to finish execution (incl. app exceptions). The event is linked to the UiPath child flow step **After Job Complete (Error)**.

{% hint style="info" %}
**NOTE:**

* We recommend you to select only these two types of events, as at this moment, the Druid AI Platform will ignore all other events. In new DRUID versions, we will add support for more orchestrator events.
* As the Orchestrator allows setting Webhooks on a tenant level, it will send all events on all processes existing in all folders on the tenant, including the ones that are not set up in DRUID; however, DRUID will ignore the events transmitted by the Orchestrator, which are not related to processes DRUID started.
{% endhint %}

Click the **UPDATE** button to save the Webhook configuration.

## Related Topics

* [Accessing Druid Endpoints in Druid Hybrid Deployments](<../../Druid Deployment/Accessing Druid Endpoints in Druid Hybrid Deployments.md>)
