# Native / Desktop / Mobile Security Reference

Read this when the target is a native app (macOS, Windows, Linux, iOS, Android) — especially one that embeds a WebView, defines custom URL schemes, or bridges native code to web/JS code.

API names below are illustrative; map them to whatever platform is actually in use (Apple's `NSTask`/`Process`/`NSWorkspace`, Node's `child_process`, JVM's `ProcessBuilder`, Android `Intent`s, etc.) — don't skip this domain just because the exact API isn't the one named here.

## Embedded WebView configuration

Audit the WebView setup (`WKWebView`, Android `WebView`, Electron `BrowserWindow`/`webPreferences`, CEF, Tauri's webview) for:
- JavaScript execution settings and whether they're broader than necessary
- file URL access permissions — specifically flag anything equivalent to `allowUniversalAccessFromFileURLs` or `allowFileAccessFromFileURLs` combined with loading untrusted content
- origin handling and navigation policy — can the WebView be made to navigate to an attacker-controlled origin and retain elevated privileges?
- injected scripts / user content controllers / preload scripts, and what they expose to loaded web content
- remote content permissions when the app is expected to only render local/bundled content

Then ask whether each permissive setting is actually necessary, and whether legitimate functionality survives if it's tightened.

## Native ↔ web bridges / IPC

Treat every message handler, `postMessage` bridge, Electron IPC channel, or JS-to-native callback as a security boundary. Verify:
- the native side validates and type-checks messages from web content rather than trusting them
- messages can't be used to invoke native functionality the web layer shouldn't reach (file access, process execution, arbitrary IPC channel names)
- origin/sender is checked before acting on a message, not just its shape

## Custom URL scheme handlers

For every custom scheme the app registers, verify: canonicalization of any path/resource the scheme resolves to, containment against traversal and symlinks, correct percent-decoding order, MIME/content-type handling, and origin isolation from other schemes. A custom scheme must not become an accidental arbitrary-file-read or arbitrary-navigation primitive.

## Native process/file execution triggered by content

Determine whether opening or interacting with a document, link, or downloaded file can cause the OS to execute something: default-handler execution of a disguised file, launching `.app`/`.exe`/scripts bundled inside an otherwise-innocuous archive or document, or AppleScript/PowerShell/shell invocation triggered by a "helpful" feature (e.g. auto-opening a downloaded file). Test extension/case bypasses and traversal into application bundles.

## Mobile-specific

- **Android**: exported `Activity`/`Service`/`BroadcastReceiver`/`ContentProvider` components reachable by other apps without permission checks; Intent redirection/injection; WebView `addJavascriptInterface` exposure; insecure `file://` handling.
- **iOS**: custom URL scheme handling (see above — iOS apps are especially prone to this), Universal Links validation, insecure use of `UIWebView`/`WKWebView` configuration, Keychain misuse for sensitive storage.

## Local data storage

Check where the app stores credentials, tokens, and sensitive user data at rest: OS keychain/keystore (good) vs. plaintext files, unencrypted local databases, or app preferences (bad). Check file permissions on anything written to disk.
