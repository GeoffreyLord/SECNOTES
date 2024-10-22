# Cross-Site Request Forgery (CSRF) Notes:

## Overview

Cross-Site Request Forgery (CSRF) is an attack where an attacker tricks a user into executing unwanted actions on a web application in which they are authenticated. The attacker forges a request on behalf of the victim by embedding the malicious request in a webpage, often through links or forms. If the victim is authenticated, the web server processes the request as if it came from the user.

## CSRF Attack Basics
**How CSRF Works**:
1. User is authenticated: The victim is logged into a web application and has an active session (e.g., cookies or tokens are stored).
2. Attacker forges a request: The attacker embeds a malicious request in a third-party site (via link, form, image, etc.).
3. Victim triggers the request: When the victim visits the attacker's site or clicks the link, the malicious request is sent to the legitimate site where the victim is authenticated.
4. Server processes the request: Since the request includes the victim's credentials (e.g., session cookies), the web server executes the action as though it was performed by the user.

## Key Elements in a CSRF Attack
1. Authenticated Session:

    - The attack works only if the victim has an active session with the target web application.
    - Most commonly relies on session cookies that browsers automatically send with requests.
2. Forged Request:

    - Can be ```GET``` or ```POST``` requests, often containing parameters to perform actions like transferring funds, changing passwords, or modifying user settings.
3. Browser’s Role:

    - Browsers automatically include cookies with requests to the same domain, making CSRF possible when cookies are used for session management.


## CSRF Attack Vectors
1. GET-Based CSRF
    - Description: The attacker tricks the victim into making a GET request with parameters that result in actions on the target application.
    - Example:
        - ```<img src="http://vulnerable.com/transfer?amount=1000&to=attacker_account">```
    - Risk: Any sensitive action triggered by GET requests is vulnerable.
2. POST-Based CSRF
    - Description: The attacker uses an HTML form or JavaScript to send a forged POST request.
    - Example:
            
        - ```<form action="http://vulnerable.com/change_email" method="POST"><input type="hidden" name="email" value="attacker@example.com"></form><script>document.forms[0].submit();</script>```
    - Risk: Sensitive state-changing operations (e.g., password changes, funds transfers) performed via POST requests can be exploited.
3. Image Tag CSRF
    - Description: An attacker places an image tag that triggers a GET request to the target application.
    - Example:
        - ```<img src="http://vulnerable.com/vote?candidate=attacker">```
    - Risk: Even though the request is embedded in an image, it can still trigger actions.
4. CSRF via JavaScript
    - Description: If the application allows cross-origin requests, JavaScript can be used to send requests.
    - Risk: JavaScript on an attacker-controlled page could exploit CORS misconfigurations to perform unauthorized actions.

## Common CSRF Vulnerabilities
1. Lack of Anti-CSRF Tokens:

    - Risk: Web applications that do not use anti-CSRF tokens are vulnerable because they cannot differentiate between legitimate and forged requests.
    - Testing:
        - Look for forms or sensitive actions that do not include a unique, unpredictable token tied to the user’s session.
        - Try submitting requests without tokens or with predictable tokens.

2. Cookies Used for Session Management:

    - Risk: CSRF attacks exploit browsers automatically including cookies with cross-site requests.
    - Testing:
        - Inspect cookies for session management and see if they are automatically included with all requests.
 
3. ```GET``` Requests Used for State-Changing Actions:

    - Risk: ```GET``` requests should not be used for actions that modify data (e.g., changing settings or transferring funds).
    - Testing:
        - Check if sensitive actions (e.g., account modifications) are performed using ```GET``` requests.

## Defense Mechanisms
1. Anti-CSRF Tokens (Synchronizer Tokens)
    - Description: A unique, unpredictable token generated on the server and sent to the client. The token is included in forms or AJAX requests, and the server verifies the token before processing the request.
    - How it works:
        - The token is tied to the user’s session.
        - For every sensitive action, the token must be included in the request (usually as a hidden form field or in headers).
    - Testing:
        - Look for the presence of CSRF tokens in requests.
        - Check if tokens are truly unpredictable and unique for each session.
        - Attempt to perform the action without a valid CSRF token to verify if it is enforced.
