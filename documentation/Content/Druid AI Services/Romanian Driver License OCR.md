<a id="RomanianDriverLicenseOCR"></a>

# Romanian Driver License OCR

The Druid API engine performs OCR and data extraction from Romanian driver licenses.

> **NOTE:**
>
> - In order to use this Druid Vision service, contact [Druid Tech Support](<mailto:support@druidai.com?subject=Request: Activate Druid Vision service RO_DriverLicense>).
> - For any APIs that are used for testing purposes and not in a production environment, Druid CANNOT be held responsible for the security of the processed data under the General Data Protection Regulation (GDPR). We highly recommend you to use sample data and documents for all APIs in testing environments.

<a id="Request"></a>

## Request

|  |  |
| --- | --- |
| Method | POST |
| API Resource URL (Endpoint) | The endpoint of the Druid Vision RO\_DriverLicense service. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md). |
| Headers | Authorization: “Bearer <your bearer token>”  Content-Type: “multipart/form-data”  ![](../Resources/Images/OCR%20ID/driver%20headers.png) |
| Authorization | Select **Bearer Token** and provide the Druid Vision **Token**. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md).  ![](../Resources/Images/OCR%20ID/driver%20license%20auth.png) |
| Body | “file”: <attached document file> (file attachment).  Supported formats: png, jpg, pdf.  ![](../Resources/Images/OCR%20ID/driver%20license.png)  If extraction fails due to issues like poor image quality, you can skip any of the following validation checks:   - BirthDate - ValidityStartDate - ValidityEndDate - Categories   Add the **skipValidations** parameter in the request body as many times as validation checks you want to escape from validation.  ![](../Resources/Images/vision/skip%20driver%20license%20valid.png)  **NOTE:** Skipping validations is available in DRUID 8.1 and higher. |

<a id="Response"></a>

## Response

**Response Example**

```
{
    "TemplateName": "RO_DriverLicense",
        "Status": "Complete",
        "StatusReason": null,
        "Confidence": 0.86,
        "Data": {
            "LastName": "XXXXXXXXX XXXXXXXX",
            "FirstName": "XXXXXXXXX",
            "FullName": "XXXXXXXXX XXXXXXXXX XXXXXXXX",
            "BirthDate": "XX.XX.XX",
            "BirthCity": "XXXXXXXXXXX, XX",
            "ValidityStartDate": "KCONDUCE XX.XX.XX",
            "ValidityEndDate": "XX.XX.XX.XX",
            "ReleaseInstitution": "SRPCIV XXXXXXXXXXXX",
            "CNP": "XXXXXXXXXXXXX",
            "DocumentNo": "XXXXXXXXX",
            "Categories": "XX XX X",
            "LastName.Confidence": 0.83,
            "FirstName.Confidence": 0.94,
            "FullName.Confidence": null,
            "BirthDate.Confidence": 0.94,
            "BirthCity.Confidence": 0.88,
            "ValidityStartDate.Confidence": 0.56,
            "ValidityEndDate.Confidence": 0.83,
            "ReleaseInstitution.Confidence": 0.96,
            "CNP.Confidence": 0.86,
            "DocumentNo.Confidence": 0.86,
            "Categories.Confidence": 0.95,
            "ReleaseInstitution.Localized": null,
            "ReleaseInstitution.Localized.Confidence": 0.0,
            "DateOfBirth": "XXXX-XX-XXTXX:XX:XXZ",
            "cnp.DateOfBirth": "XXXX-XX-XXTXX:XX:XXZ",
            "cnp.Sex": "M"
        },
        "ValidationResult": {
            "CNP": {
                "Status": "Valid"
            }
       }
}
```
