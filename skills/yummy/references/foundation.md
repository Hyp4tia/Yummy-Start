# Foundation and organization

The same foundation works across project types. Keep initial documents small,
use the user's language and terminology, and link to existing work in place.

| Root document | Purpose | Initial content |
| --- | --- | --- |
| `AGENTS.md` | How agents operate | Scope, applicable instructions, evidence rules, routing, handoff, and setup preservation boundary. Add project-specific rules only when supplied or established. |
| `PROJECT.md` | What the project aims to accomplish | Purpose, intended outcome, scope, success criteria, constraints, known stakeholders, references, and open questions. Distinguish confirmed facts from proposals. |
| `STATUS.md` | Where things stand now | Evidence-based state, known active/queued/completed work, blockers, next action, and sources. Use an actual review date only when known; never infer completion from a filename. |
| `DECISIONS.md` | Important choices and why | A decision log with context, choice, rationale, consequences, and source. Include only real decisions, including setup choices made in the current conversation. An empty log is valid. |
| `DESIGN.md` | Visual tokens and rules | YAML frontmatter and ordered Markdown guidance. Use the design guide; absence of visual evidence is a valid result. |

## Folder map

```text
project/
├── AGENTS.md
├── PROJECT.md
├── STATUS.md
├── DECISIONS.md
├── DESIGN.md
├── temp-inbox/
├── areas-sections/
├── resources/
├── active-queued-work/
│   ├── queued/
│   ├── active/
│   └── completed/
├── outputs/
├── archive/
├── .agents/skills/yummy/        # portable local bundle
└── .claude/skills/yummy/        # Claude Code discovery when selected
```

`active-queued-work` is the normalized spelling of the work folder.

- `temp-inbox/`: newly created incoming notes or material awaiting classification.
- `areas-sections/`: major areas that make sense for this specific project.
  Create named areas only when evidence supports them; an empty parent is enough.
- `resources/`: new references, assets, notes, data, and supporting materials.
  Reference existing resources at their actual paths instead of copying them.
- `active-queued-work/queued/`: new task records awaiting work.
- `active-queued-work/active/`: new records for work actually in progress.
- `active-queued-work/completed/`: new records of work whose completion is verified.
- `outputs/`: new finished or review-ready deliverables; label their readiness.
- `archive/`: destination for material archived in separately authorized future
  work. Setup does not put existing material here or move anything into it.

Folders route new material; they do not force an existing application or research
directory into this structure. Do not relocate code, documents, or assets.

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
