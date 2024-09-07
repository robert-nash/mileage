import datetime

from models.user import User, UserPersonalDetails


async def create_user():
    user_document = User(registered=datetime.datetime.now())
    return user_document


def update_user_personal_details(user: User, update: UserPersonalDetails):
    update_data = update.model_dump(exclude_unset=True)
    updated_user = user.model_copy(update=update_data)
    return updated_user
