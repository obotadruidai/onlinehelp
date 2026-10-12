---
title: Entity Data Integration (CRUD Template)
---


To seamlessly incorporate entity records from DRUID Data Services into conversational business applications, use the CRUD Template. This template simplifies the process of creating an entity web view of type "table" and a form with minimal configuration requirements:

* **Pre-configured Integrations**: The CRUD Template comes pre-configured with the mandatory integrations for DRUID Data Services.

![](../../.gitbook/assets/integrations.png)

* **Pre-configured Fields**: Additionally, the template includes the "Name" field by default.

![](<../../.gitbook/assets/name field.png>)

To add a web view and form that fetch entity data from DRUID Data Services, follow these steps:

1. Access the entity configuration page and navigate to the **Integrations** tab.
2. Click on the **Create task** button, then select **DRUID Data Services** > **CRUD Template**. This action automatically adds the necessary DRUID Data Services integrations required for web views and forms.

![](<../../.gitbook/assets/curs template integrations.png>)

3. Once the integration tasks are added, click the **Publish** button on the entity integrations page.

{% hint style="info" %}
**NOTE:** Failure to publish the entity integrations will prevent you from accessing the data.
{% endhint %}

{% hint style="info" %}
**Info:** You can add the CRUD Template multiple times, if needed. However, DRUID only duplicates the integration tasks. The web view and form will be created only during the initial addition of the CRUD Template integration, provided the entity has no existing web views or forms defined.
{% endhint %}

## Related Topics

* [Conversational AI Applications](<Conversational AI Applications.md>)
* [Druid Data Service Connector](https://druidai.gitbook.io/druid-ai-docs/integrations/enterprise-connectors/druid_data_-service_connector)
