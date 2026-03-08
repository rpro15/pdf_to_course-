# Quickstart: PDF-to-Course MVP

## Goal
Run an end-to-end flow: upload text PDF -> process chapters -> review/edit -> export -> download to PC.

## Prerequisites
- Python 3.12+
- Node.js 20+
- PostgreSQL 15+
- Redis 7+
- Environment variables configured for backend, worker, DB, and storage

## 1) Start backend and worker
1. Start API service.
2. Start background worker for chapter processing jobs.
3. Confirm health endpoint returns OK.

## 2) Start frontend
1. Run frontend dev server.
2. Open app in browser.

## 3) Upload and process PDF
1. Upload a **text-based** PDF.
2. Select a model profile.
3. If language confidence is below threshold, confirm detected language in UI.
4. Start processing and wait for completion.

Expected result:
- Chapters detected and mapped into modules.
- Each module contains non-empty summary.
- Each module has 8-10 generated questions.
- Modules with quality score <70 are flagged for review.

## 4) Edit module content
1. Open any module.
2. Edit summary text and one or more questions.
3. Save changes.

Expected result:
- Edited content persists as latest revision.

## 5) Export and download to PC
1. Click **Export Course**.
2. Wait until package status is `ready`.
3. Click **Download to PC**.

Expected result:
- Browser downloads one ZIP package.
- ZIP contains:
  - `course.json`
  - `course.md`

## 6) Failure handling check
1. Simulate chapter-level failure.
2. Trigger rerun for failed chapters only.

Expected result:
- Successful chapters are not reprocessed.
- Failed chapters are retried and merged into final project state.

## 7) Retention check
1. Verify source/intermediate artifacts are configured for 24-hour auto-deletion.
2. Confirm metadata remains available after artifact cleanup.
