---
title: "Review Integration Changes"
---

<a id="ReviewIntegrationChanges"></a>


You can review the changes made to an integration by using the Audit Trail feature that provides you with a comprehensive historical record of all changes made by authors to an inetgration.

{% hint style="info" %}
**NOTE:** The Audit trail is in technological preview in DRUID 7.8. In a future release, you will be able to restore the integration to a previous version.
{% endhint %}

To review the updates made to an integration, follow these steps:

1. Open the connector action in diagram view and select a node.
2. Click the **Code** icon (![](../../Resources/Images/Diagram/audit.png)). The Audit Trail editor appears automatically on the **Code** tab, presenting the JSON structure of the integration, along with detailed information about connector action details and all integrations within the connector action with their settings.

![](../../Resources/Images/CNN%20Designer/click%20code%20icon.png)

3. Click the **Audit Trail** tab.

![](../../Resources/Images/CNN%20Designer/select%20version.png)

4. Select the desired item from the list of historical changes.
5. The Audit trail displays the integration code of the selected record.

![](../../Resources/Images/CNN%20Designer/version%20details.png)

6. At the top-right corner of the page, click the **Compare** icon (![](../../Resources/Images/Diagram/compare%20icon.png)).
   The comparison page will display the version you selected on both sides.
7. On the left side, choose the version you wish to compare with the selected one (displayed on the right).

The two versions are displayed side-by-side (the updated version on the right side), with changes highlighted in color. The changes are highlighted in green for the version you selected to compare and in red for the version you are comparing it with.

8. To view the details of a change either scroll-down or by click directly on the color indicator.

![](../../Resources/Images/CNN%20Designer/compared%20versions.png)
