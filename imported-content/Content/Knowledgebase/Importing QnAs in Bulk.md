---
title: Importing QnAs in Bulk
---

# Importing QnAs in Bulk

This feature works with collections of QnA sets, using template-based import/export of the QnA sets from/to the current solution in Excel file format.

{% hint style="warning" %}
**IMPORTANT!** The upload process will **REPLACE** the matching QnAs for this AI Agent and solution with those in the excel file. The other non-matching QnAs will not be affected by the upload. Make sure that you download a copy of the existing train set before processing. To do so, click the **Download** button and click **DownloadTrainSet**. Based on your browser settings, the file is either automatically saved to your default Download folder or you need to save it.
{% endhint %}

You can import a new set of KB articles or update the existing one.

### Importing a new set of QnAs

To import a new set of QnAa:

1. Download the QnA train set template. To do so, click the **Download** button and select **DownloadTemplate**.

![](<../../.gitbook/assets/download template.png>)

Based on your browser settings, an excel file template containing the supported QnA Train Set format is either automatically saved to your default Download folder or you need to save it.

2. Fill in the excel template following the supported format and save the file with a different name. For reference on the solution train set format, see [QnA Set Format](<QnA Set Format.md>).
3. At the top-right corner of the Questions and Answers page, click the **Upload** button (![](../../.gitbook/assets/upload.png)). The UploadTrainSet pop-up appears.
4. Browse for your QnA train set file and select it.
5. Click the **Upload** button. Based on the file size, it might take a few seconds for the file to upload.
6. If you upload a wrong extension file or the file format is incorrect, a pop-up appears notifying that the import was unsuccessful.

Example:

![](<../../.gitbook/assets/import failed.png>)

7. Click **Ok** and retry.

When the import is successful, you can close the pop-up.

{% hint style="info" %}
**NOTE:** After the import, you need to train the AI Agent.
{% endhint %}

### Updating existing set of QnAs

To update an existing set of QnAs:

1. Download the current QnA train set file by clicking the **Download** button and selecting **DownloadTrainSet**.

![](<../../.gitbook/assets/downlaod train set.png>)

2. Store this file for backup purposes.
3. Copy and paste the file and rename it.
4. Open the renamed file and update it to accommodate your needs. For reference on the file format, see [KB Article Set Format](<QnA Set Format.md>). After you finish updating the file, save it.
5. Click the Upload button (![](../../.gitbook/assets/upload.png)).
6. The UploadTrainSet pop-up appears.
7. Browse for the updated QnA train set file and select it.
8. Click the **Upload** button. Based on the file size, it might take a few seconds for the file to upload.

If you upload a wrong extension file or the file format is incorrect, a pop-up appears notifying that the import was unsuccessful.

Example:

![](<../../.gitbook/assets/import failed.png>)

9. Click **Ok** and retry.

{% hint style="info" %}
**NOTE:** After the import, you need to train the AI Agent.
{% endhint %}
