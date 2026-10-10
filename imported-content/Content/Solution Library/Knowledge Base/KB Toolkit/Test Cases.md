---
title: "Test Cases"
---

<a id="TestCases"></a>


A test case simulates a human tester and enables you to automate a conversation. A test case is a specification of the inputs, execution conditions, testing procedure, and expected results that define a single test to be executed to achieve a particular testing objective.

You can manually create test cases or you can import test cases from Excel files following a specific format.

To access the test cases, click **KB Test Cases** in the **KB Toolkit** workspace menu.

![](../../../Resources/Images/KB%20Toolkit/test%20cases.png)

<a id="ManuallycreateQnAtestcases"></a>

## Manually create QnA test cases

To create a QnA test case, follow these steps:

1. In the Test Case page, click the **New Record** icon in the top-right corner. This opens the test case creation page, which defaults to the **Details** tab.
2. Enter the following details in the General section:

- **Question**: Specify the question to test.
- **AI Agent**: Select the AI Agent you want to test.

3. Enter the **Expected Answer**.

![](../../../Resources/Images/KB%20Toolkit/test%20case%20create.png)

4. Click **Save** to save the test case.

{% hint style="info" %}
**Info:** You can execute a single test case by clicking the **Automations** icon and selecting **Run KB Test Case**. You can also group multiple test cases in a test plan to easily test them in bulk. For more information see, [Create Test Plans](Create%20Test%20Plans.md).

![](../../../Resources/Images/KB%20Toolkit/run%20single%20test%20case.png)
{% endhint %}

<a id="ImportQnAtestcasesfromanExcelfile"></a>

## Import QnA test cases from an Excel file

To import QnA test cases from an excel file, follow these steps:

1. On the Test Cases page, from the **Automations** drop-down, select **Download Test Case Template**. The Chat window opens and you can choose to get an empty template or a template containing all the existing data.

![](../../../Resources/Images/KB%20Toolkit/download%20template.png)

2. Click the option you prefer.

![](../../../Resources/Images/KB%20Toolkit/choose%20type.png)

{% hint style="info" %}
**NOTE:** If you choose to download the test cases template with data, note that the file will include only the QnA test cases. Advanced test cases will be excluded.
{% endhint %}

3. Click on the download link provided in the chat to download the template on your computer.

![](../../../Resources/Images/KB%20Toolkit/download%20test%20template.png)

4. Close the chat window.
5. Open the downloaded file. Enter your question in the 'Question' column and the corresponding answer in the 'Expected Answer' column. To add test cases to a specific AI Agent, enter the AI Agent name in the 'BotName' column. Add as many rows as needed for the test cases and save the file.

![](../../../Resources/Images/KB%20Toolkit/excel.png)

When importing test cases from an Excel file, records with an empty 'BotName' will appear on the KBTestCase page under the 'All AI Agents' view.

6. In the Druid Portal, from the **Automations** drop-down, select **Import Test Cases**.

![](../../../Resources/Images/KB%20Toolkit/import%20test%20cases.png)

7. In the Chat window that opens, click the **Upload File** icon. Browse for the test cases file and select it. Once the import is complete, you’ll see a notification in the chat showing how many test cases were successfully imported.

![](../../../Resources/Images/KB%20Toolkit/imported%20test%20cases.png)

8. Close the chat window and refresh the Test Case page to see all test cases.

![](../../../Resources/Images/KB%20Toolkit/all%20test%20cases.png)

<a id="Createtestscriptsadvancedmultiturnconversationsoptional"></a>

## Create test scripts – advanced multi turn conversations (optional)

To create an advanced test case for testing multi turn conversations, follow these steps:

1. In the Test Case page, click the **New Record** icon in the top-right corner. This opens the test case creation page, which defaults to the **Details** tab.
2. Enter the following details:

- Specify the **Question** to test.
- Select the **AI Agent** you want to test.
- Enter the **Expected Answer**.

![](../../../Resources/Images/KB%20Toolkit/script_details.png)

3. Click **Save** to save the test case.
4. Click on the **Test Script** tab and fill in the following parameters:

| Parameter | Description |
| --- | --- |
| Start Message | The question to test. E.g., *'I want a single insurance policy'*. |
| User profile | The context of a human tester. Write a prompt to define the persona and provide additional instructions to generative AI. E.g., *'You are an insurance broker. Provide clear and concise answers in simple terms*'. |
| Goal achieved | The script is finalized with success when the provided goal is achieved. E.g., *'There is an exact match or partial match article in the KB'*. |
| Turns Limit | The maximum number of conversation turns executed by the script. |

