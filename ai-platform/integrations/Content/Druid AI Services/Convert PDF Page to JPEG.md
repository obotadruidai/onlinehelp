---
title: Convert PDF Page to JPEG
---


This Vision endpoint allows you to convert individual PDF pages into .jpeg format, enabling you to send images to GPT-4.o, which cannot perform OCR directly from PDF files.

{% hint style="warning" %}
**IMPORTANT!** If you need to convert multiple PDF pages, you must make a separate API request for each page you want to convert.
{% endhint %}

{% hint style="info" %}
**NOTE:** To use this Druid Vision service, you must have at least one Identity Vision API service enabled for your tenant. If not, please contact [Druid Tech Support](../Druid%20AI%20Services/mailto:support@druidai.com).
{% endhint %}

## Request

|                             |                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Method                      | POST                                                                                                                                                                                                                                                                                                                                                                                                                      |
| API Resource URL (Endpoint) | \*.druidplatform.com/api/document-processing/convert-pdf-page-to-jpeg                                                                                                                                                                                                                                                                                                                                                     |
| Params                      | Enter the **pageNumber** parameter and specify the PDF page number you want to convert to a .jpeg. ![](<../../.gitbook/assets/PARAMS CONVERT TO JPG.png>)                                                                                                                                                                                                                                                                 |
| Authorization               | Select Bearer Token. If you already have a Druid Vision Token generated for an Identity API service in the Druid Portal, provide that token. For details on obtaining the token, refer to [Druid Vision](<Druid Vision.md>). If you don't have a token, generate one using the Authentication endpoint from Webhooks. For more information, see [Webhooks](../Webhooks.md). ![](<../../.gitbook/assets/convert auth.png>) |
| Body                        | “file”: (file attachment) Supported formats: pdf ![](<../../.gitbook/assets/file (1).png>)                                                                                                                                                                                                                                                                                                                                |

## Response

The response returns the specified PDF page as a .jpeg file.

To capture the .jpeg file, use the **Download File** integration. You can then pass the file to GPT-4.o within your knowledge base-specific flows.

## Related Topics

* [Download File by REST API](<../7_Integrations/Download file by REST API.md>)
