# Path Traversal Vulnerabilities Notes:

## Overview
Path Traversal (Directory Traversal) is a web vulnerability that allows attackers to access files and directories stored outside the web root directory by manipulating file paths in requests. This is typically done by using sequences like ```../```(dot-dot-slash), which allow the attacker to traverse up the directory tree and potentially access sensitive files such as configuration files, password files, or application source code.

## How Path Traversal Works
When a web application accepts user input to specify file paths (e.g., through URL parameters or form inputs), attackers can manipulate this input to navigate the file system and access files that should not be publicly accessible.

**Example of Path Traversal**:

A vulnerable web application includes a file like this:

    http://example.com/get-file?filename=report.pdf

If the input is not properly validated, an attacker can manipulate the filename parameter to traverse directories:


    http://example.com/get-file?filename=../../../../etc/passwd

This could allow the attacker to access the ```/etc/passwd``` file, potentially leaking sensitive information.

## Common Path Traversal Attacks
1. Accessing Sensitive Files
    - Description: Attackers use path traversal to access sensitive files stored on the server, such as ```/etc/passwd``` (Linux) or ```C:\Windows\System32``` (Windows).
    - Example:
        
            http://example.com/get-file?filename=../../../../etc/passwd
    - Impact: The attacker can read configuration files, password hashes, or other sensitive data.
2. Source Code Disclosure
    - Description: Attackers may use path traversal to access and read the source code of the web application, gaining insight into potential vulnerabilities.
    - Example:
        
            http://example.com/get-file?filename=../../../../var/www/html/index.php
    - Impact: Exposing source code can reveal hardcoded credentials, security misconfigurations, or logic flaws.
3. Log File Access
    - Description: Attackers can access log files to gain information about the system, application, or users.
    - Example:
        
            http://example.com/get-file?filename=../../../../var/log/apache2/access.log
    - Impact: Log files can contain sensitive information such as user activity, IP addresses, or error messages that expose further vulnerabilities.
4. File Overwrite / Manipulation
    - Description: In some cases, path traversal can be used to overwrite or manipulate server-side files, potentially leading to code execution or defacement.
    - Example:
        
            http://example.com/upload?filename=../../../../var/www/html/index.html
    - Impact: Overwriting key files like web pages or configuration files can result in website defacement or backdoor installation.

## Path Traversal Variants
1. Absolute Path Traversal
    - Description: The attacker specifies an absolute file path to access sensitive files directly.
    - Example:
        
            http://example.com/get-file?filename=/etc/passwd
    - Impact: Allows direct access to sensitive files if the application does not sanitize absolute paths.
2. Relative Path Traversal
    - Description: The attacker uses relative paths (e.g., ```../../```) to navigate the directory structure and access files.
    - Example:
        
            http://example.com/get-file?filename=../../../../etc/passwd
    - Impact: Exploits improper validation of file paths, enabling access to files outside the web root.
3. URL-Encoding
    - Description: Attackers URL-encode special characters (```../``` as ```%2E%2E%2F```) to bypass basic input validation or filtering.
    - Example:
        
            http://example.com/get-file?filename=%2E%2E%2F%2E%2E%2F%2E%2E%2Fetc/passwd
    - Impact: Bypasses filters that only check for plaintext ```../``` sequences, allowing traversal attacks to succeed.
4. Null Byte Injection
    - Description: In older systems, a null byte (```%00```) could terminate strings early, potentially bypassing extensions or input sanitization.
    - Example:
        
            http://example.com/get-file?filename=../../../../etc/passwd%00.txt
    - Impact: The server may terminate the filename at the null byte, accessing the target file instead of the sanitized one.

## Path Traversal Exploitation Techniques
1. Identifying Entry Points
    - Technique: Look for user input that is used to specify file names or paths (e.g., ```filename```, ```path```, ```document``` parameters).
    - Testing:
        - Check URL parameters, form inputs, or cookies where file paths might be used.
        - Try injecting basic traversal sequences like ../ and observe server responses.
2. Incremental Traversal
    - Technique: Incrementally add ```../``` sequences to see how many directory levels are needed to reach sensitive files.
    - Testing:
        - Test varying numbers of ```../``` to navigate up the directory tree.
        - Use ```../../../../etc/passwd``` as a common payload on Linux systems to check for the presence of ```/etc/passwd```.
