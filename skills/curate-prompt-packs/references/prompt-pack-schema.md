# Prompt Pack schema

Use this section order. Fields marked **Required** must not be removed. Use `Not specified` when administrative metadata is unknown.

## 1. Pack metadata

- **Pack name — Required:** `[descriptive pack name]`
- **Pack type — Required:** `department | m365-app | role | task-family | cross-functional`
- **Scope — Required:** `[what the pack includes and excludes]`
- **Primary department:** `[department or Not specified]`
- **Primary Microsoft 365 app:** `[app or cross-app]`
- **Target roles — Required:** `[role list]`
- **Content owner:** `[owner or Not specified]`
- **Internal lifecycle status — Required:** `draft | reviewed | retired`
- **Version:** `[version or Not specified]`
- **Last reviewed:** `[date or Not specified]`
- **Source authority:** `[policy, procedure, subject-matter source, product guidance, curator input or Not specified]`
- **Source references — Required:** `[titles or controlled reference identifiers; do not invent links]`
- **Employee-facing rule — Required:** `Never expose lifecycle, approval, origin, retrieval-match or Prompt Pack status labels.`

## 2. Retrieval profile

- **Departments:** `[lowercase terms]`
- **Roles:** `[lowercase terms]`
- **Tasks:** `[lowercase primary tasks]`
- **Task synonyms:** `[natural employee phrasings]`
- **Microsoft 365 apps:** `[lowercase app names]`
- **Audiences:** `[common output audiences]`
- **Source types:** `[file, email, meeting, transcript, table, page, etc.]`
- **Output types:** `[summary, email, presentation, analysis, plan, etc.]`
- **Keywords:** `[specific deduplicated keywords]`

## 3. Pack guidance

### Intended use

`[When the agent should use this pack.]`

### Out of scope

`[Requests this pack should not govern.]`

### Terminology and constraints

`[Source-grounded terms, required phrasing and limits.]`

### Safety and personnel rules

`[Relevant data-minimization, source-grounding and neutral-documentation rules.]`

## 4. Prompt entries

Repeat this complete structure for every entry.

---

### `[ENTRY-ID]` — `[Concise task title]`

#### Entry metadata

- **Primary task — Required:** `[one task]`
- **Use when — Required:** `[recognizable employee request]`
- **Roles:** `[applicable roles]`
- **Department:** `[department or cross-functional]`
- **Microsoft 365 app — Required:** `[app]`
- **Audience:** `[intended output audience]`
- **Source types:** `[source list]`
- **Output type — Required:** `[output]`
- **Keywords — Required:** `[specific lowercase terms]`
- **Source basis — Required:** `[source reference or curator-supplied pattern]`
- **Internal lifecycle status — Required:** `draft | reviewed | retired`
- **Employee-facing status rule — Required:** `Do not surface this status or the entry’s origin.`

#### What this prompt does

`[One or two plain-language sentences describing the result.]`

#### Required intake cues

- Job role
- Department
- Task or desired outcome
- Intended audience
- Microsoft 365 app or tool
- `[task-specific detail only when essential]`

#### GCSE prompt pattern

```text
Goal

[State the task and desired result.]

Context

[State relevant role, department, audience, business purpose, background, tone and constraints.]

Source

[Identify or select the source. Do not invent source content.]

Expectation

[Define output format, structure, length, tone, detail and quality requirements. Identify missing information and prohibit unsupported content where relevant.]
```

#### Customization notes

- `[Explain important placeholders.]`
- `[Explain app-specific setup or source selection.]`

#### Safety notes

- `Do not include confidential, proprietary, protected health information or unnecessary personal information in the prompt.`
- `Review Copilot’s output for accuracy, context and completeness before using or sharing it.`
- `[Add task-specific safeguards when needed.]`

---

## 5. Coverage and maintenance

### Coverage summary

`[Roles, tasks, apps, audiences and output types covered.]`

### Known gaps

`[Missing tasks, sources, roles, authority or app guidance.]`

### Conflicts and decisions needed

`[Unresolved discrepancies and curator decisions.]`

### Retired or merged entry IDs

`[ID → governing ID and reason]`

### Maintenance notes

`[Review triggers, dependencies and future updates.]`
