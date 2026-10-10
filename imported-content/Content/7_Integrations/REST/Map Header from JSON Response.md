---
layout:
  title:
    visible: false
---

<a id="MapHeaderFromJSONResponse"></a>

# Map Header From JSON Response

To extract values of keys from the HTTP response header, follow these steps:

1. From the **Response Body Content Type** field, select **JSON**.
2. In the mapping table, click the **Add** icon next to the mapping line.
3. In **Connector field name** enter the name of the response header key you want to map from the JSON response.
> **IMPORTANT!** If the response header key contains dashes (e.g., X-Correlation-ID), in the **Connector field name** field, type it exactly as it appears in the API response and make sure to include it between square brackets: [response\_header\_key\_name].

4. From the **Connector field type** field, select **Header**.
5. In the **Druid entity field name** field, type **[[**, select the entity, and then select the entity field where you want to store the property from the response.

![](../../Resources/Images/rest/rate%20limit.png)

![](../../Resources/Images/rest/map%20header%20key%20dash.png)

6. Click the **Save** icon next to the mapping line.
7. Save and publish the integration.
