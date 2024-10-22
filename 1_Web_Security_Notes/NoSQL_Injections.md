# NoSQL Injection Vulnerabilities Notes
## Overview
NoSQL Injection occurs when attackers exploit unvalidated input in NoSQL databases (e.g., MongoDB, CouchDB, Elasticsearch) to manipulate queries. NoSQL databases are often document-based and use flexible query structures like JSON, but their flexibility can lead to injection vulnerabilities if user input is not properly handled.

## Common NoSQL Injection Techniques
1. Direct Query Manipulation
    - Description: NoSQL queries are often constructed with JSON-like syntax. If input is not sanitized, attackers can inject additional query logic.
    - Example (MongoDB):
        - ```{"username": "admin", "password": {"$ne": null}}```
        - This bypasses the password check by using the $ne operator to accept any password.
    - Risk: Attackers can bypass authentication or query unauthorized data.
2. Operator Injection
    - Description: NoSQL databases use specific operators (e.g., ```$ne```, ```$gt```, ```$lt```). Attackers can inject these operators into fields if input validation is absent.
    - Example:
        - Injecting ```{ "$gt": "" }``` into numeric fields to bypass restrictions or gain access to unauthorized records.
    - Risk: Can lead to unauthorized data access or circumvention of input constraints.
3. Array Injection
    - Description: NoSQL databases, like MongoDB, allow arrays in queries. Attackers can exploit this feature to manipulate query logic.
    - Example (MongoDB):
        - ```{"username": ["admin", "guest"], "password": {"$ne": null}}```
        - This query checks both "admin" and "guest" users, potentially expanding the attack surface.
    - Risk: Enables attackers to manipulate how the query operates on multiple documents.

## Testing for NoSQL Injections
1. Basic Input Testing
    - Try injecting NoSQL operators (e.g., ```$ne```, ```$gt```, ```$lt```) into input fields to manipulate queries.
    - Example Payload:
        - Test login forms: ```{"username": "admin", "password": {"$ne": null}}```
        - Expected result: Authentication bypass if the injection is successful.
2. Bypass Authentication
    - Technique: Inject NoSQL logic into fields to bypass authentication.
    - Example:
        - For a login form that checks both username and password, inject a query like:
            - ```{"username": "admin", "password": {"$gt": ""}}```
        - If successful, this will bypass the password check.
3. Boolean-Based Blind NoSQL Injection
    - Technique: Infer database behavior through injected queries and response variations.
    - Testing:
        - Send queries like:
            - ```{"username": "admin", "password": {"$regex": "^a"}}```
        - Observe changes in response times or behavior to infer if the query was successful.
## Defenses Against NoSQL Injection
1. Input Validation and Sanitization
    - Description: Properly validate and sanitize all user inputs, ensuring only expected values are accepted.
    - Best Practices:
        - Use strict type checking and avoid allowing special characters like ```$``` in inputs unless necessary.
2. Use Parameterized Queries
    - Description: Similar to SQL, use parameterized queries to avoid dynamically building NoSQL queries with user inputs.
    - Example (MongoDB):
        - Avoid:
            - ```db.users.find({username: userInput, password: passInput})```
        - Use parameterized queries or predefined query structures.
3. Limit Query Operators
    - Description: Restrict the use of operators like ```$gt```, ```$ne```, or ```$regex``` in fields that are user-controlled.
    - Best Practices:
        - Disallow the use of special operators in user-controlled input fields unless explicitly required.
4. Access Control
    - Description: Ensure that users only have access to the data and operations that they are authorized to perform.
    - Best Practices:
        - Use role-based access control (RBAC) to limit what data users can query or modify.
## Testing Checklist for NoSQL Injection
- Test Input Fields: Attempt to inject NoSQL operators (```$ne```, ```$gt```, etc.) and observe the behavior.
- Bypass Authentication: Inject queries that manipulate login logic (e.g., ```{"$ne": null}```) and check if unauthorized access is possible.
 - Blind Injection: Use boolean-based injection techniques to infer data by observing application behavior or response timing.
 - Check Error Handling: Look for error messages that may expose query structure or database details.

## Final Notes
- NoSQL Injections: Are less structured than traditional SQL injections but can still lead to severe impacts like data exposure or authentication bypass.
- Mitigation: Input validation, query parameterization, and restricted use of special operators are key defenses.
- Testing focus: Ensure all user input is sanitized and protected from malicious NoSQL injection attempts.
