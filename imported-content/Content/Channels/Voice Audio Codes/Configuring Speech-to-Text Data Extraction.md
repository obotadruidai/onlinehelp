---
title: Configuring Speech-to-Text Data Extraction
---

# Configuring Speech-to-Text Data Extraction

You can configure your Druid flows (using prompt steps) to extract specific data from user says using Speech-to-Text (STT) service integrated with AudioCodes. For example, authors can instruct ZevoTech Speech-to-Text (STT) service integrated with AudioCodes to extract dates from spoken input.

When you expect a user to provide a user will provide specific data (e.g., a birthdate), you send instructions to the STT service. This guides the STT engine to extract the specified data as metadata, returning both the full transcribed text and the extracted value.

### Configure data extraction

Before configuring the data extraction, your entity has:

* A string field to store the full transcribed text.
* A field of the appropriate type to accommodate the data you want to extract. If you are using ZevoTech Speech-to-Text (STT), currently, only birth\_date is supported for extraction; therefore, make sure the field name is **birth\_date**.

To configure a prompt step for data extraction, follow these steps:

1. In **Input mapping** enter the string field that will store the full transcribed text. For example, \[\[Address]].userInput.
2. Click on the **Metadata** section, tap on **Advanced Editing** and in the JSON field add the "audioCodesSTTinstructions" object. This object requires the following parameters:

| Parameter       | Type   | Description                                                                                                                                                                                                               | Mandatory |
| --------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- |
| task            | String | Set this to **"data\_extraction"** to instruct the STT service to extract specific data from the user's spoken response based on the structure defined in the **extracted\_data** object.                                 | Yes       |
| question        | String | Provide context for interpreting the user's response and guide the STT service on what information to extract. This can be the same question as in the prompt step. For example, `"question": "What is your birth date?"` | Yes       |
| extracted\_data | JSON   | Define the structure of the data to be extracted by the STT service. For ZevoTech Speech-to-Text, currently only birth\_date is supported, so ensure the field name within this object is `birth_date`.                   | Yes       |

3. Save the prompt step.

### Example: Extract dates with ZevoTech STT in AudioCodes

Let's say you want to extract a birthdate.

Before configuring the date extraction, make sure that your entity (e.g., \[\[Address]]) has:

* A string field named userInput (e.g., \[\[Address]].userInput) to store the full transcribed text.
* A field named birth\_date of type Date/DateTime (e.g., \[\[Address]].birth\_date).

To extract data from user says, configure a prompt step as follows:

1. In **Input mapping** enter \[\[Address]].userInput.
2. Click on the **Metadata** section, tap on **Advanced Editing** and in the JSON field add the following "audioCodesSTTinstructions" object:

**audioCodesSTTinstructions Example**

```
  "audioCodesSTTinstructions": {
    "task": "data_extraction",
    "question": "What is your birth date?",
    "extracted_data": {
      "birth_date": ""
    }
  }
```

The structure of the **audioCodesSTTinstructions** object is similar to ZevoTech STT **sttGenericData** object.

3. Save the prompt step.

When the STT service processes the user's speech, the ZevoTech Live STT API will return a JSON string with the following structure:

**ZevoTech STT API response**

```
{
  "type": "recognition",
  "alternatives": [
    {
      "text": "două zeci și patru a cincia nouăzeci și șapte",
      "confidence": 0.8355
    },
    {
      "text": "24 a cincia 97",
      "confidence": 0.8355
    }
  ],
  "data_extraction": {
    "response": {
      "birth_date": "24-05-1997"
    },
    "status": "success"
  }
}
```

In this response:

* The value of "text" (from alternatives) will be stored in your Druid entity in \[\[Address]].userInput.
* The value of "birth\_date" (from data\_extraction.response) will be stored in \[\[Address]].birth\_date.

![](<../../../.gitbook/assets/stt response.png>)
