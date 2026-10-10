---
layout:
  title:
    visible: false
---

<a id="RomanianResidenceCardOCR"></a>

# Romanian Residence Card OCR

The Druid API engine performs OCR and data extraction from Romanian residence cards.

> **NOTE:**
>
> - In order to use this Druid Vision service, contact [Druid Tech Support](<mailto:support@druidai.com?subject=Request: Activate Druid Vision service  RO_ResidenceCard>).
> - For any APIs that are used for testing purposes and not in a production environment, Druid CANNOT be held responsible for the security of the processed data under the General Data Protection Regulation (GDPR). We highly recommend you to use sample data and documents for all APIs in testing environments.

<a id="Request"></a>

## Request

|  |  |
| --- | --- |
| Method | POST |
| API Resource URL (Endpoint) | The endpoint of the Druid Vision RO\_ResidenceCard service. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md). |
| Headers | Authorization: “Bearer <your bearer token>”  Content-Type: “multipart/form-data”  ![](../Resources/Images/OCR%20ID/residencecard%20headers.png) |
| Authorization | Select **Bearer Token** and provide the Druid Vision **Token**. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md).  ![](../Resources/Images/OCR%20ID/residencecrad%20auth.png) |
| Body | “file”: <attached RO residence card document>.  Supported formats: png, jpg, pdf.  ![](../Resources/Images/OCR%20ID/residence%20card.png)  If extraction fails due to issues like poor image quality, you can skip any of the following validation checks:   - SIRUTA - to skip the Address validation - DateOfBirth - Validity - IssueDate - Sex   Add the **skipValidations** parameter in the request body as many times as validation checks you want to escape from validation.  ![](../Resources/Images/vision/residence%20card.png)  **NOTE:** Skipping validations is available in DRUID 8.1 and higher. |

<a id="Response"></a>

## Response

**Response Example**

```
{
        "TemplateName": "RO_ResidenceCard",
        "Status": "Partial",
        "StatusReason": null,
        "Confidence": 0.88,
        "Data": {
            "CNP": "8781001999999",
            "Series": "xxxx",
            "Number": "xxxxx",
            "LastName": "xxxxx",
            "FirstName": "xxxx",
            "DateOfBirth": "1978-10-01T00:00:00+03:00",
            "Citizenship": "OLANDA",
            "PlaceOfbirth": "OLANDA",
            "Sex": "F",
            "AddrLine1": "xxxxxxxxxxx xxx xxxxx",
            "AddrLine2": "xx xx , xx xx , xx xx , xxxxx",
            "Issuer": "xxxx - xxxxxxx",
            "IssueDate": "2011-10-01T00:00:00+03:00",
            "Validity": "2021-10-01T00:00:00+03:00",
            "MRZ1": "ISROUxxxxx<<xxxx<<<<<<<<<<<<<<<<<",
            "MRZ2": "RPUxxxxx<xNLDxxxxxxxxxxxxxxxxxxxxxxx",
            "MRZ": null,
            "Face": 1.0,
            "FullName": "xxxx xxxxx",
            "Domiciliu": "xxxxxxxxxxx xxx xxxxx xx xx , xx xx , xx xx , xxxxx",
            "CNP.Confidence": 0.97,
            "Series.Confidence": 0.99,
            "Number.Confidence": 0.98,
            "LastName.Confidence": 0.98,
            "FirstName.Confidence": 0.97,
            "DateOfBirth.Confidence": 0.98,
            "Citizenship.Confidence": 0.98,
            "PlaceOfbirth.Confidence": 0.98,
            "Sex.Confidence": 0.99,
            "AddrLine1.Confidence": 0.98,
            "AddrLine2.Confidence": 0.73,
            "Issuer.Confidence": 0.85,
            "IssueDate.Confidence": 0.98,
            "Validity.Confidence": 0.98,
            "MRZ1.Confidence": 0.72,
            "MRZ2.Confidence": 0.84,
            "MRZ.Confidence": null,
            "Face.Confidence": 1.0,
            "FullName.Confidence": null,
            "Domiciliu.Confidence": 0.86,
            "cnp.DateOfBirth": "0001-01-01T00:00:00",
            "cnp.Sex": "X",
            "mrz.CountryCode": null,
            "mrz.DateOfBirth": null,
            "mrz.DocumentSeries": null,
            "mrz.DocumentNumber": null,
            "mrz.DocumentType": null,
            "mrz.ExpireDate": null,
            "mrz.FirstName": null,
            "mrz.LastName": null,
            "mrz.Sex": null,
            "Smile": "0",
            "County": "",
            "City": "",
            "CityType": "",
            "Locality": "",
            "Village": "",
            "Commune": "",
            "StreetType": "xxx",
            "StreetName": "xx xx , xx xx , xx xx , xxxxx",
            "StreetNo": "",
            "BuildingNo": "",
            "EntranceNo": "",
            "Floor": "",
            "Apartment": "",
            "District": "",
            "LocalityType": "",
            "LocalityName": ""
        },
        "ValidationResult": {
            "CNP": {
                "Status": "Invalid"
            },
            "DateOfBirth": {
                "Status": "Invalid",
                "Description": "Missing [mrz.DateOfBirth] field in result data"
            },
            "IssueDate": {
                "Status": "Valid"
            },
            "Validity": {
                "Status": "Invalid",
                "Description": "Missing [mrz.Validity] field in result data"
            },
            "MRZ": {
                "Status": "Invalid"
            },
            "SIRUTA": {
                "Status": "Invalid",
                "Description": "County [] could not be located in SIRUTA"
            },
            "Sex": {
                "Status": "Invalid",
                "Description": "Missing [mrz.Sex] field in result data"
            }
        }
}
```
