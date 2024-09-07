from beanie import init_beanie
from models.auth import Auth
from models.user import User
from config import settings
from motor.motor_asyncio import AsyncIOMotorClient


async def init_db():
    client = AsyncIOMotorClient(settings.mongo_connection_string)

    await init_beanie(
        database=client.get_default_database(), document_models=[User, Auth]
    )
