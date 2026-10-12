---
title: Request Settings
---


Click the **Request** tab and set the request details.

| Setting                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| API Resource URL                  | The resource path to be called. It is comprised of a base URL (the URL of the REST App) and the API method. The base URL (not shown in the interface) is automatically included based on the settings in the Apps for the selected Connection Code. The base URL is set within the Apps settings and automatically used in all the integration calls. When you will move the settings to a different environment, you will need to change just once the base URL. Each third party API has specific method and resource URL for specific actions. In the Druid AI Platform, the REST endpoints include the HTTP verb (GET, POST, PUT, DELETE, HEAD, OPTIONS, PATCH, MERGE, COPY) to perform the task and the location (URL) from which the third-party API can access the resources they need to carry out their tasks. Select the HTTP verb and enter the endpoint. ![](<../../../../.gitbook/assets/Request Settings (1).png>) If the URL is dynamic, use parameters. Example: https://base-url/{OrderId}/payments. Map the parameter OrderId in the **Parameters** tab, with run time values from the chat conversation. If you want to get the value of a specific parameter dynamically from within the conversation, include the parameter in the endpoint (E.g., \&status={StatusName}) and make sure to map it in the Field Mappings > Parameters table. |
| Request entity                    | Read-only.DRUID uses it to pass input data to the REST call. This field is automatically fill-in with the request entity specified on the Connector Action set. You refer this entity in all the Fields mapping on the **Request** tab.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Iterate By (JSON PATH Expression) | Use it when you want to iterate the request for each element in the request entity. For example, you have all leave request for a certain employee stored in \[\[Employee]].LeaveRequests (“Entity List” type field), and you want to insert the leave request in 3rd party tool (one by one, not by using bulk insert). Using the JSON Path Expression $.\[\[Employee]].LeaveRequests\[\*] in this field will make the connector run the task for each element in the $.\[\[Employee]].LeaveRequests collection. You can check your JSON Path expression using the [JSON Path online evaluator](https://jsonpath.com/).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| RequestType                       | The type of request the integration call will make. For more information on the request types, see [Request Body Types](<Request Settings.md#Request_Body_Types>).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

Based on the selected Request Type and the parameters expected by the third-party API, you need to provide the parameters by using one of the following sections: Parameters, Headers or Body, and map the request parameters with the conversation context available in the Request Entity.

### Make request using Parameters

If your endpoint contains path parameters, represented through curly braces {param1}&{param2} use the **Parameters** tab to map parameters within the URL with values in the Request Entity.

### Make request using Headers

Use the Headers tab and table to add specific keys expected by the API in the Header section.

{% hint style="info" %}
**NOTE:** Usually the API headers contain authorization parameters. For security reasons, the DRUID platform provides you with a custom authentication method in Apps settings, which If done properly automatically adds the security context on the headers of all the integration calls, even if not visible in the Druid AI Platform. Username, passwords or keys defined in Apps settings are encrypted. So, there is no need for you to add the security context here.
{% endhint %}

### Make request using Body

Use the Body tab to map the fields you want to include within the body call.

If your request type is Body Template (**UseBodyTemplate** option selected as Request Type) and the body is a nested JSON, click the **Body** tab and map the fields provided in the request (**BodyTemplate** field) to the DRUID fields, which will store the values returned by the API.

## Request Body Types <a href="#request_body_types" id="request_body_types"></a>

DRUID version 1.59 and higher provides the Download File with full capabilities of a REST connector tasks covering as many use cases as possible.

![](<../../../../.gitbook/assets/Request Settings_2.png>)

{% hint style="info" %}
**NOTE:**

* For DRUID version 1.58 and below, only **UseFieldMapping** type is available.
* Both **UseFormData** and **Binary** are powerful request types for the Download File integration task, as they enable authors sending files to retrieve files.
{% endhint %}

## Set request using Field Mapping

Use Field Mapping when the REST API expects the parameters as a JSON-formatted in the request body.

The DRUID Connector automatically generates a JSON based on the structure defined in Field Mapping. By default, the Druid AI Platform generates a flat JSON object with the fields you define in the **Body** tab.

Nested JSON objects can be build using Child Mapping the option. If you have a more complex data structure to send within the body, you can use field mapping on level one and child mapping to indent fields and make a nested JSON objects data structure.

{% hint style="info" %}
**NOTE:**  Prior to using field mapping, make sure that you created the needed DRUID entities and fields. For more information about entities, see [Entities](https://druidai.gitbook.io/druid-ai-docs/build-ai-agents/authoring-tools/ai-agent-informational-model).
{% endhint %}

The Druid AI Platform enables you to do enhance fields mapping by using expressions. For information on how to use expressions in requests field mapping, see Using Expressions in Request mappings.

If you need a JSON with a complex structure, use **Body Template** instead.

## Set request using Body Template

Use **Body Template** when you want to send complex JSON structure to the external data source.

## Set request using Form Data

Use this type of request to send a file to the REST service. E.g., when sending the document for signature via the Namirial service.

**UseFormData** is especially useful when you need to send files on API calls of type multi part form data.

For more information on how to use it, see [Use Case for using Form Data Request Type](FormData_RequestType_Use_Case.md).

## Set request using Binary

Use **Binary** when you need to send the file in binary format.

## Set request using www Form Url Encoded

Use this type of request when the API requires url-encoded file in the request body.
