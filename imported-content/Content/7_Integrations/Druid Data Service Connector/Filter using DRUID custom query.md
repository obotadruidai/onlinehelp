---
title: "Filter Data using Druid Custom Query"
---

<a id="FilterDatausingDruidCustomQuery"></a>


The Druid Custom Query allows you to filter request data for Query entities and Query-related entity integration tasks. With this feature, you can retrieve and analyze data from entities beyond the request entity, without relying on the Query-related entity integration task. The Druid Custom Query supports a range of SQL statements, functions, operators, and clauses, as detailed below.

<a id="Basicstatements"></a>

## Basic statements

<a id="SELECT"></a>

## SELECT

The `SELECT` statement is used to select data from a database table.

{% hint style="warning" %}
**IMPORTANT!** Using the unqualified `*` to select all fields from an entity is not supported. Instead, specify the names of the entity fields you want to select, separating them with commas.
{% endhint %}

**Syntax**

```
SELECT field_1, field_2, field_3...
FROM entity
```

**Example - select specific fields from the entity [[Account]]**

```
SELECT FirstName, LastName, Age
FROM Account
```

<a id="Aliases"></a>

## Aliases

## Column Alias

A column alias provides a temporary name for a field in your result set, making it easier to read. For example, when concatenating fields together, you might alias the result.

**Syntax**

```
column_name AS alias_name
```

Where:

- `column_name` is the original name of the entity field that you wish to alias.
- `AS` is optional. Whether you specify the `AS` keyword or not has no impact on the alias.
- `alias_name` is the temporary name to assign to the entity field.

{% hint style="info" %}
**NOTE:**

- If the `alias_name` contains spaces, you must enclose the `alias_name` in quotes.
- It is acceptable to use spaces when you are aliasing a column name.
- The `alias_name` is only valid within the scope of the SQL statement.
{% endhint %}

**Example 1**

```
SELECT ClientId, FirstName + LastName AS Name
FROM Clients
WHERE FirstName = 'John'
```

In this example, we've aliased the second field (i.e.: FirstName and LastName concatenated) as Name. As a result, Name will display as the heading for the second field / column when the result set is returned.

**Example 2**

```
SELECT ClientId, FirstName + LastName AS "Client Name"
FROM Clients
WHERE FirstName = 'John'
```

In this example, we've aliased the second column (i.e.: FirstName and LastName concatenated) as "Client Name". Since there are spaces in this `alias_name`, we enclosed "Client Name" in quotes.

## Table Alias

Creates a temporary name for entities / tables. Table aliases are used to shorten your SQL to make it easier to read or when you are performing a self join (i.e.: listing the same entity / table more than once in the FROM clause).

**Syntax**

```
table_name AS alias_name
```

Where:

- `table_name` is the original name of the entity that you wish to alias.
- `AS` is optional. Whether you specify the `AS` keyword or not has no impact on the alias.
- `alias_name` is the temporary name to assign to the entity.

{% hint style="info" %}
**NOTE:**

- If the `alias_name` contains spaces, you must enclose the `alias_name` in quotes.
- It is not generally good practice to use spaces when you are aliasing a table name.
- The `alias_name` is only valid within the scope of the SQL statement.
{% endhint %}

In the examples below, we omit AS when aliasing a table name.

When creating table aliases, it is not necessary to create aliases for all of the entities listed in the FROM clause. You can choose to create aliases on any or all of the entities.

**Example**

```
SELECT p.ProductName, Inventory.Quantity
FROM Products p
INNER JOIN Inventory
ON p.ProductId = Inventory.ProductId
ORDER BY p.ProductName ASC, Inventory.Quantity DESC
```

The query retrieves the product names and their corresponding quantities from [[Products]] and [[Inventory]] entities. It matches these entities based on the ProductId field. The results are sorted first by ProductName in ascending order and then by Quantity in descending order within each product name.

In this example, we've created an alias for the Products entity called **p**.Within this SQL statement, we referred to the Products entity as p.

You can use table aliases in conjunction with the `GROUP BY` clause to aggregate data effectively.

{% hint style="info" %}
**NOTE:** Always use table aliases in the `GROUP BY` clause to match the aliases in the `SELECT` statement, ensuring clarity and avoiding errors in complex queries.
{% endhint %}

**Example**

```
Select t1.Id Id, t1.Name Name,  
count(*) TestCasesCount, t1.CreatedOn
, t3.Id [Bot.Id]
, t3.Name [Bot.Name]
FROM KBTestPlan t1 
LEFT JOIN KBTestPlanXTestCase t2
on t1.Id = t2.TestPlanId
LEFT JOIN KBCollection t3
on t1.BotId = t3.Id
GROUP BY t1.Id, t1.Name, t1.CreatedOn, t3.Id, t3.Name
Order By t1.CreatedOn Desc.
```

In this example, the query selects data from the KBTestPlan, KBTestPlanXTestCase, and KBCollection tables, using aliases (t1, t2, t3) to avoid repeating the full table names.

The GROUP BY clause groups aggregated result by specific columns — t1.Id, t1.Name, t1.CreatedOn, Bot.Id, and Bot.Name — while counting the test cases associated with each test plan.

<a id="Filteringandconditions"></a>

## Filtering and conditions

<a id="WHERE"></a>

## WHERE

The WHERE clause is used to filter records in a query, ensuring that only those meeting specific conditions are retrieved.

**Syntax**

```
SELECT field_1, field_2, field_3...
FROM entity
WHERE condition
```

{% hint style="info" %}
**NOTE:** When filtering by a system entity field, use the syntax '@FieldName' in the WHERE clause. Map the variable name to the DRUID system entity field without the @ symbol. For reference, see the example below.
{% endhint %}

The following query retrieves test case details from the [[KBTestCase]] entity, filtering records based on the AI Agent ID. It converts the @BotId variable into a unique identifier type before applying the filter. The results are sorted in descending order by the CreatedOn field.

**Example - filtering by BotId**

