---
layout:
  title:
    visible: false
---

<a id="ManageDataRecords"></a>

# Manage Data Records

For medical back-office staff and Solution admins

The **Appointment Admin** and **Healthcare Back-Office** workspace are the repositories for the solution intelligence. They manage the nomenclatures (static data lists) that the AI Agent uses to categorize medical needs, find the right doctors, and map locations.

<a id="EntityReference"></a>

## Entity Reference

The following table describes the core entities within the Healthcare data model and their specific roles in the patient journey:

| Entity | Description |
| --- | --- |
| Specialty | Defines medical fields (e.g., Cardiology). It includes a "Symptoms" field used by the LLM to map patient complaints to the correct professional. |
| Provider | The medical staff or doctors. Contains professional details, assigned specialties, and associated departments. |
| Medical Service | Specific procedures (e.g., "Consultation"). Each service is linked to a specialty and includes defined price and currency details. |
| Facility | The physical locations or clinics where appointments take place. Includes addresses and postal codes. |
| Department | Organizational units that group together specific Facilities, Specialties, and Providers to streamline clinic logic. |
| Timeslot | The actual availability of a Provider at a specific Facility. These are the "bookable" units searched during the scheduling flow. |
| Account (Patient) | Stores patient profiles, including medical history (allergies, blood group), contact info, and insurance details. |
| Insurance Package | A list of supported insurance types (e.g., HMO, PPO) used to validate coverage during account registration. |
| Insurance Policy | Specific policy details associated with an individual Account. |
| Healthcare Settings | Global configuration record used to enable medical guidance, set reminder intervals, and define the confirmation Website URL. |
| Account Parameter | Controls the registration form dynamically, allowing admins to toggle mandatory fields (like SSN or Insurance Details). |
| City/County/Country | Used to filter facilities by location, ensuring patients find care in their specific region. |
| Appointment Status | Tracks the visit lifecycle: New, Confirmed, Canceled, Rescheduled, Completed, or No Show. |
| Source | The specific digital channel where a patient or prospect initiated an account creation or appointment scheduling request. |

<a id="AddNewDataRecords"></a>

## Add New Data Records

You can manually add individual records at any time — for example, when onboarding a new doctor or opening a new clinic.

To add a new record:

1. Select the **Admin** workspace.
2. On the workspace menu, click the entity you wish to update (e.g., Specialty).
3. Click the **Add** (+) icon located in the upper right corner of the page.
4. Fill in the required fields. Ensure that relationships are maintained (e.g., when adding a Specialty, link them to an Department). The required relationships can be found after the initial provisioning on other records.

![](../../../../Resources/Images/Agentic%20Healthcare/add%20record.png)

5. Save the record.

<a id="EditRecords"></a>

## Edit Records

To edit a record:

1. Select the **Admin** workspace.
2. On the workspace menu, click the entity you wish to update (e.g., ProviderMedicalService).
3. Click on the record you want to update.
4. Make the desired changes.

![](../../../../Resources/Images/Agentic%20Healthcare/edit%20data.png)

5. Save the record.
