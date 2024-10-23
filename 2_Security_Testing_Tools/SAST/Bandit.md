# Bandit Notes

## Overview
Bandit is an open-source static code analysis tool designed to find security issues in Python code. It scans Python code for common security vulnerabilities and programming errors that could lead to insecure code. Bandit is part of the OpenStack Security Project but is widely used across various Python projects to ensure security and code quality.

Bandit focuses on identifying issues such as improper use of cryptographic functions, unsafe imports, weak password handling, and injection vulnerabilities. It provides a lightweight and straightforward way for Python developers to integrate security checks into their workflow.

## Key Features of Bandit
1. Static Code Analysis for Python
    - Description: Bandit performs static analysis by analyzing Python code to detect common security flaws. It examines each file for vulnerabilities, such as improper function calls or unsafe libraries.
    - Usage:
        - Run Bandit against a Python project or individual files to identify potential security issues.
        - Bandit generates a report showing the severity and type of each issue detected.
    - Key Benefits:
        - Identifies security risks early in the development cycle.
        - Helps ensure that Python code adheres to best security practices.
2. Wide Range of Vulnerability Checks
    - Description: Bandit checks for a variety of Python-specific security issues, including:
        - Input validation issues: Injection vulnerabilities (e.g., SQL, command injections).
        - Insecure cryptographic usage: Weak or insecure cryptographic functions (e.g., use of md5).
        - Unsafe use of functions: Insecure function calls like ```eval()```, ```exec()```, or ```subprocess``` without proper sanitization.
        - Insecure file operations: Unsafe file access or permissions handling.
    - Key Benefits:
        - Provides coverage for a wide range of common Python vulnerabilities, ensuring more secure code.
3. Customizable Configuration
    - Description: Bandit allows developers to configure which tests to run, exclude specific files or directories, and tailor the level of analysis to their project's needs.
    - Usage:
        - Developers can customize which issues Bandit reports on by modifying the ```bandit.yml``` configuration file or using command-line flags to include or exclude specific tests.
    - Key Benefits:
        - Offers flexibility to adapt Bandit's scanning behavior to fit various project types and security needs.
4. Integration with CI/CD Pipelines
    - Description: Bandit can easily be integrated into CI/CD pipelines to automate security checks as part of the development process.
    - Usage:
        - Add Bandit to your CI/CD pipeline configuration (e.g., with GitHub Actions, Travis CI, Jenkins) to automatically scan new code commits for vulnerabilities.
    - Key Benefits:
        - Ensures continuous security checks throughout the development lifecycle, catching vulnerabilities early before code is merged or deployed.
5. Severity Levels and Filtering
    - Description: Bandit categorizes issues by severity (LOW, MEDIUM, HIGH) and allows filtering results based on severity thresholds.
    - Usage:
        - Use command-line options to filter results to show only high-severity issues, or to suppress low-risk warnings.
    - Key Benefits:
        - Helps developers focus on the most critical security issues first.

## Common Use Cases
1. Detecting Insecure Function Usage
    - Unsafe Functions: Bandit flags the use of unsafe functions like ```eval()```, ```exec()```, and ```subprocess``` that could allow arbitrary code execution if not properly controlled.
    - Example: Detecting the use of ```eval()``` in Python code, which allows untrusted input to be executed as code.

            user_input = "some input"
            eval(user_input)  # This will be flagged as a risk by Bandit
2. Identifying Insecure Cryptography
    - Weak Cryptographic Functions: Bandit detects weak cryptographic algorithms such as MD5 and DES that are considered insecure by modern standards.
    - Example: Bandit flags the use of ```hashlib.md5()``` for hashing passwords as insecure.

            import hashlib
            m = hashlib.md5()  # This will be flagged as insecure
3. Checking for Hardcoded Credentials
    - Hardcoded Secrets: Bandit identifies hardcoded credentials, passwords, API keys, or tokens embedded in the codebase, which pose a security risk.
    - Example: Bandit will flag hardcoded credentials in your code.

            password = "SuperSecretPassword123!"  # This will be flagged
4. Validating Input and Output Handling
    - Injection Vulnerabilities: Bandit checks for improper handling of user input that could lead to injection attacks (SQL injection, command injection).
    - Example: Detecting vulnerabilities in ```subprocess``` calls where untrusted input is passed without proper sanitization.

            import subprocess
            subprocess.call("ls " + user_input, shell=True)  # Flagged for unsafe user input handling
5. Securing File Access and Permissions
    - File Operations: Bandit analyzes file handling operations to detect insecure permissions, paths, and access methods.
    - Example: It flags insecure file access modes, such as opening files with world-writable permissions.

            open("/tmp/file.txt", "w")  # This could be flagged depending on file mode and usage