```
select t1.Id Id, t1.Name Name, t1.ExpectedDataSource1, t1.ExpectedURL1, t1.ExpectedFlowName, t1.ExpectedBot1Name, t1.CreatedOn
from KBTestCase t1
where T1.BotId = CONVERT(GUID, '@BotId') -- Filter for the current <span class="mc-variable General.AI_Agent variable">AI Agent</span>
order by T1.CreatedOn DESC;
```

When using this query, we set the BotId variable to [[ChatUser]].BotId in the mapping table.

![](../../Resources/Images/Druid%20Data%20Service%20Connector/map%20filed%20custom%20query.png)

The following operators can be used in the WHERE clause:

| Operator | Description |
| --- | --- |
| = | Equal |
| > | Greater than |
| < | Less than |
| >= | Greater than or equal |
| <= | Less than or equal |
| != | Not equal to |
| LIKE | Searches for a specified pattern in a field. The LIKE operator supports two types of pattern matching: standard SQL wildcards and regular expression-like syntax.  **Info:** In DRUID versions prior to 9.4, the `LIKE` operator only supports % wildcards.  **Syntax**   ``` SELECT field_1, field_2, ... FROM entity WHERE field_n LIKE pattern ```     **SQL-style wildcard approach: Finding books where the name starts with "The"**   ``` SELECT     s.BookName,     s.Price,     s.QuantitySold,     (s.Price * s.QuantitySold) AS TotalSales FROM Sales s WHERE s.BookName LIKE 'The%' ```     **Regular expression-like approach: Finding books where the name starts with "The"**   ``` SELECT     s.BookName,     s.Price,     s.QuantitySold,     (s.Price * s.QuantitySold) AS TotalSales FROM Sales s WHERE s.BookName LIKE '^The' ```     **SQL-style wildcard approach: Finding books where the name ends with "Guide"**   ``` SELECT     s.BookName,     s.Price,     s.QuantitySold,     (s.Price * s.QuantitySold) AS TotalSales FROM Sales s WHERE s.BookName LIKE '%Guide' ```     **Regular expression-like approach: Finding books where the name ends with "Guide"**   ``` SELECT     s.BookName,     s.Price,     s.QuantitySold,     (s.Price * s.QuantitySold) AS TotalSales FROM Sales s WHERE s.BookName LIKE '%Guide$' ``` |
| AND / OR | Combines multiple conditions in a WHERE clause.  **Example**   ``` SELECT FirstName, LastName FROM Account WHERE Age > 30 AND City = 'New York' ``` |
| IN | Allows you to specify multiple values in a `WHERE` clause. Returns all records that are in any of the values in a given list or subquery.  **NOTE:** This operator is available in DRUID 9.4 and higher.  **Example 1 - select customers from Romania, Germany and Spain**   ``` SELECT s.FirstName, s.LastName, s.Country FROM Customers s WHERE Country IN ('Romania', 'Germany', 'Spain') ```     **Example 2 - Return customers that have an order**   ``` SELECT c.FirstName, c.LastName, c.Country FROM Customers c WHERE c.CustomerId IN (SELECT o.CustomerId FROM Orders o); ``` |
| NOT IN | Allows you to specify multiple values in a `WHERE` clause. Returns all records that are NOT any of the values in a given list or in the results of a subquery.  **NOTE:** This operator is available in DRUID 9.4 and higher.  **Example 1 - select customers except those from Romania, Germany and Spain**   ``` SELECT s.FirstName, s.LastName, s.Country FROM Customers s WHERE Country NOT IN ('Romania', 'Germany', 'Spain') ```     **Example 2 - Return all customers that have NOT placed any orders**   ``` SELECT c.FirstName, c.LastName, c.Country FROM Customers c WHERE c.CustomerId NOT IN (SELECT o.CustomerId FROM Orders o); ``` |
| NOT | Negates a condition, filtering out rows that match the specified criteria. Use it in combination with other operators to give the opposite result, also called the negative result.  **Syntax**   ``` SELECT field_1, field_1, ... FROM entity WHERE NOT condition; ```     **Example 1 - select customers except those from Romania**   ``` SELECT s.FirstName, s.LastName, s.Country FROM Customers s WHERE NOT Country = 'Romania' ```   If you need to exclude multiple values, use the `NOT IN` operator. |
| IS NULL | Checks for null values. Use it in the `WHERE` clause to select entity records with a NULL value in a specific field.  **Syntax**   ``` SELECT      field_1,      field_2,      field_N FROM      entity WHERE      field_N IS NULL ```     **Example: select customers who have a NULL value in the Address field**   ``` SELECT      s.CustomerName,      s.ContactName,      s.Address FROM      Customers s WHERE      s.Address IS NULL ``` |
| IS NOT NULL | Checks for non-empty values (NOT NULL values). Use it in the `WHERE` clause to select entity records with a non-empty value in a specific field.  **Syntax**   ``` SELECT      field_1,      field_2,      field_N FROM      entity WHERE      field_N IS NOT NULL ```     **Example: select customers who have a value in the Address field**   ``` SELECT      s.CustomerName,      s.ContactName,      s.Address FROM      Customers s WHERE      s.Address IS NOT NULL ``` |

## ORDER BY

Sorts the result set of a query by one or more fields / aliases in ascending or descending order.

**Syntax**

```
SELECT field_1, field_2, ...
FROM entity
ORDER BY field_1, field_2, ... ASC|DESC
```

{% hint style="info" %}
**NOTE:** The `ORDER BY` keyword sorts the records in ascending order by default.
{% endhint %}

Example:

This query will return a list of products, showing the Name, ID, and Price for each product in the Products entity, sorted alphabetically by the ProductName. If there are multiple products with the same name, they will appear in the same order they were stored in the database.

**Example - Sort the records in ascending order**

```
SELECT s.ProductName Name, s.ProductID ID, s.Price Price
FROM Products s
ORDER BY s.ProductName
```

