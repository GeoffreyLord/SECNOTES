# WebSocket Vulnerabilities Notes
## Overview
WebSockets provide full-duplex communication between a client and a server over a single, long-lived connection. While WebSockets are efficient and widely used for real-time data exchange (e.g., chat applications, live feeds), they can introduce a range of security vulnerabilities if not properly implemented. Many WebSocket vulnerabilities are related to the lack of built-in security controls compared to HTTP, such as inadequate authentication, authorization, and input validation mechanisms.

## How WebSockets Work
WebSockets establish a persistent connection between the client and server, allowing both parties to send and receive messages asynchronously over a single TCP connection. The communication begins with an HTTP handshake, after which the connection is upgraded to the WebSocket protocol.

**WebSocket Handshake Example**:

- Client request:

        GET /chat HTTP/1.1
        Host: example.com
        Connection: Upgrade
        Upgrade: websocket
        Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
        Sec-WebSocket-Version: 13
- Server response:

        HTTP/1.1 101 Switching Protocols
        Upgrade: websocket
        Connection: Upgrade
        Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=

Once the connection is established, the client and server can freely exchange messages, bypassing the standard HTTP request/response model.

## Common WebSocket Vulnerabilities
1. Lack of Authentication and Authorization
    - Description: WebSockets often rely on the initial HTTP handshake for authentication, but once the connection is established, there may be no further checks for authentication or authorization, allowing unauthorized users to access or manipulate data.
    - Example:
        - An attacker connects to an open WebSocket endpoint and listens or sends messages without proper authentication.
    - Impact: Unauthorized access to sensitive data, real-time manipulation of server data, or impersonation.
2. Cross-Site WebSocket Hijacking
    - Description: An attacker can exploit an authenticated user’s session by embedding a malicious WebSocket connection in a cross-origin request. If the server doesn’t properly validate the origin of WebSocket connections, it might allow unauthorized access.
    - Example:
        - An attacker hosts a malicious site that creates a WebSocket connection to the legitimate server using the victim’s authenticated session.

                const ws = new WebSocket('ws://example.com/chat');
                ws.onopen = () => ws.send('steal_data');
    - Impact: Hijacking a user’s WebSocket connection to access or modify sensitive data.
