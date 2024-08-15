from fastapi import APIRouter
from db.userservice import register_user_db, get_all_users, get_result_user_db

user_router = APIRouter(prefix='/user')


@user_router.post('/register_user')
async def register_user(name: str, phone_number: str, level: str):
    user = register_user_db(name=name, phone_number=phone_number, level=level)
    return {"status": 1, "message": user}
