<a id="ManageDataRecords"></a>

# Manage Data Records

The **Outbound Admin** workspace is the central repository for the agent’s intelligence. It manages the nomenclatures (static data lists) that the AI Agent uses to categorize campaign needs and use the right audience filters.

<a id="EntityReference"></a>

## Entity Reference

The following table describes the core entities within the Outbound Patient Engagement data model and their specific roles in the patient journey:

| Entity | Description |
| --- | --- |
| Audience | Defines the target group for a campaign. |
| AudienceMember | Represents an individual Contact within an audience. |
| AudienceMemberStatus | Tracks the current status of an audience member. |
| AudienceMemberTemp | Temporary holding entity for audience member processing. |
| Campaign | Stores campaign definition, type, status, and dates. |
| CampaignActivity | Logs each individual outreach attempt per student. |
| CampaignActivityStatus | Defines possible statuses for a campaign activity. |
| CampaignChannel | Defines the delivery channel (Voice, SMS, Web). |
| CampaignRecipient | Links a contact to a campaign run. |
| CampaignRunAudit | Audit trail for each campaign execution run. |
| CampaignScript | Stores the conversational script used by the agent. |
| CampaignSettings | Holds global configuration settings for campaigns. |
| CampaignStatus | Defines the possible statuses of a campaign. |
| CampaignStep | Defines a step within a campaign, including channel and audience. |
| CampaignType | Classifies the campaign type (e.g. Notification, Survey). |
| Account (Patient) | Stores patient profiles, including medical history (allergies, blood group), contact info, and insurance details. Used in the No Show and Demographic Verification Campaigns. |
| Invoice | Stores invoice information for a payment order (if paid in full) or a payment installment (if paid with a payment plan). Used in the Balance Outreach Campaign. |
