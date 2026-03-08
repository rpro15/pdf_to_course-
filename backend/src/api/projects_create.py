from datetime import datetime, timezone
from fastapi import APIRouter, File, Form, HTTPException, UploadFile

from ..services.in_memory_store import STORE
from ..services.language_confirmation_service import LanguageConfirmationService
from ..services.pdf_validation_service import PdfValidationService
from ..services.storage_service import StorageService

router = APIRouter(tags=["projects"])


@router.post("/projects")
async def create_project(title: str = Form(...), file: UploadFile = File(...)) -> dict:
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=415, detail="Unsupported file type")

    content = await file.read()
    project = STORE.create_project(
        {
            "ownerId": "local-user",
            "title": title,
            "status": "uploaded",
            "sourceFilename": file.filename,
            "sourceMimeType": file.content_type,
            "createdAt": datetime.now(timezone.utc).isoformat(),
        }
    )

    storage = StorageService()
    file_path = storage.save_file(project["id"], file.filename or "book.pdf", content)
    source_type = PdfValidationService().detect_source_type(str(file_path))
    if source_type == "image_pdf":
        project["status"] = "failed"
        project["error"] = "Unsupported source: image-only PDF"
        return project

    detected_language, confidence = LanguageConfirmationService().detect_language(
        content.decode("utf-8", errors="ignore")
    )
    project["detectedLanguage"] = detected_language
    project["languageConfidence"] = confidence
    project["languageConfirmationRequired"] = confidence < 0.8
    if project["languageConfirmationRequired"]:
        project["status"] = "awaiting_language_confirmation"

    return project
