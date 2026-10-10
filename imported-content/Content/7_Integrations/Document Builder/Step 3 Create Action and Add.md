---
title: "Step 3. Add Integration Tasks for Documents Generation"
---

<a id="Step3AddIntegrationTasksforDocumentsGeneration"></a>


1. From the main menu, click **Integrations**. The list of actions appears.
2. At the top-right corner of the page, click the **CreateConnectorAction** button (![](../../Resources/Images/Document%20Builder/Step%203%20Create%20Action%20and%20Add.png)). The Edit Connector Action page appears.
3. Provide the following details:

| Parameter | Description |
| --- | --- |
| Name | The name of the action. The field is mandatory. |
| Description | A brief description of the action that might be useful for other tenant admins. The field is mandatory. |
| Category | Define on the spot when creating the action. Useful to easily find the actions in the Integrations list. The field is mandatory. |
| Icon | Select the icon that best describes the integration. It helps you easily identify the integration action in the list of integrations. If no icon is selected, DRUID will show default icon.  ![](../../Resources/Images/default%20icon.png)  **NOTE:** This field is available in DRUID 1.71 and higher. |
| AI Agent | The name of the AI Agent, which will be using the connector action. The field is mandatory. |
| Request Entity Name | The entity used by the AI Agent to send data to the external app via the current action. |
| Response Entity Name | The entity used by the AI Agent to receive data from the external app via the current action. |
| Is Response Collection | Tick only if the response is a list of records. E.g., a list of holidays, whereas each holiday has its own data set. |
| Is Active | Tick to activate the connector action. |

![](../../Resources/Images/Document%20Builder/Step%203%20Create%20Action%20and%20Add_1.png)

4. Click **Save**. The page switches to the [ConnectorSteps](https://documentation.community.druidplatform.com/#steps) tab.
5. At the top-right corner of the page, click the **Create Task** button (![](../../Resources/Images/Document%20Builder/Step%203%20Create%20Action%20and%20Add_2.png)). The drop-down lists all types of integrations tasks you can add.
6. Scroll-down and choose the **Document Generator** task that suits your document template (Word or Excel).

![](../../Resources/Images/Document%20Builder/Step%203%20Create%20Action%20and%20Add_3.png)

The task configuration page appears.

7. Provide the following details:

| Field | Description |
| --- | --- |
| Description | Enter a brief description for the task. E.g., Invoice Generation. |
| Connection Code | Select **Document\_Generator**. |
| Document Template Name | Select the template you uploaded to Documents. |
| Use Dynamic Template Name | **NOTE:** This option is available in DRUID v1.76 and higher.  Use dynamic template to specify the document template to be used from a DRUID entity field, instead of a fixed template, e.g., [[Employee]].TemplateName. If you tap on this option, the **DocTemplateName** will be replaced by the **Dynamic Template Name** field.  For more information, see [Generate Documents with Dynamic Templates](Generate%20Documents%20with%20Dynamic%20Templates.md). |
| Dynamic File Name | **NOTE:** This option is available in DRUID 5.14 and higher.  Specify the file name of the generated document either hard coded (e.g., "Invoice April") or as a value from the context: an entity field (e.g., [[Employee]].Name) or a local variable.  If the field is empty, DRUID will use the template file name as file name of the generated document. |
| Generated Extension | The extension of the output document.  If the task you selected is of type **Word Document Generator**, the following options are available: doc, docx, pdf.  If the task you selected is of type **Excel Document Generator**, the following options are available: xls, xlsx, pdf. |
| Password Protected | **NOTE:** This setting is available in Druid version 1.57 o higher.  Tick on **PasswordProtected** to password protect a pdf output document.  On the flow that generates the PDF document, before calling the DocumentGenerator connector, make sure to set the password value in field **[[ChatUser]].PasswordForProtectedFiles** in the Set Variables section.  ![](../../Resources/Images/Document%20Builder/password%20protected.png)  **IMPORTANT!** If you're using [[ChatUser]] as request and response entity on the connector, the password will be saved in clear in the conversation history. |
| ProjectResultToEntityPath | Store the generated document in a specific entity field (a field of type file created on the request entity). |

Example:

![](../../Resources/Images/Document%20Builder/Step%203%20Create%20Action%20and%20Add_4.png)

8. Click **Save**.
9. Publish the integration.
