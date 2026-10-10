<a id="SalesforceSampleAPICalls"></a>

# Salesforce Sample API Calls

In DRUID, the Salesforce solution templates come by default with preconfigured integrations.

For example, solution Salesforce Lead Management comes with five predefined integrations.

![](../../Resources/Images/Salesforce%20Connector/Salesforce%20Sample%20API%20Calls.png)

<a id="SampleIntegrationcreatelead"></a>

## Sample Integration: create-lead

The figure below provides details of a sample integration action.

![](../../Resources/Images/Salesforce%20Connector/Salesforce%20Sample%20API%20Calls_1.png)

The integration has one REST integration task.

![](../../Resources/Images/Salesforce%20Connector/Salesforce%20Sample%20API%20Calls_2.png)

To see the API call (details, request and response), click the edit icon in line with the integration task.

<a id="GeneralInformation"></a>

### General Information

In the **General** tab, you see that integration tasks is using the Salesforce app presented in a previous section.

![](../../Resources/Images/Salesforce%20Connector/Salesforce%20Sample%20API%20Calls_3.png)

<a id="Request"></a>

### Request

In the figure below you can see that the resource path to be called is comprised of the base URL set on the Salesforce connector app and the API method as described in Salesforce documentation.

The request type in this example is is Body Template (UseBodyTemplate option is selected as Request Type) and the body is a nested JSON.

![](../../Resources/Images/Salesforce%20Connector/Salesforce%20Sample%20API%20Calls_4.png)

Clicking the **Body** tab and you will see the mapping of the fields provided in the request (**BodyTemplate** field) to the DRUID fields, which will store the values returned by the API.

![](../../Resources/Images/Salesforce%20Connector/Salesforce%20Sample%20API%20Calls_5.png)

<a id="Response"></a>

### Response

Click the **Response** tab to see how the API call response is set. The Response entity is filled in automatically with the Response entity set on the integration action.

![](../../Resources/Images/Salesforce%20Connector/Salesforce%20Sample%20API%20Calls_6.png)
