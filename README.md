# Yummy Start

**One foundation for any project. Invoke Yummy, and your AI creates the missing
structure while preserving everything already there.**

Use it for business, family projects, research, content, software, or whatever
you're working on. Start small. Specialize downward only when complexity earns it.

## Get started

Ask an assistant with project filesystem access:

> Install the yummy skill from https://github.com/Hyp4tia/Yummy-Start/tree/main/skills/yummy,
> then use it to set up the project at [my actual project path]. Preserve every
> existing file and its location.

The first use needs the skill loaded through your assistant's supported installer
or by giving it the whole bundle. A bare `/yummy` cannot install instructions the
host has never loaded. Once loaded, invoking Yummy installs project-local skill
copies and creates missing foundation paths in the selected project.

| Assistant | Install/load | Invoke |
| --- | --- | --- |
| Claude Code | Put the whole `skills/yummy/` bundle in the project's `.claude/skills/yummy/` | `/yummy` |
| Hermes Agent | `hermes skills install Hyp4tia/Yummy-Start/skills/yummy` | `/yummy` |
| ChatGPT with skills | Use the supported skill installer/selector; local authoring is supported in the desktop app | Select `@yummy`; `/yummy` is a conversational alias once loaded |
| Codex | Install `skills/yummy`; local project destination is `.agents/skills/yummy/` | `$yummy` or `/skills` |
| Claude chat or another AI | Upload the complete skill ZIP if supported, or supply the bundle as instructions | Ask it to follow Yummy; native command support depends on the host |

These activation methods follow the official [Claude Code](https://code.claude.com/docs/en/skills),
[Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/), and
[ChatGPT/Codex](https://learn.chatgpt.com/docs/build-skills) documentation. The portable
workflow does not depend on a particular model. Native command registration,
file access, and skill installation are features of the host application.

For Hermes project discovery in a Git checkout, the user may need to run
`hermes skills trust` once. Yummy does not change trust settings or initialize Git.

Without access to your actual project, an assistant can provide a scaffold ZIP,
but it cannot claim to have installed it in your project. Apply it with the
create-only helper rather than extracting an archive over existing files.

## What appears in your project

```text
project/
├── AGENTS.md                 How agents operate
├── PROJECT.md                What we're trying to accomplish
├── STATUS.md                 Where things stand now
├── DECISIONS.md              Important choices and their reasons
├── DESIGN.md                 Verified visual tokens and design rules
├── temp-inbox/               New material awaiting classification
├── areas-sections/           Natural major areas of this project
├── resources/                New supporting files and references
├── active-queued-work/       Normalized spelling of the work folder
│   ├── queued/
│   ├── active/
│   └── completed/
├── outputs/                  Finished or review-ready work
├── archive/                  Destination for later authorized archival
├── .agents/skills/yummy/     Portable project-local skill bundle
└── .claude/skills/yummy/     Claude Code project-local skill bundle
```

The AI reads actual project evidence and prepares initial content for missing
documents. Unknown goals, status, decisions, and design values stay explicit.
Existing files stay where they are; the new documents can link to them.

Root `AGENTS.md` applies project-wide. Add a local `AGENTS.md` when an area needs
its own rules, then repeat deeper only as needed. No predefined departments,
generic task queues, or elaborate hierarchy are imposed.

## DESIGN.md

The document starts with five YAML token categories: `colors`, `typography`,
`rounded`, `spacing`, and `components`. Its body follows this order: Overview,
Colors, Typography, Layout, Elevation and Depth, Shapes, Components, and Do's
and Don'ts. An evidence table records where values and rules come from.

Use the current project's code, styles, brand files, or supplied specifications.
Never invent colors, fonts, measurements, component limits, or design rationale.
With no visual evidence, categories stay empty. Nonvisual projects retain the
same foundation and can mark visual rules not applicable when confirmed.

## Preservation contract

Setup only creates missing paths. It never edits, appends to, overwrites, moves,
renames, deletes, or reformats an existing file. Occupied skill directories are
preserved as a whole. Reruns only fill gaps. File/directory conflicts and linked
paths are reported as partial setup; links and Windows junctions are not followed
for writes. Existing source code, assets, configuration, and Git state stay intact.

New material goes to its designated folder. Setup does not reorganize old material
or authorize ongoing work, document edits, archival, or dependency installation.

## Run the helper yourself

Download/clone this repository somewhere separate from the target project, then
use Python 3.9+ (standard library only):

```sh
python -B skills/yummy/scripts/bootstrap.py --root "/path/to/project" --dry-run
python -B skills/yummy/scripts/bootstrap.py --root "/path/to/project"
```

The target directory must already exist. The helper creates the empty-evidence
templates; AI-assisted use can prepare tailored content first. `--content-json`
accepts an object mapping any of the five root filenames to complete UTF-8 text.
Existing destinations always win. `--area research` adds a known major area;
`--host universal` installs only the shared bundle, `--host claude` only the
Claude bundle, and `--host all` (default) both. No global installation occurs.

The JSON receipt lists created, preserved, and blocked paths. Exit codes:
`0` complete/preview, `2` partial setup, `1` invalid input or unavailable resources.
Interrupted or partial skill copies are deliberately preserved on rerun; review
them separately rather than silently mixing versions.

## Repository contents

`skills/yummy/` is the complete distributable skill. Its references explain the
foundation, evidence rules, and host activation. Its assets are universal document
templates. `tests/` checks the helper's preservation behavior. `scripts/package.py`
builds an uploadable ZIP containing only the skill bundle.

```sh
python -B -m unittest discover -s tests -v
python -B scripts/package.py --output /path/to/yummy.zip
```

Licensed under [MIT](LICENSE).
