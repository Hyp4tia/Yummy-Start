# Yummy Start

**One foundation for any project. Invoke Yummy, and your AI creates the missing
structure while preserving everything already there.**

Use it for business, family projects, research, content, software, or whatever
you're working on. Start small. Specialize downward only when complexity earns it.

People start with the project's `README.md`, then its goals in `PROJECT.md` and
the overview in `STATUS.md`. Agents start with applicable `AGENTS.md` instructions,
then read goals, status, and their current task. Decisions and design guidance
are loaded when relevant.

## Get started

Ask an assistant with project filesystem access:

> Install the Yummy skill from the path listed for your assistant below, then
> use it to set up the project at [my actual project path]. Preserve every
> existing file and its location.

The first use needs the skill loaded through your assistant's supported installer
or by giving it the whole bundle. A bare `/yummy` cannot install instructions the
host has never loaded. Once loaded, invoking Yummy installs project-local skill
copies and creates missing foundation paths in the selected project.

| Assistant | Install/load | Invoke |
| --- | --- | --- |
| Claude Code | Put the whole `skills/yummy/` bundle in the project's `.claude/skills/yummy/` | `/yummy` |
| Hermes Agent | `hermes skills install Hyp4tia/Yummy-Start/skills/yummy-hermes` | `/yummy` |
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
├── README.md                 Human starting point and worked example
├── AGENTS.md                 How agents operate
├── PROJECT.md                What we're trying to accomplish
├── STATUS.md                 Where things stand now
├── DECISIONS.md              Important choices and their reasons
├── DESIGN.md                 Verified visual tokens and design rules
├── inbox/                    New material awaiting classification
├── areas/                    Long-lived subjects or responsibilities
├── resources/                New supporting files and references
├── work/                     Task records, not deliverable copies
│   ├── TASK-TEMPLATE.md       Reusable task form; not an actual task
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

The short folder names apply to new setups. Existing `temp-inbox/`,
`areas-sections/`, or `active-queued-work/` are reused without renaming or creating
parallel folders. Setup reports its chosen routes, and new default documents
match them. If both naming schemes exist, the short names receive new paths and
the ambiguity is reported; existing project instructions still apply.

Root `AGENTS.md` applies project-wide. Add a local `AGENTS.md` when an area needs
its own rules, then repeat deeper only as needed. No predefined departments,
generic task queues, or elaborate hierarchy are imposed.

## Where things belong

| Place | Purpose | Example |
| --- | --- | --- |
| `inbox/` | Incoming, unclassified material | A new meeting note |
| `areas/` | Long-lived subjects or responsibilities | Venue planning |
| `resources/` | Inputs and references | Venue requirements or a research article |
| `work/` | Task records with state and next action | A record for comparing venues |
| `outputs/` | Review-ready or finished artifacts | The actual venue comparison PDF |
| `archive/` | Retired material from later authorized work | A superseded plan |

### Why outputs and completed both exist

`work/completed/` holds the record of what was done and how completion was
verified. `outputs/` holds the artifact someone can use or review. For example,
`work/completed/001-compare-venues.md` links to `outputs/venue-comparison.pdf`.
Keep one copy of the artifact. A task may complete without producing a file,
and a review-ready output may exist while its task is still active. Link to
application code or other deliverables at their required paths instead of
moving them into outputs.

## One owner for each fact

| Owner | Facts |
| --- | --- |
| `PROJECT.md` | Goals, scope, constraints, success criteria |
| Task record or existing work-system entry | Progress, next action, blockers, completion evidence |
| `STATUS.md` | Short project overview linking to task records |
| `DECISIONS.md` | Confirmed important choices and rationale |
| `DESIGN.md` | Verified visual tokens and rules |
| `AGENTS.md` | Operating rules and reading order |
| `README.md` | Human navigation and explanations |

Link to the owner instead of maintaining competing copies. Surface conflicting
evidence before resolving it. Use a project's existing task system when present.

## Start and resume tasks

