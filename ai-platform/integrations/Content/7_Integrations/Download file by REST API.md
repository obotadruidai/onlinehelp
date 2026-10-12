---
title: Download File by REST API
---


The Download File integration enables you to use a REST API call to download a file from a third-party tool and store it directly in a DRUID entity.

{% hint style="info" %}
**NOTE:** Downloading files by REST API allows you to manipulate only the file. If you get other file metadata from the third-party tools, you cannot map them in the response. To download a file and handle additional metadata, use REST integration and the `CREATEFILE(file)` DRUID-specific function.
{% endhint %}

To add this integration task:

1. Go to the desired integration.
2. Click the **Connector Steps** tab.
3. Click **Create Task**.
4. Select **Files** > **Download File**.

Setting up the request is similar to a REST request. For more information, see the [REST Request](<REST/Request Settings.md>) settings. The primary difference between the Download File by REST API and REST API is how you set up the response.

To set up the response:

1. Click the **Response** tab.
2. From the **Project Result to Entity Path** field, select the field of type Entity that references the \[\[File]] system entity.

![](<../../.gitbook/assets/download file.png>)

3. To provide a custom name for the downloaded file, in the **File name** field, either provide a static name (string) or use a value stored in an entity field or variable. If the File name field is empty, the connector will try to identify the file name from the Content-Disposition header or from the URL.
4. Save the integration task.
