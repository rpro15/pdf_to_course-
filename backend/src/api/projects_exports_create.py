from fastapi import APIRouter

from ..services.export_package_service import ExportPackageService
from ..services.export_render_service import ExportRenderService
from ..services.in_memory_store import STORE
from ..services.storage_service import StorageService

router = APIRouter(tags=["exports"])


@router.post("/projects/{project_id}/exports")
def create_export(project_id: str) -> dict:
    project = STORE.get_project(project_id)
    modules = STORE.get_modules(project_id)

    renderer = ExportRenderService()
    json_text = renderer.render_json(project, modules)
    markdown_text = renderer.render_markdown(project, modules)

    storage = StorageService()
    output_dir = str(storage.project_path(project_id))
    zip_path = ExportPackageService().build_zip(output_dir, project_id, json_text, markdown_text)

    export_payload = STORE.save_export(
        project_id,
        {
            "status": "ready",
            "format": "zip",
            "files": ["course.json", "course.md"],
            "storagePath": zip_path,
        },
    )
    return export_payload
