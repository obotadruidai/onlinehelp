---
title: "Epic API inventory"
---

<a id="EpicAPIinventory"></a>

<a id="_Epic_API_inventory"></a>

The table below lists the Epic FHIR APIs used by the agent to retrieve patient data, check appointments, and book new appointments.

| Capability | Epic API or integration | Purpose | Used In |
| --- | --- | --- | --- |
| Patient Match | POST /api/FHIR/R4/Patient/$match | Resolve one patient from approved demographics when supported. | Authentication |
| Patient Read | GET /api/FHIR/R4/Patient/{ID} | Validate the selected patient and retrieve permitted demographics. | Authentication |
| Patient Create | POST /api/FHIR/R4/Patient | Validate the patient information and create a new entry. | Authentication |
| Book Appointment | POST /api/FHIR/STU3/Appointment/$book | Book the selected candidate returned by $find. | Appointment Management |
| Find Appointments | POST /api/FHIR/STU3/Appointment/$find | Return bookable Appointment candidates under the customer’s Cadence rules. | Appointment Management |
| Patient Appointments Read | GET / api/FHIR/R4/Appointment?patient={patient}&service-category=appointment | List/read appointments if enabled for the app and user context. | Appointment Management |
| Patient List | GET /api/FHIR/R4/List?code=patients&identifier={ListType}|{ListID} | Return the list of patients under the customer’s Cadence rules. | Patient View |
| Encounters | GET /api/FHIR/R4/Encounter?patient={patient} | Returns the patient’s list of encounters. | Patient 360 |
| Allergies | GET /api/FHIR/R4/AllergyIntolerance?patient={patient} | Returns the patient’s allergies. | Patient 360 |
| Care Plans | GET /api/FHIR/R4/CarePlan?patient={patient} | Returns the patient’s care plans. | Patient 360 |
| Care Teams | GET /api/FHIR/R4/CareTeam?patient={patient} | Returns the patient’s care teams. | Patient 360 |
| Clinical Notes | GET /api/FHIR/R4/DocumentReference?patient={patient}}&category=clinical-note | Returns the patient’s clinical notes. | Patient 360 |
| Conditions | GET /api/FHIR/R4/Condition?patient={patient} | Returns the patient’s conditions. | Patient 360 |
| Diagnostic Reports | GET /api/FHIR/R4/DiagnosticReport?patient={patient} | Returns the patient’s list of diagnostic reports. | Patient 360 |
| Family History | GET /api/FHIR/R4/FamilyMemberHistory?patient={patient} | Returns the patient’s family history. | Patient 360 |
| Goals | GET /api/FHIR/R4/Goal?patient={patient} | Returns the patient’s goals. | Patient 360 |
| Immunizations | GET /api/FHIR/R4/Immunization?patient={patient} | Returns the patient’s immunizations. | Patient 360 |
| Medications | GET /api/FHIR/R4/MedicationRequest?patient={patient} | Returns the patient’s medications. | Patient 360 |
| Observations | GET /api/FHIR/R4/Observation?patient={patient} | Returns the patient’s observations. | Patient 360 |
| Procedures | GET /api/FHIR/R4/Procedure?patient={patient} | Returns the patient’s procedures. | Patient 360 |
| Service Requests | GET /api/FHIR/R4/ServiceRequest?patient={patient} | Returns the patient’s service requests. | Patient 360 |
