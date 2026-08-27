# Backend / API Security Reference

Read this when the target has server-side request handling, a database, or exposes REST/GraphQL/RPC endpoints.

## Injection

Audit every place untrusted input reaches an interpreter without proper parameterization:
- **SQL/NoSQL** — string-concatenated queries, unsafe use of `$where`/raw Mongo queries, ORM methods that accept raw fragments
- **Command injection** — untrusted input passed to a shell (`subprocess.run(..., shell=True)`, `exec()`, `child_process.exec`, backticks) instead of an argument array
- **Template injection** — user input rendered through a template engine that can execute expressions (Jinja2, Freemarker, Handlebars with `{{{ }}}` or helpers)
- **Header injection / request smuggling** — untrusted input reflected into response headers or used to build upstream requests
- **LDAP / XPath / other query languages** where applicable

For each, verify parameterized queries / prepared statements / safe APIs are used consistently, not just in the file you happened to look at first — grep for the unsafe pattern across the whole repo.

## Authentication

- Token generation: sufficient entropy, no predictable session IDs, correct JWT signature verification (reject `alg: none`, verify the signing key matches the expected issuer, check expiry is enforced).
- Password handling: hashed with a modern algorithm (bcrypt/scrypt/argon2), never logged or returned in responses.
- Password reset / account recovery: reset tokens are single-use, expire, and aren't guessable or leaked via response timing/content.
- MFA: can it be bypassed by hitting an older endpoint, skipping a step, or a race condition between "MFA required" and "session issued"?

## Authorization / access control

This is one of the highest-value areas to check and one of the easiest to under-audit:
- **IDOR** — does changing an ID in a URL or request body let one user read/modify another user's or another tenant's data? Check every endpoint that takes an ID, not just the obvious ones.
- **Missing function-level access control** — is an admin-only action actually re-checked server-side, or only hidden in the UI?
- **Privilege escalation** — can a user modify their own role/permissions field via mass assignment, or influence a JWT claim that's trusted without re-verification?
- **Mass assignment** — does an update endpoint blindly bind all fields from the request body to the model, allowing an attacker to set fields they shouldn't (role, isAdmin, balance)?

## SSRF

Any place the server makes an outbound request using a URL influenced by user input (webhooks, "fetch this image," URL previews, import-from-URL features): check for allowlisting of destination hosts/schemes, blocking of internal/link-local/metadata IP ranges (e.g. `169.254.169.254`), and that redirects are re-validated rather than blindly followed.

## Deserialization

Check for unsafe deserialization of untrusted data (`pickle`, Java `ObjectInputStream`, PHP `unserialize`, YAML `load` instead of `safe_load`) that could lead to code execution or object injection.

## Business logic

- Race conditions / TOCTOU on anything involving balances, inventory, coupon codes, or one-time actions — check-then-act without a lock or atomic operation.
- Workflow bypass — can a required step (payment, approval, verification) be skipped by calling a later endpoint directly?
- Price/quantity manipulation via client-supplied values the server should be recalculating itself.

## API-specific

- GraphQL: query depth/complexity limits, introspection disabled in production if appropriate, field-level authorization (not just query-level).
- REST: consistent authZ across API versions (an old `/v1/` endpoint that skips a check added in `/v2/`).
- Rate limiting on authentication, password reset, and other abuse-prone endpoints.

## XXE

For any XML parsing of untrusted input, verify external entity resolution and DTD processing are disabled.
