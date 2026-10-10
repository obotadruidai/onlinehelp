---
title: Set up the solution
---

# Set up the solution

For solution admins

This section explains how to install and configure the PeopleSoft Integrations skill so it can securely connect to Oracle PeopleSoft Campus Solutions and retrieve student information during automations.

### Prerequisites

Before installing the solution, verify that the following requirements are met:

* Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
* Access to an Oracle PeopleSoft Campus Solutions environment, with the REST endpoints for student data exposed and reachable from Druid.
* The username and password of a PeopleSoft integration user, used for Basic authentication on the REST calls, with read permissions on student records.
* The [Academic Advisor Agent](<../Academic Advisor Agent.md>) is installed and configured in your tenant.
* Student records have already been created in the Data Service, each with the Student ID field populated. The automations cannot run without it.

### Installation and setup procedure

Complete the following steps to install the solution and configure the connection to Oracle PeopleSoft Campus Solutions:

#### Step 1. Install the solution from the Solutions Library

1. Go to the **Solutions Library**.
2. Search for **PeopleSoft Integrations**.
3. Click **Import** and wait until the import status shows Success.

#### Step 2. Configure the app connections

Go to solution Apps and configure the PeopleSoft REST connections with your credentials:

1. Enable **Basic Rest Security**.
2. Configure the **User name** and **Password** using the credentials of the PeopleSoft integration account.

![](<../../../../../.gitbook/assets/Set up the solution.png>)

3. Save the app, then click **Publish**.
