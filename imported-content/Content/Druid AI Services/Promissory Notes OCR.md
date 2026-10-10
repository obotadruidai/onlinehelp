---
title: "Promissory Notes OCR"
---

<a id="PromissoryNotesOCR"></a>


The Druid API engine performs OCR and data extraction from Promissory Notes.

> **NOTE:**
>
> - In order to use this Druid Vision service, contact [Druid Tech Support](<mailto:support@druidai.com?subject=Request: Activate Druid Vision service JAM_Passport>).
> - For any APIs that are used for testing purposes and not in a production environment, Druid CANNOT be held responsible for the security of the processed data under the General Data Protection Regulation (GDPR). We highly recommend you to use sample data and documents for all APIs in testing environments.

<a id="Request"></a>

## Request

|  |  |
| --- | --- |
| Method | POST |
| API Resource URL (Endpoint) | The endpoint of the Druid Vision **Promissory\_Note** service. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md). |
| Headers | Authorization: “Bearer <your bearer token>”  Content-Type: “multipart/form-data”  ![](../Resources/Images/vision/prom%20header.png) |
| Authorization | Select **Bearer Token** and provide the DRUID Vision **Token**. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md).  ![](../Resources/Images/vision/prom%20auth.png) |
| Body | “file”: <attached document file> (file attachment).  Supported formats: png, jpg, pdf.  ![](../Resources/Images/vision/prom%20body.png)  If extraction fails due to issues such as poor image quality, you can skip the IssuerIBAN validation by including the parameter **skipValidations** = **IssuerIBAN** in the request body.  **NOTE:** Skipping validations is available in DRUID version 8.1 and higher. |

<a id="Response"></a>

## Response

The issuer IBAN is validated.

**Response Example**

```
{
    "ResultId": "bd0ee3da-01d8-4047-acd9-eee5651c970d",
    "TemplateName": "Promissory_Note",
    "Status": "Complete",
    "StatusReason": null,
    "Confidence": 0.92,
    "Data": {
        "IssuerCode": "23010123",
        "IssuerCode.Confidence": 1.0,
        "IssuerIBAN": "RO10INGB0000000011345678",
        "IssuerIBAN.Confidence": 0.68,
        "IssuerName": "ISSUER NAME",
        "IssuerName.Confidence": 1.0,
        "Series": "BANK123",
        "Series.Confidence": 0.98
    },
    "ValidationResult": {
        "IssuerIBAN": {
            "Status": "Valid"
        }
    }
}
```
