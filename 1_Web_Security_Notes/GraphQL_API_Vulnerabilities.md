# GraphQL API Vulnerabilities Notes
## Overview
GraphQL allows flexible, client-driven queries. However, this flexibility introduces risks such as excessive data exposure, unauthorized access, and denial-of-service (DoS) attacks. Proper security measures must be in place to mitigate these risks.

## Key GraphQL Vulnerabilities
1. Introspection Exposure
    - Risk: Introspection reveals the full API schema, exposing all types, queries, and mutations.
    - Testing: Send introspection queries (e.g., ```__schema``` or ```__type```). Verify if schema details are exposed.
    - Defense: Disable introspection in production.
2. Lack of Authentication/Authorization
    - Risk: Attackers may access or modify data without proper checks.
    - Testing: Attempt unauthenticated queries/mutations to see if sensitive data or actions are accessible.
    - Defense: Enforce authentication and role-based access control (RBAC).
3. Over-Privileged Queries/Mutations
    - Risk: Exposing sensitive operations or data through unsecured queries/mutations.
    - Testing: Query sensitive fields (e.g., ```password```, ```email```, ```role```) or perform mutations (e.g., delete records) to check for overexposure.
    - Defense: Limit access to privileged fields and operations.
4. Excessive Data Exposure
    - Risk: Large or sensitive datasets can be queried, exposing more information than intended.
    - Testing: Request a large number of fields or sensitive information (e.g., PII).
    - Defense: Implement field-level restrictions, use whitelists.
5. Field-Level Authorization Bypass
    - Risk: Users access or modify fields they shouldn't.
    - Testing: Attempt to query or mutate restricted fields as a lower-privileged user.
    - Defense: Enforce field-level authorization checks.
6. DoS via Deep or Large Queries
    - Risk: Complex or large queries can overwhelm the server.
    - Testing: Send deeply nested or unbounded queries, monitor server load.
    - Defense: Set query complexity and depth limits, enforce pagination.
7. Batching Attacks
    - Risk: Batching multiple operations in one request to bypass rate limiting.
    - Testing: Batch several queries or mutations in one request and check if rate limits are bypassed.
    - Defense: Implement rate-limiting and limit batched queries.
8. SQL Injection in Resolvers
    - Risk: GraphQL resolvers may pass unsanitized inputs to SQL queries, leading to SQL injection.
    - Testing: Use SQL injection payloads in input fields (e.g., ```' OR 1=1--```).
    - Defense: Sanitize all inputs and use parameterized queries.

## Testing Checklist
1. Schema Exposure: Test introspection queries for schema leaks.
2. Authentication/Authorization: Ensure sensitive data/actions require proper authentication and role-based access.
3. Query Depth/Size: Test for DoS by sending complex or large queries. Check for proper enforcement of limits.
4. Data Exposure: Query for sensitive fields. Ensure least privilege is enforced.
5.Field-Level Security: Ensure specific fields (e.g., role, admin) are protected.
6. Input Sanitization: Test for SQL injection or other input manipulation attacks.

## Best Practices for Securing GraphQL APIs
- Disable Introspection in Production.
- Enforce RBAC: Implement strict authentication and authorization at query and field levels.
- Limit Query Complexity and Depth: Set limits on query nesting and size.
- Use Pagination and Rate Limiting.
- Sanitize Inputs in Resolvers: Always sanitize and validate inputs.

## Final Notes
- GraphQL Flexibility: While powerful, can lead to overexposure or DoS if not properly secured.
- Mitigation: Focus on introspection management, query limits, field-level controls, and proper input sanitization.
- Testing focus: Look for schema exposure, excessive data, query complexity issues, and unauthorized data access.