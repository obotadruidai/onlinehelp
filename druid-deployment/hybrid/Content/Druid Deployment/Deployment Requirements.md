---
title: "Deployment Requirements"
---

<a id="DeploymentRequirements"></a>


This section provides you with the hardware and software prerequisites for deploying various Druid configurations. Simply click on the **+** sign next to your desired configuration to reveal its specific requirements.

<a id="RequirementsforinstallingtheDruidConnectorDataServiceKBAgentonpremises"></a>

## Requirements for installing the Druid Connector & Data Service & KB Agent on premises

In this configuration, you'll install the components and services as follows:

- Deploy Druid hybrid services (Druid Connector, Data Service, and KB Agent) on a single virtual machine.
- Install the storage systems (Mongo & ElasticSearch) on separate virtual machines, distinct from the one hosting the Druid services.
- Set up the Conversation History storage (SQL Server) on a separate machine.

<a id="DruidHybridservicesrequirements"></a>

### Druid Hybrid services requirements

The requirements apply to Druid Connector, Data Service, and KB Agent.

| Item | Development / Testing environment | Light Traffic PRODUCTION environment | Heavy Load PRODUCTION environments |
| --- | --- | --- | --- |
| CPU Count | 5vCORE | 5vCORE | 10vCORE |
| CPU type | Proc Intel i7 gen 8 min or equivalent Xeon | Proc Intel i7 gen 8 min or equivalent Xeon | Proc Intel i7 gen 8 min or equivalent Xeon |
| RAM | 16GB | 20GB | 24GB |
| Storage type | Min 1500 IOPS. | Min 1500 IOPS | Min 1500 IOPS |
| Storage size | 10GB | 30GB | 100GB |
| OS | Windows Server 2022 64-bit or higher, or Windows 11 64-bit | Windows Server 2022 64-bit or higher, or Windows 11 64-bit | Windows Server 2022 64-bit or higher, or Windows 11 64-bit |

<a id="MongoDBrequirements"></a>

### Mongo DB requirements

| Item | Testing environment | Production environment |
| --- | --- | --- |
| CPU Count | 2vCORE | 4vCORE |
| CPU type | Proc Intel i7 gen 8 min or equivalent Xeon | Proc Intel i7 gen 8 min or equivalent Xeon |
| RAM | 4 GB | 16 GB |
| Storage type | Min 500 IOPS | Min 500 IOPS |
| Storage size | Min 100 GB | Min 100 GB |
| MongoDB version | 8.3 or higher | 8.3 or higher |

<a id="ElasticSearchrequirements"></a>

### ElasticSearch requirements

| Item | Testing environment | Production environment |
| --- | --- | --- |
| CPU Count | 2vCORE | 8vCORE |
| CPU type | Proc Intel i7 gen 8 min or equivalent Xeon | Proc Intel i7 gen 8 min or equivalent Xeon |
| RAM | 8GB | 32GB |
| Storage type | Min 500 IOPS | Min 500 IOPS |
| Storage size | Min 128 GB | Min 128 GB |
| ElasticSearch version | 8.19.12 or higher | 8.19.12 or higher |

<a id="CHStorageSQLServerrequirements"></a>

### CH Storage (SQL Server) requirements

| Item | Development / Testing environment | PRODUCTION environment |
| --- | --- | --- |
| CPU Count | 2vCORE | 4vCORE |
| CPU type | Proc Intel i7 gen 8 min or equivalent Xeon | Proc Intel i7 gen 8 min or equivalent Xeon |
| RAM | 8GB | 16GB |
| Storage type | Min 500 IOPS. | Min 500 IOPS. |
| Storage size | Min 50GB | Min 100GB |
| SQL Server version | SQL Server Express Edition 2019 or later (up to 10GB) or Standard Edition 2019 or later\* | SQL Server Standard Edition 2019 or later |
| OS | Windows Server 2019+ | Windows Server 2019+ |

\*Based on the conversation history size

<a id="RequirementsforinstallingtheDruidConnectorDataServiceonpremises"></a>

## Requirements for installing the Druid Connector & Data Service on premises

In this configuration, you'll install the components and services as follows:

- Deploy Druid hybrid services (Druid Connector and Data Service) on a single virtual machine.
- Install the storage systems (Mongo) on a separate virtual machine, distinct from the one hosting the Druid services.
- Set up the Conversation History storage (SQL Server) on a separate machine.

<a id="DruidHybridservicesrequirements1"></a>

### Druid Hybrid services requirements

