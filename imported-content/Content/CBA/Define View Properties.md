<a id="DefineViewProperties"></a>

# Define View Properties

You can customize view properties to enhance usability, set default behaviors, and ensure proper record layout rendering for business users.

<a id="Accessviewproperties"></a>

## Access view properties

To access a view properties:

1. In the Druid Portal, go to **Solution Contents** > **Entities**.
2. Select the target entity, then click the **Views** tab.
3. Locate the view you want to configure and click the **Edit** icon to open the View Designer.
4. Configure the view properties. For more information, refer to the next section.

<a id="Viewpropertiesreference"></a>

## View properties reference

Configure the view parameters as described below:

| Property | Description | Mandatory |
| --- | --- | --- |
| Name | The unique, internal name of the view. | Yes |
| Display Name | The user-facing label shown in the Druid Portal. If working with multi-language applications, provide localized display names for each supported language. | No |
| Details | A brief description explaining the purpose of the view. | No |
| Enable data auto refresh | If your view retrieves data from external sources, enable data auto-refresh to update data in real time without manual intervention and select the desired refresh interval. | No |
| Row Height | Controls the spacing between rows. It does not change how much content a row can display. | No |
| Apply Dashboard Date Filter | Turn the toggle on to apply the global dashboard date range filters to this view when embedded in a dashboard. When enabled, select the date entity field (e.g., CreatedOn) to filter by. | No |
| Do not show in Workspace | Hides this view from appearing in the workspace navigation list. | No |
| Preferred Form | Select a specific form to open when users select records in this view.  **Info:** This property is available starting with Druid 9.28 | No |

Save the changes.
