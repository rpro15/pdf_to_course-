from fastapi import Header, HTTPException


async def single_user_guard(owner_id: str, x_actor_id: str | None = Header(default=None)) -> None:
    if x_actor_id and x_actor_id != owner_id:
        raise HTTPException(status_code=403, detail="Single-user ownership policy violation")
