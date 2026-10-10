---
title: "Jamaican Voter ID Card OCR"
---

<a id="JamaicanVoterIDCardOCR"></a>


The Druid API engine performs OCR and data extraction from Jamaican voter ID cards.

{% hint style="info" %}
**NOTE:**

- In order to use this Druid Vision service, contact [Druid Tech Support](<mailto:support@druidai.com?subject=Request: Activate Druid Vision service JAM_VotersId>).
- For any APIs that are used for testing purposes and not in a production environment, Druid CANNOT be held responsible for the security of the processed data under the General Data Protection Regulation (GDPR). We highly recommend you to use sample data and documents for all APIs in testing environments.
{% endhint %}

<a id="Request"></a>

## Request

|  |  |
| --- | --- |
| Method | POST |
| API Resource URL (Endpoint) | The endpoint of the Druid Vision **JAM\_VotersId** service. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md). |
| Authorization | Select **Bearer Token** and provide the Druid Vision **Token**. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md).  ![](../Resources/Images/vision/jam%20voterid%20auth.png) |
| Headers | Content-Type: “multipart/form-data”  ![](../Resources/Images/vision/jam%20voter%20multipart.png) |
| Body | “file”: <attached document file> (file attachment).  Supported formats: png, jpg, pdf.  ![](../Resources/Images/vision/jam%20voter%20idbody.png) |

<a id="Response"></a>

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

<a id="ImageValidation"></a>

### Image Validation

For best results the image is automatically prepared by the API before the OCR process executes, applying multiple image processing algorithms.

Supported formats: png, jpg, pdf.
