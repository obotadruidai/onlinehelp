<a id="ManipulateDataWithoutDRUIDEntityStructures"></a>

# Manipulate Data Without DRUID Entity Structures

With the DRUID Data Service and REST connectors, you can effortlessly store JSON arrays and objects from third-party systems. There's no need for the request entity to precisely match the structure of the external data, eliminating the necessity for intricate mappings within the integration. This stored data becomes readily accessible within the conversation context and on web forms.

When configuring the request entity, ensure it includes fields of type JArray and/or JObject, depending on the data you intend to store. This simplifies the process by eliminating the need to align the AI Agent entity model with each JSON property, sparing you from creating multiple entities and fields to mirror the data structure.

Moreover, you have the flexibility to manipulate this data within integrations using Custom Code or incorporate it into flows (Set Variables or Code Extension) and forms using the Code Editor. This approach ensures swift access to the stored information.

> **NOTE:**  The JArray and JObject field types are supported in DRUID Data Service starting from version 7.6 and in the REST connector for DRUID versions 7.7 and above.

<a id="ExampleRESTIntegration"></a>

## Example: REST Integration

Suppose you have a REST integration that returns the following response from a third-party system, regarding an Account:

```
{
    "Age": 25,
    "Contracts": [
        {
            "ContractNumber": 1,
            "ContractTitle": "Cession"
        },
        {
            "ContractNumber": 2,
            "ContractTitle": "Loan"
        }
    ],
    "Name": "John Doe",
    "AccountDetails": {
        "Status": “active”,
        "AccountCurrency": “EUR”,
      “BankName”: “Bank Of America”
    }
}
```

In this example, the request entity [[Account]] includes two fields:

- [[Account]].Contracts of type JArray
- [[Account]].AccountDetails of type JObject

In the REST integration response, we will map the JArray and JObject fields.

![](../Resources/Images/druid%207.7/mapping%20jobjects.png)

We will further use the data in a flow step by employing Set variables advanced coding (using the Code Editor):

```
(
    function(){
        let myObject = [[Account]].AccountDetails;
        let b = myObject.Status;
        let c = myObject.BankName;
        let myContracts = [[Account]].Contracts;
        let x = myContracts.ContractTitle[0].ContractTitle;
        let y = myContracts.ContractTitle[0].ContractName;

    }
)()
```

![](../Resources/Images/druid%207.7/jobjects%20on%20set%20variable%20example.png)

## Related Topics

- [Druid Data Service Connector](../7_Integrations/Druid%20Data%20Service%20Connector/Druid_Data_%20Service_Connector.md)
- [Field Types](../5_Entities/Field%20Types.md)
- [REST Response General Settings](../7_Integrations/REST/Response%20Settings.md)
