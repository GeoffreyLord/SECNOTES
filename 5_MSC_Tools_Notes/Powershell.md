# Common PowerShell Commands Notes
## Overview
PowerShell is a task automation and configuration management framework from Microsoft, consisting of a command-line shell and associated scripting language. It’s widely used for automating administrative tasks on Windows, and it can interact with files, processes, and system settings, making it powerful for system administrators and developers.

## File and Directory Operations
1. Get-ChildItem (List Files)
    - Description: Lists files and directories (similar to ```ls``` in Bash).
    - Usage:

            Get-ChildItem            # List files in the current directory
            Get-ChildItem -Recurse    # List files recursively in all subdirectories
2. Set-Location (Change Directory)
    - Description: Changes the current working directory (similar to ```cd```).
    - Usage:

            Set-Location C:\Path\To\Directory   # Change to a specified directory
3. Get-Location (Print Working Directory)
    - Description: Displays the current working directory (similar to ```pwd```).
    - Usage:

            Get-Location   # Show current directory path
4. Copy-Item (Copy Files/Directories)
    - Description: Copies files or directories (similar to ```cp```).
    - Usage:

            Copy-Item -Path source.txt -Destination C:\Path\   # Copy a file
            Copy-Item -Recurse -Path C:\Source\ -Destination C:\Target\   # Copy a directory recursively
5. Move-Item (Move/Rename Files)
    - Description: Moves or renames files or directories (similar to ```mv```).
    - Usage:

            Move-Item -Path oldname.txt -Destination newname.txt    # Rename a file
            Move-Item -Path file.txt -Destination C:\NewDirectory   # Move a file to another directory
6. Remove-Item (Remove Files/Directories)
    - Description: Deletes files or directories (similar to ```rm```).
    - Usage:

            Remove-Item -Path file.txt    # Delete a file
            Remove-Item -Recurse -Path C:\Directory\   # Delete a directory recursively

## Viewing and Editing Files
1. Get-Content (Display File Content)
    - Description: Displays the contents of a file (similar to ```cat```).
    - Usage:

            Get-Content file.txt   # Display file content
2. Out-File (Write to a File)
    - Description: Sends output to a file (similar to redirection ```>``` in Bash).
    - Usage:

            Get-Process | Out-File processes.txt   # Write command output to a file
3. Set-Content (Write or Overwrite File)
    - Description: Writes or replaces content in a file.
    - Usage:

            Set-Content file.txt -Value "Hello, World"   # Write text to a file

## Process Management
1. Get-Process (List Processes)
    - Description: Displays information about running processes (similar to ```ps```).
    - Usage:

            Get-Process   # Show running processes
2. Stop-Process (Kill Processes)
    - Description: Stops a running process by its name or ID (similar to ```kill```).
    - Usage:

            Stop-Process -Id 1234   # Kill a process by its ID
            Stop-Process -Name notepad   # Kill a process by its name

## File Permissions and Ownership
1. Get-Acl (Get File Permissions)
    - Description: Retrieves the access control list (ACL) for a file or directory.
    - Usage:

            Get-Acl C:\Path\To\File   # Show file permissions
2. Set-Acl (Set File Permissions)
    - Description: Modifies the permissions of a file or directory.
    - Usage:

            $acl = Get-Acl "C:\Path\To\File"
            $acl.SetAccessRuleProtection($true, $false)
            Set-Acl -Path "C:\Path\To\File" -AclObject $acl   # Apply new permissions

## Networking
1. Test-Connection (Ping Host)
    - Description: Sends ICMP packets to test network connectivity (similar to ```ping```).
    - Usage:

            Test-Connection google.com   # Ping a host
2. Invoke-WebRequest (Download/Send Data from URLs)
    - Description: Transfers data to/from URLs (similar to ```curl```).
    - Usage:

            Invoke-WebRequest http://example.com   # Download content from a URL
3. Get-NetIPConfiguration (View Network Configuration)
    - Description: Displays detailed network configuration (similar to ```ifconfig```).
    - Usage:

            Get-NetIPConfiguration   # Show network interface configuration

## System Information
1. Get-Disk (Disk Information)
    - Description: Displays information about physical disks.
    - Usage:

            Get-Disk   # Show disk details
2. Get-ComputerInfo (System Information)
    - Description: Retrieves detailed system information.
    - Usage:

            Get-ComputerInfo   # Show system info (OS, memory, processor)
3. Get-EventLog (View Event Logs)
    - Description: Retrieves event logs from the system.
    - Usage:

            Get-EventLog -LogName System   # Show system event logs

## Final Notes
- PowerShell is a versatile shell for managing files, directories, processes, and system configurations on Windows.
- Best Practices: Make use of PowerShell’s pipeline feature to combine commands for powerful scripting and automation.
