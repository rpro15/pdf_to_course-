# Implementation Plan: PDF-to-Course MVP

**Branch**: `001-pdf-course-mvp` | **Date**: 2026-03-08 | **Spec**: `specs/001-pdf-course-mvp/spec.md`
**Input**: Feature specification from `/specs/001-pdf-course-mvp/spec.md`

## Summary

Build an MVP web application that accepts text-based PDF books, splits them into chapters, generates chapter summaries and 8-10 questions per chapter, allows manual edits, and exports/downloads the final course package to the user's PC in JSON and Markdown. The system uses a modular AI processing pipeline, cloud execution with 24-hour artifact retention, and single-user project ownership.

## Technical Context

**Language/Version**: Python 3.12 + TypeScript 5.6  
**Primary Dependencies**: FastAPI, Pydantic, SQLModel, Celery, Redis, pdfplumber, React, Vite  
**Storage**: PostgreSQL (project metadata) + object storage for temporary artifacts (24h TTL)  
**Testing**: pytest, pytest-asyncio, Playwright, Vitest  
**Target Platform**: Linux containers (cloud deployment) + modern desktop browsers  
**Project Type**: web-service + web-frontend  
**Performance Goals**: first draft for a 200-page text PDF in <=15 minutes for >=90% runs; export package generation <=20s p95  
**Constraints**: text-based PDF only in MVP, single-user projects only, mandatory JSON+Markdown export, quality score threshold <70 triggers review flag, source/intermediate artifact deletion within 24h, explicit language confirmation required when confidence <0.80, model-profile rollback compatibility required  
**Scale/Scope**: MVP for early adopters (single workspace, up to 200 pages per document, one active processing run per project)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Initial Gate (Pre-Research)

- **Meaning Preservation First**: PASS - quality scoring and review-flag path are explicit in spec.
- **Chapter-to-Module Learning Structure**: PASS - one module per chapter and 8-10 questions/module are required.
- **Human-in-the-Loop Editability**: PASS - editable summaries/questions/module titles are required.
- **Modular AI Pipeline**: PASS - model profile abstraction is included in requirements.
- **Minimal Interface, Extensible Platform**: PASS - MVP scope constrained to upload/process/review/edit/export/download.

No blocking violations.

### Post-Design Re-check (After Phase 1)

- **Meaning Preservation First**: PASS - data model includes quality scoring and module review state.
- **Chapter-to-Module Learning Structure**: PASS - contracts and entities enforce chapter→module mapping.
- **Human-in-the-Loop Editability**: PASS - patch/update contract supports editing before export.
- **Modular AI Pipeline**: PASS - processing run and model profile entities decouple model orchestration and include rollback/compatibility design coverage.
- **Minimal Interface, Extensible Platform**: PASS - contracts avoid non-MVP collaboration and advanced UX.

No violations introduced by design artifacts.

## Project Structure

### Documentation (this feature)

```text
specs/001-pdf-course-mvp/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── http-api.yaml
└── tasks.md
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── api/
│   ├── models/
│   ├── services/
│   ├── workers/
│   └── pipelines/
└── tests/
    ├── contract/
    ├── integration/
    └── unit/

frontend/
├── src/
│   ├── pages/
│   ├── components/
│   ├── services/
│   └── state/
└── tests/

infra/
└── docker/
```

**Structure Decision**: Web application split into backend and frontend. This keeps MVP UI minimal while isolating ingestion/AI pipeline/export APIs from presentation logic and enabling later extension to additional input formats and model backends.

## Phase 0: Outline & Research

- Research cloud processing and data-retention patterns for temporary document artifacts (24h TTL).
- Research robust chapter segmentation and fallback heuristics for text-based PDFs.
- Research model orchestration pattern for interchangeable summarization/question-generation profiles.
- Research export packaging patterns for dual-format output (JSON + Markdown) with one-click download to PC.

## Phase 1: Design & Contracts

- Define data model for DocumentProject, ChapterSource, CourseModule, QuestionItem, ProcessingRun, ModelProfile, ExportPackage.
- Define HTTP contracts for upload, language confirmation, process trigger, module listing/editing, export build, and package download.
- Create quickstart for end-to-end MVP scenario including download to local machine.
- Add rollback and compatibility notes for model-profile evolution and saved project migration behavior.
- Update agent context from finalized technical context.

## Complexity Tracking

No constitution violations requiring exception tracking.
