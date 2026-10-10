---
title: "Step 3. Add Integration Tasks"
---

<a id="Step3AddIntegrationTasks"></a>


<a id="Prerequisite"></a>

### Prerequisite

- Before adding integration tasks, make sure that you create an entity and add the request and response fields expected by the API call; otherwise, you won’t be able to properly set the integration task.

At the top-right corner of the Edit Connector Action page, **ConnectorSteps** tab, click on the **Create Task** button, click **Web** and then click **Soap**.

![](../../Resources/Images/SOAP%20Connector/Step%203%20Add%20Integration%20Tasks.png)

The Edit Connector Task page appears by default on the **General** tab.

<a id="Setthetaskgeneralparameters"></a>

## Set the task general parameters

Set the integration task general parameters:

| Parameter | Description |
| --- | --- |
| Description | Provide a brief relevant description of the task to be performed. |
| ConnectionCode | Select the SOAP app you created at Step 2.  **NOTE:**  Different SOAP Tasks in the same connector action (integration) can connect to different SOAP API servers, by choosing the corresponding SOAP Connector App (ConnectionCode) for each one. |

![](../../Resources/Images/SOAP%20Connector/Step%203%20Add%20Integration%20Tasks_1.png)

Click the **Save** button. Now you have to configure the request.

<a id="ConfiguretheRequest"></a>

## Configure the Request

Click the **Request** tab. Set the request general details provided in the table below.

| Setting | Description |
| --- | --- |
| URL | Enter your SOAP endpoint URL. |
| RequestDruidEntityName | **Read-only**. It is used to pass input data to the SOAP call. This field is automatically fill-in with the request entity specified on the Connector Action set.  You refer this entity in all the Fields mapping on the **Request** tab. |
| Iterate By (JSON PATH Expression) | Use it when you want to iterate the request for each element in the request entity.  For example, you have all leave request for a certain employee stored in [[Employee]].LeaveRequests (“Entity List” type field), and you want to insert the leave request in 3rd party tool (one by one, not by using bulk insert). Using the JSON Path Expression $.[[Employee]].LeaveRequests[\*] in this field will make the connector run the task for each element in the $.[[Employee]].LeaveRequests collection.  You can check your JSON Path expression using the [JSON Path online evaluator](https://jsonpath.com/). |

<a id="Addbodydata"></a>

### Add body data

The body element and its associated child elements are used to exchange information between Druid and the SOAP app.

The required SOAP Body element contains the actual SOAP message intended for the ultimate endpoint of the message.

Click the **Body** tab.

| Setting | Description |
| --- | --- |
| Message name | The name of the SOAP message.  A SOAP message is an ordinary XML document containing the following elements:   - An Envelope element that identifies the XML document as a SOAP message - A Header element that contains header information (optional) - A Body element that contains call and response information. |
| Namespace name | The namespace name identifying the namespace. It is a unique identifier for the XML elements and attributes of the SOAP envelope and is identified as an URI.  The namespace defines the Envelope as a SOAP Envelope.  **Request Example**:   ```  <soap:Envelope   xmlns:soap="http://www.w3.org/2001/12/soap-envelope"   soap:encodingStyle="http://www.w3.org/2001/12/soap-encoding">   ...   Message information goes here   ... </soap:Envelope> ```   In the example above the SOAP message elements are declared in the default namespace for the SOAP envelope: [http://www.w3.org/2001/12/soap-envelope](http://www.w3.org/2001/12/soap-envelope) and the default namespace for SOAP encoding and data types is: [http://www.w3.org/2001/12/soap-encoding](http://www.w3.org/2001/12/soap-encoding). |
| Xml schema form | Indicates if attributes or elements need to be qualified with a namespace prefix:   - **None** - Element and attribute form is not specified in the schema. - **Qualified** - Elements and attributes must be qualified with a namespace prefix. - **Unqualified** - Elements and attributes are not required to be qualified with a namespace prefix.   This value is the global default for all elements declared in the target namespace. The default is None. |
| SOAP action | The name of the SOAP method (operation). |
| SOAP version | Select the SOAP standard version: SOAP 1.1 or 1.2. |

If you have a more complex data structure to send within the body, you can use field mapping on level one and child mapping to subsequent child fields (nodes).

Use the mapping table to map the fields you want to include within the body call. Map the fields provided in the request to the Druid fields which will store the values returned by the API.

To map child fields, click the **Add Child Mapping** button (![](../../Resources/Images/SOAP%20Connector/Step%203%20Add%20Integration%20Tasks_2.png)). A new tab appears in the Request.

![](../../Resources/Images/SOAP%20Connector/Step%203%20Add%20Integration%20Tasks_3.png)

As child fields are xml elements within the SOAP body, you need to provide specific SOAP body elements when doing the mapping.

<a id="ConfiguretheResponse"></a>

## Configure the Response

Click the **Response** tab. Map the response fields of the API call to Druid response entity fields.

> **NOTE:** You can specify keys (**Connector field name**) in the following native scripts: Latin, Greek, Hebrew, Simplified Chinese, Traditional Chinese, Japanese, Hindi and Arabic.

Save the integration task. Now [publish the integration](Step%204%20Publish%20the%20integrations.md) and then you can use it on flow steps.

If the response uses a SOAP envelope namespace other than the default (http://schemas.xmlsoap.org/soap/envelope/), enter the appropriate namespace in the **Envelope Namespace** field (e.g., http://www.w3.org/2003/05/soap-envelope), then map the response.

> **NOTE:** The **Envelope Namespace** field is available in DRUID 7.14 and higher.

<a id="ExampleGetthecurrencyISOcodeandnameforacountry"></a>

## Example: Get the currency ISO code and name for a country

To better understand how to set up SOAP integration tasks, let’s take the following public SOAP API from Postman.

![](../../Resources/Images/SOAP%20Connector/Step%203%20Add%20Integration%20Tasks_4.png)

In this example:

- We created a connector app called: “SOAP”.
- We created a connector action called “GetCurrency” which has [[CountrySOAP]] as request and response entity.
- We have an integration task called “GetCurrency”.
- We created the Druid entity [[CountrySOAP]] which contains the following fields: [[CountrySOAP]].Code, [[CountrySOAP]].ISOCode and [[CountrySOAP]].Currency.

<a id="SettinguptheRequest"></a>

### Setting up the Request

![](../../Resources/Images/SOAP%20Connector/Step%203%20Add%20Integration%20Tasks_5.png)

<a id="SettinguptheResponse"></a>

### Setting up the Response

![](../../Resources/Images/SOAP%20Connector/Step%203%20Add%20Integration%20Tasks_6.png)
