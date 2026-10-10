---
layout:
  title:
    visible: false
---

<a id="LoadingUiPathEntitySchemaandMappingFields"></a>

# Loading UiPath Entity Schema and Mapping Fields

> **Info:**  Druid shows by default the mapped fields only. To view the full UiPath entity schema, tap off **Show mapped fields only**, click **Actions** and select **Refresh UiPath Schema**.

From the **Actions** drop-down, click **Refresh UiPath Schema**.

![](../../Resources/Images/UiPath%20Data%20Service%20Connector/Loading%20UiPath%20Entity%20Schema.png)

The UiPath entity schema is synced in Druid. You can now map the desired UiPath entity fields to Druid entity fields.

![](../../Resources/Images/UiPath%20Data%20Service%20Connector/Loading%20UiPath%20Entity%20Schema_1.png)

To map a UiPath entity to a Druid entity, click the drop-down in the Druid column corresponding to the UiPath entity you want to map and select the desired Druid entity.

![](../../Resources/Images/UiPath%20Data%20Service%20Connector/Loading%20UiPath%20Entity%20Schema_2.png)

Click the **Save** icon (![](../../Resources/Images/UiPath%20Data%20Service%20Connector/Loading%20UiPath%20Entity%20Schema_3.png)) displayed inline.

![](../../Resources/Images/UiPath%20Data%20Service%20Connector/Loading%20UiPath%20Entity%20Schema_4.png)

Click the **Expand** icon (![](../../Resources/Images/UiPath%20Data%20Service%20Connector/Loading%20UiPath%20Entity%20Schema_5_21x18.png)) displayed in front of the UiPath entity. All UiPath entity fields are listed. You can map the desired fields to Druid fields by clicking in the Druid column and selecting the desired field, then clicking the **Save** icon (![](../../Resources/Images/UiPath%20Data%20Service%20Connector/Loading%20UiPath%20Entity%20Schema_3.png)) displayed inline.

> **NOTE:** You can map UiPath fields to specific Druid fields based on their type. For more information, see [Fields Type Mapping](#Fields_Type_Mapping).

![](../../Resources/Images/UiPath%20Data%20Service%20Connector/Loading%20UiPath%20Entity%20Schema_6.png)

After you finish mapping the desired fields, at the bottom of the page, click the **Save** button.

![](../../Resources/Images/UiPath%20Data%20Service%20Connector/Loading%20UiPath%20Entity%20Schema_7.png)

<a id="FieldsTypeMapping"></a>

## <a id="Fields_Type_Mapping"></a>Fields Type Mapping

The table below provides a reference on how you can map different field types.

| Druid field Type | UiPath Data Service Field type |
| --- | --- |
| Boolean | Yes/No |
| Currency | - |
| Date | Date |
| DateTime | DateTime |
| Decimal | Number |
| Email | Text |
| Entity | Relationship |
| Entity List | Relationship |
| Guid | UniqueId |
| Hashtag | Text |
| Integer | Number |
| InvariantDate | Date |
| InvariantDateTime | DateTime |
| InvariantTime | - |
| IPAddress | Text |
| Long | - |
| Percentage | Number |
| String | Text |
| Time | - |
| Url | Text |
| Entity | ChoiceSet |
| Entity List | MultiChoiceSet |
| [[File]] | File |
