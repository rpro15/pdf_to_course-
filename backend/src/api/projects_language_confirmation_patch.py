from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..services.in_memory_store import STORE

router = APIRouter(tags=["projects"])


class LanguageConfirmRequest(BaseModel):
    confirmedLanguage: str


@router.patch("/projects/{project_id}/language-confirmation")
def confirm_language(project_id: str, payload: LanguageConfirmRequest) -> dict:
    project = STORE.get_project(project_id)
    if not project.get("languageConfirmationRequired"):
        raise HTTPException(status_code=409, detail="Confirmation not required for this project")

    project["language"] = payload.confirmedLanguage
    project["languageConfirmationRequired"] = False
    project["status"] = "uploaded"
    return project
