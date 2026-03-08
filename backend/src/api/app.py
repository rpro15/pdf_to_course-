from fastapi import FastAPI

from .projects_create import router as projects_create_router
from .projects_process import router as projects_process_router
from .projects_modules_list import router as projects_modules_list_router
from .projects_language_confirmation_patch import router as projects_language_confirmation_router
from .projects_modules_patch import router as projects_modules_patch_router
from .projects_exports_create import router as projects_exports_create_router
from .projects_exports_download import router as projects_exports_download_router

app = FastAPI(title="PDF-to-Course API", version="0.1.0")

app.include_router(projects_create_router)
app.include_router(projects_process_router)
app.include_router(projects_modules_list_router)
app.include_router(projects_language_confirmation_router)
app.include_router(projects_modules_patch_router)
app.include_router(projects_exports_create_router)
app.include_router(projects_exports_download_router)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
