# Agent operating rules

## Scope and reading order

These rules govern the project. Read applicable ancestor instructions and local
`AGENTS.md` for the target subtree first. Local guidance adds rules for its scope.

1. Read `PROJECT.md` for goals and `STATUS.md` for the current overview.
2. Open the task record or existing work-system entry for this assignment.
3. Read relevant `DECISIONS.md` entries when choices constrain the work or a new
   important choice is being made.
4. Read `DESIGN.md` for visual work. Load relevant resources and area guidance
   as needed; do not load every project file for every assignment.

## Ownership of facts

- `PROJECT.md` owns goals, scope, constraints, and success criteria.
- Task records own detailed progress, blockers, next action, and completion evidence.
- `STATUS.md` owns a concise overview and links to those records.
- `DECISIONS.md` owns confirmed important choices and their rationale.
- `DESIGN.md` owns verified visual tokens and visual rules.
- `AGENTS.md` owns operating rules. `README.md` helps people navigate.

Link to the owning record instead of maintaining competing versions. If records
conflict, consult their evidence and flag uncertainty before making changes.

## Route new material

- `{{inbox}}/`: unclassified incoming material.
- `{{areas}}/`: long-lived subjects or responsibilities; specialize as needed.
- `{{resources}}/`: supporting inputs; link to existing resources in place.
- `{{work}}/queued/`, `{{work}}/active/`, `{{work}}/completed/`: task records by state.
- `{{outputs}}/`: actual deliverables, labeled draft, review-ready, or finished.
- `{{archive}}/`: retired material moved only in separately authorized work.

Completed task records explain what was done and checked; outputs are artifacts
people can use. Link from a task record to its artifact; do not duplicate it.
Application code and other artifacts with required paths stay at those paths.
Use `{{work}}/TASK-TEMPLATE.md` for new records, or the project's existing task
system. Create local `AGENTS.md` only when distinct rules justify the complexity.

## Setup versus authorized ongoing work

`/yummy` setup creates missing paths only. Preserve all existing files and their
locations, including these documents, code, assets, configuration, and installed
skills. Never append, overwrite, move, rename, delete, or reformat existing
material during setup. Reuse existing legacy folder names and report conflicts.

Later project work follows the user's authorized scope and existing project
rules. Maintain affected task records, update the short `STATUS.md` overview,
and record significant confirmed decisions as part of that work. Move a task
record between state folders only when authorized, keep its ID/filename stable,
and update affected links. Do not treat setup as permission for these later edits.

## Evidence and handoffs

Separate confirmed facts, proposals, and unknowns. Cite source paths or links
for important claims. Do not invent owners, dates, progress, decisions, visual
values, or completion. Before handing off, record the next action and blockers
in the task record. Mark completed only after checking its completion criteria,
recording evidence, and linking any deliverables with their actual readiness.
