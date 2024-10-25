
# Nmap (Network Mapper) Notes

## Overview
Nmap (Network Mapper) is a powerful open-source tool for network discovery and security auditing. It is widely used for mapping networks, identifying open ports, discovering services, and detecting operating systems on network devices. Nmap can be used for routine network maintenance as well as in-depth security assessments.

## Key Features of Nmap
1. Port Scanning
    - Description: Scans target hosts for open ports, allowing you to determine which services are running.
    - Usage:

            nmap target_ip            # Basic port scan
            nmap -p 1-65535 target_ip  # Scan all 65535 ports
    - Key Benefits:
        - Identifies open ports and running services, helping detect potential security entry points.
2. Service Version Detection
    - Description: Determines the version of services running on open ports, providing more detailed information about potential vulnerabilities.
    - Usage:

            nmap -sV target_ip        # Enable service version detection
    - Key Benefits:
        - Helps identify outdated or vulnerable services.
3. Operating System Detection
    - Description: Identifies the operating system and version running on a target host.
    - Usage:

            nmap -O target_ip         # Enable OS detection
    - Key Benefits:
        - Provides valuable insight into the host system for targeted vulnerability assessments.
4. Network Discovery (Ping Scan)
    - Description: Discovers live hosts on a network by sending ICMP echo requests, TCP, or UDP packets.
    - Usage:

            nmap -sn network_range    # Ping scan to discover live hosts
    - Key Benefits:
        - Useful for quickly mapping active devices on a network.
5. Scriptable Scanning with NSE (Nmap Scripting Engine)
    - Description: Uses pre-built or custom scripts to perform detailed scans and vulnerability checks.
    - Usage:

            nmap --script http-vuln* target_ip   # Run vulnerability scripts against a host
    - Key Benefits:
        - Automates vulnerability detection for services and protocols using custom and built-in scripts.
6. Aggressive Scanning
    - Description: Combines multiple scanning options, including OS detection, version detection, script scanning, and traceroute.
    - Usage:

            nmap -A target_ip         # Run an aggressive scan
    - Key Benefits:
        - Provides comprehensive information about a target host in a single scan.

## Common Use Cases
1. Identify Open Ports on a Host
    - Port Scanning: Determine which ports are open on a server or endpoint.
    - Example:

            nmap -p 1-1000 target_ip   # Scan the first 1000 ports
2. Map All Devices on a Network
    - Network Discovery: Discover all live hosts on a subnet for network inventory or security assessments.
    - Example:

            nmap -sn 192.168.1.0/24    # Discover live hosts on a 192.168.1.0/24 network
3. Detect Service Versions for Vulnerability Assessment
    - Service Version Detection: Identify versions of running services to assess for known vulnerabilities.
    - Example:

            nmap -sV target_ip         # Determine service versions on open ports
4. Automated Vulnerability Scanning
    - Nmap Scripting Engine (NSE): Run vulnerability scripts to scan for common issues.
    - Example:

            nmap --script vuln target_ip   # Run all vulnerability scripts
5. Identify Operating Systems on Hosts
    - OS Detection: Determine the operating system of devices on the network to understand potential vulnerabilities.
    - Example:

            nmap -O target_ip            # Detect OS of the target

## Key Commands and Options
1. Basic Port Scan
    - Description: Scans for open ports on the default range (1-1000).
    - Usage:

            nmap target_ip
2. Full Port Scan
    - Description: Scans all 65535 TCP ports.
    - Usage:

            nmap -p- target_ip
3. Service Version Detection
    - Description: Detects versions of services on open ports.
    - Usage:

            nmap -sV target_ip
4. Operating System Detection
    - Description: Determines the OS of the target.
    - Usage:

            nmap -O target_ip
5. Aggressive Scan
    - Description: Runs a combination of OS detection, service detection, and NSE scripts.
    - Usage:

            nmap -A target_ip
6. Scan a Specific Port Range
    - Description: Scans only the specified range of ports.
    - Usage:

            nmap -p 80,443,8080 target_ip      # Scan specific ports
            nmap -p 1-1000 target_ip           # Scan ports 1 through 1000
7. Use Nmap Scripting Engine (NSE)
    - Description: Execute a specific script or script category.
    - Usage:

            nmap --script http-vuln* target_ip   # Run all HTTP vulnerability scripts
            nmap --script vuln target_ip         # Run general vulnerability scripts

## Interpreting Results
- Open Ports: Ports marked as ```open``` indicate active services that may need further security evaluation.
- Closed Ports: Ports marked as ```closed``` do not have active services but may respond to a scan.
- Filtered Ports: Ports marked as ```filtered``` are behind a firewall or other filtering device, which blocks access.

## Best Practices
1. Use Targeted Scans:

    - Only scan necessary hosts and ports to avoid unnecessary network load.
2. Combine Scans with NSE Scripts:

    - Use NSE scripts for vulnerability detection to provide more in-depth results.
3. Run Stealth Scans in Sensitive Environments:

    - Use ```-sS``` (SYN scan) for stealth scanning to avoid triggering intrusion detection/prevention systems.
4. Automate Routine Scans:

    - Schedule scans to run periodically to keep network information up-to-date.
5. Validate Open Ports and Services:

    - Verify open ports and services detected by Nmap to ensure the information is accurate and investigate unknown services.

## Final Notes
- Nmap is an essential tool for network mapping, vulnerability assessment, and security auditing. Its flexibility and wide range of options make it suitable for tasks from simple host discovery to in-depth vulnerability scanning.
- Best Practices: Run targeted scans, leverage NSE scripts for vulnerability checks, and consider scheduling scans for continuous monitoring.