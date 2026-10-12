---
title: Manage Data Records
---


For solution admins

While the solution comes with a predefined set of records, and you might also already have your institution data stored in Druid Data Service, admins can manually add new records based on the needs in the Admin workspace.

## Update degree offerings

Degrees are academic credentials or titles awarded by colleges and universities upon the successful completion of a structured program of study.

You can add new degree types to the offering (e.g., Bachelor of Science, Master of Arts). The **AI Agent** uses the degree types and their description when answering student questions about available programs and degree requirements.

To add a new degree:

1. On the **Admin** workspace menu, click on **Degrees**.
2. Click the **New AcademicDegree** icon at the top right corner of the page.
3. Fill in the following fields:

| Field       | Description                                                                                 |
| ----------- | ------------------------------------------------------------------------------------------- |
| Name        | The name of the degree.                                                                     |
| Description | The description the AI Agent uses when answering student questions. This field is optional. |

![](<../../../../../.gitbook/assets/Manage Data Records for solution_4.png>)

4. Save and close the form.

## Classify Academic Levels

Academic Level defines a student's standing in their degree program. The AI Agent uses Academic Level to apply level-specific enrollment rules and tailor course recommendations to the student's stage in their program.

| Academic Level | Description                                                                                                   |
| -------------- | ------------------------------------------------------------------------------------------------------------- |
| Freshman       | A first-year undergraduate student, typically in the initial stage of their degree program.                   |
| Sophomore      | A second-year undergraduate student, continuing foundational coursework and beginning to explore their major. |
| Junior         | A third-year undergraduate student, focused on major-specific coursework and program requirements.            |
| Senior         | A fourth-year undergraduate student, completing final degree requirements and preparing for graduation.       |

To add a new academic level:

1. On the **Admin** workspace menu, click on **Academic Levels**.
2. Click the **New AcademicLevel** icon at the top right corner of the page.
3. Fill in the following fields:

| Field       | Description                                                                                 |
| ----------- | ------------------------------------------------------------------------------------------- |
| Name        | The name of the level.                                                                      |
| Description | The description the AI Agent uses when answering student questions. This field is optional. |

4. Save the form.

## Add New Semesters

Academic Periods lists the academic semesters and terms (e.g., Fall 2024, Spring 2025). The AI Agent uses the active period as the default semester when students browse or enroll in courses.

To add a new semester for the upcoming term so students can enroll in courses for that period:

1. On the **Admin** workspace menu, click on **Academic Periods**.
2. Click the **New AcademicPeriod** icon at the top right corner of the page.
3. In the form, enter the name of the new academic period, the start date and end date and save the form.

![](<../../../../../.gitbook/assets/Manage Data Records for solution_1.png>)

## Understand Student Enrollment Status

The system tracks the following enrollment statuses for each course:

* **In Progress**: The students are actively enrolled and the course is currently underway. Attendance, assignments, and assessments are ongoing.
* **Incomplete**: The student has submitted a request to retake this course in the following academic year. The course will remain on the student record until successfully completed.
* **Withdrawn**: The student has withdrawn from the course. This action may have academic and financial implications depending on the withdrawal deadline.
* **Complete**: The course has been successfully concluded and a final grade has been recorded on the student's academic record.

When the student starts a conversation, the AI Agent identifies the intent and guides the student through the appropriate steps. Sensitive operations require identity verification first.

## Classify students in categories

Student classification is defined by two primary categories: student type and student status. These indicators determine a learner's residency, academic path, and eligibility for institutional actions.

### Student types

Student type primarily identifies the residency and tuition classification of the learner:

* **International student**: A learner attending the institution from outside the country.
* **In-state student**: A learner who meets local residency requirements for regional tuition rates.
* **Out-of-state student**: A learner who resides within the country but outside the local tuition jurisdiction.

The AI Agent uses student status and student type to manage enrollment:

