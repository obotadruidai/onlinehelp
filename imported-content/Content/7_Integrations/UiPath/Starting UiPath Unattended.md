---
title: Starting UiPath Unattended Processes
---

# Starting UiPath Unattended Processes

DRUID offers a simplified UiPath integration, which enables you to start a job that executes a process directly on a UiPath robot using input arguments.

### How it works

This integration ensures increased security as the UiPath robots are isolated from DRUID external networks. The response to DRUID is fully managed by the UiPath Orchestrator, eliminating the need to have open ports for the robots to communicate with DRUID.

![](<../../../.gitbook/assets/Starting UiPath Unattended.png>)

The new UiPath Connector starts a UiPath process from DRUID and delivers the input information (parameters) via the Orchestrator directly to the processes instead of going through a queue. The new connector is using the input arguments of the process itself. The process sends back the response (output arguments) to DRUID via the Orchestrator’s Webhooks.

### Prerequisites

* You need to create a UiPath connector app. The user used to obtain the UiPath Connector App credentials must have permission to run jobs on the corresponding Orchestrator Folder.
* You should have a published UiPath process with input/output arguments.
* For hybrid and on premise DRUID deployments, you must install DRUID Connector Host version 1.39 or above.

### Related Topics

* [Accessing Druid Endpoints in Druid Hybrid Deployments](<../../Druid Deployment/Accessing Druid Endpoints in Druid Hybrid Deployments.md>)
