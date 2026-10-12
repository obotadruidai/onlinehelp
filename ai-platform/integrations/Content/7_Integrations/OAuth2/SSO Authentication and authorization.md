---
title: SSO Authentication OAuth 2.0
---


OAuth (Open Authorization) 2.0 is an open standard authorization protocol designed to allow a website or application to access resources hosted by other web apps on behalf of a user. It acts as an intermediary layer, providing the third-party service (e.g., Google, Facebook, LinkedIn) with an access token that authorizes specific user account information to be shared.

By using OAuth 2.0, you authenticate users conversationally and allow the AI Agent to access their data hosted with a third–party API service without revealing their credentials to Druid.

This video shows how an authenticated user submits a support ticket directly through the web chat.

This section describes how it works and how to configure Druid for OAuth 2.0 grant type Authorization Code.

## How Does OAuth 2.0 Work?

The OAuth 2.0 authorization flow implementation in Druid is a seven-step process.

![](<../../../.gitbook/assets/SSO Authentication and authorization.png>)

1. The Druid requests authorization to access protected resources owned by the user (resource owner) by directing the user to the authorize endpoint.
2. Druid assistant displays a link in the chat that redirects the user to a login dialog at the web application. The user clicks the link and authenticates.

{% hint style="info" %}
**Info:** This link is accessible from any channel that can use a web browser to open it.
{% endhint %}

3. The resource owner authenticates and authorizes the resource access request from the application, and returns an authorization grant (authorization code) to Druid for that ConversationId.
4. Druid then requests an access token from the authorization server by presenting the authorization grant.
5. If the user identity is authenticated and the authorization grant is valid, the Authorization Server or authentication provider will issue an access token to Druid, which will be saved in the conversation context.
6. Druid can now request access on user’s behalf to protected resources from the Resource Server at the provider by presenting the access token.
7. If the access token is valid, the resource server returns the requested resources to Druid.

## OAuth Authorization Particularities

* The authentication session is held per conversation Id.
* Authentication tokens (access token, refresh token, etc.) are handled by the AI Agent in the conversation context.
* You can request authentication both for server-to-server integrations or for user’s conversation.

## OAuth 2.0 used by Druid for both user authorization and authentication

In Druid, you can use OAuth 2.0 for both authorization and user authentication.It provides you with three types of actions you can use for OAuth 2.0 purposes:

* **Sign in** – handles both authentication and authorization when calling external API services on user’s behalf without necessarily authenticating the user within the conversation.
* **Get user identity** – get user data (first name, last name, email, etc.) to identify and authenticate the user within the conversation. Requires Sign in.
* **Sign out** – You can give the users the possibility to prevent the conversation from having access to external services on user’s behalf. You can use this action only if the external service provides an endpoint for signing out.