The requirements apply to Druid Connector and Data Service.

| Item | Development / Testing environment | Light Traffic PRODUCTION environment | Heavy Load PRODUCTION environments |
| --- | --- | --- | --- |
| CPU Count | 3vCORE | 3vCORE | 6vCORE |
| CPU type | Proc Intel i7 gen 8 min or equivalent Xeon | Proc Intel i7 gen 8 min or equivalent Xeon | Proc Intel i7 gen 8 min or equivalent Xeon |
| RAM | 12GB | 16GB | 20GB |
| Storage type | Min 1000 IOPS. | Min 1000 IOPS. | Min 1000 IOPS. |
| Storage size | 10GB | 30GB | 100GB |
| OS | Windows Server 2022 64-bit or higher, or Windows 11 64-bit | Windows Server 2022 64-bit or higher, or Windows 11 64-bit | Windows Server 2022 64-bit or higher, or Windows 11 64-bit |

<a id="MongoDBrequirements1"></a>

### MongoDB requirements

| Item | Testing environment | Production environment |
| --- | --- | --- |
| CPU Count | 2vCORE | 4vCORE |
| CPU type | Proc Intel i7 gen 8 min or equivalent Xeon | Proc Intel i7 gen 8 min or equivalent Xeon |
| RAM | 4 GB | 16 GB |
| Storage type | Min 500 IOPS | Min 500 IOPS |
| Storage size | Min 100 GB | Min 100 GB |
| MongoDB version | 8.3 or higher | 8.3 or higher |

<a id="ConversationHistoryStorageSQLServerrequirements"></a>

### Conversation History Storage (SQL Server) requirements

| Item | Development / Testing environment | PRODUCTION environment |
| --- | --- | --- |
| CPU Count | 2vCORE | 4vCORE |
| CPU type | Proc Intel i7 gen 8 min or equivalent Xeon | Proc Intel i7 gen 8 min or equivalent Xeon |
| RAM | 8GB | 16GB |
| Storage type | Min 500 IOPS. | Min 500 IOPS. |
| Storage size | Min 50GB | Min 100GB |
| SQL Server version | SQL Server Express Edition 2019 or later (up to 10GB) or Standard Edition 2019 or later\* | SQL Server Standard Edition 2019 or later |
| OS | Windows Server 2019+ | Windows Server 2019+ |

\*Based on the conversation history size

<a id="RequirementsforinstallingtheDruidConnectoronpremises"></a>

## Requirements for installing the Druid Connector on premises

In this configuration, you'll install the components and services as follows:

- Set up the Conversation History storage (SQL Server) on a separate virtual machine, distinct from the one hosting the Druid Connector.

<a id="DruidHybridservicesrequirements2"></a>

### Druid Hybrid services requirements

| Item | Development / Testing environment | Light Traffic PRODUCTION environment | Heavy Load PRODUCTION environments |
| --- | --- | --- | --- |
| CPU Count | 2vCORE | 2vCORE | 4vCORE |
| CPU Type | Proc Intel i7 gen 8 min or equivalent Xeon | Proc Intel i7 gen 8 min or equivalent Xeon | Proc Intel i7 gen 8 min or equivalent Xeon |
| RAM | 8GB | 8GB | 12GB |
| Storage type | Min 500 IOPS. | Min 500 IOPS. | Min 500 IOPS. |
| Storage size | 10GB | 30GB | 100GB |
| OS | Windows Server 2022 64-bit or higher, or Windows 11 64-bit | Windows Server 2022 64-bit or higher, or Windows 11 64-bit | Windows Server 2022 64-bit or higher, or Windows 11 64-bit |

<a id="ConversationHistoryStorageSQLServerrequirements1"></a>

### Conversation History Storage (SQL Server) requirements

| Item | Development / Testing environment | PRODUCTION environment |
| --- | --- | --- |
| CPU Count | 2vCORE | 4vCORE |
| CPU type | Proc Intel i7 gen 8 min or equivalent Xeon | Proc Intel i7 gen 8 min or equivalent Xeon |
| RAM | 8GB | 16GB |
| Storage type | Min 500 IOPS. | Min 500 IOPS. |
| Storage size | Min 50GB | Min 100GB |
| SQL Server version | SQL Server Express Edition 2019 or later (up to 10GB) or Standard Edition 2019 or later\* | SQL Server Standard Edition 2019 or later |
| OS | Windows Server 2019+ | Windows Server 2019+ |

\*Based on the conversation history size
