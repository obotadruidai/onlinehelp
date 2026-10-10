---
title: "Export Solutions"
---

<a id="ExportSolutions"></a>


Before exporting a solution, you need to link all elements (integration entities, document templates, apps roles) that you need on destination (especially those which do not exist on destination, on the tenant or environment where you will import the solution); otherwise, the solution import will fail.

<a id="Linkentityentityfieldstothecurrentsolution"></a>

## Link entity / entity fields to the current solution

Linking entities / entity fields to the current solution is useful when you want to export a solution with views and forms defined for specific entities.

To link entities /entity fields, from the **Solution Contents** menu, click **Entities** and at the top-right corner of the Entities page, click ![](../Resources/Images/Working%20with%20solutions/linbk%20button.png). Click the link icon displayed in line with the entities you want to link and at the top of the page, click the **Confirm** button.

![](../Resources/Images/Working%20with%20solutions/link%20entities.png)

The Link entities and entity fields pop-up appears which lists the entities you selected and all the entities already linked to the current solution (if any).

You can link all entity fields or only specific fields that are used in web views, forms and charts. Click the drop-down displayed in front of the entity name and select all the entity fields or only the ones you want to link to the current solution, then click **Save**.

![](../Resources/Images/Working%20with%20solutions/link%20entities%20popup.png)

> **Info:** It might take up to a minute to link the entity fields to the current solution; therefore, you might want to wait until the process completes.

> **NOTE:** If you link entities that have views, forms and charts defined, then the workspaces using those entity elements are also linked to the current solution and will be included in the solution export package. If you want to exclude the workspaces, select **Select all without Views, Forms & Charts**.

<a id="Linkelementstothecurrentsolution"></a>

## Link elements to the current solution

To link elements to the current solution, from the main menu, click **References**, click the Link icon corresponding to the elements you want to link and click **Apply changes**.

![](../Resources/Images/Working%20with%20solutions/references.png)

The elements are linked to the current solution, that is the solution has all needed dependencies. You can now export the solution.

<a id="Exportasolution"></a>

## Export a solution

To export a solution, at the top-right corner of the solution configuration page, click the **Export solution** button.

![](../Resources/Images/Working%20with%20solutions/Exporting%20and%20Downloading.png)

You can include the following AI Agent-related settings in the solution export package, by selecting the **Include AI Agent settings** toggle:

- Enable Web Socket
- Block File Upload
- Is out of band upload
- Bot framework version
- Authentication expiration minutes
- Additional languages (including machine translation setup, but without credentials)
- Theme and webchat custom parameters
- NLU settings (without credentials to external NLU providers)
- Dialog management (special flows)
- Live Chat configurations (without Queues and Agents)
- Analytics
- Roles

> **IMPORTANT!** Including the AI Agent-related settings in the solution export package is fully secure as it does not contain any credentials. After the solution import on the destination AI Agent, you have to manually enter the credentials if specific AI Agent settings require credentials (e.g. machine translation).

> **NOTE:** Importing the solution package on the destination AI Agent will overwrite that AI Agent settings except for the AI Agent languages. The import will add new languages from solution to the destination AI Agent without removing the existing languages from the destination AI Agent.

If the export was successful, Druid generates a new archive (zip file) with the latest version of the elements included in the solution and it's downloaded on your computer in the default Download folder. The zip file contains json files with object metadata.

At the top of the configuration page, the status of the solution packaging operation appears. It's “Pending” while the solution is packed in a zip file and “Failed” if the operation failed. If status is “Pending”, click the **Refresh** button to refresh the status of the solution packaging operation.

<a id="Downloadasolution"></a>

## Download a solution

Downloading a solution is similar to exporting it but faster.

Click **Download solution** and wait for the download to finish.

You can restore the solution at a later moment or import it in another AI Agent or in a different tenant.
