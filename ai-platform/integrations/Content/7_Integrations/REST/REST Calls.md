---
title: REST Calls
---


Integration calls are API calls you configure to pass or request data from the Druid AI Platform to an external data source.

With the AI Agent data model and the DRUID REST app created, you can now start defining the integration actions and tasks.

{% hint style="info" %}
**Info:** In DRUID 5.19 and higher, if you need to use pre-request/post-request scripts like in Postman, you can use the Custom Code task and place it before or after the REST task.
{% endhint %}

You have two options to define the integration actions and tasks:

* Directly in the Flow Diagram. From the Flow Palette, section **Integration - Common**, drag the flow step **Rest** and drop it within the flow where you want DRUID to execute the API call. The integration step contains a dummy integration action and task.
* Using the solution’s Connector Designer. From the main menu of the current solution, click **Integrations**. The Connector Designer appears.

This section describes how to configure a REST integration call using the Connector Designer. The settings described in this section are similar if you're using the Flow Palette and Flow Diagram.

To configure a REST integration call using the Connector Designer, flow these steps:

1. Create a connector action. For detailed information on how to configure an integration call, see [Defining the Integration Actions](<../Defining the Integration Actions.md>).
2. Add a REST task. To add a task, in the Edit Connector Action page, click the ConnectorSteps tab. The page lists all tasks added on the action.
3. At the top-right corner of the page, click Create Task and from the drop-down click **Web** and select **Rest**.

![](<../../../.gitbook/assets/select rest task.png>)

4. Publish the connector action. On the main menu, click **Integrations** and at the top-right corner of the Integrations page, click the **Publish** button.

![](<../../../.gitbook/assets/publish button.png>)

To publish an integration action or task in the Flow Diagram, at the top-right corner of the editor click the **Publish** icon.

![](<../../../.gitbook/assets/publish in editor.png>)

When adding a REST task, you have to follow these steps:

1. Set the task general parameters. For more information, see [General Settings](<General Settings.md>).
2. Configure the request to the API. For more information, see [Request Settings](<Request Settings.md>).
3. Map the response into the conversation context. For more information, see [Response Settings](<Response Settings.md>).
4. Test the integration call. For more information, see [Testing Settings](<Testing Settings.md>).

{% hint style="info" %}
**NOTE:** If you need to send file(s) to an external API endpoint and retrieve a file, use the Download File Integration task and set a request of type **Form Data** or **Binary**. For more information on how to use it, see section [Download File](<DownloadFile/Download File.md>).
{% endhint %}