To sort the records in descending order, use the `DESC` keyword.

**Example - Sort the records in ascending order**

```
SELECT s.ProductName Name, s.ProductID ID, s.Price Price
FROM Products s
ORDER BY s.ProductName DESC
```

When multiple fields are specified, the query first sorts the records by the first field. If there are ties (i.e., records with the same value in the first filed), it then sorts those records based on the second field, and so on.

The following query selects all customers from the Customers entity, sorted by the Country and the CustomerName fields. This means that it orders by Country, but if some rows have the same Country, it orders them by CustomerName.

**Example - order records by multiple fields**

```
SELECT 
    s.CustomerID, 
    s.CustomerName, 
    s.ContactName, 
    s.Country, 
    s.City, 
    s.Phone
FROM Customers s
ORDER BY s.Country, s.CustomerName
```

## GROUP BY

Groups records that have the same values in specified fields. It is often used in conjunction with aggregate functions to perform calculations on each group.

**Syntax**

```
SELECT field(s)
FROM entity
WHERE condition
GROUP BY field(s)
ORDER BY field(s)
```

The following query gives the count of customers grouped by both Country and City.

**Example - grouping by multiple fields**

```
SELECT Country, City, COUNT(CustomerID) AS NumberOfCustomers
FROM Customers
GROUP BY Country, City
```

When joining data from two tables (entities), you can group results using either aliased or original column names. Grouping by original column names, introduced in druid 8.10, aligns with standard SQL conventions.

The following query groups the results using the original column names (b.CreatedOn, s.Name, s.Color).

**Example - GROUP BY column name**

```
SELECT    COUNT(*) Counter, 
   TRUNC(month, b.CreatedOn) CreatedOn, 
   s.Name Status.Name, s.Color Status.Color
FROM Book b 
LEFT JOIN BookStatus s ON b.StatusId = s.Id 
GROUP BY b.CreatedOn, s.Name, s.Color
```

The following query groups the results using the aliased column names (CreatedOn, Status.Name, Status.Color).

**Example - GROUP BY column alias**

```
SELECT    COUNT(*) Counter, 
   TRUNC(month, b.CreatedOn) CreatedOn, 
   s.Name Status.Name, s.Color Status.Color
FROM Book b 
LEFT JOIN BookStatus s ON b.StatusId = s.Id 
GROUP BY CreatedOn, Status.Name, Status.Color
```

<a id="HAVING"></a>

## HAVING

Groups records after they have been aggregated, unlike the `WHERE` clause which filters individual records before aggregation. It's specifically designed to work with aggregate functions (like `COUNT`, `SUM`, `AVG`, `MIN`, and `MAX`) and allows you to filter groups based on the results of those aggregations.

**Syntax**

```
SELECT field(s)
FROM entity
HAVING condition
```

The following query will return a list of departments from the Sales entity where the total sales for each department exceed 100,000. It will display the department name and the corresponding total sales for departments that meet this criterion.

**Example**

```
SELECT DepartmentName AS Name, SUM(Amount) AS "Total Sales"
FROM Sales
GROUP BY DepartmentName
HAVING SUM(Amount) > 100000
```

<a id="AggregateFunctions"></a>

## Aggregate Functions

<a id="MIN"></a>

## MIN

Returns the smallest value of the selected field.

**Syntax**

```
SELECT MIN(field)
FROM entity
```

**Example - return the smallest price for each category in the Products entity**

```
SELECT MIN(Price) AS SmallestPrice, CategoryID 
FROM Products
GROUP BY CategoryID
```

<a id="MAX"></a>

## MAX

Returns the highest value of the selected field.

**Syntax**

```
SELECT MAX(field)
FROM entity
```

**Example - the maximum order amount per order**

```
SELECT s.OrderID ID, 
       s.OrderName Name, 
       MAX(s.Amount) AS MaxAmount, 
       s.OrderDate
FROM Orders s
WHERE s.OrderDate >= '2024-01-01'
GROUP BY s.OrderID, s.OrderName, s.OrderDate
```

<a id="AVG"></a>

## AVG

Returns the average value in a set.

**Syntax**

```
SELECT AVG(field)
FROM entity
```

The following query returns only the customers whose average order amount exceeds $5000 for orders placed on or after January 1, 2024.

**Example**

```
SELECT s.CustomerID, 
       AVG(s.Amount) AS AverageOrderAmount
FROM Orders s
WHERE s.OrderDate >= CONVERT(DateTime, '2024-01-01')
GROUP BY s.CustomerID
HAVING AVG(s.Amount) > 5000
```

<a id="COUNT"></a>

## COUNT

Returns the number of records in a dataset.

**Syntax**

```
SELECT COUNT(*)
FROM entity
```

{% hint style="info" %}
**NOTE:** `COUNT(field)` is not supported in Druid; therefore, you cannot exclude NULL values when counting records. Only `COUNT(*)` can be used, which includes all records.
{% endhint %}

The following query retrieves the number of products in each category from the Products entity.

**Example**

```
SELECT COUNT(*) AS 'Products Number', CategoryName Name
FROM Products
GROUP BY CategoryName
```

## COUNT(DISTINCT field)

Counts the number of unique (non-duplicate) values in a specified field. This is useful when you want to determine how many distinct entries exist in a dataset for a particular field.

**Syntax**

```
SELECT COUNT(DISTINCT field)  
FROM entity
```

For example, it can be used to count the number of different prices, product categories, or any other field where duplicates may exist but are not needed in the count.

The following query returns how many distinct customers have purchased distinct products during the year 2024.

**Example**

```
SELECT COUNT(DISTINCT CustomerID) AS 'Unique Customers', 
       COUNT(DISTINCT ProductID) AS 'Unique Products'
FROM Sales
WHERE SaleDate >= CONVERT(DateTime, '2024-01-01')
  AND SaleDate <= CONVERT(DateTime, '2024-12-31')
```

<a id="STRING_AGG"></a>

## STRING\_AGG

