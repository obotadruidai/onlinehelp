---
title: "Transferring Complex Data Type through the Start Attended Job Integration"
---

<a id="TransferringComplexDataTypethroughtheStartAttendedJobIntegration"></a>


**Required!** This feature is available for DRUID Connectors v1.54 or above. If you have a hybrid or on premise DRUID deployment, install DRUID Connector Host version 1.54 or above.

Via the Start Attended Job integration, DRUID offers authors the possibility to bidirectional transfer complex data type between DRUID and UiPath. This is very useful when you want to transfer DRUID data collections or conversational data stored in DRUID entities to UiPath attended processes. The integration provides a simplified way to map both DRUID flat data type and complex data such as data collections (Entity List) or unique set of data (Entity), in the Process arguments table both on the Request and Response.

<a id="MappingRequestArguments"></a>

## Mapping Request Arguments

This section provides you with information on how to map UiPath input arguments to DRUID entity fields.

To map UiPath arguments to DRUID Relational Entity Model, use the following reference table.

| DRUID entity field type | UiPath Process Argument type |
| --- | --- |
| EntityList | JArray |
|  | DataTable |
| Entity | JObject |
|  | Dictionary |

> **NOTE:** You need to create the DRUID Relational Entity Model before mapping the UiPath process arguments. The name of the DRUID entity fields in a collection must match the name of columns or properties from the UiPath DataTable, jArray, jObject or Dictionary arguments.

To better understand how to map complex data type, let’s consider the following example: we want to send DRUID flat and complex data type to a UiPath attended process. We have an entity called UiPathCollection with the following entity relational model:

![](../../Resources/Images/Transferring%20Complex%20Data%20Type%20through%20the%20Start%20Attended%20Job%20Integration/Transferring%20Complex%20Data_1.png)

A detailed view on the entities fields and field types:

![](../../Resources/Images/Transferring%20Complex%20Data%20Type%20through%20the%20Start%20Attended%20Job%20Integration/Transferring%20Complex%20Data_1_1.png)

Following the mapping reference table, this section provides mapping examples for sending complex DRUID data to a UiPath attended process.

DRUID Connector will send all data from [[UiPathCollection]] entity in the right format for each corresponding UiPath process argument.

Mapping examples

| UiPath Process Argument | Argument Type | DRUID entity name | DRUID Entity Type |
| --- | --- | --- | --- |
| in\_datatable  (DataTable) | input | [[UiPathCollection]].DataTable | EntityList |
| in\_jArray  (JArray) | input | [[UiPathCollection]].JArray | EntityList |
| in\_jObject  (JObject) | input | [[UiPathCollection]].Dictionary | Entity |
| in\_dictionary  (Dictionary<String, String>) | input | [[UiPathCollection]].Dictionary | Entity |
| Obiect  (JObject) | output | [[UiPathCollection]].Dictionary | Entity |
| dictionar  (Dictionary<String, String>) | output | [[UiPathCollection]].Dictionary | Entity |
| ColectieJarray  (JArray) | output | [[UiPathCollection]].JArray | EntityList |
| DataTabel  (DataTable) | output | [[UiPathCollection]].DataTable | EntityList |

![](../../Resources/Images/Transferring%20Complex%20Data%20Type%20through%20the%20Start%20Attended%20Job%20Integration/Transferring%20Complex%20Data_1_2.png)

<a id="SendingtheentirecontentofaDRUIDentity"></a>

## Sending the entire content of a DRUID entity

Additionally, if authors prefer to send the entire content of a DRUID entity, to / from a single UiPath argument, then that entity should simply be mapped without any fields.

> **NOTE:** When sending the entire content of a DRUID entity, you have to map it to an UiPath argument of type jObject.

![](../../Resources/Images/Transferring%20Complex%20Data%20Type%20through%20the%20Start%20Attended%20Job%20Integration/Transferring%20Complex%20Data_1_3.png)

<a id="UsingDRUIDComplexdatatypeinStudioProcess"></a>

## Using DRUID Complex data type in Studio Process

The UiPath process gets the data transferred from DRUID through input arguments, and uses those arguments as needed, within the process.

<a id="MappingResponseArguments"></a>

## Mapping Response Arguments

In a similar way, authors will map the process output arguments directly to corresponding entity / entity list fields, in the Response tab. The DRUID Platform will automatically map the response object to the response entity, by considering that all properties inside the response object have the same name as the DRUID response entity fields.

*DataTable Response Mapping Example*:

![](../../Resources/Images/Transferring%20Complex%20Data%20Type%20through%20the%20Start%20Attended%20Job%20Integration/Transferring%20Complex%20Data_1_4.png)

*JObject Response Mapping Example*:

![](../../Resources/Images/Transferring%20Complex%20Data%20Type%20through%20the%20Start%20Attended%20Job%20Integration/Transferring%20Complex%20Data_1_5.png)
