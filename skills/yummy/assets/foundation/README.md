# Start here

This is the project's starting point for people. Agents begin with `AGENTS.md`.
The project's purpose and current progress come from actual evidence, not this
scaffold. Existing files stay in their original locations.

## First visit

1. Read [PROJECT.md](PROJECT.md): what are we trying to accomplish?
2. Read [STATUS.md](STATUS.md): where are we, and what is the next useful action?
3. Open the linked task record for the work you want to pick up.

If those facts are unknown, establish them with the project owner before
assuming a goal. Setup creates structure; it does not start the underlying work.

## Where things belong

| Place | What belongs here | Example |
| --- | --- | --- |
| `{{inbox}}/` | New material awaiting classification | An incoming meeting note |
| `{{areas}}/` | Long-lived subjects or responsibilities | A family project's venue planning area |
| `{{resources}}/` | Supporting inputs and references | Venue requirements or a research article |
| `{{work}}/queued/` | Task records waiting to start | A record describing a venue comparison |
| `{{work}}/active/` | Task records for work actually in progress | The same record while options are compared |
| `{{work}}/completed/` | Verified completion records | The record explaining what was delivered and checked |
| `{{outputs}}/` | Review-ready or finished deliverables | The actual venue comparison document |
| `{{archive}}/` | Material retired in later authorized work | A superseded plan |

`{{work}}/completed/` answers **what was done?** `{{outputs}}/` contains **what can
I use or review?** A task can finish without producing a file. A deliverable can
be ready for review while its task remains active. Keep one copy of each artifact;
link to deliverables that belong elsewhere, such as application source files.

## Which document owns each fact?

| Document | Facts it owns |
| --- | --- |
| [PROJECT.md](PROJECT.md) | Goals, scope, constraints, and success criteria |
| Task records in `{{work}}/` | Detailed progress, blockers, next actions, and completion evidence |
| [STATUS.md](STATUS.md) | A short project overview that links to task records |
| [DECISIONS.md](DECISIONS.md) | Confirmed important choices and their rationale |
| [DESIGN.md](DESIGN.md) | Verified visual tokens and visual rules |
| `AGENTS.md` | Operating rules and agent reading order |

Link to the owning document instead of keeping competing copies. If documents
disagree, inspect the evidence and flag the conflict before changing anything.

## Resume or start work

For an existing task, read its outcome, next action, blockers, and source links.
For a new authorized task, copy `{{work}}/TASK-TEMPLATE.md` into `{{work}}/queued/`
with a unique filename such as `001-compare-venues.md`. Keep its ID and filename
stable through status changes. Use the project's existing task system when one
already exists; link to it instead of making duplicate task records.

As part of authorized project work, update the task record and the short status
overview. Record important confirmed choices in `DECISIONS.md`. Task-state moves
inside `{{work}}/` are separate from `/yummy` setup and must be within the work's
authorized scope. Update links when a record's location changes. Do not mark a
task completed until its stated completion criteria are verified.

## Example: a family event

This is an illustration, not work added to your project:

- `PROJECT.md` states the event's confirmed goal and constraints.
- `{{resources}}/venue-requirements.md` holds the comparison inputs.
- `{{areas}}/venue-planning/` groups that ongoing responsibility.
- `{{work}}/active/001-compare-venues.md` records the current comparison task.
- `{{outputs}}/venue-comparison.pdf` holds its review-ready deliverable.
- Once the criteria are met, the task record goes to `{{work}}/completed/` and
  links to the same deliverable. `STATUS.md` links to the completion record.
- An actual venue choice and its reason belong in `DECISIONS.md`.

## How the project learns

During later authorized work, you can say "Always use British English in this
project" or "Remember: no animations in the dashboard." Clear lasting preferences
become rules in the appropriate `AGENTS.md`, with their source and scope. The
agent briefly tells you what it saved. Future agents can follow those rules when
they read the project instructions.

"For this report, use a table" stays with that task. "Don't make it so formal"
applies to the current work without becoming permanent. A later correction can
replace a lasting rule; "forget that rule" removes the identified learned entry.
"Don't save this" keeps a correction out of persistent learning.
"Stop remembering my corrections" pauses feedback collection for the project;
the agent records only that pause so later agents honor it. Ask to resume when
ready, or explicitly ask it to remember a particular rule.

This updates project instructions, not the AI model or everyone's shared Yummy
skill. The shared skill changes only on an explicit request. Learning requires
access to the actual project files; agents must say when a correction was not
saved. Setup never overwrites existing instructions to add learning behavior.

## Setup and later work

`/yummy` creates missing files and folders only. It never edits or relocates
existing material. If this project already uses older folder names, keep them
and use the routes selected during setup. Preserve an existing README as well.
Later authorized tasks may maintain project records within their own scope;
neither setup nor the existence of this guide grants blanket editing permission.
