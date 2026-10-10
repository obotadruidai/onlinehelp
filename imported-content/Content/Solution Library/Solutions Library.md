---
title: Solutions Library
---

# Solutions Library

Druid offers a library of business applications and solution templates that help you cut the AI Agent authoring time by providing you with the basic elements. Use the solution templates as starting points and customize them to accommodate your specific needs.

Druid Solutions Library offers a wide range of solution templates and business applications.

### AI Agent Authoring Lifecycle

{% hint style="warning" %}
**IMPORTANT!** Druid solution templates are not end-to-end production ready solutions; therefore, do not install them directly in your production AI Agent, because it might overwrite your existing configurations.
{% endhint %}

AI Agent authoring does not always go as simple as using predefined solutions directly in your production environment. You need to follow some intermediary steps which allow you to build and optimize the solution to correspond to your specific requirements and then use it in production.

The diagram below provides you with an overview of the AI Agent authoring lifecycle.

![](<../../.gitbook/assets/Solution Templates.png>)

1. On the dev or sandbox environment where you have your AI Agent configured, install the desired solution template.
2. Configure the solution template to accommodate your specific needs, then export the solution.
3. On the Test environment, import solution from file, test it and make adjustments if necessary. Your solution is now ready for production.
4. Export the solution.
5. Import the solution on the production environment.

### Accessing the Solutions Library

To access the Solutions Library, in the Druid Portal, on the main menu, click the **Solutions** dropdown and select **Import solution**. The Solution Library page appears, which lists all Druid solution templates as cards.

Each card provides you with the following information:

* The name of the solution template.
* Solution template / business app badge. It shows the installation status on the selected AI Agent:
  * **New** – You did not install the solution template on the selected AI Agent.
  * **Upgrade** – You installed the solution template and a new version is available for upgrade.
  * **Installed** – You installed the latest version of the solution template.
* The category the solution template is part of.
* A brief description of solution template.
* The publisher. Currently, only Druid can publish solution templates in the Solutions Library. In a future release, Druid technology partners will be able to publish solution templates as well.
* The version.

![](<../../.gitbook/assets/Solution Templates_2.png>)

The Solutions Library provides you with extensive filtering:

* Filter by name. Search solution template / business app by name.
* Filter alphabetically (A-Z or Z-A) or by status (newest / installed).
* Search templates / apps by publisher.
