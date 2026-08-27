# Yummy-Skills

Curated collection of Hermes Agent skills I use daily. Each skill is battle-tested, practical, and solves a real workflow I actually have.

## Skills

| Skill | Description | Category |
|-------|-------------|----------|
| [McKinsey-PPT](PowerPoint%20Skills/McKinsey-PPT.skill) | McKinsey/CFI-inspired executive presentation design system for PowerPoint. Dark navy + white, clean sans-serif, left accent bar, footer breadcrumbs. | Presentation |
| [McKinsey-PDF](PDF%20Skills/Mckinsey-PDF-user.skill) | PDF presentation output (Arabic RTL + English LTR) built on the pptx-style design system. Includes mandatory QA pass before delivery. | Presentation |
| [`security-audit`](security-audit) | Rigorous, evidence-driven security audit for any codebase. Covers web/frontend, backend/API, filesystem/execution, native/desktop, cloud/infra, dependencies. Standard pass + adversarial deep-dive escalation. | Security |

## Structure

```
Yummy-Skills/
├── PowerPoint Skills/       # McKinsey-PPT.skill
│   └── McKinsey-PPT.skill
├── PDF Skills/              # Mckinsey-PDF-user.skill
│   └── Mckinsey-PDF-user.skill
└── security-audit/          # Security audit skill with reference files
    ├── SKILL.md
    └── references/
        ├── web-frontend.md
        ├── backend-api.md
        ├── filesystem-and-execution.md
        ├── native-and-desktop.md
        ├── cloud-infra-and-secrets.md
        └── dependencies-and-crypto.md
```

## Usage

### PowerPoint & PDF Skills (`.skill` files)

Install directly from the `.skill` file:

```bash
# PowerPoint
hermes skill install ./PowerPoint\ Skills/McKinsey-PPT.skill

# PDF
hermes skill install ./PDF\ Skills/Mckinsey-PDF-user.skill
```

### Security Audit Skill (folder-based)

Install from the skill folder:

```bash
hermes skill install ./security-audit
```

Or load directly in a Hermes session:

```bash
skill_view(name='security-audit')
```

## Philosophy

- **Daily drivers only** — every skill here solves a workflow I use weekly at minimum
- **No fluff** — opinionated defaults, minimal configuration, works out of the box
- **Composable** — PDF skill builds on the PowerPoint design system; security-audit references are reusable
- **Maintained** — if I hit a bug or gap, the skill gets updated same session

## License

MIT — use freely, modify, share.