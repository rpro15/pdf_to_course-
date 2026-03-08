from pathlib import Path
import os
import shutil
from datetime import datetime, timedelta, timezone


class StorageService:
    def __init__(self, base_path: str | None = None) -> None:
        self.base_path = Path(base_path or os.getenv("STORAGE_BASE_PATH", ".storage"))
        self.base_path.mkdir(parents=True, exist_ok=True)

    def project_path(self, project_id: str) -> Path:
        path = self.base_path / project_id
        path.mkdir(parents=True, exist_ok=True)
        return path

    def save_file(self, project_id: str, file_name: str, content: bytes) -> Path:
        file_path = self.project_path(project_id) / file_name
        file_path.write_bytes(content)
        return file_path

    def create_expiration(self, hours: int) -> datetime:
        return datetime.now(timezone.utc) + timedelta(hours=hours)

    def delete_project_artifacts(self, project_id: str) -> None:
        target = self.base_path / project_id
        if target.exists():
            shutil.rmtree(target)
