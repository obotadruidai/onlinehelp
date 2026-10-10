---
layout:
  title:
    visible: false
---

<a id="TroubleshootingConnectorErrors"></a>

# Troubleshooting Connector Errors

The connector errors are marked with **CONN ERR** in the error details. When you see a CONN ERROR, it means that there is a PreAction or PostAction call on the Flow Step that raises the respective error.

![](../../../Resources/Images/troubleshooting/error%20details.png)

Close the error details pop-up and in the table check the flow and the flow step on which the error occurs.

![](../../../Resources/Images/troubleshooting/conn%20error%20flow%20step.png)

Go to **Flows** and search for the flow on which the connector error occurs. Open the step on which the error occurred, go to the action section (PreAction / PostAction)

![](../../../Resources/Images/troubleshooting/error%20flow%20step%20action.png)

Open the connector action in a new tab. The Edit Connector Action page appears.

![](../../../Resources/Images/troubleshooting/edit%20connector%20action.png)

Click the **ConnectorAuditLog** tab. The Connector Audit Log details appears. It displays the log of all connector calls from today. You can view the connector log within a different time range by selecting the Date range.

![](../../../Resources/Images/troubleshooting/many%20log%20entries.png)

If the connector audit log has many entries, you can filter the log by searching for the **Correlation ID**, the one provided in the chat and used to search in the Conversation History.

![](../../../Resources/Images/troubleshooting/search%20log%20by%20corr%20id.png)

To see the Audit log details, click the magnifier icon (![](../../../Resources/Images/troubleshooting/magnifier%20icon.png)) displayed inline with the log entry.

![](../../../Resources/Images/troubleshooting/audit%20log%20details.png)

The Audit log details contains the following information:

- User Information
- Action Information – allows you to identify on which point the action failed.
- Error State – provides you with the error description.

To understand what went wrong, you need to read the Action Information in the following order:

1. Request Entity
2. Request Task. If the value in the Request Task is null that means that the request action task has not been executed.
3. Response Task. If the value in the Response Task is null, that means that no response was received from the 3rd party system.
4. Response Entity.

If the Request Task is “null”, check the **Error State**, there might be something wrong in the Connector Request.

*Example: wrong URL*

![](../../../Resources/Images/troubleshooting/WRONG%20URL.png)

If all four fields contain data other than null, that means that there was something wrong mapping the response data to the Response Entity.

<a id="Testingthattheissuenolongeroccurs"></a>

## Testing that the issue no longer occurs

The Druid AI Platform provides you with the possibility to test the requests directly at design time, without having to publish the modification. This way, you can troubleshoot connector errors faster and publish the connector only when you are satisfied with the test result.

To test a request, in the Edit Connector Action page, click the **Test** tab, then click the **RequestEntity** tab. In the **JSON** field, provide request entity by copy/pasting it from the Audit Log Details, **Request Entity** field. Click the **Test** button.

If the test is successful, you can save and publish the action.

If the test fails, you can navigate through the **Test Result** tabs to troubleshoot misconfiguration.

![](../../../Resources/Images/troubleshooting/test%20results.png)

The **Test Result** tabs are similar to the fields include in the Action Information section of the Audit log details.

## Related Topics
