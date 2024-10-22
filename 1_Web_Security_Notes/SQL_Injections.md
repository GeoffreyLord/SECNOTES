# SQL Injection Vulnerabilities Notes:
## Overview
SQL Injection (SQLi) is a vulnerability that occurs when an attacker is able to inject malicious SQL queries into a web application’s database. This happens due to improper input validation and unsanitized data, allowing attackers to manipulate queries and perform unauthorized actions, such as data retrieval, data manipulation, administrative actions, and, in some cases, remote code execution. SQLi remains one of the most dangerous and common vulnerabilities in web applications.

## How SQL Injection Works

**Basic SQL Query Structure**

- A typical SQL query might look like:
    - ```SELECT * FROM users WHERE username = 'user' AND password = 'pass';```
- If an application directly inserts user input into this query, an attacker could manipulate the input to alter the query's behavior.

**Example of an SQL Injection**

- An attacker provides the following as the username:

    - ```' OR '1'='1```
    - This changes the query to:
    - ```SELECT * FROM users WHERE username = '' OR '1'='1' AND password = 'pass';```
- This query will always evaluate to true (```'1'='1'```), allowing the attacker to bypass authentication.

## Types of SQL Injection
1. Classic SQL Injection (In-Band SQLi)
    - Description: The attacker directly manipulates the SQL query via the application's input fields and retrieves data in the response.
    - Example:
        - ```' OR 1=1--```
        - This will cause the query to return all rows from the table.
    - Impact: Can lead to full database access or modification.
2. Union-Based SQL Injection
    - Description: The attacker uses the UNION SQL operator to combine results from multiple queries.
    - Example:
        - ```' UNION SELECT username, password FROM admin--```
        - This merges the results of the initial query with the results from a sensitive table (e.g., the admin table).
    - Impact: Exposes additional data from different tables in the database.
3. Boolean-Based Blind SQL Injection
    - Description: The attacker cannot see query results directly but uses true/false conditions to infer the database structure.
    - Example:
        - ```' AND 1=1--```
        - ```' AND 1=2--```
        - The attacker can test these conditions by observing changes in the application’s behavior (e.g., error messages, response delays).
    - Impact: Can slowly reveal data even without direct query output.
4. Time-Based Blind SQL Injection
    - Description: The attacker uses SQL commands that cause time delays to infer the response based on query execution time.
    - Example:
        - ```' OR IF(1=1, SLEEP(5), 0)--```
        - This query will pause the database for 5 seconds if the condition (```1=1```) is true.
    - Impact: Allows attackers to extract information by causing noticeable delays in responses.
5. Error-Based SQL Injection
    - Description: The attacker causes the application to return detailed database error messages that expose the query structure.
    - Example:
        - ```' OR 1=CONVERT(int, 'abc')--```
        - The error message returned may provide useful information about the database schema and query structure.
    - Impact: Provides detailed information for crafting more sophisticated attacks.
6. Second-Order SQL Injection
    - Description: The attacker injects malicious SQL that is stored in the database and later executed during a different database query.
    - Example: An attacker stores a malicious string in a user profile field. When another function queries that field (e.g., for an admin action), the SQL injection is triggered.
    - Impact: Can lead to unexpected SQL injections in unrelated parts of the application.

## Common Vulnerable Points for SQL Injection
1. Login Forms: Attackers often target authentication mechanisms by manipulating username and password fields.
2. Search Fields: Input fields used for querying data may not sanitize user input properly.
3. URL Parameters: Query parameters in URLs that pass user data to the database can be manipulated.
4. Cookies: If user cookies are not properly validated before being used in a query, they can be manipulated to inject SQL.
5. HTTP Headers: Some applications may take user-agent strings, referrers, or other headers and use them in SQL queries.

## SQL Injection Exploitation Techniques
1. Exploiting UNION-Based SQL Injection
    - Technique: Use the ```UNION``` operator to combine query results and extract data from different tables.
    - Testing:
        - Inject ```UNION SELECT NULL``` and increment the number of columns to match the query structure.
        - Once the number of columns is identified, inject ```UNION SELECT``` with actual data extraction queries (e.g., ```SELECT username, password```).
2. Database Fingerprinting
    - Technique: Use SQL injection to identify the underlying database management system (DBMS).
    - Testing:
        - Inject specific queries that behave differently in different databases (e.g., ```SELECT @@version``` for MySQL or ```SELECT version()``` for PostgreSQL).
        - Use the DBMS response to craft more targeted injection attacks.
3. Database Schema Enumeration
    - Technique: Extract the database schema, including table names and column structures.
    - Testing:
        - For MySQL:
            - ```' UNION SELECT table_name FROM information_schema.tables WHERE table_schema=database()--```
        - For PostgreSQL:
            - ```' UNION SELECT table_name FROM information_schema.tables WHERE table_catalog=current_database()--```
        - Extract table names and then enumerate columns using:
            - ```' UNION SELECT column_name FROM information_schema.columns WHERE table_name='users'--```
4. Extracting Data via Blind SQL Injection
    - Technique: Use boolean-based or time-based techniques to slowly extract sensitive data.
    - Testing:
        - Send boolean-based payloads (e.g., ```' AND SUBSTRING(username, 1, 1) = 'a'--```) and infer the response based on the application's behavior.
        - Use time-based queries to extract data without seeing the direct output (e.g., ```' OR IF(SUBSTRING(username,1,1)='a', SLEEP(5), 0)--```).
