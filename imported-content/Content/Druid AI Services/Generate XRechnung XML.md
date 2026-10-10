---
title: "Generate XRechnung XML"
---

<a id="GenerateXRechnungXML"></a>


The generate-xrechnung-xml endpoint allows you to generate an XRechnung-compliant XML invoice based on the provided invoice details. XRechnung is a structured electronic invoicing format that adheres to European e-invoicing standards (EN 16931) and is widely used for business transactions, especially with public sector entities in Germany.

This API converts the invoice details, including buyer, seller, tax information, and trade line items, into a valid Cross Industry Invoice XML document. The generated XML file follows the XRechnung format, ensuring compliance with regulatory requirements and facilitating automated invoice processing.

> **NOTE:**  This feature is available in DRUID 8.9 and higher. To use this Druid Vision service, you must have at least one Identity Vision API service enabled for your tenant. If not, please contact [Druid Tech Support](<mailto:support@druidai.com?subject=Request: Activate Druid Vision service IdentityCard>).

<a id="Request"></a>

## Request

|  |  |
| --- | --- |
| Method | POST |
| API Resource URL (Endpoint) | \*.druidplatform.com/api/document-processing/generate-xrechnung-xml |
| Authorization | Select Bearer Token. If you already have a Druid Vision Token generated for an Identity API service in the Druid Portal, provide that token. For details on obtaining the token, refer to [Druid Vision](Druid%20Vision.md).  If you don't have a token, generate one using the Authentication endpoint from Webhooks. For more information, see [Webhooks](../Webhooks.md). |
| Body | The request body must include invoice details such as including buyer, seller, tax information, and trade line items.  **Request Body General Structure**   ``` {   "documentInfo": {     "invoiceNo": "string",     "invoiceDate": "YYYY-MM-DDTHH:MM:SS.sssZ",     "currencyCode": 0,     "buyer": {       "name": "string",       "city": "string",       "country": 0,       "id": "string"     },     "seller": {       "name": "string",       "city": "string",       "country": 0,       "id": "string"     },     "totals": {       "grandTotalAmount": 0     },     "tradeLineItems": [       {         "name": "string",         "billedQuantity": 0,         "netUnitPrice": 0       }     ]   },   "businessProcess": "string",   "version": 230 } ```   Where:   - `documentInfo`: Contains details about the invoice, such as invoice number, dates, currency, buyer, seller, and trade line items. - `businessProcess`: Specifies the business process ID. - `version`: Specifies the version of the XRechnung format being generated. |

<a id="Response"></a>

## Response

If the request is successful, the API returns an XRechnung-compliant XML document, structured according to the Cross Industry Invoice (CII) standard. The response contains details such as:

The `ExchangedDocument` section contains invoice metadata such as the invoice number and issue date.

The `SupplyChainTradeTransaction` section lists the included trade line items, including product names, prices, and taxes.

**Example response**

