<a id="DRUID714"></a>

# DRUID 7.14

Deployment Dates

The table below lists the deployment date of DRUID v7.14 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| August 01, 2024 | August 29, 2024 | August 29, 2024 | August 29, 2024 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

**Recommended!** This release includes features that require upgrade of your DRUID Connector Host:

- Custom Code - new method and template for XML mapping.
- SOAP Connector - new field on the response

<a id="Improvements"></a>

## Improvements

- **Amazon Live Chat**. You can now send the conversation transcript along with Contact Center Parameters to Amazon Live Chat using the ConnectToHelpdeskAgent internal action.

**Example - Send Contact Center parameters**

```
{
     "SendConversationTranscript":true,
     "ContactCenterParameters":
        {
                "firstName":"[[Customer]].FirstName",
                "lastName":"@lastName",
                "question":"[[Customer]].Question",
                "queueId":"[[Entity]].QueueId",
                "contactId":"@contactId",
                "organizationId":""
        }
}
```

> **NOTE:** The payload must follow a key-value format where both the key and value are strings. When using values from DRUID conversation context (entities, local variables) as parameter values, ensure they are enclosed in double quotes ("") to maintain valid JSON formatting.

For more information, see [Amazon Live Chat](../../Live%20Chat/Amazon%20Live%20Chat.md).

- **Custom Code - new method and template for XML mapping**. We’ve introduced a new method, 'ParseXMLToEntityFields' and a new template, ‘Map XML string to Entity Fields’ designed to facilitate the mapping of XML strings to DRUID entity fields. This is particularly useful when REST API responses contain a complex or unstructured XML format that cannot be directly mapped to DRUID entities.

To leverage this feature:

1. Store the received XML as string in a DRUID entity field in the REST Response.

![](../../Resources/Images/druid%207.14/rest%20text.png)

2. Use Custom Code and the new template to map the desired XML data to DRUID entity fields.

![](../../Resources/Images/druid%207.14/map%20xml%20string.png)

- **Improved Trigger flow steps**: Trigger flow steps within parent flows can now programmatically initiate child intents, expanding flow capabilities beyond utterance-based triggers.

![](../../Resources/Images/druid%207.14/trigger%20flow.png)

- **Knowledge Base improvements**. This release introduces various improvements:

- **SharePoint Data Sources: prepopulated fields**. In this release, fields in the **Details** tab of SharePoint data sources are now prepopulated with the values entered during data source creation, streamlining data entry and improving consistency.

![](../../Resources/Images/druid%207.14/details%20sharepoint%20ds.png)

- **Knowledge Base Settings: Enhanced Author Experience**. This release introduces a revamped author experience for Knowledge Base (KB) settings, now organized into two distinct tabs: General Settings and Advanced Settings.

- **General Settings**: Configure essential aspects such as embedding providers, desired models, KB matching thresholds, and search balance to determine the percentage of algorithms used in KB searches. You can also enable KB usage and select specific flows.

![](../../Resources/Images/druid%207.14/general%20settings.png)

- **Advanced Settings**: Customize the KB Engine's behavior for experimental operations with new UI elements. Additionally, this tab includes the **Advanced Settings JSON** field, allowing for further customization and adding additional options.

![](../../Resources/Images/druid%207.14/advanced%20settings.png)

For more information, see [Knowledgebase](../../Knowledgebase/Knowledgebase.md).

- **Knoweledge base - Test area UI improvements**. When testing user queries against the Knowledge Base, the matched results will now display not only the total matching score but also the weight of each algorithm used in the selected score calculator strategy. Clicking the **Info** icon will show a graphical representation of these weights.

![](../../Resources/Images/druid%207.14/weights%20test%20area.png)

- **Data source creation**. Newly created data sources now automatically open upon creation, eliminating the need to manually select them from the KB page.

- **SOAP Connector - new field on the response**. We introduced a new field for handling SOAP envelope namespaces in responses. If the response uses a SOAP envelope namespace different from the default (http://schemas.xmlsoap.org/soap/envelope/), enter the namespace in the Envelope Namespace field (e.g., http://www.w3.org/2003/05/soap-envelope). After entering the namespace, map the response accordingly.

![](../../Resources/Images/druid%207.14/soap.png)

- **Integrations: Task names are now hyperlinks**. You can click on a task name to open the respective task in the same tab, similar to how you open flows or integrations by clicking their names.
- **Office 365 Email Channel**. Removed the 2,000-character limit for messages processed by the AI Agent app.
- **Natural Language Processing**: Added support for nl-BE (Flemish).
