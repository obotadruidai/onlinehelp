---
title: QR Code OCR
---


The Druid API engine performs OCR and data extraction from QR codes.

{% hint style="info" %}
**NOTE:**

* In order to use this Druid Vision service, contact [Druid Tech Support](../Druid%20AI%20Services/mailto:support@druidai.com).
* For any APIs that are used for testing purposes and not in a production environment, Druid CANNOT be held responsible for the security of the processed data under the General Data Protection Regulation (GDPR). We highly recommend you to use sample data and documents for all APIs in testing environments.
{% endhint %}

## Request

|                             |                                                                                                                                                                                                  |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Method                      | POST                                                                                                                                                                                             |
| API Resource URL (Endpoint) | The endpoint of the Druid Vision QRCode service. For information on how to get the endpoint, see [Druid Vision](<Druid Vision.md>).                                                              |
| Headers                     | Authorization: “Bearer ” Content-Type: “multipart/form-data” ![](<../../.gitbook/assets/qr code headers.png>)                                                                                    |
| Authorization               | Select **Bearer Token** and provide the Druid Vision **Token**. For information on how to get the endpoint, see [Druid Vision](<Druid Vision.md>). ![](<../../.gitbook/assets/qr code auth.png>) |
| Body                        | “file”: (file attachment). Supported formats: png, jpg, pdf. ![](<../../.gitbook/assets/qr code.png>)                                                                                            |

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
