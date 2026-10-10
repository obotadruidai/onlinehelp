<a id="Druid925"></a>

# Druid 9.25

| Druid Cloud US  \*.us.Druidplatform.com | Druid Cloud Australia  \*au.Druidplatform.com | Druid Cloud West-Europe (PROD)  \*.Druidplatform.com |
| --- | --- | --- |
| July 02, 2026 | July 02, 2026 | July 02, 2026 |

These release notes provide a high-level overview of new features and improvements in the business apps.

<a id="Healthcare"></a>

## Healthcare

<a id="OutboundPatientEngagementAgent"></a>

### Outbound Patient Engagement Agent

The Outbound Patient Engagement Agent is the core outreach engine for proactive patient communication. Launching in v9.25 with three foundational skills, it enables healthcare organizations to automate personalized outreach at scale — reducing administrative overhead while keeping patients engaged and informed:

- **No Show Skill** - The No Show Skill proactively contacts patients who missed their appointments through automated outreach, prompting them to reschedule and reducing the revenue impact of unfilled slots. It captures the reason for the no-show where possible, feeding data back into scheduling analytics for continuous operational improvement.
- **Balance Notifications Skill** - The Balance Notifications Skill sends timely, automated reminders to patients with outstanding account balances, reducing the time to engage with clients that have overdue invoices and the need for manual collections follow-up. Notifications are tailored to the patient's communication preferences and include direct payment links to maximize conversion rates.
- **Demographic Updates Skill** - The Demographic Updates Skill proactively contacts patients to verify and refresh their personal information — including address, contact details, and insurance data — at regular intervals. Maintaining accurate demographic records improves care coordination, reduces claim rejections, and supports regulatory compliance requirements.

> **NOTE:** The Outbound Patient Engagement Agent supports **voice campaigns only**.

<a id="PatientBillingAgent"></a>

### Patient Billing Agent

- **Billing Dashboard & Analytics Skill** - The Billing Dashboard Skill surfaces a consolidated view of patient billing activity — including payment statuses, outstanding balances, and recent transactions — directly within the agent's workspace. It enables billing staff to act quickly on exceptions and provides the context needed to resolve patient queries on first contact.

<a id="HigherEducation"></a>

## Higher Education

<a id="OutboundStudentEngagementAgent"></a>

### Outbound Student Engagement Agent

The Outbound Student Engagement Agent enables institutions to transition from reactive to proactive student engagement by automating personalized outreach across the admissions funnel, enrollment funnel, and active student body. Launching with four distinct skills targeting enrolled students, it helps improve overall student academic performance and experience.

- **Missing Major Campaign Skill** – The Missing Major Campaign Skill periodically engages sophomore and junior students who have not yet chosen a field of specialization or degree. By analyzing academic records and student interests, it delivers tailored encouragement and guidance to help students confidently select a major and stay on track for graduation.
- **Student Counselling Campaign Skill** – The Student Counselling Campaign Skill automates targeted outreach to students with failing grades, guiding them directly into advisor appointment scheduling and general counselling for improving their performance. It acts as an early intervention tool to help struggling students get the immediate academic support they need.
- **Student Counselling Follow-up Skill** – The Student Counselling Follow-up Skill manages automated communication to check on student progress, triggered when students explicitly request subsequent performance follow-up sessions. It ensures continuous engagement and progress monitoring throughout the academic term.
- **Freshman Orientation Campaign Skill** – The Freshman Orientation Campaign Skill streamlines student onboarding by actively assisting incoming freshmen with essential orientation activities. It drives early campus engagement by guiding students through event participation and automating the first-time class registration process.
> **NOTE:** The Outbound Student Engagement Agent supports **voice campaigns only**.

<a id="OperationalTools"></a>

## Operational Tools

<a id="AIEngagementAnalyst"></a>

### AI Engagement Analyst

**Metrics Configuration Audit Logs.** You can now track configuration changes made to metrics and metric options directly from the **Conversation Toolkit Admin** workspace, making it easier to troubleshoot reporting issues and maintain consistent dashboard configurations.

Key benefits include:

- **Complete change history** – Every update to a metric or metric option name or description is automatically recorded, providing full visibility into configuration changes.
- **Easy rollback reference** – Audit logs display the original system values first, followed by all subsequent changes in chronological order, helping administrators identify baseline values and manually restore previous configurations when needed.
- **Centralized auditing** – Review the complete change history from the Audit tab available for each metric and metric option in the Conversation Toolkit Admin workspace.

Metric Audit

![](../../../../Resources/Images/AI%20Engagement%20Analyst/metric%20audit.png)

Metric Options Audit

![](../../../../Resources/Images/AI%20Engagement%20Analyst/metric%20options%20audit.png)

This enhancement improves configuration traceability, simplifies troubleshooting, and helps preserve reporting consistency across environments.
