<a id="RunPeopleSoftautomations"></a>

# Run PeopleSoft automations

Before retrieving data from Oracle PeopleSoft, ensure that the student record meets the required prerequisites.

The following sections describe the solution limitations and explain how to manually trigger each automation to retrieve the latest student information.

<a id="Notesandlimitations"></a>

## Notes and limitations

- The student must already exist in the Data Service before running any automation.
- The Student ID field is required. Automations cannot run without it.
- Retrievals run one student at a time; there is no bulk retrieval.
- Data is not synced automatically. You need to run the automation again to refresh it.

<a id="Howtorunautomations"></a>

## How to run automations

To run the automations:

1. In the **Education** workspace, go to **Contacts**, click the **Enrolled Students** tab, and click on the desired student record. The PeopleSoft Student Details form appears.

![](../../../../Resources/Images/PeopleSoft%20Integrations/Run%20PeopleSoft%20automations.png)

2. Click **Automations** to see the list of the five PeopleSoft automations.

![](../../../../Resources/Images/PeopleSoft%20Integrations/Run%20PeopleSoft%20automations_1.png)

3. Select the automation you want to run. A side panel opens with a confirmation message including a message if the student isn't found in PeopleSoft.
4. Close the panel and refresh the form to see the retrieved data.

The automation runs only if the student already exists in the Data Service and has a Student ID filled in on the Student Information tab. This ID is what's used to look up the student in PeopleSoft.

![](../../../../Resources/Images/PeopleSoft%20Integrations/Run%20PeopleSoft%20automations_2.png)

<a id="DataPlacementOverview"></a>

## Data Placement Overview

Each PeopleSoft automation populates a dedicated section of the PeopleSoft Student Details form.

The following table shows where the information retrieved by each automation is stored within the student record.

| Automation | Populates |
| --- | --- |
| PeopleSoft - Student Profile | **Contact Details** tab  ![](../../../../Resources/Images/PeopleSoft%20Integrations/Run%20PeopleSoft%20automations_3.png) |
| PeopleSoft - Student Tasks | **Tasks** tab  ![](../../../../Resources/Images/PeopleSoft%20Integrations/Run%20PeopleSoft%20automations_4.png) |
| PeopleSoft - Student Test Scores | **Test Scores** tab  ![](../../../../Resources/Images/PeopleSoft%20Integrations/Run%20PeopleSoft%20automations_5.png) |
| PeopleSoft - Student Admissions | **Academic Information** tab, under **Academic Degree(s)**  ![](../../../../Resources/Images/PeopleSoft%20Integrations/Run%20PeopleSoft%20automations_6.png) |
| PeopleSoft - Student Transcripts | **Transcripts** tab  ![](../../../../Resources/Images/PeopleSoft%20Integrations/Run%20PeopleSoft%20automations_7.png) |
