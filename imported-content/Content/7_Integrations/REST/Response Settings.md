---
title: "Response General Settings"
---

<a id="ResponseGeneralSettings"></a>


Once you’ve set up the request settings, you need to set up the response as well. To do so, click the **Response** tab and make the necessary response settings as described in this section.

| Setting | Description |
| --- | --- |
| Scope | Allows you to define the context for the integration task. **Global** means that the integration task output will be saved in the global context, that is, the Response entity set on the connector action.  If you want to save the response in an entity different from the global one set on the connector action, than from the **Scope** field, select **Local** and from the **Response entity** field, select the desired entity.  Using the Local scope, you can do all related queries directly inside the connector action instead of building a larger context outside the connector action via additional queries within the Flow Designer to put data inside the request entity and then send the data back to the connector action. |
| Response entity | The entity the AI Agent will use to receive data from the external app and pass it into the conversation context. This field is automatically filled in with the Response Entity set on the selected REST Connector Action if the **Scope** is Global. |
| Response entity is collection | This option is automatically selected if the response entity, as defined in the selected REST Connector Action, is expected to return a list of records.  The response entity, in this case, will be [[MyResponseEntityList]], instead of [[MyResponseEntity]] (a List-type entity is created, where [[MyResponseEntityList]][i] == [[MyResponseEntity]]). |
| <a id="kanchor8"></a>Iterate by <a id="kanchor9"></a>(JSON PATH Expression) | This is the JSON Path expression provided in the Request (if any). The field is automatically filled in, just for information purpose, because iteration will affect the response of the task, as well (if any). |
| <a id="kanchor10"></a>Select token query | The query that filters the response before fields mapping is executed, that is, before the response is mapped with DRUID fields. Provide the query in JSON Path format. See [https://jsonpath.com/](https://jsonpath.com/) and [https://www.rfc-editor.org/rfc/rfc9535.html](https://www.rfc-editor.org/rfc/rfc9535.html). |
| Response Body Content Type | The format of the data returned in the response body of a REST API call. It determines how the data is structured and interpreted. You can select from various content types such as JSON, XML, or Text, depending on the API's response format. Choosing the correct content type ensures proper handling and parsing of the response data during integration.  **NOTE:** This field is available starting from DRUID version 7.16. In earlier versions, you specify the response types (Connector Field Type) within the mapping table. |
| Map Entire JSON Payload | **NOTE:** This feature is available in DRUID 8.2 and higher.  If the response body’s content type is **JSON**, you can map the entire JSON payload to a field of type jObject or jArray. To do this, enable **Map Entire JSON Payload** and from the **JSON Field**, select the DRUID jObject or jArray field that will store the JSON payload.  ![](../../Resources/Images/rest/json%20mapping.png) |
| <a id="kanchor11"></a>Project Result To Entity Path | Use this field to map the API response directly to an Entity List–type field.  For example, if the response includes a list of contracts for a specific employee, and the response entity is Employee, you can select [[Employee]].Contracts as the Project Result to Entity Path. This maps the contracts from the API response directly to the [[Employee]].Contracts field, which is an Entity List of [[Contract]].  Once you select an Entity List field, the mapping table will reference the fields of the list’s entity type ([[Contract]] in this case), not the root entity (Employee). It behaves as if [[Contract]] were the actual response entity.  **IMPORTANT!** The **Response entity is collection** option must be disabled when using this field. This option applies only to the root entity ([[Employee]] in the example), and not to fields like [[Employee]].Contracts, which are already defined as collections.    ![](../../Resources/Images/rest/project%20result%20to%20entity%20path.png) |
| Use Custom Code Mapping | Enables custom JavaScript execution directly within the REST response settings. Enable this option when you need to parse, filter, or map dynamic or complex API responses. The raw API response payload is available as a stringified JSON object in **RestContext.ResponseContent**.  For more information, see [Map REST Response using Custom Code](<https://docs.druidai.com/docs/Content/7_Integrations/REST/Map%20REST%20Response%20using%20Custom%20Code.htm>). |

The way you map response fields depends on the **Response Body Content Type** and the structure of the response. For detailed information, see the relevant Map Response topics.

## Related Topics

- [REST request settings](Request%20Settings.md)
- [Testing Settings](Testing%20Settings.md)