This function combines values from a field across an entity list into a single string, inserting a specified delimiter between each value.

it returns a string value containing all non-null field values from the entity list separated by the delimiter. If all entries in a group are NULL, the function returns NULL.

**Syntax**

```
STRING_AGG(field, delimiter)
```

Parameters:

- **field**: The target field containing values to concatenate. Non-string values are converted to string types.
- **delimiter:** The string separator inserted between concatenated values.

The following query groups records by department ID and concatenates values from the name field across the employees entity list into a single comma-separated string:

```
SELECT dept_id,
       STRING_AGG(name, ', ') AS names
FROM employees
GROUP BY dept_id;
```

<a id="Joins"></a>

## Joins

## INNER JOIN

Selects records that have matching values in both the specified parent entity and the child entity.

**Syntax**

```
SELECT entity_field(s)
FROM parent_entity
INNER JOIN child_entity
ON parent_entity.entity_field = child_entity.entity_field;
```

**Example**

```
SELECT Suppliers.SupplierId, Suppliers.SupplierName, Orders.OrderDate
FROM Suppliers
INNER JOIN Orders
ON Suppliers.SupplierId = Orders.SupplierId;
```

The query returns all records from the Suppliers and Orders entities where there is a matching SupplierId value in both the Suppliers and Orders entities. If one of the records is missing the SupplierId in one of the two entities, the record will be omitted from the result.

## LEFT JOIN

Returns all records from the parent, and the matching records from the child entity. The result is 0 records from the parent entity, if there is no match.

**Syntax**

```
SELECT field_name
FROM parent_entity
LEFT JOIN child_entity
ON parent_entity1.field_name = child_entity.field_name;
```

**Example**

```
SELECT Customers.CustomerName, Orders.OrderID
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
ORDER BY Customers.CustomerName
```

The query retrieves customer names and their corresponding order IDs. It returns all customers, including those who do not have any orders. Customers without orders will have a NULL value in the OrderID column. The results are sorted alphabetically by customer name.

## RIGHT JOIN

Druid does not support `RIGHT JOIN`. If you wanted to use a `RIGHT JOIN` (e.g., fetching all records from table B and the matching records from table A), you can rewrite it with a `LEFT JOIN` by swapping the tables.

Let’s say you want to join the Orders table and the Customers table, where you want to make sure all the Orders appear in your results, even if they don’t have matching customers.

**Example**

```
SELECT Orders.OrderID, Customers.CustomerName
FROM Customers
LEFT JOIN Orders ON Customers.CustomerID = Orders.CustomerID
ORDER BY Orders.OrderID
```

Where:

- `LEFT JOIN` ensures that all records from the Customers table are returned.
- By swapping the order of the tables, Customers becomes the left table and Orders becomes the right table. This ensures that you get all rows from Orders, just like a `RIGHT JOIN` would do in other SQL systems.

Even though Druid doesn’t support `RIGHT JOIN`, this approach using `LEFT JOIN` with the tables reversed gives you the same result.

<a id="SetOperations"></a>

## Set Operations

<a id="UNION"></a>

## UNION

Combines the results of two or more `SELECT` queries into a single result set. By default, **UNION** eliminates duplicate rows, ensuring that the result contains only unique records.

{% hint style="info" %}
**NOTE:** This operator is available in DRUID 8.9 and higher.
{% endhint %}

{% hint style="info" %}
**Info:** If you want to keep all records, including duplicates, use `UNION ALL` instead.
{% endhint %}

*Example*:

- Let's assume you have two entities: [[Sales]] and [[Revenue], both containing CustomerId and PurchaseAmount fields.
- You want to combine the data from the [[Sales]] and [[Revenue]] entities, but only include distinct records (unique combinations of CustomerId and PurchaseAmount).

**Example**

```
SELECT s.CustomerId ID, s.PurchaseAmount Amount
FROM Sales s
UNION
SELECT t.CustomerId ID, t.PurchaseAmount Amount
FROM Revenue t
```

## UNION ALL

Combines the results of two or more `SELECT` queries into a single result set, including duplicates. Unlike `UNION`, which removes duplicates, `UNION ALL` retains all records from the combined queries, even if they are identical.

{% hint style="info" %}
**NOTE:** This operator is available in DRUID 8.9 and higher.
{% endhint %}

*Example*:

- Let's assume you have two entities: [[Sales]] and [[Revenue]], both containing CustomerId and PurchaseAmount fields.
- You want to combine the data from the [[Sales]] and [[Revenue]] entities, and include all records, even duplicates.

**Example**

```
SELECT s.CustomerId ID, s.PurchaseAmount Amount
FROM Sales s
UNION ALL
SELECT t.CustomerId ID, t.PurchaseAmount Amount
FROM Revenue t
```

The result will include all records, even if there are duplicate records between the [[Sales]] and [[Revenue]] entities.

<a id="INTERSECT"></a>

## INTERSECT

Returns only the rows that are common between two `SELECT` queries. In other words, it returns the intersection of the result sets — only the records that exist in both queries.

INTERSECT removes duplicates by default, so if a record appears multiple times in both queries, it will only appear once in the result.

{% hint style="info" %}
**NOTE:** This operator is available in DRUID 8.9 and higher.
{% endhint %}

Example:

- Let’s say you have two Druid entities: [[Customers]] and [[Subscribers]], each with a CustomerId and Email field.
- You want to find the customers who are both customers and have subscribed to your newsletter.

**Example**

```
SELECT CustomerId, Email
FROM Customers
INTERSECT
SELECT CustomerId, Email
FROM Subscribers
```

The result contains only the records that are common in both entities [[Customers]] and [[Subscribers]].

<a id="EXCEPT"></a>

## EXCEPT

Returns the records from the first `SELECT` query that do not exist in the second `SELECT` query. Essentially, it retrieves the difference between the two result sets, excluding any duplicate rows by default.

{% hint style="info" %}
**NOTE:** This operator is available in DRUID 8.9 and higher.
{% endhint %}

