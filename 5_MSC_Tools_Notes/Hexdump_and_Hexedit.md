# Hexdump and Hexedit Notes
## Overview
Hexdump and Hexedit are tools for viewing and editing binary files in hexadecimal format. These tools are essential for low-level file analysis, allowing developers and system administrators to examine raw file contents, diagnose issues, or make manual changes to binary data.

## Hexdump
1. Basic Usage
    - Description: Hexdump displays the contents of a file in hexadecimal, decimal, or ASCII format.
    - Usage:

            hexdump file.bin                # Display file contents in hex
2. Display in Canonical Hex/ASCII Format
    - Description: Shows both the hex values and their ASCII representations side by side.
    - Usage:

            hexdump -C file.bin             # Display hex and ASCII values together
3. Specify Number of Bytes to Display
    - Description: Limit the number of bytes shown from the file.
    - Usage:

            hexdump -n 100 file.bin         # Display the first 100 bytes of the file
4. Display in 2, 4, or 8 Byte Words
    - Description: Control the number of bytes grouped together.
    - Usage:

            hexdump -e '2/2 "%04X " "\n"' file.bin  # Display file as 2-byte hex words
5. Display in Decimal or Octal Format
    - Description: Show the file’s contents in alternative number systems.
    - Usage:

            hexdump -d file.bin             # Display file in decimal format
            hexdump -o file.bin             # Display file in octal format
6. Skip Bytes
    - Description: Skip a certain number of bytes before displaying the file content.
    - Usage:

            hexdump -s 100 file.bin         # Skip the first 100 bytes

## Hexedit
1. Basic Usage
    - Description: Hexedit is an interactive command-line tool used to view and modify the contents of binary files in hexadecimal format.
    - Usage:

            hexedit file.bin                # Open file in hexedit for viewing/editing
2. Navigating in Hexedit
    - Description: Move through the file using arrow keys to browse its contents.
        - Up/Down Arrow: Move up and down one row.
        - Left/Right Arrow: Move left and right across the hex values.
        - Page Up/Page Down: Scroll one page up or down.
    - Usage:

            # Open hexedit and navigate using the keyboard
            hexedit file.bin
3. Editing Bytes
    - Description: Edit hex values directly within Hexedit. Type over existing hex values to modify the file.
    - Usage:
        - Move the cursor to the desired location and type the new hex values.
4. Switch Between Hex and ASCII Mode
    - Description: Toggle between hex value editing and ASCII representation editing using the Tab key.
    - Usage:

            # Press Tab to toggle between editing hex values and ASCII characters
5. Search for Hex or ASCII Strings
    - Description: Search for specific values or text within the file.
        - Use Ctrl+S to search for a hex value or ASCII string.
    - Usage:

            Ctrl + S                     # Open search in Hexedit
            # Enter the hex value or text string you want to search
6. Quit Hexedit
    - Description: Exit Hexedit by pressing Ctrl+X.
    - Usage:

            Ctrl + X                     # Quit Hexedit

## Common Use Cases
1. Examining Binary Files
    - Hexdump allows you to examine binary files such as executables, images, or firmware in hexadecimal format to understand their structure.
    - Example:

            hexdump -C program.exe        # View the raw binary structure of an executable
2. Editing Binary Files
    - Hexedit is useful when you need to manually modify a binary file for reverse engineering, patching software, or fixing corruption.
    - Example:

            hexedit firmware.bin          # Open a firmware file for editing specific bytes
3. Searching for Patterns in Files
    - You can search for specific hex values or text patterns in binary files using Hexedit, allowing you to locate specific data chunks.
    - Example:

            Ctrl + S                     # Search for "FF D8 FF" (JPEG header) in a binary file
## Final Notes
- Hexdump is ideal for viewing file contents in hexadecimal, while Hexedit enables interactive viewing and editing.
- Best Practices: Always back up files before editing with Hexedit, as modifying binary data can corrupt files if done incorrectly.