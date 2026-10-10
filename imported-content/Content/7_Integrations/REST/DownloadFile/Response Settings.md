---
layout:
  title:
    visible: false
---

<a id="ResponseSettings"></a>

# Response Settings

While the request is similar to the REST requests, the response of this connector task captures a file and maps it in a Druid entity field of type entity, which is referencing the [[File]] entity.

**Prerequisite**

- Your response entity has field of type entity referencing the [[File]] entity.

Click the **Response** tab and in the **ProjectResultToEntityPath** field, enter the name of the field of type entity referencing the [[File]] entity. This field will capture the file returned by the REST API endpoint.

Optionally, you can give the returned file a specific file name by filling in the **Filename** field.

Save the task. You can test the request (**Test** tab, **Test** button) and in case of any errors, you can further investigate and properly set the request and response.

Publish the integrations and you can use the integration task on flow steps. If you want to send the user the file returned by the REST API, on a step subsequent the one where you download the file, in the Metadata section, enter the entity field that stores the returned file.
