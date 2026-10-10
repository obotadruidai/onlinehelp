---
title: "Romanian Living Permit OCR"
---

<a id="RomanianLivingPermitOCR"></a>


The Druid API engine performs OCR and data extraction from Romanian living permits.

{% hint style="info" %}
**NOTE:**

- In order to use this Druid Vision service, contact [Druid Tech Support](<mailto:support@druidai.com?subject=Request: Activate Druid Vision service RO_LivingPermit>).
- For any APIs that are used for testing purposes and not in a production environment, Druid CANNOT be held responsible for the security of the processed data under the General Data Protection Regulation (GDPR). We highly recommend you to use sample data and documents for all APIs in testing environments.
{% endhint %}

<a id="Request"></a>

## Request

|  |  |
| --- | --- |
| Method | POST |
| API Resource URL (Endpoint) | The endpoint of the Druid Vision RO\_LivingPermit service. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md). |
| Headers | Authorization: “Bearer <your bearer token>”  Content-Type: “multipart/form-data”  ![](../Resources/Images/OCR%20ID/permit%20headers.png) |
| Authorization | Select **Bearer Token** and provide the Druid Vision **Token**. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md).  ![](../Resources/Images/OCR%20ID/living%20permit%20auth.png) |
| Body | - “file”: <attached front of the RO live permit>. - “file”: <attached back of the RO live permit>   Supported formats: png, jpg, pdf.  ![](../Resources/Images/OCR%20ID/livepermit.png)  If extraction fails due to issues like poor image quality, you can skip any of the following validation checks:   - ValidTo - ValidFrom - SIRUTA - to skip the PlaceOfPrint validation - DateOfBirth - Sex - DocNumber - to skip the DocNumber validation from the MRZ cross check   Add the **skipValidations** parameter in the request body as many times as validation checks you want to escape from validation.  ![](../Resources/Images/vision/living%20permit%20valid.png)  **NOTE:** Skipping validations is available in DRUID 8.1 and higher. |

<a id="ResponseforoldRomanianlivingpermits"></a>

## Response - for old Romanian living permits

**Response Example**

```
{
        "TemplateName": "RO_LivingPermit",
        "Status": "Partial",
        "StatusReason": null,
        "Confidence": 0.7,
        "Data": {
            "PermitSeries": "ROXXXXXXX",
            "LastName": "XXXXX",
            "FirstName": "XXXX",
            "FullName": "XXXXX XXXX",
            "ValidTo": "XX.XX.XXXX",
            "ValidFrom": "XX.XX.XXXX",
            "PlaceOfPrint": "XXXXXX",
            "PermitType": "PERMIS DE SEDERE TEMPORARA XX XX",
            "Observations_Front": "XXXXXXXXXXXXXXXXXXXX XXXXXXXXX",
            "PermitSeries.Confidence": 0.68,
            "LastName.Confidence": 0.98,
            "FirstName.Confidence": 0.95,
            "FullName.Confidence": null,
            "ValidTo.Confidence": 0.92,
            "ValidFrom.Confidence": 0.96,
            "PlaceOfPrint.Confidence": 0.98,
            "PermitType.Confidence": 0.64,
            "Observations_Front.Confidence": 0.98,
            "DateOfBirth": "U SU IVE LULU #12 02/1995 SU EU ELFEU EU FU EU EU EU EU",
            "PlaceOfBirth": "EU EU EU EU EU FU EU EU FU EU EU EU NIGERIA EU EU EU EU EU EU EU FU EU EU EU EU EU EU GU EU EU EO P EU EU EU EU EU EU EU EU EU SU PU TO EU TU EU EU EU EU EU EU EU EU EU EU EU EU EU EU FU EU EU EU",
            "Sex": "LIEU EULIEU EU EU EU EU EU EU",
            "Citizenship": "EU LU EU EU EU EU EU EU EU EU LU EU FU EU EU EU EU EU EU EU EU EU EU EU EU EU EU FU EU FU EU EU EU EU EU EU EU EU EU EU EU EU EU EU KU EU EU TU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU CO EU EU EL EU ED EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU LO EU LU EU EU FU FU EU TU EU EU ED EU EU EU CU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU FU FU SU EU SU. EU",
            "Observations_Back": "EU EU EU EU EU EV EU EU EU EU EU EU EU EU EU EU EU FU FU BU EU FUFU EU EU EU : Constanta Stry O EU EU EU EU EU EU EU EU EU EU U EU EU EU EU EU FU EU EU EU PEU EU EU LU EU EU EU EU EU EU EU EU EU EO GILZU EU EU EU EU EU EU EU LU ZU EU EU EU EU ELEU EN € EU EU EU EU EU EU DU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU LU EU EU EU EU EU EU EU EU EU EU EU EU EU EU CU EN EV EU EU EU EU EU EU EU EU RU EU EU EU EU EU EU EO EU EU EU EU EU EU EU EM EU EU EU SU EU EU EU EU EU EU EU EU EU EU EU EU EU EU O EU EU TU TU TU TU TU ED FU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EU EM EU FU FU EU EU EU EU EU EU EU EU EU EU EU EU EU FU EU FU EU EU EU EU EU EU EU LO EU EU EU EU EU EU EU EU EU EU EM EU EU EU EU EU SU EH EH EH EH EH EN EN EU EU EU EU EU EO LO BU EU EU FU FU EU PU EU EU EU FU EU EU EU EU EU FU EM EM EN SU",
            "MRZ": "IRROUR005615723<<<<<<<<<<<<<<<9502127M2011013NGA<<<<<<<<<<<0ADUEZE<<EMMANUEL<WERIDONGHA<<<",
            "DateOfBirth.Confidence": 0.56,
            "PlaceOfBirth.Confidence": 0.36,
            "Sex.Confidence": 0.56,
            "Citizenship.Confidence": 0.59,
            "Observations_Back.Confidence": 0.51,
            "MRZ.Confidence": 0.56
        },
        "ValidationResult": {
            "ValidTo": {
                "Status": "Invalid",
                "Description": "[ValidTo] document is expired"
            },
            "ValidFrom": {
                "Status": "Valid"
            },
            "DateOfBirth": {
                "Status": "Invalid",
                "Description": "Missing [DateOfBirth] field in result data"
            },
            "SIRUTA": {
                "Status": "Invalid",
                "Description": "Missing [PlaceOfPrint] field in result data"
            },
            "Sex": {
                "Status": "Invalid",
                "Description": "[Sex] field was not read correctly"
            }
        }
 }
```

