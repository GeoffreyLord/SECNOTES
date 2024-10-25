# IPTables Notes
## Overview
IPTables is a command-line utility for configuring and managing firewall rules on Linux systems. It uses predefined chains of rules to control the incoming, outgoing, and forwarded network traffic, making it essential for securing a server or network. IPTables operates by matching traffic to specified rules and performing actions like allowing, dropping, or rejecting packets.

## Key Concepts
1. Tables
    - Description: IPTables has multiple tables, each serving a different purpose.
        - Filter: The default table, used for general packet filtering.
        - Nat: Used for network address translation (NAT) and port forwarding.
        - Mangle: Modifies packets to alter their quality of service (QoS).
        - Raw: Configures exceptions for connection tracking.
    - Usage:

            iptables -t nat -L        # List rules in the NAT table
2. Chains
    - Description: Each table has chains where rules are organized and applied to packets.
        - INPUT: Handles incoming packets destined for the host.
        - OUTPUT: Manages packets originating from the host.
        - FORWARD: Manages packets routed through the host.
        - PREROUTING: Alters packets before routing.
        - POSTROUTING: Alters packets after routing.
    - Usage:

            iptables -L INPUT         # List rules in the INPUT chain
3. Targets
    - Description: Defines what action to take when a packet matches a rule.
        - ACCEPT: Allow the packet to pass.
        - DROP: Silently drop the packet.
        - REJECT: Reject the packet and send an error message.
        - LOG: Log the packet for review.
    - Usage:

            iptables -A INPUT -j DROP   # Add a rule to drop packets in the INPUT chain
Basic Commands
1. List Rules
    - Description: Display the current rules for a specific chain or all chains.
    - Usage:

            iptables -L                     # List rules in the default table (Filter)
            iptables -t nat -L              # List rules in the NAT table
            iptables -L -v -n               # List rules with more detail and IP addresses
2. Adding a Rule
    - Description: Add a rule to a specific chain.
    - Usage:

            iptables -A INPUT -p tcp --dport 22 -j ACCEPT   # Allow SSH connections on port 22
            iptables -A INPUT -s 192.168.1.100 -j DROP      # Drop all traffic from IP 192.168.1.100
3. Deleting a Rule
    - Description: Remove a rule from a specific chain.
    - Usage:

            iptables -D INPUT -p tcp --dport 22 -j ACCEPT   # Delete rule allowing SSH
            iptables -D INPUT 1                             # Delete rule by its line number (e.g., first rule)
4. Flushing All Rules
    - Description: Remove all rules from all chains, effectively clearing the firewall configuration.
    - Usage:

            iptables -F                   # Flush all rules in the default table (Filter)
            iptables -t nat -F            # Flush all rules in the NAT table
5. Saving Rules
    - Description: Save the current firewall rules so they persist after a reboot.
    - Usage:

            # Command may vary by Linux distribution:
            sudo iptables-save > /etc/iptables/rules.v4     # Save IPv4 rules
            sudo ip6tables-save > /etc/iptables/rules.v6    # Save IPv6 rules
6. Restoring Rules
    - Description: Restore previously saved IPTables rules from a file.
    - Usage:

            sudo iptables-restore < /etc/iptables/rules.v4  # Restore IPv4 rules
            sudo ip6tables-restore < /etc/iptables/rules.v6 # Restore IPv6 rules

## Common Use Cases
1. Allow Specific Ports
    - Example: Allow traffic on HTTP (port 80) and HTTPS (port 443).

            iptables -A INPUT -p tcp --dport 80 -j ACCEPT
            iptables -A INPUT -p tcp --dport 443 -j ACCEPT
2. Block a Specific IP Address
    - Example: Block traffic from IP address 203.0.113.5.

            iptables -A INPUT -s 203.0.113.5 -j DROP
3. Limit SSH Access
    - Example: Allow SSH only from the local network (192.168.1.0/24).

            iptables -A INPUT -p tcp --dport 22 -s 192.168.1.0/24 -j ACCEPT
            iptables -A INPUT -p tcp --dport 22 -j DROP  # Drop all other SSH attempts
4. Log Dropped Packets
    - Example: Log and drop packets from a specific IP.

            iptables -A INPUT -s 203.0.113.5 -j LOG --log-prefix "Dropped: "
            iptables -A INPUT -s 203.0.113.5 -j DROP
5. Enable NAT (Network Address Translation)
    - Example: Configure IP masquerading for network 192.168.1.0/24 on eth0.

            iptables -t nat -A POSTROUTING -s 192.168.1.0/24 -o eth0 -j MASQUERADE

## Useful Options
1. Specify Protocol
    - Description: Apply rules to specific protocols, such as TCP, UDP, or ICMP.
    - Usage:

            iptables -A INPUT -p tcp --dport 80 -j ACCEPT   # Allow TCP on port 80
            iptables -A INPUT -p icmp -j ACCEPT             # Allow ICMP (ping)
2. Limit Connections
    - Description: Limit the rate of connections to mitigate DoS attacks.
    - Usage:

            iptables -A INPUT -p tcp --dport 22 -m limit --limit 3/min -j ACCEPT   # Limit SSH connections
3. Connection Tracking
    - Description: Use connection states (e.g., NEW, ESTABLISHED) to control traffic based on session state.
    - Usage:

            iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT
            iptables -A INPUT -p tcp --dport 22 --ctstate NEW -j ACCEPT            # Allow new SSH connections

## Best Practices
1. Default to Drop All Incoming Traffic:

    - Use a default DROP policy for the INPUT chain and allow only necessary traffic.

            iptables -P INPUT DROP
            iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT  # Allow established connections

2.  Allow Loopback Interface Traffic:

    - Always allow traffic on the loopback interface to avoid self-restrictions.

            iptables -A INPUT -i lo -j ACCEPT
3. Save Rules for Persistence:

    - Save IPTables rules so they persist across reboots.

            sudo iptables-save > /etc/iptables/rules.v4
4. Limit SSH Access and Monitor Logs:

    - Restrict SSH access to specific IPs and enable logging for potential intrusions.
5. Use Connection Tracking for Stateful Filtering:

    - Allow established connections to improve security and minimize the risk of unwanted connections.

## Final Notes
- IPTables is a flexible firewall utility that provides granular control over network traffic. It is essential for securing Linux systems and is often the first line of defense against network attacks.
- Best Practices: Apply a default DROP policy, allow only essential traffic, and use connection tracking for improved security.