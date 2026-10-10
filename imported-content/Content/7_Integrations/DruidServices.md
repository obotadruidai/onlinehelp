---
title: "Druid Services"
---

<a id="DruidServices"></a>


To integrate DRUID-specific resources — such as DRUID LLM or DRUID Vision — especially when using solutions from the Solution Library or migrating them between tenants, you must configure the Base URL and token for each DRUID resource. DRUID Services apps simplify this process by using dedicated connector variables tailored to the DRUID services available in your tenant.

> **NOTE:** This feature is available in DRUID 8.15 and higher. For hybrid and on premise deployments, you need to upgrade the DRUID Connector Host to version 8.15 or higher.

This section guides you through setting up and connecting DRUID-specific resources using DRUID Services apps.

<a id="CreateaDruidServicesapp"></a>

## Create a Druid Services app

1. Go to **Solution Contents** > **Apps**.
2. Click **Create App** in the upper-right corner and select **DruidServices**.
3. In the **Code** field, enter a unique name for your Druid Services app.
4. The Druid Services table displays dedicated connector variables tailored to the DRUID services available in your tenant.

| Variable name | Value |
| --- | --- |
| The variable name that holds the DRUID service name containing URL | The Base URL for the DRUID service resource. |
| The variable name that holds the DRUID service name containing the token claims | The last 5 characters of the JWT token. |

![](../Resources/Images/DRUID%208.15/ds%20variables%20table.png)

> **Info:** The values displayed in this table are automatically pulled from **Administration** > **Druid Services**.
>
> ![](../Resources/Images/DRUID%208.15/administration.png)

5. In the **Base URL** field of the app, enter the variable name (for example, @\_Druid.LLM\_URL) that corresponds to the resource you want to use in your integrations.
> **Info:** Starting with DRUID 9.1, you can concatenate a variable that holds the DRUID service URL (for example, @\_Druid.LLM\_URL) with an API path (such as chat/completions) directly in the Base URL field. This enables dynamic construction of endpoints and eliminates the need to manually enter or update the full request path when defining integrations.
>
> ![](../Resources/Images/druid%209.1/BASE%20URL.png)
>
> ![](../Resources/Images/druid%209.1/integration%20url.png)

> **NOTE:** Using the variable name in the Base URL field is available in DRUID 8.18 and higher, for previous releases you have to configure the URL in the integrations.

6. Copy the name of the variables for the URL and token specific to the resource you want to use. You will need them to configure your REST integrations.
7. Click **Save & Close**.
8. Publish the apps to make your app available for use.

> **IMPORTANT!** If a token becomes invalid or expires, it will no longer be available in the Connector. The Druid Services variable information is updated each time you publish the apps. This automatic update also applies to tokens generated after the Druid Service app was initially created. Therefore, any token changes in **Administration** > **Druid Services** will be reflected in your Connector after a simple publish of the Apps.

<a id="UseDruidServicesinRESTIntegrations"></a>

## Use Druid Services in REST Integrations

1. Open your desired REST integration.
2. In the **General** tab, from the **Connection Code** field, select the Druid Services app you created.
3. Click on the **Request** tab.
4. In the Variables section, map the appropriate token for the DRUID service you’re calling. These Druid Services variables can be used in Parameters, Headers, Body, and Child Mappings. You can map additional parameters based on your needs.
> **NOTE:** In DRUID Versions prior to 8.18, you also have to map the appropriate URL for the DRUID service you’re calling.
>
> ![](../Resources/Images/DRUID%208.15/cnn%20variables%20ds.png)

5. Save the integration.
6. Publish the integrations.
