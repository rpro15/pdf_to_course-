# PDF-to-Course MVP

Minimal MVP for converting text-based PDF books into editable course modules with generated questions and downloadable course package.

## Scope (MVP)
- Upload text-based PDF only (scanned/image-only PDFs are rejected).
- Summarize chapters into course modules.
- Generate 8-10 questions per module.
- Edit module summary and questions.
- Export in JSON + Markdown and download one ZIP package to PC.

## Project Structure
- `backend/` FastAPI + worker/service layer.
- `frontend/` React UI for upload, review, editing, and export.
- `infra/docker/` Local and cloud runtime compose files.
- `docs/operations/` Operator and policy docs.

## Quick Start
1. Backend setup
	- Create Python environment and install backend dependencies from `backend/pyproject.toml`.
	- Configure variables using `backend/.env.example`.
2. Frontend setup
	- Install dependencies from `frontend/package.json`.
	- Configure variables using `frontend/.env.example`.
3. Optional local services
	- Start Redis/Postgres with `infra/docker/docker-compose.yml`.
4. Run application
	- Start backend API.
	- Start frontend dev server.
5. Validate supporting assets
	- `./scripts/validate_quickstart.ps1`
	- `./scripts/validate_performance_targets.ps1`