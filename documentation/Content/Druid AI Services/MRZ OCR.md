<a id="MachineReadingZoneOCR"></a>

# Machine Reading Zone OCR

The Druid API engine performs OCR and data extraction from documents which contain Machine Reading Zone (MRZ), such as Romanian identity cards (both old and new), living permits, passports and residence cards.

> **NOTE:**
>
> - In order to use this Druid Vision service, contact [Druid Tech Support](<mailto:support@druidai.com?subject=Request: Activate Druid Vision service MRZ>).
> - For any APIs that are used for testing purposes and not in a production environment, Druid CANNOT be held responsible for the security of the processed data under the General Data Protection Regulation (GDPR). We highly recommend you to use sample data and documents for all APIs in testing environments.

<a id="Request"></a>

## Request

|  |  |
| --- | --- |
| Method | POST |
| API Resource URL (Endpoint) | The endpoint of the Druid Vision MRZ service. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md). |
| Authorization | Select **Bearer Token** and provide the Druid Vision **Token**. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md).  ![](../Resources/Images/OCR%20ID/mrz%20auth.png) |
| Headers | Content-Type: “multipart/form-data”  ![](../Resources/Images/OCR%20ID/mrz%20headers.png) |
| Body without face validation | “file”: <attached document file> (file attachment).  Supported formats: png, jpg, pdf.  ![](../Resources/Images/OCR%20ID/mrz.png) |

<a id="Response"></a>

## Response

Data Returned by MRZ interpretation is found in the Data section of the response.

Click the desired option below to see the response for the specific request.

## Identity Cards

**Response Example**

```
Identity Cards [
{
    "DocumentData": {
          "TemplateName": "IdentityCard",
          "Status": "Complete",
          "StatusReason": null,
          "Confidence": 0.8,
          "Data": {
                "Seria": "XX",
                "NR": "XXXXXX",
                "Sex": "X",
                "CNP": "XXXXXXXXXXXXX",
                "Nume": "XXXXX",
                "Prenume": "XXXX",
                "Cetatenie": "Romana / ROU",
                "Loc nastere": "Jud.XX Mun.XXXX",
                "AddrLine1": "Mun.XXXX",
                "AddrLine2": "Str. XX XXX nr.XX sc.X et.X ap.X",
                "Emisa de": "XXX XX",
                "Validity": "XX.XX.XX-XX.XX.XXXX",
                "MRZ1": "IDROUXXXXX<<XXXX<<<<<<<<<<<",
                "MRZ2": "XXXXXXXX<XROUXXXXXXXXXXXXXXXXXXXX",
                "MRZ": "IDROUXXXXX<<XXXX<<<<<<<<<<<XXXXXXXX<XROUXXXXXXXXXXXXXXXXXXXX",
                "Face": 1.0,
                "FaceSmall": 0.0,
                "Domiciliu": "Mun.XXXX Str. XX XXX nr.XX sc.X et.X ap.X",
                "Seria.Confidence": 0.99,
                "NR.Confidence": 0.98,
                "Sex.Confidence": 0.99,
                "CNP.Confidence": 0.98,
                "Nume.Confidence": 0.96,
                "Prenume.Confidence": 0.99,
                "Cetatenie.Confidence": 0.75,
                "Loc nastere.Confidence": 0.89,
                "AddrLine1.Confidence": 0.95,
                "AddrLine2.Confidence": 0.93,
                "Emisa de.Confidence": 0.98,
                "Validity.Confidence": 0.96,
                "MRZ1.Confidence": 0.74,
                "MRZ2.Confidence": 0.64,
                "MRZ.Confidence": 0.69,
                "Face.Confidence": 1.0,
                "FaceSmall.Confidence": 0.0,
                "Domiciliu.Confidence": 0.94,
                "DateOfBirth": "XX.XX.XXXXT00:00:00Z",
                "cnp.DateOfBirth": "XX.XX.XXXXT00:00:00Z",
                "cnp.Sex": "X",
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
                "ExpireDate": "XX.XX.XXXXT00:00:00Z",
                "IssueDate": "XX.XX.XXXXT00:00:00Z",
                "mrz.CountryCode": "ROU",
                "mrz.DateOfBirth": "XX.XX.XXXXT00:00:00Z",
                "mrz.DocumentSeries": "XX",
                "mrz.DocumentNumber": "XXXXXX",
                "mrz.DocumentType": "IdentityCard",
                "mrz.ExpireDate": "XX.XX.XXXXT00:00:00Z",
                "mrz.FirstName": "XXXX",
                "mrz.LastName": "XXXXX",
                "mrz.Sex": "X",
                "Smile": "0",
                "County": "B",
                "City": "XXXX",
                "CityType": "XXX",
                "Locality": "",
                "Village": "",
                "Commune": "",
                "StreetType": "XXX",
                "StreetName": "XXXXXXXX",
                "StreetNo": "XX",
                "BuildingNo": "",
                "EntranceNo": "X",
                "Floor": "X",
                "Apartment": "X",
                "District": "X",
                "LocalityType": "Municipiul",
                "LocalityName": "XXXXXXXXXX",
                "County.SirutaId": 403,
                "Locality.SirutaId": XXXXXX
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
                },
                "CrossCheck_DocSeriesNumber": {
                    "Status": "Valid"
                }
        }
    },
    "ResultId": "XXXXXX-fXXXX-XXXX-XXXX-XXXXXXXX",
        "Status": "Complete",
        "StatusReason": null,
        "Confidence": 0.999257142857143,
        "Data": {
                "Code": "ID",
                "IssuingState": "ROU",
                "LastName": "XXXXX",
                "FirstName": "XXXX",
                "DocNumber": "XXXXXXXX",
                "Nationality": "ROU",
                "DateOfBirth": "XX/XX/XXXX",
                "Sex": "X",
                "DateOfExpiry": "XX/XX/XXXX",
                "OptionalData": "XXXXXXX"
        },
        "Validation": {
                "DocNumber": true,
                "DateOfBirth": true,
                "DateOfExpiry": true,
                "Line_2": true,
                "Sex": true,
                "DBirthVsDExpiry": true
        },
        "FieldsConfidence": {
                "Code": 0.9973,
                "IssuingState": 0.9944,
                "LastName": 0.9986,
                "FirstName": 0.9997,
                "DocNumber": 0.9999,
                "Nationality": 0.9999,
                "DateOfBirth": 1.0,
                "Sex": 1.0,
                "DateOfExpiry": 1.0,
                "OptionalData": 0.9998
        }
}
]
```

