---
title: "Expense Booking with OCR"
---

<a id="ExpenseBookingwithOCR"></a>


This solution empowers users to upload documents, such as invoice receipts, directly into a conversation. The AI Agent processes these documents using Optical Character Recognition (OCR) to extract key information, which is then securely stored for easy access and future use.

<a id="SolutionSkills"></a>

## Solution Skills

| Functionality | Description |
| --- | --- |
| Book a travel expense | Upload invoices or receipts directly into the conversation. The AI Agent uses Optical Character Recognition (OCR) to extract key information from the document and saves it in a dedicated Druid Workspace. |
| Approval process | View extracted document information in a dedicated workspace.  Back-office employees review the information and approve or reject the travel expense. |

<a id="Prerequisites"></a>

## Prerequisites

- Tenant Druid community (open new tenant [here](https://www.druidai.com/license-activation)) or Druid subscription.
- You should have a AI Agent. For information on how to create an AI Agent, see [Creating AI Agents](https://druidai.gitbook.io/druid-ai-docs/ai-platform/build-ai-agents/authoring-tools/creating-ai-agents).
- Enable the API Resources for Druid WebView and Druid Data Service. Then, activate the Druid Data Service in your tenant by navigating to **Administration** > **Settings** > **Druid Data Service**, and selecting **Is enabled** and clicking the **Save all** button at the top right of the page.
