<a id="NewRomanianIdentityCardsOCR"></a>

# New Romanian Identity Cards OCR

The Druid API engine supports OCR and data extraction for Romanian identity cards issued with a CIP (electronic chip), applicable to identity cards issued starting in January 2024.

> **NOTE:**
>
> - In order to use this Druid Vision service, contact [Druid Tech Support](<mailto:support@druidai.com?subject=Request: Activate Druid Vision service JAM_VotersId>).
> - For any APIs that are used for testing purposes and not in a production environment, Druid CANNOT be held responsible for the security of the processed data under the General Data Protection Regulation (GDPR). We highly recommend you to use sample data and documents for all APIs in testing environments.

<a id="Request"></a>

## Request

|  |  |
| --- | --- |
| Method | POST |
| API Resource URL (Endpoint) | The endpoint of the Druid Vision **New\_IdentityCard** service. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md). |
| Authorization | Select **Bearer Token** and provide the Druid Vision **Token**. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md).  ![](../Resources/Images/vision/new%20ro%20id%20auth.png) |
| Headers | Content-Type: “multipart/form-data”  ![](../Resources/Images/vision/new%20ro%20id%20headers.png) |
| Body without face validation | “file”: <attached document file> (file attachment). Add two separate PDF files, each containing one side of the identity card.  Supported formats: png, jpg, pdf.  ![](../Resources/Images/vision/new%20ro%20id%20files.png)  **NOTE:** In Druid versions prior to 9.12, add a single PDF file containing both sides of the identity card.  In Druid 9.12 and higher, you can also upload the official address certificate issued by the national authority responsible for population records and identity documents.  **NOTE:** Only original electronic documents downloaded from the Romanian Police Department are accepted. Scans or photos of the document are not allowed. The file must be in PDF format for security reasons.  If extraction fails due to issues like poor image quality, you can skip any of the following validation checks:   - Sex - DateOfBirth - ExpireDate - SIRUTA - to skip Address validation from the identity card back.   Add the **skipValidations** parameter in the request body as many times as validation checks you want to escape from validation.  ![](../Resources/Images/vision/new%20ro%20id%20skip%20valid.png)  **NOTE:** Skipping validations is available in DRUID 8.1 and higher. |
| Body with face validation | “file”: <attached document file> (file attachment). Add the front of the new identity card.  “selfie”: <attached selfie photo> (file attachment)  ![](../Resources/Images/vision/mewro%20id%20with%20selfie.png)  Supported formats: png, jpg, pdf.  **NOTE:** The user needs to smile in the selfie, otherwise the face validation will fail.    **NOTE:** You can skip the same validation checks listed at **Body without face validation**. |

<a id="Response"></a>

## Response

Data Returned by MRZ interpretation is found in the Data section of the response.

Click the desired option below to see the response for the specific request.

## Identity Card without face validation

**Response Example**

