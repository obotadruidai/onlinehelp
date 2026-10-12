---
title: "Data Model and Workspace References"
---

<a id="DataModelandWorkspaceReferences"></a>


The Academic Advisor Agent structures its data across three purpose-built workspaces, each scoped to a specific user role and exposes only the entities relevant to that role — giving staff, administrators and instructors access to the information they need.

<a id="AdminWorkspaceDataReference"></a>

## Admin Workspace Data Reference

Solution administrators use the Admin workspace to configure and maintain the reference data the AI Agent depends on. It provides full CRUD (create, read, update, and delete) access to the core lookup entities. that drive academic logic: campuses, degrees, academic levels, semesters, student classifications, and enrollment status types.

| Entity | Description |
| --- | --- |
| Campus | The physical or virtual campuses associated with the institution. |
| CourseStatus | Stores the enrollment status of a course for a student. Possible values: Withdrawn, Incomplete, In Progress, Complete, and Failed. |
| Degrees | Defines all degree types offered by the institution. |
| AcademicLevel | Defines academic standing levels (e.g., Freshman, Sophomore, Junior, Senior). |
| AcademicPeriod | Stores all academic semesters and terms (e.g., Fall 2024, Spring 2025, Summer 2025). The active period is used as the default semester when students browse or enroll in courses without specifying a term. Must be kept current as new terms open. |
| InstructorStatus | Tracks the current employment standing of each instructor (e.g., Active, On Leave, Retired). |
| InstructorType | Identifies the employment classification of each instructor (e.g., Full Time, Part Time, Adjunct, Visiting). |
| InstructorTitle | Identifies the academic rank of each instructor (e.g., Professor, Associate Professor, Assistant Professor, Lecturer, Senior Lecturer, Instructor, Teaching Assistant). |
| StudentStatuses | Tracks the current enrollment standing of each student (e.g., Declared, Undeclared, Prospect, Suspended). |
| StudentTypes | Classifies students into institutional categories (e.g., International Student, In-State Student, Out-of-State Student). Used for eligibility rules, tuition logic, and enrollment reporting. |

<a id="EducationWorkspaceDataReference"></a>

## Education Workspace Data Reference

| Entity | Description |
| --- | --- |
| Contact | The primary contact record. There are two types of Contacts: student and instructor. Stores personal details including name, email address, phone number, date of birth, and linked academic program. The phone number field is the key identifier used during agent authentication. All student and instructor-specific operations begin by with a Contact record. |
| Departments | Defines the academic departments and colleges within the institution (e.g., Computer Science, Mathematics). The agent organizes course browse results by department and validates enrollment against departmental rules. |
| InstructorCourse | The course catalog. Contains all courses available for enrollment, including course code, title, description, associated department, prerequisites, and semester availability. This is the primary entity queried when a student asks about available courses. |

<a id="SystemEntities"></a>

## System Entities

| Entity | Description |
| --- | --- |
| EducationAdvisorSettings | Central configuration including data provisioning and AI Agent personality and institution rules. |
| HigherEdHelper | A system-level configuration entity that holds global agent settings, behavioral parameters, and operational flags used to tune the AI Agent responses and workflow rules. |

<a id="BusinessEntities"></a>

## Business Entities

These entities are provisioned as part of the data model setup; records are created and managed at runtime by students, and business processes.

| Entity | Description |
| --- | --- |
| AcademicProgram | Defines the structured degree programs offered by the institution, linking degrees, academic units, and required course sets. Used to validate a student’s program eligibility and to display program details when students inquire about their enrollment. |
| EnrolledStudentCourse | Links students to individual course enrollments. Used for schedule and history queries. |
| EnrolledStudentProgram | Links students to their enrolled academic programs. |
