# Fortify Notes
## Overview
Fortify is a comprehensive application security platform provided by Micro Focus, designed to help organizations identify and remediate security vulnerabilities in software throughout the development lifecycle. Fortify offers both static application security testing (SAST) and dynamic application security testing (DAST), enabling developers and security teams to identify vulnerabilities in code and deployed applications.

Fortify integrates seamlessly into development pipelines, providing detailed security analysis across a wide range of programming languages, frameworks, and platforms. It ensures that security vulnerabilities are addressed early in the development cycle, reducing the risk of security breaches in production.

## Key Components of Fortify
1. Fortify Static Code Analyzer (SCA)
    - Description: Fortify’s Static Code Analyzer (SCA) performs static analysis of source code, identifying security vulnerabilities, coding errors, and quality issues before the code is executed.
    - Languages Supported: Supports a wide range of languages, including Java, C/C++, JavaScript, Python, Ruby, PHP, .NET, and more.
    - Usage:
        - Scans source code for vulnerabilities and security flaws.
        - Integrates with development environments (IDEs) and CI/CD pipelines.
    - Key Features:
        - Identifies vulnerabilities based on industry standards (e.g., OWASP Top 10, CWE).
        - Helps address security risks before code is deployed, reducing potential security incidents.
2. Fortify WebInspect (DAST)
    - Description: WebInspect is a dynamic application security testing (DAST) tool that analyzes live, running web applications for vulnerabilities by simulating attacks against the application.
    - Usage:
        - Scans deployed web applications to find vulnerabilities such as SQL injection, cross-site scripting (XSS), CSRF, and misconfigurations.
        - Can be used for black-box testing, where the internal structure of the application is not known.
    - Key Features:
        - Identifies vulnerabilities in real-time by simulating attacker behavior.
        - Provides remediation suggestions based on discovered vulnerabilities.
3. Fortify Software Security Center (SSC)
    - Description: The Software Security Center (SSC) is the central hub for managing application security assessments and tracking vulnerabilities across development projects.
    - Usage:
        - Provides a dashboard for managing, prioritizing, and remediating security issues found by Fortify’s analysis tools (SCA and WebInspect).
        - Tracks vulnerability trends over time and integrates with issue tracking systems (e.g., JIRA).
    - Key Features:
        - Centralized management of security assessments across multiple projects.
        - Tracks vulnerabilities and assigns risk ratings to help prioritize fixes.
        - Supports collaboration between security teams and developers.
4. Fortify Audit Workbench
    - Description: The Audit Workbench is a desktop application that provides detailed insights into vulnerabilities found by Fortify’s Static Code Analyzer. It allows developers and security teams to review, audit, and prioritize issues.
    - Usage:
        - Review and analyze the findings from static code scans.
        - Use filtering and categorization to prioritize the most critical vulnerabilities.
    - Key Features:
        - Provides contextual information about vulnerabilities, including CWE references and remediation suggestions.
        - Allows users to flag false positives and group similar vulnerabilities for efficient management.
5. Fortify Remediation Plugin for IDEs
    - Description: Fortify provides a plugin that integrates with popular development environments (IDEs) like Eclipse, IntelliJ IDEA, and Visual Studio, allowing developers to view and fix security vulnerabilities directly within their coding environment.
    - Usage:
        - Run static code analysis within the IDE and view security vulnerabilities as part of the development workflow.
        - Receive remediation suggestions and fix vulnerabilities in real-time.
    - Key Features:
        - Enables "security as you code" by flagging security issues during development.
        - Streamlines the process of fixing vulnerabilities without leaving the IDE.

## Common Use Cases
1. Detecting Security Vulnerabilities in Source Code
    - Static Analysis with SCA:
        - Fortify SCA identifies security vulnerabilities during the development phase by scanning source code for flaws like SQL injection, buffer overflows, and improper input validation.
        - Example: Finding and remediating an XSS vulnerability in a JavaScript application before deployment.
2. Real-Time Vulnerability Detection in Deployed Applications
    - Dynamic Analysis with WebInspect:
        - Fortify WebInspect scans live web applications by simulating attacker behaviors, identifying vulnerabilities like cross-site scripting, SQL injection, and insecure configurations.
        - Example: Scanning a production e-commerce platform for security flaws without needing access to the underlying code.
3. Continuous Integration with CI/CD Pipelines
    - CI/CD Integration:
        - Fortify integrates with CI/CD tools like Jenkins, GitLab, and Azure DevOps to automate security testing as part of the build process.
        - Example: Automatically triggering a Fortify SCA scan after each code commit to ensure new vulnerabilities aren’t introduced during development.
4. Compliance with Industry Standards
    - Security Compliance:
        - Fortify supports compliance with industry standards such as OWASP Top 10, CWE/SANS Top 25, PCI DSS, and HIPAA by detecting and reporting vulnerabilities based on these frameworks.
        - Example: Ensuring that an application meets OWASP Top 10 compliance requirements before launch.
5. Managing Application Security Posture
    - Security Management with SSC:
        - Use Fortify SSC to track security assessments across multiple applications, prioritize critical vulnerabilities, and assign remediation tasks to developers.
        - Example: Using SSC’s dashboard to monitor security issues across multiple development teams and projects.

