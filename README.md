# Yummy-Skills

Curated collection of Hermes Agent skills I use daily. Each skill is battle-tested, practical, and solves a real workflow I actually have.

## Skills

| Skill | Description | Category |
|-------|-------------|----------|
| [`zeyad-pptx-style`](zeyad-pptx-style) | McKinsey/CFI-inspired executive presentation design system for PowerPoint. Dark navy + white, clean sans-serif, left accent bar, footer breadcrumbs. | Presentation |
| [`pdf-presentation`](pdf-presentation) | PDF presentation output (Arabic RTL + English LTR) built on the pptx-style design system. Includes mandatory QA pass before delivery. | Presentation |
| [`security-audit`](security-audit) | Rigorous, evidence-driven security audit for any codebase. Covers web/frontend, backend/API, filesystem/execution, native/desktop, cloud/infra, dependencies. Standard pass + adversarial deep-dive escalation. | Security |

## Structure

```
Yummy-Skills/
├── zeyad-pptx-style/       # PowerPoint design system skill
│   └── SKILL.md
├── pdf-presentation/       # PDF presentation skill (Arabic/English)
│   └── SKILL.md
└── security-audit/         # Security audit skill with reference files
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

Install a skill into your Hermes profile:

```bash
# From this repo's root
hermes skill install ./zeyad-pptx-style
hermes skill install ./pdf-presentation
hermes skill install ./security-audit
```

Or load directly in a session:

```bash
# In Hermes chat
skill_view(name='zeyad-pptx-style')
```

## Philosophy

- **Daily drivers only** — every skill here solves a workflow I use weekly at minimum
- **No fluff** — opinionated defaults, minimal configuration, works out of the box
- **Composable** — pdf-presentation builds on pptx-style; security-audit references are reusable
- **Maintained** — if I hit a bug or gap, the skill gets updated same session

## License

MIT — use freely, modify, share.