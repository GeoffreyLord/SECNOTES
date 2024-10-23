
# Common Bash Commands Notes
Overview
Bash (Bourne Again Shell) is a command-line interpreter used in Unix-based operating systems like Linux and macOS. It allows users to interact with the system, run scripts, and automate tasks. Mastering common Bash commands helps efficiently manage files, directories, processes, and system configurations.

## File and Directory Operations
1. ls (List Files)
    - Description: Lists files and directories in the current working directory.
    - Usage:

            ls        # List files in the current directory
            ls -la    # List files with detailed information, including hidden files
2. cd (Change Directory)
    - Description: Changes the current working directory.
    - Usage:

            cd /path/to/directory   # Move to a specific directory
            cd ..                   # Move one directory up
            cd ~                    # Move to the home directory
3. pwd (Print Working Directory)
    - Description: Displays the full path of the current directory.
    - Usage:

            pwd   # Print current directory path
4. cp (Copy Files/Directories)
    - Description: Copies files or directories.
    - Usage:

            cp source.txt destination.txt      # Copy a file
            cp -r /source/directory /target/   # Copy a directory recursively
5. mv (Move/Rename Files)
    - Description: Moves or renames files or directories.
    - Usage:

            mv oldname.txt newname.txt         # Rename a file
            mv file.txt /path/to/directory     # Move a file to another directory
6. rm (Remove Files/Directories)
    - Description: Deletes files or directories.
    - Usage:

            rm file.txt             # Delete a file
            rm -r directory/        # Delete a directory recursively

## Viewing and Editing Files
1. cat (Concatenate and Display File Content)
    - Description: Displays the content of a file.
    - Usage:

            cat file.txt            # Display the content of a file
2. less (View File Content Page-by-Page)
    - Description: Opens a file in a scrollable view.
    - Usage:

            less file.txt           # View file with pagination
3. nano (Text Editor)
    - Description: Opens a file in the nano text editor.
    - Usage:

            nano file.txt           # Edit a file with nano

## Process Management
1. ps (List Processes)
    - Description: Displays information about running processes.
    - Usage:

            ps aux                  # Show all running processes with detailed information
2. top (Monitor Processes)
    - Description: Displays active processes in real-time.
    - Usage:

            top                     # Show real-time system processes and resource usage
3. kill (Terminate Processes)
    - Description: Kills a running process by its process ID (PID).
    - Usage:

            kill PID                # Terminate a specific process by its PID
            kill -9 PID             # Forcefully terminate a process
## File Permissions
1. chmod (Change File Permissions)
    - Description: Changes the read, write, and execute permissions of a file or directory.
    - Usage:

            chmod 755 script.sh     # Set permissions (rwxr-xr-x)
            chmod +x script.sh      # Add execute permission to a script
2. chown (Change File Owner)
    - Description: Changes the owner and group of a file or directory.
    - Usage:

            chown user:group file   # Change the owner of a file

## Networking
1. ping (Check Network Connectivity)
    - Description: Sends packets to a specified host to check network connectivity.
    - Usage:

            ping google.com         # Ping a host to check if it's reachable
2. curl (Transfer Data from URLs)
    - Description: Transfers data from or to a server, commonly used for downloading or testing APIs.
    - Usage:

            curl http://example.com # Retrieve data from a URL
3. ifconfig (View Network Configuration)
    - Description: Displays network interface configuration details.
    - Usage:

            ifconfig                # Show network interface configuration

## System Information
1. df (Disk Usage)
    - Description: Displays available disk space on mounted file systems.
    - Usage:

            df -h                   # Show disk usage in human-readable format
2. du (Directory Size)
    - Description: Displays the disk usage of a directory or file.
    - Usage:

            du -sh /path/to/dir     # Show total size of a directory
3. uname (System Information)
    - Description: Displays system information like the kernel version and OS type.
    - Usage:

            uname -a                # Show detailed system information

## Final Notes
- Bash commands are essential for managing files, directories, processes, and system configurations in Linux and macOS environments.
- Best Practices: Always double-check commands that modify or delete files (rm, mv) and use caution when modifying file permissions or running processes as the root user (sudo).