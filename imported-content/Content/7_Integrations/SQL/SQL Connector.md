---
title: SQL Connector
---

# SQL Connector

The Druid AI Platform enables you to easily connect to any SQL database to store and retrieve data for different use cases.

You can integrate Druid with the following types of SQL databases: SQL Server, Oracle, MySQL and PostgreSQL.

![](<../../../.gitbook/assets/SQL Connector.png>)

Druid Integrations are called from the Flow Engine, which sends the conversation parameters as request parameters and receives back the integration results as response entity.

The entities transport data via integrations. Druid packages the data as request entity and send it to the systems integrated with the AI Agent. When receiving data from apps, the AI Agent maps the data within the conversation as response entity.

### Prerequisites

* You have access to an SQL database, using SQL Server Authentication (user and password).

{% hint style="info" %}
**NOTE:** “Windows Authentication” is available in DRUID version 5.11 and higher.
{% endhint %}

* Create the Druid entities that will store data from your SQL Database.

### Creating SQL Connectors

To create an SQL connector, follow these steps:

[Step 1 Create SQL App](<Step 1 Create SQL App.md>)

[Step 2 Create Integration](<Step 2 Create Integration.md>)

[Step 3 Add Integration Tasks](<Step 3 Add Integration Tasks.md>)
