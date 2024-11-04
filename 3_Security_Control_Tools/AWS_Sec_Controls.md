# AWS Security Controls Notes

## Overview
AWS provides a wide range of security controls and tools to protect cloud infrastructure, applications, and data. These controls help secure resources by managing access, monitoring activity, encrypting data, and maintaining compliance. This notes sheet outlines key AWS security features across identity and access management, network protection, data security, and logging/monitoring.

## Identity and Access Management (IAM)
1. AWS IAM (Identity and Access Management)
    - Description: AWS IAM enables administrators to manage user access to AWS resources, controlling permissions based on roles and policies.
    - Key Controls:
        - Users: Individual accounts with personalized access.
        - Groups: Collections of users with shared permissions.
        - Roles: Assign permissions to AWS services or external users.
        - Policies: Define permissions, either AWS-managed or custom.
    - Best Practices:
        - Enforce least privilege by assigning only necessary permissions.
        - Use IAM roles instead of user credentials for services accessing other AWS resources.
        - Enable MFA (Multi-Factor Authentication) for IAM users, especially for privileged accounts.
2. AWS Organizations
    - Description: Manages multiple AWS accounts under one organization, allowing centralized control over account access and security.
    - Key Controls:
        - Service Control Policies (SCPs): Restrict services and actions across accounts.
        - Organizational Units (OUs): Group accounts by function or environment for targeted policy application.
    - Best Practices:
        - Apply SCPs to enforce mandatory security controls across accounts.
        - Separate production and non-production accounts for better security management.
3. AWS Single Sign-On (SSO)
    - Description: Provides centralized access control across multiple AWS accounts and applications with single sign-on capabilities.
    - Best Practices:
        - Integrate with on-premises Active Directory or SAML-based identity providers for streamlined authentication.
        - Enforce MFA and password policies for SSO users.

## Network Security
1. Virtual Private Cloud (VPC)
    - Description: An isolated network environment within AWS, allowing control over IP addressing, subnets, route tables, and network gateways.
    - Key Controls:
        - Security Groups: Stateful, virtual firewalls that control inbound and outbound traffic at the instance level.
        - Network ACLs: Stateless access control lists that manage subnet-level traffic.
    - Best Practices:
        - Limit traffic by configuring least privilege rules in Security Groups.
        - Use Network ACLs for additional layer of subnet protection.
2. AWS Web Application Firewall (WAF)
    - Description: Protects web applications from common threats (e.g., SQL injection, XSS) by filtering HTTP and HTTPS traffic.
    - Key Controls:
        - Rules: Define filters for specific attacks, such as OWASP Top 10 threats.
        - Managed Rules: Predefined rule sets by AWS and security partners.
    - Best Practices:
        - Use Managed Rules to protect against known web application vulnerabilities.
        - Enable rate limiting to mitigate denial-of-service (DoS) attacks.
3. AWS Shield
    - Description: DDoS protection service that automatically safeguards applications against large-scale attacks.
    - Key Controls:
        - AWS Shield Standard: Automatic protection for all AWS customers.
        - AWS Shield Advanced: Enhanced DDoS protection and 24/7 support.
    - Best Practices:
        - Enable Shield Advanced for critical applications with higher DDoS risks.
        - Integrate Shield with AWS WAF for comprehensive web protection.
4. VPC Flow Logs
    - Description: Captures detailed information about the IP traffic going to and from network interfaces in a VPC.
    - Best Practices:
        - Enable Flow Logs on all VPCs and subnets for traffic monitoring.
        - Send logs to CloudWatch Logs or S3 for analysis.

## Data Security
1. AWS Key Management Service (KMS)
    - Description: Centralized service for managing encryption keys to secure data at rest and in transit.
    - Key Controls:
        - Customer Master Keys (CMKs): Encrypt data across AWS services.
        - Key Policies: Define access permissions for CMKs.
    - Best Practices:
        - Use AWS-managed CMKs for default encryption and customer-managed CMKs for custom access controls.
        - Rotate CMKs and set up audit logging with AWS CloudTrail.
