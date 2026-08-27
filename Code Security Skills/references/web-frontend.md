# Web / Frontend Security Reference

Read this when the target renders content in a browser or browser-like surface: a web app, an SPA, a browser extension, or a WebView (also read `native-and-desktop.md` for the embedding shell if there is one).

## XSS / HTML injection

Trace the full path: `untrusted input → parser → transformations → sanitization/escaping → DOM insertion → browser execution`.

Verify every path into the DOM is sanitized or safely constructed, not just that a sanitizer library is present somewhere. Specifically check:
- `innerHTML`/`outerHTML`/`insertAdjacentHTML`, `document.write`, `createContextualFragment`
- content that's sanitized once but then mutated or re-inserted afterward
- `eval`, `new Function`, `setTimeout`/`setInterval` called with a string
- generated SVG (`<script>`, `foreignObject`, event handlers inside SVG)
- `<iframe>`, `<object>`, `<embed>` with attacker-influenced `src`
- third-party renderer output (Markdown parsers, diagram/chart libraries like Mermaid/Vega/Graphviz, math renderers like KaTeX) — don't trust generated HTML just because a library produced it
- error messages, diff/source views, and templates that echo user input
- attributes built dynamically from user input (`href`, `src`, `style`, `on*`)

Test payload families: script tags, event-handler attributes, `javascript:`/`data:`/`vbscript:` URLs (plain and encoded, e.g. `java%73cript:`, `java%09script:`), malformed/nested HTML, mutation-based payloads, Unicode and control characters, CSS-based vectors (`expression()`, `url()` exfiltration).

## Content Security Policy

Verify the actual policy value, not just that a CSP header exists. Check `default-src`, `script-src`, `style-src`, `img-src`, `connect-src`, `font-src`, `frame-src`, `object-src`, `worker-src`, `base-uri` for `unsafe-inline`, `unsafe-eval`, broad wildcards, unrestricted `http:`/`https:`/`data:`/`file:`/`blob:`, or unrestricted custom schemes. Ask whether the policy would actually stop a realistic exfiltration or code-execution attempt, not just whether one exists.

## URL / link navigation

Trace `user-controlled href → renderer → resolver → security checks → navigation`. Verify the allowed scheme list, URL parsing and percent-decoding order, normalization, and handling of fragments/relative paths. Never rely on `startsWith("http")` or similar as the entire security model — test scheme confusion, encoded traversal, and credentials embedded in URLs (`https://evil.com@trusted.com/`).

## CSRF and cross-origin

Check state-changing requests (POST/PUT/DELETE, and any GET with side effects) for CSRF tokens or equivalent (SameSite cookies, custom-header checks). Check CORS configuration for `Access-Control-Allow-Origin: *` combined with `Access-Control-Allow-Credentials: true`, and for origin-reflection bugs (echoing the request's `Origin` header without an allowlist).

## postMessage and cross-frame communication

For any `window.postMessage` usage, verify the receiving handler checks `event.origin` against an allowlist before trusting the message, and that the sender doesn't post sensitive data to `*`. Check for clickjacking (`X-Frame-Options` / `frame-ancestors`) on pages that perform sensitive actions.

## Client-side storage and data exposure

Check `localStorage`/`sessionStorage`/cookies for sensitive data (tokens, PII) stored without appropriate flags (`HttpOnly`, `Secure`, `SameSite`) or exposed to any script on the page via XSS. Check that client-side "authorization" (hiding a button) isn't the only enforcement — the backend must re-check.
