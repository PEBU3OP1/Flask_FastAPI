from typing import List

from fastapi import APIRouter,HTTPException
from HW6.model.database import users, database
from HW6.model.schemas import User, Userin
from pydantic import ValidationError
router = APIRouter()



@router.get("/users", response_model=List[User])
async def get_users():
    query = users.select()
    return await database.fetch_all(query)


@router.get("/users/{user_id}")
async def get_user(user_id:int):
    query = users.select().where(users.c.id == user_id)
    info = await database.fetch_one(query)
    return {'vse ploho'} if not info else info




@router.post("/add_user")
async def add_user(user:Userin):
    query = users.insert().values(name=user.name,last_name=user.name,bday = user.bday , email=user.email, address = user.address)
    await database.execute(query)
    return {"Vse OK"}

@router.put("/update_user/{user_id}", response_model=User)
async def update_user(user_id:int, new_user:Userin):
    query = users.update().where(users.c.id == user_id).values(**new_user.dict())
    await database.execute(query)
    return {**new_user.dict(), 'id': user_id}


@router.delete("/delete_user/{user_id}")
async def delete_user(user_id:int):
    query = users.delete().where(users.c.id == user_id)
    info_del = await database.execute(query)
    return {'msg': 'User deleted'} if info_del else {'User not found'}