3. Insecure WebSocket Connection (ws://)
    - Description: WebSockets can operate over insecure channels (```ws://``` instead of ```wss://```). If a WebSocket connection is established over an insecure channel, an attacker can intercept and manipulate the data via Man-in-the-Middle (MitM) attacks.
    - Example:
        - Using ```ws://example.com``` instead of ```wss://example.com``` allows an attacker to intercept the communication and manipulate messages.
    - Impact: Eavesdropping on sensitive data, message manipulation, or session hijacking.
4. Injection Attacks (XSS, SQLi, Command Injection)
    - Description: Since WebSockets often deal with user input (e.g., chat messages, commands), they are vulnerable to injection attacks if input is not properly validated. This includes Cross-Site Scripting (XSS), SQL Injection (SQLi), and command injection.
    - Example:
        - An attacker sends a malicious payload through the WebSocket:

                ws.send('<script>alert("XSS")</script>');
    - Impact: XSS in the client’s browser, SQLi on the server, or command injection leading to arbitrary code execution.
5. Denial of Service (DoS) via WebSocket Flooding
    - Description: Attackers can flood a WebSocket server with a large volume of messages, overwhelming the server's resources and causing a Denial of Service (DoS) condition.
    - Example:
        - An attacker sends thousands of messages per second through an open WebSocket connection.

                for(let i = 0; i < 100000; i++) { ws.send('flood'); }
    - Impact: Exhaustion of server resources, causing the server to become unresponsive or crash.
6. Message Tampering
    - Description: Attackers can intercept and modify WebSocket messages if they control the network or if the connection is insecure. This can lead to tampered data or altered communication between the client and server.
    - Example:
        - An attacker intercepts a message using a proxy tool (e.g., Burp Suite) and changes the message before forwarding it to the server.
    - Impact: Unauthorized actions, such as modifying a chat message or altering data being sent to the server.
7. Cross-Site Scripting (XSS) via WebSocket Responses
    - Description: The server sends data through WebSockets, which may be reflected in the client’s web application without proper sanitization, leading to XSS.
    - Example:
        - The server sends an unescaped message containing HTML or JavaScript, which is rendered in the client’s browser.

                ws.onmessage = (event) => { document.body.innerHTML += event.data; }
    - Impact: XSS attacks that allow attackers to steal cookies, hijack sessions, or execute malicious code in the victim’s browser.

## Real-World Impacts of WebSocket Vulnerabilities
1. Sensitive Data Exposure
    - Description: Lack of encryption (```ws://```) or proper authentication can expose sensitive data transmitted over WebSockets, such as personal details, financial transactions, or session tokens.
    - Example:
        - Transmitting user credentials or payment information over an unencrypted WebSocket connection (```ws://```).
2. Session Hijacking
    - Description: Attackers can hijack user sessions by exploiting cross-site WebSocket hijacking or manipulating authentication tokens sent via WebSocket connections.
    - Example:
        - An attacker opens a WebSocket connection with the victim’s authenticated session to access private data or perform unauthorized actions.
3. Real-Time Data Manipulation
    - Description: Attackers can intercept and modify messages in real-time to alter critical data (e.g., live chat messages, stock trading data) if WebSocket messages are not properly protected.
    - Example:
        - Manipulating WebSocket messages to alter a user's stock trades, changing values or amounts in transit.
4. Denial of Service (DoS)
    - Description: Flooding WebSocket servers with an overwhelming number of requests can cause service disruptions, preventing legitimate users from accessing the service.
    - Example:
        - An attacker sends thousands of WebSocket messages per second, causing the server to become unresponsive.

## Exploitation Techniques
1. Intercepting WebSocket Traffic
    - Technique: Use tools like Burp Suite or Wireshark to intercept and inspect WebSocket traffic. Look for sensitive data, authorization tokens, or unencrypted communication.
    - Example:
        - Intercepting a WebSocket connection using ```ws://``` and inspecting the messages for sensitive information.
2. Cross-Site WebSocket Hijacking
    - Technique: Embed malicious WebSocket connections on an attacker's website and leverage the victim's session to hijack the connection.
    - Example:
        
            const ws = new WebSocket('wss://example.com/chat');
            ws.onopen = () => ws.send('steal_session_data');
3. Flooding WebSocket Connections
    - Technique: Use client-side scripts or automated tools to flood WebSocket servers with an excessive number of messages.
    - Example:
    
            for(let i = 0; i < 100000; i++) { ws.send('flood_message'); }
4. Injecting Malicious Payloads
    - Technique: Send malicious input through WebSocket messages to test for injection vulnerabilities such as XSS or SQLi.
    - Example:

            ws.send('<script>alert("XSS")</script>');
5. Testing for Message Tampering
    - Technique: Intercept WebSocket messages with tools like Burp Suite, modify the message content, and forward the tampered message to the server.
    - Example:
        - Changing the value of a WebSocket message in transit:

                {"action": "transfer", "amount": "1000"}
        - Modify the ```amount``` to ```10000``` before forwarding to the server.

## Defense Mechanisms Against WebSocket Vulnerabilities
1. Use Secure WebSockets (wss://)
    - Description: Always use WebSockets over a secure channel (```wss://```) to encrypt communication and prevent man-in-the-middle (MitM) attacks.
    - Best Practices:
        - Enforce the use of ```wss://``` for all WebSocket connections.
        - Disable ```ws://``` connections on production environments.
2. Implement Proper Authentication and Authorization
    - Description: Perform strict authentication and authorization checks both during the WebSocket handshake and throughout the lifetime of the WebSocket connection.
    - Best Practices:
        - Require user authentication for every WebSocket connection.
        - Implement role-based access control (RBAC) to ensure only authorized users can perform certain actions.
3. Validate and Sanitize Input
    - Description: Validate and sanitize all incoming WebSocket messages to prevent injection attacks like XSS, SQLi, or command injection.
    - Best Practices:
        - Ensure proper input validation on both client and server side.
        - Use parameterized queries to prevent SQL injection.
4. Check WebSocket Origins
    - Description: Use the ```Origin``` header to validate that incoming WebSocket connections are from trusted domains, preventing cross-site WebSocket hijacking.
    - Best Practices:
        - Verify the ```Origin``` header during the WebSocket handshake.
        - Reject connections from untrusted or unknown origins.
5. Rate Limiting and Message Throttling
    - Description: Implement rate limiting and message throttling to prevent WebSocket DoS attacks by limiting the number of messages or connections from a single user or IP address.
    - Best Practices:
        - Limit the number of messages that can be sent over a WebSocket connection per second.
        - Enforce rate limiting to block abusive users.
## Testing for WebSocket Vulnerabilities
1. Intercept WebSocket Traffic
    - Manual Testing: Use tools like Burp Suite to intercept WebSocket traffic. Test for sensitive data exposure, improper authentication, or insecure WebSocket communication (```ws://```).
    - Example:
        - Inspect WebSocket frames for authentication tokens or sensitive information.
2. Cross-Site WebSocket Hijacking
    - Manual Testing: Embed a malicious WebSocket connection on a website you control and test if it can hijack an authenticated session of the target site.
    - Example:

            const ws = new WebSocket('wss://example.com/chat');
            ws.onopen = () => ws.send('test_hijacking');
3. Injection Testing
    - Manual Testing: Send injection payloads through WebSocket messages to test for XSS, SQLi, or command injection.
    - Example:

            ws.send('<script>alert("XSS")</script>');
4. Flood Testing
    - Automated Testing: Use automated scripts or tools to flood WebSocket connections with a large number of messages, testing for DoS vulnerabilities.
    - Example:

            for(let i = 0; i < 100000; i++) { ws.send('flood'); }
5. Message Tampering
    - Manual Testing: Use tools like Burp Suite to intercept WebSocket messages, modify the content, and forward the altered message to the server.
    - Example:
        - Modify a WebSocket message payload (e.g., changing transaction amounts) and observe the server’s response.

## WebSocket Defense Checklist
1. Use ```wss://``` for Secure WebSocket Connections:

    - Ensure all WebSocket connections are established over wss:// to protect against man-in-the-middle attacks.
2. Enforce Authentication and Authorization:

    - Authenticate users during the WebSocket handshake and revalidate periodically.
3. Sanitize and Validate Input:

    - Validate all incoming messages to prevent injection attacks like XSS and SQLi.
4. Check the ```Origin``` Header:

    - Validate the ```Origin``` header to prevent cross-site WebSocket hijacking.
5. Implement Rate Limiting:

    - Limit the number of messages or connections from each user or IP address to prevent DoS attacks.
## Final Notes
- WebSocket Vulnerabilities: Pose significant risks like unauthorized access, sensitive data exposure, injection attacks, and denial of service.
- Mitigation: Focus on secure WebSocket connections (wss://), strong authentication, proper input validation, and message rate limiting.
- Testing: Use manual and automated tools to intercept, modify, and test WebSocket communications for vulnerabilities.