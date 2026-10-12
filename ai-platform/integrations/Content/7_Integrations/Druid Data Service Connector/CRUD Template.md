---
title: CRUD Template
---


{% hint style="info" %}
**NOTE:** This feature is available in DRUID 5.24 and higher and is available only on entity integrations.
{% endhint %}

The CRUD Template enables you to easily create a web view and form that consume data from the DRUID Data Services. The view and form have minimum configuration:

* They come pre-configured with the required integrations (DRUID Data Services integrations).

![](../../../.gitbook/assets/integrations.png)

* They come pre-configured with the “Name” field.

![](<../../../.gitbook/assets/name field.png>)

To add a web view and form that consume entity data from the DRUID Data Services, access the entity configuration page and select the **Integrations** tab.

From there, click the **Create task** button and select **DRUID Data Services** > **CRUD Template**. This will add the DRUID Data Services integrations mandatory for web views and forms.

![](<../../../.gitbook/assets/curs template integrations.png>)

{% hint style="info" %}
**NOTE:** On the entity integrations page, click the **Publish** button to publish the entity integrations; otherwise, you will not be able to consume the data.
{% endhint %}

{% hint style="info" %}
**Info:** You can add the CRUD Template multiple times, but DRUID only duplicates the integration tasks. The web view and form will only be created the first time the CRUD Template integration is added if the entity has no web views or forms defined.
{% endhint %}
