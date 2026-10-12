---
title: Use Case for using Form Data Request Type
---


If you want to send multiple files to an endpoint, which concatenates them into a single file, you can use the **FormData** request type.

In this example:

* In entity \[\[Employee]], we have three fields of type entity referencing the \[\[File]] entity: \[Employee]].InitialContract, \[\[Employee]].Annex and \[\[Employee]].FullContract.
* We have employee’s initial contract and the annex to contract stored in two DRUID entities: \[Employee]].InitialContract and \[\[Employee]].Annex.
* We want to get the employee’s full contract, concatenating the two files previously mentioned (assuming that the endpoint performs this concatenation).
* We will use the Download File integration task for that.

### Setting up the request

In the API Resource URL, enter the REST API endpoint that concatenates multiple files.

From the **RequestType** field, select **UseFormData** and click the **Body** tab.

While the body type can be File, Text or File Content, map two connector fields (Document1 and Document2) to the two DRUID entity fields that capture the files specified above. You can map add additional mapping here based on how many files you need to send to the REST API endpoint.

![](<../../../../.gitbook/assets/Response Settings (1).png>)

In our example, the integration task will send two documents.

### Setting up the response

Click the **Response** tab and in the **ProjectResultToEntityPath** field, enter the name of the field that will store the file returned by the REST API endpoint (the two files sent concatenated in one).

![](<../../../../.gitbook/assets/Response Settings_1.png>)

Save the integration task and use it on flow steps. If you want to send the file returned by the REST API endpoint to the user in the chat, make sure that on a step subsequent to the one where you’re using the **Download File** integration task, in the Metadata section, you enter the entity field that stores the returned file. In our case, it’s \[\[Employee]].FullContract.
