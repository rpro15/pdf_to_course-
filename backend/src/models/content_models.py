from enum import Enum
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class ChapterStatus(str, Enum):
    EXTRACTED = "extracted"
    FAILED = "failed"
    RETRY_PENDING = "retry_pending"


class ModuleStatus(str, Enum):
    GENERATED = "generated"
    EDITED = "edited"
    APPROVED = "approved"


class ChapterSource(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    project_id: UUID
    chapter_index: int
    chapter_title: str
    source_text: str
    start_page: int
    end_page: int
    extraction_confidence: float
    status: ChapterStatus = ChapterStatus.EXTRACTED


class CourseModule(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    project_id: UUID
    chapter_source_id: UUID
    module_index: int
    title: str
    summary_text: str
    quality_score: int
    review_required: bool
    edit_revision: int = 0
    status: ModuleStatus = ModuleStatus.GENERATED
