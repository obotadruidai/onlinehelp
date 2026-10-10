---
title: SOAP Connector
---

# SOAP Connector

The Druid AI Platform enables you to easily connect to any enterprise application through any SOAP APIs.

![](<../../../.gitbook/assets/SOAP Connector.png>)

Druid Integrations are called from the Flow Engine which sends the conversation parameters as request parameters and receives back the integration results as response entity.

The entities transport data via integrations. The data is packed as request entity and send it to the systems integrated with the AI Agent. When receiving data from apps, the AI Agent maps the data within the conversation as response entity. For more information, see [Integrations](<../Enterprise Connectors.md>).

{% hint style="info" %}
**NOTE:** The calls to your on premise systems are possible in a secured way, without being required to have your APIs accessible from the Internet. For more information, see [Installing the Druid Connector Host](<../../Druid Deployment/Install Druid Connector Host.md>).
{% endhint %}

### Creating SOAP Connectors

To create an SQL connector, follow these steps:

[Step 1. Create SOAP app](<Step 1 Create SOAP App.md>)

[Step 2 Create integration action](<Step 2 Create Integration.md>)

[Step 3 Add integration tasks](<Step 3 Add Integration Tasks.md>)

[Step 4. Publish the integrations](<Step 4 Publish the integrations.md>).
