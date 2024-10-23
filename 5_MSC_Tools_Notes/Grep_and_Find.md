# Grep and Find Notes
## Overview
Grep and Find are powerful command-line tools in Unix/Linux environments for searching files and directories. Grep searches for patterns within files, while Find locates files and directories based on various criteria.

## Grep (Global Regular Expression Print)
1. Basic Usage
    - Description: Grep searches for specific patterns in files or outputs.
    - Usage:

            grep "pattern" file.txt     # Search for "pattern" in a file
2. Recursive Search
    - Description: Search for a pattern across multiple files in directories.
    - Usage:

            grep -r "pattern" /path/to/directory   # Recursive search in a directory
3. Case-Insensitive Search
    - Description: Ignore case when searching for patterns.
    - Usage:

            grep -i "pattern" file.txt   # Case-insensitive search
4. Display Line Numbers
    - Description: Show line numbers for matched patterns.
    - Usage:

            grep -n "pattern" file.txt   # Show line numbers with matches
## Find (File Search)
1. Basic Usage
    - Description: Find locates files and directories based on name, type, or attributes.
    - Usage:

            find /path/to/dir -name "filename"     # Search for a file by name
2. Search by File Type
    - Description: Search for files of a specific type (e.g., regular files, directories).
    - Usage:

            find /path/to/dir -type d              # Find directories
            find /path/to/dir -type f              # Find regular files
3. Search by Size
    - Description: Find files larger or smaller than a given size.
    - Usage:

            find /path/to/dir -size +100M          # Find files larger than 100MB
4. Execute a Command
    - Description: Perform an action on the results of the find command.
    - Usage:

            find /path/to/dir -name "*.log" -exec rm {} \;   # Delete all .log files

## Final Notes
- Grep is used for searching within files, while Find locates files and directories based on various attributes.
- Both commands are essential for file management and pattern searching in Unix/Linux systems.
