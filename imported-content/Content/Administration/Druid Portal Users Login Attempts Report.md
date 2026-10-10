---
layout:
  title:
    visible: false
---

<a id="DruidPortalUsersLoginAttemptsReport"></a>

# Druid Portal Users Login Attempts Report

The Druid Portal Users Login Attempts Report provides administrators with a comprehensive view of login activity across their tenant. This report helps enhance security by tracking login attempts, detecting unauthorized access, and identifying unusual patterns. With advanced filtering options, administrators can refine search results based on specific criteria, exclude certain users for focused monitoring, and export data for further analysis. These capabilities support proactive threat detection, compliance auditing, and improved access control, helping organizations safeguard their Druid Portal environment.

> **NOTE:** This feature is available in DRUID 8.11 onwards.

<a id="AccessingtheLoginAttemptsReport"></a>

## Accessing the Login Attempts Report

To view the Login attempts report, follow these steps:

1. In the **Administration** menu, click **Users**.
2. On the Users page, select the **Login attempts** tab.
3. In the **Creation time** field, choose the time range for the report.
4. Click **Refresh** to generate the report.

![](../Resources/Images/druid%208.11/login%20attempts%20report.png)

> **NOTE:** The report does not currently include successful logins.

<a id="ReportDetails"></a>

## Report Details

The report includes the following information for each login attempt:

|  |  |
| --- | --- |
| Username or Email | Identifies the user attempting to log in, except for users who log in via SSO.. |
| Result | Indicates the outcome of the login attempt. Currently, the report does not track successful logins. |
| Creation time | The exact timestamp of the login attempt. |
| Browser info | The user agent string of the browser used during the login attempt.  For example, a record like: *Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0* indicates that the user accessed the portal using Microsoft Edge (version 132.0.0.0) on Windows 10 (64-bit). |
| Client IP Address | The IP address from which the login request originated. |

<a id="ExcludingUsersfromtheReport"></a>

## Excluding Users from the Report

Excluding users from the Login attempts report can be beneficial in the following scenarios:

- **Reducing noise in monitoring** – Excluding SSO login attempts helps focus on unusual activity.
- **Focusing on specific investigations** – When investigating potential security incidents, you may want to exclude known trusted users to narrow the report to suspicious logins.
- **Enhancing performance** – Filtering out high-volume, non-critical logins can speed up report generation and improve usability.

If you need to exclude specific users:

1. Locate the user in the report.
2. Click the **Actions** button next to their record.
3. Select **Exclude**.

![](../Resources/Images/druid%208.11/exclude%20user.png)

4. Repeat for all users you want to remove.
5. Click **Refresh** to update the report.

<a id="FilteringandExportingData"></a>

## Filtering and Exporting Data

Use the filtering options to refine search results based on your specific criteria. Click **Refresh** to apply the filters.

Once the report is filtered, click **Export Excel** to download the report for further analysis and maintain a detailed record of login attempts for security audits and compliance reporting.

![](../Resources/Images/druid%208.11/export%20to%20excel.png)

<a id="LoginAttemptsReportforaSpecificPortalUser"></a>

## Login Attempts Report for a Specific Portal User

DRUID allows administrators to view login attempts for individual Portal users. This granular access helps track user-specific login activity.

To generate the Login attempts report for a specific user:

1. Navigate to the Users page.
2. Click the **Users** tab.
3. Locate the desired user and click the **Actions** button next to their record.
4. Select **See Login Attempts**.

![](../Resources/Images/druid%208.11/seeloginuser.png)

5. In the **Creation time** field, choose the time range for the report.
6. Click **Refresh** to generate the report.

![](../Resources/Images/druid%208.11/user%20login%20details.png)

> **NOTE:**  This report does not include additional filtering options. However, you can download the data in Excel format for further analysis.