![](../../../Resources/Images/KB%20Toolkit/define%20script.png)

5. Click **Save** to save the test case.

<a id="ImportFeedbackasTestCases"></a>

## Import Feedback as Test Cases

Importing feedback as test cases is a proven best practice for automating User Acceptance Testing (UAT). By encouraging users to interact with the AI Agent and provide feedback during conversations, you can convert their insights into actionable test cases. These test cases can be replayed in bulk at any time, streamlining the testing process and saving countless hours of human effort.

This process allows you to refine test cases based on feedback, retest corrections, and validate improvements effectively.

<a id="WhyImportFeedbackasTestCases"></a>

### Why Import Feedback as Test Cases?

- After each test, you provide feedback using a thumbs-up or thumbs-down.
- Negative feedback indicates a mismatch between the AI Agent response and the expected answer.
- By importing feedback, you can create test cases to retest and verify that the AI Agent responses align with the expected outcomes.

<a id="BenefitsofImportingFeedback"></a>

### Benefits of Importing Feedback

- Retest negative feedback to ensure the AI Agent now delivers expected answers.
- Validate that responses with positive feedback remain accurate.
- Maintain a high standard for AI Agent performance and user satisfaction.

To import feedback as test cases, follow these steps:

1. On the workspace menu, click **Feedback**.
2. In the Feedback page, from the **Automations** drop-down, select **Export Feedback to Excel**. The Chat window opens and the feedback is exported to Excel.

![](../../../Resources/Images/KB%20Toolkit/export%20feedback.png)

3. Click on the download link provided in the chat to download the feedback file on your computer.

![](../../../Resources/Images/KB%20Toolkit/download%20feedback.png)

4. Close the chat window.
5. Open the Excel file and filter it to identify relevant feedback.
   You can filter the CreatedOn column to focus on feedback submitted during a specific time period.

![](../../../Resources/Images/KB%20Toolkit/filter%20feedback.png)

6. Download the test case template following these steps:

1. Click **Test Cases** in the **KB Toolkit** workspace menu.
2. On the Test Cases page, from the **Automations** drop-down, select **Download Test Case Template**. The Chat window opens and you can choose to get an empty template or a template containing all the existing data.

![](../../../Resources/Images/KB%20Toolkit/download%20template.png)

3. Choose **empty**.

![](../../../Resources/Images/KB%20Toolkit/choose%20type.png)

4. Click on the download link provided in the chat to download the test case template on your computer.

![](../../../Resources/Images/KB%20Toolkit/download%20test%20template.png)

5. Close the chat window.

7. Prepare Test Cases.

- For **positive feedback**:

- Copy the **Question** and **Answer** columns from the feedback file.
- Paste them into the **Question** and **ExpectedAnswer** columns in the test case template.

- For **negative feedback**:

- Copy the **Question** column from the feedback file and paste it in the **Question** column in the test case template.
- Copy the **Comments** (which usually reflect the expected answer) and paste them into the **ExpectedAnswer** column in the test case template.

8. Save the updated test case template.
9. Import the updated file as test cases:

1. In the Test Case page, from the **Automations** drop-down, select **Import Test Cases**.

![](../../../Resources/Images/KB%20Toolkit/import%20test%20cases.png)

2. In the Chat window that opens, click the **Upload File** icon. Browse for the test cases file and select it. Once the import is complete, you’ll see a notification in the chat showing how many test cases were successfully imported.

![](../../../Resources/Images/KB%20Toolkit/imported%20test%20cases.png)

3. Close the chat window and refresh the Test Case page to see all test cases.

<a id="Bulkupdatetestcasedefinition"></a>

## Bulk update test case definition

To update test cases definition in bulk, follow these steps:

1. In the Test Case page, from the **Automations** drop-down, select **Export Test Cases to Excel**.

![](../../../Resources/Images/KB%20Toolkit/export%20tests.png)

2. Click on the download link provided in the chat to download the file on your computer.
3. Close the Chat window.
4. Open the test cases file and make the desired changes, then save the file.
{% hint style="info" %}
**Info:** Keep only the test cases you want to update in the Excel file, ensuring the test case **Id** is included. If the Id is missing, new test cases will be created instead of updating the existing ones.
![](../../../Resources/Images/KB%20Toolkit/update%20tests.png)
{% endhint %}

{% hint style="info" %}
**Info:**
{% endhint %}

5. In the Test Case page, from the **Automations** drop-down, select **Import Test Cases**. The Chat window opens.
6. In the Chat window that opens, click the **Upload File** icon. Browse for the test cases file and select it. Once the import is complete, you’ll see a notification in the chat showing how many test cases were successfully imported.
