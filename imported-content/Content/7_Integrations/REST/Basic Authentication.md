---
title: "Basic Authentication"
---

<a id="BasicAuthentication"></a>


Basic Authentication is an HTTP authentication method that verifies a client's identity by sending a username and password with each request. The credentials are combined, encoded using Base64, and included in the HTTP Authorization header.

When Basic Authentication is enabled in a REST App, Druid automatically includes an Authorization header in every request sent through that application. The header contains a Base64-encoded representation of the configured username and password in the following format:

Authorization: Basic <Base64 encoded username and password>

{% hint style="info" %}
**Info:** Basic autehntication is available starting with Druid version 9.24.
{% endhint %}

<a id="ConfigureBasicAuthentication"></a>

## Configure Basic Authentication

To configure Basic Authentication:

1. Open the desired REST App.
2. Turn the **Basic REST Security** toggle on.
3. Enter the API username in the **User name** field.
4. Enter the corresponding password in the **Password** field.
5. Save the app.

Druid basic autehntication for REST API calls works similarly to selecting Basic Auth in Postman and providing values in the Username and Password fields. When a request is sent, Druid combines the username and password, encodes them using Base64, and includes the resulting value in the HTTP Authorization header.

![](../../Resources/Images/druid%209.24/basic%20auth%20header.png)

<a id="SecurityConsiderations"></a>

## Security Considerations

Base64 encoding is not encryption. To protect credentials during transmission, use Basic Authentication only over HTTPS connections.
