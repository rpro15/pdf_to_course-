from datetime import datetime, timezone
from pathlib import Path


class ArtifactCleanupWorker:
    def cleanup_expired(self, base_path: str, expiration_before: datetime) -> list[str]:
        cleaned: list[str] = []
        root = Path(base_path)
        if not root.exists():
            return cleaned

        for item in root.glob("*.zip"):
            modified = datetime.fromtimestamp(item.stat().st_mtime, tz=timezone.utc)
            if modified < expiration_before:
                item.unlink(missing_ok=True)
                cleaned.append(str(item))
        return cleaned
