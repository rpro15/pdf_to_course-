from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from ..services.in_memory_store import STORE

router = APIRouter(tags=["exports"])


@router.get("/projects/{project_id}/exports/{export_id}/download")
def download_export(project_id: str, export_id: str):
    export_payload = STORE.get_export(project_id, export_id)
    if export_payload.get("status") != "ready":
        raise HTTPException(status_code=409, detail="Export package not ready")

    path = Path(export_payload["storagePath"])
    if not path.exists():
        raise HTTPException(status_code=410, detail="Export package expired")

    return FileResponse(path, media_type="application/zip", filename=path.name)
