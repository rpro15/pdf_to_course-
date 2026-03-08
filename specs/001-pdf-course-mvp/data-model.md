# Data Model: PDF-to-Course MVP

## Entity: DocumentProject
- Purpose: Root work item for one uploaded document and resulting course draft.
- Fields:
  - `id` (UUID, required)
  - `owner_id` (string, required, single-user MVP)
  - `title` (string, required, 1..200)
  - `source_filename` (string, required)
  - `source_mime_type` (enum: `application/pdf`)
  - `source_type` (enum: `text_pdf`, `image_pdf`)
  - `language` (string, optional)
  - `detected_language` (string, optional)
  - `language_confidence` (float 0..1, optional)
  - `language_confirmation_required` (bool, required, default false)
  - `status` (enum: `uploaded`, `awaiting_language_confirmation`, `processing`, `ready_for_review`, `ready_for_export`, `exported`, `failed`)
  - `created_at`, `updated_at` (datetime, required)
- Validation rules:
  - Reject project processing if `source_type=image_pdf` in MVP.
  - Set `language_confirmation_required=true` when `language_confidence < 0.80`.
  - Exactly one active processing run per project.

## Entity: ChapterSource
- Purpose: Canonical extracted chapter source segment.
- Fields:
  - `id` (UUID, required)
  - `project_id` (UUID, FK -> DocumentProject)
  - `chapter_index` (int, required, >=1)
  - `chapter_title` (string, required)
  - `source_text` (text, required)
  - `start_page`, `end_page` (int, required)
  - `extraction_confidence` (float 0..1, required)
  - `status` (enum: `extracted`, `failed`, `retry_pending`)
- Validation rules:
  - (`project_id`, `chapter_index`) unique.
  - `start_page <= end_page`.

## Entity: CourseModule
- Purpose: Learning module derived from one chapter.
- Fields:
  - `id` (UUID, required)
  - `project_id` (UUID, FK -> DocumentProject)
  - `chapter_source_id` (UUID, FK -> ChapterSource)
  - `module_index` (int, required, >=1)
  - `title` (string, required)
  - `summary_text` (text, required)
  - `quality_score` (int, required, 0..100)
  - `review_required` (bool, required)
  - `edit_revision` (int, required, default 0)
  - `status` (enum: `generated`, `edited`, `approved`)
- Validation rules:
  - `review_required = true` when `quality_score < 70`.
  - Summary must be non-empty.

## Entity: QuestionItem
- Purpose: Generated or edited question inside a module.
- Fields:
  - `id` (UUID, required)
  - `module_id` (UUID, FK -> CourseModule)
  - `question_index` (int, required, >=1)
  - `question_text` (string, required)
  - `question_type` (enum: `recall`, `understanding`, `application`)
  - `source` (enum: `generated`, `manual_edit`)
- Validation rules:
  - For generated set, count per module must be in [8, 10].
  - (`module_id`, `question_index`) unique.

## Entity: ModelProfile
- Purpose: Selectable profile for processing pipeline.
- Fields:
  - `id` (UUID, required)
  - `name` (string, required, unique)
  - `summary_model` (string, required)
  - `question_model` (string, required)
  - `prompt_version` (string, required)
  - `is_active` (bool, required)

## Entity: ProcessingRun
- Purpose: Execution metadata for one project processing attempt.
- Fields:
  - `id` (UUID, required)
  - `project_id` (UUID, FK -> DocumentProject)
  - `model_profile_id` (UUID, FK -> ModelProfile)
  - `status` (enum: `queued`, `running`, `partially_failed`, `completed`, `failed`)
  - `started_at`, `finished_at` (datetime)
  - `failed_chapter_count` (int, default 0)
  - `run_config_snapshot` (json, required)
- Validation rules:
  - Immutable `run_config_snapshot` after run start.

## Entity: ExportPackage
- Purpose: Downloadable package for local PC use.
- Fields:
  - `id` (UUID, required)
  - `project_id` (UUID, FK -> DocumentProject)
  - `format` (enum: `zip`)
  - `contains_files` (set: `course.json`, `course.md`)
  - `storage_path` (string, required)
  - `status` (enum: `building`, `ready`, `expired`, `failed`)
  - `created_at`, `expires_at` (datetime)
- Validation rules:
  - Package is downloadable only when `status=ready`.

## Relationships
- DocumentProject 1..* ChapterSource
- DocumentProject 1..* CourseModule
- CourseModule 1..* QuestionItem
- DocumentProject 1..* ProcessingRun
- ProcessingRun *..1 ModelProfile
- DocumentProject 1..* ExportPackage
- ChapterSource 1..1 CourseModule (MVP assumption)

## State Transitions

### DocumentProject
- `uploaded` -> (`awaiting_language_confirmation` | `processing`)
- `awaiting_language_confirmation` -> `processing`
- `processing` -> (`ready_for_review` | `failed`)
- `ready_for_review` -> `ready_for_export`
- `ready_for_export` -> `exported`

### ProcessingRun
- `queued` -> `running` -> (`completed` | `partially_failed` | `failed`)
- `partially_failed` -> `running` (retry failed chapters)

### ExportPackage
- `building` -> (`ready` | `failed`)
- `ready` -> `expired` (TTL policy)
