---
title: "UiPath Unattended Process"
---

<a id="UiPathUnattendedProcess"></a>


Triggering unattended robots will execute tasks and interact with applications independent of human interaction. They typically perform batch operations that do not require user intervention. For example, a batch of new client information is received in a spreadsheet and needs to be entered into multiple applications.

The process includes UiPath integration with unattended automation. Contact Center Agent is chatting with the AI Agent and triggers an unattended automation.

{% hint style="info" %}
**NOTE:** You need a UiPath tenant but you can easily open a free Community subscription.
{% endhint %}

1. Download the UiPath process you want to use:

- UiPath process via webhooks

[!\[\](../Resources/Images/Download.png)](https://druiddocs.file.core.windows.net/docs-shares/Druid_StartingPack_Unattended_Webhook.zip?st=2021-07-22T09%3A38%3A01Z&se=2024-07-23T09%3A38%3A00Z&sp=rl&sv=2018-03-28&sr=f&sig=rpMANMdkXlYdKIGxu8i4yk5WaLN2aFMem5%2FQ83dtAeI%3D)

- UiPath process via queues - Retrieve response from UiPath with single item

[!\[\](../Resources/Images/Download.png)](https://druiddocs.file.core.windows.net/docs-shares/UiPath_Starter_Unattended_Single_Item.zip?st=2021-07-22T09%3A36%3A07Z&se=2024-07-23T09%3A36%3A00Z&sp=rl&sv=2018-03-28&sr=f&sig=Z6toNlo3nO7sHKIBR760M4y812vLgOYp2jaM83m0L4w%3D)

- UiPath process via queues - Retrieve response from UiPath with a collection

[!\[\](../Resources/Images/Download.png)](https://druiddocs.file.core.windows.net/docs-shares/UiPath_Starter_Unnatended_Queues_List.zip?st=2021-07-22T09%3A36%3A27Z&se=2024-07-23T09%3A36%3A00Z&sp=rl&sv=2018-03-28&sr=f&sig=s6YB1HlId7UTKGa5ftVi0dJSpq622Bm8Tyaz9GWmUZU%3D)

2. On the desired AI Agent, import the **Druid\_StartingPack\_Unattended**.zip file. For information on how to import solutions, see [Importing Solutions](https://druidai.gitbook.io/druid-ai-docs/release-lifecycle-and-versioning/importing-solutions).
3. Customize the process based on your needs following the appropriate procedure listed in the table below.

| UiPath process | Procedure |
| --- | --- |
| UiPath process via webhooks | [Starting UiPath Unattended](https://druidai.gitbook.io/druid-ai-docs/integrations/enterprise-connectors/uipath-connector/starting-uipath-unattended) |
| UiPath process via queues - Retrieve response from UiPath with single item | [Running Unattended Process using Orchestrator Queues](https://druidai.gitbook.io/druid-ai-docs/integrations/enterprise-connectors/uipath-connector/running-unattended-process-using-orchestrator-queues) |
| UiPath process via queues - Retrieve response from UiPath with a collection | [Running Unattended Process using Orchestrator Queues](https://druidai.gitbook.io/druid-ai-docs/integrations/enterprise-connectors/uipath-connector/running-unattended-process-using-orchestrator-queues) |
