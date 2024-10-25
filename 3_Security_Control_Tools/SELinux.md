# SELinux (Security-Enhanced Linux) Notes
## Overview
SELinux (Security-Enhanced Linux) is a security architecture integrated into the Linux kernel that enforces mandatory access control (MAC) policies to enhance system security. Unlike traditional discretionary access control (DAC), SELinux policies restrict processes and users based on rules that cannot be changed by individual users, offering more granular and strict security.

SELinux is commonly found in Linux distributions like Red Hat, CentOS, and Fedora, where it is used to secure applications, network services, and other system processes.

## Key Concepts
1. Modes of Operation
    - Description: SELinux can run in different modes to control the enforcement of its policies.
        - Enforcing: Actively enforces SELinux policies, denying access based on policy rules.
        - Permissive: Logs actions that would be denied in enforcing mode but does not block them. Useful for troubleshooting.
        - Disabled: Completely disables SELinux.
    - Usage:

            # Temporarily change mode
            sudo setenforce 1             # Set to enforcing
            sudo setenforce 0             # Set to permissive

            # Check current mode
            getenforce                    # Shows current SELinux mode
2. SELinux Contexts
    - Description: Every file, process, and user in an SELinux-enabled system has a context label, which defines permissions based on SELinux policies.
        - User: The SELinux user associated with the object (e.g., ```system_u```).
        - Role: Defines roles (e.g., ```object_r```) that processes or files can take.
        - Type: The type (e.g., ```httpd_t```, ```var_t```) is the most critical part and controls access permissions.
        - Level: Optional multi-level security (MLS) field.
    - Usage:

            ls -Z /path/to/file           # Display SELinux context for files
            ps -eZ                         # Show SELinux context for running processes
3. SELinux Policies
    - Description: Define the rules governing access control. The two main policies are:
        - Targeted: Applies SELinux protection to a targeted set of processes (default in most distributions).
        - MLS (Multi-Level Security): A strict policy with enhanced security controls.
    - Usage:

            sestatus                      # Check active policy and SELinux status
4. Types of Access Control
    - Description: SELinux enforces multiple types of access control:
        - Type Enforcement (TE): Restricts interactions between different types, focusing on process and file types.
        - Role-Based Access Control (RBAC): Manages access based on user roles.
        - Multi-Level Security (MLS): Manages access based on classification levels (e.g., Confidential, Secret).

## Basic Commands
1. Checking SELinux Status
    - Description: Displays the current SELinux status and policy.
    - Usage:

            sestatus                      # Show SELinux status, mode, and policy
2. Changing SELinux Mode Temporarily
    - Description: Temporarily switches SELinux between enforcing and permissive modes.
    - Usage:

            sudo setenforce 1             # Enable enforcing mode
            sudo setenforce 0             # Enable permissive mode
3. Permanently Changing SELinux Mode
    - Description: Change SELinux mode persistently across reboots by editing the configuration file.
    - Usage:

            sudo vi /etc/selinux/config   # Edit SELinux configuration
            # Set SELINUX=enforcing, permissive, or disabled
4. Viewing and Setting SELinux Contexts
    - Description: Display or modify the SELinux context of files or directories.
    - Usage:

            ls -Z /path/to/file           # View SELinux context of a file
            chcon -t httpd_sys_content_t /var/www/html  # Temporarily change context for web content
5. Restoring Default SELinux Context
    - Description: Reapply default SELinux contexts to files and directories if modified.
    - Usage:

            restorecon -v /path/to/file_or_directory   # Restore default SELinux context

## Common Use Cases
1. Securing Web Server Files
    - Description: Set the appropriate SELinux type for web content so the HTTPD process can access it.
    - Example:

            chcon -R -t httpd_sys_content_t /var/www/html  # Allow HTTPD to access web files
2. Troubleshooting Access Issues
    - Description: Temporarily switch to permissive mode to log (but not enforce) denied actions, which aids troubleshooting.
    - Example:

            sudo setenforce 0             # Set to permissive mode to identify issues
3. Allowing Services to Use Non-Default Ports
    - Description: Update SELinux rules to allow services to run on custom ports.
    - Example:

            sudo semanage port -a -t http_port_t -p tcp 8080   # Allow HTTPD on port 8080
4. Checking and Adjusting File Contexts
    - Description: Ensure files have the correct SELinux contexts, especially after moving or copying files.
    - Example:

            restorecon -R /var/www/html   # Restore default context for web files

## Useful Tools and Commands
1. audit2allow
    - Description: Generates SELinux policy rules from denial messages in the audit log.
    - Usage:

            grep "avc:  denied" /var/log/audit/audit.log | audit2allow -M mypolicy   # Generate custom policy
            sudo semodule -i mypolicy.pp                                            # Install custom policy
2. semanage
    - Description: Manages SELinux configurations, such as port rules, file contexts, and more.
    - Usage:

            semanage port -l                  # List all SELinux port rules
            semanage fcontext -a -t httpd_sys_content_t "/mydir(/.*)?"  # Add custom file context
3. getsebool and setsebool
    - Description: View and configure SELinux booleans, which control permissions for specific actions (e.g., allowing HTTPD to connect to databases).
    - Usage:

            getsebool -a                      # List all SELinux booleans
            sudo setsebool httpd_can_network_connect_db on   # Allow HTTPD to connect to databases
4. ausearch
    - Description: Searches audit logs for SELinux denial messages.
    - Usage:

            ausearch -m avc -ts today         # Show today’s SELinux denials

## Best Practices
1. Use Enforcing Mode for Production:

    - Run SELinux in enforcing mode on production servers to ensure policies are strictly applied.
2. Apply the Principle of Least Privilege:

    - Only enable necessary SELinux booleans and ports, and apply the minimum required contexts for each service.
3. Utilize Permissive Mode for Troubleshooting:

    -   Switch to permissive mode temporarily when troubleshooting, then review audit logs for necessary policy adjustments.
4. Regularly Check Contexts and Restore Defaults:

    - Use ```restorecon``` to ensure files and directories retain their proper contexts, especially after updates or migrations.
5. Use audit2allow for Custom Policies:

    - Generate custom policies with ```audit2allow``` if necessary, based on specific application needs reflected in denial logs.

## Final Notes
- SELinux is a powerful MAC system that provides an additional layer of security in Linux by enforcing strict access controls. Although it may seem complex, understanding its key features and configuration commands helps maintain a secure system.
- Best Practices: Run in enforcing mode in production, use permissive mode for troubleshooting, and manage SELinux contexts carefully to avoid unintended access issues.