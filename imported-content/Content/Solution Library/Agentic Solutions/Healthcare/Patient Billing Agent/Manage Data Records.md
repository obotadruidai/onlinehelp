---
title: Manage Data Records
---

# Manage Data Records

The **Billing Admin** workspace is the central repository for the agent’s intelligence. It manages the nomenclatures (static data lists) that the AI Agent uses to categorize billing needs and find the right payment plans.

### Entity Reference

The following table describes the core entities within the Patient Billing data model and their specific roles in the patient journey:

| Entity                   | Description                                                                                                                                                                             |
| ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Appointments             | Stores info about the appointment, including the medical service(name, price), provider, facility and appointment details.                                                              |
| Account (Patient)        | Stores patient profiles, including medical history (allergies, blood group), contact info, and insurance details.                                                                       |
| Payment Order            | Stores payment order information for a completed appointment.                                                                                                                           |
| Invoice                  | Stores invoice information for a payment order (if paid in full) or a payment installment (if paid with a payment plan)                                                                 |
| Payment                  | Stores payment information attached to a paid invoice.                                                                                                                                  |
| Payment Plan             | The generated payment plan for the user’s payment order. It contains a list of Installments and other important financial information (financed amount, interest amount, total amount). |
| Payment Plan Installment | Stores installment related information for the patient’s payment plan.                                                                                                                  |
| Payment Plan Template    | Generic payment plan templates that a patient can choose from to pay their balances in installments.                                                                                    |
| Invoice Status           | Tracks the Invoice lifecycle: Generated, Payment in progress (if an installment has an invoice attached), Paid partially, Paid, Overdue.                                                |
| Payment Plan Status      | Tracks if a payment plan template is active or inactive.                                                                                                                                |
| Payment Order Statuses   | Tracks the Payment Order lifecycle: New, Invoiced (if paid fully), Partially Paid (if paid in installments), and Paid.                                                                  |
| Payment Statuses         | Tracks the Payment lifecycle: New, Submitted, Finalized.                                                                                                                                |
| Payment Plan Frequencies | List of available Payment Plan durations, expressed in months                                                                                                                           |
| Payment Methods          | List of available payment methods and instructions for how to handle them.                                                                                                              |

### Add New Data Records

You can manually add individual records at any time — for example, when adding new types of Payment Plans.

To add a new record:

1. Select the **Billing Admin** workspace.
2. On the workspace menu, click the entity you wish to update (e.g., Payment Plan Template).
3. Click the **Add** icon located in the upper right corner of the page.
4. Fill in the required fields. Ensure that relationships are maintained (e.g., when adding a Payment Plan Template, link the frequency of the plan). The required relationships can be found after the initial solution data provisioning.

![](<../../../../../.gitbook/assets/plan freq.png>)

5. Save the record.

### Edit Records

To edit a record:

1. Select the **Billing Admin** workspace.
2. On the workspace menu, click the entity you wish to update (e.g., PaymentStatus).
3. Click on the record you want to update.
4. Make the desired changes.

![](<../../../../../.gitbook/assets/edit record.png>)

5. Save the record.