Example:

- Let’s say you have two Druid entities: [[Employees]] and [[Contractors]], each with EmployeeId and Name fields.
- You want to find all the employees who are not contractors.

```
SELECT EmployeeId, Name
FROM Employees
EXCEPT
SELECT EmployeeId, Name
FROM Contractors;
```

<a id="ExpressionsandOperators"></a>

## Expressions and Operators

Expressions allow you to perform calculations or operations on fields, literals, and constants. These expressions are often combined with operators to manipulate the data within your queries.

{% hint style="info" %}
**Info:** You can also use expressions in the `WHERE` clause to filter results.
{% endhint %}

## Arithmetic Operators

Druid supports basic arithmetic operators for mathematical calculations:

- +: Addition
- -: Subtraction
- \*: Multiplication
- /: Division

{% hint style="info" %}
**NOTE:**

- The arithmetic operators are used for arithmetic calculations when both fields are numeric data types (e.g., int, float, decimal).
- If any of expression fields contains NULL values, the result of the addition will be NULL unless handled explicitly with functions like `COALESCE` or `ISNULL`.
- The expression can be used in the `SELECT` clause to create a new column in the result set that holds the result.
{% endhint %}

This example multiplies Price by Quantity to calculate the total cost of an order:

**Example**

```
SELECT Price * Quantity AS TotalCost
FROM Orders
```

## Expression Literals

Literals are fixed values used directly in statements. They can be of various data types, including strings, numbers and date and time.

{% hint style="info" %}
**NOTE:**

- **String Literals**: Use single quotes to enclose string values. Double quotes are not used for strings.
- **Numeric Literals**: Write numbers directly without quotes.
- **Date and Time Literals**: Use single quotes to enclose date and time values.
{% endhint %}

This expression adds 10 to the Price field for each record, creating a new calculated field NewPrice.

**Example**

```
SELECT Price + 10 AS NewPrice
FROM Products
```

<a id="Functions"></a>

## <a id="Function"></a>Functions

<a id="ROUND"></a>

## ROUND

{% hint style="info" %}
**Info:** This function is available starting with Druid 9.30.
{% endhint %}

Rounds a numeric value or calculation to a specified number of decimal places. `ROUND()` can be used on numeric expressions, as well as wrapped around aggregate functions (such as `AVG`, `SUM`, `MIN`, `MAX`, or `COUNT`).

**Syntax**

```
ROUND(numeric_expression, decimal_places)
```

Where:

- **numeric\_expression**: A numeric field, arithmetic calculation, or aggregate function (e.g., AVG()).
- **decimal\_places**: The number of decimal places to round the result to.

**Example — Using ROUND with an Aggregate Function**

```
SELECT
    [item].[Name] AS [Name],
    ROUND(AVG([item].[Price] * 1.0), 2) AS [AveragePrice]
FROM [Item] [item]
WHERE [item].[Price] > 1
GROUP BY [item].[Name]
ORDER BY [item].[Name] ASC;
```

<a id="StringFunctions"></a>

## String Functions

String functions are used to manipulate and process text (string) data. These functions help format, extract, replace, and analyze string values.

{% hint style="info" %}
**NOTE:** The string functions are supported in DRUID 7.2 and higher.
{% endhint %}

<a id="LEFT"></a>

## LEFT

Returns the leftmost part of a character string based on the specified number of characters.

**Syntax**

```
LEFT(character_expression, integer_expression)
```

Where:

- *character\_expression*  is an entity field.
- *integer\_expression* is a positive integer that specifies how many characters of the *character\_expression* will be returned. If *integer\_expression* is negative, an error is returned.

**Example - extract the first 3 characters from the CustomerName**

```
SELECT LEFT(CustomerName, 3) AS ShortName
FROM Customers
```

<a id="LEN"></a>

## LEN

Returns the number of characters in a specified string, excluding trailing spaces.

**Syntax**

```
LEN(field)
```

This function is useful for validating input lengths, formatting data, or applying text-based conditions in queries.

**Example**

```
SELECT CustomerName, LEN(CustomerName) AS NameLength  
FROM Customers  
WHERE LEN(CustomerName) > 5  
ORDER BY NameLength DESC
```

<a id="LTRIM"></a>

## LTRIM

Removes leading spaces (or specified characters) from the beginning of a string. This function is useful for cleaning up user input, standardizing text, and improving data quality in queries.

**Syntax**

```
LTRIM(field [, characters])
```

**Example**

```
SELECT CustomerName, LTRIM(CustomerName) AS TrimmedName
FROM Customers
```

<a id="LOWER"></a>

## LOWER

converts all uppercase letters in a string to lowercase. This function is useful for case-insensitive comparisons, normalizing text, and formatting data consistently.

**Syntax**

```
LOWER(field)
```

**Example**

```
SELECT CustomerName, LOWER(CustomerName) AS LowercaseName
FROM Customers
```

<a id="REPLACE"></a>

## REPLACE

Replaces all occurrences of a specified substring within a string with another substring. This function is useful for standardizing text, cleaning data, and making bulk text modifications in queries.

**Syntax**

```
REPLACE(field, string_pattern, string_replacement)
```

Where:

- `field` – The original field of type string where replacements occur.
- `string_pattern` – The substring to be found and replaced.
- `string_replacement` – The new substring that replaces `string_pattern`.

**Example - replace occurrences of "Inc." with "LLC" in company names**

```
SELECT CompanyName, REPLACE(CompanyName, 'Inc.', 'LLC') AS UpdatedCompanyName
FROM Companies
```

<a id="RIGHT"></a>

## RIGHT

Returns a specified number of characters from the end (right side) of a string. This function is useful for extracting suffixes, checking data patterns, and formatting outputs.

**Syntax**

```
RIGHT(field, integer_expression)
```

**Example - extract the last 4 characters of customer phone numbers**

