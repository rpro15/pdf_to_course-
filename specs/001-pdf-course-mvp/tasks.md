# Tasks: PDF-to-Course MVP

**Input**: Design documents from `/specs/001-pdf-course-mvp/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/

**Tests**: Test tasks are intentionally omitted because the specification does not explicitly require TDD-first test authoring.

**Organization**: Tasks are grouped by user story for independent implementation and validation.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Initialize backend/frontend projects and baseline tooling.

- [X] T001 Initialize backend Python service skeleton in backend/pyproject.toml
- [X] T002 Initialize frontend React app skeleton in frontend/package.json
- [X] T003 [P] Add backend environment template in backend/.env.example
- [X] T004 [P] Add frontend environment template in frontend/.env.example
- [X] T005 [P] Create local container orchestration file in infra/docker/docker-compose.yml

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Build common runtime foundations required by all user stories.

**⚠️ CRITICAL**: No user story work should start before this phase is complete.

- [X] T006 Create backend application bootstrap and middleware pipeline in backend/src/api/app.py
- [X] T007 [P] Configure database engine/session management in backend/src/models/db.py
- [X] T008 [P] Implement shared base ORM model utilities in backend/src/models/base.py
- [X] T009 [P] Configure asynchronous worker application in backend/src/workers/celery_app.py
- [X] T010 [P] Implement object storage abstraction with TTL support in backend/src/services/storage_service.py
- [X] T011 [P] Create processing job state manager in backend/src/services/job_state_service.py
- [X] T012 [P] Initialize frontend router and application shell in frontend/src/pages/App.tsx
- [X] T013 [P] Create shared frontend API client in frontend/src/services/apiClient.ts

**Checkpoint**: Common backend/frontend runtime and processing infrastructure are ready.

---

## Phase 3: User Story 1 - Generate Course Modules From PDF (Priority: P1) 🎯 MVP

**Goal**: Upload a text-based PDF, process chapters, and produce per-chapter summaries with review flagging.

**Independent Test**: Upload a valid text-based multi-chapter PDF and verify module list with non-empty summaries and source references.

### Implementation for User Story 1

- [X] T014 [US1] Implement `DocumentProject` and `ProcessingRun` ORM models in backend/src/models/project_models.py
- [X] T015 [US1] Implement `ChapterSource` and `CourseModule` ORM models in backend/src/models/content_models.py
- [X] T016 [P] [US1] Implement text-based PDF extraction service in backend/src/services/pdf_extraction_service.py
- [X] T017 [P] [US1] Implement image-only PDF detection and rejection service in backend/src/services/pdf_validation_service.py
- [X] T018 [P] [US1] Implement chapter segmentation service in backend/src/services/chapter_segmentation_service.py
- [X] T019 [P] [US1] Implement chapter summarization pipeline stage in backend/src/pipelines/summarization_pipeline.py
- [X] T020 [US1] Implement rule-based quality scoring (<70 => review) in backend/src/services/quality_score_service.py
- [X] T021 [US1] Implement processing orchestration worker for chapter pipeline in backend/src/workers/process_project_worker.py
- [X] T022 [US1] Implement `POST /projects` API endpoint in backend/src/api/projects_create.py
- [X] T023 [US1] Implement `POST /projects/{projectId}/process` API endpoint in backend/src/api/projects_process.py
- [X] T024 [US1] Implement `GET /projects/{projectId}/modules` API endpoint in backend/src/api/projects_modules_list.py
- [X] T025 [US1] Implement `PATCH /projects/{projectId}/language-confirmation` endpoint in backend/src/api/projects_language_confirmation_patch.py
- [X] T026 [US1] Implement upload-and-process page in frontend/src/pages/UploadProcessPage.tsx
- [X] T027 [US1] Implement modules list page with review flags in frontend/src/pages/ModulesListPage.tsx
- [X] T028 [US1] Implement language confirmation dialog and flow in frontend/src/components/LanguageConfirmationDialog.tsx

**Checkpoint**: User can upload supported PDF and receive chapter-based module summaries.

---

## Phase 4: User Story 2 - Generate and Edit Questions Per Module (Priority: P2)

**Goal**: Generate 8-10 questions per module and allow manual edits to summary/questions.

**Independent Test**: For a processed project, verify 8-10 generated questions/module and persistent edits.

### Implementation for User Story 2

- [X] T029 [US2] Implement `QuestionItem` ORM model in backend/src/models/question_models.py
- [X] T030 [P] [US2] Implement question generation service (8-10, mixed types) in backend/src/services/question_generation_service.py
- [X] T031 [US2] Extend processing worker to persist generated questions in backend/src/workers/process_project_worker.py
- [X] T032 [US2] Implement module edit validation rules in backend/src/services/module_edit_validation_service.py
- [X] T033 [US2] Implement `PATCH /projects/{projectId}/modules/{moduleId}` API endpoint in backend/src/api/projects_modules_patch.py
- [X] T034 [US2] Implement module editor page for summary/question editing in frontend/src/pages/ModuleEditorPage.tsx
- [X] T035 [US2] Implement question list edit component in frontend/src/components/QuestionEditorList.tsx
- [X] T036 [US2] Implement save workflow and optimistic UI state for edits in frontend/src/state/moduleEditorState.ts

**Checkpoint**: Questions are generated and users can edit/save module content.

---

## Phase 5: User Story 3 - Manage Processing Profiles and Export/Download Course (Priority: P3)

**Goal**: Select model profiles and export final course as JSON+Markdown package downloadable to PC.

**Independent Test**: Run processing with selected profile and complete one-click download of ZIP package to local machine.

### Implementation for User Story 3

- [X] T037 [US3] Implement `ModelProfile` ORM model and repository in backend/src/models/model_profile_models.py
- [X] T038 [P] [US3] Implement profile selection and run snapshot service in backend/src/services/model_profile_service.py
- [X] T039 [US3] Implement `ExportPackage` ORM model in backend/src/models/export_models.py
- [X] T040 [P] [US3] Implement JSON and Markdown export renderers in backend/src/services/export_render_service.py
- [X] T041 [US3] Implement ZIP package builder for `course.json` + `course.md` in backend/src/services/export_package_service.py
- [X] T042 [US3] Implement `POST /projects/{projectId}/exports` API endpoint in backend/src/api/projects_exports_create.py
- [X] T043 [US3] Implement `GET /projects/{projectId}/exports/{exportId}/download` API endpoint in backend/src/api/projects_exports_download.py
- [X] T044 [US3] Implement artifact cleanup worker for 24h retention in backend/src/workers/artifact_cleanup_worker.py
- [X] T045 [US3] Implement model profile selector UI in frontend/src/components/ModelProfileSelector.tsx
- [X] T046 [US3] Implement export and download panel with "Download to PC" action in frontend/src/components/ExportDownloadPanel.tsx
- [X] T047 [US3] Implement export state polling logic in frontend/src/services/exportService.ts
- [X] T048 [US3] Implement project ownership guard service for single-user enforcement in backend/src/services/ownership_guard_service.py
- [X] T049 [US3] Apply ownership guard across project and export endpoints in backend/src/api/access_guards.py
- [X] T050 [US3] Implement model-profile rollback compatibility manager in backend/src/services/model_profile_rollback_service.py

**Checkpoint**: User can choose profile, export, and download final course package to PC.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final hardening, documentation, and operational readiness.

- [X] T051 [P] Document unsupported PDF behavior and operator notes in docs/operations/pdf-input-policy.md
- [X] T052 [P] Document export package contract and PC download UX in docs/operations/export-download.md
- [X] T053 Add quickstart validation checklist script in scripts/validate_quickstart.ps1
- [X] T054 Update root project guidance with MVP workflow in README.md
- [X] T055 [P] Implement input adapter base interface for future formats in backend/src/pipelines/input_adapters/base_adapter.py
- [X] T056 [P] Implement PDF adapter via base interface in backend/src/pipelines/input_adapters/pdf_adapter.py
- [X] T057 Configure cloud runtime and queue/storage bindings for cloud-only policy in infra/docker/cloud.runtime.yml
- [X] T058 [P] Implement language detection confidence + confirmation flow service in backend/src/services/language_confirmation_service.py
- [X] T059 Add performance acceptance validation script for processing and export targets in scripts/validate_performance_targets.ps1
- [X] T060 Document model-profile rollback and compatibility policy in docs/operations/model-profile-compatibility.md
- [X] T061 [P] Define and version meaning-preservation scoring rubric in docs/quality/meaning-retention-rubric.md

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: starts immediately.
- **Phase 2 (Foundational)**: depends on Phase 1 completion and blocks all user stories.
- **Phase 3 (US1)**: depends on Phase 2 completion; establishes MVP core value.
- **Phase 4 (US2)**: depends on US1 output (existing modules) and Phase 2.
- **Phase 5 (US3)**: depends on US1/US2 artifacts and Phase 2.
- **Phase 6 (Polish)**: depends on completion of US1-US3.

### User Story Dependency Graph

- `US1 -> US2 -> US3`
- Rationale:
  - US2 edits/extends module content produced by US1.
  - US3 export package must include finalized module and question content from US1+US2.

---

## Parallel Execution Examples

### US1 Parallel Example

- Run `T016` and `T017` together (different services/files).
- Run `T018` and `T019` together after extraction interface is stable.
- Run `T026` and `T027` in parallel with backend endpoint work once API contracts are fixed.

### US2 Parallel Example

- Run `T030` and `T035` together (backend generation vs frontend editor component).
- Run `T032` and `T034` in parallel after API payload schema is agreed.

### US3 Parallel Example

- Run `T038` and `T040` together (profile management vs export rendering).
- Run `T045` and `T041` together (UI selector vs backend package assembly).

---

## Implementation Strategy

### MVP First

1. Complete Phase 1 and Phase 2.
2. Deliver Phase 3 (US1) as first shippable increment.
3. Validate upload -> processing -> module summary flow.

### Incremental Delivery

1. Add Phase 4 (US2) to make module content editable and learning-ready.
2. Add Phase 5 (US3) to support profile selection + export + local PC download.
3. Finish with Phase 6 polish/documentation.

### Execution Notes

- Keep single-user scope intact; do not introduce collaboration features in MVP.
- Enforce text-based PDF gate at ingestion boundary before queueing processing.
- Ensure 24-hour retention policy applies to source and intermediate artifacts.
- Ensure export endpoint always produces both `course.json` and `course.md` in one ZIP package.
