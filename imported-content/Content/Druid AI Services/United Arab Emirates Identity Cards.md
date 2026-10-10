---
title: "United Arab Emirates Identity Cards"
---

<a id="UnitedArabEmiratesIdentityCards"></a>


The Druid API engine supports OCR and data extraction for identity cards issued by the United Arab Emirates.

> **NOTE:**
>
> - In order to use this Druid Vision service, contact [Druid Tech Support](<mailto:support@druidai.com?subject=Request: Activate Druid Vision service JAM_VotersId>).
> - For any APIs that are used for testing purposes and not in a production environment, Druid CANNOT be held responsible for the security of the processed data under the General Data Protection Regulation (GDPR). We highly recommend you to use sample data and documents for all APIs in testing environments.

<a id="Request"></a>

## Request

|  |  |
| --- | --- |
| Method | POST |
| API Resource URL (Endpoint) | The endpoint of the Druid Vision **UAE\_IdentityCard** service. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md). |
| Authorization | Select **Bearer Token** and provide the Druid Vision **Token**. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md).  ![](../Resources/Images/vision/uae%20auth.png) |
| Headers | Content-Type: “multipart/form-data”  ![](../Resources/Images/vision/uae%20headers.png) |
| Body | “file”: <attached document file> (file attachment). Send both the front and the back of identity card.  Supported formats: png, jpg, pdf.  ![](../Resources/Images/vision/uae%20files.png) |

<a id="Response"></a>

## Response

Data Returned by MRZ interpretation is found in the Data section of the response.

**Response Example**

```
{
    "ResultId": "972e0b5f-005e-4ee1-a1cc-1a85d0845416",
    "TemplateName": "UAE_IdentityCard",
    "Status": "Complete",
    "StatusReason": null,
    "Confidence": 0.77,
    "Data": {
        "CardNumber": "082278150",
        "CardNumber.Confidence": 0.96,
        "DateOfBirth": "05/12/1985",
        "DateOfBirth.Confidence": 0.95,
        "ExpiryDate": "23/02/2027",
        "ExpiryDate.Confidence": 0.96,
        "Face": 0,
        "Face.Confidence": 0,
        "IDNumber": "784-1995-2791050-1",
        "IDNumber.Confidence": 0.96,
        "MRZ": "IDARE08227815017841985020213838512051F2702238ARE<<<<<<<<<<<3LATIFA<MOHD<RASHED<ALMAKTOUM<<",
        "MRZ.Confidence": 0.96,
        "mrz.CountryCode": "ARE",
        "mrz.DateOfBirth": "1985-12-05T00:00:00Z",
        "mrz.DocumentNumber": "082278150",
        "mrz.DocumentSeries": null,
        "mrz.DocumentType": "IdentityCard",
        "mrz.ExpireDate": "2027-02-23T00:00:00Z",
        "mrz.FirstName": "",
        "mrz.LastName": "LATIFA MOHD RASHED ALMAKTOUM",
        "mrz.OptionalData": null,
        "mrz.Sex": "F",
        "MRZ1": "IDARE0822781501784198502021383",
        "MRZ1.Confidence": 0.94,
        "MRZ2": "8512051F2702238ARE<<<<<<<<<<<3",
        "MRZ2.Confidence": 0.99,
        "MRZ3": "LATIFA<MOHD<RASHED<ALMAKTOUM<<",
        "MRZ3.Confidence": 0.96,
        "NameAR": "شهريار جاويد جاويد فدا",
        "NameAR.Confidence": 0.93,
        "NameEN": "Shebaryar Javed Javed Fida",
        "NameEN.Confidence": 0.71,
        "NationalityAR": "باكستان",
        "NationalityAR.Confidence": 0.88,
        "NationalityEN": "Pakistan",
        "NationalityEN.Confidence": 0.99,
        "SexAR": "أنثى",
        "SexAR.Confidence": 0.56,
        "SexEN": "",
        "SexEN.Confidence": null,
        "Smile": "0"
    },
    "ValidationResult": {
        "MRZ": {
            "Status": "Valid",
            "Description": null
        }
    }
}
```
