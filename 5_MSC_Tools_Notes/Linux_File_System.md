# Linux File System Notes
## Overview
The Linux file system is a structured hierarchy of directories that organizes files and folders. It follows the Filesystem Hierarchy Standard (FHS), providing a consistent structure across Linux distributions. The root directory ```/``` is the starting point, with all other directories branching from it. Understanding the Linux file system helps with managing files, permissions, and system resources.

## Key Directories
1. Root Directory (```/```)
    - Description: The top-level directory containing all other directories and files on the system.
    - Usage:
        - Serves as the starting point for the entire file system hierarchy.
2. /bin (Binary Executables)
    - Description: Contains essential command binaries like ```ls```, ```cp```, ```mv```, and ```bash```. These commands are available to all users and are required for system boot.

3. /sbin (System Binaries)
    - Description: Contains essential system administration binaries like ```ip```, ```iptables```, and ```fsck```, usually reserved for the root user.

4. /etc (Configuration Files)
    - Description: Holds system-wide configuration files and shell scripts for various services and applications.
        - Files like ```/etc/fstab```, ```/etc/hosts```, and ```/etc/passwd``` are stored here.

5. /home (User Home Directories)
    - Description: Contains a subdirectory for each user, where personal files and settings are stored (e.g., ```/home/username```).

6. /root (Root User’s Home Directory)
    - Description: Home directory for the root user, separate from ```/home``` for security purposes.

7. /var (Variable Data Files)
    - Description: Stores files that frequently change, such as logs, mail, and spool files. Contains subdirectories like ```/var/log```, ```/var/spool```, and ```/var/tmp```.

8. /tmp (Temporary Files)
    - Description: Temporary storage for files created by users and applications. Contents are often deleted on reboot.

9. /usr (User Binaries and Application Files)
    - Description: Contains secondary files and applications for users. It includes:
        - ```/usr/bin```: General command binaries.
        - ```/usr/sbin```: System administration binaries.
        - ```/usr/local```: Locally installed software.

10. /opt (Optional Software)
    - Description: Used for third-party software and optional applications not included by default with the system.

11. /dev (Device Files)
    - Description: Contains device files that represent hardware components (e.g., ```/dev/sda``` for a hard disk).

12. /proc (Process and System Information)
    - Description: A virtual filesystem providing process and system information, such as memory, CPU, and running processes. Files here are dynamically generated.

13. /sys (System Files)
    - Description: Another virtual filesystem that provides information about the kernel, devices, and system hardware, typically used for system diagnostics.

14. /lib (Libraries)
    - Description: Contains essential shared libraries needed by binaries in ```/bin``` and ```/sbin```. For example, ```libc.so``` for C library functions.

15. /mnt and /media (Mount Points)
    - Description:
        - ```/mnt```: Temporary mount point for filesystems, typically used by system administrators.
        - ```/media```: Automatically created directories for removable devices, such as USB drives or CDs.

## Common Commands for File System Management
1. Mount and Unmount Filesystems (mount/umount)
    - Description: Mounts or unmounts filesystems, such as external drives.
    - Usage:

            sudo mount /dev/sdb1 /mnt/usb      # Mount a device to /mnt/usb
            sudo umount /mnt/usb               # Unmount the device

## File System Types
- ext4: Default Linux filesystem with journaling and high reliability.
- xfs: High-performance filesystem, commonly used in enterprise systems.
- vfat: Compatible with Windows systems, used for flash drives.
- ntfs: Windows NT Filesystem, readable by Linux but often not writable without ```ntfs-3g```.
- tmpfs: Temporary filesystem stored in memory, used for temporary storage like ```/tmp```.

## Important Configuration Files
1. /etc/fstab
    - Description: Defines the filesystems to mount at boot, including mount points, filesystem types, and options.
    - Example:

            cat /etc/fstab               # View all filesystems and their mount points
2. /etc/mtab
    - Description: Lists currently mounted filesystems, dynamically updated.
    - Usage:

            cat /etc/mtab                # View currently mounted filesystems
3. /proc/mounts
    - Description: Virtual file that shows active mounts, similar to ```/etc/mtab```.
    - Usage:

            cat /proc/mounts             # View active mounts

## Best Practices
1. Organize Files According to the FHS:

    - Place configuration files in ```/etc```, user files in ```/home```, and executables in ```/bin``` or ```/usr/bin``` for consistency.

2. Use ```/mnt``` and ```/media``` for Mounting:

    - Use ```/mnt``` for temporary mounts and ```/media``` for removable devices to follow conventions.
3. Monitor Disk Usage Regularly:

    - Use ```df``` and ```du``` to monitor disk space, especially in ```/var``` and ```/home```, which can fill up quickly.
4. Back Up Important Configuration Files:

    - Keep backups of essential files like ```/etc/fstab```, ```/etc/passwd```, and ```/etc/shadow``` to recover from accidental changes.
5. Avoid Changing Permissions on System Directories:

    - Changing permissions on directories like ```/bin```, ```/sbin```, or ```/lib``` can cause security issues or break system functionality.

## Final Notes
- Linux file system organization is key to efficient system administration, allowing users and administrators to navigate, manage, and secure files effectively.
- Best Practices: Follow FHS guidelines, monitor disk usage, and avoid modifying critical system directories unnecessarily.