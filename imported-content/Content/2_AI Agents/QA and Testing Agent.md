<a id="QATestingAgent"></a>

# QA Testing Agent

The QA Testing Agent runs automated test suites using simulated user interactions.

<a id="KeyCapabilities"></a>

## Key Capabilities

- Generates functional test scenarios based on step inputs, defined user behaviors, and target criteria.
- Executes test cases sequentially in a fixed order. Logs execution failures per test step while continuing remaining test suite execution.
- Outputs test summary reports detailing overall pass/fail rates and specific step error logs.

<a id="OperationalRules"></a>

## Operational Rules

- Restricts actions strictly to test generation and execution.
- Hands off requests for structural agent or integration edits to corresponding AI Authoring Agents.
