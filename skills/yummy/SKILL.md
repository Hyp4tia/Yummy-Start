---
name: yummy
description: Set up a universal project foundation with operating rules, goals, status, decisions, design evidence, and organized work folders. Use for /yummy or requests to initialize this foundation in a new or existing project without changing existing files.
license: MIT
---

# Yummy

Distributed under the [MIT license](assets/LICENSE).

Build a small, useful foundation for any project: business, family, research,
content, software, or another kind of work. Specialize only when the project
earns the complexity. Treat `/yummy` as a request to run this workflow once the
host has loaded these instructions. Native command registration is host-specific;
see [portability](references/portability.md).

## Setup boundary

During setup, **create missing files and directories only**. Never overwrite,
append to, patch, rename, move, delete, or reformat anything already in the target
project, including existing foundation documents and skill installations. Never
change Git state, application configuration, dependencies, global skills, trust
settings, or the user's home directory. Organize newly created material; leave
existing material at its current paths and link to it where useful.

An existing path always wins, even if it is empty, outdated, or looks like a
Yummy file. Report conflicting paths without creating duplicate foundation
documents or silently picking a different project root. Repeated invocations
fill missing paths only. Do not interpret setup as permission to start project
work or keep editing its documents afterward.

## Workflow

1. Establish the actual target project root from the user's request or the active
   workspace. If there are several plausible targets, ask for the target while
   continuing read-only discovery. Do not infer project intent from a random
   directory name. Read applicable existing agent instructions first.
2. Inspect a bounded selection of relevant project files, current documents,
   and user-provided context. Establish known goals, work status, decisions,
   natural areas, and visual evidence. Avoid secrets and unrelated private data.
   Missing facts stay explicitly unknown; ask only for information that blocks
   a useful setup. Reading a project does not authorize changing it.
3. Read [the foundation guide](references/foundation.md). Prepare concise,
   evidence-based initial contents for **missing** foundation documents before
   writing them. Existing files are authoritative within their scope. Preserve
   uncertainty and source paths. Do not invent owners, dates, priorities, past
   decisions, progress, or project-specific rules.
4. Read [the design guide](references/design.md) for `DESIGN.md`. Extract values
   from this project's actual styles, brand files, or supplied design evidence.
   With no evidence, use the empty token template and mark visual rules unknown
   or not applicable. Never transplant another app's styles or guess values.
5. With Python 3.9+ and filesystem access, run
   [scripts/bootstrap.py](scripts/bootstrap.py), first with `--dry-run`, then
   without it. The helper installs project-local copies of this skill and
   creates only missing foundation files and folders. Its options are shown by
   `--help`. To tailor new documents, prepare a temporary JSON object outside
   the target containing root filenames mapped to complete document text, then
   pass `--content-json`; the helper still preserves any occupied destination.
   Select `--host universal`, `claude`, or `all` (default `all`) as appropriate.
   Pass `--area` only for a major area supported by project evidence.
6. Without Python, reproduce the same behavior using the host's file tools:
   check destination and ancestor types, reject links/junctions, use exclusive
   creation where available, and preserve occupied paths. Copy this whole skill
   bundle into a missing project-local skill directory as described in the
   portability guide. The helper's templates are
   [AGENTS.md](assets/foundation/AGENTS.md),
   [PROJECT.md](assets/foundation/PROJECT.md),
   [STATUS.md](assets/foundation/STATUS.md),
   [DECISIONS.md](assets/foundation/DECISIONS.md), and
   [DESIGN.md](assets/foundation/DESIGN.md).
   If the host cannot reliably inspect and write the target, return a scaffold
   bundle or instructions and clearly say it has **not** been installed there.
7. Verify new paths and that pre-existing files are unchanged. Report the target,
   created paths, preserved paths, conflicts, design evidence gaps, and the host's
   next invocation method. A blocked foundation path means partial setup; do not
   call it complete. Host trust/discovery requirements are separate from copying
   files: explain any remaining manual activation without altering settings.

Create a nested `AGENTS.md` only when an area needs distinct operating rules.
Ancestor rules still apply; local instructions narrow their own subtree. Repeat
the pattern deeper only when justified. Empty folders need no ceremonial rules.
