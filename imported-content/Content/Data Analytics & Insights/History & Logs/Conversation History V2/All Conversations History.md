---
title: All Conversations History
---

# All Conversations History

On the Conversations History page, below the filtering area, click on the **Show all messages**.

When viewing all conversation history, you can:

* debug the flows and flows steps in the Flow Diagram directly from the Conversation History by clicking on the desired flow name or flow step name.
* debug integration errors by viewing the message details and the integration log.

To view message details and the integration log for a specific message, click the **View message details** icon (![](<../../../../.gitbook/assets/Activities grouped by conversations_15.png>)) corresponding to the desired message.

![](<../../../../.gitbook/assets/view message details.png>)

In the Message details, the **Flow log** tab displays the name of the flow where the error occurred.

![](<../../../../.gitbook/assets/flow name click.png>)

Click on the **Integration log** tab, then click the magnifier icon displayed inline with the log entry where the error occurred.

![](<../../../../.gitbook/assets/cnn error.png>)

The flow step where the error appeared displays in the Flow Diagram in a new browser window.

The Integration log detail appears.

![](<../../../../.gitbook/assets/integration log detail.png>)

The Audit log details contains the following information:

* User Information
* Action Information – allows you to identify on which point the action failed.
* Error State – provides you with the error description.

To understand what went wrong, you need to read the Action Information in the following order:

1. Request Entity
2. Request Task. If the value in the Request Task is null that means that the request action task has not been executed.
3. Response Task. If the value in the Response Task is null, that means that no response was received from the 3rd party system.
4. Response Entity.

If the Request Task is “null”, check the **Error State**, there might be something wrong in the Connector Request.

If all four fields contain data other than null, that means that there was something wrong mapping the response data to the Response Entity.

### Testing that the issue no longer occurs

The Druid AI Platform provides you with the possibility to test the requests directly at design time, without having to publish the modification. This way, you can troubleshoot connector errors faster and publish the connector only when you are satisfied with the test result.

To test a request, in the Edit Connector Action page, click the **Test** tab, then click the **RequestEntity** tab. In the **JSON** field, provide request entity by copy/pasting it from the Audit Log Details, **Request Entity** field. Click the **Test** button.

If the test is successful, you can save and publish the action.

If the test fails, you can navigate through the **Test Result** tabs to troubleshoot misconfiguration.

![](<../../../../.gitbook/assets/test results.png>)

The **Test Result** tabs are similar to the fields include in the Action Information section of the Audit log details.

### Related Topics

* [Flow Designer](<../../../4_Flows/Flow Designer.md>)
