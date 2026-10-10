---
title: Google LLM
---

# Google LLM

The GoogleLLM Connector allows you to authenticate directly to Google Vertex AI using your own Google service account. This secure connection eliminates the need for the DRUID Service Gateway and credential sharing, enabling you to leverage your Google resources, for powering conversational responses with Google's Large Language Models (LLMs) in Knowledge Base (KB) generative endpoints and CNN.

{% hint style="info" %}
**NOTE:** The GoogleLLM Connector is available in DRUID version 8.17 and later. For hybrid and on-premises deployments, you must upgrade the DRUID Connector Host to version 8.17 or later.
{% endhint %}

### Prerequisites

Before you begin, make sure the following requirements are met:

* You have a Google Cloud Platform (GCP) service account. If you don’t have one, create it [here](https://console.cloud.google.com/iam-admin/serviceaccounts/project).
* For DRUID on premise deployments, make sure that you provide access to/from the necessary messaging endpoints as follows:

|          |                  |
| -------- | ---------------- |
| Outbound | \*googleapis.com |
| Inbound  | DRUID.BotApp     |

* You must have a service account JSON file that contains the private key. If you don’t have one, generate it by following these steps:

1. Go to the [Service Accounts page](https://console.cloud.google.com/iam-admin/serviceaccounts/project) in the Google Cloud Console.
2. Select your service account.

![](<../../.gitbook/assets/service account (1).png>)

3. Click the **Keys** tab.

![](<../../.gitbook/assets/keys tab.png>)

4. Click **Add Key** > **Create new key**.

![](<../../.gitbook/assets/add key.png>)

5. Choose **JSON** as the Key type.
6. Click **Create**.

![](<../../.gitbook/assets/cerate json key.png>)

The **service-account.json** file will be downloaded automatically to your local machine.

### Define Google Vertex AI connection strings

1. Log in to the Druid Portal.
2. Select your AI Agent and solution.
3. In the Solution menu, click **Apps**.
4. At the top right corner of the Apps page, click **Create App** and **select GoogleLLM**.
5. On the New App page, fill out the following fields:

| Field              | Description                                                                                 |
| ------------------ | ------------------------------------------------------------------------------------------- |
| Code               | A unique name for the app. You’ll use this reference in REST calls. This field is required. |
| ServiceAccountJSON | Paste the full content of the service-account.json file downloaded in the prerequisites.    |

![](<../../.gitbook/assets/GOOGLELLM APP.png>)

6. Click **Save & Close**.
7. Click **Publish** to make the app available.

### Use your Google Vertex AI resource

To use your own Google Vertex AI resource, make REST API calls and in the **Connection Code** field, select the GoogleLLM app you created.

![](<../../.gitbook/assets/connection code.png>)

For supported API calls and usage details, refer to the [Google Vertex AI API documentation](https://cloud.google.com/vertex-ai/docs/reference/rest).