The [task template](skills/yummy/assets/work/TASK-TEMPLATE.md) is installed as
`work/TASK-TEMPLATE.md`. It records a stable ID, state, owner if known, area,
intended outcome, completion criteria, progress, next action, blockers, sources,
decisions, deliverable readiness, and completion evidence. No example tasks are
created during setup.

Resume a task by reading its next action and blockers. In later authorized work,
keep its record current, refresh the short status overview, and record significant
confirmed decisions. Move task records between state folders only within the
authorized work scope, keeping ID/filename stable and updating links. Complete a
task only after verifying its criteria and recording evidence.

The [project README template](skills/yummy/assets/foundation/README.md) includes
a hypothetical family-event example that walks from goals and reference inputs
through an active task, review-ready artifact, completion record, and confirmed
decision. The helper renders its folder names to match the actual setup routes.

## Learn from your corrections

Yummy supports document-based project learning during later authorized work:

| What you say | What the agent does |
| --- | --- |
| "Always use British English in this project" | Saves a sourced project-wide rule in `AGENTS.md` |
| "Remember: no animations in the dashboard" | Saves the rule in the dashboard's applicable instructions |
| "For this report, use a table" | Applies it to that task, without a project-wide preference |
| "Don't make it so formal" | Adjusts the current work; does not infer a permanent preference |
| "From now on, use US English instead" | Replaces the conflicting active learned rule at the same scope |
| "Forget the animation rule" | Removes the identified learned rule in the requested scope |
| "Don't save this" | Applies the current correction without persistent learning |
| "Stop remembering my corrections" | Records only a learning-pause marker that future agents honor |

Rules retain their source and scope. The agent avoids duplicate entries and
briefly reports what it actually remembered. Meaningful replacements are linked
from `DECISIONS.md`; `AGENTS.md` owns the active rule. Task-specific exceptions
do not erase lasting project preferences. Repeated corrections may suggest a
shared skill improvement, but changing Yummy itself requires an explicit request.

This learning needs readable/writable project files and agents that load the
instructions. It is not model retraining, a background watcher, or global memory
across unrelated projects. Web pages, documents, and other agents cannot silently
establish user preferences. `/yummy` setup continues to preserve every existing
file, including older instruction files and skill installations; the learning
workflow does not automatically rewrite those installations.

See [the learning guide](skills/yummy/references/learning.md) for scope, sources,
conflicts, and how learning remains separate from setup.

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
Later authorized project work may maintain records within its own scope; the
create-only setup rule does not freeze the project forever.

## Run the helper yourself

Download/clone this repository somewhere separate from the target project, then
use Python 3.9+ (standard library only):

```sh
python -B skills/yummy/scripts/bootstrap.py --root "/path/to/project" --dry-run
python -B skills/yummy/scripts/bootstrap.py --root "/path/to/project"
```

The target directory must already exist. The helper creates the empty-evidence
templates; AI-assisted use can prepare tailored content first. `--content-json`
accepts an object mapping any of the five foundation filenames or `README.md`
to complete UTF-8 text. Supplied content is preserved verbatim; default templates
are rendered using the selected folder routes.
Existing destinations always win. `--area research` adds a known major area;
`--host universal` installs only the shared bundle, `--host claude` only the
Claude bundle, and `--host all` (default) both. No global installation occurs.

The JSON receipt lists selected routes, routing notes, created, preserved, and blocked paths. Exit codes:
`0` complete/preview, `2` partial setup, `1` invalid input or unavailable resources.
Interrupted or partial skill copies are deliberately preserved on rerun; review
them separately rather than silently mixing versions.

## Repository contents

`skills/yummy/` is the complete portable skill, including project learning, for
Claude Code, ChatGPT, Codex, and other harnesses. Its references and assets are
the canonical bundle, and `scripts/package.py` packages it unchanged.
`skills/yummy-hermes/` is the Hermes-install variant. It keeps Yummy setup
create-only and omits the separate project-learning instructions that Hermes'
security scanner blocks. Both use the `/yummy` command. `tests/` checks setup
preservation and keeps the variants distinct.

```sh
python -B -m unittest discover -s tests -v
python -B scripts/package.py --output /path/to/yummy.zip
```

Licensed under [MIT](LICENSE).