## Vulnerabilities Detected by Fortify
1. SQL Injection (SQLi)
    - Description: An attacker manipulates input fields to execute malicious SQL queries, potentially allowing unauthorized access to data.
    - Example: Improperly validated user input being passed into SQL queries without sanitization.
2. Cross-Site Scripting (XSS)
    - Description: An attacker injects malicious scripts into web pages, which are then executed in the browser of other users.
    - Example: Failing to sanitize user input in form fields or URLs, leading to JavaScript injection.
3. Buffer Overflow
    - Description: Occurs when a program writes more data to a buffer than it can hold, potentially leading to crashes or arbitrary code execution.
    - Example: Writing beyond the bounds of an array in C/C++ code, leading to memory corruption.
4. Cross-Site Request Forgery (CSRF)
    - Description: A malicious website tricks a user’s browser into making unintended requests to another site where the user is authenticated.
    - Example: A user unknowingly performs an unintended action (e.g., changing a password) by clicking a malicious link while logged in.
5. Insecure Configuration
    - Description: Security misconfigurations such as weak security settings, exposed sensitive data, or improper error handling.
    - Example: Exposing server version details in HTTP headers or having weak SSL/TLS configurations.
6. Data Leakage and Exposure
    - Description: Exposing sensitive data such as passwords, tokens, or API keys in logs, error messages, or source code.
    - Example: Including hardcoded credentials in source code or configuration files.
7. Insecure Deserialization
    - Description: A vulnerability that occurs when untrusted data is used to reconstruct objects, potentially leading to remote code execution or privilege escalation.
    - Example: Accepting untrusted serialized data from external sources without validation.

## Fortify Workflow
1. Set Up Fortify SCA:

    - Install and configure Fortify SCA in your development environment.
    - Define the codebase or project to scan for static analysis.
2. Run Static Analysis:

    - Perform a static code scan using Fortify SCA to detect vulnerabilities.
    - Review the scan results in Audit Workbench or within the IDE plugin for more detailed analysis.
3. Use Fortify WebInspect for Dynamic Testing:

    - Deploy Fortify WebInspect to scan live web applications for runtime vulnerabilities.
    - Configure scan settings based on the target web application and perform a dynamic scan.
4. Manage and Track Vulnerabilities in SSC:

    - Use Software Security Center (SSC) to track all security assessments and vulnerability findings across projects.
    - Prioritize critical vulnerabilities and assign remediation tasks to developers.
5. Fix Vulnerabilities and Rescan:

    - Developers can fix vulnerabilities within their IDE using the Fortify plugin, or manually based on SSC or Audit Workbench findings.
    - After fixes are applied, rescan the code or application to ensure the issues are resolved.
6. Monitor and Report:

    - Use SSC’s reporting features to generate detailed reports on vulnerability trends and project security posture.
    - Continuously monitor new vulnerabilities and ensure compliance with security standards.

## Key Benefits of Fortify
1. Early Detection of Vulnerabilities:

    - Identifying security issues early in the development cycle helps prevent vulnerabilities from reaching production, saving both time and resources.
2. Comprehensive Security Coverage:

    - Fortify covers a wide range of security vulnerabilities, including both common and advanced threats like SQL injection, XSS, buffer overflows, and insecure configurations.
3. Integration with DevSecOps:

    - Fortify integrates with CI/CD tools and IDEs, enabling "security as code" by incorporating security testing directly into development pipelines.
4. Standards Compliance:

    - Fortify supports industry standards like OWASP, CWE, PCI DSS, and HIPAA, helping organizations meet regulatory and compliance requirements.
5. Centralized Management:

    - Fortify’s SSC allows security teams and developers to collaborate effectively, tracking vulnerabilities across multiple projects from a single platform.

## Fortify Defense Checklist
1. Run Regular Static and Dynamic Scans:

    - Use Fortify SCA for static code analysis during development and Fortify WebInspect for dynamic analysis of live applications.
2. Integrate with CI/CD:

    - Automate security testing in your CI/CD pipeline to ensure code changes are secure before deployment.
3. Prioritize Critical Vulnerabilities:

    - Use Fortify SSC to track and prioritize high-risk vulnerabilities, ensuring they are addressed before moving to production.
4. Enable IDE Plugins:

    - Allow developers to detect and fix security vulnerabilities directly in their IDEs to minimize disruption to their workflow.
5. Monitor Compliance:

    - Ensure your application adheres to industry security standards and compliance frameworks by regularly scanning and auditing with Fortify.
6. Regularly Review and Update:

    - Continuously monitor and reassess your application for new vulnerabilities, especially as the codebase evolves.

## Final Notes
- Fortify is a robust security platform that provides both static and dynamic testing capabilities, enabling teams to identify and remediate vulnerabilities throughout the software development lifecycle.
- Best Practices: Integrate Fortify into your development pipeline, run regular scans, and use the Software Security Center to manage and track vulnerabilities efficiently.
- Collaboration: Fortify fosters collaboration between developers and security teams, ensuring that vulnerabilities are addressed as part of the development process, improving both security and code quality.