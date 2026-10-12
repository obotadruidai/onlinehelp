---
title: Loading UiPath Entity Schema and Mapping Fields
---


{% hint style="info" %}
**Info:** Druid shows by default the mapped fields only. To view the full UiPath entity schema, tap off **Show mapped fields only**, click **Actions** and select **Refresh UiPath Schema**.
{% endhint %}

From the **Actions** drop-down, click **Refresh UiPath Schema**.

![](<../../../.gitbook/assets/Loading UiPath Entity Schema.png>)

The UiPath entity schema is synced in Druid. You can now map the desired UiPath entity fields to Druid entity fields.

![](<../../../.gitbook/assets/Loading UiPath Entity Schema_1.png>)

To map a UiPath entity to a Druid entity, click the drop-down in the Druid column corresponding to the UiPath entity you want to map and select the desired Druid entity.

![](<../../../.gitbook/assets/Loading UiPath Entity Schema_2.png>)

Click the **Save** icon (![](<../../../.gitbook/assets/Loading UiPath Entity Schema_3.png>)) displayed inline.

![](<../../../.gitbook/assets/Loading UiPath Entity Schema_4.png>)

Click the **Expand** icon (![](<../../../.gitbook/assets/Loading UiPath Entity Schema_5_21x18.png>)) displayed in front of the UiPath entity. All UiPath entity fields are listed. You can map the desired fields to Druid fields by clicking in the Druid column and selecting the desired field, then clicking the **Save** icon (![](<../../../.gitbook/assets/Loading UiPath Entity Schema_3.png>)) displayed inline.

{% hint style="info" %}
**NOTE:** You can map UiPath fields to specific Druid fields based on their type. For more information, see [Fields Type Mapping](<Loading UiPath Entity Schema.md#Fields_Type_Mapping>).
{% endhint %}

![](<../../../.gitbook/assets/Loading UiPath Entity Schema_6.png>)

After you finish mapping the desired fields, at the bottom of the page, click the **Save** button.

![](<../../../.gitbook/assets/Loading UiPath Entity Schema_7.png>)

## Fields Type Mapping <a href="#fields_type_mapping" id="fields_type_mapping"></a>

The table below provides a reference on how you can map different field types.

| Druid field Type  | UiPath Data Service Field type |
| ----------------- | ------------------------------ |
| Boolean           | Yes/No                         |
| Currency          | -                              |
| Date              | Date                           |
| DateTime          | DateTime                       |
| Decimal           | Number                         |
| Email             | Text                           |
| Entity            | Relationship                   |
| Entity List       | Relationship                   |
| Guid              | UniqueId                       |
| Hashtag           | Text                           |
| Integer           | Number                         |
| InvariantDate     | Date                           |
| InvariantDateTime | DateTime                       |
| InvariantTime     | -                              |
| IPAddress         | Text                           |
| Long              | -                              |
| Percentage        | Number                         |
| String            | Text                           |
| Time              | -                              |
| Url               | Text                           |
| Entity            | ChoiceSet                      |
| Entity List       | MultiChoiceSet                 |
| \[\[File]]        | File                           |
