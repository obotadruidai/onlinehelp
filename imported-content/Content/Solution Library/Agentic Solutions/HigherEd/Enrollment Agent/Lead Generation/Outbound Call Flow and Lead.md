---
layout:
  title:
    visible: false
---

<a id="OutboundCallFlowandLeadExperience"></a>

# Outbound Call Flow and Lead Experience

When triggered, the outbound campaign initiates a voice call to each target audience member. The interaction follows a structured call flow based on lead validation and response:

1. **Introduction & Identity Verification**

- The agent delivers a personalized greeting introducing the institution and the reason for the call.
- The agent verifies lead identity against existing records (full name, phone number, and email).

2. **Branching Outcomes**

- Verified Lead: If identity details match, the agent proceeds with the discovery questions.
- Incorrect Details: If the lead indicates the details are incorrect, the agent skips the survey and offers to connect them with an advisor.
- Unrelated Party: If the recipient has no connection to the university, the agent apologizes and concludes the call.

3. **Discovery Survey & Response Tracking**

- The agent asks short discovery questions sequentially.
- Answers, along with completion status, timestamps, call duration, and response values, are saved and visible in the Survey Responses tab on the contact record.

![](../../../../../Resources/Images/Lead%20Generation%20Skill/Outbound%20Call%20Flow%20and%20Lead.png)

![](../../../../../Resources/Images/Lead%20Generation%20Skill/Outbound%20Call%20Flow%20and%20Lead_1.png)

![](../../../../../Resources/Images/Lead%20Generation%20Skill/Outbound%20Call%20Flow%20and%20Lead_2.png)

4. **Advisor Scheduling & Interaction Summary**

- If an advisor follow-up is requested, the agent agrees on a date and time with the lead, confirming the appointment slot and contact phone number.
- Upon call completion, a full conversation summary and follow-up details save automatically to the interaction record.

![](../../../../../Resources/Images/Lead%20Generation%20Skill/Outbound%20Call%20Flow%20and%20Lead_3.png)
