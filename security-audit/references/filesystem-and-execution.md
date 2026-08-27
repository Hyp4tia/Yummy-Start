# Filesystem & Process Execution Security Reference

Read this when the target reads/writes files based on any input that traces back to a user, a URL, a document, or another service — or spawns processes/executes code dynamically.

## Path traversal / arbitrary file read or write

Determine whether untrusted input can make the app read or write outside its intended directory: user files, system files, credentials, SSH keys, config, or another tenant's data.

Test combinations of:
- `../`, `../../`, absolute paths, `file://` URLs
- percent-encoded traversal (`%2e%2e`, `%2E%2E`, encoded slashes/backslashes, mixed/double encoding)
- repeated separators, `....//`, `./../`
- null bytes, Unicode normalization tricks/lookalikes
- trailing separators, case variation
- symlinks and symlink chains (including dangling symlinks), sibling-directory prefix collisions (e.g. `/app-data-evil` passing a naive `startsWith("/app-data")` check)

Containment must be based on the **canonicalized, symlink-resolved** path, not a lexical string prefix check. A check like `path.startsWith(baseDir)` is not sufficient on its own — verify the code actually resolves the real path first (`realpath`/`canonicalize`/equivalent) and checks containment against that.

## Archive extraction (zip slip and friends)

If the app extracts uploaded archives (zip/tar/gzip), verify each entry's path is validated after resolving `../` sequences before being written to disk — a malicious archive entry named `../../etc/cron.d/evil` should not escape the extraction directory.

## Command / process execution

Look for any path from untrusted input to:
- shelling out (`subprocess`, `child_process`, `os/exec`, `ProcessBuilder`, backticks, `os.system`)
- dynamic script interpreters (`osascript`, PowerShell, `eval`-like constructs in the host language)
- opening files/URLs with the OS default handler in a way that could resolve to an executable

For each, check whether arguments are passed as an array (safe) or interpolated into a shell string (unsafe), and whether the executable/path itself, not just its arguments, can be influenced by untrusted input — including via traversal, symlinks, or extension/case bypasses (e.g. `file.PDF.exe`, a script with a misleading MIME type).

## Dynamic code execution

Search for `eval`, `new Function`, dynamically constructed scripts, dynamic `import()` of untrusted paths, and dynamic loading/compilation of WebAssembly. For each, determine: is it actually required, is the input constrained to a trusted set, and is it loaded only from trusted bundled assets rather than anything user-supplied? Static loading of a bundled, trusted `.wasm` asset is not equivalent to arbitrary code execution — don't over-flag it, but do verify the asset really is static and not swappable via an input path.

## Temporary files

Check for predictable temp file names (race condition / symlink attack potential), insecure permissions on created temp files, and failure to clean up files that might contain sensitive data.
