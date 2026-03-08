# Feature Specification: PDF-to-Course MVP

**Feature Branch**: `001-pdf-course-mvp`  
**Created**: 2026-03-08  
**Status**: Draft  
**Input**: User description: "MVP приложения: загрузка PDF-книги, сжатие глав без потери смысла, превращение глав в модули курса, генерация 8-10 вопросов на каждую главу, минимальный интерфейс и возможность в будущем менять/дообучать модели и добавлять другие форматы"

## Clarifications

### Session 2026-03-08

- Q: Где обрабатываются документы и как долго хранятся исходные/промежуточные данные? → A: Обработка в облаке + автоудаление исходников/промежуточных данных через 24 часа.
- Q: Как обрабатываются сканированные (image-only) PDF в MVP? → A: В MVP поддерживаем только text-based PDF; сканы помечаем как unsupported и запрашиваем другой файл.
- Q: В каком формате делать экспорт черновика курса в MVP? → A: Экспорт выполняется одновременно в JSON и Markdown.
- Q: Какой quality-gate использовать для автоматического флага на review? → A: Rule-based quality score (0-100) с порогом 70.
- Q: Какой режим пользователей и коллаборации в MVP? → A: Один пользователь на проект, без совместного редактирования.
- Q: Должен ли пользователь скачивать готовый курс на ПК? → A: Да, система должна давать скачивание готового курса на ПК из интерфейса.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Generate Course Modules From PDF (Priority: P1)

As a course author, I upload a PDF book and receive one course module per detected chapter, with each module containing a concise chapter summary.

**Why this priority**: This is the core product value. Without reliable chapter-to-module generation, the product does not deliver the promised workflow.

**Independent Test**: Upload a multi-chapter PDF and verify the system returns a module list where each detected chapter has a non-empty summary and source reference.

**Acceptance Scenarios**:

1. **Given** a valid PDF with clear chapter structure, **When** the user starts processing, **Then** the system returns one module per chapter with a summary for each module.
2. **Given** a valid PDF, **When** processing completes, **Then** each summary is linked to its source chapter and includes key chapter takeaways.

---

### User Story 2 - Generate and Edit Questions Per Module (Priority: P2)

As a course author, I want each module to include generated questions and I want to edit the content before finalizing the course draft.

**Why this priority**: Generated questions turn summaries into learning content, and editability ensures the output is usable in real educational workflows.

**Independent Test**: For any processed chapter module, verify that 8-10 questions are generated and can be edited, added, or removed manually.

**Acceptance Scenarios**:

1. **Given** a processed module, **When** question generation runs, **Then** the module receives 8-10 questions covering recall, understanding, and application.
2. **Given** generated summaries and questions, **When** the user edits content, **Then** the edited version is saved as the current module draft.

---

### User Story 3 - Manage Processing Profiles and Export Draft Course (Priority: P3)

As a course author, I want to choose or switch processing model profiles and export the resulting draft course to continue work in downstream tools.

**Why this priority**: Model flexibility and export make the MVP practical and future-proof without overloading the first release UI.

**Independent Test**: Process the same PDF with two different model profiles and verify run metadata is stored; export the final module set in a structured format.

**Acceptance Scenarios**:

1. **Given** available model profiles, **When** the user selects a profile and runs processing, **Then** output is tagged with profile metadata (model/profile/version/prompt configuration).
2. **Given** completed modules, **When** the user exports the draft course, **Then** exported data contains module summaries, questions, and ordering.

### Edge Cases