```
<?xml version="1.0" encoding="utf-8"?>
<rsm:CrossIndustryInvoice xmlns:a="urn:un:unece:uncefact:data:standard:QualifiedDataType:100" xmlns:rsm="urn:un:unece:uncefact:data:standard:CrossIndustryInvoice:100" xmlns:qdt="urn:un:unece:uncefact:data:standard:QualifiedDataType:100" xmlns:ram="urn:un:unece:uncefact:data:standard:ReusableAggregateBusinessInformationEntity:100" xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:udt="urn:un:unece:uncefact:data:standard:UnqualifiedDataType:100">
    <rsm:ExchangedDocumentContext>
        <ram:BusinessProcessSpecifiedDocumentContextParameter>
            <ram:ID>string</ram:ID>
        </ram:BusinessProcessSpecifiedDocumentContextParameter>
        <ram:GuidelineSpecifiedDocumentContextParameter>
            <ram:ID>urn:cen.eu:en16931:2017#compliant#urn:xeinkauf.de:kosit:xrechnung_3.0</ram:ID>
        </ram:GuidelineSpecifiedDocumentContextParameter>
    </rsm:ExchangedDocumentContext>
    <rsm:ExchangedDocument>
        <ram:ID>string</ram:ID>
        <ram:TypeCode>380</ram:TypeCode>
        <ram:IssueDateTime>
            <udt:DateTimeString format="102">20241212</udt:DateTimeString>
        </ram:IssueDateTime>
        <ram:IncludedNote>
            <ram:ContentCode>EEV</ram:ContentCode>
            <ram:Content>string</ram:Content>
        </ram:IncludedNote>
    </rsm:ExchangedDocument>
    <rsm:SupplyChainTradeTransaction>
        <ram:IncludedSupplyChainTradeLineItem>
            <ram:AssociatedDocumentLineDocument>
                <ram:LineID>1</ram:LineID>
                <ram:IncludedNote>
                    <ram:Content>string</ram:Content>
                </ram:IncludedNote>
            </ram:AssociatedDocumentLineDocument>
            <ram:SpecifiedTradeProduct>
                <ram:SellerAssignedID>string</ram:SellerAssignedID>
                <ram:BuyerAssignedID>string</ram:BuyerAssignedID>
                <ram:Name>string</ram:Name>
                <ram:Description>string</ram:Description>
            </ram:SpecifiedTradeProduct>
            <ram:SpecifiedLineTradeAgreement>
                <ram:BuyerOrderReferencedDocument />
                <ram:NetPriceProductTradePrice>
                    <ram:ChargeAmount>0.00</ram:ChargeAmount>
                    <ram:BasisQuantity unitCode="Unknown">0.0000</ram:BasisQuantity>
                </ram:NetPriceProductTradePrice>
            </ram:SpecifiedLineTradeAgreement>
            <ram:SpecifiedLineTradeDelivery>
                <ram:BilledQuantity unitCode="Unknown">0.0000</ram:BilledQuantity>
            </ram:SpecifiedLineTradeDelivery>
            <ram:SpecifiedLineTradeSettlement>
                <ram:ApplicableTradeTax>
                    <ram:TypeCode>Unknown</ram:TypeCode>
                    <ram:CategoryCode>Unknown</ram:CategoryCode>
                    <ram:RateApplicablePercent>0.00</ram:RateApplicablePercent>
                </ram:ApplicableTradeTax>
                <ram:BillingSpecifiedPeriod>
                    <ram:StartDateTime>
                        <udt:DateTimeString format="102">20241212</udt:DateTimeString>
                    </ram:StartDateTime>
                    <ram:EndDateTime>
                        <udt:DateTimeString format="102">20241212</udt:DateTimeString>
                    </ram:EndDateTime>
                </ram:BillingSpecifiedPeriod>
                <ram:SpecifiedTradeSettlementLineMonetarySummation>
                    <ram:LineTotalAmount>0.00</ram:LineTotalAmount>
                </ram:SpecifiedTradeSettlementLineMonetarySummation>
            </ram:SpecifiedLineTradeSettlement>
        </ram:IncludedSupplyChainTradeLineItem>
        <ram:ApplicableHeaderTradeAgreement>
            <ram:BuyerReference>string</ram:BuyerReference>
            <ram:SellerTradeParty>
                <ram:ID>string</ram:ID>
                <ram:Name>string</ram:Name>
                <ram:Description>string</ram:Description>
                <ram:SpecifiedLegalOrganization>
                    <ram:ID schemeID="0000">string</ram:ID>
                </ram:SpecifiedLegalOrganization>
                <ram:PostalTradeAddress>
                    <ram:PostcodeCode>string</ram:PostcodeCode>
                    <ram:LineOne>string</ram:LineOne>
                    <ram:CityName>string</ram:CityName>
                </ram:PostalTradeAddress>
                <ram:SpecifiedTaxRegistration>
                    <ram:ID schemeID="FC">string</ram:ID>
                </ram:SpecifiedTaxRegistration>
            </ram:SellerTradeParty>
            <ram:BuyerTradeParty>
                <ram:ID>string</ram:ID>
                <ram:Name>string</ram:Name>
                <ram:SpecifiedLegalOrganization>
                    <ram:ID schemeID="0000">string</ram:ID>
                </ram:SpecifiedLegalOrganization>
                <ram:DefinedTradeContact>
                    <ram:PersonName>string</ram:PersonName>
                    <ram:DepartmentName>string</ram:DepartmentName>
                    <ram:TelephoneUniversalCommunication>
                        <ram:CompleteNumber>string</ram:CompleteNumber>
                    </ram:TelephoneUniversalCommunication>
                    <ram:EmailURIUniversalCommunication>
                        <ram:URIID>string</ram:URIID>
                    </ram:EmailURIUniversalCommunication>
                </ram:DefinedTradeContact>
                <ram:PostalTradeAddress>
                    <ram:PostcodeCode>string</ram:PostcodeCode>
                    <ram:LineOne>string</ram:LineOne>
                    <ram:LineTwo>string</ram:LineTwo>
                    <ram:CityName>string</ram:CityName>
                </ram:PostalTradeAddress>
                <ram:SpecifiedTaxRegistration>
                    <ram:ID schemeID="FC">string</ram:ID>
                </ram:SpecifiedTaxRegistration>
            </ram:BuyerTradeParty>
            <ram:BuyerOrderReferencedDocument>
                <ram:IssuerAssignedID>string</ram:IssuerAssignedID>
            </ram:BuyerOrderReferencedDocument>
        </ram:ApplicableHeaderTradeAgreement>
        <ram:ApplicableHeaderTradeDelivery>
            <ram:ActualDeliverySupplyChainEvent>
                <ram:OccurrenceDateTime>
                    <udt:DateTimeString format="102">20241212</udt:DateTimeString>
                </ram:OccurrenceDateTime>
            </ram:ActualDeliverySupplyChainEvent>
            <ram:DeliveryNoteReferencedDocument>
                <ram:IssuerAssignedID>string</ram:IssuerAssignedID>
            </ram:DeliveryNoteReferencedDocument>
        </ram:ApplicableHeaderTradeDelivery>
        <ram:ApplicableHeaderTradeSettlement>
            <ram:PaymentReference>string</ram:PaymentReference>
            <ram:InvoiceCurrencyCode>Unknown</ram:InvoiceCurrencyCode>
            <ram:ApplicableTradeTax>
                <ram:CalculatedAmount>0.00</ram:CalculatedAmount>
                <ram:TypeCode>Unknown</ram:TypeCode>
                <ram:ExemptionReason>string</ram:ExemptionReason>
                <ram:BasisAmount>0.00</ram:BasisAmount>
                <ram:CategoryCode>S</ram:CategoryCode>
                <ram:ExemptionReasonCode>VATEX-132-2</ram:ExemptionReasonCode>
                <ram:RateApplicablePercent>0.00</ram:RateApplicablePercent>
            </ram:ApplicableTradeTax>
            <ram:SpecifiedTradePaymentTerms>
                <ram:Description>#SKONTO#TAGE=0#PROZENT=0.00#BASISBETRAG=0.00#
</ram:Description>
                <ram:DueDateDateTime>
                    <udt:DateTimeString format="102">20241212</udt:DateTimeString>
                </ram:DueDateDateTime>
            </ram:SpecifiedTradePaymentTerms>
            <ram:SpecifiedTradeSettlementHeaderMonetarySummation>
                <ram:LineTotalAmount>0.00</ram:LineTotalAmount>
                <ram:ChargeTotalAmount>0.00</ram:ChargeTotalAmount>
                <ram:AllowanceTotalAmount>0.00</ram:AllowanceTotalAmount>
                <ram:TaxBasisTotalAmount>0.00</ram:TaxBasisTotalAmount>
                <ram:TaxTotalAmount currencyID="Unknown">0.00</ram:TaxTotalAmount>
                <ram:RoundingAmount>0.00</ram:RoundingAmount>
                <ram:GrandTotalAmount>0.00</ram:GrandTotalAmount>
                <ram:TotalPrepaidAmount>0.00</ram:TotalPrepaidAmount>
                <ram:DuePayableAmount>0.00</ram:DuePayableAmount>
            </ram:SpecifiedTradeSettlementHeaderMonetarySummation>
        </ram:ApplicableHeaderTradeSettlement>
    </rsm:SupplyChainTradeTransaction>
</rsm:CrossIndustryInvoice>
```

If the request contains invalid data, an error message is returned in JSON format.