```
SELECT CustomerName, CustomerPhone, RIGHT(CustomerPhone, 4) AS LastDigits
FROM Customers
```

<a id="RTRIM"></a>

## RTRIM

Removes trailing spaces (or specified characters) from the end of a string. This function is useful for cleaning up user input, normalizing text, and ensuring consistent data formatting.

**Syntax**

```
RTRIM(field [, characters])
```

Where:

- `field` – A field of type string value to be trimmed.
- `characters` (Optional) – A set of characters to remove from the end of the string. If not specified, only space characters (CHAR(32)) are removed.

**Example - remove trailing spaces from customer names**

```
SELECT CustomerName, RTRIM(CustomerName) AS TrimmedName
FROM Customers
```

<a id="SUBSTRING"></a>

## SUBSTRING

Extracts a portion of a string based on the given starting point and length of the desired substring.

**Syntax**

```
SUBSTRING(field, start, length)
```

Where:

- `field` – A field from which the substring will be extracted.
- `start` – An integer that specifies the starting position for the substring. The position starts at 1, meaning the first character is at position 1. If start is less than 1, the substring will begin at the first character.
- `length` – A positive integer that specifies how many characters to extract from the starting position. If the sum of start and length exceeds the available characters, the entire string from start will be returned. A negative length will generate an error.

**Example - extract the first 5 characters from the CustomerName field**

```
SELECT CustomerName, SUBSTRING(CustomerName, 1, 5) AS First5Chars
FROM Customers
```

<a id="UPPER"></a>

## UPPER

Converts all lowercase letters in a string to uppercase. This function is useful for standardizing text, ensuring consistent capitalization, and comparing strings in a case-insensitive manner.

**Syntax**

```
UPPER(field)
```

**Example - convert customer names to uppercase**

```
SELECT CustomerName, UPPER(CustomerName) AS Name
FROM Customers
```

<a id="DATETIMEFunctions"></a>

## DATETIME Functions

You can use the following DATETIME functions in a DRUID Custom Query to manipulate and filter data based on date and time values. These functions support use cases such as rounding to specific time intervals, shifting dates, and extracting specific parts of a timestamp.

<a id="DATEADD"></a>

## DATEADD

Adds or subtracts a specific interval from a DATETIME value.

**Syntax**

```
DATEADD(unit, number, datetime_value)
```

Where:

- `unit` – The part of the date to change (e.g., 'DAY', 'HOUR', 'MONTH').
- `number` – A positive or negative integer indicating the amount to add or subtract.
- `datetime_value` – The base date or timestamp.

**Example: Orders from the Last 7 Days**

```
SELECT ClientName, OrderDate
FROM Clients
WHERE OrderDate >= DATEADD(DAY, -7, CURRENT_TIMESTAMP)
```

The query returns clients with orders placed in the last 7 days.

**Example: Orders in the Previous Quarter**

```
SELECT ClientName, OrderDate
FROM Clients
WHERE TRUNC(QUARTER, OrderDate) = TRUNC(QUARTER, DATEADD(QUARTER, -1, CURRENT_TIMESTAMP))
```

The query returns orders from the previous quarter.

<a id="DATEPART"></a>

## DATEPART

Extracts a specific part of a DATETIME value.

**Syntax**

```
DATEPART(unit, datetime_value)
```

Supported units:

- YEAR
- QUARTER
- MONTH
- DAY
- HOUR
- MINUTE
- SECOND
- WEEK
- WEEKDAY (day of week)

**Example: Orders in the Current Month**

```
SELECT ClientName, OrderDate
FROM Clients
WHERE DATEPART(MONTH, OrderDate) = DATEPART(MONTH, CURRENT_TIMESTAMP)
  AND DATEPART(YEAR, OrderDate) = DATEPART(YEAR, CURRENT_TIMESTAMP)
```

The query returns orders from the current month and year.

<a id="DATEDIFF"></a>

## DATEDIFF

Calculates the number of specified time units that have elapsed between a starting date/time expression and an ending date/time expression. This function is useful for determining durations, calculating age, measuring time differences, or filtering records based on time intervals.

{% hint style="info" %}
**NOTE:** This function is available in Druid 9.11 and higher.
{% endhint %}

**Syntax**

```
DATEDIFF(start_datetime, end_datetime, unit)
```

- YEAR
- QUARTER
- MONTH
- DAY
- HOUR
- MINUTE
- SECOND
- WEEK

The functions returns a numeric value representing the difference in the specified unit:

- A **positive integer** if end\_datetime is later than start\_datetime.
- A **negative integer** if end\_datetime is earlier than start\_datetime.
- **0** if both dates are the same for the specified unit.

**Example: Group Orders by Month Difference**

```
SELECT DATEDIFF(OrderDate, CURRENT_TIMESTAMP, MONTH) AS MonthsAgo,
       COUNT(*) AS OrderCount
FROM Orders
GROUP BY DATEDIFF(OrderDate, CURRENT_TIMESTAMP, MONTH)
ORDER BY MonthsAgo ASC
```

In the example above:

1. The function calculates the number of months between when the order was placed and today. This creates categories like: 0 (this month), 1 (last month), 2 (2 months ago), etc.
2. All orders from the same "months ago" period are grouped together.
3. Counts how many orders are in each group.
4. Sorts the results in ascending order - showing the most recent months first.

**Example: Calculate Minutes Between Record Creation and Modification**

```
SELECT
    ModifiedOn,
    CreatedOn,
    DATEDIFF(CreatedOn, ModifiedOn, MINUTE) AS DurationInMinutes
FROM
    Event
WHERE
    DateDiff(CreatedOn, ModifiedOn, MINUTE) > 0
```

In the example above:

1. The function calculates the difference in minutes between when the Event entity was created and when it was last modified.
2. The result is returned in a new column named DurationInMinutes.
3. The `WHERE` clause filters the results to only include records where the modification date is after the creation date (i.e., the duration is positive).

<a id="GETDATE"></a>

## GETDATE

