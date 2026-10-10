---
title: Define Form Data by Adding Integrations
---

# Define Form Data by Adding Integrations

Integrations allow your form to display data from DRUID Data Services and external sources, ensuring users see accurate and up-to-date information. By configuring integrations, you can create, read, update, and delete entity records within the form.

{% hint style="info" %}
**NOTE:** Before defining form data, the entity you’re creating forms for must be set as the Response Entity in the integration task, with the **Is Response Collection** option selected in the **Response** tab.
{% endhint %}

{% hint style="info" %}
**Info:** For quick integration with Druid Data Services, you can use the CRUD Template in the entity integrations. While you can add the CRUD Template multiple times, note that DRUID only duplicates the integration tasks. For more information, see CRUD Template.
{% endhint %}

To fetch and display entity data in a form, follow these steps:

1. At the top side of the Form Diagram, click the **Add Integrations** icon (![](<../../.gitbook/assets/add integrations iscon.png>)). A pop-up appears with four integration sections:

* **Create Data** – Creates new entity records.
* **Read Data** – Displays data for a specific record ID.
* **Update Data** – Updates entity record data.
* **Delete Data** – Defines actions for record deletion.

{% hint style="info" %}
**NOTE:** If you don’t add an integration for a section, users won’t be able to perform that action on entity records.
{% endhint %}

2. Add an integration action to the relevant section:

* Add an existing integration action. Search for an existing integration action in the current solution and press **Enter**.

![](<../../.gitbook/assets/save form integrations.png>)

* Add a new integration:

1. Click **Add New** and define the connector action using the editor. Ensure the current entity is set as the Response Entity and the options Is Response Collection and Is Active are selected.

![](<../../.gitbook/assets/form integration action.png>)

2. Save the integration action by clicking the **Save** icon (![](<../../.gitbook/assets/save view icon.png>)) at the top-right corner of the editor.

{% hint style="warning" %}
**IMPORTANT!** You can add only one connector action per integration section but can include multiple integration tasks to aggregate data from various sources.
{% endhint %}

3. Add integration tasks. Click on the **Add task** icon and select the desired integration task from the list where the current entity is Response entity and **Is Response Collection** is selected.

![](<../../.gitbook/assets/form select task.png>)

You must publish new integrations after adding them to apply the changes.

After setting up integrations, preview the form and make any necessary adjustments.
