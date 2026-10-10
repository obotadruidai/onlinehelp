---
layout:
  title:
    visible: false
---

<a id="ActiveDirectoryConnector"></a>

# Active Directory Connector

The Druid AI Platform enables you to connect to Active Directory to search, add to group and unlock users from Active Directory (AD).

Druid integrations are called from the Flow Engine, which sends the conversation parameters as request parameters and receives back the integration results as response entity.

The entities transport data via integrations. Druid packages the data as request entity and sends it to the systems integrated with the AI Agent. When receiving data from apps, the AI Agent maps the data within the conversation as response entity.

![](../../Resources/Images/AD%20integration/AD%20connector.png)

<a id="UseCasesforADIntegration"></a>

## Use Cases for AD Integration

- You need to validate that a user is member of a certain AD group before providing the user specific data through chat.
- You can develop a service desk AI Agent for employees who block their AD accounts, and unlock them only after they validate a certain quiz.

<a id="Prerequisites"></a>

## Prerequisites

- You have a domain admin account in AD with permission to run the Active Directory lookup.
- Create the Druid entities that will store data from your AD Database.
