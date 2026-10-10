---
layout:
  title:
    visible: false
---

<a id="Hospitality"></a>

# Hospitality

The hospitality solution is a multi-language solution that offers comprehensive support for both clients and hotel staff. Guests can effortlessly search for hotel information, book rooms, and report any room issues. Hotel employees can use the assistant to streamline their daily tasks, boosting efficiency and service quality.

<a id="SolutionSkills"></a>

## Solution Skills

This solution template provides a wide range of skills:

| Functionality | Target audience | Description |
| --- | --- | --- |
| FAQ/Knowledgebase | Guests | Guests planning a trip to Porto can ask the AI Agent questions about the hotel. |
| Book a room | Guests | Guests can book a room with the help of the AI Agent.  Note: To demonstrate voice capabilities during the Collect Feedback process, use your own phone number when booking. |
| Check-in/Check-out | Reception officers | When a guest arrives, the reception staff can use the platform’s functionalities to easily check them in or out. |
| Add a complaint | Guests | If something in the room is not working properly, guests can scan the QR code in the room and report the issue via the AI Agent. |
| Complaint management | Reception officers | The AI Agent logs all complaints, allowing reception staff to address them. A summary of complaints is available in a dedicated Druid workspace. |
| Recommendations with GPT | Guests | Guests can ask the AI Agent for recommendations on local attractions, restaurants, activities, and more. |
| Collect feedback | Guests | After check-out, the AI Agent will call the guest to collect feedback. Reception staff can trigger this call from a dedicated Druid workspace. |
| Cleaning process management | Cleaning staff | At the start of the day, cleaning staff receive a list of rooms to clean and are guided by the AI Agent through their tasks. |

<a id="Prerequisites"></a>

## Prerequisites

- Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
- You should have a AI Agent. For information on how to create an AI Agent, see [Creating AI Agents](../../2_AI%20Agents/Creating%20AI%20Agents.md).
- Enable the API Resources for Druid WebView and Druid Data Service. Then, activate the Druid Data Service in your tenant by navigating to **Administration** > **Settings** > **Druid Data Service**, and selecting **Is enabled** and clicking the **Save all** button at the top right of the page.
