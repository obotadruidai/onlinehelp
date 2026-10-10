<a id="AustraliaNewSouthWalesDrivingLicense"></a>

# Australia New South Wales Driving License

The Druid API engine supports OCR and data extraction for driving licenses issued by Australia New South Wales.

> **NOTE:**
>
> - In order to use this Druid Vision service, contact [Druid Tech Support](<mailto:support@druidai.com?subject=Request: Activate Druid Vision service JAM_VotersId>).
> - For any APIs that are used for testing purposes and not in a production environment, Druid CANNOT be held responsible for the security of the processed data under the General Data Protection Regulation (GDPR). We highly recommend you to use sample data and documents for all APIs in testing environments.

<a id="Request"></a>

## Request

|  |  |
| --- | --- |
| Method | POST |
| API Resource URL (Endpoint) | The endpoint of the Druid Vision **AU\_NSW\_DL** service. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md). |
| Authorization | Select **Bearer Token** and provide the Druid Vision **Token**. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md).  ![](../Resources/Images/vision/au%20auth.png) |
| Headers | Content-Type: “multipart/form-data”  ![](../Resources/Images/vision/au%20headers.png) |
| Body | “file”: <attached document file> (file attachment).  Supported formats: png, jpg, pdf.  ![](../Resources/Images/vision/au%20body.png) |

<a id="Response"></a>

## Response

Data Returned by MRZ interpretation is found in the Data section of the response.

**Response Example**

```
{
    "ResultId": "9bdc5e64-a666-4860-b647-ee4cc1b5814e",
    "TemplateName": "AU_NSW_DL",
    "Status": "Complete",
    "StatusReason": null,
    "Confidence": 0.59,
    "Data": {
        "Address": "8 PINDARI AVE MOSMAN NSW 2088",
        "Address.Confidence": null,
        "AddressLine1": "8 PINDARI AVE",
        "AddressLine1.Confidence": 0.99,
        "AddressLine2": "MOSMAN NSW 2088",
        "AddressLine2.Confidence": 0.99,
        "CardNumber": "2 035 446 985",
        "CardNumber.Confidence": 0.99,
        "DateOfBirth": "1957-05-12T00:00:00",
        "ExpiryDate": "2020-09-15T00:00:00",
        "FirstName": "Angelo Franco",
        "FullName": "Angelo Franco CANEPA",
        "FullName.Confidence": null,
        "FullName1": "Angelo Franco CANEPA",
        "FullName1.Confidence": 0.99,
        "FullName2": "",
        "FullName2.Confidence": null,
        "LastName": "CANEPA",
        "LicenseClass": "C",
        "LicenseClass.Confidence": 0.99,
        "LicenseNumber": "13511698 ath Wales",
        "LicenseNumber.Confidence": 0.32
    },
    "ValidationResult": {
        "DateOfBirth": {
            "Status": "Valid",
            "Description": null
        },
        "ExpiryDate": {
            "Status": "Valid",
            "Description": null
        }
    }
}
```
