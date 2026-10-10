<a id="OutboundPatientEngagementAgent"></a>

# Outbound Patient Engagement Agent

The **Outbound Patient Engagement Agent** is the core outreach engine for proactive patient communication. It comes in with three foundational skills and enables healthcare organizations to automate personalized outreach at scale — reducing administrative overhead while keeping patients engaged and informed.

At the core of the solution is an outbound engagement engine that proactively initiates contact with patients across Voice (AudioCodes) and optional SMS (Twilio) and Web (Direct Line). The Voice channel enables the AI Agent to place real outbound calls to patients conducting natural, LLM-driven conversations without any human operator involved. Campaigns are triggered by alerts that monitor patient records continuously, firing automatically when a qualifying condition is met, with no manual intervention required from staff.

<a id="PatientEngagementSkills"></a>

## Patient Engagement Skills

The solution includes three preconfigured agentic skills:

- **No Show Skill** - The skill proactively contacts patients who missed their appointments through automated outreach, prompting them to reschedule and reducing the revenue impact of unfilled slots. It captures the reason for the no-show where possible, feeding data back into scheduling analytics for continuous operational improvement.
- **Balance Notifications Skill** - The skill sends timely, automated reminders to patients with outstanding account balances, reducing the time to engage with clients that have overdue invoices and the need for manual collections follow-up. Notifications are tailored to the patient's communication preferences and include direct payment links to maximize conversion rates.
- **Demographic Updates Skill** - The skill proactively contacts patients to verify and refresh their personal information — including address, contact details, and insurance data — at regular intervals. Maintaining accurate demographic records improves care coordination, reduces claim rejections, and supports regulatory compliance requirements.

<a id="KeyComponents"></a>

## Key Components

The main components of the solution include:

- **Business workflows**. Dedicated workflows for running the patient engagement campaigns and storing the information.
- Two dedicated workspaces.

- **Campaign & Contacts** - The primary workspace for business users and campaign managers. It provides a central interface for managing campaigns, contacts, audiences, survey responses, campaign activities, and message templates - everything needed to create, run, and monitor outbound engagement campaigns.
- **Outbound Admin** - The configuration workspace for administrators. It manages the reference data and operational settings the solution depends on, including campaign statuses, audience member statuses, campaign types, activity statuses, campaign channels, language codes, audience filters, and campaign settings.

- **Data Model**. Contains all essential entities.
