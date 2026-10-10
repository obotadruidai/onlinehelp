---
title: "Romanian Identity Cards OCR"
---

<a id="RomanianIdentityCardsOCR"></a>


The Druid API engine supports OCR and data extraction for Romanian identity cards.

> **NOTE:**
>
> - In order to use this Druid Vision service, contact [Druid Tech Support](<mailto:support@druidai.com?subject=Request: Activate Druid Vision service JAM_VotersId>).
> - For any APIs that are used for testing purposes and not in a production environment, Druid CANNOT be held responsible for the security of the processed data under the General Data Protection Regulation (GDPR). We highly recommend you to use sample data and documents for all APIs in testing environments.

<a id="Request"></a>

## Request

|  |  |
| --- | --- |
| Method | POST |
| API Resource URL (Endpoint) | The endpoint of the Druid Vision **IdentityCard** service. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md). |
| Authorization | Select **Bearer Token** and provide the Druid Vision **Token**. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md).  ![](../Resources/Images/OCR%20ID/auth.png) |
| Headers | Content-Type: “multipart/form-data”  ![](../Resources/Images/OCR%20ID/headers.png) |
| Body without face validation | “file”: <attached document file> (file attachment).  Supported formats: png, jpg, pdf.  ![](../Resources/Images/OCR%20ID/id%20simple.png)  If extraction fails due to issues like poor image quality, you can skip any of the following validation checks:   - Sex - DateOfBirth - IssueDate - ExpireDate - SIRUTA - to skip Address validation - CountryCode - DocNumber - to skip the document number validation from the MRZ cross check - CNP - to skip the CNP validation from the MRZ cross check   Add the **skipValidations** parameter in the request body as many times as validation checks you want to escape from validation.  ![](../Resources/Images/vision/roid%20card%20valid.png)  **NOTE:** Skipping validations is available in DRUID 8.1 and higher. |
| Body with face validation | “file”: <attached document file> (file attachment)  “selfie”: <attached selfie photo> (file attachment)  Supported formats: png, jpg, pdf.  **NOTE:** The client/user needs to smile in the selfie, otherwise the face validation will fail.    ![](../Resources/Images/OCR%20ID/id%20with%20selfie.png)  **NOTE:** You can skip the same validation checks listed at Body without face validation. |

<a id="Response"></a>

## Response

Data Returned by MRZ interpretation is found in the Data section of the response.

Click the desired option below to see the response for the specific request.

## Identity Card without face validation

**Response Example**

