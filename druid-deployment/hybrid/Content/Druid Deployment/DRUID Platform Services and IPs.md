---
title: Druid AI Platform Services and IPs
---


In the context of the Druid AI Platform (Cloud and Hybrid Druid deployments), egress and ingress refer to outgoing and incoming traffic respectively. For example, in the Community environment, if a component within the platform attempts to access an external service, the external service perceives the request as originating from the egress IP address.

Although we know the specific names of various Azure storage accounts, we prefer to use generic names since they might change in the future due to upgrades or other reasons.

{% hint style="info" %}
**NOTE:** For hybrid deployments, you should allow outbound calls to IP addresses specific per Cloud environment.
{% endhint %}

## Community environment

{% hint style="info" %}
**NOTE:** For community environments, using the Connector Host in Druid hybrid deployments is only permitted in special situations with Druid team approval. Please contact [DRUID Support](../Druid%20Deployment/mailto:support@druidai.com) for assistance.
{% endhint %}

| Service                        | Description                                                                                                                                   | IP             | Name                                                                                                                              | Port      |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------- |
| egress generic                 | Used by all Druid AI Platform applications, including but not limited to the DRUID Connector and DRUID KB Web Scraper.                        | 20.126.205.196 | -                                                                                                                                 | -         |
| Ingress https                  | Access to Druid AI Platform-related HTTP services.                                                                                            | 20.31.122.105  | community.druidplatform.com \*.community.druidplatform.com \*.comm.eu.druidplatform.com \*.druidapcback.comm.eu.druidplatform.com | 80 443    |
| rabbitmq ampqs                 | Access to RabbitMQ required by connectors installed on client premises.                                                                       | 20.93.245.250  | rabbitmq.comm.eu.druidplatform.com                                                                                                | 5671      |
| sb amqps                       | Access to RabbitMQ (legacy) required by connectors installed on client premises.                                                              | 23.97.226.21   | comm-eu-druid-bus.servicebus.windows.net                                                                                          | 5671      |
| various Azure Storage accounts | Used for various data transit purposes.                                                                                                       | -              | \*.blob.core.windows.net                                                                                                          | -         |
| kb agent                       | A KB Agent dependency that is required only for hybrid KB deployments. **NOTE:** Whitelisting the URL listed in the Name column is mandatory. | -              | https://playwright.azureedge.net                                                                                                  | 443       |
| Druid SIP Host                 | Access to Druid SIP Host voice services                                                                                                       | 20.56.251.87   |                                                                                                                                   | 5060 5061 |

## PROD AU environment

| Service                        | Description                                                                                                                                   | IP            | Name                                                                              | Port      |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | --------------------------------------------------------------------------------- | --------- |
| egress generic                 | Used by all Druid AI Platform applications, including but not limited to the DRUID Connector and DRUID KB Web Scraper.                        | 20.92.210.91  | -                                                                                 | -         |
| Ingress https                  | Access to Druid AI Platform-related HTTP services.                                                                                            | 20.92.213.40  | au.druidplatform.com \*.au.druidplatform.com \*.druidapcback.au.druidplatform.com | 80 443    |
| rabbitmq ampqs                 | Access to RabbitMQ required by connectors installed on client premises.                                                                       | 20.53.210.152 | rabbitmq.au.druidplatform.com                                                     | 5671      |
| various Azure Storage accounts | Used for various data transit purposes.                                                                                                       | -             | \*.blob.core.windows.net                                                          | -         |
| kb agent                       | A KB Agent dependency that is required only for hybrid KB deployments. **NOTE:** Whitelisting the URL listed in the Name column is mandatory. | -             | https://playwright.azureedge.net                                                  | 443       |
| Druid SIP Host                 | Access to Druid SIP Host voice services                                                                                                       | 4.147.95.8    |                                                                                   | 5060 5061 |

## PROD US environment