2. SameSite Cookie Attribute
    - Description: A cookie attribute that restricts when cookies are sent in cross-origin requests.
    - Values:
        - ```SameSite=Strict```: Cookies are not sent with cross-site requests.
        - ```SameSite=Lax```: Cookies are only sent with top-level navigation and ```GET``` requests (safe by default, but can allow some CSRF).
        - ```SameSite=None```: Cookies are sent with all requests (least secure, but necessary for cross-origin access).
    - Testing:
        - Check the cookies used for session management to see if they have the ```SameSite``` attribute set.
        - Test if the cookies are sent with cross-site requests and determine if CSRF protections are in place.
3. Double-Submit Cookies
    - Description: A method where the CSRF token is set both in a cookie and as a form value. The server verifies that both the token in the form and the token in the cookie match.
    - How it works:
        - The client receives a CSRF token in a cookie.
        - The client includes the token in the form or AJAX request, and the server verifies that both tokens match.
    - Testing:
        - Inspect whether the CSRF token is set both as a cookie and in the request body.
        - Check if the tokens match and if the server properly validates them.
4. CORS and CSRF
    - Description: If Cross-Origin Resource Sharing (CORS) is improperly configured, CSRF attacks can be performed via JavaScript by allowing cross-origin requests.
    - Testing:
        - Check if CORS headers are overly permissive (e.g., ```Access-Control-Allow-Origin: *```) and if credentials are allowed (```Access-Control-Allow-Credentials: true```).
        - Attempt cross-origin requests to verify if the server accepts them.
5. Referer Header Validation
    - Description: Some applications defend against CSRF by checking the ```Referer``` or ```Origin``` headers to ensure that requests are coming from trusted origins.
    - Testing:
        - Inspect the server’s behavior when the ```Referer``` or ```Origin``` header is missing or spoofed.
    - Check if the server properly validates the origin before processing the request.

## CSRF Testing Checklist
1. Test for CSRF Tokens:

    - Look for sensitive actions like form submissions or AJAX requests that do not include anti-CSRF tokens.
    - Test if submitting requests without a CSRF token or with a forged token bypasses protections.
2. Check Cookie Settings:

    - Verify if session cookies have the ```SameSite``` attribute set to ```Strict``` or ```Lax```.
    - Check if cookies are sent automatically with cross-site requests.
3. Test ```GET``` Requests for State-Changing Actions:

    - Identify if ```GET``` requests are used for actions that modify server-side state (e.g., voting, deleting, updating).
    - Attempt to perform these actions by embedding the URL in an img or iframe tag.
4. Inspect CORS Settings:

    - Ensure that CORS policies are not overly permissive.
    - Verify that credentials (e.g., cookies) are not allowed across untrusted origins.

5. Check for Double-Submit Cookie Implementation:

    - Confirm if CSRF tokens are stored both in a cookie and submitted in the request body.
    - Check if both tokens are properly validated on the server.
6. Validate Referer or Origin Header:

    - Check if the server validates the Referer or Origin header for all sensitive requests.
    - Attempt to send requests without these headers and observe the server’s response.

## CSRF Best Practices
1. Use Anti-CSRF Tokens:

    - Always include unique, unpredictable anti-CSRF tokens for sensitive actions, and validate them on the server.
2. Set SameSite Cookies:

    - Use ```SameSite=Strict``` or ```SameSite=Lax``` for session cookies to limit cross-site cookie usage.
3. Avoid ```GET``` for State-Changing Actions:

    - Never use ```GET``` requests for actions that modify server-side data; always use ```POST``` or another safe method.
4. Proper CORS Configuration:

    - Ensure CORS is only enabled for trusted domains, and avoid allowing credentials across multiple origins.
5. Token Validation:

    - For sensitive actions, ensure that CSRF tokens are validated against the session and are not predictable.

## Final Notes

- CSRF attacks: Can lead to severe impacts such as fund transfers, account takeovers, or changing user settings.
- Mitigation: Always implement anti-CSRF tokens, use ```SameSite``` cookies, and ensure state-changing actions are performed with proper authentication and validation.
- Testing: Focus on finding endpoints without anti-CSRF tokens, checking for unsafe GET requests, and validating cookie settings.