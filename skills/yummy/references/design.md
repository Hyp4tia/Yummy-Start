# DESIGN.md: exact values, explicit evidence

Use two layers. This is Yummy's document convention, not a claim that every
design tool implements the same schema. Do not derive a design from a different
project, an app name, screenshots of unrelated products, or general taste.

## Layer 1: YAML tokens

Place valid YAML frontmatter at byte one of `DESIGN.md`. Include five categories:

- `colors`: semantic jobs, with exact colors or literal variable references.
- `typography`: actual families, weights, sizes, and scales.
- `rounded`: shape/corner-radius values with units where applicable.
- `spacing`: actual base unit and scale values, preserving units.
- `components`: actual atomic mappings to tokens, such as the string
  `"{colors.primary}"`, only when the implementation supports the relationship.

Quote colors and references. Preserve units and expressions such as `rem`, `px`,
`clamp(...)`, and `var(...)`; do not silently convert them. Record mode-specific
values, aliases, and exceptions when present. If the implementation uses raw
values, do not pretend it has a token abstraction. An unresolved category is
`{}`; an unresolved individual value can be `null`. A nonvisual project still
gets the document, with its visual relevance explicitly unresolved or absent.

Use the [empty template](../assets/foundation/DESIGN.md) until evidence exists.
No default palette, font, radius, spacing system, or button rules are supplied.

## Layer 2: ordered rationale and rules

1. **Overview**: verified identity, mood, visual relevance, and evidence scope.
2. **Colors**: semantic roles, modes, states, and actual use constraints.
3. **Typography**: where headings, body, labels, and other styles occur.
4. **Layout**: measured/declared grids, alignment, breakpoints, and responsiveness.
5. **Elevation and Depth**: real shadows, glows, layering, and z-index rules.
6. **Shapes**: corner treatments and geometry with known exceptions.
7. **Components**: actual buttons, inputs, cards, states, and behavior limits.
8. **Do's and Don'ts**: explicit project constraints and confirmed patterns.

Do not invent bans on gradients or shadows, or an arbitrary limit on primary
buttons. Label interpretation as interpretation; code shows implementation but
does not necessarily establish the original designer's rationale.

## Evidence and unknowns

Inspect real stylesheets, theme/configuration files, UI components, brand guides,
and other relevant user-provided artifacts. Record source paths, symbols or
line locations, and revision/date where available. For exact numeric values,
prefer implementation/design specifications over visual estimation. Screenshots
can support qualitative observations but do not establish exact tokens.

Maintain an evidence table associating token/rule paths with their sources.
Surface conflicting sources rather than silently choosing one. Ask for source
material only if needed; setup can complete with unknown values. Do not install
dependencies or edit the app to make inspection easier. If `DESIGN.md` already
exists, read and preserve it; report gaps in the setup response.
