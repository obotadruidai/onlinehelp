---
title: "Location"
---

<a id="Location"></a>


With Location steps, Druid enables you to bring the real world to your users with maps by rendering a geographical location similar to Google Maps preview and configure your AI Agents to get and store user’s geographical location shared in the chat.

> **IMPORTANT!** The Location flow step is available for the following channels:
>
> - RingCentral (Available starting with Druid 9.19)
> - WhatsApp (Only for Vonage API version V1)

<a id="Usecases"></a>

## Use cases

- Collect location data from your users (with Location flow steps) and use it to present location-aware messages that are more likely to convert them into leads. E.g. share location of a shop, business, etc.
- Assist users with instant location of a place rendered similar to Google Maps preview.

<a id="AddingandconfiguringLocationsteps"></a>

## Adding and configuring Location steps

To add and configure a Location step in a flow:

1. Open the desired flow in Flow Diagram view.
2. Expand the Flow Palette, then drag the **Location** step from the Dialog category into the main flow window and drop it onto the step you want to link it to.
3. Select the step on the diagram, then click the **Settings** icon from the Actions menu.
4. Configure the Location step according to your objective: either to capture and store the user's location or to share a specific location with the user in the chat.

<a id="Capturingandstoringtheuserslocation"></a>

### Capturing and storing the user's location

To store the user's location shared in the chat, configure the Location step as follows:

| Parameter | Description |
| --- | --- |
| Step name | The name of the step that is used by the system. It is not visible to the end user, but is useful for the author to document the dialog and later understand reports in conversation analytics. |
| Step message | The message which will be displayed to the user in the chat. |
| Input mapping (to receive user's location) | By default, Druid stores the user's location in the system entity [[GeoLocation]]. If you want to store the location in another entity field, first make sure that you have an entity field of type Entity referencing the [[GeoLocation]] system entity, then on the Location flow step enter that field in **Input mapping (to receive user's location)** in the following format [[<Entity>]].<Field>. |

![](../Resources/Images/Flows/store%20location.png)

When the step is executed, the AI Agent will return the message specified in the **Step message** field, wait for the user to share the geographical location and store that location in the entity provided in the **Input mapping (to receive user's location)** field (if any) or in the [[GeoLocation]] system entity (if you want to store it in Druid default system entity).

<a id="Sharingaspecificlocationwiththeuserinthechat"></a>

### Sharing a specific location with the user in the chat

To share a geographical location with the user in the chat, configure the Location step as follows:

| Parameter | Description |
| --- | --- |
| Step name | The name of the step that is used by the system. It is not visible to the end user, but is useful for the author to document the dialog and later understand reports in conversation analytics. |
| Step message | The message which will be displayed to the user in the chat. |
| Input mapping (to receive user's location) | Make sure that this field is empty. |
| Attachment (to send location to user) | Enter the entity that stores locations as best suits your needs, in the following format [[<Entity>]].<Field>. Your entity should have an entity field of type Entity referencing the [[GeoLocation]] system entity. |

<a id="ExampleSharinglocationbasedonusersinputaddress"></a>

### Example: Sharing location based on user’s input address

User says: “Give me the location of Opera Center, Strada Costache Negri 1-5”

AI Agent replies “Here it is” and shares the place location in Google Maps preview.

![](../Resources/Images/Flows/share%20location%20based%20address.png)

In this example:

- We created a REST connector to integrate with the a Maps API that retrieves location in **[[Place]].Location** based on [[Place]].Address that stores user input address.
- [[Place]].Location is of type Entity referencing the [[GeoLocation]] system entity.
- The flow dedicated to sharing locations has one or more utterances that contain [[Place]].Address that will store user input address.

![](../Resources/Images/Flows/share%20location%20flow%20utterances.png)

To share a geographical location with the users in the chat in Google map preview on a flow step of type Location, make sure that **Input mapping (to receive user's location)** is empty and in the **Attachment (to send location to user)** field enter [[GeoLocation]] or an entity field related to [[GeoLocation]] (in our example, [[Place]].Location ).

![](../Resources/Images/Flows/atatchment%20field%20share%20location.png)

On the location step, in the PreAction section, also add an integration which interrogates the Google Maps API and receives the location attributes (GPS latitude, longitude, name, address)

Whenever the dialog reaches the Location flow step, the AI Agent takes the address provided by the user and queries the Google Maps API, which returns the geolocation of the place located at the specified address. The AI Agent renders the location in the chat similar to the Google maps preview.

## Related Topics

- [System Entities](../5_Entities/System%20Entities.md)