- PDF is scanned/image-only; system marks it as unsupported in MVP and asks for a text-based PDF.
- PDF has no explicit chapter headers or contains inconsistent heading styles.
- One or more chapters are extremely long and must be processed in chunks.
- Processing fails for selected chapters while others succeed.
- Selected model profile is unavailable during processing.
- User re-uploads a revised edition of the same book and needs a new version without losing prior results.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST allow users to upload a PDF document as the primary input format.
- **FR-002**: System MUST extract text from uploaded PDF and detect chapter boundaries.
- **FR-003**: System MUST create one course module per detected chapter.
- **FR-004**: System MUST generate a concise summary for each chapter module with a default compression target of 10-15 source pages to 1 summary page, measured as 350-700 words per module for source chapters within 10-15 pages.
- **FR-005**: System MUST preserve chapter intent, key terms, and primary takeaways in generated summaries.
- **FR-006**: System MUST generate 8-10 questions per module by default.
- **FR-007**: System MUST ensure generated questions include a mix of recall, understanding, and application prompts.
- **FR-008**: Users MUST be able to edit summaries, questions, and module titles before export.
- **FR-009**: System MUST store processing metadata per run (selected model/profile/version/prompt configuration).
- **FR-010**: System MUST support rerunning processing for failed chapters without requiring full-document reprocessing.
- **FR-011**: System MUST calculate a rule-based quality score from 0 to 100 for each generated module and flag the module for human review when score is below 70.
- **FR-012**: System MUST provide a minimal MVP interface covering upload, process start, module review/edit, and export actions.
- **FR-013**: System MUST export course draft data in a structured format that preserves module order, summaries, and questions.
- **FR-014**: System architecture MUST support adding or replacing processing models without redesigning the core workflow.
- **FR-015**: System architecture MUST allow future support for additional book formats (such as EPUB, DOCX, TXT) through adapters while keeping the PDF flow unchanged.
- **FR-016**: System MUST process documents in cloud mode for MVP.
- **FR-017**: System MUST automatically delete uploaded source files and intermediate extracted artifacts within 24 hours of processing completion.
- **FR-018**: System MUST support only text-based PDF inputs in MVP.
- **FR-019**: System MUST detect image-only/scanned PDF files and return an explicit unsupported-file message with guidance to upload a text-based PDF.
- **FR-020**: System MUST export each finalized course draft in both JSON and Markdown formats in the same export action.
- **FR-021**: System MUST enforce single-user project ownership in MVP and MUST NOT include collaborative multi-user editing.
- **FR-022**: System MUST provide a direct "Download to PC" action in MVP that downloads the finalized course export package to the user's local machine.
- **FR-023**: System MUST detect document language during ingestion and produce a `languageConfidence` score from 0.00 to 1.00.
- **FR-024**: System MUST require explicit user language confirmation before processing when `languageConfidence` is below 0.80.
- **FR-025**: System MUST provide rollback strategy for model-profile changes and preserve compatibility with previously saved projects.
- **FR-026**: System MUST define and version a meaning-preservation review rubric used for expert scoring of generated summaries.

### Key Entities *(include if feature involves data)*

- **DocumentProject**: A user work item for one uploaded source document; includes source file info, language, status, and export state.
- **ChapterSource**: Extracted chapter unit from the document; includes chapter title, chapter order, source text, and source references.
- **CourseModule**: Learning module derived from one chapter; includes module title, summary draft, review status, and edit history.
- **QuestionItem**: A question linked to a course module; includes question text, question type (recall/understanding/application), and order index.
- **ProcessingRun**: A single execution attempt; includes selected model profile, run configuration, timestamps, and per-chapter outcomes.
- **ModelProfile**: Named processing profile representing one model or model pipeline configuration used for summarization/question generation.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: In acceptance testing, at least 95% of detected chapters produce a module containing a non-empty summary and 8-10 questions in one run.
- **SC-002**: In expert review of pilot documents, at least 80% of generated summaries receive a meaning-preservation score of 4/5 or higher using the project meaning-preservation rubric.
- **SC-003**: For pilot books up to 200 pages, users can go from upload to first exportable course draft in 15 minutes or less in at least 90% of runs.
- **SC-004**: At least 90% of modules can be finalized with five or fewer manual edits per module.
- **SC-005**: In failure-recovery tests, rerun of failed chapters succeeds without reprocessing successful chapters in 100% of tested scenarios.
- **SC-006**: In acceptance testing, 100% of finalized course drafts can be downloaded to the user's PC in one click as an export package.
- **SC-007**: In acceptance testing, 100% of uploads with `languageConfidence < 0.80` require explicit language confirmation before processing starts.
