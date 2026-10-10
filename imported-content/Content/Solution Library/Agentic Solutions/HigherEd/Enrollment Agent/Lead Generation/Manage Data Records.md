<a id="ManageDataRecords"></a>

# Manage Data Records

All lead, student and outbound campaign data used by the solution is stored in the Druid Data Service, where you can review, update, or delete the records. The entities below represent the core building blocks the solution uses to orchestrate and record all outbound engagement operations.

| Entity | Description |
| --- | --- |
| Address | Stores the postal address associated with a contact. |
| Audience | Defines the target group for a campaign. |
| AudienceFilter | Defines the filtering criteria used to build an audience. |
| AudienceMember | Represents an individual student within an audience. |
| AudienceMemberStatus | Tracks the current status of an audience member. |
| AudienceMemberTemp | Temporary holding entity for audience member processing. |
| AudioCodes | Configuration/integration with the AudioCodes platform (voice channel). |
| Campaign | Stores campaign definition, type, status, and dates. |
| CampaignActivity | Logs each individual outreach attempt per student. |
| CampaignActivityStatus | Defines possible statuses for a campaign activity. |
| CampaignChannel | Defines the delivery channel (Voice, SMS, Web). |
| CampaignHelper | Auxiliary/utility entity used in campaign processing. |
| CampaignRecipient | Links a student contact to a campaign run. |
| CampaignRunAudit | Audit trail for each campaign execution run. |
| CampaignSettings | Holds global configuration settings for campaigns. |
| CampaignStatus | Defines the possible statuses of a campaign. |
| CampaignStep | Defines a step within a campaign, including channel and audience. |
| CampaignType | Classifies the campaign type (e.g. Notification, Survey). |
| Contact | Stores information about a contact/student. |
| ContactType | Classifies the type of contact. |
| CurrentFlow | Tracks the current flow/stage a contact is in within a campaign. |
| EducationAdvisorSettings | Stores the Bot Name, University Name, Rules and Prompts. |
| EmailTemplate | Stores the email templates used in campaigns. |
| ExcelReport | Stores reports generated in Excel format. |
| General | Entity holding general system settings/configuration. |
| ImportContact | Manages the import of contacts into the system. |
| ImportData | Manages the import of raw data into the system. |
| LanguageCode | Defines the available language codes. |
| Lead | Umbrella entity for the Lead Generation Campaign. |
| StudentSuccessInteraction | Stores the summary of the conversation and follow-up data captured during an interaction. |
| SurveyQuestionResponse | Stores individual student responses to survey questions. |
| SurveyResponse | Stores the full survey response record per interaction. |
| TempContact | Temporary entity for contact import. |
| Validate | Entity used for data validation. |
