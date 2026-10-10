---
layout:
  title:
    visible: false
---

<a id="StandardQueryDateFunctionsReference"></a>

# Standard Query Date Functions Reference

When filtering data using standard queries in Druid Data Service Connector tasks (such as Query Entity, Query Related Entity, or Update Entity), you can leverage built-in date and datetime filtering functions. These operators evaluate records relative to the execution time or calendar periods.

> **Info:** For all dynamic interval operators (Next X and Last X), the calculation is inclusive of the current time block. If you specify a value of X, the filter scans the current period plus X - 1 periods ahead or behind.

| Function | Description | Supported Input Values |
| --- | --- | --- |
| Today | Filters records based on the current calendar day. | None required |
| Yesterday | Filters records based on the entire previous calendar day. | None required |
| Next X Hours | Filters records falling within the current hour and the next X - 1 hours ahead. | Numeric integer offset (e.g., 3), variable, or entity field storing the value. |
| Last X Hours | Filters records falling within the current hour and the past X - 1 hours behind. | Numeric integer offset (e.g., 3), variable, or entity field storing the value. |
| Next X Days | Filters records falling within the current day and the next X - 1 days ahead. | Numeric integer offset (e.g., 5), variable, or entity field storing the value. |
| Last X Days | Filters records falling within the current day and the past X - 1 days behind. | Numeric integer offset (e.g., 5), variable, or entity field storing the value. |
| This Week | Filters records within the current calendar week (starting from Sunday or Monday depending on system locale). | None required |
| This Month | Filters records falling within the current calendar month boundaries. | None required |
| Next X Months | Filters records falling within the current month and the next X - 1 months ahead. | Numeric integer offset (e.g., 12), variable, or entity field storing the value. |
| Last X Months | Filters records falling within the current month and the past X - 1 months behind. | Numeric integer offset (e.g., 12), variable, or entity field storing the value. |
| This Year | Filters records falling between January 1 and December 31 of the current year. | None required |
| Last Year | Filters records falling between January 1 and December 31 of the previous year. | None required |
| Same Hour | Filters records based on the exact hour matching the input value. | Literal 24h string (e.g., 03:00), variable, or entity field storing the value. |
| Same Day | Filters records based on the exact calendar date matching the input value. | Literal date string (e.g., 2026-07-10), variable, or entity field storing the value. |
| Same Week | Filters records based on the exact calendar week index matching the input value. | Context evaluation variable or entity field storing the value. |
| Same Month | Filters records based on the exact calendar month index matching the input value. | Literal month string (e.g., 07), variable, or entity field storing the value. |
| Same Quarter | Filters records based on the exact calendar quarter (Q1-Q4) matching the input value. | Literal quarter string (e.g., q1, q2, q3, q4),, variable, or entity field storing the value. |
| Same Year | Filters records based on the exact calendar year matching the input value. | Literal year value (e.g., 2026), variable, or entity field storing the value. |