```
Identity Card without face validation{
        "TemplateName": "IdentityCard",
        "Status": "Complete",
        "StatusReason": null,
        "Confidence": 0.8,
        "Data": {
            "Seria": "xx",
            "NR": "xxxxxx",
            "Sex": "x",
            "CNP": "xxxxxxxxxxxxx",
            "Nume": "xxxxxxx",
            "Prenume": "xxxx",
            "Cetatenie": "Romana / ROU",
            "Loc nastere": "Jud.xx xxx.xxxxxxx",
            "AddrLine1": "xxx.xxxxxxx",
            "AddrLine2": "Str.x xxx nr.xx sc.x et.x ap.x",
            "Emisa de": "xxxx xx",
            "Validity": "xx.xx.xx-xx.xx.xxxx",
            "MRZ1": "IDROUxxxxxxx<<xxxx<<<<<<<<<<<",
            "MRZ2": "xxxxxxxx<xROUxxxxxxxxxxxxxxxxxxxxxxx",
            "MRZ": "IDROUxxxxxxx<<xxxx<<<<<<<<<<<xxxxxxxx<xROUxxxxxxxxxxxxxxxxxxxxxxx",
            "Face": 1.0,
            "FaceSmall": 0.0,
            "Domiciliu": "xxx.xxxxxxx Str.x xxx nr.xx sc.x et.x ap.x",
            "Seria.Confidence": 0.99,
            "NR.Confidence": 0.98,
            "Sex.Confidence": 0.99,
            "CNP.Confidence": 0.97,
            "Nume.Confidence": 0.96,
            "Prenume.Confidence": 0.99,
            "Cetatenie.Confidence": 0.7,
            "Loc nastere.Confidence": 0.94,
            "AddrLine1.Confidence": 0.96,
            "AddrLine2.Confidence": 0.92,
            "Emisa de.Confidence": 0.92,
            "Validity.Confidence": 0.95,
            "MRZ1.Confidence": 0.71,
            "MRZ2.Confidence": 0.64,
            "MRZ.Confidence": 0.68,
            "Face.Confidence": 1.0,
            "FaceSmall.Confidence": 0.0,
            "Domiciliu.Confidence": 0.94,
            "DateOfBirth": "xxxx-xx-xxT00:00:00Z",
            "cnp.DateOfBirth": "xxxx-xx-xxT00:00:00Z",
        "cnp.CountyOfBirth": "Gorj",
        "cnp.CountyOfBirth.Id": 18,
            "cnp.Sex": "x",
            "Nume.Localized": null,
            "Nume.Localized.Confidence": 0.0,
            "Prenume.Localized": null,
            "Prenume.Localized.Confidence": 0.0,
            "Loc nastere.Localized": null,
            "Loc nastere.Localized.Confidence": 0.0,
            "AddrLine1.Localized": null,
            "AddrLine1.Localized.Confidence": 0.0,
            "AddrLine2.Localized": null,
            "AddrLine2.Localized.Confidence": 0.0,
            "ExpireDate": "xxxx-xx-xxT00:00:00Z",
            "IssueDate": "xxxx-xx-xxT00:00:00Z",
            "mrz.CountryCode": "ROU",
            "mrz.DateOfBirth": "xxxx-xx-xxT00:00:00Z",
            "mrz.DocumentSeries": "xx",
            "mrz.DocumentNumber": "xxxxxx",
            "mrz.DocumentType": "IdentityCard",
            "mrz.ExpireDate": "xxxx-xx-xxT00:00:00Z",
            "mrz.FirstName": "xxxx",
            "mrz.LastName": "xxxxxxx",
            "mrz.Sex": "x",
            "Smile": "0",
            "County": "B",
            "City": "xxxxx",
            "CityType": "xxxx",
            "Locality": "",
            "Village": "",
            "Commune": "",
            "StreetType": "xxxx",
            "StreetName": "xxxx",
            "StreetNo": "x",
            "BuildingNo": "",
            "EntranceNo": "x",
            "Floor": "x",
            "Apartment": "x",
            "District": "x",
            "LocalityType": "xxxx",
            "LocalityName": "xxxx",
            "County.SirutaId": xxx,
            "Locality.SirutaId": xxxxxx
        },
        "ValidationResult": {
            "CNP": {
                "Status": "Valid"
            },
            "Validity": {
                "Status": "Valid"
            },
            "MRZ": {
                "Status": "Valid"
            },
            "Sex": {
                "Status": "Valid"
            },
            "DateOfBirth": {
                "Status": "Valid"
            },
            "IssueDate": {
                "Status": "Valid"
            },
            "ExpireDate": {
               "Status": "Valid"
            },
            "SIRUTA": {
                "Status": "Valid"
            }
        }
}
```

## Identity Card with face validation

**Response Example**

