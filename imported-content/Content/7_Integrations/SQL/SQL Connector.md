---
title: "SQL Connector"
---

<a id="SQLConnector"></a>


The Druid AI Platform enables you to easily connect to any SQL database to store and retrieve data for different use cases.

You can integrate Druid with the following types of SQL databases: SQL Server, Oracle, MySQL and PostgreSQL.

![](../../Resources/Images/SQL%20Connector/SQL%20Connector.png)

Druid Integrations are called from the Flow Engine, which sends the conversation parameters as request parameters and receives back the integration results as response entity.

The entities transport data via integrations. Druid packages the data as request entity and send it to the systems integrated with the AI Agent. When receiving data from apps, the AI Agent maps the data within the conversation as response entity.

<a id="Prerequisites"></a>

## Prerequisites

- You have access to an SQL database, using SQL Server Authentication (user and password).
{% hint style="info" %}
**NOTE:**  “Windows Authentication” is available in DRUID version 5.11 and higher.
{% endhint %}

- Create the Druid entities that will store data from your SQL Database.

<a id="CreatingSQLConnectors"></a>

## Creating SQL Connectors

To create an SQL connector, follow these steps:

[Step 1 Create SQL App](Step%201%20Create%20SQL%20App.md)

[Step 2 Create Integration](Step%202%20Create%20Integration.md)

[Step 3 Add Integration Tasks](Step%203%20Add%20Integration%20Tasks.md)
