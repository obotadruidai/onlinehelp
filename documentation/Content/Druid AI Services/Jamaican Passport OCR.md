<a id="JamaicanPassportOCR"></a>

# Jamaican Passport OCR

The Druid API engine performs OCR and data extraction from Jamaican passports.

> **NOTE:**
>
> - In order to use this Druid Vision service, contact [Druid Tech Support](<mailto:support@druidai.com?subject=Request: Activate Druid Vision service JAM_Passport>).
> - For any APIs that are used for testing purposes and not in a production environment, Druid CANNOT be held responsible for the security of the processed data under the General Data Protection Regulation (GDPR). We highly recommend you to use sample data and documents for all APIs in testing environments.

<a id="Request"></a>

## Request

|  |  |
| --- | --- |
| Method | POST |
| API Resource URL (Endpoint) | The endpoint of the Druid Vision **JAM\_Passport** service. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md). |
| Authorization | Select **Bearer Token** and provide the Druid Vision **Token**. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md).  ![](../Resources/Images/vision/jam%20pass%20auth.png) |
| Headers | Content-Type: “multipart/form-data”  ![](../Resources/Images/vision/jamaican%20pass%20multipart.png) |
| Body without face validation | “file”: <attached document file> (file attachment).  Supported formats: png, jpg, pdf.  ![](../Resources/Images/vision/jam%20pass%20body.png)  If extraction fails due to issues like poor image quality, you can skip any of the following validation checks:   - DateOfBirth - Validity - IssueDate - Sex   Add the **skipValidations** parameter in the request body as many times as validation checks you want to escape from validation.  ![](../Resources/Images/vision/JAM_Passport%20valid.png)  **NOTE:** Skipping validations is available in DRUID 8.1 and higher. |
| Body with face validation | “file”: <attached document file> (file attachment)  “selfie”: <attached selfie photo> (file attachment)  Supported formats: png, jpg, pdf.  **NOTE:** The user needs to smile in the selfie, otherwise the face validation will fail. |

<a id="Response"></a>

## Response

Data Returned by MRZ interpretation is found in the Data section of the response.

**Response Example**

```
{
     "ResultId": "9d995aec-91ee-4e16-9e71-581d4c7767ea",
     "TemplateName": "JAM_Passport",
     "Status": "Complete",
     "StatusReason": null,
     "Confidence": 0.92,
     "Data": {
        "Type": "P",
        "IssueState": "JAM",
        "DocumentNumber": "xxxxxxxx",
        "LastName": "SEVILLE",
        "FirstName": "xxxxxxxxx xxxxx xxxxxx xx xxxxxxx",
        "Citizenship": "JAMAICAN",
        "DateOfBirth": "06.07.1982",
        "Occupation": "IT MANAGER",
        "Sex": "M",
        "PlaceOfBirth": "ST ANDREW, JAM",
        "PlaceOfIssue": "KINGSTON",
        "IssueDate": "10.08.2015",
        "DateOfExpiry": "09.08.2025",
        "MRZ1": "P<xxxxxxxxx<<xxxxx<xxxxxx<xx<xxxxxxx<<<<<<",
        "MRZ2": "xxxxxxxx<7JAM8207067M2508094BY7985<<<<<<<<88",
        "MRZ": "P<xxxxxxxxx<<xxxxx<xxxxxx<xx<xxxxxxx<<<<<<xxxxxxxx<7JAM8207067M2508094BY7985<<<<<<<<88",
        "Face": 1.0,
        "FullName": "xxxxxxxxx xxxxx xxxxxx xx xxxxxxx",
        "Type.Confidence": 0.99,
        "IssueState.Confidence": 1.0,
        "DocumentNumber.Confidence": 1.0,
        "LastName.Confidence": 1.0,
        "FirstName.Confidence": 0.99,
        "Citizenship.Confidence": 0.99,
        "DateOfBirth.Confidence": 0.99,
        "Occupation.Confidence": 1.0,
        "Sex.Confidence": 0.97,
        "PlaceOfBirth.Confidence": 1.0,
        "PlaceOfIssue.Confidence": 0.99,
        "IssueDate.Confidence": 0.99,
        "DateOfExpiry.Confidence": 0.99,
        "MRZ1.Confidence": 0.94,
        "MRZ2.Confidence": 0.93,
        "MRZ.Confidence": 0.94,
        "Face.Confidence": 1.0,
        "FullName.Confidence": null,
        "mrz.CountryCode": "JAM",
        "mrz.DateOfBirth": "1982-07-06T00:00:00Z",
        "mrz.DocumentSeries": null,
        "mrz.DocumentNumber": "xxxxxxxx",
        "mrz.DocumentType": "Passport",
        "mrz.ExpireDate": "2025-08-09T00:00:00Z",
        "mrz.FirstName": "xxxxxxxxx xxxxx xxxxxx xx xxxxxxx",
        "mrz.LastName": "xxxxxxx",
        "mrz.Sex": "M",
        "mrz.OptionalData": "BY7985",
        "Smile": "0"
     },
     "ValidationResult": {
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
        "Validity": {
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

- If Code = “ID” and Nationality = “JAM”, the template “JAM\_Passport” is used.

The results of the JAM\_Passport template provide the following validations:

- **Validity** - Status Invalid if the OCR service fails to retrieve information in **IssueDate** and **ExpiryDate**.
- **MRZ** - Status Invalid if at least one of the cross-checks on the MRZ field fails (document number, date of birth, date of expiry, sex, IssuingState).
- **Sex** - Status Invalid if the cross-check of the following fields fail: Sex from Document, Sex from MRZ.
- **DateOfBirth** - Status Invalid if the cross-check of the following fields fail: DateOfBirth from Document, DateOfBirth from MRZ.
- **IssueDate** - Status Invalid if the cross-check of the following fields fail: IssueDate from Document, IssueDate from MRZ.
- **ExpireDate** - Status Invalid if the cross-check of the following fields fail: ExpireDate from Document, ExpireDate from MRZ.
- **SIRUTA** - Status Invalid if the value of field Locality cannot be matched to the SIRUTA dictionary.
- **Face** - Status Invalid if the "Face.Confidence" is not 1.0 or "Invalid: you forgot to smile" if the customer is not smiling in the selfie. This validation is done for OCR of Jamaican passports with selfie.

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
