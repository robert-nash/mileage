import datetime
from typing import Optional
from beanie import Document
from pydantic import BaseModel


class UserPersonalDetails(BaseModel):
    email: Optional[str] = None


class BaseUser(UserPersonalDetails, BaseModel):
    registered: datetime.datetime


class User(BaseUser, Document): ...
