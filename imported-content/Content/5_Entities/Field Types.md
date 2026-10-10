---
title: "Field Types"
---

<a id="FieldTypes"></a>


Understanding the field type is essential as it determines specific capabilities, particularly in natural language processing (NLP). For instance, a field like Vacation.StartDate, categorized as datetime, will intelligently interpret user input to convert it into a date format.

The table below provides a comprehensive description of the field types available within Druid:

| Field Type | Description | Has NLP Skills? |
| --- | --- | --- |
| Boolean | Represents a value that supports True and False. | Yes |
| Currency | Enables selection of from a drop-down menu. | No |
| Date | Stores only the date portion of the DateTime type, useful when time zone conversion is unnecessary. | Yes |
| DateTime | Combines a date with a time of day and fractional seconds, adhering to a 24-hour clock. | Yes |
| Decimal | Allows storage of up to 32 digits with a maximum of six digits after the decimal point. | Yes |
| Email | Stored as a string but recognized as a distinct type for specialized behavior and validation. The string is stored in Unicode format. Druid applies a set of validation rules to capture email addresses. For more information, see [Capturing Email Addresses in Channels](../How%20to/Capturing%20email%20addresses%20in%20channels.md). | Yes |
| Entity | Establishes a one-to-one relation with a specified entity. | Yes |
| Entity List | Establishes a one-to-many relation with a specified entity. | No |
| Guid | Represents a unique identifier for objects in a database. It is a number in a 16-byte binary representation. | No |
| Hash Tag | Obsolete, it will be removed from the system in a future release. |  |
| Integer | Stores integer values between -2,147,483,648 and 2,147,483,647. | Yes |
| Invariant Date | Defines a field displaying date only, accommodating various time zone, daylight saving time scenarios, winter time or leap a specific day based on year (e.g. February 28). Use it for attributes such as birth dates, expiration dates, or issuing dates. | Yes |
| InvariantDate Time | Defines a field displaying both date and time, considering time zone and daylight saving time adjustments. | Yes |
| Invariant Time | Defines a field displaying time only, considering different time zones and daylight saving time. | Yes |
| IPAddress | Represents a 32-bit identifier assigned to a host using Internet Protocol, stored in decimal format of an IP address whereas it consists of four fields separated by dots, where each field contains a value in the range 0 - 255. | No |
| JArray | Stores JSON arrays from third-party systems within your conversational AI solutions. You have the flexibility to manipulate this data within integrations using Custom Code or incorporate it into flows (Set Variables or Code Extension) and forms using the Code Editor. For more information, see [Manipulate Data without Druid Entity Structures](<https://docs.druidai.com/docs/Content/How%20to/Manipulate%20Data%20without%20Entity%20Structures.htm>). | No |
| JObject | Stores JSON objects from third-party systems. This simplifies the process by eliminating the need to align the AI Agent entity model with each JSON property, sparing you from creating multiple entities and fields to mirror the data structure. Additionally, utilizing this field type eliminates the need for complex mappings within the integration. You have the flexibility to manipulate this data within integrations using Custom Code or incorporate it into flows (Set Variables or Code Extension) and forms using the Code Editor. For more information, see [Manipulate Data without Druid Entity Structures](<https://docs.druidai.com/docs/Content/How%20to/Manipulate%20Data%20without%20Entity%20Structures.htm>). | No |
| Location | Enhances NLP models for better extraction of location names from user input. You can further use the value stored in this field in connectors as data of type string. | Yes |
| Long | Obsolete, it will be removed from the system in a future release. |  |
| Organization | Enhances NLP models for better extraction of organization names from user input. You can further use the value stored in this field in connectors as data of type string. | Yes |
| Percentage | Represents numerical values formatted as percentages, stored as fractions of 100 with a percent sign. | No |
| Person | Enhances NLP models for better extraction of person names (full name, first name or last name) from user input. You can further use the value stored in this field in connectors as data of type string. | Yes |
| String | Stores a single line of text, with a maximum length typically not exceeding 128 characters, stored in Unicode format. | No |
| Time | Stores only the time portion of the DateTime type, useful when time zone conversion is unnecessary. | Yes |
| Url | Stores a single line of text in URL format, stored in Unicode format. | No |

## Related Topics

- [Managing Entity Fields](Managing%20Entity%20Fields.md)
