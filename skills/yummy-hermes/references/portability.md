# Portable instructions, host-specific activation

The portable unit is the entire `yummy/` folder, including `SKILL.md`, references,
scripts, and templates. No connector, model API, account, or network request is
required for setup. Python 3.9+ is optional; the file-tool workflow remains valid.

The bootstrap helper can copy its own bundle into the target's
`.agents/skills/yummy/` and `.claude/skills/yummy/`. Existing skill directories
are skipped as a whole, including partial ones, to avoid mixing versions.
Review incomplete copies separately; setup never repairs them by overwriting.

## Claude Code

Put the whole bundle in `.claude/skills/yummy/` for a project, or install it through
the host's supported skill flow before first use. Invoke `/yummy`. Setup creates
the foundation and a local bundle; it does not edit `CLAUDE.md` or host settings.
The skill tells Claude to read applicable root and local `AGENTS.md` explicitly.

Official reference: [Claude Code skills](https://code.claude.com/docs/en/skills).

## Hermes Agent

For initial installation, use the supported skills command:

```sh
hermes skills install Hyp4tia/Yummy-Start/skills/yummy-hermes
```

Then invoke `/yummy-hermes` in the target workspace. Current Hermes versions
also find project-local `.agents/skills/` in Git checkouts after the user trusts the project.
Explain `hermes skills trust` if needed; do not run it or change global trust
configuration as part of setup. In non-Git folders, use the already installed
Hermes skill; the copied local bundle remains portable without initializing Git.

Official reference: [Hermes skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/).

## ChatGPT and Codex

Use the host's skill installer to load `skills/yummy` from this repository for
first use. Local project copies live in `.agents/skills/yummy/`. Codex uses
`$yummy` or the `/skills` selector; ChatGPT's skill-enabled interface uses its
skill selector (currently `@`). `/yummy` remains the conversational alias once
these instructions are loaded. A Markdown file cannot register a native slash
command in every product.

Official reference: [Build skills](https://learn.chatgpt.com/docs/build-skills).

## Claude chat and other assistants

Where the host accepts skill ZIP uploads, upload a ZIP whose root contains the
`yummy/` folder and complete bundle. Otherwise attach/read `SKILL.md` and its
referenced resources, then ask the assistant to follow Yummy for the target.
Do not claim native discovery or a slash command unless that host supports it.

A chat sandbox is not the user's local project. Without access to the actual
target, produce a scaffold archive for the user to apply, explain that it has
not changed their project, and preserve any paths occupied when it is applied.
Never use an overwrite-style archive extraction to install into an existing
project. Prefer running the included bootstrap helper against that project.
