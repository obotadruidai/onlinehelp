---
title: "RingCentral CX Data Provisioning & Configuration"
---

<a id="RingCentralCXDataProvisioningConfiguration"></a>

<a id="_RingCentral_CX_Data"></a>

{% hint style="info" %}
**Info:** To run RingCentral CX Campaigns requires business app upgrade to version 10.1. or higher.
{% endhint %}

To provision RingCentral CX campaigns data:

1. Go to **Administrators - Campaign Management Settings** workspace>  **Campaign Settings** .
2. Click the **Import Settings** button to load default configuration data.

![](../../../Resources/Images/Ring%20central%20%2B%20excel%20export%20updates/RingCentral%20CX%20Data%20Provisioning.png)

![](../../../Resources/Images/Ring%20central%20%2B%20excel%20export%20updates/RingCentral%20CX%20Data%20Provisioning_1.png)

3. Switch the **Call Center System**. Click on the **Default** record, change the **Call Center System** field from **Druid Data Service** to **Ring Central** and save your changes.
{% hint style="warning" %}
**IMPORTANT!** Setting the call center system to RingCentral is mandatory so that the RingCentral CX agent can correctly load and map RingCentral CX dispositions.
{% endhint %}

![](../../../Resources/Images/Ring%20central%20%2B%20excel%20export%20updates/RingCentral%20CX%20Data%20Provisioning_2.png)

![](../../../Resources/Images/Ring%20central%20%2B%20excel%20export%20updates/RingCentral%20CX%20Data%20Provisioning_3.png)

4. Click the **Import Settings** button again.

This process retains existing data while adding RingCentral-specific assets:

- **Campaigns**. The **OB – Missed Recalls** campaign, available under **Campaign Managers - Campaigns & Audiences** workspace > **Campaigns** > **RingCentral Campaigns** tab.

![](../../../Resources/Images/Ring%20central%20%2B%20excel%20export%20updates/RingCentral%20CX%20Data%20Provisioning_4.png)

- **Audiences**. An empty audience linked to the campaign. This is an automatically populated dynamic audience where contacts are added one-by-one as calls take place.
- **Activity Statuses**. Pre-mapped RingCentral CX dispositions located under **Administrators – Campaign Management Settings workspace** > **Campaign Activity Statuse**s, where individual statuses can be enabled or disabled.

![](../../../Resources/Images/Ring%20central%20%2B%20excel%20export%20updates/RingCentral%20CX%20Data%20Provisioning_5.png)