3. Testing Common Files
    - Technique: Test for common system files that may provide valuable information.
    - Common Targets:
        - Linux: ```/etc/passwd```, ```/etc/shadow```, ```/var/log/apache2/access.log```
        - Windows: ```C:\Windows\System32\drivers\etc\hosts```, ```C:\Windows\win.ini```
4. Bypassing Filters with Encodings
    - Technique: Use URL-encoding, double encoding, or other encoding methods to bypass basic path validation.
    - Example:
        - URL encode traversal sequences: ```%2E%2E%2F%2E%2E%2Fetc%2Fpasswd```
        - Double encode %2E%2E%2F as ```%252E%252E%252F``` to further bypass filters.

## Defense Mechanisms Against Path Traversal
1. Canonicalization and Path Normalization
     - Description: Convert all file paths to their canonical form before processing, eliminating redundant ```../``` sequences.
    - Best Practices:
        - Use functions that normalize paths and prevent directory traversal (e.g., ```realpath()``` in PHP).
        - Reject paths that contain directory traversal sequences like ../.
2. Whitelist Valid File Paths
    - Description: Restrict file access to a predefined set of directories and files using a whitelist approach.
    - Best Practices:
        - Allow access only to specific directories or files that are explicitly required by the application.
        - Ensure all user inputs are validated against this whitelist.
3. Input Validation
    - Description: Validate all user inputs to ensure they contain only allowed characters and do not contain directory traversal sequences.
    - Best Practices:
        - Only allow filenames without special characters (```/```, ```\```, ```.```).
        - Reject any input containing ```../```, ```%2E%2E```, or similar sequences.
4. Use Least Privilege Principle
    - Description: Run the application with the least privileges necessary to operate, limiting its access to sensitive files.
    - Best Practices:
        - Ensure the web server or application only has access to files within its designated directory and cannot access system files.
5. Chroot Jail / Virtualization
    - Description: Use chroot jails or containers to isolate the application’s file system, preventing it from accessing files outside a defined environment.
    - Best Practices:
        - Use chroot to restrict the application’s view of the file system to a safe environment.
        - Ensure the application cannot escape the chroot jail or container.

## Testing for Path Traversal Vulnerabilities
1. Manual Testing
    - Inject Path Traversal Sequences:

        - Test with simple ```../``` sequences in user-controllable fields to see if traversal is possible.
        - Example:
            
                http://example.com/get-file?filename=../../../../etc/passwd

    - Test URL Encoding:

        - Encode traversal sequences as ```%2E%2E%2F``` and inject them into file path parameters.
2. Automated Tools
    - Burp Suite:

        - Use Burp Suite’s Intruder to automate the injection of path traversal payloads.
        - Monitor the responses to identify file access or error messages indicating traversal success.
    - OWASP ZAP:

        - OWASP ZAP includes path traversal payloads that can be used in automated scans to detect vulnerabilities.
3. Check for Common Files
    - Test Known Files:
        - Try accessing files such as ```/etc/passwd```, ```C:\Windows\win.ini```, or other system files that are known to be present.
4. Monitor Server Responses
    - Look for Indicators of Traversal:
    - Success indicators include:
        - The presence of file content (e.g., the ```/etc/passwd``` file being displayed).
        - Error messages such as "file not found" or "access denied" indicating traversal attempts are occurring.

## Path Traversal Defense Checklist
1. Normalize Paths:

    - Ensure all paths are canonicalized and normalized to eliminate directory traversal sequences.
2. Validate Input:

    - Validate file path inputs to ensure they don’t contain special characters like ```../``` or ```%2E%2E```.
3. Whitelist Valid Directories:

    - Use a whitelist to restrict file access to known, safe directories and files only.
4. Apply Least Privilege:

    - Limit the web server’s permissions to only access necessary directories and files.
5. Use Containers/Chroot Jails:

    - Isolate the application’s file system using a chroot jail or container to prevent access to sensitive files outside the web root.
## Final Notes
- Path Traversal: A critical vulnerability that allows attackers to access sensitive files outside the web root directory.
- Mitigation: Focus on input validation, path normalization, and whitelisting to prevent traversal attacks.
- Testing: Use manual and automated techniques to inject traversal payloads and attempt to access sensitive files.