---
title: Workspace Designer
---

# Workspace Designer

The Workspace Designer helps creating create and refining workspace components—including charts, forms, views, and dashboards—using natural language. It transforms your business requirements into workspace configurations, reducing manual design effort and accelerating workspace design.

{% hint style="info" %}
**NOTE:** The Workspace Designer currently supports chart authoring only. Support for additional workspace components, including forms, views, and dashboards, is planned for future releases.
{% endhint %}

### Charts Agent

The Charts Agent configures visual analytics dashboard components.

#### Key Capabilities

* Guides chart parameter definition for Bar, Line, Pie, and Doughnut formats.
* Maps chart elements to data sources and recommends creating targeted queries when current data sources are insufficient.
* Modifies visual attributes, layout filters, and display labels without exposing raw code.
* Generates data queries as readable plain text for manual application, or applies queries automatically when explicitly commanded.
* Scans chart output data automatically and flags data quality anomalies, such as high volumes of unassigned category values.

#### Operational Rules

* Restricts chart rendering strictly to the four supported chart types.
* Requires explicit user commands ("save," "apply," or "enable") before writing queries directly to chart settings.
* Stops execution and prompts for user instruction upon encountering execution errors.

#### Create a chart <a href="#create3" id="create3"></a>

1. Open the entity for which you want to create a chart.
2. Select the **Charts** tab.
3. Click the **Page Help** icon in the upper-right corner.

![](<../../.gitbook/assets/chart druid help.png>)

4. Follow the Workspace Designer guidance to describe the chart you want to create.

#### Fine-tune an existing chart <a href="#fine-tun" id="fine-tun"></a>

1. Open the chart you want to modify.
2. In the chart configuration page, click **Author with AI**.

![](<../../.gitbook/assets/author with ai.png>)

3. Describe the changes you want to make and follow the Workspace Designer guidance.

All AI-assisted chart changes appear on the chart configuration page in the **Advanced data visualization** area.