| Service                        | Description                                                                                                                                   | IP             | Name                                                                              | Port      |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- | -------------- | --------------------------------------------------------------------------------- | --------- |
| egress generic                 | Used by all Druid AI Platform applications, including but not limited to the DRUID Connector and DRUID KB Web Scraper.                        | 52.226.239.127 | -                                                                                 | -         |
| Ingress https                  | Access to Druid AI Platform-related HTTP services.                                                                                            | 20.83.136.183  | us.druidplatform.com \*.us.druidplatform.com \*.druidapcback.us.druidplatform.com | 80 443    |
| rabbitmq ampqs                 | Access to RabbitMQ required by connectors installed on client premises.                                                                       | 13.82.195.74   | rabbitmq.us.druidplatform.com                                                     | 5671      |
| various Azure Storage accounts | Used for various data transit purposes.                                                                                                       | -              | \*.blob.core.windows.net                                                          | -         |
| kb agent                       | A KB Agent dependency that is required only for hybrid KB deployments. **NOTE:** Whitelisting the URL listed in the Name column is mandatory. | -              | https://playwright.azureedge.net                                                  | 443       |
| Druid SIP Host                 | Access to Druid SIP Host voice services                                                                                                       | 20.83.136.183  |                                                                                   | 5060 5061 |

## Prod US - HIPAA compliant environment

| Service                      | Description                                                                                                                               | IP             | Name                                                                                       | Port      |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | -------------- | ------------------------------------------------------------------------------------------ | --------- |
| egress generic               | Used by all Druid AI Platform applications, including but not limited to the DRUID Connector and DRUID KB Web Scraper.                    | 172.175.39.9   | -                                                                                          | -         |
| ingress https                | Access to Druid AI Platform-related HTTP services.                                                                                        | 4.153.29.221   | us.druidplatform-hs.com \*.us.druidplatform-hs.com \*.druidapcback.us.druidplatform-hs.com | 443       |
| ingress service gateway grpc | Handles gRPC communication between external client services (e.g., mobile apps, frontend systems) and internal DRUID Platform components. | 20.161.173.244 | druidservicegateway.us.druidplatform-hs.com                                                | 443       |
| rabbitmq ampqs               | Access to RabbitMQ required by connectors installed on client premises.                                                                   | 4.152.165.186  | rabbitmq.us.druidplatform-hs.com                                                           | 5671      |
| Azure Storage account        | Used for various data transit purposes.                                                                                                   | 20.209.69.193  | produsdruidplatformoob.blob.core.windows.net                                               | 443       |
| Druid SIP Host               | Access to Druid SIP Host voice services                                                                                                   | 20.85.98.81    |                                                                                            | 5060 5061 |

## PROD EU environment

| Service                        | Description                                                                                                                                   | IP                                                 | Name                                                                                                | Port      |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------- |
| egress generic                 | Used by all Druid AI Platform applications, including but not limited to the DRUID Connector and DRUID KB Web Scraper.                        | 20.31.251.4 20.82.33.99                            | -                                                                                                   | -         |
| Ingress https                  | Access to Druid AI Platform-related HTTP services.                                                                                            | 20.82.36.44                                        | druidplatform.com \*.druidplatform.com \*.eu.druidplatform.com \*.druidapcback.eu.druidplatform.com | 80 443    |
| sb amqps                       | Access to RabbitMQ (legacy) required by connectors installed on client premises.                                                              | 52.236.186.66 13.69.106.64 13.69.64.64 20.86.92.11 | prod2-druid-bus.servicebus.windows.net                                                              | 5671      |
| various Azure Storage accounts | Used for various data transit purposes.                                                                                                       | -                                                  | \*.blob.core.windows.net                                                                            | -         |
| kb agent                       | A KB Agent dependency that is required only for hybrid KB deployments. **NOTE:** Whitelisting the URL listed in the Name column is mandatory. | -                                                  | https://playwright.azureedge.net                                                                    | 443       |
| Druid SIP Host                 | Access to Druid SIP Host voice services                                                                                                       | 20.50.55.224                                       |                                                                                                     | 5060 5061 |
