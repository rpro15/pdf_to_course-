from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass
class JobState:
    project_id: str
    status: str
    updated_at: datetime


class JobStateService:
    def build_state(self, project_id: str, status: str) -> JobState:
        return JobState(
            project_id=project_id,
            status=status,
            updated_at=datetime.now(timezone.utc),
        )
