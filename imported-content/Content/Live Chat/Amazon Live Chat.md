---
layout:
  title:
    visible: false
---

<a id="AmazonLiveChatIntegration"></a>

# Amazon Live Chat Integration

You can now integrate Amazon Connect with Druid to allow your customers chat with the AI Agent and get support from your Contact Center agents who are using Amazon Connect.

![](../Resources/Images/Live%20Chat%20providers/amazon.png)

<a id="Prerequisites"></a>

## Prerequisites

- You need to have the call center set up in Amazon Connect.
- You need an Amazon Console account.

<a id="Configuringtheintegration"></a>

## Configuring the integration

This section provides the steps necessary to place a customer live chat in Amazon Connect (that is, start an Amazon live chat session).

<a id="Step1CreateAWSuserdedicatedfortheAmazonConnectDruidIntegration"></a>

### <a id="Step_1:"></a>Step 1: Create AWS user dedicated for the Amazon Connect - Druid Integration

1. Log in the AWS Management Console and go to Identity Access Management (IAM).
2. Create a DRUID-dedicated IAM user and assign an IAM policy that grants access to the Amazon Connect service and the following actions:

- **StartChatContact**
- **StopContact**

If you want to pass the client’s position in the queue to Druid, also grant access to: **GetContactMetrics**.

3. You can provide specific flow access in the Policy Editor as per examples below.

Example of IAM Policy which grants user access to all Amazon Connect resources:

```
{
"Version": "2012-10-17",
"Statement": [
   {
      "Action": [
         "connect:StartChatContact",
         "connect:StopContact",
         "connect:GetContactMetrics"
      ],
      "Resource": ["*"],
      "Effect": "Allow"
   }
]
}
```

Example of IAM Policy which grants user access to specific Amazon Connect resources:

![](../Resources/Images/Live%20Chat/Amazon%20Live%20Chat/complex%20iam%20policy.png)