Returns the current date and time in UTC. Unlike traditional SQL's GETDATE() which returns server local time, this function always returns UTC time with the 'Z' timezone indicator.

{% hint style="info" %}
**NOTE:** This function is available in Druid 9.10 and higher.
{% endhint %}

**Syntax**

```
GETDATE()
```

**Example: Orders placed today (UTC)**

```
SELECT ClientName, OrderDate
FROM Orders
WHERE TRUNC(DAY, OrderDate) = TRUNC(DAY, GETDATE())
```

**Example: Orders from the last 24 hours**

```
SELECT ClientName, OrderDate, OrderAmount
FROM Orders
WHERE OrderDate >= DATEADD(HOUR, -24, GETDATE())
ORDER BY OrderDate DESC
```

<a id="TODAY"></a>

## TODAY

Returns the current date in UTC with the time component set to midnight (00:00:00). This function is useful for date-only comparisons without considering the time of day.

{% hint style="info" %}
**NOTE:** This function is available in Druid 9.10 and higher.
{% endhint %}

**Syntax**

```
TODAY()
```

**Example: Orders placed today**

```
SELECT ClientName, OrderDate, OrderAmount
FROM Orders
WHERE OrderDate >= TODAY()
```

**Example: Orders from the last 7 days**

```
SELECT ClientName, OrderDate
FROM Orders
WHERE OrderDate >= DATEADD(DAY, -7, TODAY())
ORDER BY OrderDate DESC
```

<a id="TRUNC"></a>

## TRUNC

Rounds down a DATETIME value to the nearest specified unit.

**Syntax**

```
TRUNC(unit, datetime_value)
```

Supported units:

- SECOND
- MINUTE
- HOUR
- DAY
- WEEK
- MONTH
- QUARTER
- QUARTER\_END
- YEAR

**Example: Orders Rounded to the Same Day**

```
SELECT ClientName, OrderDate
FROM Clients
WHERE TRUNC(DAY, OrderDate) = TRUNC(DAY, CURRENT_TIMESTAMP)
```

The query returns clients who placed orders today.

**Example: Orders This Quarter**

```
SELECT ClientName, OrderDate
FROM Clients
WHERE TRUNC(QUARTER, OrderDate) = TRUNC(QUARTER, CURRENT_TIMESTAMP)
```

The query returns orders placed in the current quarter.

<a id="AdvancedFunctions"></a>

## Advanced Functions

<a id="COALESCE"></a>

## COALESCE

Handles missing data (NULL values) in a dataset by providing an alternative (default) value. This can be useful when displaying data in reports or queries where missing information should be replaced with a more meaningful or user-friendly substitute.

**Syntax**

```
SELECT COALESCE(field(s), 'default value')
FROM entity
```

The following query ensures that for each client, the client name is displayed, and if a phone number or address is missing, default values are substituted.

**Example with multiple fields and default values**

```
SELECT s.ClientName AS Name,
       COALESCE(s.ClientPhone, 'No phone number') AS Phone,
       COALESCE(s.ClientAddress, 'No address provided') AS Address
FROM Account s
```

**Example with multiple fields and default value**

```
SELECT s.ClientName AS Name,
       COALESCE(s.ClientPhone, s.ClientAddress 'No data') AS ContactInfo
FROM Account s
```

## CONVERT to VARCHAR, INTEGER, FLOAT or DECIMAL

Converts the value of a field in a dataset to a specified data type. You can use this function to transform data into the following types: varchar, int, float, or decimal. Use this function when you need to ensure that data is in the correct format for querying, calculations, or comparisons.

**Syntax**

```
CONVERT(target_data_type, field)
```

**Convert to VARCHART example**

The following query converts the ProductID field to a string and combines it with the product name. Converting ProductID to varchar allows you to combine numeric and text values in one column, which is useful for labels, reports, or display purposes.

```
SELECT 
    s.ProductName AS Name, 
    'Product #' + CONVERT(varchar, s.ProductID) AS ProductLabel
FROM Products s
```

Example output:

![](../../Resources/Images/Druid%20Data%20Service%20Connector/varchart%20output.png)

**Convert to INTEGER example**

The following query converts the ProductPrice field to an integer data type.

```
SELECT s.ProductName AS Name, CONVERT(int, s.ProductPrice) AS Price
FROM Products s
```

Example output:

![](../../Resources/Images/Druid%20Data%20Service%20Connector/integert%20example.png)

{% hint style="info" %}
**NOTE:** Converting to **int** removes any decimal portion—it does not round, it just truncates.
{% endhint %}

**Convert to FLOAT example**

The following query converts the ProductPrice field to a float data type.

```
SELECT s.ProductName AS Name, CONVERT(float, s.ProductPrice) AS Price
FROM Products s
```

Example output:

![](../../Resources/Images/Druid%20Data%20Service%20Connector/float%20example.png)

**Convert to DECIMAL example**

The following query converts the ProductPrice field to a decimal data type.

```
SELECT s.ProductName Name, CONVERT(decimal, s.ProductPrice) AS Price
FROM Products s
```

Example output:

![](../../Resources/Images/Druid%20Data%20Service%20Connector/decimal%20example.png)

## CONVERT to the specified date format

Converts int, decimal, double, datetime and varchar to the specified date format.

Use the following syntax for CONVERT with three parameters:

**Syntax**

```
convert(data_type, data_to_convert, {FormatId})
```

**Example**

```
SELECT CONVERT(VARCHAR, a.CreatedOn) AS CreatedOnFormatted
FROM Account a;
```