```
Identity Card with face validation{
        "TemplateName": "IdentityCard",
        "Status": "Complete",
        "StatusReason": null,
        "Confidence": 0.8,
        "Data": {
                "Seria": "xx",
                "NR": "xxxxxx",
                "Sex": "x",
                "CNP": "xxxxxxxxxxxxx",
                "Nume": "xxxxx",
                "Prenume": "xxxxx",
                "Cetatenie": "Romana / ROU",
                "Loc nastere": "Jud.xxx Mun.xxx",
                "AddrLine1": "Mun.xxxx x",
                "AddrLine2": "Str.xxxx nr.72 sc.x et.x ap.xx",
                "Emisa de": "S.P.C.E.P. Sector 1",
                "Validity": "09.07.19-20.06.2029",
                "MRZ1": "IDROUxxxxx<<xxxxx<<<<<<<<<<<<<<<<<",
                "MRZ2": "xxxxxxxx<xROUxxxxxxxxxxxxxxxxxxxxxx",
                "MRZ": "IDROUxxxxx<<xxxxx<<<<<<<<<<<<<<<<<xxxxxxxx<xROUxxxxxxxxxxxxxxxxxxxxxx",
                "Face": 1.0,
                "FaceSmall": 0.0,
                "Domiciliu": "Mun.xxxx Str.xxxx nr.72 sc.x et.x ap.xx",
                "Seria.Confidence": 0.99,
                "NR.Confidence": 0.98,
                "Sex.Confidence": 0.99,
                "CNP.Confidence": 0.98,
                "Nume.Confidence": 0.98,
                "Prenume.Confidence": 0.99,
                "Cetatenie.Confidence": 0.59,
                "Loc nastere.Confidence": 0.95,
                "AddrLine1.Confidence": 0.94,
                "AddrLine2.Confidence": 0.94,
                "Emisa de.Confidence": 0.98,
                "Validity.Confidence": 0.95,
                "MRZ1.Confidence": 0.72,
                "MRZ2.Confidence": 0.61,
                "MRZ.Confidence": 0.66,
                "Face.Confidence": 1.0,
                "FaceSmall.Confidence": 0.0,
                "Domiciliu.Confidence": 0.94,
                "DateOfBirth": "xxxx-xx-xxT00:00:00Z",
                "cnp.DateOfBirth": "xxxx-xx-xxT00:00:00Z",
         "cnp.CountyOfBirth": "Gorj",
         "cnp.CountyOfBirth.Id": 18,
                "cnp.Sex": "x",
                "Nume.Localized": null,
                "Nume.Localized.Confidence": 0.0,
                "Prenume.Localized": null,
                "Prenume.Localized.Confidence": 0.0,
                "Loc nastere.Localized": null,
                "Loc nastere.Localized.Confidence": 0.0,
                "AddrLine1.Localized": null,
                "AddrLine1.Localized.Confidence": 0.0,
                "AddrLine2.Localized": null,
                "AddrLine2.Localized.Confidence": 0.0,
                "ExpireDate": "xxxx-xx-xxT00:00:00Z",
                "IssueDate": "xxxx-xx-xxT00:00:00Z",
                "mrz.CountryCode": "ROU",
                "mrz.DateOfBirth": "xxxx-xx-xxT00:00:00Z",
                "mrz.DocumentSeries": "xx",
                "mrz.DocumentNumber": "xxxxxx",
                "mrz.DocumentType": "IdentityCard",
                "mrz.ExpireDate": "xxxx-xx-xxT00:00:00Z",
                "mrz.FirstName": "xxxxx",
                "mrz.LastName": "xxxxx",
                "mrz.Sex": "x",
                "Smile": "0.999",
                "County": "x",
                "City": "xxxx",
                "CityType": "xxxxx",
                "Locality": "",
                "Village": "",
                "Commune": "",
                "StreetType": "xxxx",
                "StreetName": "xxxx",
                "StreetNo": "x",
                "BuildingNo": "",
                "EntranceNo": "x",
                "Floor": "x",
                "Apartment": "xx",
                "District": "x",
                "LocalityType": "xxxxxxx",
                "LocalityName": "xxxxx",
                "County.SirutaId": 403,
                "Locality.SirutaId": xxxxxx
         },
         "ValidationResult": {
                "CNP": {
                    "Status": "Valid"
                },
                "Validity": {
                    "Status": "Valid"
                },
                "MRZ": {
                    "Status": "Valid"
                },
                "Face": {
                    "Status": "Valid"
                },
                "Sex": {
                    "Status": "Valid"
                },
                "DateOfBirth": {
                    "Status": "Valid"
                },
                "IssueDate": {
                    "Status": "Valid"
                },
                "ExpireDate": {
                    "Status": "Valid"
                },
                "SIRUTA": {
                    "Status": "Valid"
                }
          }
   }
```

<a id="Validations"></a>

### Validations

Validations performed in the MRZ section:

- **DocumentNumber** - checksum cross-checked with MRZ Line\_2 first control digit.
- **DateOfBirth** - checksum cross-checked with MRZ Line\_2 second control digit.
- **DateOfExpiry** - checksum cross-checked with MRZ Line\_2 third control digit.
- **Line\_2** - checksum of the entire MRZ line 2 (if any of the above fails, the entire line fails and the entire MRZ checksum fails).
- **Sex** - validation on values “F” or “M”.

