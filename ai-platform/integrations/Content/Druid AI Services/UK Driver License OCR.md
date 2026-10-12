---
title: UK Driver License OCR
---


The Druid API engine performs OCR and data extraction from UK driver licenses.

{% hint style="info" %}
**NOTE:**

* In order to use this Druid Vision service, contact [Druid Tech Support](../Druid%20AI%20Services/mailto:support@druidai.com).
* For any APIs that are used for testing purposes and not in a production environment, Druid CANNOT be held responsible for the security of the processed data under the General Data Protection Regulation (GDPR). We highly recommend you to use sample data and documents for all APIs in testing environments.
{% endhint %}

## Request

|                             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Method                      | POST                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| API Resource URL (Endpoint) | The endpoint of the Druid Vision UK\_DrivingLicence service. For information on how to get the endpoint, see [Druid Vision](<Druid Vision.md>).                                                                                                                                                                                                                                                                                                                                                                              |
| Headers                     | Authorization: “Bearer ” Content-Type: “multipart/form-data”                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Authorization               | Select **Bearer Token** and provide the Druid Vision **Token**. For information on how to get the endpoint, see [Druid Vision](<Druid Vision.md>).                                                                                                                                                                                                                                                                                                                                                                           |
| Body                        | “file”: (file attachment). Supported formats: png, jpg, pdf. ![](<../../.gitbook/assets/uk driver.png>) If extraction fails due to issues like poor image quality, you can skip any of the following validation checks: - BirthDate - IssueDate - ExpireDate Add the **skipValidations** parameter in the request body as many times as validation checks you want to escape from validation. ![](<../../.gitbook/assets/uk driving license valid.png>) **NOTE:** Skipping validations is available in DRUID 8.1 and higher. |

## Response

**Response Example**

```
{
   "ResultId": "6bf14994-c716-4d6b-a65c-0db42bf8226b",
   "TemplateName": "UK_DrivingLicence",
   "Status": "Complete",
   "StatusReason": null,
   "Confidence": 0.99,
   "Data": {
      "LastName": "MORGAN",
      "FirstName1": "SARAH",
      "FirstName2": "MEREDYTH",
      "FullName": "SARAH MEREDYTH MORGAN",
      "BirthDate": "1976-03-11T00:00:00",
      "BirthCountry": "UNITED KINGDOM",
      "ValidityStartDate": "2021-01-01T00:00:00",
      "ValidityEndDate": "2030-12-31T00:00:00",
      "ReleaseInstitution": "DVLA",
      "DocumentNo": "MORGA753116SM9IJ 35",
      "Address1": "122 BURNS CRESCENT",
      "Address2": "EDINBURGH",
      "Address3": "EH1 9GP",
      "Address": "122 BURNS CRESCENT EDINBURGH EH1 9GP",
      "Categories": "AM/A/B1/B/BE/f/k/l/n/p/q",
      "LastName.Confidence": 1,
      "FirstName1.Confidence": 1,
      "FirstName2.Confidence": 0.99,
      "FullName.Confidence": null,
      "BirthCountry.Confidence": 1,
      "ReleaseInstitution.Confidence": 0.99,
      "DocumentNo.Confidence": 0.97,
      "Address1.Confidence": 0.99,
      "Address2.Confidence": 0.99,
      "Address3.Confidence": 1,
      "Address.Confidence": null,
      "Categories.Confidence": 0.93
   },
   "ValidationResult": {
      "BirthDate": {
         "Status": "Valid"
      },
      "ValidityStartDate": {
         "Status": "Valid"
      },
      "ValidityEndDate": {
         "Status": "Valid"
      }
   }
}
```

## Validations

The results of the UK\_DrivingLicence template provide the following validation:

* **Issue Date**
  * Status Invalid if the ValidityStartDate from Document fails.
* **Expiration Date** - Status Invalid if the ValidityEndDate from Document fails.
* **BirthDate** - Status Invalid if the BirthDate from Document fails.
