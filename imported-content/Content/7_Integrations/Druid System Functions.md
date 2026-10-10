<a id="DRUIDSystemFunctions"></a>

# DRUID System Functions

This section provides description of DRUID system functions you can use when mapping responses on connectors.

| Function | Description | Syntax | Example | Result |
| --- | --- | --- | --- | --- |
| LIST | Creates a JSON array from a list of arguments. | `LIST (argument1, argument2)` | `LIST('abc','123','xyz')` | ["abc","123","xyz"] |
| CONCAT | Concatenates two strings. | `CONCAT(string1, string2)` | `CONCAT('Bearer ','12345')` | Bearer 12345 |
|  |  |  | `CONCAT('Bearer ',@token)` |  |
|  |  |  | `CONCAT('Bearer ',[[Entity]].StringField)` |  |
| BASE64 | Performs Base64 encoding on a given string. | `BASE64(string)` | `BASE64('abcde')` | YWJjZGU= |
| SPLIT | Transforms a string separated by a given character into an array of strings or objects. | `SPLIT(``string``,``'split separater character'``,``' stringVariable'``)` | `SPLIT([[Brand]].Name,',','AccountNumber') "001,002,003"` | { "ArrayProperty": [ { "AccountNumber": "001" }, { "AccountNumber": "002" }, { "AccountNumber": "003" } ] } |
|  |  |  | `SPLIT([[Brand]].Name,',','') "001,002,003"` | ["001", "002", "003"] |
| FILECONTENT | Loads a file in binary format. To be used in Request tabs when a file needs to be sent to an API or inserted into a database table. The file must be identified by its Name property. | `FILECONTENT(druid_entity.Name)` | `FILECONTENT([[Employee]].Certificate.Name)` | Binary object of the file. |
| HASHSHA512ASHEX | Performs SHA-512 hashing on a given string, returning the result in HEX format. | `HASHSHA512ASHEX(string)` | `HASHSHA512ASHEX('abcde')` | 3837386165363561393265383663616330313161353730643463333061376561656334343262383563653865636130633239353262356533636330363238633265373964383839616434643563376336323639383664343532646438363337346236666661613763643862363736363562656632323839613563373062306131 |
| TOLOWER | Converts a given string to lowercase. | `TOLOWER(string)` | `TOLOWER('aBcDe')` | abcde |
| TOJSONSTRING | Converts a JSON object to a JSON string. Mostly used when mapping the response task | `TOJSONSTRING(JSON object)` | `TOJSONSTRING({"FilterValue":"test33"})` | {"FilterValue":"test33"} |
| CREATEFILE | Transforms file content (in string format) received from a database or third-party system into a file and saves it in a file-type field. Map this function to an Entity field (created on the response entity) referencing the File system entity.  **Parameters**:   - `FileContent`: The content of the file. If the content of the file is Base64 encoded, use `BASE64DECODE()` to convert it to a string. - `FileName`: The desired filename, including its extension (e.g., 'document.pdf'). The function automatically escapes special characters (e.g., <, >, \, etc.) from the filename. | `CREATEFILE(FileUpload, FileName)`  If the content of the file from the third-party system is base64 encoded, use the following syntax:  `CREATEFILE(BASE64DECODE(Base64 string),FileName)` | `CREATEFILE(BASE64DECODE('YWJjZGU='),'Download.pdf')` | The result is a file named Download.pdf with the content "abcde". |
| BASE64DECODE | Decodes a given Base64 string. Can be used in both response and request tabs. | `BASE64DECODE(Base64 string)` | `BASE64DECODE('YWJjZGU=')` | abcde |

> **NOTE:** Functions can be nested within other function arguments. For example, you can use `BASE64(FILECONTENT([[Employee]].Certificate.Name))` to perform Base64 encoding on the binary content of an employee's certificate.
