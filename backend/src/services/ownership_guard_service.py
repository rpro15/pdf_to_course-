class OwnershipGuardService:
    def assert_owner(self, project_owner_id: str, actor_id: str) -> None:
        if project_owner_id != actor_id:
            raise PermissionError("Single-user ownership policy violation")
