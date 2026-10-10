---
title: "Generate a PDF Document and Merge it With PDFs from DRUID Storage"
---

<a id="GenerateaPDFDocumentandMergeitWithPDFsfromDRUIDStorage"></a>


This section describes how to use the Document Builder to generate a PDF document using a specific document template (Word or Excel), then merge it with other PDF files stored in DRUID storage, Documents.

{% hint style="warning" %}
**IMPORTANT!** You can only merge a generated PDF document with specific PDF files stored in the DRUID Document Templates. You cannot generate a Word or Excel file and then merge it with specific PDF files.
{% endhint %}

<a id="Step1Createthedocumenttemplate"></a>

## Step 1. Create the document template

<a id="Prerequisite"></a>

### Prerequisite

- Before creating templates, you need to define the entities from which the Document\_Generator connector will merge entity-sourced dynamic data. If you want to dynamic generate a table, which contains records from a collection, make sure that on your parent entity there is a field of type Entity List, which references a collection entity.

<a id="Whichtypeofdocumenttemplateshouldyoubeusing"></a>

### Which type of document template should you be using?

If you need a document, which returns records from a collection and perform calculations based on specific formulas, than the Excel template is the right answer; otherwise, use Word templates.

<a id="Howdocumentgenerationworks"></a>

## How document generation works

When the AI Agent executes a flows step that has the action defined by the AI Agent author for document generation, the Document\_Generator connector app fills in the document template mentioned in the integration task with entity-sourced dynamic data and returns the output in the format/extension provided the integration task (either Word (doc, docx), Excel (xls, xlsx) or user-friendly PDF).

<a id="Howtocreateadocumenttemplate"></a>

### How to create a document template

On your local computer, create the document template (word or excel) that best suits your needs following the appropriate instructions: [Creating Word Document Templates](Creating%20Word%20Document%20Templates.md) or [Creating Excel Templates](Creating%20Excel%20Templates.md).

<a id="Step2Uploaddocuments"></a>

## Step 2. Upload documents

In the Druid Portal, you need to add to DRUID storage the document template you created on your local computer and the PDF files you want to merge with the PDF file that will be generated from the document template. Select the AI Agent and the solution, from the solution main menu, click **Documents**, then follow the procedure below:

At the top-right corner of the page, click the **Create New Template** button. The **Create or update document** page appears. Click on General.

Enter a **Name** and **Category** for the file to upload, then browse for the document template (either Word or Excel) and select it.

![](../../Resources/Images/Document%20Builder/Step%202%20Upload%20document.png)

Click **Save**.

<a id="Step3GeneratemergedPDFfile"></a>

## Step 3. Generate merged PDF file

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

Add a Document Generator specific task that suits your document template (Word or Excel).

![](../../Resources/Images/Document%20Builder/word%20task.png)

Click on the integration task and in the right-side editor provide the details described in the table below.

| Field | Description |
| --- | --- |
| Description | Enter a brief description for the task. E.g., Invoice Generation. |
| Use Dynamic Template Name | Use dynamic template to specify the document template to be used from a DRUID entity field, instead of a fixed template, e.g., [[Employee]].TemplateName. If you tap on this option, the **DocTemplateName** will be replaced by the **Dynamic Template Name** field.  For more information, see [Generate Documents with Dynamic Templates](Generate%20Documents%20with%20Dynamic%20Templates.md). |
| Document Template Name | Select the template you uploaded to Documents. |
| Generated Extension | Select **PDF**. |
| Password Protected | Tick on **PasswordProtected** to password protect a pdf output document.  On the flow that generates the PDF document, before calling the DocumentGenerator connector, make sure to set the password value in field **[[ChatUser]].PasswordForProtectedFiles** in the Set Variables section.  ![](../../Resources/Images/Document%20Builder/set%20password%20protect.png)  **IMPORTANT!** If you're using [[ChatUser]] as request and response entity on the connector, the password will be saved in clear in the conversation history. |
| Merge PDF templates | Tap on **Merge PDF templates**. |
| PDFs to be merged | **NOTE:** This field is available only if you tap on **Merge PDF templates**.  If the filename of the PDF file you want to merge is stored in an entity field of type string, provide the entity name field here (e.g., [[Account]].Appendix).  If you want to merge multiple PDF files with the PDF file generated from the selected document template, then in this field provide as string the name of the PDF files you uploaded in Documents (the names as their appear in Documents, including the filename extension) separated by comma. E.g., "Appendix1.pdf,Appendix2.pdf,Appendix3.pdf"  **Info:** The connector will merge the PDFs in the order they appear in the string you provide in the **PDFs to be merged** field. |
| Dynamic File Name | Specify the file name of the generated document either hard coded (e.g., "Invoice April") or as a value from the context: an entity field (e.g., [[Employee]].Name) or a local variable.  If the field is empty, DRUID will use the template file name as file name of the generated document. |
| ProjectResultToEntityPath | Select the entity field (a field of type file created on the request entity) that will store the generated document. |

Click the **Save** icon (![](../../Resources/Images/Document%20Builder/save%20integr%20icon_29x30.png)), then the **Publish** icon (![](../../Resources/Images/Document%20Builder/publish%20integration%20icon_34x33.png)) at the top of the right-side editor.
