from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from sqlalchemy import select


class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db



async def user_by_email(self,email:str)->User:
    result =await self.db.execute(select(User).where(User.email == email)).first()
    return result.scalar_one_or_none()