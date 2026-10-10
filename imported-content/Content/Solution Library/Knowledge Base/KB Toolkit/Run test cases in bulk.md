<a id="RunTestPlansandAnalyzeResults"></a>

# Run Test Plans and Analyze Results

Running test cases in bulk ensures thorough testing and helps maintain the quality of your AI Agent performance. It allows you to efficiently test multiple scenarios within a test plan.

<a id="Createtestrun"></a>

## Create test run

To create a test run for a specific test plan, in the Test Plan page, click on the desired test plan.

From the **Automations** drop-down, select **Create Test Run**.

![](../../../Resources/Images/KB%20Toolkit/create%20test%20run.png)

DRUID fetches the test plan details and creates a test run.

A chat window appears on the right-hand side of the screen, providing updates and confirming when the test run is created.

![](../../../Resources/Images/KB%20Toolkit/test%20run%20created.png)

<a id="Executetestrun"></a>

## Execute test run

To execute a test run, follow these steps:

1. On the workspace menu, click **KB Test Runs**. The Test Run page appears.

![](../../../Resources/Images/KB%20Toolkit/test%20run%20page.png)

2. Click on the desired test run. The Test Run configuration page appears.
3. From the **Automations** drop-down, select **Run KB+ GPT**.

![](../../../Resources/Images/KB%20Toolkit/run%20test%20run.png)

DRUID automatically executes all the test cases included in the test plan. During the execution, you may be prompted to confirm whether to continue the process.

A chat window appears on the right-hand side of the screen, providing updates and confirming when the test run has completed.

![](../../../Resources/Images/KB%20Toolkit/test%20run%20completed.png)

4. Close the Chat window.

You can review the test run results when the run completes.

<a id="Reviewtestrunresults"></a>

## Review test run results

The **Summary** tab displays the AI Agent accuracy. You get an overview of the test cases number per status and the failure reason.

![](../../../Resources/Images/KB%20Toolkit/test%20run%20summary.png)

> **Info:** Aim for an accuracy rate of 90% or higher.

To find out more information about a failed test that helps you improve the KB, click on the **Reviews Complete** tab, then click on a failed test.

![](../../../Resources/Images/KB%20Toolkit/failed%20test.png)

By default, the test case results displays on the **Review** tab.

![](../../../Resources/Images/KB%20Toolkit/test%20case%20review.png)

Navigating through the tabs, you can drill-down to more detailed information :

- The **KB Search** tab provides you with the list of articles that were extracted from the KB.

![](../../../Resources/Images/KB%20Toolkit/kb%20search.png)

- The **Answer** tab allows you to check the actual answer versus the expected answer.

![](../../../Resources/Images/KB%20Toolkit/compare%20answers.png)

- The **GPT prompt** tab displays the GPT prompt that was executed to perform the test. This information displays only for advanced test cases.

![](../../../Resources/Images/KB%20Toolkit/GPT%20prompt.png)

<a id="Comparetestiterations"></a>

## Compare test iterations

Comparing test iterations is very useful for monitoring AI Agent performance over time.

To compare two test runs, follow these steps:

1. In the Test Run page, click on the desired test run.
2. In the Test run configuration page, click the **Comparison** tab.

![](../../../Resources/Images/KB%20Toolkit/comparison.png)

3. From the list, select the test run against which the current will be compared to.

The two test runs displays side-by-side and you can easily compare the responses provided in both cases and decide which one was better suited for the user question.

![](../../../Resources/Images/KB%20Toolkit/comapring%20runs.png)

<a id="ExportTestRunresultstoExcel"></a>

## Export Test Run results to Excel

You can export test run results to Excel for further analysis.

In the Test Run page, click on the desired test run. In the Test run configuration page, from the **Automations** drop-down, select either **Export to Excel** or **Export to Excel with Comparison**.

![](../../../Resources/Images/KB%20Toolkit/export%20test%20run%20results.png)

A chat window appears on the right-hand side of the screen, providing you with the export link.

Click on the download link provided in the chat to download the test run results on your computer.

![](../../../Resources/Images/KB%20Toolkit/downlaoded%20test%20results.png)
