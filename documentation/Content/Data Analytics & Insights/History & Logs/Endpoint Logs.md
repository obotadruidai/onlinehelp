<a id="EndpointLogs"></a>

# Endpoint Logs

Endpoint Logs allows authors to evaluate the Start flow events from initial call up to conversation triggering.

To access the Endpoint Logs, from the main menu, click **History & Logs**, then click **Endpoint Logs**.

![](../../Resources/Images/troubleshooting/endpoint%20menu.png)

To view the logs, select the AI Agent and click the **Refresh** button at the top-right corner of the page.

Endpoint logs contain the history of all Druid StartFlow API events, which are mostly used by the UiPath and Namirial processes.

![](../../Resources/Images/Release%20Notes/endpoint%20logs.png)

The Endpoint Logs contain the following information about StartFlow API calls:

| Log info | Description |
| --- | --- |
| Date and time | The date and time (UTC) when the StartFlow API call was executed. |
| Status |  |
| Called Identifier | The Druid AI Platform automatically recognizes only the UiPath and Namirial calls. |
| Endpoint | Druid specific endpoint. |
| Flow | The flow triggered in the conversation. |
| Target User | The user for which the conversation will be started. |
| ExecutionId | **UiPath only!** The ID of the Druid “Place Item To UiPath Queue” connector task, which started the UiPath process that triggered the Druid conversation via StartFlow. |
| Connector Action Name | **UiPath only!** The name of the Connector Action which generated the ExecutionId mentioned above. |
| IP Address | The IP address of the calling system. |
| Duration | The duration from initial API call until the Flow is triggered in the conversation. |

To see the logging details of a specific call, click the lens icon in front of the log entry.

![](../../Resources/Images/Release%20Notes/endpoint%20log%20details.png)

If you want to see information about all Druid calls to a specific UiPath process and the corresponding call back data, all in a single place, click the **ExecutionId** and the Connector Audit Log Detail pop-up will appear containing all the information.

![](../../Resources/Images/Release%20Notes/audit%20log%20details.png)
