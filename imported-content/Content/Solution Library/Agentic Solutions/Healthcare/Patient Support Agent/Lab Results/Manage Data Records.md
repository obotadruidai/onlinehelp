---
title: "Manage Data Records"
---

<a id="ManageDataRecords"></a>


For medical back-office staff and solution admins

The **Lab Order Admin** workspace is the central repository for the agent’s intelligence. It manages the nomenclatures (static data lists) that the AI Agent uses to categorize the tests.

<a id="Entityreference"></a>

## Entity reference

The following table describes the core entities within the Test Result data model and their specific roles in the patient journey:

| Entity | Description |
| --- | --- |
| Appointments | Stores info about the appointment, including the medical service (name, price), provider, facility and appointment details. |
| Account (Patient) | Stores patient profiles, including contact info and the recent lab orders shown to the Test Results Status Agent. |
| LabOrder | Stores the lab order record: clinical reason, requesting provider (OrderedBy), performing laboratory, status and its list of lab order items (ordered tests). |
| LabOrderItem | A single test line on a lab order. It stores: the ordered test, performing laboratory, priority, status, information from the laboratory (Notes) and the test results once they’re processed. |
| LabResult |  |
| OrderedTest | The test catalog searched when adding or replacing a lab order item — includes category / normal range / patient preparations. |
| OrderedTestCategories | Nomenclature listing the test categories(e.g. Blood, Cardiology, Allergy). |
| LabOrderStatuses | Tracks the Lab Order lifecycle: Pending, InProgress, Resulted, Reviewed, Released, Cancelled. |
| LabOrderItemStatus | Tracks the Lab Order Item lifecycle: Draft, Active, On Hold, Cancelled, Completed, Entered In Error. |
| LabOrderItemPriority | Nomenclature listing the valid refill frequencies (e.g. Routine, Urgent) available when creating or updating a lab order item. |
| TestResultFlag | Nomenclature listing the test result flags (e.g. Normal, Low, High, Critical). |

<a id="Addnewdatarecords"></a>

## Add new data records

You can manually add individual records at any time — for example, when adding new types of Medication.

To add a new record:

1. Select the **Lab Results Admin** workspace.

1. On the workspace menu, click the entity you wish to update (e.g., Ordered Tests).

1. Click the **Add** icon located in the upper right corner of the page.

1. Fill in the required fields. Ensure that relationships are maintained (e.g., when adding a test, link the category of the test). The required relationships can be found after the initial solution data provisioning.

![](../../../../../Resources/Images/Lab%20Results%20Skill/Manage%20Data%20Records.png)

1. Save the record.

<a id="Editrecords"></a>

## Edit records

To edit a record:

1. Select the **Lab Results Admin** workspace.

1. On the workspace menu, click the entity you wish to update (e.g., Test Result Flags).

1. Click on the record you want to update.

1. Make the desired changes.

![](../../../../../Resources/Images/Lab%20Results%20Skill/Manage%20Data%20Records_1.png)

1. Save the record.
