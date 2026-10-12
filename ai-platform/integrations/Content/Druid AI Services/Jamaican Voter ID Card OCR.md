---
title: Jamaican Voter ID Card OCR
---


The Druid API engine performs OCR and data extraction from Jamaican voter ID cards.

{% hint style="info" %}
**NOTE:**

* In order to use this Druid Vision service, contact [Druid Tech Support](../Druid%20AI%20Services/mailto:support@druidai.com).
* For any APIs that are used for testing purposes and not in a production environment, Druid CANNOT be held responsible for the security of the processed data under the General Data Protection Regulation (GDPR). We highly recommend you to use sample data and documents for all APIs in testing environments.
{% endhint %}

## Request

|                             |                                                                                                                                                                                                      |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Method                      | POST                                                                                                                                                                                                 |
| API Resource URL (Endpoint) | The endpoint of the Druid Vision **JAM\_VotersId** service. For information on how to get the endpoint, see [Druid Vision](<Druid Vision.md>).                                                       |
| Authorization               | Select **Bearer Token** and provide the Druid Vision **Token**. For information on how to get the endpoint, see [Druid Vision](<Druid Vision.md>). ![](<../../.gitbook/assets/jam voterid auth.png>) |
| Headers                     | Content-Type: “multipart/form-data” ![](<../../.gitbook/assets/jam voter multipart.png>)                                                                                                             |
| Body                        | “file”: (file attachment). Supported formats: png, jpg, pdf. ![](<../../.gitbook/assets/jam voter idbody.png>)                                                                                       |

## Response

**Response Example**

```
{
    "ResultId": "b8f34b34-6751-4c6b-9a98-75d0c2562a4d",
    "TemplateName": "JAM_VotersId",
    "Status": "Complete",
    "StatusReason": null,
    "Confidence": 0.72,
    "Data": {
        "Surname": "SEVILLE",
        "FirstName": "SELTECA",
        "MiddleName": "MARTINA",
        "DateOfBirth": "AUG 31, 1951",
        "Height": "5 '05\" 165cm",
        "Sex": "F",
        "DupNo": "0",
        "DistinguishingMarks": "",
        "ElectorRegistrationNo": "688631",
        "CardIssueDate": "FEB 28, 2022",
        "CardExpiryDate": "DEC 31, 2031",
        "Face": 1.0,
        "Name": "SELTECA MARTINA SEVILLE",
        "Surname.Confidence": 0.97,
        "FirstName.Confidence": 0.9,
        "MiddleName.Confidence": 0.97,
        "DateOfBirth.Confidence": 0.98,
        "Height.Confidence": 0.77,
        "Sex.Confidence": 0.89,
        "DupNo.Confidence": 0.37,
        "DistinguishingMarks.Confidence": null,
        "ElectorRegistrationNo.Confidence": 0.99,
        "CardIssueDate.Confidence": 0.87,
        "CardExpiryDate.Confidence": 0.96,
        "Face.Confidence": 1.0,
        "Name.Confidence": null,
        "Smile": "0"
    },
    "ValidationResult": {}
}
```

### Image Validation

For best results the image is automatically prepared by the API before the OCR process executes, applying multiple image processing algorithms.

Supported formats: png, jpg, pdf.
