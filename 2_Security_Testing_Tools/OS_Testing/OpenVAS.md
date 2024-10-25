# OpenVAS (Open Vulnerability Assessment System) Notes
## Overview
OpenVAS (Open Vulnerability Assessment System) is an open-source vulnerability scanner used for conducting security assessments on network systems, devices, and applications. Part of the Greenbone Vulnerability Management (GVM) framework, OpenVAS helps security professionals identify security risks by scanning for known vulnerabilities and misconfigurations. It supports a wide range of network protocols and regularly updates its vulnerability definitions to ensure comprehensive assessments.

## Key Features of OpenVAS
1. Network Vulnerability Scanning
    - Description: OpenVAS performs comprehensive network scans to detect vulnerabilities across various network devices, applications, and operating systems.
    - Usage:
        - Configure and run network scans to identify open ports, services, and potential vulnerabilities.
    - Key Benefits:
        - Helps detect insecure configurations, missing patches, and known vulnerabilities in networked systems.
2. Regularly Updated Vulnerability Feed
    - Description: OpenVAS regularly updates its vulnerability definitions through Greenbone’s feed, which includes checks for thousands of vulnerabilities (CVEs).
    - Usage:
        - Ensure the vulnerability feed is updated frequently to maintain an up-to-date assessment of security threats.
    - Key Benefits:
        - Provides the latest vulnerability checks, allowing for accurate assessments against new and emerging threats.
3. Flexible Scan Configurations
    - Description: OpenVAS offers various scanning options, allowing users to perform full scans, partial scans, or customized scans targeting specific protocols, devices, or vulnerabilities.
    - Usage:
        - Configure scan settings to focus on specific assets or prioritize critical services.
    - Key Benefits:
        - Tailored scans improve efficiency by allowing users to prioritize high-risk assets or specific vulnerabilities.
4. Authenticated Scanning
    - Description: OpenVAS supports credential-based scans, allowing it to perform authenticated checks that reveal vulnerabilities only accessible with system credentials.
    - Usage:
        - Provide credentials (e.g., SSH, SMB) for systems where authenticated scans are required.
    - Key Benefits:
        - In-depth scanning of authenticated systems provides a more accurate view of system vulnerabilities that may not be visible to unauthenticated scans.
5. Comprehensive Reporting
    - Description: OpenVAS generates detailed reports on vulnerabilities discovered during scans, including severity ratings, descriptions, and remediation recommendations.
    - Usage:
        - Review scan results in the OpenVAS interface or export them in various formats (PDF, HTML, XML) for detailed analysis and reporting.
    - Key Benefits:
        - Clear and actionable reporting helps prioritize and track vulnerability remediation efforts.
6. Integrations and Automation
    - Description: OpenVAS integrates with various security management and DevSecOps tools, allowing for automated vulnerability scanning and streamlined reporting.
    - Usage:
        - Integrate OpenVAS into a CI/CD pipeline to automate scans on new builds or regularly schedule scans for continuous monitoring.
    - Key Benefits:
        - Automating scans helps ensure continuous security monitoring, especially in dynamic or high-velocity environments.

## Common Use Cases
1. Routine Vulnerability Scanning
    - Network Scanning: Schedule regular scans to keep track of vulnerabilities and misconfigurations in the network infrastructure.
    - Example:
        
            # Set up a daily scan schedule to detect newly introduced vulnerabilities.
2. Authenticated Scans for In-Depth Analysis
    - Credential-Based Scanning: Use authenticated scans to uncover vulnerabilities that require access to system internals.
    - Example:

            # Provide SSH credentials for a Linux server to perform a deep scan.
3. Targeted Scanning for High-Impact Assets
    - Custom Scan Profiles: Use custom scan configurations to target critical systems, such as servers with sensitive data or systems exposed to the internet.
    - Example:

            # Configure a scan to focus on high-risk servers only.
4. Integration with CI/CD Pipelines
    - Automated Security Testing: Integrate OpenVAS scans into CI/CD workflows to automatically scan new code deployments or infrastructure changes.
    - Example:

            # Run a scan as part of the CI/CD pipeline to detect vulnerabilities before production deployment.

## Key Commands and Usage
1. Starting OpenVAS
    - Description: Start the OpenVAS services to prepare the scanner.
    - Usage:

            sudo systemctl start openvas-scanner     # Start the OpenVAS scanner service
            sudo systemctl start gvmd                # Start the Greenbone Vulnerability Manager
            sudo systemctl start gsad                # Start the Greenbone Security Assistant (web interface)
2. Updating the Vulnerability Feed
    - Description: Download the latest vulnerability definitions from Greenbone’s feed to keep scans up-to-date.
    - Usage:

            sudo greenbone-nvt-sync                  # Update Network Vulnerability Tests (NVTs)
            sudo greenbone-certdata-sync             # Update CERT data
            sudo greenbone-scapdata-sync             # Update SCAP data
3. Running a Basic Scan
    - Description: Run a basic scan from the OpenVAS web interface.
    - Usage:
        - Log in to the Greenbone Security Assistant (GSA) web interface.
        - Create a new target and task, then start the scan.
4. Viewing Scan Results
    - Description: Review the scan results to identify vulnerabilities and security risks.
    - Usage:
        - Access results through the GSA web interface, which categorizes vulnerabilities by severity and provides remediation suggestions.
5. Exporting Reports
    - Description: Export scan reports in various formats for distribution and further analysis.
    - Usage:
        - In the GSA interface, navigate to the specific task and choose the export format (PDF, HTML, CSV, etc.).

## Interpreting Results
- Severity Ratings: OpenVAS categorizes vulnerabilities by severity (Low, Medium, High, Critical) to help prioritize remediation.
- CVE References: Vulnerabilities often include CVE IDs, allowing for further research on vulnerability specifics and patches.
- Remediation Recommendations: OpenVAS provides actionable remediation steps, helping teams address and fix vulnerabilities effectively.

## Best Practices
1. Keep Vulnerability Feeds Updated:

    - Regularly update the OpenVAS feed to ensure the latest vulnerability definitions are used in scans.
2. Run Regular Scans:

    - Schedule periodic scans to maintain visibility into your network’s security status and catch new vulnerabilities.
3. Use Authenticated Scans When Possible:

    - Credentialed scans provide a more comprehensive view of vulnerabilities, especially for critical internal systems.
4. Focus on High-Risk Assets:

    - Prioritize scanning high-impact assets (e.g., internet-exposed servers or systems with sensitive data) and address high-severity vulnerabilities first.
5. Integrate into CI/CD Pipelines:

    - Automate scans in your CI/CD pipelines to detect vulnerabilities early in the development cycle, ensuring new code is secure.

## Final Notes
- OpenVAS is a robust, open-source vulnerability scanner ideal for identifying network security issues and ensuring systems remain secure over time.
- Best Practices: Regularly update vulnerability definitions, prioritize critical vulnerabilities, and integrate OpenVAS into security workflows for continuous monitoring.