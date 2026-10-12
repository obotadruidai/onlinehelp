---
title: "Data Model and Workspace References"
---

<a id="DataModelandWorkspaceReferences"></a>


The Retail Agentic Solution organizes its data across three workspaces, each managing a distinct set of entities.

<a id="WorkspaceReference"></a>

## Workspace Reference

The solution spans three workspaces, each responsible for a distinct domain:

| Workspace | Key Entities Managed | Purpose |
| --- | --- | --- |
| Admin | RetailSettings  RetailStatus  RetailDeliveryType  RetailPaymentType | Global settings, provisioning, and privacy/preview toggles. |
| Retail Back-Office | RetailProductCategory  RetailProductSubcategory  Store Stock  ProductWishlist  ProductCampaign  Audience | Inventory "Engine Room," stock levels per store, and backend campaign data. |
| Retail Front-Office | RetailCustomer  RetailOrder  RetailClaim  RetailReturnedProducts  Wishlist  CampaignPromo | Customer management, sales fulfillment, and marketing execution. |

<a id="ProvisionedEntities"></a>

## Provisioned Entities

The following entities are automatically provisioned during solution setup and provide the core configuration and catalog data:

| Entity Name | Description |
| --- | --- |
| RetailSettings | Central configuration holding the Anonymization and Image Preview toggles. |
| RetailStatus | Defines order lifecycle stages (New, In Transit, Delivered, etc.). |
| RetailDeliveryType | Fulfillment methods (Home Delivery, Store Pickup). |
| RetailPaymentType | Accepted payment methods (Cash, Credit Card, etc.). |
| RetailProductCategory | Top-level catalog grouping (Shoes, Shirts, Books). |
| RetailProductSubcategory | Secondary catalog grouping (Running Shoes, History Books). |
| Store | Physical shop locations with address, city, and postal code. |
| RetailProduct | Core product records (Price, Brand, ImageUrl, Author, Sizes). |
| Stock | Bridge linking a RetailProduct to a Store with a Quantity. |

<a id="BusinessEntities"></a>

## Business Entities

These entities are provisioned as part of the data model setup; records are created and managed at runtime by users, front-office, and business processes.

| Entity Name | Description |
| --- | --- |
| RetailCustomer | Profiles for shoppers, including contact and insurance/account info. |
| RetailOrder | Sales transactions (includes Draft and Abandoned statuses). |
| RetailClaim | User claims linked to images stored in Azure. |
| RetailReturnedProducts | Tracking for items returned by customers. |
| Wishlist | Parent record representing a customer’s collection of saved items. |
| ProductWishlist | Individual items saved within a specific Wishlist. |
| CampaignPromo | Management record for marketing campaigns (Codes/Dates). |
| ProductCampaign | Links specific products to a CampaignPromo. |
| Audience | List of users targeted for outreach when a campaign runs. |
