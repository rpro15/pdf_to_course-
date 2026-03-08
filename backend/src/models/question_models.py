from enum import Enum
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class QuestionType(str, Enum):
    RECALL = "recall"
    UNDERSTANDING = "understanding"
    APPLICATION = "application"


class QuestionSource(str, Enum):
    GENERATED = "generated"
    MANUAL_EDIT = "manual_edit"


class QuestionItem(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    module_id: UUID
    question_index: int
    question_text: str
    question_type: QuestionType
    source: QuestionSource = QuestionSource.GENERATED
