from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class ModelProfile(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    name: str
    summary_model: str
    question_model: str
    prompt_version: str
    is_active: bool = True
