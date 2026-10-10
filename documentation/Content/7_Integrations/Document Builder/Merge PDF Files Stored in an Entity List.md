<a id="MergePDFFilesStoredinanEntityList"></a>

# Merge PDF Files Stored in an Entity List

> **NOTE:** This feature is available in DRUID 5.25 and higher.

If you store PDF files in an entity list of files and you want to merge them, you can use the Document Builder.

On the desired flow step, in the PostAction section, add a connection action and provide the following details:

| Parameter | Description |
| --- | --- |
| Name | The name of the action. The field is mandatory. |
| Description | A brief description of the action that might be useful for other tenant admins. The field is mandatory. |
| Category | Define on the spot when creating the action. Useful to easily find the actions in the Integrations list. The field is mandatory. |
| Icon | Select the icon that best describes the integration. It helps you easily identify the integration action in the list of integrations. If no icon is selected, DRUID will show default icon. |
| Request Entity Name | The entity used by the AI Agent to send data to the external app via the current action. |
| Response Entity Name | The entity used by the AI Agent to receive data from the external app via the current action. |
| Is Active | Tick to activate the connector action. |

![](../../Resources/Images/Document%20Builder/cnn%20action%20set.png)

Click **Save**.

Add a Document Generator task (Word or Excel).

![](../../Resources/Images/Document%20Builder/word%20task.png)

Click on the integration task and in the right-side editor provide the details described in the table below.

| Field | Description |
| --- | --- |
| Description | Enter a brief description for the task. E.g., Invoice Generation. |
| Generated Extension | Select **PDF**. |
| Password Protected | Tick on **PasswordProtected** to password protect a pdf output document.  On the flow that generates the PDF document, before calling the DocumentGenerator connector, make sure to set the password value in field **[[ChatUser]].PasswordForProtectedFiles** in the Set Variables section.  ![](../../Resources/Images/Document%20Builder/set%20password%20protect.png)  **IMPORTANT!** If you're using [[ChatUser]] as request and response entity on the connector, the password will be saved in clear in the conversation history. |
| Merge PDF templates | Tap on **Merge PDF templates**. |
| PDFs to be merged | **NOTE:** This field is available only if you tap on **Merge PDF templates**.  Enter the name of the entity field (of type entity list of files) that stores the PDFs you want to merge (e.g., [[Account]].Files). |
| Dynamic File Name | Specify the file name of the generated document either hard coded (e.g., "Invoice April") or as a value from the context: an entity field (e.g., [[Employee]].Name) or a local variable.  If the field is empty, DRUID will use the template file name as file name of the generated document. |
| ProjectResultToEntityPath | Select the entity field (a field of type file created on the request entity) that will store the generated document. |

Click the **Save** icon (![](../../Resources/Images/Document%20Builder/save%20integr%20icon_29x30.png)), then the **Publish** icon (![](../../Resources/Images/Document%20Builder/publish%20integration%20icon_34x33.png)) at the top of the right-side editor.
