---
title: "Network Shared Drive Data Sources"
---

<a id="NetworkSharedDriveDataSources"></a>


A Network Shared Drive data source enables you to enrich your KB with internal documents, policies, or FAQs, improving the accuracy and comprehensiveness of your AI Agent responses. By incorporating Network Shared Drive data sources, you will extract paragraphs from Excel, Word, and PDF files stored on your network.

Druid supports adding and extracting data from the following storage types:

- **Local File**: Extract data from files located on the same machine as the KB Agent.
- **Local Share**: Access and process information from files stored on a shared drive within your network, accessible to the KB Agent.
- **FTP**: Integrate data from an FTP server using TLS implicit encryption (for cloud deployments only).
- **SFTP**: Integrate data from an SFTP server using TLS implicit encryption (for cloud deployments only).

{% hint style="info" %}
**NOTE:** While all storage options are available for Druid hybrid (KB Agent installed on premises) and full on-premise deployments, FTP and SFTP storage stand as the sole option available for KB in the cloud.
{% endhint %}

This section will guide you through the process of adding data from network shared drive to the KB:

<a id="Step1Createthedatasource"></a>

## Step 1: Create the data source

To begin, follow the step-by-step instructions in [Data Source Creation](Data%20Source%20Creation.md). In the Add New Data Source modal, follow these instructions to create a data source based on your storage type.

## FTP storage

1. From the **Type** dropdown, select **Shared drive**.
2. Select **FTP** as **Storage Type**.
3. In the **Uri** field, enter the relative path to the folder (on the FTP server) you want to crawl.
4. In the **Host** field, enter the host name of the FTP server.
5. Enter the FTP login ID (**User name**) and the FTP login password (**Password**).
6. Select the **Data connection type** from the dropdown.
7. If the FTP server uses a self-signed certificate or one not issued by a recognized Certificate Authority, select **Disable Certificate Validation**. Failure to do so will result in unsuccessful data crawling and extraction.
8. Enter the FTP **Port** for data transfers.
9. To verify the FTP credentials, click the **Test** button. If the check fails, check and review the FTP credentials to ensure they are correct. You can also verify the FTP credentials later by going to the Details tab of the data source and clicking the Test button at the bottom of the page.
10. Click **Create**.

## SFTP storage

{% hint style="info" %}
**NOTE:** Currently, connecting to the SFTP server is only supported via SFTP credentials (username and password). Public key authentication will be supported in a future release.
{% endhint %}

To create data sources from SFTP storage via TLS implicit encryption:

1. From the **Type** drop-down, select **Shared drive**.
2. Select **SFTP** as **Storage Type**.
3. In the **Uri** field, enter the relative path to the folder (on the SFTP server) you want to crawl.
4. In the **Host** field, enter the host name of the SFTP server.
5. Enter the SFTP login ID (**User name**) and the SFTP login password (**Password**).
6. Enter the SFTP **Port** for data transfers.

![](../Resources/Images/KB/ftp%20data%20source.png)

7. To verify the SFTP credentials, click the **Test** button. If the check fails, check and review the SFTP credentials to ensure they are correct. You can also verify the SFTP credentials later by going to the **Details** tab of the data source and clicking the **Test** button at the bottom of the page.
8. Click **Create**.

## Local file storage

To create data sources from the local machine where the KB Agent is installed:

1. From the **Type** drop-down, select **Shared drive**.
2. Select **Local File** as **Storage Type**.
3. In the **Uri** field, enter path to the local folder you want to crawl. To get the path, go to the desired folder and from Windows explorer, copy the folder path.
4. Click **Create**.

## Local share storage

To crawl and extract data from files stored on the shared drive within your network, accessible to the KB Agent:

1. From the **Type** drop-down, select **Shared drive**.
2. Select **Local Share** as **Storage Type**.
3. In the **Uri** field, enter the shared drive file path the KB Agent can access.
4. Click **Create**.

<a id="Step2Crawlthedatasource"></a>

## Step 2. Crawl the data source

The data source configuration page appears by default on the **Extracted paragraphs** tab. The content of the root reflects the file structure from the Uri link you provided during data source creation. By default, all folders and files are excluded from scraping. To include files / folders for scrapping, hover the mouse over the desired item in the tree, click the Actions menu (the three dots) and select **Include**.

Click the **Crawl** button at the top-right corner of the page. In the Start Crawling Parameters modal, define the crawling policy by setting the parameters described in the table below.

| Parameter | Description |
| --- | --- |
| URL | Automatically populated with the Uri (or the Host for FTP storage) you specified when adding the data source. |
| Depth | The number of directory levels the crawler will explore from the URL.  **NOTE:** To improve crawling efficiency, crawl each node individually instead of the entire root, especially if the storage has a deep structure. Set the depth to '0' to achieve this. |

Click **Start**.

{% hint style="info" %}
**Info:** Based on the crawling policy set, it might take up to a few minutes for the crawling to complete. You might want to refresh from time to time to see when the action has completed.
{% endhint %}

To crawl specific nodes, click the dots next to the desired node in the file repository explorer and select **Crawl Path**.

When the crawling completes, the extracted articles display under the **Extracted paragraphs** tab.

<a id="Step3Trainthedatasource"></a>

## Step 3. Train the data source

To ensure the KB Engine searches through the data source paragraphs, train your data source by clicking the **Train** button at the top-left corner of the data source or select **Train data source** from the actions menu. Alternatively, you can **Train all data sources**.

## Related Topics

- [Advanced Features and Optimization](Advanced%20Features%20and%20Optimization.md)
- [Data Management and Schedules](Data%20Management%20and%20Schedules.md)
