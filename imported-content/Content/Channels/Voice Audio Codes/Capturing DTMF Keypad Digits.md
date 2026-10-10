<a id="CapturingDTMFKeypadDigits"></a>

# Capturing DTMF Keypad Digits

You can configure flow steps to capture a collection of digits the user presses at the phone's keypad, either within a specific time frame between digits, or a maximum number of digits or the digits pressed prior a specific digit set on the flow step.

To capture digits, on the flow step, click the **Metadata** section, tap on **Advanced Editing** and in the JSON field add the "audioCodesDTMF" object and set the parameters described in the table below.

| Parameter | Type | Description | Mandatory |
| --- | --- | --- | --- |
| sendDTMF | Boolean | To capture a collection of digits, set the parameter **sendDTMF** to **false**; otherwise, the AI Agent will capture only the first digit pressed by the user on the phone’s keypad. | Yes |
| bargeInOnDTMF | Boolean | When set to true, allows the user to interrupt the AI Agent by pressing a DTMF digit which terminates the AI Agent response.  **NOTE:**  To prevent users from interrupting the AI Agent, we strongly recommend you to set the parameter **bargeInOnDTMF** to false. | No |
| dtmfCollect | Boolean | Set this parameter to true to capture all the DTMF digits entered by the user.  Default value is false; that is, the AI Agent captures only the first digit pressed by the user. | Yes |
| dtmfCollectInterDigitTimeoutMS | Number | The timeout in milliseconds the AI Agent waits for the user to press another digit before it captures the digits. The timeout is triggered after the user enters the first DTMF digit and is reset after each digit.  The default value is **2000ms**.  **NOTE:**   - The parameter is applicable only when the **dtmfCollect** parameter is set to **true**. - If the timeout is reached, the parameters **dtmfCollectMaxDigits** and **dtmfCollectSubmitDigit** are disregarded. | Yes\* |
| dtmfCollectMaxDigits | Number | The maximum number of DTMF digits the user is expected to press on the phone’s keypad.  The default is **5**.  **NOTE:**   - The parameter is applicable only when the **dtmfCollect** parameter is configured to true. - If the timeout is reached, the parameters **dtmfCollectInterDigitTimeoutMS** and **dtmfCollectSubmitDigit** are disregarded. - If **dtmfCollectMaxDigits** is set to **0**, digits are captured based on the parameters **dtmfCollectInterDigitTimeoutMS** and **dtmfCollectSubmitDigit**. | Yes\* |
| dtmfCollectSubmitDigit | String | Defines a special DTMF "submit" digit that when received from the user, the AI Agent captures the digits pressed before it without waiting for the timeout to expire or for the maximum number of expected digits. The valid value is any symbol on a phone keypad. The default is **#** (pound key).  **NOTE:**  The parameter is applicable only when the dtmfCollect parameter is configured to **true**. | Yes\* |

\*The parameter controls how the AI Agent captures the digits. You can use these parameters in any combination, but at least one is mandatory.

## Example: Capture the user’s CNP on a prompt step

This section describes how to configure a prompt step to capture the CNP provided by the users prior to pressing **#** (pound key) on their phone keypad.

Enter [[Account]].ClientCNP in Input mapping on the step.

On the prompt step **Metadata** section, click **Advanced editing** and in the JSON editor add the following code:

```
"audioCodesDTMF":{
    "sendDTMF":false,
    "bargeInOnDTMF":false, 
    "dtmfCollect":true,
    "dtmfCollectSubmitDigit":"#"
}
```
