# Research: PDF-to-Course MVP

## Decision 1: Cloud processing with 24-hour artifact retention
- Decision: Run PDF extraction and AI processing in cloud workers; auto-delete uploaded source files and intermediate artifacts after 24 hours.
- Rationale: Matches clarified product decision, enables scalable processing, and limits storage/privacy exposure.
- Alternatives considered: Local-only processing (rejected for operational complexity across user devices), indefinite cloud retention (rejected due to privacy risk and unnecessary cost).

## Decision 2: Text-based PDF only in MVP
- Decision: Accept only text-based PDFs in MVP and explicitly reject image-only/scanned PDFs.
- Rationale: Improves quality predictability and reduces OCR-related ambiguity during initial release.
- Alternatives considered: Full OCR in MVP (rejected as too high risk/scope), best-effort OCR (rejected due to inconsistent quality and support burden).

## Decision 3: Modular AI pipeline via profile abstraction
- Decision: Separate ingestion, summarization, and question generation into pluggable pipeline stages configured by `ModelProfile`.
- Rationale: Enables adding/replacing models later without redesigning API or UI.
- Alternatives considered: Hard-coded single model flow (rejected due to poor extensibility), multi-model consensus in MVP (rejected as over-scope).

## Decision 4: Rule-based quality gate for review flagging
- Decision: Compute a rule-based quality score (0-100) for each module; if score < 70, mark module for human review.
- Rationale: Provides deterministic, explainable quality gating for MVP.
- Alternatives considered: Pure manual review (rejected due to no automatic triage), LLM-as-judge only (rejected for instability/cost in MVP).

## Decision 5: Export contract = JSON + Markdown + one-click PC download
- Decision: Generate both JSON and Markdown artifacts in one export action and expose a direct download endpoint/UI action to save package to local PC.
- Rationale: Covers machine interoperability (JSON) and human readability/editability (Markdown) while meeting explicit user requirement.
- Alternatives considered: JSON-only (rejected for readability), Markdown-only (rejected for system integration), CSV-based export (rejected due to weak hierarchical structure support).

## Decision 6: MVP single-user project scope
- Decision: Keep project ownership single-user and exclude collaboration in MVP.
- Rationale: Reduces complexity in authz/conflict resolution and accelerates delivery.
- Alternatives considered: Read-only collaborators (rejected as still requiring roles/access control), full collaboration (rejected as non-MVP).

## Decision 7: Asynchronous processing model
- Decision: Use async job orchestration for document processing with per-chapter retry.
- Rationale: Supports long-running workloads and fulfills rerun-failed-chapters requirement.
- Alternatives considered: Fully synchronous API processing (rejected due to timeout risk and poor UX).

## Decision 8: Package download format
- Decision: Build export package as a ZIP containing `course.json` and `course.md`.
- Rationale: Simple user experience for download-to-PC and easy backend implementation.
- Alternatives considered: Separate file downloads (rejected due to fragmented UX), custom binary bundle (rejected due to interoperability cost).