| Format Id | DRUID Data Service Pattern | T-SQL Pattern |
| --- | --- | --- |
| 1 | "%m/%d/%Y" | "MM/DD/YY" |
| 2 | "%Y.%m.%d | "YY.MM.DD" |
| 3 | "%d/%m/%Y" | "DD/MM/YY" |
| 4 | "%d.%m.%Y" | "DD.MM.YY" |
| 6 | "%d %b %Y" | "DD MMM YY" |
| 8 | "%H:%M:%S" | "hh:mm:ss" |
| 110 | "%m-%d-%Y" | "MM-DD-YYYY" |
| 111 | "%Y/%m/%d" | "YYYY/MM/DD" |
| 112 | "%Y%m%d" | "YYYYMMDD" |
| 114 | "%d %b %Y %H:%M:%S:%L" | "DD MMM YYYY HH:MM:SS:MMM" |
| 120 | "%Y-%m-%d %H:%M:%S" | "YYYY-MM-DD HH:MM:SS" |
| 121 | "%Y-%m-%d %H:%M:%S.%L" | "YYYY-MM-DD HH:MM:SS.mmm" |
| 130 | "%d %b %Y %H:%M:%S:%L" | "dd mon yyyy hh:mi:ss:mmm(AM/PM)" |

{% hint style="info" %}
**NOTE:**

- DRUID Data Services pattern is currently missing 2-digit years.
- %b or Month as 3 letter in DRUID Data Services pattern is after FormatId **7** (130, 114, 6).
{% endhint %}

<a id="Recordslimitingclauses"></a>

## Records limiting clauses

<a id="OFFSET"></a>

## OFFSET

Skips a specified number of records before returning results. Used in combination with `FETCH NEXT`, limits the number of records returned after the offset.

{% hint style="info" %}
**NOTE:** This clause is available in DRUID 8.3 and higher.
{% endhint %}

**Example**

```
SELECT e.Id, e.Name, e.Description, ef.EntityMetadataId, ef.LastModificationTime 
FROM EntityMetadata e 
JOIN EntityFieldMetadata ef ON ef.EntityMetadataId = e.Id 
ORDER BY ef.LastModificationTime DESC 
OFFSET 90 ROWS FETCH NEXT 15 ROWS ONLY
```

In this example:

- The query retrieves a specific subset of rows from a joined result of two tables, EntityMetadata (e) and EntityFieldMetadata (ef).
- The results are ordered by the LastModificationTime column from the EntityFieldMetadata table (ef) in descending order. This means that the most recently modified records will appear first in the result set.
- The `OFFSET` statement skips the first 90 rows of the ordered result set. It means that the retrieval starts from the 91st row onward.
- After skipping the first 90 rows, the `FETCH` statement limits the number of rows returned to the next 15 rows only, effectively giving rows 91 through 105 in the ordered list.

<a id="TOP"></a>

## TOP

Limits the result set to a specified number of rows. However, without proper ordering, the results can appear in an arbitrary order. To ensure a predictable and meaningful result, it is always recommended to use the `TOP` clause in combination with `ORDER BY`.

{% hint style="info" %}
**NOTE:**  This function is supported in DRUID 7.2 and higher.
{% endhint %}

**Syntax**

```
SELECT TOP <number_of_rows> field
FROM entity
ORDER BY field
```

**Example**

```
SELECT TOP 5 FirstName, LastName
FROM Contact
ORDER BY FirstName
```

<a id="JoiningwithEntityFieldsforLargeDataVolumes"></a>

## <a id="Joining"></a>Joining with Entity Fields for Large Data Volumes

When working with large data volumes, using the `GROUP BY` clause correctly is essential for both accurate results and good query performance. Aggregating data by specific groupings, especially when joining related entity fields, allows you to combine data from multiple entities while ensuring correct aggregation across joined entities. Incorrect grouping can lead to inaccurate results or inefficient queries.

{% hint style="warning" %}
**IMPORTANT!** Indexing is critical when working with large data sets. Make sure that entities and fields used in joins and aggregation are properly indexed. For more information, see [Add Data Service Indexes](../Data%20Service/Druid_Data_Service.md#Add).
{% endhint %}

{% hint style="info" %}
**NOTE:** Joining data from referenced entities is available starting with Druid 19.16.
{% endhint %}

<a id="Importantconsiderations"></a>

### Important considerations

When joining entity fields and aggregating data, keep the following in mind:

- Bracket notation is used to expose related entity fields in the result set.
- All non-aggregated fields in the `SELECT` clause must also appear in the `GROUP BY` clause.
- Aliases help avoid ambiguity when referencing fields from joined entities.
- All date and time values are stored in Druid as UTC. Time offsets may be required to account for user time zones. Truncating the adjusted timestamp removes the time component so all records for the same day are grouped together.

<a id="Syntax"></a>

### Syntax

**Syntax**

```
SELECT 
  aggregate_function(field_1) AS Alias, 
  field_2, 
  RelatedEntity.Field 
FROM 
  Entity AS alias 
GROUP BY 
  field_2, 
  RelatedEntity.Field 
ORDER BY 
  field_2 ASC
```

<a id="Example1Aggregatingdatausingrelatedentityfields"></a>

### Example 1: Aggregating data using related entity fields

The following example counts books and groups the results by author. The **Book** entity is joined with the related Author entity, and author fields are included in the aggregation.

**Example 1 query**

```
SELECT 
COUNT(*) AS Counter, 
author.Id   [BookAuthor.Id] // BookAuthor is field Book for Authors
author.FirstName   [BookAuthor.FirstName]   // 
FROM Book AS book
JOIN Author AS author on author.Id = book.BookAuthorId
GROUP BY field_2, RelatedEntity.Field 
ORDER BY field_2 ASC
```

<a id="Example2Aggregatingdatausingdatenormalization"></a>

### Example 2: Aggregating data using date normalization

The following example aggregates books by name and by day. The **ReceivedOn** timestamp is adjusted by 120 minutes and then truncated to the start of the day to ensure correct daily grouping.

**Example 2 query**

```
SELECT
    b.BookName,
    TRUNC(day, DATEADD(minute, 120, b.ReceivedOn)) AS ReceivedOn,
    COUNT(*) Counter
FROM Book b
GROUP BY b.BookName, b.ReceivedOn
ORDER BY b.BookName, b.ReceivedOn
```
