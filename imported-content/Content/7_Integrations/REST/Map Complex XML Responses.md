---
title: "Map Complex XML Responses"
---

<a id="MapComplexXMLResponses"></a>


If a GET request returns an XML response with a complex or unstructured format that prevents direct field mapping, consider the following approach:

1. From the **Response Body Content Type** field, select **XML**.
2. Store the entire XML response as a string in a DRUID entity field.

![](../../Resources/Images/rest/xml%20response.png)

> **Info:** The XML object will be stringified and saved in the specified DRUID field.

3. Save the REST integration.
4. Create a Custom Code integration after the REST integration to process the XML string.
5. Use the 'Map XML string to Entity Fields' template within the Custom Code integration to map the desired XML data to DRUID entity fields.

![](../../Resources/Images/druid%207.14/map%20xml%20string.png)

6. Save and publish the integration.
