class ModelProfileRollbackService:
    def build_compatibility_note(self, from_profile: str, to_profile: str) -> str:
        return (
            f"Rollback path available: {from_profile} -> {to_profile}. "
            "Stored projects keep previous run snapshots and remain readable."
        )
