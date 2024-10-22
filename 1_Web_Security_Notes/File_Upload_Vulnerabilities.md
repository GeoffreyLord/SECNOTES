# File Upload Vulnerabilities Notes:
## Overview
File upload vulnerabilities occur when web applications allow users to upload files without properly validating or securing them. This can lead to various types of attacks, including remote code execution, cross-site scripting (XSS), and denial of service (DoS). Ensuring the security of file upload functionality is critical, especially when dealing with file types that could be malicious.

## Types of File Upload Vulnerabilities
1. Unrestricted File Upload
    - Description: The server allows uploading files without validating the file type, size, or content.
    - Risk: Attackers can upload executable files (e.g., ```.php```, ```.jsp```, ```.exe```) that may be executed on the server, leading to remote code execution.
    - Testing:
        - Try uploading a file with executable extensions (e.g., ```.php```, ```.asp```, ```.exe```) and see if the server processes or executes it.
        - Inspect how the server handles different MIME types or file headers.
2. Content-Type Mismatch
    - Description: The server relies on the ```Content-Type``` header for file validation, which can be easily spoofed.
    - Risk: An attacker can upload a file with a harmless extension (e.g., ```.jpg```), but the content is actually executable code (e.g., a PHP script).
    - Testing:
        - Modify the ```Content-Type``` header in the upload request to match a valid file type but upload a malicious file.
        - Test uploading files with mismatched extensions and headers (e.g., renaming a ```.php``` file to ```.jpg```).
3. Directory Traversal
    - Description: The server does not properly sanitize file paths, allowing an attacker to upload files to unintended directories.
    - Risk: Attackers can use directory traversal (```../```) in the file path to overwrite or upload files in sensitive locations (e.g., system directories, config files).
    - Testing:
        - Attempt to manipulate the upload path with directory traversal sequences (e.g., ```../../```).
        - Test if files can be uploaded outside of the intended directory (e.g., root directories).
4. File Overwrite
    - Description: The server allows uploaded files to overwrite existing files without verifying uniqueness.
    - Risk: Attackers can overwrite important files on the server, such as configuration files, system binaries, or other user-uploaded content.
    - Testing:
        - Upload a file with the same name as an existing file on the server.
        -Check if the existing file is overwritten without validation.
5. Large File Upload (Denial of Service)
    - Description: The server does not limit the size of uploaded files, leading to resource exhaustion (disk space, CPU, memory).
    - Risk: Attackers can upload excessively large files, causing denial of service by exhausting server resources.
    - Testing:
        - Upload large files (e.g., in the range of gigabytes) to check if the server enforces file size limits.
        - Test if the server handles multipart file uploads that can bypass size restrictions.
6. Stored XSS via File Upload
    - Description: Attackers upload files that contain malicious JavaScript (e.g., in image metadata or as HTML content), which can execute when users or admins view the file.
    - Risk: When the file is viewed or rendered, the embedded script executes in the context of the web application, allowing the attacker to steal cookies, hijack sessions, or perform other actions.
    - Testing:
        - Upload files with embedded XSS payloads (e.g., in image metadata or HTML files).
        - Verify if the uploaded files are rendered or displayed in the browser without proper sanitization.

## Exploitation Techniques
1. Uploading a Web Shell
    - Technique: Upload a file with server-side code (e.g., a PHP or JSP web shell) and execute it by visiting the uploaded file.
    - Example:
        - ```<?php system($_GET['cmd']); ?>```
    - Testing:
        - Upload the web shell to the server.
        - Access the uploaded file via a browser and append a command to the URL (e.g., ```?cmd=ls```).
        - Check if the server executes the command.
2. MIME Sniffing Bypass
    - Technique: Bypass content-type restrictions by using file headers or magic numbers that match an allowed type (e.g., start with the header for an image but embed malicious content).
    - Testing:
        - Modify file headers to make them appear as valid types (e.g., using exiftool to modify image metadata).
        - Upload files with manipulated headers or magic numbers and observe how the server processes them.
3. Polyglot Files
    - Technique: Create a file that is valid as more than one file type (e.g., a file that is both a valid image and executable code).
    - Example:
        - A ```.jpg``` file that also contains embedded PHP code.
    - Testing:
        - Upload polyglot files and test if they are executed or displayed by the server.
4. Null Byte Injection
    - Technique: Use null byte characters (```%00```) to truncate the file extension in some older systems, tricking the server into treating the file as a different type.
    - Testing:
        - Upload a file with a null byte before the extension (e.g., ```file.php%00.jpg```) and test if the server processes it as a ```.php``` file.
