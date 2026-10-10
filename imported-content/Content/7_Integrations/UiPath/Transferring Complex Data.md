---
title: "Transferring Complex Data Type through the Start Unattended Job Integration"
---

<a id="microcontent1"></a>

<a id="TransferringComplexDataTypethroughtheStartUnattendedJobIntegration"></a>


**Required!** This feature is available for DRUID Connectors v1.47 or above. If you have a hybrid or on premise DRUID deployment, install DRUID Connector Host version 1.47 or above.

Via the Start Unattended Job integration, DRUID offers authors the possibility to bidirectional transfer complex data type between DRUID and UiPath. This is very useful when you want to transfer DRUID data collections or conversational data stored in DRUID entities to UiPath unattended processes. The integration provides a simplified way to map both DRUID flat data type and complex data such as data collections (Entity List) or unique set of data (Entity), in the Process arguments table both on the Request and Response.

<a id="MappingRequestArguments"></a>

## Mapping Request Arguments

This section provides you with information on how to map UiPath input arguments to DRUID entity fields.

<a id="microcontent2"></a>

To map UiPath arguments to DRUID Relational Entity Model, use the following reference table.

| DRUID entity field type | UiPath Process Argument type |
| --- | --- |
| EntityList | JArray |
|  | DataTable |
| Entity | JObject |
|  | Dictionary |

{% hint style="info" %}
**NOTE:** You need to create the DRUID Relational Entity Model before mapping the UiPath process arguments. The name of the DRUID entity fields in a collection must match the name of columns or properties from the UiPath DataTable, jArray, jObject or Dictionary arguments.
{% endhint %}

To better understand how to map complex data type, let’s consider the following example:

- We want to send DRUID flat and complex data type to a UiPath unattended process. We have an entity called [[HR\_Employee]] with the following entity relational model:

![](../../Resources/Images/Transferring%20Complex%20Data%20Type%20through%20the%20UiPath%20Integration/Transferring%20Complex%20Data.png)

A detailed view on the entities fields and field types:

![](../../Resources/Images/Transferring%20Complex%20Data%20Type%20through%20the%20UiPath%20Integration/Transferring%20Complex%20Data_1.png)

Following the mapping reference table, this section provides mapping examples for sending the list of holiday requests and the Identity Card information for a specific employee, to a UiPath process.

DRUID Connector will send all data from [[HR\_Employee]] entity in the right format for each corresponding UiPath process argument.

*DataTable and Dictionary mapping example*

![](../../Resources/Images/Transferring%20Complex%20Data%20Type%20through%20the%20UiPath%20Integration/Transferring%20Complex%20Data_2.png)

*Or alternatively, JArray and JObject Mapping example*

![](../../Resources/Images/Transferring%20Complex%20Data%20Type%20through%20the%20UiPath%20Integration/Transferring%20Complex%20Data_3.png)

<a id="PreviewingArguments"></a>

## Previewing Arguments

For DRUID fields of type Entity and Entity List, authors can see a preview of how the data structure should look like in UiPath Studio by clicking the desired **Preview** icon (![](../../Resources/Images/Transferring%20Complex%20Data%20Type%20through%20the%20UiPath%20Integration/Transferring%20Complex%20Data_4.png)) in the Process arguments table. For JObject, JArray and Dictionary arguments, the preview is in JSON format.

DataTable arguments preview.

The structure of DRUID [[Employee]] entity will be transferred to the UiPath input arguments, meaning that the fields of [[Employee]] entity will represent the header of the data table UiPath argument, respectively the keys of the dictionary argument.

![](../../Resources/Images/Transferring%20Complex%20Data%20Type%20through%20the%20UiPath%20Integration/Transferring%20Complex%20Data_5.png)

*JArray, JObject and Dictionary arguments preview*

![](../../Resources/Images/Transferring%20Complex%20Data%20Type%20through%20the%20UiPath%20Integration/Transferring%20Complex%20Data_6.png)

![](../../Resources/Images/Transferring%20Complex%20Data%20Type%20through%20the%20UiPath%20Integration/Transferring%20Complex%20Data_7.png)

![](../../Resources/Images/Transferring%20Complex%20Data%20Type%20through%20the%20UiPath%20Integration/Transferring%20Complex%20Data_8.png)

<a id="SendingtheentirecontentofaDRUIDentity"></a>

## Sending the entire content of a DRUID entity

Additionally, if authors prefer to send the entire content of a DRUID entity, to / from a single UiPath argument, then that entity should simply be mapped without any fields, just like in the image below.

{% hint style="info" %}
**NOTE:** When sending the entire content of a DRUID entity, you have to map it to an UiPath argument of type jObject.
{% endhint %}

![Graphical user interface, application Description automatically generated](../../Resources/Images/Transferring%20Complex%20Data%20Type%20through%20the%20UiPath%20Integration/Transferring%20Complex%20Data.jpg)

You can preview the expected structure of the jObject argument as below:

![Text Description automatically generated](../../Resources/Images/Transferring%20Complex%20Data%20Type%20through%20the%20UiPath%20Integration/Transferring%20Complex%20Data_1.jpg)

<a id="UsingDRUIDComplexdatatypeinStudioProcess"></a>

## Using DRUID Complex data type in Studio Process

The UiPath process gets the data transferred from DRUID through input arguments, and uses those arguments as needed, within the process.

In the example below, the UiPath process simply logs the input arguments sent by a AI Agent, using the Log Message activity, for demonstration purpose.

*Data collection example – with DataTable*

Studio Process

![](../../Resources/Images/Transferring%20Complex%20Data%20Type%20through%20the%20UiPath%20Integration/Transferring%20Complex%20Data_9.png)

Orchestrator Log

![](../../Resources/Images/Transferring%20Complex%20Data%20Type%20through%20the%20UiPath%20Integration/Transferring%20Complex%20Data_10.png)

*Data collection example – with JArray*

The UiPath process logs both flat data and transforms DRUID data collection to a string, logging it.

Studio Process

![](../../Resources/Images/Transferring%20Complex%20Data%20Type%20through%20the%20UiPath%20Integration/Transferring%20Complex%20Data_11.png)

Orchestrator Log

![](../../Resources/Images/Transferring%20Complex%20Data%20Type%20through%20the%20UiPath%20Integration/Transferring%20Complex%20Data_12.png)

<a id="MappingResponseArguments"></a>

## Mapping Response Arguments

In a similar way, authors will map the process output arguments directly to corresponding entity / entity list fields, in the **Response** tab. The DRUID Platform will automatically map the response object to the response entity, by considering that all properties inside the response object have the same name as the DRUID response entity fields.

## Related Topics

- [How to Set Up the UiPath Integration](How%20to%20set%20up%20the%20UiPath%20Integration.md)
- [Starting UiPath Unattended Processes](Starting%20UiPath%20Unattended.md)
