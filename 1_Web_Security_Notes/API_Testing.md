# API Testing Notes:

## API Basics

**API Types**:
- REST: Uses HTTP, usually JSON for data exchange.
- SOAP: XML-based protocol, more rigid.
- GraphQL: Query language for APIs, more flexible but prone to complex attacks.
- WebSockets: Full-duplex communication channels over a single TCP connection.

**Common HTTP Methods**:
- GET: Retrieve data (shouldn't change the state).
- POST: Send data to the server (creates new resources).
- PUT: Update an existing resource.
- DELETE: Remove a resource.

**Key Headers to Pay Attention To**:
- Authorization: Tokens, API keys, etc.
- Content-Type: Defines the type of data being sent (e.g., ```application/json```).
- Accept: What the client expects in response (e.g., ```application/json```).

## Authentication & Authorization Vulnerabilities
**Broken Authentication**:
- Common Mistakes: Missing rate limiting, poor session management, exposing sensitive tokens.
- Testing:
    - Check if login is brute-forceable.
    - Look for session fixation issues.
    - Test for token reuse or weak session expiration mechanisms.

**Broken Object Level Authorization (BOLA)**:

- Description: Unauthorized users can access other users’ data by manipulating object identifiers (e.g., ```user_id``` in URL).
- Testing:
    - Modify resource IDs in requests (IDOR testing).
    - Verify if the API checks authorization properly for each request.

## Injection Attacks
**SQL Injection in APIs**:
- Test for blind SQLi: Send payloads via API parameters and observe responses.
- Look for JSON inputs: If API accepts JSON, check if it filters inputs properly or allows injection.

**Command Injection**:
- Testing: Find endpoints that directly execute system commands.
    - Common in APIs handling file uploads or system interaction.
    - Inject OS commands like ```; ls```, ```&& whoami```.

**NoSQL Injection**:
- Common in MongoDB-based APIs:
```{ "$gt": "" }``` or ```{ "$ne": 1 }``` can sometimes bypass queries.

## Lack of Rate Limiting
 - Impact: Allows brute-force attacks, DoS, data scraping.
- Testing:
    - Try repeated requests for login or sensitive endpoints. 
    - If the API doesn’t block or slow down after many requests, it’s vulnerable.
    - Look for ```429 Too Many Requests``` responses (good practice).

## Insecure Data Exposure
- Types:
    - Leaking sensitive data like API keys, tokens, PII.
    - Over-sharing in API responses (e.g., too much user data in a ```GET /users``` response).
- Testing:
    - Inspect response bodies for excessive or sensitive data.
    - Watch out for ```email```, ```password_hash```, ```SSN```, etc., in responses.
- Examples:
    - API returns user info, but includes internal fields like ```user_role``` or ```admin_flag```.
    
## Security Misconfigurations
**CORS Issues**:
- Problem: Misconfigured CORS policy allows cross-origin requests from untrusted sources.
- Testing:
    - Check for ```Access-Control-Allow-Origin: *``` in the API response.
    - Try sending requests from unauthorized origins and see if they're accepted.

## Cross-Site Scripting (XSS) in APIs
- Reflected: APIs may return unfiltered user inputs in the response.
- Testing:
    - Inject basic XSS payloads (e.g., ```<script>alert(1)</script>```) into inputs like query params or JSON bodies.
    - Look for places where user input is reflected directly into HTML or JavaScript.

## Business Logic Vulnerabilities
- Description: Exploit flaws in API’s business processes (e.g., bypassing payment system, ordering negative quantities).
- Testing:
    - Try to perform actions that should be restricted (e.g., changing prices, buying more items than in stock).
    - Manipulate request data and observe how the API processes unexpected or nonsensical values.

## API Testing with Burp Suite
**Setup**:
- Use Proxy to intercept API requests.
- Send intercepted requests to Repeater for manual testing.
- JSON/REST: Can edit and resend JSON data easily through Burp.

**Tips**:
- Use Intruder to brute-force parameters or test rate limiting.
- Check Burp's Scanner for automated vulnerability detection in APIs.

**Common APIs in Burp**:
- Content-Type: ```application/json``` for modern APIs.
- Authorization: JWTs often used; manually modify tokens to check for bypasses.

## API Security Best Practices (Testing Checklist)
1. Authentication:

    - Enforce strong authentication (OAuth2, token expiration).
    - No sensitive tokens in URLs or GET requests.

2. Authorization:

    - Test for BOLA (broken object level authorization).
    - Check role-based access control (RBAC) consistently.

3. Input Validation:

    - Strict validation of user inputs (JSON, XML, etc.).
    - Use parameterized queries to prevent SQL/NoSQL injection.
4. Rate Limiting:

    - Ensure APIs implement rate limiting and throttling for sensitive endpoints.

5. Sensitive Data Exposure:

    - Avoid returning sensitive information in responses (no debug info or stack traces).
    - Always encrypt sensitive data in transit and at rest.
6. Error Handling:

    - Don’t expose internal error messages or sensitive data in API error responses.

## Final Notes
- Focus on business logic: Think creatively about how users could misuse or exploit API functions.
- APIs are everywhere: They often have weaker security compared to web interfaces, making them prime targets for attackers.