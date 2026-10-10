---
title: Barcode OCR
---

# Barcode OCR

The Druid API engine performs OCR and data extraction from Barcodes.

{% hint style="info" %}
**NOTE:**

* In order to use this Druid Vision service, contact [Druid Tech Support](../Druid%20AI%20Services/mailto:support@druidai.com).
* For any APIs that are used for testing purposes and not in a production environment, Druid CANNOT be held responsible for the security of the processed data under the General Data Protection Regulation (GDPR). We highly recommend you to use sample data and documents for all APIs in testing environments.
{% endhint %}

### Request

|                             |                                                                                                                                                                                                   |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Method                      | POST                                                                                                                                                                                              |
| API Resource URL (Endpoint) | The endpoint of the Druid Vision **Barcode** service. For information on how to get the endpoint, see [Druid Vision](<Druid Vision.md>).                                                          |
| Authorization               | Select **Bearer Token** and provide the Druid Vision **Token**. For information on how to get the endpoint, see [Druid Vision](<Druid Vision.md>). ![](<../../.gitbook/assets/jam pass auth.png>) |
| Headers                     | Content-Type: “multipart/form-data” ![](<../../.gitbook/assets/barcode headers.png>)                                                                                                              |
| Body                        | “file”: (file attachment). Supported formats: png, jpg, pdf. ![](<../../.gitbook/assets/barcode file.png>)                                                                                        |

### Response

**Response Example**

```
{
    "ResultId": "27ec090e-a5db-4dab-908a-bf1f25e9c949",
    "TemplateName": "barcode",
    "Status": "Complete",
    "StatusReason": null,
    "Confidence": 0.0,
    "Data": {
        "barcode": "1112227"
    },
    "ValidationResult": null
}
```
