---
title: "Managing Entity Fields"
---

<a id="ManagingEntityFields"></a>


Entity fields play a crucial role in storing and managing data within your AI Agent. Druid offers a seamless process to add, edit, and delete entity fields, ensuring efficient management of your AI Agent informational model.

<a id="Viewentityfields"></a>

## View entity fields

To access and review the fields of an entity, simply click on the entity within the Entity Designer interface.

![](../Resources/Images/Entity%20Designer/entity%20fields.png)

![](../Resources/Images/Entities/Viewing%20Entity%20Fields.png)

<a id="Addfields"></a>

## Add fields

The process of adding fields remains consistent across all Entity Designer views:

- In list view, click the **Create New Entity Field** button at the top right corner of the Entity Fields page.
- In diagram or tree view, click on the entity, then access the **Fields** tab in the right-side editor and click the **Create New Entity Field** button.

![](../Resources/Images/Entities/add%20field%20in%20diagram%20view.png)

Fill in the required field properties.

| Property | Mandatory | Description |
| --- | --- | --- |
| Name | Yes | Enter a unique **Name** for the entity, ensuring adherence to naming conventions:   - Does not start with a number. - Does not contain spaces. - Is ASCII no diacritics. - Does not contain the following special characters: -, +, ., # and @.   **Info:** We recommend you to use PascalCaseNames (upper camel), no spaces. The Name starts with an uppercase, as do all additional words. E.g., AccountId. |
| Display Name | No | Allows you to localize entity records when using Druid Data Service in conversations. |
| Comment | No |  |
| Length | No | The field length if you want to restrict the user typing a specific number of characters. |
| Is Primary Key | No | Marks the field as the entity's primary key (the unique entity identifier) and Druid will use it to identify the entity records. |
| Is Nullable | No | Obsolete, it will be removed from the system in a future release. |
| Holds Sensitive Data | No | **NOTE:**  This field is available for AI Agents using bot framework version 4 (direct line only).  Tap on if you want to use this field in Input Mapping on prompt steps to capture user sensitive data / receive sensitive data from external systems and send it to third-party systems via connectors. The user data will be encrypted using a dRUID proprietary encryption method from the moment the user inputs data in the chat and remains encrypted while being transmitted to the connector. The connector will decrypt the data using a Druid proprietary decryption method and send the data to external systems.  Druid provides you with four options, which allow doing extensive configurations for sensitive data manipulation as best suits your needs. For more information, see [Manipulating Sensitive Data](../Governance%20%26%20Security/Extensive%20Sensitive%20Data%20Manipulation.md#Manipulate_Sensitive_Data).  **IMPORTANT!** You cannot enable this option if your entity **Holds multilanguage records**. |
| Holds multilanguage records | No | **NOTE:** This field is available for entity fields of type **String** (**Data Type** is "String").  When enabled, the Druid AI Platform automatically creates for all tenant agents languages associated field clones to store the language-specific values. The field clones have the following naming syntax <fieldname>\_<LanguageCode>  and are not visible in Entity Designer.  Druid uses the clone fields to match entities records aligned with the current chat user language.  **IMPORTANT!** You cannot enable this option if your entity field **Holds Sensitive Data**. |
| Data Type | Yes | Select the type of field you want to add. You might need to provide field properties specific to the selected field data type. |
| ReferencedEntity | Yes if the **Data Type** is either "Entity" or "Entity List". | Select the entity that is parent entity for the current entity. |

Save the field properties.

<a id="Editfields"></a>

## Edit fields

Editing entity fields allows you to modify their properties based on your evolving needs.

In diagram or tree view, select the desired node and click on the field within the Fields section to access the Entity Field Editor.

In list view, locate the field within the **Fields** tab and click the **Edit** icon in line with the field.

You can change the data type of existing entity fields, provided they refer to the same storage data type (email, URL, Hash, etc. which are all using the same string Storage data type). For example, changing the Email entity field from **Email** to **String**.

<a id="DisablingHoldsmultilanguagerecords"></a>

### Disabling Holds multilanguage records

You can disable the **Holds multilanguage records** option and choose to automatically delete the auto-generated field clones or manually handle deletion.

![](../Resources/Images/Entities/diable%20multilanguage.png)

Disabling the **Holds multilanguage records** option impacts the conversational flows if you're using clone fields in flow / flow step training phrases and integration tasks. In this case, we recommend you to manually handle deletion. Clicking **Handle Manually** will make the auto-generated language specific field(s) visible in Entity Designer and you can review the conversational flows and remove the field clones afterwords.

To automatically delete the field clones, click **Delete**. All auto-generated language specific field(s) will be deleted on entity field save.

For more information, see [Multilingual Entity Fields](Multilingual%20Entity%20Fields.md).

<a id="Deletefields"></a>

## Delete fields

> **IMPORTANT!** Carefully review your AI Agent informational model before deleting fields, as the action is irreversible. Fields that are included in web views and forms are protected from deletion. Attempting to delete entity fields that are used in web views and forms will result in an error message.
>
> ![](../Resources/Images/RELEASE%207.2/error%20field%20deletion.png)

To delete a field, click the **Delete** icon beside the field in list view. In diagram or tree view, the deletion occurs automatically.

In list view, a confirmation dialog appears upon attempting to delete a field. Confirm the action to proceed.

## Related Topics

- [Field Types](Field%20Types.md)
- [Managing Entities](Managing%20Entities.md)
- [Manipulate Data Without DRUID Entity Structures](../How%20to/Manipulate%20Data%20without%20Entity%20Structures.md)
- [Multilingual Entity Fields](Multilingual%20Entity%20Fields.md)