## Defensive Mechanisms
1. File Type Validation
    - Description: Restrict file uploads to only safe, expected file types by validating both file extensions and MIME types.
    - Best Practices:
        - Validate the file extension and MIME type on both the client and server side.
        - Use a whitelist of allowed file types (e.g., ```.jpg```, ```.png```, ```.pdf```).
        - Avoid relying solely on ```Content-Type``` headers, as they can be spoofed.
    - Testing:
        - Test file uploads with different extensions and MIME types to ensure the validation is enforced.
2. File Content Validation
    - Description: Validate the actual content of the file (e.g., magic numbers) to ensure it matches the claimed file type.
    - Best Practices:
        -Check the file’s magic numbers (the first few bytes of the file) to c  confirm the file type.
        - Scan uploaded files for malicious content (e.g., using antivirus software or security tools).
    - Testing:
        - Upload files with mismatched content and extensions to see if content validation is performed.
3. Renaming Uploaded Files
    - Description: Rename uploaded files to prevent attackers from controlling file names or paths.
    - Best Practices:
        -Generate unique file names (e.g., using a UUID or hash) to prevent overwriting and to avoid exposing sensitive information in file names.
    - Testing:
        - Check if the uploaded file’s name is changed on the server.
        - Attempt to upload files with the same name to see if the server overwrites existing files.
4. Storing Files Outside the Web Root
    - Description: Store uploaded files in a directory outside the web root to prevent direct access and execution.
    - Best Practices:
        - Store files in a directory that is not publicly accessible and serve them via a handler script that controls access.
    - Testing:
        - Try accessing uploaded files via direct URL paths.
        - Verify that sensitive files are not directly accessible or executable.
5. Size Limits and Throttling
    - Description: Enforce file size limits and throttle the number of uploads to prevent resource exhaustion.
    - Best Practices:
        - Set reasonable limits on file sizes (e.g., a few MBs for images, larger for documents).
        - Implement rate-limiting or CAPTCHA to prevent DoS attacks via file uploads.
    - Testing:
        - Upload large files or attempt many uploads in a short time and observe if the server restricts or throttles the requests.

## Testing Checklist for File Upload Vulnerabilities
1. Test for Allowed File Types:

    - Try uploading files with restricted or executable extensions (e.g., ```.php```, ```.asp```, ```.exe```).
    - Check if the server blocks files based on extension or MIME type.

2. Inspect File Name and Path Handling:

    - Check if uploaded files are renamed and if paths are properly sanitized.
Test for directory traversal by manipulating file paths (e.g., ```../../file```).

3. Test MIME Type and Content Validation:

    - Upload files with mismatched MIME types and content (e.g., a ```.jpg``` file with embedded code).
    - Verify if the server checks the actual content and structure of the file.

4. Check File Size and Rate Limits:

    - Attempt to upload excessively large files and observe if the server enforces size restrictions.
    - Test if multiple file uploads are rate-limited to prevent DoS.

5. Validate File Storage Security:

    - Ensure uploaded files are stored outside the web root and cannot be accessed or executed directly.
    - Try accessing files via direct URLs to verify if access is properly restricted.

## Best Practices for Securing File Uploads
1. Validate Both Client and Server Side:

    - Perform client-side validation for user feedback, but always enforce file validation on the server.

2. Sanitize File Names and Paths:

    - Always sanitize file names and paths to prevent directory traversal or overwriting issues.
3. Use Whitelisting for File Types:

    - Only allow specific, known-safe file types to be uploaded (e.g., ```.jpg```, ```.png```, ```.pdf```).
4. Limit File Size and Enforce Rate-Limiting:

    - Set reasonable file size limits and throttle uploads to avoid resource exhaustion.
5. Disable Direct Execution of Files:

    - Store files in non-executable directories and serve them through controlled handlers.
6. Use Antivirus Scanning:

    - Consider integrating antivirus or malware scanning for uploaded files to detect harmful content.

## Final Notes
- File uploads: Present significant security risks if not properly validated and handled. Attackers can exploit misconfigurations to upload malicious files or manipulate file paths.
- Defense: Ensure strict validation of file types, sizes, and content. Store files securely and outside the web root, and avoid executing uploaded content.
- Testing focus: Try uploading executable files, oversized files, and files with mismatched MIME types to find potential vulnerabilities.
