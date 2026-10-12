---
title: "Druid AI Platform Network Matrix"
---

<a id="DruidAIPlatformNetworkMatrix"></a>


The table outlines the communication channels and protocols used between various components of the Druid AI Platform. It details the source and destination machines, the protocols and ports used, and the purpose of each connection.

| Source | Destination | Protocol | Port (default) | Communication purpose |
| --- | --- | --- | --- | --- |
| KB Agent machine | <Druidservicegateway-URL> | https | 443 | Druid Embeddings Models training |
| KB Agent machine | Elasticsearch instance | https | 9200 | Trained Embeddings |
| KB Agent machine | MongoDB instance | https | 27017 | Extracted paragraphs storage |
| Dataservice machine | MongoDB instance | https | 27017 | Conversational context storage |
| Connector Host machine | <Druidplatform-URL> | https | 443 | DRUID Platform |
| Connector Host machine | <Service-BUS> | amqps | 5671 | Message broker |
| Connector Host machine | SQL Server instance | tcp | 1433 | Conversation History database |
| Connector Host machine | Dataservice machine | https | 5101 | Conversational context storage |
| Connector Host machine | KB Agent machine | https | 5110  5111 | KB related requests (web crawling, document extraction, embedding, train and predict) |

The table below provides the list of URLs per DRUID environment.

| Environment | <Druidservicegateway-URL> | <Druidplatform-URL> | <Service-BUS> |
| --- | --- | --- | --- |
| Community | [https://druidservicegateway.comm.eu.druidplatform.com](https://druidservicegateway.community.druidplatform.com) | community.druidplatform.com  \*.community.druidplatform.com  \*.comm.eu.druidplatform.com  \*.druidapcback.comm.eu.druidplatform.com | rabbitmq.comm.eu.druidplatform.com |
| Production West Europe | [https://druidservicegateway.eu.druidplatform.com](https://druidservicegateway.druidplatform.com) | druidplatform.com  \*.druidplatform.com  \*.eu.druidplatform.com  \*.druidapcback.eu.druidplatform.com | prod2-druid-bus.servicebus.windows.net  rabbitmq.eu.druidplatform.com |
| Production US | [https://druidservicegateway.us.druidplatform.com](https://druidservicegateway.us.druidplatform.com) | us.druidplatform.com  \*.us.druidplatform.com  \*.druidapcback.us.druidplatform.com | rabbitmq.us.druidplatform.com |
| Prod US - HIPAA compliant | [https://druidservicegateway.us.druidplatform-hs.com](https://druidservicegateway.us.druidplatform-hs.com/) | us.druidplatform-hs.com  \*.us.druidplatform-hs.com  \*.druidapcback.us.druidplatform-hs.com | rabbitmq.us.druidplatform-hs.com |
| Production Australia | [https://druidservicegateway.au.druidplatform.com](https://druidservicegateway.au.druidplatform.com) | au.druidplatform.com  \*.au.druidplatform.com  \*.druidapcback.au.druidplatform.com | rabbitmq.au.druidplatform.com |
