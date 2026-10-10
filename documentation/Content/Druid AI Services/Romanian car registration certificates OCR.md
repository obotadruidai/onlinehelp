<a id="RomanianCarRegistrationCertificatesOCR"></a>

# Romanian Car Registration Certificates OCR

The Druid API engine performs OCR and data extraction from Romanian car registration certificates.

> **NOTE:**
>
> - In order to use this Druid Vision service, contact [Druid Tech Support](<mailto:support@druidai.com?subject=Request: Activate Druid Vision service RO_RegistrationCertificate>).
> - For any APIs that are used for testing purposes and not in a production environment, Druid CANNOT be held responsible for the security of the processed data under the General Data Protection Regulation (GDPR). We highly recommend you to use sample data and documents for all APIs in testing environments.

<a id="Request"></a>

## Request

|  |  |
| --- | --- |
| Method | POST |
| API Resource URL (Endpoint) | The endpoint of the Druid Vision **RO\_RegistrationCertificate** service. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md). |
| Authorization | Select **Bearer Token** and provide the Druid Vision **Token**. For information on how to get the endpoint, see [Druid Vision](Druid%20Vision.md).  ![](../Resources/Images/OCR%20ID/car%20auth.png) |
| Headers | Content-Type: “multipart/form-data”  ![](../Resources/Images/OCR%20ID/car%20headers.png) |
| Body | “file”: <attached document file> (file attachment). Add both pages of the car registration certificate.  Supported formats: png, jpg, pdf.  ![](../Resources/Images/OCR%20ID/car.png)  If extraction fails due to issues such as poor image quality, you can skip the IssuerIBAN validation by including the parameter **skipValidations** = **NumarTalon** in the request body.  **NOTE:** Skipping validations is available in DRUID version 8.1 and higher. |

<a id="Response"></a>

## Response

**Response Example**

```
{
    "ResultId": "2717947d-d263-4d97-9e46-d7901f5450c0",
    "TemplateName": "RO_RegistrationCertificate",
    "Status": "Complete",
    "StatusReason": null,
    "Confidence": 0.97,
    "Data": {
        "AdresaProprietar1": "Bdul EXPOZITIEI Nr.2 mun",
        "AdresaProprietar1.Confidence": 0.96,
        "AdresaProprietar2": "BUCURESTI SECTORUL 1",
        "AdresaProprietar2.Confidence": 0.99,
        "AdresaProprietar3": "",
        "AdresaProprietar3.Confidence": null,
        "AdresaUtilizator1": "Str. EDEREI Nr.21 com",
        "AdresaUtilizator1.Confidence": 0.99,
        "AdresaUtilizator2": "CORBEANCA sat TAMASI Jud.",
        "AdresaUtilizator2.Confidence": 0.98,
        "AdresaUtilizator3": "ILFOV",
        "AdresaUtilizator3.Confidence": 0.99,
        "CapacitateCilindrica": "2143",
        "CapacitateCilindrica.Confidence": 0.99,
        "Clasa": "AUTOTURISM M1",
        "Clasa.Confidence": 0.98,
        "Combustibil": "MOTORINA",
        "Combustibil.Confidence": 0.99,
        "Culoare": "GRI",
        "Culoare.Confidence": 1,
        "D2Field": "245 G 23S2P2",
        "D2Field.Confidence": 0.99,
        "DataEmitereTalon": "12.09.2018",
        "DataEmitereTalon.Confidence": 0.99,
        "DataTalon": "11.01.2018",
        "DataTalon.Confidence": 0.99,
        "EmisaDe": "SRPCIV Bucuresti",
        "EmisaDe.Confidence": 0.99,
        "MasaIncarcata": "2015",
        "MasaIncarcata.Confidence": 0.99,
        "MasaVehicol": "1525",
        "MasaVehicol.Confidence": 0.99,
        "Model": "CLA 220 D",
        "Model.Confidence": 0.98,
        "NrInmatriculare": "B-112-BOG",
        "NrInmatriculare.Confidence": 0.99,
        "NrTalonP1": "B04097059",
        "NrTalonP1.Confidence": 0.96,
        "NrTalonP2": "B04097059",
        "NrTalonP2.Confidence": 0.99,
        "NumarCarteIdentitate": "N107680",
        "NumarCarteIdentitate.Confidence": 0.99,
        "NumarIdentificare": "e1*2001/116*0470*16",
        "NumarIdentificare.Confidence": 0.49,
        "NumarLocuri": "5",
        "NumarLocuri.Confidence": 0.99,
        "NumarTalon": "B04097059",
        "NumeProprietar1": "TIRIAC LEASING IFN SA",
        "NumeProprietar1.Confidence": 0.98,
        "NumeProprietar2": "",
        "NumeProprietar2.Confidence": null,
        "ObsLine1": "MASA MAX TEHN ADM A ANS DE",
        "ObsLine1.Confidence": 0.98,
        "ObsLine2": "VEH 3555 KG NOT VALID FOR SALE",
        "ObsLine2.Confidence": 0.99,
        "ObsLine3": "OR REGISTRATION ABROAD",
        "ObsLine3.Confidence": 0.99,
        "PrenumeProprietar1": "",
        "PrenumeProprietar1.Confidence": null,
        "PrenumeProprietar2": "",
        "PrenumeProprietar2.Confidence": null,
        "PrimaInmatriculare": "26.09.2016",
        "PrimaInmatriculare.Confidence": 0.99,
        "Producator": "MERCEDES-BENZ",
        "Producator.Confidence": 0.99,
        "Putere": "130",
        "Putere.Confidence": 1,
        "SerieSasiu": "WDD1173031N395659",
        "SerieSasiu.Confidence": 0.99,
        "Utilizator": "DOX SOFTWARE SRL",
        "Utilizator.Confidence": 0.99
    },
    "ValidationResult": {
        "NumarTalon": {
            "Status": "Valid",
            "Description": null
        }
    }
}
```
