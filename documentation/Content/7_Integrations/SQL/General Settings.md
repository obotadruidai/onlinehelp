<a id="GeneralSettings"></a>

# General Settings

After you click to create an SQL task, the Edit Connector Task page appears by default on the **General** tab.

Set the general parameters:

| Parameter | Description |
| --- | --- |
| Description | Provide a brief relevant description of the task to be performed. |
| ConnectionCode | Select the SQL app (for Connection Strings to the database)  **NOTE:** Different SQL Tasks in the same connector action (integration) can connect to different SQL instances/databases, by choosing the corresponding SQL Connector App (ConnectionCode) for each one. |
| TransactionMode | Select the transaction mode based on which a specific SQL statement is performed against the DB:  ![](../../Resources/Images/SQL%20Connector/General%20Settings.png)  The following options are available:   - **IfAnyTransactionUseTransaction**- If the SQL connection opened by the Druid Connector finds any open transaction, it will run the statement within that transaction. Closing the transaction (commit or rollback) will NOT be performed by the Druid Connector, in this case, as the transaction is not initiated by it. - **NoTransaction** - The Druid Connector will run the SQL statement outside any transaction. - **BeginAndCommitTransaction** - The Druid Connector will begin a transaction, will run the statement within that transaction, and then will commit the transaction. - **UseAndCommitTransaction** - The Druid Connector will use an existing transaction to run the statement, then it will commit the transaction.  **NOTE:** That transaction must be initiated in advance. For example, by using BeginTransaction in a previous SQL Task. - **BeginTransaction** - The Druid Connector will begin a transaction and run the statement. The transaction will NOT be closed in this case, so another task which closes the transaction (UseAndCommitTransaction) should follow after this one. |

Click the **Save** button. Now you have to [configure the](Request%20Settings.md) [request to the SQL database](Request%20Settings.md).