<a id="Passports"></a>

## Passports

**Response Example**

```
Passports [
    {
        "DocumentData": null,
        "ResultId": "xxxxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
        "Status": "Complete",
        "StatusReason": null,
        "Confidence": 0.9657466666666668,
        "Data": {
                "Code": "xx",
                "IssuingState": "ROU",
                "LastName": "xxxxx",
                "FirstName": "xxxx",
                "DocNumber": "xxxxxxxxx",
                "Nationality": "ROU",
                "DateOfBirth": "xx/xx/xxxx",
                "Sex": "x",
                "DateOfExpiry": "xx/xx/xxxx",
                "OptionalData": "xxxxxxxxxxxxxxxx"
        },
        "Validation": {
                "DocNumber": true,
                "DateOfBirth": true,
                "DateOfExpiry": true,
                "OptionalData": true,
                "Line_2": true,
                "Sex": true,
                "DBirthVsDExpiry": false
        },
        "FieldsConfidence": {
                "Code": 0.9998,
                "IssuingState": 0.9972,
                "LastName": 0.53,
                "FirstName": 0.9885,
                "DocNumber": 0.9984,
                "Nationality": 0.9881,
                "DateOfBirth": 0.9999,
                "Sex": 1.0,
                "DateOfExpiry": 0.9944,
                "OptionalData": 0.9902
         }
    }
 ]
```

<a id="Validations"></a>

### Validations

Validations performed in the MRZ section:

- **DocumentNumber** - checksum cross-checked with MRZ Line\_2 first control digit.
- **DateOfBirth** - checksum cross-checked with MRZ Line\_2 second control digit.
- **ExpireDate** - checksum cross-checked with MRZ Line\_2 third control digit.
- **Line\_2** - checksum of the entire MRZ line 2 (if any of the above fails, the entire line fails and the entire MRZ checksum fails).
- **Sex** - validation on values “F” or “M”.
- **DBirthVsDExpiry** - checks if the identity card has expired.
- **CrossCheck\_DocSeriesNumber** - Crosschecks the document serial number versus the one in the MRZ line. The validation is done for Identity cards only.
