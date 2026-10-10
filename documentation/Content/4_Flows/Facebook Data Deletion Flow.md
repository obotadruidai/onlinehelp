<a id="FacebookDataDeletionFlow"></a>

# Facebook Data Deletion Flow

Facebook requires applications to provide a mechanism for deleting user personal data when a user requests it or deletes their Facebook account. Druid supports this requirement through the Facebook Data Deletion Flow.

When Facebook sends a Data Deletion Callback request, Druid automatically triggers this special flow, allowing you to execute the required data anonymization while optionally extending the process with your own business logic.

The flow runs automatically for the Facebook user identified in the callback request.

> **IMPORTANT!** The **Facebook Data Deletion Flow** is event-driven. It runs only when Facebook sends a Data Deletion Callback request for a specific user. Druid does not perform scheduled or bulk deletion of Facebook users.

<a id="SettingUptheDataDeletionFlow"></a>

## Setting Up the Data Deletion Flow

To handle Facebook data deletion requests, you must first create a specific flow and then assign it to your AI Agent.

1. Create a new flow that contains the **DeteleFacebookData** internal action, which performs the anonymization required for Facebook compliance.

Extend the flow with custom logic (Optional). You can add any additional actions required by your organization's compliance or operational processes. For more information, see [Auditing and extending the deletion process](#Auditing).

2. Navigate to the AI Agent details page.
3. Click on **Dialogue Management**.
4. Scroll down and from the **Facebook data deletion flow** dropdown, select the flow you created in step 1.
5. Save the configuration.

<a id="HowItWorks"></a>

## How It Works

When Facebook sends a Data Deletion Callback request:

1. Druid validates the callback request.
2. Druid starts the Facebook Data Deletion Flow.
3. The flow executes the DeleteFacebookData internal action to anonymize the user's personal data stored by Druid.
4. Any additional actions configured in the flow are executed.

The flow is triggered separately for each Facebook user who submits a data deletion request.

<a id="Whatdataisanonymized"></a>

## What data is anonymized

The **DeleteFacebookData** internal action anonymizes personally identifiable information (PII) associated exclusively with the Facebook user identified in the callback request. This includes:

- User names and Facebook profile information
- Conversation messages and chat logs
- Raw integration payloads and NLU engine responses
- Other metadata that may contain personal information

The anonymization affects only the Facebook user that initiated the Data Deletion Callback request.

<a id="Impactondashboardsandreporting"></a>

## Impact on dashboards and reporting

Executing the Facebook Data Deletion Flow does not affect Druid reporting metrics or dashboards. The process anonymizes conversation content and personal data while preserving the metadata required for reporting and analytics.

As a result:

- Dashboard metrics remain unchanged and conversation counts are preserved.
- Historical reports remain fully consistent.
- User and conversation statistics are not recalculated.
- Deleting a Facebook user's data does not retroactively change dashboard values.

Only the personal data associated with the affected Facebook user is anonymized.

<a id="Auditingandextendingthedeletionprocess"></a>

## <a id="Auditing"></a>Auditing and extending the deletion process

Druid does not automatically create audit records for Facebook data deletion requests.

Instead, the **Facebook Data Deletion Flow** allows you to implement your own auditing and notification mechanisms.

For example, you can extend the flow to:

- store deletion events in a custom database
- send notifications to administrators
- notify external compliance systems
- create custom audit records

The **DeleteFacebookData** internal action is responsible exclusively for anonymizing Facebook user data. Any additional logging, auditing, or notification logic can be implemented by adding steps to the **Facebook Data Deletion Flow**.
