---
layout:
  title:
    visible: false
---

<a id="ManageDataRecords"></a>

# Manage Data Records

The Outbound Student Engagement solution is built on a structured data model that covers the full campaign lifecycle, from audience definition and campaign configuration through to activity tracking, interaction logging, and outcome storage. The entities below represent the core building blocks the solution uses to orchestrate and record all outbound engagement operations.

| Entity | Description |
| --- | --- |
| Audience | Defines the target group for a campaign. |
| AudienceMember | Represents an individual student within an audience. |
| AudienceMemberStatus | Tracks the current status of an audience member. |
| AudienceMemberTemp | Temporary holding entity for audience member processing. |
| Campaign | Stores campaign definition, type, status, and dates. |
| CampaignActivity | Logs each individual outreach attempt per student. |
| CampaignActivityStatus | Defines possible statuses for a campaign activity. |
| CampaignChannel | Defines the delivery channel (Voice, SMS, Web). |
| CampaignRecipient | Links a student contact to a campaign run. |
| CampaignRunAudit | Audit trail for each campaign execution run. |
| CampaignScript | Stores the conversational script used by the agent. |
| CampaignSettings | Holds global configuration settings for campaigns. |
| CampaignStatus | Defines the possible statuses of a campaign. |
| CampaignStep | Defines a step within a campaign, including channel and audience. |
| CampaignType | Classifies the campaign type (e.g. Notification, Survey). |
| Counselling | Umbrella entity for the Student Counselling and Counselling Follow Up campaigns. |
| FreshmanOrientation | Umbrella entity for the Freshman Orientation campaign. |
| NoDeclaredMajor | Umbrella entity for the No Declared Major campaign. |
| SurveyQuestionResponse | Stores individual student responses to survey questions. |
| SurveyResponse | Stores the full survey response record per interaction. |

<a id="AcademicAdvisorEntities"></a>

## Academic Advisor Entities

The following entities extend the data model to support the academic advising workflows triggered during outbound interactions. They store the student academic context, appointment availability, and interaction outcomes that the agent relies on during counselling and follow-up campaigns.

| Entity | Description |
| --- | --- |
| StudentSuccessInteraction | Stores the summary, barriers, and next steps captured during a student counselling or follow-up interaction. |
| AdvisorTimeslot | Holds available and upcoming appointment slots for academic advisors, used during counselling scheduling interactions. |
| Grade | Stores student grades data. |
