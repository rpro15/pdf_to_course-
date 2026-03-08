from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..services.in_memory_store import STORE
from ..services.module_edit_validation_service import ModuleEditValidationService

router = APIRouter(tags=["projects"])


class ModuleEditRequest(BaseModel):
    title: str | None = None
    summaryText: str | None = None
    questions: list[dict] | None = None


@router.patch("/projects/{project_id}/modules/{module_id}")
def patch_module(project_id: str, module_id: str, payload: ModuleEditRequest) -> dict:
    modules = STORE.get_modules(project_id)
    target = next((m for m in modules if m["id"] == module_id), None)
    if not target:
        raise HTTPException(status_code=404, detail="Module not found")

    validator = ModuleEditValidationService()
    if payload.summaryText is not None:
        validator.validate_summary(payload.summaryText)
        target["summaryText"] = payload.summaryText
    if payload.questions is not None:
        validator.validate_questions(payload.questions)
        target["questions"] = payload.questions
    if payload.title is not None:
        target["title"] = payload.title

    return target
