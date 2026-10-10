---
title: PDF Page Count
---

# PDF Page Count

This Vision endpoint provides the total number of pages in a PDF document. This feature is especially useful when preparing to convert specific PDF pages to JPEG.

{% hint style="info" %}
**NOTE:** This feature is available in DRUID 8.7 and higher. To use this Druid Vision service, you must have at least one Identity Vision API service enabled for your tenant. If not, please contact [Druid Tech Support](../Druid%20AI%20Services/mailto:support@druidai.com).
{% endhint %}

### Request

|                             |                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Method                      | POST                                                                                                                                                                                                                                                                                                                                                                                                                        |
| API Resource URL (Endpoint) | \*.druidplatform.com/api/document-processing/pdf-properties                                                                                                                                                                                                                                                                                                                                                                 |
| Authorization               | Select Bearer Token. If you already have a Druid Vision Token generated for an Identity API service in the Druid Portal, provide that token. For details on obtaining the token, refer to [Druid Vision](<Druid Vision.md>). If you don't have a token, generate one using the Authentication endpoint from Webhooks. For more information, see [Webhooks](../Webhooks.md). ![](<../../.gitbook/assets/pdf count auth.png>) |
| Body                        | “file”: (file attachment) Supported formats: pdf ![](<../../.gitbook/assets/pdf body.png>)                                                                                                                                                                                                                                                                                                                                  |

### Response

The response includes the total page count of the PDF.

![](<../../.gitbook/assets/pages coutn response.png>)
