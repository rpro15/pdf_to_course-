from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..services.in_memory_store import STORE
from ..services.model_profile_service import ModelProfileService
from ..services.pdf_extraction_service import PdfExtractionService
from ..services.storage_service import StorageService
from ..workers.process_project_worker import ProcessProjectWorker

router = APIRouter(tags=["projects"])


class ProcessRequest(BaseModel):
    modelProfileId: str


@router.post("/projects/{project_id}/process")
def process_project(project_id: str, payload: ProcessRequest) -> dict:
    project = STORE.get_project(project_id)
    if project.get("languageConfirmationRequired") and project.get("status") == "awaiting_language_confirmation":
        raise HTTPException(status_code=409, detail="Language confirmation required before processing")

    profile = ModelProfileService().select_profile(payload.modelProfileId)
    project["modelProfileId"] = profile["id"]
    project["status"] = "processing"

    storage = StorageService()
    file_path = storage.project_path(project_id) / project["sourceFilename"]
    text = PdfExtractionService().extract_text(str(file_path))
    generated = ProcessProjectWorker().process_text(project_id=project_id, text=text)

    modules: list[dict] = []
    for module in generated:
        modules.append(
            {
                "id": f"{project_id}-m{module.module_index}",
                "moduleIndex": module.module_index,
                "title": module.title,
                "summaryText": module.summary_text,
                "qualityScore": module.quality_score,
                "reviewRequired": module.review_required,
                "questions": module.questions,
            }
        )

    STORE.set_modules(project_id, modules)
    project["status"] = "ready_for_review"

    return {
        "id": f"run-{project_id}",
        "modelProfileId": profile["id"],
        "status": "completed",
    }
