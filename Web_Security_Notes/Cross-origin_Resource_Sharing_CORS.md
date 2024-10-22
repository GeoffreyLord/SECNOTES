# CORS (Cross-Origin Resource Sharing) Notes:
## Overview
Cross-Origin Resource Sharing (CORS) is a security feature implemented by browsers to prevent web pages from making requests to a different domain than the one that served the web page. It controls how resources on a web page are shared across different origins.

An origin is defined as a combination of:

- Scheme: Protocol (e.g., ```http```, ```https```).
- Host: Domain (e.g., ```example.com```).
- Port: Port number (e.g., ```80```, ```443```).

Without proper CORS configuration, APIs and web pages can be vulnerable to attacks like Cross-Site Request Forgery (CSRF) or data theft.

## CORS Basics
Same-Origin Policy (SOP):

- By default, web browsers block requests between different origins (e.g., ```https://example.com``` cannot fetch resources from ```https://other.com```).
- CORS provides a controlled way to relax the SOP by allowing a server to specify which origins can access its resources.

## CORS Headers
**Key CORS Response Headers:**
1. Access-Control-Allow-Origin:

    - Specifies which origins are allowed to access the resource.
    - Can be a specific domain (```https://example.com```) or a wildcard (```*``` for any domain).
    - Risk: Using ```*``` allows any domain to access resources, which is insecure if sensitive data is involved.
2. Access-Control-Allow-Credentials:

    - Indicates whether credentials (cookies, HTTP authentication, client-side certificates) are allowed in cross-origin requests.
    - Setting: ```true``` to allow credentials; ```false``` or omit to block them.
    - Risk: If Access-Control-Allow-Origin is set to ```*``` and ```Access-Control-Allow-Credentials``` is ```true```, this can expose sensitive data to any origin.

3. Access-Control-Allow-Methods:

    - Specifies which HTTP methods are allowed for cross-origin requests (e.g., ```GET```, ```POST```, ```PUT```, ```DELETE```).

4. Access-Control-Allow-Headers:

    - Defines which headers can be used in the actual request (e.g., ```Content-Type```, ```Authorization```, ```X-Custom-Header```).

5. Access-Control-Expose-Headers:

    - Indicates which response headers can be accessed by the browser (e.g., custom headers).
6. Access-Control-Max-Age:

    - Specifies how long the results of a preflight request can be cached.

**Key Request Headers**:
1. Origin:

    - Automatically included by the browser in cross-origin requests.
    - Identifies the domain making the request.
2. Access-Control-Request-Method:

    - Sent in a preflight request to indicate the HTTP method that will be used in the actual request.
3. Access-Control-Request-Headers:

    - Sent in a preflight request to indicate which headers will be used in the actual request.

## Preflight Requests
**What is a Preflight Request?**
- Preflight requests are CORS requests made with the ```OPTIONS``` method to check whether the server will allow the actual request.
- This happens automatically when:
    - The request uses methods other than ```GET``` or ```POST```.
    - Custom headers are included (e.g., ```Authorization```, ```Content-Type: application/json```).
    - Credentials like cookies or authentication tokens are included.
**How Preflight Works**:
1. Browser sends a preflight request (```OPTIONS```) with the necessary headers to the server.
2. Server responds with the appropriate CORS headers, specifying which methods, headers, and origins are allowed.
3. Browser decides whether the actual request can proceed based on the server's response.

## Common CORS Vulnerabilities
1. Misconfigured Wildcard Origin (```Access-Control-Allow-Origin: *```)
    - Risk: Allowing all origins to access the resource.
    - Impact: Sensitive data could be exposed to any third-party site.
    - Testing:
        - Inspect the response headers for ```Access-Control-Allow-Origin: *```.
        - Try making a cross-origin request from a different domain and see if the response contains sensitive data.
