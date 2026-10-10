---
layout:
  title:
    visible: false
---

<a id="MapStructuredJSONResponseBody"></a>

# Map Structured JSON Response Body

> **IMPORTANT!** The structure of entities that capture the JSON object response should reflect the structure of the JSON data object that you map on the response.

To map a simple and structured JSON response body, follow these steps:

1. From the **Response Body Content Type** field, select **JSON**.
2. In the mapping table, click the **Add** icon next to the mapping line.
3. In **Connector field name** enter the name of the property you want to map from the JSON response body.
> **Info:** You can also specify **Connector field name** in the following native scripts: Latin, Greek, Hebrew, Simplified Chinese, Traditional Chinese, Japanese, Hindi and Arabic.

> **NOTE:** The way you map the fields depends on the structure of the JSON response body. For more information, see the examples provided below.

4. Leave the **Connector field type** field empty.
5. In the **Druid entity field name**, type **[[**, select the entity, then select the entity field where you want to store the property from the response.
6. Click the **Save** icon next to the mapping line.
7. Save the integration.

<a id="Exampleusecases"></a>

## Example use cases

This section helps you understand how to map the response body based on the response entity, the complexity of the response body and the entity where you want to save the response body.

<a id="MapflatJSONobject"></a>

### Map flat JSON object

In this example, the response entity is [[Contract]] and the response body is a flat JSON object:

**JSON response body**

```
{
  "ContractNumber":"DRUID-1234",
  "ContractValue":150.00
}
```

Fields Mapping:

- Connector field name: ContractNumber → Druid entity field: [[Contract]].CNumber
- Connector field name: ContractValue → Druid entity field: [[Contract]].Value

![](../../Resources/Images/rest/FLAT%20JSON%20OBJECT.png)

<a id="MapnestedJSONobject"></a>

### Map nested JSON object

In this example, the response entity is [[Contract]] and the response body is a nested JSON object:

**Nested JSON object**

```
{
  "Contract": {
    "ContractNumber": "DRUID-1234",
    "ContractValue": 150.00
  }
}
```

Fields Mapping:

- Connector field name: Contract.ContractNumber → Druid field: [[Contract]].CNumber
- Connector field name: Contract.ContractValue → Druid field: [[Contract]].Value

Use the dot notation (Parent.Child) in the **Connector field name** to access nested values.

![](../../Resources/Images/rest/nestes%20json%20obkect.png)

<a id="MapacollectionofobjectstoanotherEntityscollection"></a>

### Map a collection of objects to another Entity’s collection

In this example, the response entity is [[Employee]] and you want to save the list of contracts to an Entity List field like [[Employee]].Contracts.

The response body is a collection:

**Response body is a collection**

```
[
  {
    "ContractNumber": "DRUID-1234",
    "ContractValue": 150.00
  },
  {
    "ContractNumber": "DRUID-1235",
    "ContractValue": 200.00
  },
  {
    "ContractNumber": "DRUID-1236",
    "ContractValue": 250.00
  }
]
```

Response settings:

- Make sure **Response Entity Is Collection** is disabled at integration level, since [[Employee]].Contracts is already an entity list.
- In the **Project Result to Entity Path** field, select [[Employee]].Contracts.

Fields Mapping

In the mapping table, map the fields of the list’s entity type ([[Contract]] in this case), not the root entity ([[Employee]]):

- Connector field name: ContractNumber → Druid entity field: [[Contract]].CNumber
- Connector field name: ContractValue → Druid entity field: [[Contract]].Value

![](../../Resources/Images/rest/project%20result%20mapping.png)

> **NOTE:** You can use JSONPath filter expressions in the **Connector field name** field to filter the items in the collection (e.g., use **$[?@.ContractValue >=200]** to store only the contracts with a value equal to or greater than 200.00).
>
> ![](../../Resources/Images/rest/jsonpath%20filter.png)

<a id="Mapacollectionofobjectsintherootentity"></a>

### Map a collection of objects in the root entity

In this example, the response entity is [[Contract]].

Response settings:

- Make sure **Response Entity Is Collection** is enabled at integration level.
- Leave the **Project Result to Entity Path** field, empty.

Fields Mapping

In the mapping table, map the fields of the root entity ([[Contract]]):

- Connector field name: ContractNumber → Druid entity field: [[Contract]].CNumber
- Connector field name: ContractValue → Druid entity field: [[Contract]].Value

![](../../Resources/Images/rest/CONTRACT%20COLLECTION.png)
