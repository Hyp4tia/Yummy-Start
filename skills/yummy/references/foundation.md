# Foundation and organization

The same foundation works across project types. Keep initial documents small,
use the user's language and terminology, and link to existing work in place.

| Root document | Purpose and ownership | Initial content |
| --- | --- | --- |
| `AGENTS.md` | How agents operate | Scope, applicable instructions, evidence rules, routing, handoff, and setup preservation boundary. Add project-specific rules only when supplied or established. |
| `PROJECT.md` | What the project aims to accomplish | Purpose, intended outcome, scope, success criteria, constraints, known stakeholders, references, and open questions. Distinguish confirmed facts from proposals. |
| `STATUS.md` | Short project overview | Link to task records or existing work-system entries for details. Summarize state and the project-level next action. Task records own detailed progress, blockers, and completion evidence; do not maintain a rival log here. |
| `DECISIONS.md` | Important choices and why | A decision log with context, choice, rationale, consequences, and source. Include only real decisions, including setup choices made in the current conversation. An empty log is valid. |
| `DESIGN.md` | Visual tokens and rules | YAML frontmatter and ordered Markdown guidance. Use the design guide; absence of visual evidence is a valid result. |
| `README.md` | Human starting point | Where to start, folder boundaries with examples, ownership of facts, how to resume work, and one explicitly hypothetical worked example. Preserve an existing README. |

Each fact has one owner. `PROJECT.md` owns goals; task records own execution
details; `DECISIONS.md` owns confirmed choices; `DESIGN.md` owns visual rules;
`AGENTS.md` owns operating instructions. Other documents link to these facts.
If sources conflict, inspect the evidence and surface uncertainty before edits.

## Folder map

```text
project/
├── README.md                 human starting point
├── AGENTS.md
├── PROJECT.md
├── STATUS.md
├── DECISIONS.md
├── DESIGN.md
├── inbox/
├── areas/
├── resources/
├── work/
│   ├── TASK-TEMPLATE.md       reusable form, not a queued task
│   ├── queued/
│   ├── active/
│   └── completed/
├── outputs/
├── archive/
├── .agents/skills/yummy/        # portable local bundle
└── .claude/skills/yummy/        # Claude Code discovery when selected
```

These short names are defaults for new setups. Existing legacy names are reused:
`temp-inbox` for inbox, `areas-sections` for areas, and `active-queued-work` (or
`actve-queued-work`) for work. Never rename or migrate existing folders during
setup. The helper reports the selected routes and renders new default documents
to match. When short and legacy names both exist, the helper uses the short name
for new paths and reports the ambiguity; inspect existing instructions and state
clearly which route applies. Do not merge or reorganize the existing contents.

- `inbox/`: incoming material awaiting classification, such as a new meeting note.
- `areas/`: long-lived subjects or responsibilities, such as venue planning.
  Create named areas only when evidence supports them; an empty parent is enough.
- `resources/`: supporting inputs, such as a requirements note or research article.
  Reference existing resources at their actual paths instead of copying them.
- `work/queued/`: task records awaiting work, such as a venue-comparison task.
- `work/active/`: records for work actually in progress.
- `work/completed/`: records of verified completion and its evidence.
- `outputs/`: actual deliverables, such as the venue-comparison PDF. Label readiness.
- `archive/`: destination for material archived in separately authorized future
  work. Setup does not put existing material here or move anything into it.

Folders route new material; they do not force an existing application or research
directory into this structure. Do not relocate code, documents, or assets.

## Task records and deliverables

Setup creates `work/TASK-TEMPLATE.md` but no invented tasks. Use
[the task template](../assets/work/TASK-TEMPLATE.md) for new authorized work:
unique stable ID/filename, state, owner if known, area, intended outcome,
completion criteria, verified progress, next action, blockers, sources/decisions,
deliverable links/readiness, and completion evidence. Prefer an existing task
system when present; link to its entries rather than duplicating them.

Completed records answer what was done and checked. Outputs are what people can
use or review. Link between them and keep one copy of each artifact. A task may
have no artifact; an output may be review-ready while the task is still active.
Source code and artifacts requiring another location stay there and are linked.

## Agent reading order and ongoing work

Read applicable root, ancestor, and local `AGENTS.md`; then `PROJECT.md` and
`STATUS.md`; then the current task. Read relevant decisions when choices matter
and design guidance for visual work. Load other area guidance/resources as needed.

The create-only boundary applies to `/yummy` setup. Later authorized work can
maintain affected task records, the short status overview, and confirmed choices
within its scope and existing project rules. State changes should preserve a
task's ID and filename and update affected links. Verify completion criteria and
record evidence before marking completed. Setup alone authorizes none of these
later edits or moves. See [the human guide](../assets/foundation/README.md) for a
clearly labeled hypothetical family-event example; do not seed it as real work.

## Scaling downward

Root `AGENTS.md` governs the project. A subtree gets its own `AGENTS.md` when it
has distinct review criteria, evidence requirements, terminology, or workflow
that would clutter root instructions. The local file states its scope and what
it adds to ancestor guidance. Existing local instructions remain untouched.
Create deeper rules only when another distinct workflow makes them useful.

## Verification

Before setup, inventory occupied destinations and retain hashes of existing
files in the affected paths when practical. After setup, compare them and check
new documents, folders, and skill bundles. A rerun should create nothing when
the scaffold is intact. Treat path conflicts as partial setup and list them;
do not resolve them by editing the user's existing project.
