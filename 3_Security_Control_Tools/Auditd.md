# Auditd (Linux Audit Daemon) Notes
## Overview
Auditd (Linux Audit Daemon) is a user-space component for the Linux Audit framework, responsible for monitoring and logging system activities to detect unauthorized access or suspicious behavior. Auditd records events like file access, user logins, system calls, and process actions, helping administrators maintain system integrity and security.

Auditd is especially useful for regulatory compliance (e.g., PCI-DSS, HIPAA) by providing an audit trail for security-related events on Linux systems.

## Key Concepts
1. Audit Rules
    - Description: Define which system events are logged. Rules can be customized to monitor file access, user actions, system calls, and more.
    - Types:
        - File/Directory Watch: Monitors specific files or directories.
        - System Call Monitoring: Logs specific system calls (e.g., ```open```, ```execve```).
        - User/Group Monitoring: Logs actions by specific users or groups.
    - Usage:

            auditctl -w /etc/passwd -p wa -k passwd_watch  # Watch for writes/attributes on /etc/passwd
2. Auditd Configuration File
    - Description: ```/etc/audit/auditd.conf``` controls how Auditd operates, including logging options, buffer size, and rotation.
    - Key Parameters:
        - ```log_file```: Path to the audit log file (default: /var/log/audit/audit.log).
        - ```max_log_file```: Max size of a single audit log file.
        - ```max_log_file_action```: Action when log file reaches max size (e.g., rotate, keep_logs).
        - ```space_left_action```: Action when disk space is low (e.g., email, halt).
    - Usage:

            sudo vi /etc/audit/auditd.conf   # Edit configuration file
3. Audit Log Format
    - Description: Audit logs contain detailed event records, including timestamps, affected objects, and user IDs.
    - Fields:
        - UID/Username: User ID or username of the process or user.
        - SYSCALL: System call name (e.g., ```open```, ```chmod```).
        - PATH: The file path associated with the action.
        - KEY: Custom keyword to help identify the rule that triggered the log entry.

## Basic Commands
1. Starting and Stopping Auditd
    - Description: Start, stop, and restart the Audit daemon.
    - Usage:

            sudo systemctl start auditd       # Start Auditd
            sudo systemctl stop auditd        # Stop Auditd
            sudo systemctl restart auditd     # Restart Auditd
2. Adding Audit Rules with auditctl
    - Description: Temporarily add rules to monitor specific files, directories, or system calls (lost on reboot).
    - Usage:

            auditctl -w /path/to/file -p rwa -k my_watch  # Monitor file for read, write, and attribute changes
            auditctl -a always,exit -S chmod -F uid=1000  # Log chmod calls by user with UID 1000
3. Persisting Rules with /etc/audit/rules.d
    - Description: Save rules in configuration files to persist across reboots.
    - Usage:

            sudo vi /etc/audit/rules.d/audit.rules   # Add rules to persist
            # Example rule to monitor /etc/shadow:
            -w /etc/shadow -p wa -k shadow_watch
4. Listing Active Audit Rules
    - Description: Display all active audit rules.
    - Usage:

            auditctl -l                  # List current audit rules
5. Deleting Audit Rules
    - Description: Remove specific audit rules by identifier or all rules.
    - Usage:

            auditctl -d -w /path/to/file  # Delete a specific file watch rule
            auditctl -D                   # Delete all rules

## Common Use Cases
1. Monitoring Sensitive Files
    - Example: Monitor access to ```/etc/passwd``` for changes.

            auditctl -w /etc/passwd -p wa -k passwd_watch  # Log writes and attribute changes
2. Tracking User Actions
    - Example: Log every command run by a specific user (UID 1001).

            auditctl -a always,exit -F arch=b64 -S execve -F uid=1001 -k user_commands
3. Monitoring System Calls
    - Example: Track calls to ```chmod``` by any user for auditing permission changes.

            auditctl -a always,exit -S chmod -k chmod_watch
4. Logging All Root Commands
    - Example: Capture all commands executed by the root user.

            auditctl -a always,exit -F arch=b64 -S execve -F uid=0 -k root_commands
5. File Integrity Monitoring
    - Example: Monitor any modifications to files in ```/etc/``` to detect unauthorized changes.

            auditctl -w /etc -p wa -k etc_watch

## Useful Tools and Commands
1. ausearch
    - Description: Searches audit logs for specific events or keywords.
    - Usage:

            ausearch -f /etc/passwd               # Search logs for access to /etc/passwd
            ausearch -k passwd_watch              # Search logs by rule key
            ausearch -m USER_LOGIN -ts today      # Find all login events from today
2. aureport
    - Description: Generates reports from audit logs, useful for analyzing audit data.
    - Usage:

            aureport -au                          # Report on all user login attempts
            aureport -f                           # Report on all accessed files
            aureport -l                           # Report on login events
3. auditspd-plugins (Auditd Plugins)
    - Description: Plugins that help forward audit logs to other systems or external files, such as ```syslog``` or remote log aggregators.
    - Usage:

            # Configure in /etc/audisp/plugins.d/
            sudo vi /etc/audisp/plugins.d/syslog.conf  # Forward audit logs to syslog
4. auditd.conf Settings
    - Description: Configure global Auditd settings such as log file location and rotation.
    - Usage:

            sudo vi /etc/audit/auditd.conf       # Edit Auditd configuration
            # Example configuration options:
            log_file = /var/log/audit/audit.log
            max_log_file = 10                    # Set max log file size to 10MB

## Best Practices
1. Define Clear Audit Rules:

    - Avoid overly broad rules to prevent excessive logging and focus on critical files and actions.
2. Use ```key``` Tags for Easy Searching:

    - Tag rules with meaningful keywords (```-k key_name```) to simplify searching and reporting.
3. Rotate and Manage Audit Logs:

    - Configure log rotation in ```auditd.conf``` to prevent disk space issues and keep logs manageable.
4. Regularly Review Audit Logs:

    - Use ```ausearch``` and ```aureport``` to review key activities, especially those related to sensitive files or privileged users.
5. Enable Audit Rules for Compliance:

    - Use Auditd for regulatory compliance by monitoring and recording access to sensitive data as required by standards like PCI-DSS and HIPAA.
6. Use Permissive Mode for Testing:

    - Test new rules in a permissive environment before deploying in production to avoid unintentional disruptions.
## Final Notes
- Auditd is a powerful tool for monitoring and logging system activity, crucial for security and compliance on Linux systems.
- Best Practices: Set targeted audit rules, use ```key``` tags for easier log analysis, and regularly review logs to detect suspicious activities and prevent unauthorized access.