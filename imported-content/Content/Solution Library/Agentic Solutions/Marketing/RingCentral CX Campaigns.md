<a id="RingCentralCXCampaigns"></a>

# RingCentral CX Campaigns

RingCentral CX campaigns are automated outbound calling campaigns built on the Druid platform and integrated with RingCentral CX. They use a voice AI Agent to call contacts on behalf of the business and complete specific campaign goals, such as scheduling appointments, sending reminders, or collecting information.

During the call, the AI Agent can verify the contact’s identity, execute requested actions, or transfer the call to a live agent when necessary. All call outcomes are automatically saved in the Druid Data Service and displayed in campaign reports, allowing teams to review results without manual calling.

> **Info:** A ready-to-use example, the OB – Missed Recalls campaign, is included in the business app and is referenced throughout this section as an example.

<a id="HowItWorks"></a>

## How It Works

When RingCentral CX places an outbound call, it sends the call to the Druid AI Agent along with the patient’s personal information and the campaign name. This includes the patient’s name, phone number, provider and the IDs needed for scheduling. The agent stores this data for use during the conversation and creates a campaign activity in Druid.

The AI Agent then greets the caller and follows the campaign script. The conversation can take one of the following paths:

| Outcome | Description |
| --- | --- |
| OB Campaign Appointment Scheduled | The caller confirms their identity, verifies their date of birth and books the recall appointment. |
| OB Campaign Live Person Negative | The caller does not want to schedule now. The agent shares the clinic’s contact details and ends the call. |
| OB Campaign Patient Unavailable | The caller is not the patient, and the patient is not available. The call ends so the patient can be contacted later. |
| OB Campaign Transferred to Agent | The call is transferred if the caller asks for a real person, fails date-of-birth verification twice, gives a name that doesn’t match, or refuses verification but accepts help from the team. |
| OB Campaign Refused Authentication | The caller refuses to verify their identity and does not want a transfer. |
| OB Campaign Left Voicemail | A voicemail greeting is detected, and the call ends without a conversation. |
| OB Campaign Add to DNC | The caller asks not to be contacted again and is flagged for the Opted Out list. |
| OB Campaign Already Scheduled | The caller already has an upcoming appointment, so no further outreach is needed. |

Once a call terminates, the AI Agent logs the outcome (disposition), updating the activity status in Druid automatically to the matching status based on the description.
