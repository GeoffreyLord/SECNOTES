# Server-Side Request Forgery (SSRF) Vulnerabilities Notes
## Overview
Server-Side Request Forgery (SSRF) occurs when an attacker can make a web application send unauthorized requests to internal or external systems. SSRF allows attackers to manipulate and control how a vulnerable server interacts with other services, potentially exposing sensitive data or performing unauthorized actions. This can lead to accessing internal networks, sensitive data, or even executing arbitrary commands depending on the system architecture.

## How SSRF Works
SSRF vulnerabilities arise when a web application takes user-supplied input and uses it to make requests to other servers without proper validation. The attacker can manipulate the input to force the server to make requests to unintended destinations, including:

- Internal services: Accessing private or local networks (e.g., ```127.0.0.1``` or ```http://localhost```) or cloud metadata services.
- External services: Bypassing firewalls or network restrictions by making the server request external services controlled by the attacker.

**Example of SSRF**:
A web application allows users to provide a URL to fetch an external resource (e.g., a profile picture):

    http://example.com/fetch?url=http://example.com/profile.jpg

An attacker can modify the url parameter to target internal systems:

    http://example.com/fetch?url=http://localhost/admin

## Types of SSRF
1. Basic SSRF
    - Description: The attacker controls the target URL, allowing them to interact with internal services or retrieve sensitive data.
    - Example:
        - ```http://example.com/fetch?url=http://127.0.0.1/admin```
        - This could expose sensitive admin interfaces or internal services.
    - Impact: Accessing internal endpoints, services, or sensitive files, which are usually not exposed to the public internet.
2. Blind SSRF
    - Description: The attacker cannot see the server's response, but can still control the target and infer actions based on server behavior (e.g., timing or error messages).
    - Example:
        - ```http://example.com/fetch?url=http://internal-service/api/delete```
        - The attacker triggers actions on internal services without seeing the response.
    - Impact: Even without seeing the response, attackers can perform malicious actions like triggering internal services or performing denial of service attacks.
3. SSRF to Internal Networks
    - Description: Attackers use SSRF to access and explore internal networks by targeting internal IP addresses or hostnames.
    - Example:
        - Target internal services using private IP ranges:
        - ```http://example.com/fetch?url=http://192.168.1.1```
    - Impact: Exposes internal network details, potentially allowing further network exploration, internal service access, or lateral movement.
4. SSRF via Cloud Metadata Services
    - Description: Many cloud services provide a metadata API (e.g., AWS, Google Cloud) that can be accessed from within the infrastructure. Attackers can exploit SSRF to retrieve sensitive information, like credentials.
    - Example (AWS):
        - ```http://example.com/fetch?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/```
        - This URL accesses the metadata service, potentially exposing AWS access keys.
    - Impact: Exposing cloud instance metadata, which can reveal sensitive information like instance details or cloud service credentials.

## Real-World Impacts of SSRF
1. Accessing Internal Resources
    - Description: SSRF can allow attackers to access internal resources that are not meant to be exposed to the public, such as administrative interfaces, databases, or internal APIs.
    - Example:
        - An attacker can access an internal management portal:
        - ```http://example.com/fetch?url=http://localhost/admin```
2. Exfiltrating Sensitive Data
    - Description: Attackers can use SSRF to request sensitive internal files or data, such as system credentials, logs, or configuration files.
    - Example:
        - Access internal sensitive files like:
        - ```http://example.com/fetch?url=file:///etc/passwd```
3. Exploiting Cloud Metadata Services
    - Description: Attackers can use SSRF to retrieve cloud provider metadata, such as credentials or instance information.
    - Example:
        - Access AWS credentials through the metadata API:
        - ```http://example.com/fetch?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/```
4. Pivoting to Internal Services
    - Description: Once an attacker has access to an internal service via SSRF, they can use it to pivot and explore further into the internal network.
    - Example:
        - An attacker can discover internal services running on private IPs:
        - ```http://example.com/fetch?url=http://192.168.1.10:8080```
5. Performing Denial of Service (DoS)
    - Description: SSRF can be exploited to target internal or external services with a flood of requests, causing performance degradation or service interruption.
    - Example:
        - Flood internal services with requests, causing them to overload.

## Exploitation Techniques
1. Basic SSRF Exploitation
    - Technique: Modify user-controllable input (e.g., a URL parameter) to point to sensitive internal services or files.
    - Example:
        - ```http://example.com/fetch?url=http://127.0.0.1/admin```
2. Exploiting Cloud Metadata Services
    - Technique: Use SSRF to request cloud instance metadata endpoints that can expose sensitive information, such as access credentials or configuration details.
    - Example (AWS):
        - http://example.com/fetch?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/