2. Insecure Use of ```Access-Control-Allow-Credentials```
    - Risk: Allowing credentials (cookies, authentication tokens) to be shared across origins while using a wildcard (```*```) for ```Access-Control-Allow-Origin```.
    - Impact: Attacker-controlled websites can make authenticated requests on behalf of the user.
    - Testing:
        - Check if ```Access-Control-Allow-Credentials: true``` and ```Access-Control-Allow-Origin: *``` are used together. This is a serious misconfiguration.
        - Attempt to make requests that require credentials and see if they are successful from an untrusted origin.
3. Overly Permissive Methods and Headers
    - Risk: Allowing dangerous HTTP methods like ```PUT```, ```DELETE```, or sensitive headers like ```Authorization``` without proper validation.
    - Impact: Attackers could perform actions like modifying or deleting data.
    - Testing:
        - Inspect the ```Access-Control-Allow-Methods``` and ```Access-Control-Allow-Headers``` headers.
        - Check if sensitive methods or headers are allowed unnecessarily.
4. Reflection of Arbitrary Origin
    - Risk: Server reflects the origin from the request's ```Origin``` header without proper validation.
    - Impact: Any untrusted origin can make requests to the API.
    - Testing:
        - Send requests with different ```Origin``` headers (e.g., ```http://evil.com```) and check if the server reflects them in ```Access-Control-Allow-Origin```.
        - The server should only reflect trusted origins, or better, specify them explicitly.

## CORS Exploitation Techniques
**Exploiting Misconfigured ```Access-Control-Allow-Origin```**
- If the ```Access-Control-Allow-Origin``` header is set to ```*```, or reflects any origin, try making a request from an attacker-controlled domain to steal sensitive information.

**Exploiting ```Access-Control-Allow-Credentials```**
- If ```Access-Control-Allow-Credentials: true``` is present along with a wildcard origin or reflected origin, perform a Cross-Site Request Forgery (CSRF) attack to make authenticated requests on behalf of the victim.

**Preflight Request Tampering**
- Manipulate ```OPTIONS``` requests (preflight requests) to bypass restrictions on methods or headers, especially if the server has lax validation for preflight responses.

## Testing CORS Configurations
**Checklist for Testing CORS**:
1. Inspect Response Headers:

    - Ensure ```Access-Control-Allow-Origin``` is correctly configured (no wildcards for sensitive data).
    - Verify if ```Access-Control-Allow-Credentials``` is set only when necessary and doesn’t allow dangerous combinations like ```*``` origin with credentials.

2. Simulate Cross-Origin Requests:

    - Use tools like cURL, Postman, or Burp Suite to simulate cross-origin requests and inspect the server's response.
    - Make requests from different domains and see if the server allows them.

3. Check Preflight Responses:

    - Verify that preflight requests respond with appropriate headers and don’t allow dangerous methods (e.g., ```PUT```, ```DELETE```).
    - Test caching of preflight results using the ```Access-Control-Max-Age``` header.

4. Origin Reflection:

    - Test if the server reflects the ```Origin``` header dynamically. A secure server should only allow trusted origins or a specific list of domains.

## CORS Best Practices
1. Set Specific Origins:

    - Use explicit origins for ```Access-Control-Allow-Origin``` (e.g., ```https://trusted.com```) instead of using the wildcard (```*```).
2. Control Credential Sharing:

    - Only use ```Access-Control-Allow-Credentials: true``` when necessary, and never with the wildcard origin (```*```).
3. Restrict Methods and Headers:

    - Limit ```Access-Control-Allow-Methods``` to only the methods the API actually needs (e.g., ```GET```, ```POST```).
    - Restrict ```Access-Control-Allow-Headers``` to only necessary headers like ```Content-Type```.

4. Use Content-Security-Policy (CSP):

    - Implement CSP along with CORS for additional protection, preventing unauthorized cross-origin interactions.
5. Preflight Validation:

    - Ensure proper validation of preflight requests and only allow necessary methods, headers, and origins.

## Final Notes
- CORS configuration: Must be handled carefully, especially when sensitive data or credentials are involved.
- Common mistakes: Using wildcards (```*```) in ```Access-Control-Allow-Origin``` or combining it with ```Access-Control-Allow-Credentials: true```.
- Testing focus: Look for overly permissive headers and the possibility of credential leakage across origins.