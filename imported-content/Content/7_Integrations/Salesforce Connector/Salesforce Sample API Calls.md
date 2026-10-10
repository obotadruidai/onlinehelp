---
title: Salesforce Sample API Calls
---

# Salesforce Sample API Calls

In DRUID, the Salesforce solution templates come by default with preconfigured integrations.

For example, solution Salesforce Lead Management comes with five predefined integrations.

![](<../../../.gitbook/assets/Salesforce Sample API Calls.png>)

### Sample Integration: create-lead

The figure below provides details of a sample integration action.

![](<../../../.gitbook/assets/Salesforce Sample API Calls_1.png>)

The integration has one REST integration task.

![](<../../../.gitbook/assets/Salesforce Sample API Calls_2.png>)

To see the API call (details, request and response), click the edit icon in line with the integration task.

#### General Information

In the **General** tab, you see that integration tasks is using the Salesforce app presented in a previous section.

![](<../../../.gitbook/assets/Salesforce Sample API Calls_3.png>)

#### Request

In the figure below you can see that the resource path to be called is comprised of the base URL set on the Salesforce connector app and the API method as described in Salesforce documentation.

The request type in this example is is Body Template (UseBodyTemplate option is selected as Request Type) and the body is a nested JSON.

![](<../../../.gitbook/assets/Salesforce Sample API Calls_4.png>)

Clicking the **Body** tab and you will see the mapping of the fields provided in the request (**BodyTemplate** field) to the DRUID fields, which will store the values returned by the API.

![](<../../../.gitbook/assets/Salesforce Sample API Calls_5.png>)

#### Response

Click the **Response** tab to see how the API call response is set. The Response entity is filled in automatically with the Response entity set on the integration action.

![](<../../../.gitbook/assets/Salesforce Sample API Calls_6.png>)
