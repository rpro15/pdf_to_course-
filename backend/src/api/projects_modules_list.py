from fastapi import APIRouter

from ..services.in_memory_store import STORE

router = APIRouter(tags=["projects"])


@router.get("/projects/{project_id}/modules")
def list_modules(project_id: str) -> list[dict]:
    return STORE.get_modules(project_id)
