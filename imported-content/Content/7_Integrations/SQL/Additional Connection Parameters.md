---
title: "Additional Connection Parameters"
---

<a id="AdditionalConnectionParameters"></a>


To provide additional connection parameters, use the following syntax:

`<Connection Parameter>``=``<value>``;` `<Connection Parameter>``=``<value>``;` `<Connection Parameter>``=``<value>`

Example:

`Integrated Security=true; MultiSubnetFailover=Yes; Trusted_Connection=Yes`

To see the additional connection parameters you can use in Druid, click the link corresponding to the type of SQL database you want to integrate with:

- [SQL Server](#SQL_Server)
- [DB 2](#DB_2)
- [PostgreSQL](#PostgreSQL)
- [MySQL](#MySQL)
- [OracleSQL](#OracleSQL)

<a id="SQLServer"></a>

## <a id="SQL_Server"></a>SQL Server

The table below provides you with the list of additional connection parameters you can use when connecting to an SQL Server.

> **Info:** Use the table as a reference to ensure that you have included every property applicable to your specific situation. Some parameters have several equivalents. For those, each variant is specified on its own line separated with "-or-".

| Connection Parameter | Description |
| --- | --- |
| ApplicationName | The name of the application, or 'Core Microsoft SqlClient Data Provider' if no application name is provided.  This parameter is useful for debugging purposes. You can use the application name in the SQL profiler to filter the actions performed by the SQL Connector on the database. |
| Async | When true, enables asynchronous operation support. Recognized values are `true`, `false`, `yes`, and `no`. |
| Connect Timeout -or- Connection Timeout | The length of time (in seconds) to wait for a connection to the server before terminating the attempt and generating an error. |
| Connection Lifetime | When a connection is returned to the pool, its creation time is compared with the current time, and the connection is destroyed if that time span (in seconds) exceeds the value specified by Connection Lifetime. This is useful in clustered configurations to force load balancing between a running server and a server just brought online. A value of zero (0) causes pooled connections to have the maximum connection timeout. |
| Context Connection | `true` if an in-process connection to SQL Server should be made. |
| Connection Reset | Determines whether the database connection is reset when being removed from the pool. Setting to `false` avoids making an additional server round-trip when obtaining a connection, but the connection state is not being reset. |
| Current Language | The SQL Server Language record name. |
| Encrypt | When `true`, SQL Server uses SSL encryption for all data sent between the client and server if the server has a certificate installed. Recognized values are `true`, `false`, `yes` and `no`. |
| Enlist | When `true`, the pooler automatically enlists the connection in the creation thread's current transaction context. Recognized values are `true`, `false`, `yes` and `no`. |
| Failover Partner | The name of the failover partner server where database mirroring is configured. The Failover Partner keyword is not supported by .NET Framework version 1.0 or 1.1. |
| Load Balance Timeout | The minimum time, in seconds, for the connection to live in the connection pool before being destroyed. |
| MultipleActiveResultSets | When `true`, an application can maintain multiple active result sets (MARS). When `false`, an application must process or cancel all result sets from one batch before it can execute any other batch on that connection. Recognized values are `true` and `false`. The keyword is not supported by .NET Framework version 1.0 or 1.1. |
| Integrated Security -or- Trusted\_Connection | Whether the connection is to be a secure connection or not. Recognized values are 'true', 'false', and 'sspi', which is equivalent to 'true'. |
| Max Pool Size | The maximum number of connections allowed in the pool. |
| Min Pool Size | The minimum number of connections allowed in the pool. |
| Network Library -or- Net | The network library used to establish a connection to an instance of SQL Server. Supported values include `dbnmpntw` (Named Pipes), `dbmsrpcn` (Multiprotocol, Windows RPC), `dbmsadsn` (Apple Talk), `dbmsgnet` (VIA), `dbmslpcn` (Shared Memory, local machine only) and `dbmsspxn` (IPX/SPX), `dbmssocn` (TCP/IP) and `Dbmsvinn` (Banyan Vines). The corresponding network DLL must be installed on the system to which you connect. If you do not specify a network and you use a local server (for example, "." or "(local)"), shared memory is used. |
| Packet Size | Size in bytes of the network packets used to communicate with an instance of SQL Server. |
| Persist Security Info | When set to `false` (strongly recommended), security-sensitive information, such as the password, is not returned as part of the connection if the connection is open or has ever been in an open state. Resetting the connection string resets all connection string values including the password. |
| Pooling | When `true`, the SQLConnection object is drawn from the appropriate pool, or if necessary, is created and added to the appropriate pool. Recognized values are `true`, `false`, `yes` and `no`. |
| Replication | `true` if replication is supported using the connection. |
| Transaction Binding | Controls connection association with an enlisted System.Transactions transaction. Possible values are:   - `Transaction Binding=Implicit Unbind;` - `Transaction Binding=Explicit Unbind;`   `Implicit Unbind` causes the connection to detach from the transaction when it ends. After detaching, additional requests on the connection are performed in autocommit mode. The `System.Transactions.Transaction.Current` property is not checked when executing requests while the transaction is active. After the transaction has ended, additional requests are performed in autocommit mode.  `Explicit Unbind` causes the connection to remain attached to the transaction until the connection is closed or an explicit `SqlConnection.TransactionEnlist(null)` is called. An `InvalidOperationException` is thrown if `Transaction.Current` is not the enlisted transaction or if the enlisted transaction is not active. |
| TrustServerCertificate | When set to `true`, SSL is used to encrypt the channel when bypassing walking the certificate chain to validate trust. If `TrustServerCertificate` is set to `true` and `Encrypt` is set to `false`, the channel is not encrypted. Recognized values are `true`, `false`, `yes` and `no`. |
| Type System Version | A string value that indicates the type system the application expects. Possible values are:   - `Type System Version=SQL Server 2000;` - `Type System Version=SQL Server 2005;` - `Type System Version=SQL Server 2008;` - `Type System Version=Latest;`   When set to SQL Server 2000, the SQL Server 2000 type system is used. The following conversions are performed when connecting to a SQL Server 2005 instance:   - XML to NTEXT - UDT to VARBINARY - VARCHAR(MAX), NVARCHAR(MAX) and VARBINARY(MAX) to TEXT, NEXT and IMAGE respectively.   When set to SQL Server 2005, the SQL Server 2005 type system is used. No conversions are made for the current version of ADO.NET. When set to Latest, the latest version than this client-server pair can handle is used. This will automatically move forward as the client and server components are upgraded. |
| User Instance | A value that indicates whether to redirect the connection from the default SQL Server Express instance to a runtime-initiated instance running under the account of the caller. |
| Workstation ID | The name of the workstation connecting to SQL Server. |

<a id="DB2"></a>

## <a id="DB_2"></a>DB 2

The table below provides you with the list of additional connection parameters you can use when connecting to a DB 2.

<a id="ConnectionPooling"></a>

### Connection & Pooling

| Connection Parameter | Description |
| --- | --- |
| ConnectionLifetime | Sets the maximum time (in seconds) a pooled connection can remain open before being destroyed and recreated upon return to the pool. |
| ConnectionReset | Determines whether to reset the database connection state (such as temporary tables or session variables) when returned to the connection pool. |
| Enlist | Controls whether the connection automatically enlists in the application’s current ambient TransactionScope context. |
| MaxPoolSize / MinPoolSize | Specifies the upper and lower limits for the total number of physical database connections maintained in the connection pool. |
| Pooling | Enables or disables connection pooling. Set to `true` to reuse existing database connections and improve performance. |
| Connect\_Timeout | Sets the maximum duration (in seconds) the driver waits to establish a connection to the Db2 server before aborting and raising a timeout error. |
| QueryTimeout | Sets the default execution timeout (in seconds) for commands and queries sent over the connection before throwing an exception. |

<a id="SecurityCredentials"></a>

### Security / Credentials

| Connection Parameter | Description |
| --- | --- |
| PersistSecurityInfo | Determines whether sensitive security details (such as the database password) are preserved in the **ConnectionString`** object after the connection is established. Set to `false` to improve application security. |
| ConnStrPwdEncrypt | Encrypts the connection string password stored in process memory to protect against unauthorized memory dump inspections. |
| NewPWD | Specifies a new password during connection setup. Used to handle password expiration flows by changing the current user password upon connecting. |
| TrustedContextSystemUserID / TrustedContextSystemPassword | System user credentials used to establish an explicit Db2 trusted context. Allows a privileged application process to switch end-user identities on the same connection without requiring repeated authentication. |
| TrustedContextUserRegistryName | Identifies the security registry (such as LDAP or local OS) used to authenticate end-user identities when switching users within a trusted context session. |

<a id="SSLTLS"></a>

### SSL / TLS

Configure secure communication between Druid and IBM DB2 using SSL / TLS parameters.

> **IMPORTANT!** Always use a single certificate file (preferably the root issuing CA for certificate renewal resilience, or the leaf certificate as a fallback). Do not concatenate a full certificate chain into SSLServerCertificate. If you experience connection issues on SSL-only ports, verify that **Authentication** mode settings match server requirements.

| Connection Parameter | Description |
| --- | --- |
| Security | Set to SSL to enable TLS.  **NOTE:** This parameter is required for SSL/TLS connection. |
| SSLServerCertificate | Absolute path to server PEM cert (modern approach, no keystore needed).  **Example**   ``` Security=SSL;SSLServerCertificate=/path/db2cert/cert.pem ``` |
| SSLClientKeystoredb / SSLClientKeystash | Classic GSKit keystore deployment.  **Example**   ``` Security=SSL;SSLServerCertificate=C:/certs/clientkeystore.kdb ``` |
| SSLClientKeystoreDBPassword | Keystore password | Keystore password (required only when a .sth stash file is not present). |
| SSLClientLabel | Client certificate label (required for mutual TLS authentication). |
| TLSVersion | Specifies the explicit TLS protocol version (for example, TLSV12, TLSV13). |

#### Server Certificate Extraction

Follow these steps to extract and prepare the server certificate for connection configuration:

1. **Extract Certificate Text**. Copy a single -----BEGIN CERTIFICATE----- to -----END CERTIFICATE----- block.
> **NOTE:** Select the root or issuing CA (the final certificate in the chain) instead of the leaf certificate to prevent connection breaks during routine certificate renewals.

2. **Save File**. Save the copied content directly into a plain text file using a **.pem** extension (no format conversion is required as the source output is standard PEM/Base64 format).
3. **Validate Certificate**. Run the following command to verify certificate integrity:

**Bash**

```
openssl x509 -in db2-server-cert.pem -text -noout
```

#### OpenShift Container Deployment Notes

When deploying Druid on Red Hat OpenShift or Kubernetes, consider the following environmental constraints for certificate storage and permissions:

- **Mount Paths**. Deliver certificates and keystore files through a mounted Secret using an absolute file path (for example, /certs/db2-server-cert.pem). Relative paths are not supported.
- **File Permissions**. Configure file permissions using chgrp 0 and chmod g+rX (or specify defaultMode: 0440 in the Secret manifest) to ensure readability under OpenShift non-root user ID models (Group ID 0).
- **Configuration Strategy**. Prefer **SSLServerCertificate** (PEM file path) over standard **SSLClientKeystoredb / SSLClientKeystash** options to avoid container level keystore permission issues.
- **Base Image Runtime**. Verify that the underlying container base image uses glibc (such as RHEL or Ubuntu) rather than Alpine Linux (musl), as GSKit native libraries require glibc compatibility.

<a id="SchemaCatalog"></a>

### Schema / Catalog

| Connection Parameter | Description |
| --- | --- |
| CurrentSchema | Sets the default schema used to resolve unqualified database object names (such as tables or views) in queries. |
| CLISchema / SysSchema | Overrides the default system catalog schemas used by the driver for metadata queries and system table lookups. |
| DBName | Specifies an alternate database name or catalog alias to target during connection initialization. |
| TableType | Filters metadata retrieval calls to return only specified database object types (for example, TABLE, VIEW, or ALIAS). |
| SchemaList | A comma-separated list of schema names used to restrict metadata queries and object discovery to specific schemas. |

<a id="DataTypeMapping"></a>

### Data Type Mapping

| Connection Parameter | Description |
| --- | --- |
| MapDate / MapTime / MapTimestamp | Controls how Db2 date, time, and timestamp data types are mapped to native .NET data types (such as DateTime, TimeSpan, or String) during data retrieval. |
| Graphic | Specifies how Db2 graphic and double-byte character set (DBCS) data types (GRAPHIC, VARGRAPHIC) are converted and represented in the application. |
| ConvertToLong | Forces large text or binary data types (such as VARCHAR exceeding standard length limits) to be mapped and treated as LONG types. |
| FitHighPrecisionType | Controls the handling and rounding behavior of high-precision numeric values (such as DECIMAL or NUMERIC) to fit within application-supported numeric precision bounds without overflow. |
| RetrieveXmlInBinaryFormat | Determines whether XML column data is retrieved from the database server in binary XML format to improve performance and reduce network payload size. |

<a id="AuthenticationMode"></a>

### Authentication Mode

| Connection Parameter | Description |
| --- | --- |
| Authentication | Specifies the authentication mechanism used to validate credentials with the Db2 server (for example, SERVER, SERVER\_ENCRYPT, CLIENT, or KERBEROS). |
| Instance | Specifies the targeted Db2 server instance name, which is required by certain authentication modes to establish valid context. |

> **NOTE:** **Common SSL Connection Pitfall**: The standard plaintext port (e.g., 50000) and the dedicated SSL port (e.g., 50001) often use different server-side **AUTHENTICATION** settings. If authentication fails only after enabling SSL, verify the server configuration for the SSL listener using:
>
> ```
> db2 get dbm cfg | grep -i AUTHENTICATION
> ```
>
> Set the matching authentication parameter (typically **SERVER\_ENCRYPT**) in the DB2 connection configuration.

<a id="ClientIdentificationMonitoring"></a>

### Client Identification / Monitoring

| Connection Parameter | Description |
| --- | --- |
| ClientAccountingString | Custom accounting information passed to the Db2 server for tracking and workload monitoring (visible in system views such as SYSIBMADM.APPLICATIONS). |
| ClientApplicationName | Identifies the name of the calling application on the Db2 server (equivalent to ApplicationName used by other database providers). |
| ClientUserID | Specifies the end-user identity associated with the database connection, enabling individual user tracking when using connection pooling. |
| ClientWorkstationName | Specifies the hostname or client machine name displayed in Db2 server-side administrative tools and audit logs. |
| ClientCorrelationToken | A unique identifier used to trace and correlate client requests across distributed systems and application tiers. |

<a id="TracingDiagnostics"></a>

### Tracing / Diagnostics

| Connection Parameter | Description |
| --- | --- |
| traceFile / traceLevel | Configures file output paths and verbosity levels for IBM driver-level diagnostic tracing. |
| Db2dumpSQLCodes / Db2DumpSQLCodesInterval | Captures and dumps specific SQL error codes and diagnostic data to logs at specified time intervals. |
| DB2Explain | Enables execution plan capture (Explain facility) on the Db2 server to analyze query performance and optimization strategies. |

<a id="DynamicSQLQueryBehavior"></a>

### Dynamic SQL / Query Behavior

| Connection Parameter | Description |
| --- | --- |
| allowDynamicSQL | Controls whether dynamic SQL statements can be executed over the database connection. |
| enableDynamicSQLReplacement | Enables automatic replacement of SQL literals in dynamic SQL queries with parameter markers to promote statement caching and security. |
| sqlLiteralSubstitution | Configures literal value substitution behavior when utilizing the Db2 statement concentrator. |
| StatementConcentrator | Enables server-side statement concentration to modify dynamic SQL statements, allowing similar queries to share access plans in the package cache. |
| maxNonParmSQL | Sets the maximum number of non-parameterized dynamic SQL statements to retain in the local driver or package cache. |
| HostVarParameters | Defines how host variables and parameter markers (such as **?** or named parameters) are processed and bound during query execution. |
| DelimIdent | Controls support for delimited identifiers, allowing double quotes (") to enclose schema, table, or column names containing special characters or mixed case. |

<a id="MiscellaneousAdvanced"></a>

### Miscellaneous / Advanced

| Connection Parameter | Description |
| --- | --- |
| ConcurrentAccessResolution | Specifies the lock and isolation conflict resolution strategy (for example, instructing the server to use "Currently Committed" data to avoid lock waits on uncommitted updates). |
| IsolationLevel | Defines the default transaction isolation level for the database session (such as ReadCommitted, RepeatableRead, or Serializable). |
| ClientEncAlg | Specifies the encryption algorithm used to secure client-side data transmission and credential exchange. |
| CodePage | Sets the character encoding code page used for converting data sent between the application and the Db2 server. |
| WalletID / `WalletPwd | Specifies the identifier and password for an encrypted credential store (Oracle Wallet style; rarely used in Db2 environments). |
| LibraryList | Defines the library search order used for unqualified object resolution when connecting to Db2 for i (iSeries / AS400). |
| FetchBufferSize | Configures the network buffer size (in bytes) allocated for row prefetching to optimize query retrieval performance. |
| EnableEFCaseSensitivity | Toggles case-sensitivity handling for Entity Framework queries and mapping rules. |
| TargetPrincipal | Identifies the Kerberos target principal name of the Db2 service when using Kerberos authentication. |
| RetryParameterBindingOnError | Automatically retries statement parameter binding using fallback data types when data conversion errors occur during execution. |
| ConnectNodeNumber | Specifies the target database partition node number in a Db2 Data Partitioning Feature (DPF) environment. |
| CurrentPackageSet / CurrentSQLID | Configures the default schema collection (package set) or authorization ID used for dynamic SQL execution and package selection. |
| CurrentFunctionPath | Sets an ordered list of schema names used to resolve unqualified user-defined functions and stored procedures. |
| ProgramId / ProgramName | Identifies the client program name and application binary ID sent to the Db2 server for monitoring and governance. |
| SessionTimeZone | Sets the active time zone for the database session, ensuring consistent date and time calculations relative to the application layer. |

<a id="PostgreSQL"></a>

## <a id="PostgreSQL"></a>PostgreSQL

This section provides you with the list of additional connection parameters which PostgreSQL understands, as well as some standard PostgreSQL environment variables.

<a id="Securityandencryption"></a>

### Security and encryption

| Connection Parameter | Description |
| --- | --- |
| SSL Mode | Controls whether SSL is used, depending on server support. Can be Require, Disable, or Prefer. |
| Trust Server Certificate | Whether to trust the server certificate without validating it. |
| Client Certificate | Location of a client certificate to be sent to the server. |
| Client Certificate Key | Location of a client key for a client certificate to be sent to the server. |
| Root Certificate | Location of a CA certificate used to validate the server certificate. |
| Check Certificate Revocation | Whether to check the certificate revocation list during authentication. False by default. |
| Integrated Security | Whether to use integrated security to log in (GSS/SSPI), currently supported on Windows only. |
| Persist Security Info | Gets or sets a Boolean value that indicates if security-sensitive information, such as the password, is not returned as part of the connection if the connection is open or has ever been in an open state. |
| Include Error Detail | When enabled, PostgreSQL error and notice details are included on PostgresException.Detail and PostgresNotice.Detail. These can contain sensitive data. |

<a id="Pooling"></a>

### Pooling

| Connection Parameter | Description |
| --- | --- |
| Pooling | Whether connection pooling should be used. |
| Minimum Pool Size | The minimum connection pool size. |
| Maximum Pool Size | The maximum connection pool size. |
| Connection Idle Lifetime | The time (in seconds) to wait before closing idle connections in the pool if the count of all connections exceeds Minimum Pool Size. |
| Connection Pruning Interval | How many seconds the pool waits before attempting to prune idle connections that are beyond idle lifetime. |
| ConnectionLifetime | The total maximum lifetime of connections (in seconds). Connections that have exceeded this value will be destroyed instead of returned from the pool. This is useful in clustered configurations to force load balancing between a running server and a server just brought online. |

<a id="Timeoutsandkeepalive"></a>

### Timeouts and keepalive

| Connection Parameter | Description |
| --- | --- |
| Timeout | The time to wait (in seconds) while trying to establish a connection before terminating the attempt and generating an error. |
| Command Timeout | The time to wait (in seconds) while trying to execute a command before terminating the attempt and generating an error. Set to zero for infinity. |
| Internal Command Timeout | The time to wait (in seconds) while trying to execute an internal command before terminating the attempt and generating an error. -1 uses CommandTimeout, 0 means no timeout. |
| Cancellation Timeout | The time to wait (in milliseconds) while trying to read a response for a cancellation request for a timed out or cancelled query, before terminating the attempt and generating an error. -1 skips the wait, 0 means infinite wait. Added in 5.0. |
| Keepalive | The number of seconds of connection inactivity before Npgsql sends a keepalive query. |
| Tcp Keepalive | Whether to use TCP keepalive with system defaults if overrides is not specified. |
| Tcp Keepalive Time | The number of milliseconds of connection inactivity before a TCP keepalive query is sent. We recommend you to use KeepAlive instead (if possible). Supported only on Windows. |
| Tcp Keepalive Interval | The interval, in milliseconds, between when successive keep-alive packets are sent if no acknowledgement is received. Tcp KeepAlive Time must be non-zero as well. Supported only on Windows. |

<a id="Performance"></a>

### Performance

| Connection Parameter | Description |
| --- | --- |
| Max Auto Prepare | The maximum number SQL statements that can be automatically prepared at any given point. Beyond this number, the least-recently-used statement will be recycled. Zero disables automatic preparation. |
| Auto Prepare Min Usages | The minimum number of usages an SQL statement is used before it is automatically prepared. |
| Read Buffer Size | Determines the size of the internal buffer Npgsql uses when reading. Increasing may improve performance if transferring large values from the database. |
| Write Buffer Size | Determines the size of the internal buffer Npgsql uses when writing. Increasing may improve performance if transferring large values to the database. |
| Socket Receive Buffer Size | Determines the size of socket receive buffer. |
| Socket Send Buffer Size | Determines the size of socket send buffer. |
| No Reset On Close | Improves performance in some cases by not resetting the connection state when it is returned to the pool, at the cost of leaking state. Use only if benchmarking shows a performance improvement |

<a id="Failoverandloadbalancing"></a>

### Failover and load balancing

| Connection Parameter | Description |
| --- | --- |
| Target Session Attributes | Determines the preferred PostgreSQL target server type. |
| Load Balance Hosts | Enables balancing between multiple hosts by round-robin. |
| Host Recheck Seconds | Controls for how long the host's cached state will be considered as valid. |

<a id="Misc"></a>

### Misc

| Connection Parameter | Description |
| --- | --- |
| Options | Specifies any valid PostgreSQL connection options, surrounded by single ticks. |
| Application Name | The optional application name parameter to be sent to the backend during connection initiation. |
| Enlist | Whether to enlist in an ambient TransactionScope. |
| Search Path | Sets the schema search path. |
| Client Encoding | Gets or sets the client\_encoding parameter. |
| Timezone | Gets or sets the session timezone. |
| EF Template Database | The database template to specify when creating a database in Entity Framework. |
| Load Table Composites | Load table composite type definitions, and not just freestanding composite types. |

<a id="Compatibility"></a>

### Compatibility

| Connection Parameter | Description |
| --- | --- |
| Server Compatibility Mode | A compatibility mode for special PostgreSQL server types. Currently "Redshift" is supported, as well as "NoTypeLoading", which will bypass the normal type loading mechanism from the PostgreSQL catalog tables and supports a hardcoded list of basic types. |
| Convert Infinity DateTime | Makes MaxValue and MinValue timestamps and dates readable as infinity and negative infinity. |

<a id="Environmentvariables"></a>

### Environment variables

Npgsql also recognizes the standard PostgreSQL environment variables listed in the table below. This helps Npgsql-based applications behave similar to other, non-.NET PostgreSQL client applications.

| Environment variable | Description |
| --- | --- |
| PGSSLCERT | Specifies the file name of the client SSL certificate |
| PGSSLKEY | Specifies the location for the secret key used for the client certificate. This parameter is ignored if an SSL connection is not made. |
| PGSSLROOTCERT | Specifies the name of a file containing SSL certificate authority (CA) certificate(s). If the file exists, the server's certificate will be verified to be signed by one of these authorities. |
| PGCLIENTENCODING | Sets the client\_encoding configuration parameter for this connection. |
| PGTZ | Sets the default time zone. |
| PGOPTIONS | Specifies command-line options to send to the server at connection start. |

<a id="MySQL"></a>

## <a id="MySQL"></a>MySQL

| Connection Parameter | Description |
| --- | --- |
| ssl-mode | The desired security state for the connection. The following modes are permissible:   - DISABLED - PREFERRED - REQUIRED - VERIFY\_CA - VERIFY\_IDENTITY |
| ssl-ca | The path to the X.509 certificate authority file in PEM format. |
| ssl-capath | The path to the directory that contains the X.509 certificates authority files in PEM format. |
| ssl-cert | The path to the X.509 certificate file in PEM format. |
| ssl-cipher | The encryption cipher to use for connections that use TLS protocols up through TLSv1.2. |
| ssl-crl | The path to the file that contains certificate revocation lists in PEM format. |
| ssl-crlpath | The path to the directory that contains certificate revocation-list files in PEM format. |
| ssl-key | The path to the X.509 key file in PEM format. |
| tls-version | The TLS protocols permitted for classic MySQL protocol encrypted connections. This option is supported by MySQL Shell only. The value of tls-version (singular) is a comma separated list, for example `TLSv1.1,TLSv1.2`. This option depends on the ssl-mode option not being set to DISABLED. |
| tls-versions | The permissible TLS protocols for encrypted X Protocol connections. The value of `tls-versions` (plural) is an array such as [TLSv1.2,TLSv1.3]. This option depends on the `ssl-mode` option not being set to DISABLED. |
| tls-ciphersuites | The permitted TLS cipher suites. The value of `tls-ciphersuites` is a list of IANA cipher suite names as listed at TLS Ciphersuites.This option depends on the ssl-mode option not being set to DISABLED. |
| auth-method | The authentication method to use for the connection. The default is AUTO, meaning that the server attempts to guess. The following methods are permissible:   - AUTO - MYSQL41 - SHA256\_MEMORY - FROM\_CAPABILITIES - FALLBACK   PLAIN   For X Protocol connections, any configured `auth-method` is overridden to this sequence of authentication methods: `MYSQL41`, `SHA256_MEMORY`, `PLAIN`. |
| get-server-public-key | Request from the server the public key required for RSA key pair-based password exchange. Use when connecting to MySQL 8.0 servers over classic MySQL protocol with SSL mode DISABLED. You must specify the protocol in this case.  This option applies to clients that authenticate with the **caching\_sha2\_password** authentication plugin. For that plugin, the server does not send the public key unless requested. This option is ignored for accounts that do not authenticate with that plugin. It is also ignored if RSA-based password exchange is not used, as is the case when the client connects to the server using a secure connection. |
| server-public-key-path | The path name to a file in PEM format containing a client-side copy of the public key required by the server for RSA key pair-based password exchange. Use when connecting to MySQL 8.0 servers over classic MySQL protocol with SSL mode DISABLED. This option applies to clients that authenticate with the sha256\_password or **caching\_sha2\_password** authentication plugin. This option is ignored for accounts that do not authenticate with one of those plugins. It is also ignored if RSA-based password exchange is not used, as is the case when the client connects to the server using a secure connection. |
| connect-timeout | An integer value used to configure the number of seconds that clients, such as MySQL Shell, wait until they stop trying to connect to an unresponsive MySQL server. |
| compression | This option requests or disables compression for the connection. Up to MySQL 8.0.19 it operates for classic MySQL protocol connections only, and from MySQL 8.0.20 it also operates for X Protocol connections.  Up to MySQL 8.0.19, the values for this option are true (or 1) which enables compression, and the default false (or 0) which disables compression.  From MySQL 8.0.20, the values for this option are required, which requests compression and fails if the server does not support it; `preferred`, which requests compression and falls back to an uncompressed connection; and `disabled`, which requests an uncompressed connection and fails if the server does not permit those. preferred is the default for X Protocol connections, and disabled is the default for classic MySQL protocol connections. |
| compression-algorithms and compression-level | These options are available in MySQL Shell 8.0.20 and later for more control over connection compression. You can specify them to select the compression algorithm used for the connection, and the numeric compression level used with that algorithm. You can also use compression-algorithms in place of compression to request compression for the connection. |
| connection-attributes | Controls the key-value pairs that application programs pass to the server at connect time. |

<a id="OracleSQL"></a>

## <a id="OracleSQL"></a>OracleSQL

| Connection Parameter | Description |
| --- | --- |
| Connection Lifetime | Minimum life time (in seconds) of the connection. |
| Connection Timeout | Minimum time (in seconds) to wait for a free connection from the pool. |
| Context Connection | Returns an implicit database connection if set to true. |
| DBA Privilege | Administrative privileges: `SYSDBA` or `SYSOPER`. |
| Decr Pool Size | Number of connections that are closed when an excessive amount of established connections are unused. |
| Enlist | Controls the enlistment behavior and capabilities of a connection in context of COM+ transactions or `System.Transactions`. |
| HA Events | Enables ODP.NET connection pool to proactively remove connections from the pool when an Oracle database service, service member, instance, or node goes down. Works with Oracle Global Data Services, including Oracle RAC, Data Guard, GoldenGate, and some single instance deployments. |
| Load Balancing | Enables ODP.NET connection pool to balance work requests across Oracle database instances based on the load balancing advisory and service goal. Works with Oracle Global Data Services, including Oracle RAC, Active Data Guard, and GoldenGate. |
| Incr Pool Size | Number of new connections to be created when all connections in the pool are in use. |
| Max Pool Size | Maximum number of connections in a pool. |
| Metadata Pooling | Caches metadata information. |
| Min Pool Size | Minimum number of connections in a pool. |
| Persist Security Info | Retrieval of the password in the connection string. |
| Pooling | Connection pooling. |
| Promotable Transaction | Indicates whether or not a transaction is local or distributed throughout its lifetime. |
| Proxy User Id | User name of the proxy user. |
| Proxy Password | Password of the proxy user. |
| Self Tuning | Enables or disables self-tuning for a connection. |
| Statement Cache Purge | Statement cache purged when the connection goes back to the pool. |
| Statement Cache Size | Statement cache enabled and cache size, that is, the maximum number of statements that can be cached. |
| Validate Connection | Validation of connections coming from the pool. |
