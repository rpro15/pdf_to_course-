# PDF-to-Course Constitution

## Core Principles

### I. Meaning Preservation First (Non-Negotiable)
Every summarization feature MUST preserve chapter intent, core claims, definitions, and causal logic.

- Compression targets are configurable, with default target: reduce approximately 10-15 source pages to approximately 1 summary page.
- Generated summaries MUST include: key concepts, critical terms, and chapter-level takeaways.
- If confidence in preservation is low (e.g., OCR noise, malformed PDF), system MUST flag output for human review instead of pretending quality.

### II. Chapter-to-Module Learning Structure
Each book chapter MUST map to one independent course module.

- For every chapter/module, system MUST generate 8-10 comprehension questions by default.
- Questions MUST cover factual recall, understanding, and application (not only trivia).
- Output structure MUST be consistent and machine-readable so modules can be rendered by UI and edited later.

### III. Human-in-the-Loop Editability
All AI outputs are drafts and MUST be editable.

- Users MUST be able to modify summary text, questions, and module metadata before publish/export.
- System MUST preserve source references (chapter/page anchors when available) to support manual verification.
- No irreversible transformation is allowed without keeping original extracted text snapshots.

### IV. Modular AI Pipeline and Model Agnosticism
The system MUST support one or more interchangeable processing models.

- Model orchestration MUST be separated from UI and file ingestion code.
- System MUST allow adding, removing, or replacing summarization/question-generation models with minimal code changes.
- Fine-tuning or adapter-based improvement paths MUST remain possible without redesigning core workflow.

### V. Minimal Interface, Extensible Platform
MVP UX MUST stay intentionally minimal while architecture remains extensible.

- MVP UI scope: upload PDF, process, inspect module outputs, edit outputs, export/save.
- Avoid non-essential UI complexity in MVP (advanced analytics, heavy dashboards, complex role systems).
- PDF is first-class input format; other formats (EPUB, DOCX, TXT) MUST be introduced via adapters without breaking existing PDF flow.

## Product and Quality Constraints

- Language handling MUST be explicit per document; if auto-detected language confidence is low, require user confirmation.
- Large-book processing MUST support chunking and resumable pipeline steps.
- The application MUST store processing metadata (model/version/prompt/config) for reproducibility.
- If copyrighted content is processed, output behavior MUST follow user-provided legal constraints and local policy.
- Sensitive documents SHOULD default to local/private processing modes when available.

## Delivery Workflow and Quality Gates

- Every new feature spec MUST define measurable success criteria for:
	- meaning retention quality,
	- module completeness,
	- question quality,
	- processing time budget.
- Each implementation plan MUST include at least one independent validation path (manual review checklist or automated rubric).
- Changes to model pipeline MUST include rollback strategy and compatibility notes for existing saved projects.
- MVP-first scope control applies: when in doubt, choose the simplest implementation that satisfies this constitution.

## Governance

This constitution is the highest-priority project rule for product and architecture decisions.

- Any spec, plan, or task that conflicts with this document MUST be revised before implementation.
- Amendments require: (1) rationale, (2) impact analysis on existing modules/projects, (3) migration steps.
- Versioning policy follows semantic intent:
	- MAJOR: breaking governance change,
	- MINOR: new principle/section,
	- PATCH: clarifications without behavioral change.

**Version**: 1.0.0 | **Ratified**: 2026-03-08 | **Last Amended**: 2026-03-08
