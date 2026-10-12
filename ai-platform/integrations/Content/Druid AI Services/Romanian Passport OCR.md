---
title: Romanian Passports OCR
---


The DRUIDAPI engine performs OCR and data extraction from Romanian passports.

{% hint style="info" %}
**NOTE:**

* In order to use this DRUID Vision service, contact [Druid Tech Support](../Druid%20AI%20Services/mailto:support@druidai.com).
* For any APIs that are used for testing purposes and not in a production environment, DRUID CANNOT be held responsible for the security of the processed data under the General Data Protection Regulation (GDPR). We highly recommend you to use sample data and documents for all APIs in testing environments.
{% endhint %}

## Request

|                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Method                       | POST                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| API Resource URL (Endpoint)  | The endpoint of the DRUID Vision **RO\_Passport** service. For information on how to get the endpoint, see [Druid Vision](<Druid Vision.md>).                                                                                                                                                                                                                                                                                                                                                 |
| Headers                      | Authorization: “Bearer ” Content-Type: “multipart/form-data”                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Authorization                | Select **Bearer Token** and provide the Druid Vision **Token**. For information on how to get the endpoint, see [Druid Vision](<Druid Vision.md>).                                                                                                                                                                                                                                                                                                                                            |
| Body without face validation | “file”: (file attachment). Supported formats: png, jpg, pdf. If extraction fails due to issues like poor image quality, you can skip any of the following validation checks: - DateOfBirth - ExpireDate - IssueDate - Sex - CNP Add the **skipValidations** parameter in the request body as many times as validation checks you want to escape from validation. ![](<../../.gitbook/assets/RO_Passport validation.png>) **NOTE:** Skipping validations is available in DRUID 8.1 and higher. |
| Body with face validation    | “file”: (file attachment) “selfie”: (file attachment) Supported formats: png, jpg, pdf. **NOTE:** The client/user needs to smile in the selfie, otherwise the face validation will fail.                                                                                                                                                                                                                                                                                                      |

## Response

Data Returned by MRZ interpretation is found in the Data section of the response.

**Response Example**

```
{
    "ResultId": "3bee49b1-e07f-432f-8a9f-4aa733aa8699",
    "TemplateName": "RO_Passport",
    "Status": "Partial",
    "StatusReason": null,
    "Confidence": 0.92,
    "Data": {
        "Type": "PE",
        "IssueState": "ROU",
        "DocumentNumber": "053539516",
        "LastName": "XXXX-XXXX",
        "FirstName": "XXXX",
        "Citizenship": "ROMANA",
        "DateOfBirth": "09.03.86",
        "CNP": "XXXXXXXXXXXXX",
        "Sex": "M",
        "PlaceOfBirth": "XXXXXXXXXXX",
        "IssueDate": "18.02.16",
        "Issuer": "XXXXXXXXX",
        "DateOfExpiry": "18.02.21",
        "MRZ1": "PEROUXXXX<XXXX<<XXXX<<<<<<<<<<<<<<<<<<<",
        "MRZ2": "XXXXXXXXXXROUXXXXXXXMXXXXXXXXXXXXXXXXXXXX<46",
        "MRZ": "PEROUXXXX<XXXX<<XXXX<<<<<<<<<<<<<<<<<<<XXXXXXXXXXROUXXXXXXXMXXXXXXXXXXXXXXXXXXXX<46",
        "Face": 1.0,
        "FullName": "XXXX XXXX-XXXX",
        "Type.Confidence": 1.0,
        "IssueState.Confidence": 0.99,
        "DocumentNumber.Confidence": 0.99,
        "LastName.Confidence": 0.99,
        "FirstName.Confidence": 0.99,
        "Citizenship.Confidence": 0.99,
        "DateOfBirth.Confidence": 1.0,
        "CNP.Confidence": 0.99,
        "Sex.Confidence": 1.0,
        "PlaceOfBirth.Confidence": 1.0,
        "IssueDate.Confidence": 1.0,
        "Issuer.Confidence": 0.97,
        "DateOfExpiry.Confidence": 1.0,
        "MRZ1.Confidence": 0.94,
        "MRZ2.Confidence": 0.88,
        "MRZ.Confidence": 0.91,
        "Face.Confidence": 1.0,
        "FullName.Confidence": null,
        "cnp.DateOfBirth": "1986-03-09T00:00:00Z",
        "cnp.Sex": "M",
        "cnp.CountyOfBirth": "XXXXXXX",
        "cnp.CountyOfBirth.id": 29,
        "mrz.CountryCode": "ROU",
        "mrz.DateOfBirth": "1986-03-09T00:00:00Z",
        "mrz.DocumentSeries": null,
        "mrz.DocumentNumber": "XXXXXXXXX",
        "mrz.DocumentType": "Passport",
        "mrz.ExpireDate": "2021-02-18T00:00:00Z",
        "mrz.FirstName": "XXXX",
        "mrz.LastName": "XXXX XXXX",
        "mrz.Sex": "M",
        "mrz.OptionalData": "XXXXXXXXXXXXX",
        "Smile": "0"
    },
    "ValidationResult": {
        "CNP": {
            "Status": "Valid"
        },
        "MRZ": {
            "Status": "Valid"
        },
        "DateOfBirth": {
            "Status": "Valid"
        },
        "Validity": {
            "Status": "Invalid",
            "Description": "[DateOfExpiry] document is expired"
        },
        "IssueDate": {
            "Status": "Valid"
        },
        "Sex": {
            "Status": "Valid"
        },
        "CrossCheck_CNP": {
            "Status": "Valid"
        }
    }
}
```

