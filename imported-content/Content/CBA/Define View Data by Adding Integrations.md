---
title: Define View Data by Adding Integrations
---

# Define View Data by Adding Integrations

After defining your view, the next step is to fetch the entity data that will populate the view. This is done by adding integrations with external data sources. By defining these integrations, you can ensure that the view is populated with the appropriate entity records, allowing you to display dynamic, real-time data from both DRUID Data Services and external sources.

{% hint style="info" %}
**NOTE:** To fetch the correct data, the entity you’re creating views for must be set as the Response Entity in the integration task, with the **Is Response Collection** option selected in the **Response** tab.
{% endhint %}

{% hint style="info" %}
**Info:** For quick integration with Druid Data Services, you can use the CRUD Template in the entity integrations. While you can add the CRUD Template multiple times, note that DRUID only duplicates the integration tasks. For more information, see CRUD Template.
{% endhint %}

To define the view data follow these steps:

1. At the top side of the View Diagram, click the **Add Integrations** icon (![](<../../.gitbook/assets/add integrations iscon.png>)). A pop-up will appear with two sections:

* **Read Data** – This section allows you to define the data source from which DRUID reads and aggregates information for the view.
* **Delete Data** – This section allows you to define what happens when records are deleted from the view.

![](<../../.gitbook/assets/add integrations.png>)

2. Click on **Read Data** to expand the section.
3. Define the data source from which DRUID reads the data:

* Add an existing integration action. Search for an existing integration action in the current solution and press **Enter**.

![](<../../.gitbook/assets/search integrations.png>)

* Add a new integration:

1. Click **Add New** and define the connector action using the editor. Ensure the current entity is set as the Response Entity and the options **Is Response Collection** and **Is Active** are selected.

![](<../../.gitbook/assets/define integration action.png>)

2. Save the integration action by clicking the **Save** icon (![](<../../.gitbook/assets/save view icon.png>)) at the top-right corner of the editor.

{% hint style="warning" %}
**IMPORTANT!** You can add only one connector action in the Read Data section and multiple integration tasks to aggregate data coming from various data sources.
{% endhint %}

3. Add integration tasks. Click on the **Add task** icon and select the desired integration task from the list where the current entity is Response entity and **Is Response Collection** is selected.

![](<../../.gitbook/assets/select integration task.png>)

![](<../../.gitbook/assets/read data.png>)

You must publish new integrations after adding them to apply the changes.

4. Select the integration from where you want to data. This functionality is similar to defining integrations on flows.
5. Click on **Delete Data** to expand the section.
6. Select the desired integration to define the behavior when records are deleted from the view.

![](<../../.gitbook/assets/delete data.png>)

{% hint style="info" %}
**NOTE:** If no integration is selected, the Delete icon will not be shown in the view, and users won’t be able to delete records.

<img src="../../.gitbook/assets/delete records.png" alt="" data-size="original">
{% endhint %}

Once you’ve set up the integrations, preview the view to check how the data is displayed and make any further adjustments as needed.

By following these steps, you will ensure that your view is populated with the correct data from both internal and external sources and that proper handling of data deletion is defined.

### Related Topics

* [Preview and Validate Views](<Preview and Validate Views.md>)
