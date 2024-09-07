from fastapi import APIRouter, Depends
from pydantic import BaseModel
from models.user import UserPersonalDetails
from services.auth import create_user, update_user_personal_details
from models.auth import EmailCredentialsRequest

router = APIRouter(prefix="/auth", tags=["auth"])


class RegisterResponse(BaseModel):
    id: str


@router.post("/register")
async def register(credentials: EmailCredentialsRequest):
    user = await create_user()
    user = update_user_personal_details(
        user, UserPersonalDetails(email=credentials.email)
    )
    await user.save()
    assert user.id
    return RegisterResponse(id=str(user.id))
