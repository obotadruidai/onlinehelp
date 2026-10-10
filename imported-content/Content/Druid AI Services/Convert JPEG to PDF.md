---
title: Convert JPEG to PDF
---

# Convert JPEG to PDF

Druid Vision provides flexible JPEG-to-PDF conversion through two specialized endpoints, each designed for different use cases:

* **/convert-jpeg-to-pdf** – Returns the converted PDF as a byte array, ideal for scenarios where you need to store, manipulate, or transmit the complete file data.
* **/convert-jpeg-to-pdf-stream** – Returns the PDF as a stream for improved performance and lower memory overhead, making it the preferred option for handling larger files or high-volume conversions.

{% hint style="info" %}
**NOTE:** To use this Druid Vision service, you must have at least one Identity Vision API service enabled for your tenant. If not, please contact [Druid Tech Support](../Druid%20AI%20Services/mailto:support@druidai.com).
{% endhint %}

### Request

|                             |                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Method                      | POST                                                                                                                                                                                                                                                                                                                                                                        |
| API Resource URL (Endpoint) | \*.druidplatform.com/api/document-processing/convert-jpeg-to-pdf \*.druidplatform.com/api/document-processing/convert-jpeg-to-pdf-stream                                                                                                                                                                                                                                    |
| Params                      | You can customize the output PDF using the following request parameters:                                                                                                                                                                                                                                                                                                    |
| Authorization               | Select Bearer Token. If you already have a Druid Vision Token generated for an Identity API service in the Druid Portal, provide that token. For details on obtaining the token, refer to [Druid Vision](<Druid Vision.md>). If you don't have a token, generate one using the Authentication endpoint from Webhooks. For more information, see [Webhooks](../Webhooks.md). |
| Body                        | “files”: file attachment(s) The body must contain the image files to be converted. **Supported Extensions**: .jpg, .jpeg, and .png. **Multi-file Support**: You can upload a single image or multiple images in a single request.                                                                                                                                           |

### Response

The output format is determined by the selected endpoint. In both cases, if the request body contains multiple image files, DRUID Vision merges them into a single multi-page PDF, with each image occupying its own page.

* **/convert-jpeg-to-pd**f: Returns the PDF as a **byte array** (binary data). This is the standard output, suitable for most common file-handling scenarios.
* **/convert-jpeg-to-pdf-stream**: Returns the PDF as a **data stream**. This method is optimized for high performance and efficient memory management, making it the preferred choice for handling large files or high-volume processing.

### Related Topics

* [Download File by REST API](<../7_Integrations/Download file by REST API.md>)
