---
title: UiPath Automation Hub Starter
---


Use this solution if you want to showcase DRUID-UiPath AutomationHub integration. You can use it when the intent not recognized flow is triggered and recommend your employees to submit an idea for automation in the Automation Hub.

{% hint style="info" %}
**NOTE:** The solution is available only in EN-US.
{% endhint %}

1. Download the UiPathAutomationHub template by clicking on the **Download** button below.

[!\[\](../Resources/Images/Download.png)](https://druiddocs.file.core.windows.net/docs-shares/UiPathAutomationHub_202144040244.zip?st=2022-01-18T11%3A27%3A09Z\&se=2026-01-19T11%3A27%3A00Z\&sp=rl\&sv=2018-03-28\&sr=f\&sig=auxlLYNtXzaO7dp20Ahofcz0vQCm2lG1u%2BwClLSdrwg%3D)

2. On the desired AI Agent, import the solution .zip file. For information on how to import solutions, see [Importing Solutions](https://druidai.gitbook.io/druid-ai-docs/ai-platform/release-lifecycle-and-versioning/importing-solutions).
3. Set up the UiPathAutomationHub solution.

## How to set up UiPath Automation Hub solution template

### Prerequisites

* You need to have an organization account on UiPath Automation Hub.
* You completed the set-up process for your UiPath Automation Hub account.
* In the UiPath Automation Hub Platform, go to **Admin Console** > **Platform Setup** > **Open Api** > **Generate Token** and generate a new access token to your environment. Copy the token and App Key, you will need them in Druid to authenticate the requests.

![](<../../.gitbook/assets/automhub get token.png>)

![](<../../.gitbook/assets/hub key and token.png>)

To set up the UiPath Automation Hub connector in Druid:

1. From solution Apps, click **UiPath-AutomationHub**. The Edit Connector page appears. The **URL** (https://automation-hub.uipath.com/api/v1/openapi) and **Security Type** (Custom) are selected by default.
2. From the **AuthorizeRequestConnectorAction** field, select **UiPath-AutomationHub-Authorize**.
3. In the Variables section, add the following variables:

* **AutomationHubAccessToken** - The token you copied from the UiPath Automation Hub Platform.
* **AppKey** - The App Key you copied from the UiPath Automation Hub Platform.
* **OwnerEmail** - Your email from UiPath Automation Hub.

![](<../../.gitbook/assets/autom hub druid setup.png>)

4. Click **Save and Close**.

You can start chatting with the AI Agent by saying things like "I have an idea" or " I would like to make a suggestion".
