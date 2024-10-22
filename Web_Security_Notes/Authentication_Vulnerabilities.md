# Authentication Vulnerabilities Notes:

## Overview
- Authentication is the process that verifies a user’s identity. Vulnerabilities in authentication can allow attackers to bypass security measures, impersonate users, or access sensitive data.

## Authentication Basics
- Common Authentication Mechanisms:

    - Password-based Authentication: The most common form of authentication where users provide a password.
    - Token-based Authentication: Involves the use of JWTs (JSON Web Tokens) or OAuth tokens for verifying identity.
    - Multi-Factor Authentication (MFA): Requires users to provide two or more verification factors.

- Important Terms:

    - Session: Represents an authenticated user’s interaction with the web application.
    - Session Tokens: Used to maintain authentication state across multiple HTTP requests.
## Authentication Vulnerabilities

**Weak Password Policies**
- Problem: Users may set weak passwords that are easy to guess or brute-force.
- Testing:
    - Check for password complexity requirements (length, special characters).
    - Attempt brute-force attacks to guess passwords.
    - Use weak passwords and see if the system accepts them (e.g., ```password123```).

**Brute Force Attacks**
- Problem: Repeated attempts to guess passwords, PINs, or authentication tokens.
- Testing:
    - Check if rate limiting or account lockout mechanisms are in place after multiple failed login attempts.
    - Use Burp Suite Intruder to automate password guessing.

**Credential Stuffing**
- Problem: Reusing stolen username/password combinations from one site to log in to another.
- Testing:
    - Check if rate limiting or CAPTCHA mechanisms are in place for login attempts.
    - See if the application allows multiple failed login attempts without response.

**Session Hijacking**
- Problem: Attackers steal or guess session tokens to impersonate users.
- Testing:
    - Inspect session tokens in cookies or headers (e.g., check if ```HttpOnly``` and ```Secure``` flags are missing).
    - Test if sessions can be fixed or reused across users.
    - Attempt to capture session tokens over unencrypted traffic.

**Broken Authentication Logic**
- Problem: Flaws in the authentication flow allow attackers to bypass authentication mechanisms.
- Testing:
    - Try logging in with invalid credentials and check how the server responds.
    - Inspect redirections and see if it is possible to bypass login forms (e.g., manipulating URLs).
    - Verify the logic for “Remember Me” or “Stay Logged In” features.

**Weak or Exposed Session Management**
- Problem: Poor handling of session tokens can lead to hijacking or reuse.
- Testing:
    - Check session expiration and renewal mechanisms.
    - Validate if session cookies are properly flagged (e.g., ```HttpOnly```, ```Secure```).
    - Test if sessions are properly invalidated on logout.

## Multi-Factor Authentication (MFA) Vulnerabilities

**Missing or Weak MFA Implementation**
- Problem: MFA is not enforced, or weak mechanisms allow bypassing second factors.
- Testing:
    - Check if MFA can be bypassed (e.g., by intercepting or modifying requests).
    - Test if backup MFA methods are weak (e.g., SMS-based MFA can be vulnerable to SIM-swapping).
    - Try common MFA brute-force techniques (like guessing OTPs).

**MFA Token Reuse**
- Problem: MFA tokens are re-used or valid for too long.
- Testing:
    - Check if old tokens are still valid after being used.
    - Try replaying MFA tokens captured during login.

## Common Authentication Exploits
**Username Enumeration**
- Problem: Application leaks information about valid usernames.
- Testing:
    - Submit different usernames and observe differences in error messages or responses.
    - Check response times to see if valid usernames are processed differently.

**Default Credentials**
- Problem: Using default usernames and passwords set by the application (e.g., ```admin/admin```).
- Testing:
    - Try common default credentials (e.g., ```admin:admin```, ```root:root```).
    - Verify if the application enforces password changes after first login.

**OAuth Misconfigurations**
- Problem: Misconfigured OAuth flows may allow token theft or session hijacking.
- Testing:
    - Verify the proper implementation of OAuth flows (e.g., Authorization Code flow).
    - Check for exposed access tokens or improper redirect URI validation.
    - Look for open redirect vulnerabilities in the OAuth flow.

## API Authentication Vulnerabilities

**Insecure Token Storage**
- Problem: API tokens stored insecurely on the client-side.
- Testing:
    - Check if tokens are stored in localStorage or sessionStorage (which may be accessible via JavaScript).
    - Look for tokens in URLs, which can be captured by intermediaries.

**JWT (JSON Web Token) Attacks**
- Problem: Poorly implemented JWTs can be manipulated or decoded.
- Testing:
    - Inspect the JWT structure; if it uses ```None``` as the signing algorithm, it’s vulnerable.
    - Try changing the JWT’s payload and resigning it with a valid key to impersonate another user.
    - Check if JWT tokens have proper expiration times (```exp``` claim).


## Authentication Best Practices (Testing Checklist)
1. Strong Password Policy:

    - Enforce minimum password complexity (length, special characters).
    - Enforce password changes after a certain period or after breaches.
    - Implement proper password hashing (```bcrypt```, ```scrypt```, ```argon2```).

2. Multi-Factor Authentication:

    - Enforce MFA for sensitive operations.
    - Use secure MFA methods (e.g., hardware tokens or app-based tokens over SMS).
    - Ensure MFA tokens expire after a short duration and cannot be reused.

3. Session Management:

    - Use short-lived, rotating session tokens.
    - Set ```HttpOnly``` and ```Secure``` flags on session cookies.
    - Invalidate sessions after logout or inactivity.

4. Rate Limiting:

    - Implement rate limiting on login and authentication-related endpoints.
     - Lock accounts or add CAPTCHA after multiple failed login attempts.

5. Token Security:

    - Ensure JWT tokens are signed with a strong algorithm (e.g., ```HS256```, ```RS256```).
    - Avoid storing tokens in localStorage or sessionStorage on the client-side.
    - Implement token expiration and proper validation of token claims.

## Final Notes
- Common Mistakes: Many authentication vulnerabilities come from weak password policies, poor session handling, and insecure token management.
- Think Like an Attacker: Always test for brute-force protection, session hijacking risks, and proper OAuth flow implementations.
- API Authentication: Pay attention to how APIs handle tokens (JWTs, API keys), and ensure tokens are stored and transmitted securely.