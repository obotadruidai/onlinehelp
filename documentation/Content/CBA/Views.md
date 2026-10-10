<a id="Views"></a>

# Views

A view is a structured representation of entity data, similar to a database table. It displays specific records in a grid format, with dynamically generated rows and columns based on the view definition. Views retrieve and aggregate data from various sources through integrations.

AI Agents can provide business users with high-volume data by sharing links to specific views in chat. Users can click these links to access the data within a Workspace. To ensure seamless access, authors must define views for all links added to a workspace. Views can be created for Entity-type records (lists of records).

<a id="ViewTypes"></a>

## View Types

Views can be displayed in different formats based on business needs:

- **Table** – Displays data in a grid format with columns and rows.
- **Kanban** – Presents records as cards in a board layout for workflow visualization.
- **Calendar** – Shows records in a calendar format based on date fields.
- **Tree** – Display data in a hierarchical tree structure, typically reading from top to bottom

<a id="SpecialViewTypes"></a>

## Special View Types

Special views enhance how business users interact with data by providing search capabilities, displaying related records, and enabling drilldowns in charts.

Some views offer enhanced functionality:

- **Quick Search** – Allows authors to add a search bar to a view, enabling users to quickly find records within the view.
- **Sub Grid** –
  Displays a list of related records inside a form for fields of type Entity List. Use it to embed a related view inside a form to display associated records.
- **Lookup** – Provides a searchable list of related records inside a form for fields of type Entity.
- **Chart Drilldown** – Enables users to explore detailed data by clicking on chart elements.

**Quick Search** is available in table views, while **Chart Drilldown** is used in charts. **Sub Grid** and **Lookup** views are available only when authoring entity forms and cannot be used in Workspace views or the **Data** tab on entities.
