---
title: Add Forms
---


Forms allow you to display and manipulate entity record data. Authors can create simple forms to show specific data or complex forms that enable business users to edit records, add details, attach files, and more.

The first form you create for an entity is automatically set as the default form. You can change the default form at any time. The default form will be used when creating or editing entity records.

{% hint style="info" %}
**Info:** To automatically generate a form that retrieves data from DRUID Data Services, use the CRUD Template. Applying the CRUD Template to entity integrations automatically creates a default view and form, preconfigured with the necessary integrations. For more details, see [CRUD Template](<Entity Data Integration.md>).
{% endhint %}

Follow these steps to create a form for an entity:

1. In the Solution drop-down, select the desired solution.
2. In the **Solution Contents** menu, click **Entities** to display the list of entities associated with the solution.

![](<../../.gitbook/assets/access entities list.png>)

3. Select the entity you want to add a form for. The Entity Configuration page opens on the **Details** tab.
4. Click the **Forms** tab. A list of forms for the entity appears. If no forms have been created, the page will be empty.

![](<../../.gitbook/assets/forms list.png>)

5. In the top-right corner, click the **Create new form** button. The Create New Form pop-up opens.
6. Enter a form name and description. The description helps you identify the form’s content.

![](<../../.gitbook/assets/add form.png>)

7. Click **Save**.

The first form added to an entity is set as the default. When you click a record in one of the entity’s views, DRUID displays the record details from the default form.

You can now define the form's properties, fields, and layout.
