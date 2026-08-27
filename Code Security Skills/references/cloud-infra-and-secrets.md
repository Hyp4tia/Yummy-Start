# Cloud Infrastructure, CI/CD & Secrets Reference

Read this when the repo includes Dockerfiles, Kubernetes/Terraform/CloudFormation/Pulumi definitions, CI/CD pipeline configs, or direct cloud SDK usage.

## Secrets and credentials

Search source, config files, environment files, container images, logs, and CI/CD pipeline definitions for API keys, tokens, passwords, private keys, and connection strings. Check `.env` files aren't committed, secrets aren't baked into Docker image layers (even if later deleted — check earlier layers), and secrets aren't printed in CI logs (e.g. via `echo $SECRET` in a debug step, or a verbose flag that dumps environment variables). Never reproduce a discovered secret verbatim in the report — name its location and recommend rotation.

## Cloud IAM and access

- Overly broad roles/policies (wildcard actions/resources, `*:*`, admin-equivalent roles attached to a service that only needs read access to one bucket).
- Public or improperly-scoped storage (S3 buckets, GCS buckets, Azure Blob containers) — check bucket policies and ACLs, not just the application code that uses them.
- Cross-account trust relationships that are broader than intended.
- Long-lived credentials where short-lived/assumed-role credentials would work.

## Containers

- Containers running as root without need.
- Privileged mode or unnecessary capability grants (`--privileged`, `CAP_SYS_ADMIN`, etc.).
- Mounted Docker socket (`/var/run/docker.sock`) exposed to a container that processes untrusted input — this is effectively host root access.
- Base images that are unpinned (`latest` tag) or known-vulnerable.

## CI/CD pipeline security

- Third-party GitHub Actions / CI steps referenced by a mutable tag (`@main`, `@v1`) instead of a pinned commit SHA — a supply-chain risk if that action is compromised or maintainer account is hijacked.
- Pipeline steps that echo secrets, or secrets passed to a step that has broader network/artifact access than it needs.
- Pull-request-triggered workflows that run with write permissions or secret access on untrusted fork contributions (`pull_request_target` misuse).
- Deployment credentials scoped wider than the specific deploy target.

## Infrastructure as code

- Security groups / firewall rules open to `0.0.0.0/0` on ports that shouldn't be public (databases, admin panels, internal services).
- Databases or caches (RDS, Redis, Elasticsearch) reachable from the public internet or without authentication.
- Encryption at rest not enabled where it should be for sensitive data stores.
- Logging/monitoring disabled on security-relevant resources.

## Multi-tenancy / data isolation

If the infrastructure or application design implies multiple tenants sharing resources, verify isolation is enforced at the infrastructure level too (separate namespaces/schemas/encryption keys as appropriate), not only in application-layer authorization checks.
