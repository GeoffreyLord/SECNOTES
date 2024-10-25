# User and Group Management Notes
## Overview
User and group management is essential for controlling access on Linux systems. Properly adding, deleting, and modifying users and groups ensures security and helps maintain organized system permissions. Commands such as ```useradd```, ```usermod```, ```userdel```, ```groupadd```, and ```groupdel``` allow system administrators to create, manage, and remove users and groups.

## User Management Commands
1. Adding a New User (useradd)
    - Description: Creates a new user account and a home directory if specified.
    - Usage:

            sudo useradd -m username             # Create user with a home directory
            sudo useradd -m -s /bin/bash username  # Specify shell (e.g., bash)
    - Key Options:
        - ```-m```: Creates a home directory for the user.
        - ```-s```: Sets the user’s default shell (e.g., ```/bin/bash```, ```/bin/sh```).
        - ```-d```: Specifies a custom home directory path.
2. Setting a User Password (passwd)
    - Description: Sets or updates the password for a user account.
    - Usage:

            sudo passwd username                 # Set or change password for a user
3. Modifying a User (usermod)
    - Description: Edits user attributes such as username, home directory, and group memberships.
    - Usage:

            sudo usermod -l newname oldname      # Change username
            sudo usermod -d /new/home username   # Change home directory
            sudo usermod -aG groupname username  # Add user to an additional group
    - Key Options:
        - ```-l```: Changes the username.
        - ```-d```: Updates the home directory location.
        - ```-aG```: Adds the user to a supplementary group (use ```-a``` to avoid overwriting existing groups).
4. Deleting a User (userdel)
    - Description: Removes a user account and optionally their home directory.
    - Usage:

            sudo userdel username                # Delete user account only
            sudo userdel -r username             # Delete user and their home directory
    - Key Options:
        - ```-r```: Removes the user’s home directory and mail spool.
5. Viewing User Details
    - Description: Display information about a user, including their groups and home directory.
    - Usage:

            id username                          # Show user ID, group ID, and groups
            getent passwd username               # Display user’s details from /etc/passwd

## Group Management Commands
1. Adding a New Group (groupadd)
    - Description: Creates a new group.
    - Usage:

            sudo groupadd groupname              # Create a new group
    - Key Options:
        - ```-g GID```: Assign a specific group ID (GID).
2. Modifying a Group (groupmod)
    - Description: Updates group attributes such as group name and GID.
    - Usage:

        - sudo groupmod -n newgroup oldgroup   # Rename a group
        - sudo groupmod -g 1050 groupname      # Change GID for a group
3. Deleting a Group (groupdel)
    - Description: Removes a group from the system.
    - Usage:

        - sudo groupdel groupname              # Delete the group
4. Adding a User to a Group
    - Description: Adds an existing user to a group, granting them additional permissions.
    - Usage:

            sudo usermod -aG groupname username  # Add user to an additional group

## Common Use Cases
1. Creating a User with a Home Directory and Shell
    - Example: Create a user named ```jdoe``` with a home directory and bash shell.

            sudo useradd -m -s /bin/bash jdoe
            sudo passwd jdoe                       # Set password for the user
2. Creating a Group and Adding Users to It
    - Example: Create a group named ```developers``` and add ```jdoe``` and ```asmith``` to it.

            sudo groupadd developers
            sudo usermod -aG developers jdoe
            sudo usermod -aG developers asmith
3. Deleting a User and Their Home Directory
    - Example: Remove user ```jdoe``` and delete their home directory.

            sudo userdel -r jdoe
4. Renaming a User and Updating Their Home Directory
    - Example: Change the username ```jdoe``` to ```john``` and their home directory to ```/home/john```.

            sudo usermod -l john jdoe
            sudo usermod -d /home/john -m john
5. Viewing All Users in a Group
    - Example: Check which users belong to the ```developers``` group.

        getent group developers

## Key Configuration Files
1. /etc/passwd
    - Description: Contains user account information such as usernames, UIDs, GIDs, home directories, and shells.
    - Usage:

            cat /etc/passwd              # View all user entries
2. /etc/shadow
    - Description: Stores encrypted user passwords and password policies (e.g., expiration). Requires root access to view.
    - Usage:

            sudo cat /etc/shadow          # View encrypted passwords (root only)
3. /etc/group
    - Description: Lists groups, GIDs, and group memberships.
    - Usage:

            cat /etc/group               # View all group entries

## Best Practices
1. Use Strong Passwords for User Accounts:

    - Set and enforce password policies to ensure user account security.
2. Add Users to Groups for Permission Management:

    - Use groups to manage permissions rather than assigning permissions individually for easier and scalable access control.
3. Avoid Deleting Users without Backups:

    - Always verify and backup any user data before deleting accounts, especially with the -r option.
4. Use the Least Privilege Principle:

    - Only assign necessary permissions by limiting users to relevant groups and system access.
5. Regularly Review /etc/passwd and /etc/group Files:

    - Periodically check system users and groups for unexpected accounts or group memberships.

## Final Notes
- User and group management is essential for Linux system administration, helping to control access and permissions efficiently.
- Best Practices: Use groups for managing permissions, apply least privilege principles, and ensure strong passwords and backup processes are in place.