2. AWS Certificate Manager (ACM)
    - Description: Provision, manage, and deploy SSL/TLS certificates for securing network communications.
    - Best Practices:
        - Use ACM certificates for all public-facing applications.
        - Regularly review and renew certificates to avoid expiration.
3. Encryption Options in AWS Services
    - Description: AWS provides encryption options across services, such as S3, RDS, EBS, and DynamoDB.
    - Best Practices:
        - Enable encryption by default on S3 buckets, EBS volumes, and RDS databases.
        - Use client-side encryption for additional security if data is managed outside AWS.

## Monitoring and Logging
1. AWS CloudTrail
    - Description: Monitors and logs account activity across the AWS infrastructure, tracking API calls, user actions, and changes.
    - Key Controls:
        - Event History: Stores recent activity for quick analysis.
        - Trails: Configure custom trails to log activity to an S3 bucket for long-term storage.
    - Best Practices:
        - Enable CloudTrail on all accounts and configure multi-region trails.
        - Store logs in an S3 bucket with encryption and controlled access.
2. Amazon CloudWatch
    - Description: Collects and monitors performance data, system metrics, and application logs.
    - Key Controls:
        - CloudWatch Logs: Stores logs from AWS resources (e.g., EC2, Lambda).
        - CloudWatch Alarms: Triggers notifications based on performance thresholds.
    - Best Practices:
        - Set up CloudWatch Alarms for critical metrics (e.g., CPU usage, memory).
        - Use CloudWatch Logs Insights to analyze log data and detect anomalies.
3. AWS Config
    - Description: Tracks and records configuration changes to AWS resources, allowing administrators to assess compliance and audit history.
    - Best Practices:
        - Define AWS Config Rules to evaluate compliance for critical resources.
        - Enable Config in all regions and regularly review non-compliant resources.
4. AWS GuardDuty
    - Description: Threat detection service that monitors malicious activity, unauthorized behavior, and compromised instances.
    - Best Practices:
        - Enable GuardDuty across all accounts for continuous threat monitoring.
        - Regularly review GuardDuty findings to detect and respond to incidents.
5. AWS Security Hub
    - Description: Centralizes security findings and provides compliance checks across AWS accounts.
    - Key Controls:
        - Integrates with AWS services like GuardDuty, Macie, and Inspector.
        - Provides CIS and PCI-DSS compliance checks.
    - Best Practices:
        - Enable Security Hub for a consolidated security view.
        - Use findings to prioritize remediation for critical vulnerabilities.

## Compliance and Governance
1. AWS Trusted Advisor
    - Description: Offers best practice recommendations across cost, performance, security, and fault tolerance.
    - Best Practices:
        - Regularly review Trusted Advisor security checks (e.g., S3 permissions, IAM permissions).
        - Address high-severity recommendations promptly.
2. AWS Artifact
    - Description: Provides access to AWS compliance reports, certifications, and agreements.
    - Best Practices:
        - Download relevant compliance documents for audits and regulatory needs.
        - Use Artifact to review AWS’s certifications for compliance requirements.
3. Amazon Inspector
    - Description: Automated security assessment service that checks for vulnerabilities and compliance in EC2 instances.
    - Best Practices:
        - Schedule Inspector assessments regularly for vulnerability management.
        - Address critical findings to keep instances secure and compliant.

## Best Practices Summary
1. Use IAM Roles instead of user access keys for service permissions.
2. Enable Multi-Factor Authentication (MFA) for all users, especially root.
3. Enforce Encryption by default across all data storage services.
4. Enable Monitoring services like CloudTrail, GuardDuty, and Config for activity tracking and compliance.
5. Regularly Audit Security Group Rules and limit inbound/outbound access.
6. Use AWS Security Hub for a unified view of security and compliance.

## Final Notes
- AWS Security Controls provide robust tools to manage access, secure data, and monitor for suspicious activities, critical for maintaining a secure cloud environment.
- Best Practices: Apply the principle of least privilege, enable monitoring, enforce encryption, and use Security Hub for consolidated findings and compliance.