<a id="ResponseSettings"></a>

# Response Settings

Once you’ve set up the request settings, you need to set up the response as well. To do so, click the **Response** tab and make the necessary response settings as described in this section.

![](../../Resources/Images/SQL%20Connector/Response%20Settings.png)

| Setting | Description |
| --- | --- |
| <a id="kanchor4"></a>Iterate by <a id="kanchor5"></a>(JSON PATH Expression) | This is the JSON Path expression provided in the Request (if any). The field is automatically filled in, just for information purpose, because iteration will affect the response of the task, as well (if any). |
| Scope | Allows you to define the context for the integration task. **Global** means that the integration task output will be saved in the global context, that is, the Response entity set on the connector action.  If you want to save the response in an entity different from the global one set on the connector action, than from the **Scope** field, select **Local** and from the **Response entity** field, select the desired entity.  Using the Local scope, you do all related queries directly inside the connector action instead of building a larger context outside the connector action via additional queries within the Flow Designer to put data inside the request entity and then send the data back to the connector action.  **NOTE:** The **Scope** field is available in DRUID 5.26 and higher. |
| Response entity | The entity used by the AI Agent to receive data from the SQL DB and pass it into the conversation context. This field automatically fills in with the Response Entity set on the selected SQL Connector Action set. |
| Response entity is collection | This field is automatically ticked if the Response Entity set on the selected SQL Connector Action, is expected to be a list of records.  The response from the integration, in this case, will be saved in **[[<ResponseEntity>List]]** instead of [[<ResponseEntity>]] (E.g., [[HolidayList]]) |
| <a id="kanchor6"></a>Project Result To Entity Path | Use it when you want to map the response directly to an Entity List type field. E.g., directly to [[Employee]].Contracts, where Contracts is an EntityList field referred to [[Contract]]. |

<a id="Mappingresponsefields"></a>

## Mapping response fields

Add a new line in the mapping table. In the **Connector field name** column, write the name of the field from the SQL DB.

> **NOTE:**  You MUST name all the columns returned by the SQL statement in order for the connector to map their values. Use column name aliases, where needed.

For example, `select getdate()` will return a date value, without a column name – in this case, the Druid connector cannot map the date value. Use `select getdate() as CurrentDate` to map "CurrentDate" in **Connector field name**.

> **NOTE:** In DRUID 5.14 and higher, you can specify keys (**Connector field name**) in the following native scripts: Latin, Greek, Hebrew, Simplified Chinese, Traditional Chinese, Japanese, Hindi and Arabic.

From the **Connector field source type**, select the source type of the DB field:

- **Reader** – if you want to read the value of the field from the statement response.
- **OutParameter** – if you want to store the value of on output parameter from the SQL statement (e.g., stored procedures with output parameters):

```
(SELECT Id FROM User WHERE Email = :InitiatorEmail)

RETURNING Id INTO :IdEvent;

select IdEvent from dual; 
```

In the **DruidEntityFieldName** column, select the corresponding Druid entity field.

In order to properly fill in the **DruidEntityFieldName** field, type “[[“, in the “DruidEntityfieldName”, choose the Request entity from the drop-down, type “.” after the closing brackets ]] and choose the correct entity field from the new drop-down that appears.

Click the **Save** icon displayed inline. Click **Save** to save the settings and stay on page, or click **Save & Close** to save and exit the page.

Now the connector action is ready to be [Published](https://documentation.community.druidplatform.com/docs/Content/7_Integrations/Defining%20the%20Integration%20Actions.htm).

<a id="Consumevaluesfromanentitythatisglobalattheintegrationconnectoractionlevelwithinanintegrationtaskwithlocalscope"></a>

### Consume values from an entity that is global at the integration (connector action) level within an integration task with local scope

- There may be scenarios where the response entity is both local and global, and it possesses distinct memory slots. You have the capability to retrieve values from a globally scoped entity at the integration (connector action) level within an integration task that has local scope.
> **NOTE:** This feature is available in DRUID 5.31 and higher and requires DRUID Connector Host upgrade.

For instance, consider a campaign scenario where an integration task with local scope is employed to create a new campaign sharing the same category as the campaign from the global entity. In the add/create integration task, referencing the [[Campaign]] with local scope, you can assign a new name and date while maintaining the category from the global entity's Campaign. To achieve this, map the relevant DRUID entity fields on the Response, assuming they exist: [[Campaign]].Name, [[Campaign]].CreationOn, and [[Campaign]]\_Global.Category.
