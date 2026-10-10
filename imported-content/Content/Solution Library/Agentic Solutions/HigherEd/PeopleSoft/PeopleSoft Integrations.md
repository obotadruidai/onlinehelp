---
layout:
  title:
    visible: false
---

<a id="RetrieveStudentDataFromPeopleSoft"></a>

# Retrieve Student Data From PeopleSoft

The **PeopleSoft Integrations Skill** enables Druid AI Agents to retrieve student information directly from Oracle PeopleSoft Campus Solutions and make it available during conversations and business automations.

By accessing student records in real time, AI Agents can answer questions, support advisors, and enrich education workflows without requiring users to manually search for information across multiple systems.

<a id="Howitworks"></a>

## How it works

The skill communicates with Oracle PeopleSoft Campus Solutions through REST endpoints exposed by your institution. Each request uses the student's Student ID to retrieve the latest information directly from PeopleSoft.

Once the student has been identified, AI Agents can retrieve profile information, tasks, test scores, admissions data, and transcript records as needed.

<a id="AvailablePeopleSoftautomations"></a>

## Available PeopleSoft automations

The solution includes five predefined automations, each designed to retrieve a specific category of student information from Oracle PeopleSoft.

When an automation is triggered from a student record, the retrieved information is stored in the Druid Data Service, where it becomes available to other solution components.

| Automation | Retrieves |
| --- | --- |
| Student Profile | Identity, contact details, mailing address, residency status, and assigned advisors. |
| Student Tasks | Checklists and checklist items, with status, due dates, instructions, and any holds on the record. |
| Student Test Scores | Standardized test results, by component, with score, test date, and reporting agency. |
| Student Admissions | Admissions application details: career, program and plan, admit term and type, program status, and completeness. |
| Student Transcripts | Transcripts on file from previous institutions, with academic career, level, term type, and receipt status. |
