---
layout:
  title:
    visible: false
---

<a id="ReadExcelFile"></a>

# Read Excel File

The Read Excel File integration task allows you to easily read data from an Excel file and then import or update it in the DRUID Data Service or a third-party system.

How to use it:

1. **Upload the Excel file**: The user uploads the Excel file in the chat.
2. **Read data**: The AI Agent reads the data from the first sheet of the file using the Read Excel File integration.
3. **Import / update data**: The data is imported or updated in the target system based on your requirements using other integrations.

> **NOTE:**  This integration task reads data only from the first sheet of the Excel file.

This section describes how to use the Read Excel file integration.

<a id="Step1Createaconnectoraction"></a>

## Step 1. Create a connector action

A Connector Action hosts one or more integration tasks. If it contains multiple tasks, the response data will be returned only after all tasks have run. Data in the response entity might be altered by each task's execution. Thus, only general information is saved and used to describe and identify the action.

Use the Connector Designer or Flow Designer to define integration actions and tasks. This section explains how to add a connector action using the Flow Designer.

1. After the File Upload step, where you receive the Excel file from the user, add a step of type "message" or "action".
2. In the Post actions section of the step, add a connector app.
3. Provide the connector action details by setting the parameters below:

| Parameter | Description |
| --- | --- |
| Name | The name of the action. This field is mandatory. |
| Description | A brief description useful for other tenant admins. This field is mandatory. |
| Category | Define on the spot when creating the action. Useful for finding actions in the Integrations list. This field is mandatory. |
| Icon | Select an icon that best describes the integration. If no icon is selected, DRUID will show a default icon. |
| Request Entity Name | The entity used by the AI Agent to send data via the current action. |
| Response Entity Name | The entity that the AI Agent uses to receive data via the current action. |
| Is Response Collection | Tick only if the expected response is a list of records. |
| Is Active | Tick to activate the connector action. DRUID ignores inactive connector actions at runtime. |

![](../Resources/Images/Read%20Excel%20File/Read%20Excel%20File.png)

4. Save the settings and stay on page to add tasks.

> **NOTE:**  A Connector Action represents a set of one or more integration tasks, which run sequentially and use the same request and response entities.

<a id="Step2AddandconfiguretheReadExcelfileintegration"></a>

## Step 2. Add and configure the Read Excel file integration

After saving the connector action, click the **Open Connector Designer** icon (![](../Resources/Images/Read%20Excel%20File/Read%20Excel%20File_1.png)) next to the connector action. The Connector Designer will appear in a new browser window.

From the Connector Palette, click **Integration – Common**, then drag the **Read Excel file** integration to the working area.

Click the **Settings** icon on the integration task to configure it using the Integration Editor on the right, which defaults to the **General** tab. Set the integration general settings.

<a id="Settheintegrationgeneralsettings"></a>

### Set the integration general settings

On the **General** tab, provide description for the integration and select **Document\_Generator** from the **Connection Code** field. The Read Excel File integration leverages the Document\_Generator app, so you don't need to create a dedicated app for this task.

![](../Resources/Images/Read%20Excel%20File/Read%20Excel%20File_2.png)

<a id="Definetherequest"></a>

### Define the request

Click on the **Request** tab.

In the **DruidFieldForFileName** field, provide the name of the field that stores the Excel file you want to read data from. Reference it by **Name** (e.g., [[Customer]].PaymentsFile.Name).

![](../Resources/Images/Read%20Excel%20File/Read%20Excel%20File_3.png)

If you want to read data from a list of Excel files (e.g., [[Customer]].PaymentFiles), use the **Iterate by** field. For example, using the JSON Path Expression [[Customer]].PaymentFiles[\*] will run the integration for each file in the collection of payment files for a client. You can check your JSON Path expression using the [JSON Path online evaluator](https://jsonpath.com/).

<a id="Definetheresponse"></a>

### Define the response

Click on the **Response** tab to define the response parameters:

| Parameter | Description |
| --- | --- |
| Iterate by (JSON PATH Expression) | The JSON Path expression provided in the Request (if any). This is automatically filled in. |
| Response entity | The entity the AI Agent uses to read data from the Excel file and pass into the conversation context. This is automatically filled in. |
| Response entity is collection | This field is automatically ticked if the Response Entity is expected to be a list of records. |
| Use header row | Select **Table includes header row** if the Excel file contains a header. Otherwise, select **Table doesn’t have header row**. |
| Row filter | The query that filters the response before fields mapping. Provide the query in JSON Path format. Example: $[?(@.year== “2024”)] extracts data only from the rows that have the value ‘2024’ in the column ‘year’.  ![](../Resources/Images/Read%20Excel%20File/Read%20Excel%20File_4.png) |
| Project Result To Entity Path | Use it when you want to map the response directly to an Entity List type field. |

Mapping fields depends on what you selected in the **Use header row** field.

If the Excel file contains a header row, map column names to DRUID entity fields. If not, map column identifiers (A, B, C, etc.) to DRUID entity fields.![](../Resources/Images/Read%20Excel%20File/Read%20Excel%20File_5.png)

> **Info:** Add as many integrations as needed based on what you want to do with the data from the file.

<a id="Publishtheintegration"></a>

### Publish the integration

Ensure you publish the integrations, or the AI Agent will not be able to read data from Excel files.

<a id="Step3Continuedefiningtheflow"></a>

## Step 3. Continue defining the flow

Finish defining the flow based on your needs. You might want to inform the user that the data has been updated or provide specific information.
