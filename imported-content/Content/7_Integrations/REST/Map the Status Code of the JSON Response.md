---
title: "Map the Status Code of the JSON Response"
---

<a id="MaptheStatusCodeoftheJSONResponse"></a>


To store the status code of the response, follow these steps:

1. From the **Response Body Content Type** field, select **JSON**.
2. In the mapping table, click the **Add** icon next to the mapping line.
3. From the **Connector field type** field, select **StatusCode**.
4. From the **Connector field name**, select **IntValue** if the expected status code is a number like 200 or **StringValue** if the expected status code is a string like "Success" or "OK".
5. In the **Druid entity field name** field, type **[[**, select the entity, and then select the entity field where you want to store the response status code.
   Make sure that the DRUID entity field type accommodates the expected status code type (that is, integer or string).

![](../../Resources/Images/rest/response%20status%20code.png)

![](../../Resources/Images/rest/map%20status%20code.png)

6. Click the **Save** icon next to the mapping line.
7. Save and publish the integration.
