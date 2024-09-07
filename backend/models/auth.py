import datetime

from beanie import Document, Link
from pydantic import BaseModel

from models.user import User


class Password(BaseModel):
    value: str


class EmailCredentials(BaseModel):
    email: str
    password: Password


class EmailCredentialsRequest(BaseModel):
    email: str
    password: str


class Auth(Document):
    user: Link[User]
    credentials: EmailCredentials
    """
        The credentials used for this authentication method.
        It is intended that in the future there will be a union of
        different credentials such as PhoneCredentials, OauthCredentials
    """
    first_used: datetime.datetime