You can use the [AWS Policy Generator](https://awspolicygen.s3.amazonaws.com/policygen.html) to generate the policy.

![](../Resources/Images/Live%20Chat/Amazon%20Live%20Chat/aws%20policy%20generator.png)

4. On the user details page, click the **Security credentials** tab and generate access key for this user by clicking the **Create access key** button. When the access key is created, the **Access key ID** displays in the table and you also get the secret key.
5. Write down or copy / paste in a document the Access key ID and secret key, you will need them later to configure your AI Agent for Amazon Connect integration.

![](../Resources/Images/Live%20Chat/Amazon%20Live%20Chat/access%20key.png)

> **NOTE:** If you lose or forget your secret key, you cannot retrieve it. Instead, create a new access key and make the old key inactive. You can have a maximum of two access keys (active or inactive) at a time.

<a id="Step2GetAmazonConnectInstanceIDandFlowID"></a>

### Step 2: Get Amazon Connect Instance ID and Flow ID

In Amazon Connect, go to the details page of the flow you want to trigger from DRUID. On the flow menu, click **Show additional flow information**. From the ARN section, copy the Instance ID and the flow Id and paste them in a document, you will need these IDs to configure your AI Agent for Amazon Connect integration.

![](../Resources/Images/Live%20Chat/Amazon%20Live%20Chat/instance%20and%20flow%20id.png)

<a id="Step3ConfigureDRUIDforAmazonConnect"></a>

### Step 3: Configure DRUID for Amazon Connect

Go to AI Agent details page and click the **Live Chat** section header. The section expands.

![](../Resources/Images/Live%20Chat/Amazon%20Live%20Chat/amazon%20live%20chat%20settings.png)

Set the Amazon Live Chat fields as described in the table below

| Field | Description |
| --- | --- |
| Live chat provider | Select **Amazon**. |
| AWSConnectServiceUrl | Enter your Amazon Connect endpoint in the following format:  https://connect.[REGION].amazonaws.com  For the complete list of Amazon regions, see [Amazon Connect documentation](https://docs.aws.amazon.com/general/latest/gr/connect_region.html).  Example: https://connect.**eu-central-1**.amazonaws.com for region eu-central-1. |
| AWSParticipantServiceUrl | Enter your Amazon Connect Participant Service endpoint in the following format:  https://participant.connect.[REGION].amazonaws.com.  For the complete list of Amazon regions, see [Amazon Connect documentation](https://docs.aws.amazon.com/general/latest/gr/connect_region.html).  Example: https://participant.connect.**eu-central-1**.amazonaws.com for region eu-central-1. |
| AWSApiId | The Access key ID created for your DRUID dedicated user (the one from Step 1.) |
| AWSApiKey | The Access key secret provided to you when creating the access key for your DRUID dedicated user (the one from Step 1). |
| AWSInstanceId | Amazon Connect Instance ID (the one you got at Step 2). |
| AWSFlowId | The flow ID that will be triggered in Amazon Connect (the one you got at Step 2). |

After you set up the Amazon Live Chat fields, click the **Save & Close** button to save the settings.

<a id="Step4ConfiguretheflowstepforconnectingtoAmazonAgent"></a>

### Step 4: Configure the flow step for connecting to Amazon Agent

On the flow of choice, add a step dedicated to connecting clients to Amazon Connect. On the flow step set the following variables:

- [[Chatuser]].Name = [[HelpdeskClient]].FirstName
- [[ChatUser]].HelpdeskSubject = [[HelpdeskClient]].Subject

On the dedicated step, in the PreActions section, call the internal action **ConnectToHelpdeskAgent**.

![](../Resources/Images/Live%20Chat/Amazon%20Live%20Chat/flow%20steo%20config.png)

> **NOTE:** If you do not set the two variables **[[ChatUser]].Name** and **[[ChatUser]].HelpdeskSubject**, the AI Agent will fail placing the customer in the Amazon Connect live chat. Please note that in figure above, the [[HelpdeskClient]] entity in the right hand side of the SetVariables section are used only as an example - you can set any values in **[[ChatUser]].Name** and **[[ChatUser]].Subject**, as per your specific flow configuration.

<a id="SendtheconversationtranscripttoAmazonLiveChatAgents"></a>

## Send the conversation transcript to Amazon Live Chat Agents

Most contact centers want their helpdesk agents to get the transcript of the conversation the client had with the AI Agent prior to being engaged in a live chat session.

To save the conversation transcript and make it available for Amazon Live Chat agents, on the flow that connects the client with the agent, make the following settings:

1. On the step where you call the internal action **ConnectToHelpdeskAgent**(Post Actions section), in the **Pre Actions** section, call the internal action **GetConversationTranscript**.
> **IMPORTANT!**  When calling the **GetConversationTranscript** internal action on the same step where you call **ConnectToHelpdeskAgent**, make sure to call it in the PreActions section. Calling it in the PostActions section will not send the conversation transcript to agents.

> **Info:**  You can call the **GetConversationTranscript** internal action on a previous step.

2. On the **ConnectToHelpdeskAgent** internal action add the following:

```
{
  "SendConversationTranscript": true
}
```

> **Info:** You can send additional client information to Amazon Live Chat Agents together with the conversation transcript. For more information, see [Send Contact Center Parameters](#Send_Contact_Center_Parameters).

3. Save the step.

<a id="EnablerealtimequeuepositionretrievalfromAmazonConnect"></a>

## <a id="Enable"></a>Enable real-time queue position retrieval from Amazon Connect

> **NOTE:** This feature is available starting with DRUID version 9.12. It also requires the AWS user dedicated to the Amazon Connect–Druid integration to be granted an IAM policy with **GetContactMetrics** permissions. For more information about this policy, see [Step 1](#Step_1%3A).

To include a waiting user’s real-time position from the Amazon Live Chat queue in the Druid conversation context, set the **PositionInQueueSetByCC** parameter to **true** in the **ConnectToHelpdeskAgent** internal action.

```
{
  "PositionInQueueSetByCC": true,
  "SendConversationTranscript": true
}
```

<a id="SendContactCenterParameters"></a>

## <a id="Send_Contact_Center_Parameters"></a>Send Contact Center Parameters

The table below lists the Contact Center parameters authors can send to Amazon Live Chat.

| Parameter | Data Type | Description |
| --- | --- | --- |
| firstName | String | The first name of the client. |
| lastName | String | The last name of the client. |
| question | String | The question asked by the client. |
| queueId | Long | The ID of the queue to which the client will be assigned.  **NOTE:** If you have multiple queues, this is the Id of the Amazon Live Chat queue to which the client will be assigned. |
| contactId | Long | The contact ID of the client. |
| organizationId | Long | The client organization ID. |

To send Contact Center parameters to Amazon Live Chat, on the **ConnectToHelpdeskAgent** internal action, provide the desired parameters inside the `ContactCenterParameters` object in JSON format.

> **NOTE:** The payload must follow a key-value format where both the key and value are strings. When using values from DRUID conversation context (entities, local variables) as parameter values, ensure they are enclosed in double quotes ("") to maintain valid JSON formatting.

**Example - Send Contact Center parameters**

```
{
     "SendConversationTranscript":true,
     "ContactCenterParameters":
        {
                "firstName":"[[Customer]].FirstName",
                "lastName":"@lastName",
                "question":"[[Customer]].Question",
                "queueId":"[[Entity]].QueueId",
                "contactId":"@contactId",
                "organizationId":""
        }
}
```