```
{
    "ResultId": "ba12ac00-9dc5-497f-ba91-2f57ee8058ae",
    "TemplateName": "New_IdentityCard",
    "Status": "Partial",
    "StatusReason": null,
    "Confidence": 0.77,
    "Data": {
        "AddrLine1": "Mun. Bucuresti Sec.6",
        "AddrLine1.Confidence": 0.99,
        "AddrLine1.Localized": null,
        "AddrLine1.Localized.Confidence": 0,
        "AddrLine2": "Str. Mare nr.12",
        "AddrLine2.Confidence": 0.99,
        "AddrLine2.Localized": null,
        "AddrLine2.Localized.Confidence": 0,
        "AddrLine3": "bl.D1, sc.1",
        "AddrLine3.Confidence": 0.81,
        "AddrLine3.Localized": null,
        "AddrLine3.Localized.Confidence": 0,
        "AddrLine4": "et.2, ap.4",
        "AddrLine4.Confidence": 0.96,
        "AddrLine4.Localized": null,
        "AddrLine4.Localized.Confidence": 0,
        "Apartment": "4",
        "BuildingNo": "",
        "Cetatenie": "ROU",
        "Cetatenie.Confidence": 0.99,
        "City": "Bucuresti",
        "CityType": "Municipiul",
        "CNP": "2830703460094",
        "CNP.Confidence": 0.99,
        "cnp.CountryOfBirth": "Invalid",
        "cnp.CountyOfBirth": "Invalid",
        "cnp.CountyOfBirth.id": 0,
        "cnp.DateOfBirth": "0001-01-01T00:00:00",
        "cnp.Sex": "X",
        "Commune": "",
        "County": "B",
        "County.SirutaId": 403,
        "DateOfBirth": "1983-07-03T00:00:00",
        "DateOfIssue": "02 09 2021",
        "DateOfIssue.Confidence": 0.99,
        "District": "6",
        "DocumentNumber": "SP1234691",
        "DocumentNumber.Confidence": 0.99,
        "Domiciliu": "Mun. Bucuresti Sec.6 Str. Mare nr.12 et.2, ap.4",
        "Domiciliu.Confidence": 0.99,
        "EntranceNo": "",
        "ExpireDate": "2031-09-01T00:00:00",
        "Face": 1,
        "Face.Confidence": 1,
        "FaceSmall": 0,
        "FaceSmall.Confidence": 0,
        "Floor": "2",
        "Issuing Authoriry": "D.E.P.A.B.D.",
        "Issuing Authoriry.Confidence": 0.72,
        "Locality": "",
        "Locality.SirutaId": 179196,
        "LocalityName": "Bucuresti",
        "LocalityType": "Municipiul",
        "MRZ": "IDROUSP12346919<2830703460094<8307037F3109018ROU<<<<<<<<<<<8MANOLE<<CORINA<IOANA<<<<<<<<<<",
        "MRZ.Confidence": 0.96,
        "mrz.CountryCode": "ROU",
        "mrz.DateOfBirth": "1983-07-03T00:00:00Z",
        "mrz.DocumentNumber": "SP1234691",
        "mrz.DocumentSeries": null,
        "mrz.DocumentType": "IdentityCard",
        "mrz.ExpireDate": "2031-09-01T00:00:00Z",
        "mrz.FirstName": "CORINA IOANA",
        "mrz.LastName": "MANOLE",
        "mrz.OptionalData": null,
        "mrz.Sex": "F",
        "MRZ1": "IDROUSP12346919<2830703460094<",
        "MRZ1.Confidence": 0.95,
        "MRZ2": "8307037F3109018ROU<<<<<<<<<<<8",
        "MRZ2.Confidence": 0.98,
        "MRZ3": "MANOLE<<CORINA<IOANA<<<<<<<<<<",
        "MRZ3.Confidence": 0.98,
        "Municipiul.SirutaId": 179132,
        "Number": "1234691",
        "Nume": "MANOLE",
        "Nume.Confidence": 1,
        "Nume.Localized": null,
        "Nume.Localized.Confidence": 0,
        "Prenume": "CORINA IOANA",
        "Prenume.Confidence": null,
        "Prenume1": "CORINA",
        "Prenume1.Confidence": 0.99,
        "Prenume1.Localized": null,
        "Prenume1.Localized.Confidence": 0,
        "Prenume2": "IOANA",
        "Prenume2.Confidence": 0.99,
        "Prenume2.Localized": null,
        "Prenume2.Localized.Confidence": 0,
        "Series": "SP",
        "Sex": "F",
        "Sex.Confidence": 0.99,
        "Smile": "0",
        "StreetName": "Mare",
        "StreetNo": "12",
        "StreetType": "Strada",
        "Village": ""
    },
    "ValidationResult": {
        "DateOfBirth": {
            "Status": "Invalid",
            "Description": "[DateOfBirth] field does not equal [cnp.DateOfBirth]"
        },
        "CNP": {
            "Status": "Invalid",
            "Description": null
        },
        "ExpireDate": {
            "Status": "Valid",
            "Description": null
        },
        "Sex": {
            "Status": "Invalid",
            "Description": "[Sex] field does not equal [cnp.Sex]"
        },
        "MRZ": {
            "Status": "Valid",
            "Description": null
        },
        "SIRUTA": {
            "Status": "Valid",
            "Description": null
        }
    }
}
```

## Identity Card with face validation

**Response Example**

```
{
    "ResultId": "53caa06f-3cdb-4ee4-80ef-5d5cb2b061dc",
    "TemplateName": "New_IdentityCard",
    "Status": "Partial",
    "StatusReason": null,
    "Confidence": 0.69,
    "Data": {
        "Cetatenie": "ROU",
        "Cetatenie.Confidence": 0.99,
        "CNP": "2830703460094",
        "CNP.Confidence": 0.99,
        "cnp.CountryOfBirth": "Invalid",
        "cnp.CountyOfBirth": "Invalid",
        "cnp.CountyOfBirth.id": 0,
        "cnp.DateOfBirth": "0001-01-01T00:00:00",
        "cnp.Sex": "X",
        "DateOfBirth": "1983-07-03T00:00:00",
        "DocumentNumber": "SP1234691",
        "DocumentNumber.Confidence": 0.99,
        "ExpireDate": "2031-09-01T00:00:00",
        "Face": 1,
        "Face.Confidence": 1,
        "Number": "1234691",
        "Nume": "MANOLE",
        "Nume.Confidence": 1,
        "Nume.Localized": null,
        "Nume.Localized.Confidence": 0,
        "Prenume": "CORINA IOANA",
        "Prenume.Confidence": null,
        "Prenume1": "CORINA",
        "Prenume1.Confidence": 0.99,
        "Prenume1.Localized": null,
        "Prenume1.Localized.Confidence": 0,
        "Prenume2": "IOANA",
        "Prenume2.Confidence": 0.99,
        "Prenume2.Localized": null,
        "Prenume2.Localized.Confidence": 0,
        "Series": "SP",
        "Sex": "F",
        "Sex.Confidence": 0.99,
        "Smile": "0"
    },
    "ValidationResult": {
        "DateOfBirth": {
            "Status": "Invalid",
            "Description": "[DateOfBirth] field does not equal [cnp.DateOfBirth]"
        },
        "CNP": {
            "Status": "Invalid",
            "Description": null
        },
        "ExpireDate": {
            "Status": "Valid",
            "Description": null
        },
        "Face": {
            "Status": "Invalid",
            "Description": "Expecting one face in selfie image"
        },
        "Sex": {
            "Status": "Invalid",
            "Description": "[Sex] field does not equal [cnp.Sex]"
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

To ensure optimal OCR results, the API automatically enhances the image before processing by applying multiple image optimization algorithms.

Supported formats: PNG, JPG, PDF.