* Student status determines access. The AI Agent checks if a learner is eligible to perform actions (e.g., a Declared student can register, while a Suspended student or Prospect cannot).
* Student type determines requirements. The AI Agent applies specific rules based on residency (e.g., calculating different tuition rates for an In-State student versus an International student).

To add a new student type:

1. On the **Admin** workspace menu, click on **Student Types**.
2. Click the **New StudentType** icon at the top right corner of the page.
3. Fill in the following fields:

| Field       | Description                                                                                 |
| ----------- | ------------------------------------------------------------------------------------------- |
| Name        | The name of the category.                                                                   |
| Description | The description the AI Agent uses when answering student questions. This field is optional. |

4. Save and close the form.

### Student statuses

Student status defines the current academic standing or progress of the learner:

* **Prospect**: A potential learner who has expressed interest but is not yet enrolled.
* **Undeclared**: An active student who has not yet selected a specific major or field of study.
* **Declared**: An active student who has officially selected and been accepted into a specific major.
* **Suspended**: A student who is temporarily prohibited from participating in academic activities.

To define a new student status:

1. On the **Admin** workspace menu, click on **Student Statuses**.
2. Click the **New StudentStatus** icon at the top right corner of the page.
3. Fill in the following fields:

| Field       | Description                                                                                 |
| ----------- | ------------------------------------------------------------------------------------------- |
| Name        | The name of the status.                                                                     |
| Description | The description the AI Agent uses when answering student questions. This field is optional. |

4. Save and close the form.

## Add New Campuses

You can define the physical or virtual campuses associated with the institution. The AI Agent uses campus information when answering student questions about location-specific resources and events.

To add a new campus:

1. On the **Admin** workspace menu, click on **Campus**.
2. Click the **New Campus** icon at the top right corner of the page.
3. Fill in the following fields:

| Field            | Description                                                                                                                                                                                                                                                     |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name             | The name of the campus (e.g., Main Campus, Forest Campus).                                                                                                                                                                                                      |
| Address          | The address of the campus location.                                                                                                                                                                                                                             |
| City             | The city where the campus is located.                                                                                                                                                                                                                           |
| State            | The state or province where the campus is located.                                                                                                                                                                                                              |
| Country          | The country where the campus is located.                                                                                                                                                                                                                        |
| Office Locations | In the view on the form, click the **New Record** icon above the table. The New Office Location form appears. Enter a location name, then select the Campus from the dropdown. ![](<../../../../../.gitbook/assets/OFFICE RECORD.png>) Save and close the form. |

4. Save and close the form.

## Define Instructor Statuses

Instructor Status defines the current employment standing of an instructor. The AI Agent uses Instructor Status to determine whether an instructor is available to teach courses in the current academic period.

The following instructor statuses are provisioned by default: Active, On Leave, and Retired.

To add a new instructor status:

1. On the **Admin** workspace menu, click on **Instructor Status**.
2. Click the **New InstructorStatus** icon at the top right corner of the page.
3. Enter the name of the status.
4. Save and close the form.

## Define Instructor Types

Instructor Type identifies the employment classification of an instructor. The AI Agent uses the Instructor Type to determine teaching load, course assignment eligibility, and scheduling availability.

The following instructor types are provisioned by default: Full Time, Part Time, Adjunct, and Visiting.

To add a new instructor type:

1. On the Admin workspace menu, click on **Instructor Type**.
2. Click the **New Instructor Type** icon at the top right corner of the page.
3. Enter the name of the type.
4. Save and close the form.

## Add Instructor Titles

Instructor Title identifies the academic rank of an instructor. The AI Agent uses the Instructor Title to apply rank-specific rules for course assignment, supervision, and academic responsibilities.

The following instructor titles are provisioned by default:: Professor, Associate Professor, Assistant Professor, Lecturer, Senior Lecturer, Instructor, and Teaching Assistant.

To add a new instructor title:

1. On the **Admin** workspace menu, click on **Instructor Title**.
2. Click the **New InstructorTitle** icon at the top right corner of the page.
3. Enter the name of the title.
4. Save and close the form.
