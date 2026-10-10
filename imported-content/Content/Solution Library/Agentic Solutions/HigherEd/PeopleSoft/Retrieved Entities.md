<a id="RetrievedEntities"></a>

# Retrieved Entities

When a PeopleSoft automation retrieves student information, the data is stored in the Druid Data Service as a set of reusable entities.

These entities are used throughout the solution in forms, dashboards, reports, automations, and other components. Because the data is stored in the Data Service, it can also be reviewed, updated, or deleted independently of the source system.

| Name | Description |
| --- | --- |
| AcademicCareer | The student's academic career (for example Undergraduate or Graduate). |
| AcademicLevel | The student's academic level within a given term. |
| AcademicPeriod | The academic period or term (Spring, Fall). |
| Address | The student's address. |
| CheckItem | A checklist item associated with the student. |
| Contact | The student's contact details. |
| EnrolledStudentProgram | The academic program the student is enrolled in. |
| ProgramStatus | The status of the academic program (active, withdrawn, and so on). |
| StudentAdvisor | The advisor assigned to the student. |
| StudentCheck | Specific checks related to the student. |
| StudentHold | Holds or restrictions applied to the student's account. |
| StudentTest | Tests taken by the student. |
| StudentTranscript | The student's transcript. |
| TermType | The type of academic term. |
| TestComponent | A component of a test (sub-section or partial score). |
| TranscriptRecord | An individual record within the transcript. |
| ExtractedStudent | The umbrella entity used for pulling student data from PeopleSoft to perform batch add operations. |
