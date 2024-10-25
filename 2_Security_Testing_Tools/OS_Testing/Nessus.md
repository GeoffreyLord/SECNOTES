# Nessus Notes
## Overview
Nessus is a widely-used vulnerability scanner developed by Tenable that helps organizations identify and manage security vulnerabilities across IT infrastructure. Nessus scans systems for vulnerabilities, misconfigurations, default passwords, and sensitive data exposure. It is available in different versions, including Nessus Essentials (free for home users), Nessus Professional (for business), and Tenable.io (for cloud-based scans).

## Key Features of Nessus
1. Comprehensive Vulnerability Scanning
    - Description: Nessus performs in-depth vulnerability scans across network devices, operating systems, databases, applications, and configurations.
    - Usage:
        - Run a full scan to detect vulnerabilities on endpoints, servers, network equipment, and more.
    - Key Benefits:
        - Detects a broad range of security issues, including missing patches, misconfigurations, and weak credentials.
2. Regularly Updated Plugins
    - Description: Nessus uses plugins to perform vulnerability checks. These plugins are updated regularly with new vulnerability signatures, checks, and remediation recommendations.
    - Usage:
        - Keep plugins updated automatically via Nessus or manually update as needed.
    - Key Benefits:
        - Ensures that scans detect the latest vulnerabilities by using up-to-date plugins.
3. Customizable Scan Templates
    - Description: Nessus offers predefined scan templates, including basic network scans, compliance checks, web application tests, and malware scans. Custom templates can also be created for tailored needs.
    - Usage:
        - Choose or create a scan template based on specific assessment requirements, such as a network vulnerability scan or compliance audit.
    - Key Benefits:
        - Saves time by providing ready-to-use templates and enables custom scans to focus on specific areas.
4. Credentialed and Uncredentialed Scans
    - Description: Nessus supports both credentialed (authenticated) and uncredentialed (unauthenticated) scans to increase scan depth.
    - Usage:
        - Provide system credentials (e.g., SSH, Windows credentials) for deeper scans on trusted hosts.
    - Key Benefits:
        - Authenticated scans reveal more vulnerabilities by accessing system internals that unauthenticated scans cannot detect.
5. Detailed and Actionable Reporting
    - Description: Nessus generates reports with vulnerability details, including severity, affected systems, and remediation steps.
    - Usage:
        - View or export reports in formats such as PDF, HTML, CSV, or Nessus format for analysis and distribution.
    - Key Benefits:
        - Helps prioritize and track vulnerabilities with actionable recommendations for remediation.
6. Policy Compliance Checks
    - Description: Nessus performs compliance checks against security policies and standards like CIS, NIST, PCI DSS, and HIPAA.
    - Usage:
        - Run compliance scans to assess adherence to regulatory and organizational policies.
    - Key Benefits:
        - Ensures systems meet regulatory requirements, reducing the risk of non-compliance penalties.

## Common Use Cases
1. Routine Vulnerability Scanning
    - Network Scanning: Schedule scans to keep an updated view of vulnerabilities across the network.
    - Example: Running weekly scans on critical systems to ensure vulnerabilities are detected promptly.
2. Deep Scans with Credentials
    - Authenticated Scanning: Use credentials for a thorough scan that uncovers vulnerabilities requiring system access.
    - Example: Providing SSH keys for Linux servers to identify vulnerabilities in system files and configurations.
3. Compliance Audits
    - Policy Compliance Checks: Run scans to assess system compliance with standards like PCI DSS, HIPAA, and CIS.
    - Example: Running PCI DSS compliance checks on systems handling credit card data.
4. Customized Scanning
    - Custom Scan Templates: Create templates to scan specific areas, like web applications, file servers, or IoT devices.
    - Example: Customizing a scan to focus on web application vulnerabilities, such as SQL injection or cross-site scripting.
5. Integration with Security Workflows
    - Automated Scanning: Integrate Nessus scans into CI/CD pipelines or automated workflows for continuous security monitoring.
    - Example: Adding a Nessus scan to a Jenkins pipeline to check new code for security vulnerabilities before deployment.

## Key Commands and Usage
1. Starting a Scan
    - Description: Launch a vulnerability scan from the Nessus web interface.
    - Usage:
        - Access Nessus via the web UI, create a new scan, configure targets, and start the scan.
        - Choose from templates (e.g., Basic Network Scan, Web Application Tests) or create a custom scan.
2. Updating Plugins
    - Description: Update plugins to ensure the latest vulnerability checks.
    - Usage:
        - Plugin updates are usually automated but can be manually triggered in the Nessus web interface.

                sudo /opt/nessus/sbin/nessuscli update  # Command-line update for Nessus plugins
3. Viewing Scan Results
    - Description: View the list of vulnerabilities and affected systems after a scan.
    - Usage:
        - Access scan results in the web UI, categorized by severity (Info, Low, Medium, High, Critical).
4. Exporting Reports
    - Description: Export detailed reports of scan results for further analysis and distribution.
    - Usage:
        - Export scan results in PDF, HTML, CSV, or .nessus format from the Nessus web UI for sharing with stakeholders or uploading to other security tools.
5. Scheduling Regular Scans
    - Description: Set up recurring scans to keep vulnerability data up to date.
    - Usage:
        - In the Nessus web interface, configure a scan schedule (daily, weekly, monthly) for automated assessments.

## Interpreting Results
    - Severity Ratings: Nessus rates vulnerabilities as Info, Low, Medium, High, or Critical, helping prioritize remediation.
    - CVE and Plugin ID References: Vulnerabilities link to CVE IDs and Nessus plugin IDs, enabling further research.
    - Remediation Recommendations: Each finding includes recommended remediation steps, helping teams address vulnerabilities effectively.

## Best Practices
1. Update Plugins Regularly:

    - Keep Nessus plugins updated to detect the latest vulnerabilities.
2. Run Frequent Scans on Critical Systems:

    - Schedule regular scans for high-value assets (e.g., databases, public-facing servers) to detect vulnerabilities quickly.
3. Use Credentialed Scans for Greater Depth:

    - Perform authenticated scans on trusted systems to reveal deeper, more complex vulnerabilities.
4. Prioritize Critical Vulnerabilities:

    - Address High and Critical findings first, focusing on vulnerabilities with the highest risk.
5. Leverage Compliance Checks:

    - Use Nessus’s compliance scanning feature to ensure systems meet regulatory standards like PCI DSS, HIPAA, or NIST.
6. Integrate into CI/CD Pipelines:

    - Automate Nessus scans in CI/CD workflows to identify vulnerabilities before code is deployed to production.

## Final Notes
- Nessus is a versatile and powerful tool for vulnerability management, offering in-depth scans, compliance checks, and customizable reporting for thorough security assessments.
- Best Practices: Regularly update plugins, prioritize critical vulnerabilities, and use authenticated scans to maximize the effectiveness of Nessus scanning.