# Burp Suite Notes

## Overview
Burp Suite is a comprehensive web application security testing tool, widely used for penetration testing and vulnerability assessment. It consists of multiple tools that work together to support the entire testing process, from initial mapping and analysis of an application's attack surface, to finding and exploiting vulnerabilities.

**Burp Suite comes in two editions**:

- Community Edition (Free): Limited functionality, suitable for manual testing.
- Professional Edition (Paid): Includes advanced features such as automated scanning and more powerful attack features.


## Key Components of Burp Suite
1. Proxy
    - Description: The Proxy allows Burp Suite to intercept, inspect, and modify HTTP/S requests and responses between your browser and web applications.
    - Usage:
        - Set up Burp Suite as a proxy server (typically ```127.0.0.1:8080```).
        - Configure your browser to send traffic through Burp.
        - Intercept requests and responses, modify them as needed, and forward them to their destination.
    - Key Features:
        - Inspect and manipulate web traffic in real-time.
        - Interception can be toggled on/off for specific domains or request types.
2. Repeater
    - Description: The Repeater tool allows you to modify and resend HTTP/S requests repeatedly, observing the response from the server each time.
    - Usage:
        - Send requests from Proxy (or other tools) to Repeater.
        - Modify parts of the request such as headers, parameters, or body, and send it repeatedly.
    - Key Features:
        - Excellent for testing inputs and payloads to observe different behaviors.
        - Useful for manual exploration of how parameters affect the server response.
3. Intruder
    - Description: Intruder automates attacks by fuzzing input parameters, brute-forcing credentials, or performing injection attacks.
    - Usage:
        - Identify positions in the request to fuzz or brute force (called "attack positions").
        - Select payloads (e.g., username lists, fuzz strings) and the type of attack (Sniper, Battering Ram, Pitchfork, or Cluster Bomb).
        - Run the attack and observe the responses to detect vulnerabilities or weaknesses.
    - Key Features:
        - Supports customizable payloads and attack configurations.
        - Ideal for testing things like brute-force login attempts or fuzzing web form inputs.
4. Scanner (Professional Edition Only)
    - Description: The Scanner tool automatically scans web applications for common vulnerabilities like SQL injection, cross-site scripting (XSS), or security misconfigurations.
    - Usage:
        - Configure the target scope for scanning.
        - Run passive or active scans on the application.
        - Review the report generated, which includes identified vulnerabilities and remediation guidance.
    - Key Features:
        - Automated detection of a wide range of web vulnerabilities.
        - Can crawl entire web applications and find hidden attack surfaces.
5. Decoder
    - Description: Decoder is used to encode or decode data in various formats such as Base64, URL encoding, or hexadecimal.
    - Usage:
        - Paste encoded or obfuscated data, choose the encoding type (e.g., Base64, HTML), and decode or encode as needed.
    - Key Features:
        - Quickly converts data into different formats.
        - Useful for analyzing obfuscated or encoded data, such as cookies or tokens.
6. Comparer
    - Description: Comparer helps you identify differences between two sets of data, typically used to compare HTTP requests, responses, or other text-based data.
    - Usage:
        - Load two pieces of data and compare them to see differences.
        - Useful for understanding how different inputs affect server responses.
    - Key Features:
        - Provides a side-by-side comparison of two data sets.
        - Useful for finding subtle differences in responses or request behavior.
7. Sequencer
    - Description: Sequencer is used to analyze the randomness or predictability of tokens or session IDs.
    - Usage:
        - Capture multiple tokens or session IDs, and run an analysis to evaluate their randomness.
    - Key Features:
        - Provides statistical analysis on the quality of session tokens.
        - Helps identify weak or predictable session tokens that could be vulnerable to session hijacking.

## Common Use Cases
1. Intercepting and Modifying HTTP Requests
    - Proxy is used to capture and alter requests, allowing for manipulation of parameters, headers, and cookies to test for vulnerabilities like SQLi or XSS.
2. Brute-Force Attacks
    - Use Intruder to brute-force login forms by submitting a large list of usernames and passwords or testing multiple payloads in parameters to identify potential weaknesses.
3. Manual Vulnerability Testing
    - Repeater is ideal for manually testing how different inputs affect the server, such as probing for SQL injection vulnerabilities, exploring authentication bypasses, or analyzing server behavior under varying conditions.
4. Automated Vulnerability Scanning
    - In the Professional Edition, Scanner can automatically crawl and scan web applications for a range of security issues, providing detailed reports on found vulnerabilities.
5. Testing Token Predictability
    - Sequencer is useful for evaluating the randomness of session tokens, CSRF tokens, or other key tokens used in an application.

## Burp Suite Workflow
1. Configure Proxy:

    - Set up Burp to intercept traffic by configuring the proxy in both Burp and your browser.
    - Browse the target application while intercepting requests and responses.
2. Explore Application Manually:

    - Use Repeater to manually explore how the application behaves when receiving different inputs.
    - Identify sensitive endpoints, forms, and parameters.
3. Automate Attacks:

    - Use Intruder to automate fuzzing, brute-forcing, or injection attacks.
    0 Define payload positions and run the attack, monitoring the results for vulnerabilities.
4. Scan for Vulnerabilities (Professional Edition):

    - Set up Scanner to automatically detect vulnerabilities across the target web application.
    - Review reports and take action on high-risk findings.

5. Decode/Compare:

    - Use Decoder to encode/decode data (e.g., tokens or cookies) and Comparer to analyze differences between responses or requests.

## Key Shortcuts and Tips
- Ctrl + I: Quickly send a request from Proxy to Intruder.
- Ctrl + R: Send a request from Proxy to Repeater.
 - Right-Click: Context menu lets you send intercepted requests to any of Burp's tools (Repeater, Intruder, Scanner, etc.).
- Scope Management: Define a target scope to limit your interactions and scans to only the relevant parts of an application.
- Filter Options: Use filters in Proxy to focus on specific types of traffic or specific domains.

## Burp Suite Extensions
Burp Suite has an Extender tool that allows you to add extensions, which can be found in the BApp Store. Popular extensions include:

- SQLMap: Automates SQL injection testing.
- AuthMatrix: Tests authorization and access control.
- Logger++: Provides detailed logging of all HTTP requests and responses.
- Retire.js: Identifies outdated JavaScript libraries with known vulnerabilities.

## Final Notes
- Burp Suite is an all-in-one solution for manual and automated web application security testing, with tools for intercepting traffic, modifying requests, automating attacks, and scanning for vulnerabilities.
- Use Burp responsibly and ensure you have permission to test any web application.
- Proxy, Repeater, and Intruder form the core of manual testing, while Scanner automates vulnerability detection in the Professional Edition.