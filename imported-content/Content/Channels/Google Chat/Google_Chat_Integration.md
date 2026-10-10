<a id="GoogleChat"></a>

# Google Chat

Connect your Druid AI Agent directly to Google Workspace through Google Chat. This integration enables automated conversation workflows, direct messaging, and group space interactions within your organization's Google Chat environment using a single configuration.

<a id="Prerequisites"></a>

## Prerequisites

- [Google Cloud Platform (GCP)](https://console.cloud.google.com/) account with project creation / admin permissions.
- Create a project in the Google Cloud project for your AI Agent. For information on how to create a Google Cloud Project, see [Google Cloud documentation](https://cloud.google.com/resource-manager/docs/creating-managing-projects).
- Druid Portal administrator access.
- For Druid on premise deployments, make sure that you provide access to/from the necessary messaging endpoints as follows:

|  |  |
| --- | --- |
| Outbound | \*googleapis.com |
| Inbound | DRUID.BotApp |

<a id="Integrationprocedure"></a>

## Integration procedure

To integrate an AI Agent with Google Chat, follow these steps:

<a id="Step1GetGoogleCloudProjectdetails"></a>

### Step 1. Get Google Cloud Project details

Log in the Google Console, select the project you’ll be using for Druid - Google Chat channel. On the project Dashboard, from the Project info card, copy the **Project number** as you will need it for Druid channel setup.

![](../../Resources/Images/Google%20Chat/get%20project%20number_1913x872.png)

<a id="Step2AddServiceaccountforyourGoogleConsoleproject"></a>

### Step 2. Add Service account for your Google Console project

A service account is an identity that Google Cloud can use to run API requests on your behalf.

1. From the **APIs & Services** menu, select **Credentials**.

![](../../Resources/Images/Google%20Chat/services%20credentials_1911x855.png)

2. In the Service Accounts section, click the Manage service accounts link.

![](../../Resources/Images/Google%20Chat/manage%20service%20accounts.png)

The Service accounts page appears.

3. At the top of the page, click **CREATE SERVICE ACCOUNT**.

![](../../Resources/Images/Google%20Chat/CREATE%20SERVICE%20ACCOUNT.png)

The Create service account page appears.

4. Provide the service account details: a unique **Service account name** and the desired **Service account ID**.

![](../../Resources/Images/Google%20Chat/service%20account%20details.png)

5. Click the **CREATE AND CONTINUE** button.
6. Grant this service account Owner access to your Google Console project so that it has permission to complete specific actions on the resources in your project. From the **Role** drop-down, select **Owner**.

![](../../Resources/Images/Google%20Chat/grant%20service%20account%20access%20to%20project.png)

You can also grand users access to this service account. For more information on the service account settings, see [Google Cloud documentation](https://cloud.google.com/iam/docs/service-accounts?hl=en#types).

7. Click **DONE**. The service account appears in the Service accounts page.

![](../../Resources/Images/Google%20Chat/servce%20account%20saved.png)

<a id="Step3GetserviceaccountEmail"></a>

### Step 3. Get service account Email

In the Service accounts page, click on the service account your created for your Google Console project.

The Service account details appears. Copy the value from the **Email** field.

![](../../Resources/Images/Google%20Chat/copy%20email.png)

Now you have to add a service account key.

<a id="Step4Addserviceaccountkey"></a>

### Step 4. Add service account key

In the Service account details page, click the **KEYS** tab.

You can easily add a service account key by either uploading it or by creating / generating a new one.

![](../../Resources/Images/Google%20Chat/add%20key.png)

If you choose to create a new key, the key will be automatically downloaded in your default Download folder. You will need the file later during Google Chat channel configuration in Druid.

For information about adding service account keys, see [Google Chat API documentation](https://developers.google.com/chat/how-tos/service-accounts).

<a id="Step5ActivatetheGoogleChatchannelinDruidPortal"></a>

### Step 5. Activate the Google Chat channel in Druid Portal

1. In the Druid Portal go to your AI Agent settings.
2. Click the **Channels** tab, then search for **Google Chat** and click on the channel card.
3. In the modal, fill in the fields as follows:

| Druid Field | Google Console Field |
| --- | --- |
| Google Chat Project Number | The Google Console project number. |
| Google Chat Service Account Email | The Email of the service account you granted access to your Google Console project. |
| Google Chat Service Account Private Key | The Key you added to the service account you granted access to your Google Console project. If you created a new one, open the key file and copy its value (the value between the “ ”).  ![](../../Resources/Images/Google%20Chat/copy%20the%20key.png) |

![](../../Resources/Images/Google%20Chat/channel%20configuration.png)

4. Optionally, customize channel display settings as follows:

- **Alias**: Enter a clear, business-friendly display name (e.g., Interactive Messaging). This value is stored in**[[ChatUser]].ChannelDisplayName**, which appears in reporting tools like AI Agent Summary dashboard - Engagement KPIs and can also be referenced in flow business logic.
- **Description**: Enter a brief description. This is particularly helpful when using an alias, as it helps identify the channel's specific purpose within the Druid Portal.
- **Channel Icon**: Upload a custom icon to display on the channel card within the Druid Portal.

5. Click the **Publish** button. The channel activation might take up to 1 minute.
6. When the channel is active, click on the channel card and copy the value of the **Google Chat Inbound Url** field that is automatically filled in. You will need the value at [Step 6](#Step_6.).

![](../../Resources/Images/Google%20Chat/copy%20inbound%20url.png)

7. Close the modal.

When the channel is active, the following fields are available in Druid:

- **[[ChatUser]].ChannelId** = "googlechat"
- **[[ChatUser]].UserId** - Stores an unique identifier of the Google user account.
- **[[ChatUser]].ChannelDisplayName** - Stores the Alias which is used in AI Agent Summary Dashboard > Engagement KPIs > Channel chart.

<a id="Step6EnabletheGoogleChatAPIforyourGoogleConsoleproject"></a>

### <a id="Step_6."></a>Step 6. Enable the Google Chat API for your Google Console project

New Google Console projects have by default a set of predefined Google APIs and services. For Druid Google Chat, you need to add the Google Chat API to your project. This Google API enables you to create a AI Agent for Google Chat:

1. From the left menu, click **APIs & Services** and select **Dashboard**.

![](../../Resources/Images/Google%20Chat/select%20api%20dashboard_1914x872.png)

The list of Google APIs and Services available in your project appears.

2. At the top of the page, click **ENABLE APIS AND SERVICES**.

![](../../Resources/Images/Google%20Chat/enable%20api.png)

Google API Library appears.

3. Search for the "Google Chat API".

![](../../Resources/Images/Google%20Chat/search%20chat%20api.png)

The search might return more results.

4. Click **Google Chat API**. The API details page appears.
5. Click **Enable**.

![](../../Resources/Images/Google%20Chat/enable%20chat%20api.png)

The Hangout Chat API is enabled and the Overview page appears.

6. From the main menu, click **Configuration**.
7. Configure the Hangout Chat API as provided in the figure below:

![](../../Resources/Images/Google%20Chat/api%20configuration.png)

8. Click **SAVE**.

<a id="Step7TalktoyourAIAgent"></a>

### Step 7. Talk to your AI Agent

> **NOTE:** When a user initiates a conversation with the AI Agent, the Welcome flow will be automatically triggered. Regardless of the user's subscription status to the AI Agent channel, the welcome message will be promptly sent to the user, ensuring a seamless and engaging interaction experience.

You have two options to talk to your AI Agent:

#### From Druid Portal, Google Chat channel

To open the AI Agent in the Google Chat channel, in the Druid Portal, go to the AI Agent settings, click the **Channels** tab. Search for Google Chat and click the channel card. In the modal, click the Google Chat icon at the top-left corner of the modal. You can start talking to the AI Agent.

#### From Gmail account, Google Chat

Log into your Gmail account and in the Chat section click Start a chat and search for the AI Agent you previously integrated in Google Chat. Select the AI Agent.

![](../../Resources/Images/Google%20Chat/start%20chat.png)

The chat appears and you can start chatting with your AI Agent.

![](../../Resources/Images/Google%20Chat/chatting.png)

<a id="GoogleUserInformation"></a>

## Google User Information

The following Google user details are automatically available in the [[ChatUser]] entity:

- Google user's email in [[ChatUser]].Email.
- Google display name in [[Chatuser]].FirstName.

These details are useful to authenticate the user based on the Google email.

Messages sent in HTML format, including images and formatted content, are rendered similarly to the Direct Line channel instead of displaying raw HTML code.
