# OWASP ZAP Notes
## Overview
OWASP ZAP (Zed Attack Proxy) is an open-source web application security scanner maintained by the OWASP (Open Web Application Security Project). ZAP is designed to help find security vulnerabilities in web applications during the development and testing phases. It is widely used by both beginners and professionals for manual as well as automated security testing.

OWASP ZAP is highly versatile and includes features for intercepting, modifying, scanning, and fuzzing web application requests and responses.

## Key Features of OWASP ZAP
1. Proxy
    - Description: The Proxy feature allows you to intercept and inspect HTTP/S traffic between your browser and the web server. This helps identify vulnerabilities by observing and modifying requests/responses.
    - Usage:
        - Configure your browser to route traffic through ZAP’s proxy (default: ```localhost:8080```).
        - Intercept and view requests/responses for inspection and manual testing.
    - Key Features:
        - Real-time interception of HTTP/S traffic.
        - Modify requests and responses before forwarding them to the server.
2. Automated Scanner
    - Description: The Automated Scanner tool allows ZAP to crawl and passively or actively scan web applications for common vulnerabilities like SQL Injection, XSS, CSRF, and misconfigurations.
    - Usage:
        - Define a target URL and start an automated scan.
        - The scanner will crawl the web application and generate a report with discovered vulnerabilities.
    - Types of Scans:
        - Passive Scan: Scans web pages as they are browsed but does not actively interact with inputs (e.g., doesn’t submit forms).
        - Active Scan: Actively interacts with the web application to find vulnerabilities (e.g., injecting payloads into form fields).
    - Key Features:
        - Provides detailed reports with vulnerability findings.
        - Useful for quickly identifying common security flaws.
3. Spider (Crawling)
    - Description: The Spider tool crawls the web application, identifying pages, forms, and links. It maps out the structure of the application and helps in discovering hidden or unlinked pages.
    - Usage:
        - Start the Spider on a specific target URL.
        - ZAP will automatically traverse the application, identifying as many pages and endpoints as possible.
    - Key Features:
        - Crawls both traditional websites and modern web applications (including those with JavaScript).
        - Helps locate all possible attack surfaces for further testing.
4. Fuzzer
    - Description: Fuzzer allows you to inject multiple inputs (payloads) into a specific part of an HTTP request to test how the web application handles different types of input.
    - Usage:
        - Choose a request to fuzz (e.g., form fields, parameters) and define fuzzing payloads (e.g., common SQL injection payloads or custom values).
        - Run the fuzzer and observe how the application responds to each input.
    - Key Features:
        - Supports custom payload lists and encoding options.
        - Can be used to find SQL injection, command injection, buffer overflows, and other input-based vulnerabilities.
5. Passive Scan
    - Description: ZAP’s Passive Scan examines HTTP traffic as it passes through the proxy without modifying or injecting any payloads. It looks for vulnerabilities based on headers, cookies, content, etc.
    - Usage:
        - Simply browse the web application while ZAP’s proxy is running.
        - ZAP will automatically passively scan the application and highlight potential vulnerabilities.
    - Key Features:
        - Low impact on the application since no active attacks are performed.
        - Identifies security headers, cookie issues, and information disclosure.
6. Active Scan
    - Description: Active Scan is used to actively test web applications for security vulnerabilities by injecting various attack payloads into forms, URLs, and headers.
    - Usage:
        - After crawling the target, launch an active scan to simulate attack scenarios.
        - ZAP will attempt to exploit known vulnerabilities (e.g., XSS, SQLi, LFI) by sending crafted requests.
    - Key Features:
        - Actively tests for common vulnerabilities by interacting with the target.
        - Can cause changes to the application (use caution on live systems).
7. Scripting and Extensions
    - Description: ZAP allows users to write custom scripts for various purposes (e.g., custom active scan rules, authentication handling, fuzzing strategies) using languages like JavaScript, Python, or Zest (ZAP’s own scripting language).
    - Usage:
        - Go to the Scripts tab, choose a script type (e.g., proxy scripts, active scan scripts), and write your custom logic.
        - Use available templates to create attack scenarios or modify ZAP’s behavior.
    - Key Features:
        - Highly customizable for advanced testing needs.
        - Supports both server-side and client-side scripting for tailored testing scenarios.
## Common Use Cases
1. Intercepting and Modifying HTTP Requests
    - Proxy is used to capture and modify HTTP/S requests and responses. You can change form inputs, manipulate headers, or inject payloads into requests to test how the server reacts.
2. Automated Vulnerability Scanning
    - Use the Automated Scanner to perform both passive and active scans on web applications to quickly detect vulnerabilities such as SQL injection, XSS, and CSRF.
