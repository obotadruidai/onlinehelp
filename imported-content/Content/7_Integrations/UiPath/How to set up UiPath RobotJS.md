---
title: "How to Set Up UiPath RobotJS"
---

<a id="HowtoSetUpUiPathRobotJS"></a>


No connector actions or internal actions are needed in order to run the UiPath attended process. All configurations are made within the Flow Designer.

Running a local process and transferring structured data between the chat AI Agent and the UiPath robot can simply be managed by a flow step of type UiPath which uses the **Automation: attended (Robot JS)** technology.

<a id="Prerequisites"></a>

## Prerequisites

- You should have a published UiPath process with input / output arguments.
- If you want to load a process from the Orchestrator, you need to create a UiPath connector app (see [Creating the UiPath Connection Strings](Creating%20the%20UiPath%20Connection%20Strings.md)). Manually configuring a process is also available (see [Manually add process](#Manually_add_process)).

<a id="Step1AddUiPathflowstep"></a>

## Step 1. Add UiPath flow step

- From the Flow Palette section **Integration - UiPath**, drag the **Start attended process** integration and drop it within the flow where you want DRUID to trigger the attended robot.

![](../../Resources/Images/UiPath%20Connector/select%20start%20attended%20task.png)

When you add a flow step of type UiPath to a flow, the flow step automatically has four child steps, providing you with all possible flow exits:

- **Request successful**. DRUID successfully sends the “Start a job” request to the local UiPath Assistant.
- **Error sending the request**. An error occurred while DRUID tried sending the request to the local UiPath Assistant.
- **After job completes successfully**. The job executed the process and completed successfully.
- **After job completes with error**. An error occurred during the job execution.

![](../../Resources/Images/UiPath%20Connector/start%20unattended%20step.png)

The conditions set on child steps are read-only making the flow configuration simple.

With this new UiPath flow step; there is no need to create a different, dedicated callback flow because the Druid AI Platform knows to resume the flow to the corresponding exit endpoint: either job completes successfully or the job completes with errors.

The events following process job completion can be designed in the same flow from where the process is initiated. After the job completes, the conversation will begin in the same flow, but not from its first step, but directly from one of the two “After job completes…” steps.

<a id="Step2ConfiguretheUiPathflowstep"></a>

## Step 2. Configure the UiPath flow step

**Automation: attended (Robot JS)** is automatically selected in the **Technology** field.

You can [load a process from the Orchestrator](#Load_process_from_Orchestrator) on your local machine, or you can [Manually add process](#Manually_add_process).

<a id="LoadprocessfromOrchestrator"></a>

### <a id="Load_process_from_Orchestrator"></a>Load process from Orchestrator

By default, **Load processes from orchestrator** is selected.

To load a process from Orchestrator on your local machine, follow these steps:

1. From the **Code** field, select the UiPath connector and from the **Process** field, select the desired UiPath attended process. The **Process** field lists all processes in the Orchestrator folder associated to the connector app (connector app specified in the **Code** field).
2. Click the **Load** button (![](../../Resources/Images/Running%20UiPath%20Attended%20Processes/How%20to%20set%20up%20UiPath%20RobotJS_1.png)). The process input and output arguments appear in the table.
3. Map the process input and output arguments to DRUID entity fields.

![](../../Resources/Images/Running%20UiPath%20Attended%20Processes/How%20to%20set%20up%20UiPath%20RobotJS_2.png)

4. At the top-right corner of the right editor, click the **Save** icon (![](../../Resources/Images/Running%20UiPath%20Attended%20Processes/How%20to%20set%20up%20UiPath%20RobotJS_3.png)) to save the step configuration.

<a id="Manuallyaddprocess"></a>

### <a id="Manually_add_process"></a>Manually add process

1. To manually set process information, tap off **Load processes from orchestrator**.
2. In the **Process** field, type the name of the process you created on the local machine.
3. In the Process Input /Output arguments table, click the **Add** icon (![](../../Resources/Images/Running%20UiPath%20Attended%20Processes/How%20to%20set%20up%20UiPath%20RobotJS_4.png)) and add the process input (in) and output (out) arguments.
4. After you add the arguments, select their type (in, out, in / out) and map them to DRUID entity fields.

   ![](../../Resources/Images/Running%20UiPath%20Attended%20Processes/How%20to%20set%20up%20UiPath%20RobotJS_5.png)
5. At the top-right corner of the right editor, click the **Save** icon (![](../../Resources/Images/Running%20UiPath%20Attended%20Processes/How%20to%20set%20up%20UiPath%20RobotJS_3.png)) to save the step configuration.

{% hint style="info" %}
**NOTE:** This conversation will be initiated to the same AI Agent user which triggered the UiPath process.
{% endhint %}

{% hint style="info" %}
**NOTE:** DRUID stores in the system entity **[[UiPathEvent]]**, the following process related information: EventType, JobId, ErrorMessage, StartTime and EndTime.
{% endhint %}

{% hint style="warning" %}
**IMPORTANT!** At first process run, make sure that you [authorize the UiPath Assistant](UiPath%20Assistant%20Authorization.md).
{% endhint %}