## Vulnerabilities Detected by Bandit
1. Command Injection
    - Description: Occurs when untrusted input is passed to a command execution function (e.g., ```os.system()```, ```subprocess```) without proper sanitization.
    - Example:

            os.system("rm -rf " + user_input)  # This can be exploited with user-controlled input
2. SQL Injection
    - Description: Occurs when user input is directly included in SQL queries without proper sanitization, allowing attackers to manipulate the SQL query.
    - Example:

        query = "SELECT * FROM users WHERE id = " + user_input
3. Insecure Use of ```eval()``` and ```exec()```
    - Description: eval() and exec() functions allow Python code execution based on input, which can be exploited to execute arbitrary code.
    - Example:

            eval(user_input)  # Executes user input as Python code, a significant security risk
4. Weak Cryptography
    - Description: Using weak or outdated cryptographic algorithms (e.g., MD5, DES) that are prone to attacks.
    - Example:

            hashlib.md5(data).hexdigest()  # MD5 is flagged as insecure
5. Hardcoded Secrets
    - Description: Storing sensitive information like passwords, API keys, or tokens directly in the source code is flagged as a critical security risk.
    - Example:

            api_key = "mysecretapikey"  # Hardcoded API key will be flagged by Bandit
6. Insecure File Permissions
    - Description: Improper file handling, such as opening files with insecure permissions, can be flagged by Bandit for posing a security risk.
    - Example:

            open("/tmp/important.txt", "w+")  # Insecure access permissions could be flagged
7. Insecure Imports
    - Description: Importing unsafe or outdated libraries can introduce vulnerabilities. Bandit flags the use of insecure or obsolete libraries (e.g., ftplib, telnetlib).
    - Example:

            import telnetlib  # This library is insecure and will be flagged by Bandit

## Workflow with Bandit
1. Install Bandit:

    - Install Bandit using pip:

            pip install bandit
2. Run Bandit on Your Codebase:

    - Run Bandit on your Python project or individual files:

            bandit -r /path/to/your/project
    - The -r option tells Bandit to recursively scan the project directory.
3. Review the Results:

    - Bandit will output a report of the findings, including:
        - The severity of the issue (LOW, MEDIUM, HIGH).
        - The specific line in the code where the vulnerability exists.
        - Recommendations for remediation.
4. Fix Vulnerabilities:

    - Address the issues identified by Bandit, such as replacing insecure functions, adding input validation, or removing hardcoded credentials.
5. Re-run Bandit:

    - After making changes, re-run Bandit to ensure that vulnerabilities have been resolved.
6, Integrate with CI/CD Pipelines:

    - Set up Bandit in your CI/CD pipeline to automatically scan for vulnerabilities during each build.

## Key Benefits of Bandit
1. Focuses on Python-Specific Security Issues:

    - Bandit is tailored to Python, making it highly effective for identifying security risks specific to Python applications.
2. Lightweight and Easy to Use:

    - Bandit is simple to install and use, with minimal setup required. It provides actionable insights with a single command.
3. Continuous Security Scanning:

    - Bandit can be integrated into CI/CD pipelines to provide continuous security checks, ensuring code is secure before being merged or deployed.
4. Customization:

    - Developers can customize which tests to run, exclude specific files or directories, and set severity thresholds, making Bandit flexible for various project requirements.
5. Prioritization of Critical Issues:

    - Bandit’s severity categorization (LOW, MEDIUM, HIGH) helps developers prioritize the most critical vulnerabilities.

## Bandit Defense Checklist
1. Check for Insecure Function Usage:

    - Ensure that Bandit flags any insecure functions (e.g., ```eval()```, ```exec()```, ```os.system()```) for remediation.
2. Monitor Cryptography Usage:

    - Ensure that Bandit identifies any weak cryptographic algorithms and replace them with more secure alternatives like SHA-256 or AES.
3. Scan for Hardcoded Secrets:

    - Regularly scan for hardcoded credentials, API keys, and passwords, ensuring sensitive information is stored securely (e.g., environment variables).
4. Validate Input Handling:

    - Use Bandit to identify insecure input handling that could lead to injection vulnerabilities (e.g., SQLi, command injection).
5. Regular Scans with CI/CD Integration:

    - Integrate Bandit into your CI/CD pipeline to automatically scan for security vulnerabilities on every commit or pull request.
6. Review File Access and Permissions:

    - Use Bandit to flag improper file access modes and ensure files are handled with secure permissions.

## Final Notes
- Bandit is a powerful, lightweight tool for ensuring Python code security. It identifies common security issues and vulnerabilities specific to Python, helping developers secure their applications early in the development lifecycle.
- Best Practices: Use Bandit regularly, integrate it into your CI/CD pipeline, and address high-severity vulnerabilities before they lead to potential security incidents.