3. Web Crawling and Attack Surface Discovery
    - The Spider tool crawls a web application to discover all accessible pages, forms, and parameters, helping identify potential entry points for further testing.
4. Fuzzing Web Inputs
    - Use the Fuzzer to test the resilience of input fields by injecting different payloads (e.g., SQL injection strings, XSS payloads) and monitoring how the server handles them.
5. Session Hijacking and Token Analysis
    - Capture session tokens or authentication cookies via the Proxy and analyze them using ZAP’s Passive Scan to check if they are securely handled (e.g., check for secure cookie flags, session expiration).

## OWASP ZAP Workflow
1. Start Proxy:

    - Configure your browser to use ZAP’s proxy.
    - Browse the target application while ZAP captures and analyzes the traffic.
2. Map the Application:

    - Use Spider to automatically crawl and discover the web application’s pages and inputs.
    - Review the discovered URLs and forms for manual testing later.
3. Perform Passive Scanning:

    - As you browse the web application, ZAP passively scans HTTP/S traffic for basic vulnerabilities, such as missing security headers, information disclosure, or improper cookie handling.
4. Run Active Scanning:

    - Once the Spider has mapped the application, run an Active Scan to automatically test for known vulnerabilities like SQLi, XSS, and file inclusion attacks.
5. Fuzz Parameters:

    - Use Fuzzer to test input fields or parameters with multiple payloads to discover vulnerabilities related to improper input handling.
6. Review Results and Remediate:

    - Analyze the results from scans and fuzzing sessions. Take note of the identified vulnerabilities and follow ZAP’s remediation guidance to secure the application.

## Key Shortcuts and Tips
- Context Configuration: Set up contexts to define the boundaries of the target application (e.g., URL patterns, authentication settings). This helps ZAP focus its attacks and scans on specific areas.
- Scope: Always define a target scope before performing active scans to avoid attacking out-of-scope assets or external systems.
- Right-Click Actions: Right-click on requests or URLs in the history to access quick options like sending to Fuzzer, Repeater, or Scanner.
- Exclude Content: Exclude static content (e.g., images, stylesheets) from scans to focus only on dynamic parts of the application.

## OWASP ZAP Plugins and Extensions
OWASP ZAP supports a variety of plugins and extensions to extend its functionality. Some popular ones include:

- WS-Attacker: A tool for testing SOAP-based web services.
- Retire.js: Scans for outdated and vulnerable JavaScript libraries in web applications.
- Ajax Spider: A tool to crawl AJAX-heavy or JavaScript-rich applications.
- Script Console: An extension to develop and test custom ZAP scripts.

## Common Vulnerabilities Detected by ZAP
1. SQL Injection (SQLi):
    - ZAP can test for SQL injection by sending crafted input into form fields or URL parameters.
2. Cross-Site Scripting (XSS):
    - Both reflected and stored XSS can be detected by ZAP during active scans.
3. Cross-Site Request Forgery (CSRF):
    - ZAP identifies missing CSRF tokens in forms and requests to protect against unauthorized actions.
4. Information Disclosure:
    - ZAP detects sensitive information leaks, such as server version headers, detailed error messages, or exposed configuration files.
5. Insecure Cookies:
    - ZAP analyzes cookie flags (e.g., ```HttpOnly```, ```Secure```) and highlights security misconfigurations in session management.

## OWASP ZAP Defense Checklist
1. Use Active and Passive Scanning:

    - Always start with passive scanning and escalate to active scanning for more aggressive vulnerability checks.
2. Fuzz Inputs:

    - Use the Fuzzer to explore how different inputs and payloads impact the application, identifying injection vulnerabilities or denial-of-service risks.
3. Analyze Session Tokens:

    - Inspect session tokens for security flaws, such as predictability or missing secure flags.
4. Monitor Security Headers:

    - Ensure the application sets security headers such as ```Content-Security-Policy```, ```X-Frame-Options```, ```Strict-Transport-Security```, and ```X-XSS-Protection```.
5. Examine Logs for Sensitive Data:

    - Check for sensitive information being disclosed in logs or error messages (e.g., stack traces, API keys).

## Final Notes
- OWASP ZAP is a powerful and flexible web application security tool suitable for both beginners and advanced users. It allows both automated and manual security testing, with features like active/passive scanning, fuzzing, and web crawling.
- Best Practices: Always define a clear scope for testing and avoid performing aggressive scans or attacks on production systems.
- Open Source Advantage: OWASP ZAP’s extensibility and support for scripting make it highly adaptable to a wide range of security testing scenarios.