### Validations

Validations performed in the MRZ section:

* **DocumentNumber** - checksum cross-checked with MRZ Line\_2 first control digit.
* **DateOfBirth** - checksum cross-checked with MRZ Line\_2 second control digit.
* **DateOfExpiry** - checksum cross-checked with MRZ Line\_2 third control digit.
* **Line\_2** - checksum of the entire MRZ line 2 (if any of the above fails, the entire line fails and the entire MRZ checksum fails).
* **Sex** - validation on values “F” or “M”.

Based on **Code** and **Nationality**, an existing template of the OCR service is identified:

* If Code = “PE” and Nationality = “ROU”, the template “RO\_Passport” is used.

The results of the “RO\_Passport” template provide the following validations:

* **CNP** - Status Invalid if the checksum of the CNP cross-checked with the control digit fails. The CNP validation is performed against the ID values provided in the reference table below.

| ID | County of Birth      |
| -- | -------------------- |
| 0  | Invalid              |
| 1  | Alba                 |
| 2  | Arad                 |
| 3  | Argeș                |
| 4  | Bacău                |
| 5  | Bihor                |
| 6  | Bistrița\_Năsăud     |
| 7  | Botoșani             |
| 8  | Brașov               |
| 9  | Brăila               |
| 10 | Buzău                |
| 11 | Caraș\_Severin       |
| 12 | Cluj                 |
| 13 | Constanța            |
| 14 | Covasna              |
| 15 | Dâmbovița            |
| 16 | Dolj                 |
| 17 | Galați               |
| 18 | Gorj                 |
| 19 | Harghita             |
| 20 | Hunedoara            |
| 21 | Ialomița             |
| 22 | Iași                 |
| 23 | Ilfov                |
| 24 | Maramureș            |
| 25 | Mehedinți            |
| 26 | Mureș                |
| 27 | Neamț                |
| 28 | Olt                  |
| 29 | Prahova              |
| 30 | Satu\_Mare           |
| 31 | Sălaj                |
| 32 | Sibiu                |
| 33 | Suceava              |
| 34 | Teleorman            |
| 35 | Timiș                |
| 36 | Tulcea               |
| 37 | Vaslui               |
| 38 | Vâlcea               |
| 39 | Vrancea              |
| 40 | București            |
| 41 | București\_Sector\_1 |
| 42 | București\_Sector\_2 |
| 43 | București\_Sector\_3 |
| 44 | București\_Sector\_4 |
| 45 | București\_Sector\_5 |
| 46 | București\_Sector\_6 |
| 47 | București\_Sector\_7 |
| 48 | București\_Sector\_8 |
| 51 | Călărași             |
| 52 | Giurgiu              |
| 80 | Outside\_Romania     |

* **Validity** - Status Invalid if the OCR service fails to retrieve information in **IssueDate** and **ExpiryDate**.
* **MRZ** - Status Invalid if at least one of the cross-checks on the MRZ field fails (document number, date of birth, date of expiry, sex, IssuingState).
* **Sex** - Status Invalid if the cross-check of the following fields fail: Sex from CNP, Sex from Document, Sex from MRZ.
* **DateOfBirth** - Status Invalid if the cross-check of the following fields fail: DateOfBirth from CNP, DateOfBirth from Document, DateOfBirth from MRZ.
* **IssueDate** - Status Invalid if the cross-check of the following fields fail: IssueDate from Document, IssueDate from MRZ.
* **Face** - Status Invalid if the "Face.Confidence" is not 1.0 or "Invalid: you forgot to smile" if the customer is not smiling in the selfie. This validation is done for OCR of Romanian identity cards with selfie.

If the data cannot be extracted by the OCR Service, validations on all of the above fields will fail.

### Status field

1. **InvalidDocument**. All validations on the document failed.
2. **Partial**. There are failed validations.
3. **Complete**. All validations succeeded.
4. **InvalidTemplate**. Template is invalid (for development purpose only).
5. **InvalidImage**. Image is invalid (format, size).

If Status is other than “Complete”, you see the error and the validation details in the “ValidationResult” attribute.

### Image Validation

For best results the image is automatically prepared by the API before the OCR process executes, applying multiple image processing algorithms.

Supported formats: png, jpg, pdf.
