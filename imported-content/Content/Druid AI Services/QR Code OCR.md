---
layout:
  title:
    visible: false
---

<a id="QRCodeOCR"></a>

# QR Code OCR

The Druid API engine performs OCR and data extraction from QR codes.

> **NOTE:**
>
> - In order to use this Druid Vision service, contact [Druid Tech Support](<mailto:support@druidai.com?subject=Request: Activate Druid Vision service QRCode>).
> - For any APIs that are used for testing purposes and not in a production environment, Druid CANNOT be held responsible for the security of the processed data under the General Data Protection Regulation (GDPR). We highly recommend you to use sample data and documents for all APIs in testing environments.

<a id="Request"></a>

## Request

|  |  |
| --- | --- |
| Method | POST |
| API Resource URL (Endpoint) | The endpoint of the Druid Vision QRCode service. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md). |
| Headers | Authorization: “Bearer <your bearer token>”  Content-Type: “multipart/form-data”  ![](../Resources/Images/OCR%20ID/qr%20code%20headers.png) |
| Authorization | Select **Bearer Token** and provide the Druid Vision **Token**. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md).  ![](../Resources/Images/OCR%20ID/qr%20code%20auth.png) |
| Body | “file”: <attached document file> (file attachment).  Supported formats: png, jpg, pdf.  ![](../Resources/Images/OCR%20ID/qr%20code.png) |

<a id="Response"></a>

## Response

**Response Example**

```
{
    "TemplateName": "qrcode",
    "Status": "Complete",
    "StatusReason": null,
    "Confidence": 0.0,
    "Data": {
            "qrCode": "just a simple QR Code for test"
            },
            "ValidationResult": null
}
```
