# GDB (GNU Debugger) Notes
## Overview
GDB (GNU Debugger) is a powerful debugging tool for programs written in languages like C, C++, and Fortran. It allows developers to see what is happening inside a program while it is running or what it was doing just before it crashed. GDB enables you to inspect variables, control execution, and analyze program behavior in detail.

## Basic GDB Commands
1. Starting GDB
    - Description: Launch GDB with an executable or attach it to a running process.
    - Usage:

            gdb ./program               # Start GDB with the program executable
            gdb ./program core           # Start GDB with a core dump file
            gdb -p <pid>                 # Attach GDB to a running process by PID
2. Running a Program
    - Description: Start or rerun the program inside GDB.
    - Usage:

            run [args]                   # Start the program with optional arguments
r                            # Shortcut for run
3. Quitting GDB
    - Description: Exit GDB.
    - Usage:

            quit                         # Exit GDB

## Breakpoints and Watchpoints
1. Setting Breakpoints
    - Description: Pause the execution of the program at a specific line, function, or address.
    - Usage:

            break [file:]line_number      # Set a breakpoint at a specific line
            break function_name           # Set a breakpoint at a function
            b main                        # Shortcut for setting a breakpoint in main function
2. Listing Breakpoints
    - Description: Show all breakpoints currently set.
    - Usage:

            info breakpoints              # List all breakpoints
3. Deleting Breakpoints
    - Description: Remove a specific or all breakpoints.
    - Usage:

            delete N                      # Delete breakpoint number N
            delete                        # Delete all breakpoints
4. Watchpoints
    - Description: Stop execution when a specific variable or memory location changes.
    - Usage:

            watch variable                 # Watch a variable for changes

## Controlling Program Execution
1. Continue Execution
    - Description: Resume the program’s execution after it stops at a breakpoint.
    - Usage:

            continue                      # Continue execution until the next breakpoint
            c                             # Shortcut for continue
2. Step Through Code
    - Description: Execute the program line-by-line.
        - step enters function calls, while next skips over them.
    - Usage:

            step                          # Step into functions
            next                          # Step over functions
3. Finish Function Execution
    - Description: Continue execution until the current function returns.
    - Usage:

            finish                        # Execute until the current function returns
4. Jump to a Line
    - Description: Jump to a specific line of code without executing intermediate lines.
    - Usage:

            jump line_number              # Jump to a specific line in the current function

## Inspecting Variables and Memory
1. Printing Variables
    - Description: Display the value of a variable or expression.
    - Usage:

            print variable                 # Print the value of a variable
            p variable                     # Shortcut for print
            print/x variable               # Print in hexadecimal format
2. Inspecting Local Variables
    - Description: Show all local variables in the current function.
    - Usage:

            info locals                    # Show all local variables
3. Examining Memory
    - Description: Display raw memory contents at a given address.
    - Usage:

            x/Nf address                   # Examine memory at an address (N = number of units, f = format)
            x/10x $esp                     # Example: Display 10 words in hexadecimal starting from $esp
4. Backtrace
    - Description: Show the current call stack.
    - Usage:

            backtrace                      # Display the call stack
            bt                             # Shortcut for backtrace
5. Frame
    - Description: Switch to a specific stack frame in the call stack.
    - Usage:

            frame N                        # Switch to frame number N

## GDB Scripting and Commands
1. Define Custom Commands
    - Description: Define custom GDB commands for common tasks.
    - Usage:

            define mycommand               # Start defining a command
            commands...                    # Add your commands here
            end                            # End command definition
2. Run Shell Commands
    - Description: Execute shell commands from inside GDB.
    - Usage:

            shell ls                       # Run shell command (e.g., `ls`) from within GDB

## Debugging Optimized Code
1. Set Debug Info during Compilation
    - Description: Compile with debugging information enabled to use GDB effectively.
    - Usage:

            gcc -g -O0 source.c -o program  # Compile with debug info (-g) and without optimization (-O0)

## Final Notes
- GDB is essential for debugging low-level issues in C/C++ and other compiled languages.
- Best Practices: Use breakpoints strategically and inspect variables regularly to understand program state during execution.