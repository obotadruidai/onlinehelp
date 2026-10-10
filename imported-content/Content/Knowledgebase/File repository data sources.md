---
title: "File Repository Data Sources"
---

<a id="FileRepositoryDataSources"></a>


A File Repository data source empowers you to extract and index content directly from uploaded unstructured documents (such as Word, PDF, and TXT) and structured spreadsheets (Excel) to power AI Agent responses. It allows you to organize multiple documents into custom folder structures within the Knowledge Base.

<a id="AdddatafromfilestotheKnowledgeBase"></a>

## Add data from files to the Knowledge Base

To add content from files, you must configure a File Repository data source container, define the file repository structure, upload the files and extract the data.

<a id="Step1Createthedatasource"></a>

### Step 1. Create the data source

To begin, follow the step-by-step instructions in [Data Source Creation](Data%20Source%20Creation.md). In the Add New Data Source modal, make the following settings:

1. From the **Type** dropdown, select **File repository**.
2. Click the **Create** button.

<a id="Step2Definefolderstructureanduploadfiles"></a>

### Step 2. Define folder structure and upload files

The content of a File Repository is organized under a root folder named after your data source. You can upload files directly to the root directory or structure them into subfolders.

To add a folder, select the tree element under which the folder will be added and click the **New Folder** button. Alternatively, hover over the tree element, click the dots next to it and select **New Folder**. Enter the folder name in the modal and click **Save**.

![](../Resources/Images/KnowledgeBase_0.2/new%20folder.png)

To upload a file, click on the node where you want to upload it, and click Upload file(s).

![](../Resources/Images/KnowledgeBase_0.2/upload%20files.png)

Browse for the desired file(s), select it / them, and then click **Open**. You can upload multiple files at the same time.

> **Info:** When uploading files, you can manage duplicate filenames using options similar to Windows file handling: **Replace**, **Create Copy**, or **Skip**. These actions can be applied individually per file or globally (**Replace All**, **Create Copy for All)**. The Skip option is available starting with Druid version 9.31.

> **NOTE:** The maximum file upload size is limited to 20 MB. You can also upload video files as long as the file size is limited to 20 MB.

The selected file(s) appear in the tree under the selected folder.

![](../Resources/Images/KnowledgeBase_0.2/uploaded%20files.png)

<a id="Step3Includeorexcludefilesfromscrapingoptional"></a>

### Step 3. Include or exclude file(s) from scraping (optional)

If you want to extract data from specific nodes or exclude nodes from extraction, hover the mouse over the desired tree element (node/leaf), click the dots and select **Include** or **Exclude**. If you want to exclude specific leaves within a specific node, hover over it, click the dots and select **Exclude**.

<a id="Step4Extractthedata"></a>

### Step 4. Extract the data

You can extract paragraphs from the entire File repository (the data source root) or from specific nodes / leaves. Choose which nodes to include or exclude in the extraction.

To extract data from the root library, click the **Extract** button at the top left corner of the page.

![](../Resources/Images/KnowledgeBase_0.2/extract%20data.png)

You can extract data only from specific documents by using bulk actions.  For more information, see [Data Source Status and Bulk Actions](Data%20source%20status.md).

> **NOTE:** The extraction might take a few seconds, depending on the number of links included in the scrapping.

To extract data only from a specific node / leaf, click the dots next to the tree element and select **Extract**.

<a id="Step5Trainthedatasource"></a>

### Step 5. Train the data source

To ensure the KB Engine searches through the data source paragraphs, train your data source by clicking the **Train** button at the top-left corner of the data source or select **Train data source** from the actions menu. Alternatively, you can **Train all data sources**.

<a id="Replacefiles"></a>

## Replace files

You can perform a file replacement in the File Repository without losing any associated file metadata. Previously, updating a file required a manual delete and re-upload process, which erased all metadata and forced you to re-enter it.

When you replace a file, the system keeps all associated metadata (including KBWebsitePageId) and updates only the file content.

To replace a file:

1. In the tree explorer, locate the file you want to update.
2. Click the **More options** menu (three dots) next to the file.
3. Select **Replace file**.

![](../Resources/Images/KnowledgeBase_0.2/replace%20file.png)

4. Upload the new version of the file using the same file name.

The system replaces the existing file and preserves all associated metadata.

## Related Topics

- [Advanced Features and Optimization](Advanced%20Features%20and%20Optimization.md)
- [Data Management and Schedules](Data%20Management%20and%20Schedules.md)
