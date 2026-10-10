---
layout:
  title:
    visible: false
---

<a id="MapRESTResponseusingCustomCode"></a>

# Map REST Response using Custom Code

When integration scenarios require advanced data transformations, conditional checks, or custom array processing, you can write JavaScript directly in the REST response configuration to map response attributes to DRUID entity fields.

External REST APIs often return dynamic structures, nested objects, or collection arrays where target fields depend on runtime conditions. Enabling **Use Custom Code Mapping** provides direct access to the raw API response within the execution context, letting you programmatically parse, filter, and assign response data directly to Druid entity fields. This approach replaces standard JSON Path mapping and eliminates the need for an additional, standalone Custom Code integration task after the REST integration task.

> **Info:** This feature is available starting with Druid 9.28.

<a id="Example"></a>

## Example

In this example, an external REST API returns a response payload containing a list of audience members across multiple locations. Using Audience as the Response Entity, the script demonstrates how to parse the payload, filter for members belonging to a specific campus ("North Campus"), create child entity records dynamically, and populate a response entity collection.

**Example script**

```
(function mapRestResponse(){
//EXAMPLE SCRIPT
const responseEntity = Context.GetResponseEntity();
let responseJson = JSON.parse(RestContext.ResponseContent)

if (responseJson != null && responseJson.Members.Count >0){
    responseEntity.Members = EntityFactory.CreateCollection("AudienceMember");
    for (let i=0; i<responseJson.Members.Count; i++){
        //we map to our response collection the members from "North Campus" only
        if (responseJson.Members[i].Campus == "North Campus") {
            let member = EntityFactory.CreateEntityByName("AudienceMember");
            member.Name = responseJson[i].Name;
            responseEntity.Members.Add(member);
        }

        
    }
}

Context.SetResponseEntity(responseEntity);
})()
```
