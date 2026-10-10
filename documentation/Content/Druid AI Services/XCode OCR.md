<a id="XCodeOCR"></a>

# XCode OCR

The DRUID API engine performs OCR and data extraction from the following XCodes: QRCode, Barcode, PharmaCode and MaxCode.

> **NOTE:**
>
> - In order to use this Druid Vision service, contact [Druid Tech Support](<mailto:support@druidai.com?subject=Request: Activate Druid Vision service QRCode>).
> - For any APIs that are used for testing purposes and not in a production environment, Druid CANNOT be held responsible for the security of the processed data under the General Data Protection Regulation (GDPR). We highly recommend you to use sample data and documents for all APIs in testing environments.

<a id="Request"></a>

## Request

|  |  |
| --- | --- |
| Method | POST |
| API Resource URL (Endpoint) | The endpoint of the Druid Vision XCode service (...api/Engine/xcode). For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md). |
| Headers | Authorization: “Bearer <your bearer token>”  Content-Type: “multipart/form-data” |
| Authorization | Select **Bearer Token** and provide the Druid Vision **Token**. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md). |
| Body | “file”: <attached document file> (file attachment).  Supported formats: png, jpg, pdf. |

<a id="Response"></a>

## Response

**Response Example**

```
{
    "ResultId": "27ec090e-a5db-4dab-908a-bf1f25e9c948",
    "TemplateName": "xcode",
    "Status": "Complete",
    "StatusReason": null,
    "Confidence": 0.0,
    "Data": {
        "xcode": "7"
    },
    "ValidationResult": null
}
```