<a id="ResponsefornewRomanianlivingpermits"></a>

## Response - for new Romanian living permits

The ValidationResult object in the OCR response performs real-time cross-checks on the extracted fields from the Romanian living permit. A validation is considered "Valid" if the extracted information matches the control standards or successfully cross-references with other document sections (such as the Machine Reading Zone - MRZ).

**Response Example**

```
{
    "TemplateName": "RO_LivingPermit",
    "Status": "Partial",
    "StatusReason": null,
    "Confidence": 0.7,
    "Data": {
        "Authority": "I.G. T.",
        "Authority.Confidence": 0.21,
        "Citizenship": "UTO",
        "Citizenship.Confidence": 1.0,
        "DateOfBirth": "1990-01-01T00:00:00",
        "DocumentNumber": "900000114",
        "DocumentNumber.Confidence": 0.99,
        "FirstName1": "Livia",
        "FirstName1.Confidence": 1.0,
        "FirstName2": "Cristina",
        "FirstName2.Confidence": 1.0,
        "FullName": "Livia Cristina POPESCU IONESCU",
        "FullName.Confidence": null,
        "LastName": "POPESCU IONESCU",
        "LastName.Confidence": 0.99,
        "MRZ": null,
        "MRZ.Confidence": null,
        "mrz.CountryCode": null,
        "mrz.DateOfBirth": null,
        "mrz.DocumentNumber": null,
        "mrz.DocumentSeries": null,
        "mrz.DocumentType": null,
        "mrz.ExpireDate": null,
        "mrz.FirstName": null,
        "mrz.LastName": null,
        "mrz.OptionalData": null,
        "mrz.Sex": null,
        "MRZ1": "IRROU9O00001147<<<<<<<<<<<<<<<",
        "MRZ1.Confidence": 0.86,
        "MRZ2": "9001011F2505174UTO<<<<<<<<<<<0",
        "MRZ2.Confidence": 0.81,
        "MRZ3": "POPESCU<IONESCU<<LIVIA<CRISTIN",
        "MRZ3.Confidence": 0.95,
        "Observations_Back1": "Mun. Arad Str Craciunite Nr. 5",
        "Observations_Back1.Confidence": 0.76,
        "Observations_Back2": "Bl.1 Sc.2 Ap.3 Jud. Arad",
        "Observations_Back2.Confidence": 0.65,
        "Observations_Back3": "DREPT DE MUNCA",
        "Observations_Back3.Confidence": 0.99,
        "Observations_Front": "CNP 8000000000001",
        "Observations_Front.Confidence": null,
        "Observations_Front1": "CNP 8000000000001",
        "Observations_Front1.Confidence": 0.99,
        "Observations_Front2": "",
        "Observations_Front2.Confidence": null,
        "PermitType": "PERMIS DE SEDERE PE TERMEN LUNG",
        "PermitType.Confidence": null,
        "PermitType1": "PERMIS DE SEDERE",
        "PermitType1.Confidence": 0.99,
        "PermitType2": "PE TERMEN LUNG",
        "PermitType2.Confidence": 0.99,
        "PlaceOfBirth": "UTOPIAJEU",
        "PlaceOfBirth.Confidence": 0.34,
        "PlaceOfPrint": "Bucuresti",
        "PlaceOfPrint.Confidence": 0.97,
        "Sex": "F",
        "Sex.Confidence": 0.94,
        "ValidFrom": "2020-05-04T00:00:00",
        "ValidTo": "2025-05-17T00:00:00"
    },
    "ValidationResult": {
        "ValidFrom": {
            "Status": "Valid"
        },
        "MRZ": {
            "Status": "Invalid"
        },
        "DateOfBirth": {
            "Status": "Valid"
        },
        "ValidTo": {
            "Status": "Valid"
        },
        "CrossCheck_DocSeriesNumber": {
            "Status": "Valid"
        }
        
        "MRZ": {
            "Status": "Valid"
          },
 
          "ValidTo": {
            "Status": "Valid"
          },
          "Sex": {
                "Status": "Valid"
          },
          "CNP": {
            "Status": "Valid"
          }
    }
}
```
