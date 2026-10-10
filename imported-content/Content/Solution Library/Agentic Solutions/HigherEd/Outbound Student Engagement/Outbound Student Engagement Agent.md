---
title: "Outbound Student Engagement"
---

<a id="OutboundStudentEngagement"></a>


The Outbound Student Engagement Agent is a solution designed to help higher education institutions transition to proactive student engagement. It automates personalized outreach across the enrollment funnel, enabling academic and admissions teams to scale their efforts without increasing headcount.

At the core of the solution is an outbound engagement engine that proactively initiates contact with students across Voice (AudioCodes) and optional SMS (Twilio) and Web (Direct Line). The Voice channel enables the agent to place real outbound calls to students conducting natural, GPT-driven conversations without any human operator involved. Campaigns are triggered by alerts that monitor student records continuously, firing automatically when a qualifying condition is met, with no manual intervention required from staff.

<a id="StudentEngagementSkills"></a>

## Student Engagement Skills

The solution includes three preconfigured agentic skills:

- **Missing Major Campaign Skill** – The Missing Major Campaign Skill periodically engages sophomore and junior students who have not yet chosen a field of specialization or degree. By analyzing academic records and student interests, it delivers tailored encouragement and guidance to help students confidently select a major and stay on track for graduation.
- **Student Counselling Campaign Skill** – The Student Counselling Campaign Skill automates targeted outreach to students with failing grades, guiding them directly into advisor appointment scheduling and general counselling for improving their performance. It acts as an early intervention tool to help struggling students get the immediate academic support they need.
- **Student Counselling Follow-up Skill** – The Student Counselling Follow-up Skill manages automated communication to check on student progress, triggered when students explicitly request subsequent performance follow-up sessions. It ensures continuous engagement and progress monitoring throughout the academic term.
- **Freshman Orientation Campaign Skill** – The Freshman Orientation Campaign Skill streamlines student onboarding by actively assisting incoming freshmen with essential orientation activities. It drives early campus engagement by guiding students through event participation and automating the first-time class registration process.

<a id="KeyComponents"></a>

## Key Components

The main components of the solution include:

- **Business workflows**. Dedicated workflows for running the student engagement campaigns and storing the information.
- Two dedicated workspaces.
  - **Campaign & Contacts** - The primary workspace for business users and campaign managers. It provides a central interface for managing campaigns, contacts, audiences, survey responses, campaign activities, and message templates - everything needed to create, run, and monitor outbound engagement campaigns.
  - **Outbound Admin** - The configuration workspace for administrators. It manages the reference data and operational settings the solution depends on, including campaign statuses, audience member statuses, campaign types, activity statuses, campaign channels, language codes, audience filters, and campaign settings.
- **Data Model**. Contains all essential entities.
