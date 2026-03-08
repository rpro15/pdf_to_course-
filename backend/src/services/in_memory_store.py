from typing import Any
from uuid import UUID, uuid4


class InMemoryStore:
    def __init__(self) -> None:
        self.projects: dict[str, dict[str, Any]] = {}
        self.modules: dict[str, list[dict[str, Any]]] = {}
        self.exports: dict[str, dict[str, Any]] = {}

    def create_project(self, data: dict[str, Any]) -> dict[str, Any]:
        project_id = str(uuid4())
        project = {"id": project_id, **data}
        self.projects[project_id] = project
        self.modules[project_id] = []
        return project

    def get_project(self, project_id: str) -> dict[str, Any]:
        return self.projects[project_id]

    def set_modules(self, project_id: str, modules: list[dict[str, Any]]) -> None:
        self.modules[project_id] = modules

    def get_modules(self, project_id: str) -> list[dict[str, Any]]:
        return self.modules.get(project_id, [])

    def save_export(self, project_id: str, export_data: dict[str, Any]) -> dict[str, Any]:
        export_id = str(uuid4())
        payload = {"id": export_id, **export_data}
        self.exports[f"{project_id}:{export_id}"] = payload
        return payload

    def get_export(self, project_id: str, export_id: str) -> dict[str, Any]:
        return self.exports[f"{project_id}:{export_id}"]


STORE = InMemoryStore()
