---
layout:
  title:
    visible: false
---

<a id="RomanianBirthCertificates"></a>

# Romanian Birth Certificates

The Druid API engine performs OCR and data extraction from Romanian birth certificates.

> **NOTE:**
>
> - In order to use this Druid Vision service, contact [Druid Tech Support](<mailto:support@druidai.com?subject=Request: Activate Druid Vision service BirthCertificate>).
> - For any APIs that are used for testing purposes and not in a production environment, Druid CANNOT be held responsible for the security of the processed data under the General Data Protection Regulation (GDPR). We highly recommend you to use sample data and documents for all APIs in testing environments.

<a id="Request"></a>

## Request

|  |  |
| --- | --- |
| Method | POST |
| API Resource URL (Endpoint) | The endpoint of the Druid Vision BirthCertificate service. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md). |
| Headers | Authorization: “Bearer <your bearer token>”  Content-Type: “multipart/form-data”  ![](../Resources/Images/OCR%20ID/birth%20headers.png) |
| Authorization | Select **Bearer Token** and provide the Druid Vision **Token**. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md).  ![](../Resources/Images/OCR%20ID/birtcertif%20auth.png) |
| Body | “file”: <attached document file> (file attachment).  Supported formats: png, jpg, pdf.  ![](../Resources/Images/OCR%20ID/birth%20certif.png)  If extraction fails due to issues like poor image quality, you can skip any of the following validation checks:   - Sex - SIRUTA - to skip PlaceOfBirthvalidation - DateOfBirth   Add the **skipValidations** parameter in the request body as many times as validation checks you want to escape from validation.  ![](../Resources/Images/vision/birth%20cert%20validation.png)  **NOTE:** Skipping validations is available in DRUID 8.1 and higher. |

<a id="Response"></a>

## Response

**Response Example**

```
{
   "TemplateName": "BirthCertificate",
   "Status": "Complete",
   "StatusReason": null,
   "Confidence": 0.86,
   "Data": {
                "CNSeries": "N.11",
                "BirthCertificateNumber": "xxxxxx",
                "CNP": "xxxxxxxxxxxxx",
                "LastName": "xxxxxxx",
                "FirstName": "xxxxxx",
                "FullName": "xxxxxxx xxxxxxx",
                "Sex": "FEMININ",
                "BirthYear": "xxxx",
                "BirthMonth": "xxxxx",
                "BirthDay": "xxxx",
                "Place": "xxxxx",
                "County": "xxxxxxxxxxxxx",
                "FatherFirstName": "xxxxx",
                "FatherLastName": "xxxxxxxxxxxx",
                "FatherFullName": "xxxxxxxx xxxxxx",
                   "MotherLastName": "xxxxxxxxxxxxx",
                "MotherFirstName": "xxxxxxxxxxx",
                "MotherFullName": "xxxxxxxxxxx xxxxxxxxxxxxxxxx",
                "BirthDocumentNumber": "xxxx",
                "CNDate": "xx xxxxx xxxx",
                "CNRegisteredPlace": "de/from xxxxxxxxxx -",
                "CNRegisteredCounty": "(ziua, luna, anul / jour, mois, annee / day, month, year) xxxxxxx",
                "Mentions1": "",
                "Mentions2": "Mentions/ Mentions ROMANIA",
                "Mentions": "Mentions/ Mentions ROMANIA",
                "CNRegisteredInstitution": "Sipar de Stare Civila xxxxxxxxxxxxxxxxx ---",
                "CNRegisteredDate": "xxxx x x x x | AAAALLZZ",
                "CNSeries.Confidence": 0.83,
                "BirthCertificateNumber.Confidence": 0.98,
                "CNP.Confidence": 0.88,
                "LastName.Confidence": 0.95,
                "FirstName.Confidence": 0.98,
                "FullName.Confidence": null,
                "Sex.Confidence": 0.98,
                "BirthYear.Confidence": 0.99,
                "BirthMonth.Confidence": 0.98,
                "BirthDay.Confidence": 0.99,
                "Place.Confidence": 0.97,
                "County.Confidence": 0.98,
                "FatherFirstName.Confidence": 0.99,
               "FatherLastName.Confidence": 0.95,
                "FatherFullName.Confidence": null,
                "MotherLastName.Confidence": 0.95,
                "MotherFirstName.Confidence": 0.64,
                "MotherFullName.Confidence": null,
                "BirthDocumentNumber.Confidence": 0.95,
                "CNDate.Confidence": 0.98,
                "CNRegisteredPlace.Confidence": 0.64,
                "CNRegisteredCounty.Confidence": 0.64,
                "Mentions1.Confidence": null,
                "Mentions2.Confidence": 0.56,
                "Mentions.Confidence": null,
                "CNRegisteredInstitution.Confidence": 0.56,
               "CNRegisteredDate.Confidence": 0.63,
                "DateOfBirth": "2018-03-03T00:00:00Z",
                "cnp.DateOfBirth": "2018-03-03T00:00:00Z",
                "cnp.Sex": "xxxxxxx",
                "County.SirutaId": xxxxxx,
                "Locality.SirutaId": xxxxxx
   },
   "ValidationResult": {
                "CNP": {
                    "Status": "Valid"
               },
               "Sex": {
                    "Status": "Valid"
                },
                "SIRUTA": {
                    "Status": "Valid"
                },
                "DateOfBirth": {
                    "Status": "Valid"
                }
   }
}
```