3. Port Scanning Internal Networks
    - Technique: Use SSRF to perform port scans of internal networks by testing various IP addresses and ports to identify services running on them.
    - Example:
        - Scanning an internal service:
        - ```http://example.com/fetch?url=http://192.168.1.10:8080```
4. Blind SSRF
    - Technique: Even without seeing the server’s response, attackers can perform actions by observing side effects, such as error messages or response time.
    - Example:
        - Triggering a request that leads to an external service to check for network activity or changes:
        - ```http://example.com/fetch?url=http://attacker.com```

## Defense Mechanisms Against SSRF
1. Whitelist External Resources
    - Description: Implement strict whitelists for external URLs or IPs that are allowed to be fetched by the server.
    - Best Practices:
        - Only allow requests to trusted domains and IP addresses.
        - Avoid allowing arbitrary URL inputs from users.
2. Blacklist Internal IP Ranges
    - Description: Block access to internal IP addresses (e.g., 127.0.0.1, 192.168.x.x, 10.x.x.x) to prevent access to internal resources.
    - Best Practices:
        - Implement firewalls or network rules to block requests to internal/private IP ranges.
        - Use regular expressions or IP filtering to block requests to internal services.
3. DNS Resolution Controls
    - Description: Ensure that user-provided URLs do not resolve to internal IP addresses or services.
    - Best Practices:
        - Resolve URLs server-side and verify they belong to allowed external domains before making a request.
        - Use DNS rebinding protection to prevent attackers from manipulating DNS responses.
4. Disable Unnecessary Network Access
    - Description: Restrict the server’s ability to make outbound requests to unnecessary services or networks.
    - Best Practices:
        - Limit the server's outbound traffic to only necessary external services.
        - Block access to cloud metadata endpoints from within instances.
5. Input Validation and URL Parsing
    - Description: Validate and sanitize user input to ensure it adheres to expected URL formats and doesn’t contain unsafe characters.
    - Best Practices:
        - Use robust URL parsing libraries to validate user inputs.
        - Reject malformed or dangerous URL formats (e.g., file://, ftp://).
6. Rate Limiting
        - Description: Implement rate limiting to prevent abuse of SSRF vulnerabilities, such as sending a high volume of requests to internal or external services.
        - Best Practices:
            - Set limits on the number of requests a user can initiate in a given time frame.
            - Monitor logs for unusual patterns of requests to detect SSRF attacks.


## Testing for SSRF
1. Manual Testing
    - Inject Internal and External URLs:
        - Test with URLs pointing to internal services, local files, or cloud metadata endpoints.
        - Examples:
            - ```http://example.com/fetch?url=http://127.0.0.1/admin```
            - ```http://example.com/fetch?url=file:///etc/passwd```
            - ```http://example.com/fetch?url=http://169.254.169.254/latest/meta-data/```
2. Automated Testing Tools
    - Burp Suite:
        - Use Burp Suite Intruder to test SSRF by sending multiple requests to internal/external IPs and URLs.
        - Burp Collaborator can be used to detect blind SSRF by tracking callbacks or external requests triggered by the SSRF attack.
    - OWASP ZAP:
        - Use OWASP ZAP to scan for SSRF by injecting internal/external URLs into user-controllable inputs and analyzing server responses.
3. Test for Cloud Metadata Access
    - Cloud-Specific SSRF:
        - Target cloud metadata services like AWS or Google Cloud to retrieve sensitive information.
        - Example (AWS):
            - ```http://example.com/fetch?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/```
4. Monitor Server Responses and Logs
    - Look for Indicators of SSRF:
        - Check server responses for internal IP addresses or unexpected external responses.
        - Monitor logs for requests made to internal networks, files, or metadata endpoints.

## SSRF Defense Checklist
1. Implement URL Whitelisting:

    - Only allow requests to specific trusted URLs and domains.
2. Block Internal IP Ranges:

    - Prevent requests to internal IP addresses or private network ranges.
3. Use DNS Resolution and IP Filtering:

    - Ensure URLs resolve to allowed domains and not internal IP addresses.
4, Sanitize and Validate Input:

    - Use URL validation and sanitization to prevent malicious URLs from being processed.
5. Disable Outbound Network Access:

    - Restrict the server’s ability to make outbound requests, especially to cloud metadata services.
6. Monitor and Rate Limit Requests:

    - Implement rate limiting and log monitoring to detect and prevent abuse of SSRF vulnerabilities.

## Final Notes
- SSRF: A critical vulnerability that allows attackers to exploit a server's ability to make requests to unintended destinations, often exposing internal networks or sensitive data.
- Mitigation: Implement URL whitelisting, input validation, internal IP blocking, and DNS resolution controls to prevent SSRF attacks.
- Testing: Focus on manipulating URL parameters and targeting internal/external services to detect SSRF vulnerabilities.