Based on **Code** and **Nationality**, an existing template of the OCR service is identified:

- If Code = “ID” and Nationality = “ROU”, the template “Identity Card” is used.
- If Code = “IS” and Nationality = “ROU”, the template “RO\_ResidenceCard” is used.

The results of the “Identity Card” template provide the following validations:

- **CNP** - Status Invalid if the checksum of the CNP cross-checked with the control digit fails. The CNP validation is performed against the ID values provided in the reference table below.

| ID | County of Birth |
| --- | --- |
| 0 | Invalid |
| 1 | Alba |
| 2 | Arad |
| 3 | Argeș |
| 4 | Bacău |
| 5 | Bihor |
| 6 | Bistrița\_Năsăud |
| 7 | Botoșani |
| 8 | Brașov |
| 9 | Brăila |
| 10 | Buzău |
| 11 | Caraș\_Severin |
| 12 | Cluj |
| 13 | Constanța |
| 14 | Covasna |
| 15 | Dâmbovița |
| 16 | Dolj |
| 17 | Galați |
| 18 | Gorj |
| 19 | Harghita |
| 20 | Hunedoara |
| 21 | Ialomița |
| 22 | Iași |
| 23 | Ilfov |
| 24 | Maramureș |
| 25 | Mehedinți |
| 26 | Mureș |
| 27 | Neamț |
| 28 | Olt |
| 29 | Prahova |
| 30 | Satu\_Mare |
| 31 | Sălaj |
| 32 | Sibiu |
| 33 | Suceava |
| 34 | Teleorman |
| 35 | Timiș |
| 36 | Tulcea |
| 37 | Vaslui |
| 38 | Vâlcea |
| 39 | Vrancea |
| 40 | București |
| 41 | București\_Sector\_1 |
| 42 | București\_Sector\_2 |
| 43 | București\_Sector\_3 |
| 44 | București\_Sector\_4 |
| 45 | București\_Sector\_5 |
| 46 | București\_Sector\_6 |
| 47 | București\_Sector\_7 |
| 48 | București\_Sector\_8 |
| 51 | Călărași |
| 52 | Giurgiu |
| 80 | Outside\_Romania |

- **Validity** - Status Invalid if the OCR service fails to retrieve information in **IssueDate** and **ExpiryDate**.
- **MRZ** - Status Invalid if at least one of the cross-checks on the MRZ field fails (document number, date of birth, date of expiry, sex, IssuingState).
- **Sex** - Status Invalid if the cross-check of the following fields fail: Sex from CNP, Sex from Document, Sex from MRZ.
- **DateOfBirth** - Status Invalid if the cross-check of the following fields fail: DateOfBirth from CNP, DateOfBirth from Document, DateOfBirth from MRZ.
- **IssueDate** - Status Invalid if the cross-check of the following fields fail: IssueDate from Document, IssueDate from MRZ.
- **ExpireDate** - Status Invalid if the cross-check of the following fields fail: ExpireDate from Document, ExpireDate from MRZ.
- **SIRUTA** - Status Invalid if the value of field Locality cannot be matched to the SIRUTA dictionary.
- **Face** - Status Invalid if the "Face.Confidence" is not 1.0 or "Invalid: you forgot to smile" if the customer is not smiling in the selfie. This validation is done for OCR of Romanian identity cards with selfie.

If the data cannot be extracted by the OCR Service, validations on all of the above fields will fail.

<a id="Statusfield"></a>

### Status field

1. **InvalidDocument**. All validations on the document failed.
2. **Partial**. There are failed validations.
3. **Complete**. All validations succeeded.
4. **InvalidTemplate**. Template is invalid (for development purpose only).
5. **InvalidImage**. Image is invalid (format, size).

If Status is other than “Complete”, you see the error and the validation details in the “ValidationResult” attribute.

<a id="ImageValidation"></a>

### Image Validation

For best results the image is automatically prepared by the API before the OCR process executes, applying multiple image processing algorithms.

Supported formats: png, jpg, pdf.
