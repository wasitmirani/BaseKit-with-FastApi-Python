from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/")
async def create_user(user: UserCreate):
    return await UserService.create_user(user)

