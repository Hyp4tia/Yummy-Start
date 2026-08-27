# Dependencies, Supply Chain & Cryptography Reference

Read this for any repo with a package manifest and lockfile, or any custom use of cryptographic primitives.

## Dependency and supply-chain risk

- Check for known-vulnerable dependency versions (cross-reference package + version against public advisories where you have the ability to check; otherwise flag versions that look old/unmaintained for manual verification).
- Unpinned or overly loose version ranges (`*`, unconstrained `^`/`~` ranges on security-sensitive packages) that could silently pull in a compromised update.
- Presence of a lockfile and whether it's actually committed and used in CI (a missing or ignored lockfile undermines reproducible, vetted installs).
- Typosquatting risk — package names that are suspiciously close to a popular package.
- Packages with install-time scripts (`postinstall`, etc.) — these execute arbitrary code at install time and deserve extra scrutiny for anything newly added or unfamiliar.
- Vendored/bundled third-party code that isn't tracked by the normal package manager (and so bypasses normal update/audit tooling).

## Cryptography

- **Weak or broken algorithms**: MD5/SHA1 used for password hashing (should be bcrypt/scrypt/argon2) or for anything security-sensitive (fine for non-security checksums only); DES/RC4/ECB mode.
- **ECB mode** specifically — check any AES usage isn't defaulting to ECB, which leaks structural patterns in the plaintext.
- **Hardcoded or predictable keys/IVs/salts** — a static IV reused across encryptions, a key committed in source, a salt that's constant across all users.
- **Insufficient randomness** — session tokens, password reset tokens, or API keys generated from a non-cryptographic PRNG (e.g. `Math.random()`, `rand()`) instead of a CSPRNG.
- **Custom cryptography** — home-rolled encryption or hashing schemes instead of vetted libraries; flag for replacement regardless of whether an immediate break is found.
- **Certificate/TLS validation** — TLS verification disabled or overly permissive (accepting self-signed certs, disabled hostname verification) outside of clearly-scoped local dev config.
- **Key management** — are encryption keys stored separately from the data they protect, with reasonable rotation/access control, rather than alongside the ciphertext or in the same config file?
