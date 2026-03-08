from uuid import UUID


DEFAULT_PROFILE = {
    "id": str(UUID("00000000-0000-0000-0000-000000000001")),
    "name": "default-profile",
    "summary_model": "summary-model-v1",
    "question_model": "question-model-v1",
    "prompt_version": "2026-03-08",
}


class ModelProfileService:
    def select_profile(self, model_profile_id: str | None) -> dict:
        if not model_profile_id:
            return DEFAULT_PROFILE
        profile = dict(DEFAULT_PROFILE)
        profile["id"] = model_profile_id
        return profile

    def snapshot(self, profile: dict) -> str:
        return (
            f"{{\"modelProfileId\":\"{profile['id']}\","
            f"\"summaryModel\":\"{profile['summary_model']}\","
            f"\"questionModel\":\"{profile['question_model']}\","
            f"\"promptVersion\":\"{profile['prompt_version']}\"}}"
        )