5. Bypassing Authentication
    - Technique: Inject SQL queries to bypass login forms and access restricted areas.
    - Testing:
        - Inject ```' OR '1'='1``` in the username or password field to bypass authentication checks.
        - Test different parts of the login form to see if any allow SQL injection (e.g., username, password, remember me tokens).

## Defense Mechanisms Against SQL Injection
1. Parameterized Queries (Prepared Statements)
    - Description: Parameterized queries separate SQL code from user input, preventing attackers from injecting code.
    - Best Practices:
        - Use parameterized queries in all database interactions.
        - Avoid dynamic query building with user input directly inserted into SQL strings.
    - Example (in Python with MySQL):
        - ```cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (user, password))```
2. Stored Procedures
    - Description: Stored procedures are pre-defined SQL queries that run on the database server, reducing the risk of SQL injection if written correctly.
    - Best Practices:
        - Use stored procedures for database interactions, ensuring they do not build dynamic SQL from untrusted input.
    - Caution: Stored procedures can still be vulnerable if dynamic SQL is used inside the procedure.
3. Input Validation and Sanitization
    - Description: Validate and sanitize user input before using it in queries.
    - Best Practices:
        - Ensure all input is of the expected type (e.g., integers for numeric fields).
        - Use whitelisting to only allow acceptable characters (e.g., disallow special characters like ';).
        - Reject any input that doesn’t conform to validation rules.
4. Escaping Input
    - Description: Properly escape special characters (e.g., quotes) in SQL queries to prevent them from being treated as part of the query.
    - Best Practices:
        - Use built-in database escaping functions to safely handle user input.
        - Avoid building SQL queries manually where possible.
5. Least Privilege Principle
    - Description: Limit database user permissions to only what is necessary for the application to function.
    - Best Practices:
        - Ensure that application database users have minimal permissions (e.g., no permission to modify or drop tables unless required).
        - Segregate access for different application modules or users.
6. Error Handling and Logging
    - Description: Do not expose detailed error messages to users, as they may contain information about the database schema or query structure.
    - Best Practices:
        - Use generic error messages (e.g., "An error occurred") while logging detailed errors on the server side.
        - Avoid displaying SQL errors directly to the user.
7. Web Application Firewalls (WAFs)
    - Description: A WAF can help detect and block SQL injection attempts by monitoring and filtering malicious requests.
    - Best Practices:
        - Use a WAF with built-in rules to detect common SQL injection patterns.
        - Regularly update the WAF rule set to address new attack vectors.

## Testing for SQL Injection
1. Manual Testing
    - Inject Simple Payloads:

        - Try common SQLi payloads like ```' OR 1=1--``` into input fields (e.g., login forms, search bars).
        - Check if the application returns unexpected behavior or data.

    - Use Union Injection:

        - Test the number of columns with ```UNION SELECT NULL```.
        - Attempt to extract data by using ```UNION SELECT``` with known column numbers.
2. Automated Testing Tools
    - SQLMap:

        - A powerful tool for automating the discovery and exploitation of SQL injection vulnerabilities.
        - Run SQLMap on known endpoints to test for vulnerabilities:
            - ```sqlmap -u "http://example.com?id=1" --dbs```
        - Use SQLMap to enumerate databases, tables, and columns and extract data.
    - Burp Suite:

        - Use Burp Suite to intercept and manipulate requests.
        - Inject SQL payloads into various parameters and observe server responses.
3. Error-Based Testing
    - Generate SQL Errors:
         -Try injecting payloads that generate SQL errors to reveal details about the query or database (e.g., ```' OR 1=CONVERT(int, 'abc')--```).
    - Look for detailed error messages that expose table or column names.
4. Blind SQL Injection Testing
    - Boolean-Based Testing:
        - Inject payloads like ```' AND 1=1--``` and ```' AND 1=2--``` to infer success or failure based on response differences.
    - Time-Based Testing:
        - Use time-based payloads to check for response delays (e.g., ```' OR IF(1=1, SLEEP(5), 0)--```).

        - Measure the response time to infer query execution.
## SQL Injection Best Practices (Defense Checklist)
1. Use Parameterized Queries:

    - Always use prepared statements to separate SQL logic from user input.
2. Employ Stored Procedures:

    - Use stored procedures that do not rely on dynamic SQL.
3. Input Validation:

    - Validate user input for type, format, and range. Use whitelisting.
4. Escape Inputs:

    - Properly escape inputs before inserting them into queries if using dynamic SQL (as a fallback to parameterized queries).
5. Implement Least Privilege:

    - Restrict database access for application users to the minimum necessary permissions.
6. Hide Error Messages:

    - Don’t expose detailed database error messages to end users.
7. Monitor with WAFs:

    - Use Web Application Firewalls to detect and block SQLi attempts.

## Final Notes
- SQL Injection: One of the most dangerous vulnerabilities, often leading to full database compromise or remote code execution.
- Prevention: Parameterized queries and input validation are the most effective defenses.
- Testing: Manual testing, combined with automated tools like SQLMap, is critical for detecting SQLi vulnerabilities.