---
title: Handling Input Mapping Exceptions
---

# Handling Input Mapping Exceptions

You can configure the way AI Agents handle exceptions on flow steps with input mapping where Druid validates the input data.

#### Exception types

Druid addresses four types of exceptions, which are treated independently at runtime:

* **Integration Error** (CNN Error) – Handles connector errors. It means that there is a PreAction or PostAction call on the Flow Step that raises the respective error.
* **Internal Action Error** – There is an internal action on the flow step that throws an exception or returns false.
* **Exceeded number of input mapping attempts** – The number of input attempts was reached or file uploads with text from user input has failed.
* **Uploaded file type not supported** – The user uploaded a file with extension other than the supported file extentions: .pdf, .png, .jpg, .jpeg, .doc, .docx, .xls, .xlsx, .odt, .ods, .tiff, .tif, .mp3, .mp4, .mkv, .webm, .txt, .json and .csv.

{% hint style="info" %}
**NOTE:** For mobile channels (e.g., MS Teams on mobile), when uploading an image in the chat, the image extension is automatically changed to .png. The antimalware check allows a mismatch between the file extension .png and the following file signatures: jpg, png, jpeg, tif, tiff and bmp.
{% endhint %}

{% hint style="warning" %}
**IMPORTANT!** Set Variable error will NOT raise an exception; they will remain “silent” errors allowing the flow to continue its defined execution, but logging the errors in Conversation History.
{% endhint %}

### How it works

On a flow step with input mapping or file upload steps, you can set the number of input attempts when Exception Handler is active. The way DRUID treats the exceptions is described below:

1. DRUID resets the error context at the beginning of the flow step execution; it sets \[\[SystemError]] to null.
2. DRUID executes the flow step by the existing rules (runs the integrations, performs data validation, NER, etc.), counts the number of iterations of the step and compare it against the defined number of input attempts set on the flow step.
3. DRUID continues the flow execution as follows:

* If the user provides valid input, the AI Agent will either continue the flow or do intent switch.
* When the number of input attempts is reached, DRUID stops the flow step execution at that point and proceeds to the Exception step, executing the Exceeded Attempts step that meets the specific condition.
* In case an error occurs in the pre-actions, DRUID will raise a CNN error (executes the CNN Error step).

![](<../../.gitbook/assets/Exception Handling on Flow_3.png>)

{% hint style="warning" %}
**IMPORTANT!** For flow steps with input mapping and exception handler active, when none of the Exception child steps conditions is met, DRUID will trigger the special flow ExceptionFlowId set on the AI Agent (AI Agent Details > Special Flows).
{% endhint %}

### How to handle exceptions on flow steps with input mapping

On the desired step, go to the Metadata section, toggle on **Exception handler** and select the **Number of attempts**.

![](<../../.gitbook/assets/Exception Handling on Flow_4.png>)

Save the step.

A new child step of type action is automatically added to the flow, with the name format “\_Exception” which will be executed whenever condition `[[SystemError]].IsException == true` is met. The step condition is also automatically set and is read-only.

![](<../../.gitbook/assets/Exception Handling on Flow_5.png>)

Based on the types of exceptions you want to be treated at runtime, add child step(s) to the Exception step and set the specific step condition as listed in the table below:

| Exception type                                                                                                                         | Step condition                                           |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- |
| Integration error (CNN Error)                                                                                                          | \[\[SystemError]].ExceptionType == “ConnectorError”      |
| Internal Action Error                                                                                                                  | \[\[SystemError]].ExceptionType == “InternalActionError” |
| Exceeded the number of input attempts                                                                                                  | \[\[SystemError]].ExceptionType == “ExceededAttempts”    |
| Uploaded file type not supported                                                                                                       | \[\[SystemError]].ExceptionType == “UnsupportedFileType” |
| For exceptions that occur due to other reasons than the ones mentioned above. E.G., errors that occur on adaptive cards submit button. | \[\[SystemError]].ExceptionType == “OtherException”      |

### Removing exceptions from flow steps with input mapping

You cannot delete the Exception step from the Flow diagram. To remove exception handling, on the step with input mapping, go to the Metadata section and tap off **Exception Handler**. A warning message appears. Click **OK** to remove the Exception step and its child steps (if any).
