<a id="DRUID520"></a>

# DRUID 5.20

Deployment Dates

The table below lists the deployment date of DRUID v5.20 across DRUID Clouds. To view the DRUID Releases Calendar, see [Druid AI Releases](../Druid%20AI%20Releases.md).

| Druid Cloud Community  \*.community.Druidplatform.com | Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- | --- |
| August 03, 2023 | August 31, 2023 | August 31, 2023 | August 31, 2023 |

These release notes give you a brief, high-level description of the improvements implemented to existing features.

If you have questions about your DRUID tenant, please contact [support@Druidai.com](mailto:support@druidai.com) or your local DRUID partner for more information.

<a id="WhatsNew"></a>

## What's New

- **Calendar views**. Calendar views allow you to track record events (records with have at least one Date / DateTime field) on a calendar. You can track tasks, leads, appointments, employees' holidays and many other.

![](../../Resources/Images/CBA/calendar%20view%20example.png)

For more information, see [../../Governance%20%26%20Security/User%20Management/Provisioning%20Portal%20Users%20with%20LDAP.md](../../Governance%20%26%20Security/User%20Management/Provisioning%20Portal%20Users%20with%20LDAP.md)[Calendar Views](../../CBA/Calendar%20Views.md).

- **Linking entities to solutions**.With this release you can include web views, forms and charts to the solution package before export, by linking specific entities / entity fields to the solution. Workspaces are also included in the solution. For more information, see [Exporting and Downloading Solutions](../../Working%20with%20Solutions/Exporting%20and%20Downloading.md).
- **Image navigation URL for images on Hero and Thumbnail cards**. You can now add a navigation URL to the image displayed on hero / thumbnail cards. When users will click the image in a card, the navigation URL will open in a new page in the browser. It is particularly useful for example, when the chat users click the product image to get the product page.

![](../../Resources/Images/druid%205.20/product%20images.png)

<a id="Improvements"></a>

## Improvements

- **Currency entity field selector**. When adding entity fields of type Currency, you can now select the currency from a drop-down or search for the desired currency and select it.

![](../../Resources/Images/druid%205.20/currency%20selector.png)

![](../../Resources/Images/druid%205.20/currency%20search.png)

At runtime, in web views and forms, the currency is shown at the right side of the amount.

<a id="BugFixes"></a>

## Bug Fixes

- Channels: Even if the Step Message is empty, the Hero/Thumbnail buttons are now rendered in the following channels: Instagram, WhatsApp Vonage and Sunshine Conversations apps in the WhatsApp channel.
- REST Connector: When mapping errors, you can now map both the ErrorCode and the StatusCode.
- Knowledge Base: When adding structured data sources, DRUID calculates the size of the file.

![](../../Resources/Images/druid%205.20/file%20size%20kb.png)
