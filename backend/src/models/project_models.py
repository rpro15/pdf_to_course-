from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class ProjectStatus(str, Enum):
    UPLOADED = "uploaded"
    AWAITING_LANGUAGE_CONFIRMATION = "awaiting_language_confirmation"
    PROCESSING = "processing"
    READY_FOR_REVIEW = "ready_for_review"
    READY_FOR_EXPORT = "ready_for_export"
    EXPORTED = "exported"
    FAILED = "failed"


class ProcessingRunStatus(str, Enum):
    QUEUED = "queued"
    RUNNING = "running"
    PARTIALLY_FAILED = "partially_failed"
    COMPLETED = "completed"
    FAILED = "failed"


class DocumentProject(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    owner_id: str
    title: str
    source_filename: str
    source_mime_type: str = "application/pdf"
    source_type: str = "text_pdf"
    language: str | None = None
    detected_language: str | None = None
    language_confidence: float | None = None
    language_confirmation_required: bool = False
    status: ProjectStatus = ProjectStatus.UPLOADED
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class ProcessingRun(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    project_id: UUID
    model_profile_id: UUID
    status: ProcessingRunStatus = ProcessingRunStatus.QUEUED
    started_at: datetime | None = None
    finished_at: datetime | None = None
    failed_chapter_count: int = 0
    run_config_snapshot: str = "{}"
