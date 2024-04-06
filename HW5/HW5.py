"""
Задание №3
Создать API для добавления нового пользователя в базу данных. Приложение
должно иметь возможность принимать POST запросы с данными нового
пользователя и сохранять их в базу данных.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс User с полями id, name, email и password.
Создайте список users для хранения пользователей.
Создайте маршрут для добавления нового пользователя (метод POST).
Реализуйте валидацию данных запроса и ответа.

"""

from fastapi import FastAPI, HTTPException
from typing import Optional
import uvicorn
from pydantic import BaseModel, EmailStr, Field



app = FastAPI()
users = []
id_counter = 0
class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    password: str = Field(..., min_length=4, max_length=5, )

@app.get("/")
def read_root():
    return {"Hello":"world"}
@app.get("/users")
def get_users():
    if len(users) == 0:
       return "No users found"
    return users
@app.post("/add_user")
def create_user(name:str, email:EmailStr, password:str):
    if not password:
        raise HTTPException(status_code=400, detail="wrong password")

    if not email:
        raise HTTPException(status_code=400, detail="wrong email address")
    global id_counter
    new_user = User(id=id_counter, name=name, email=email,password=password)
    users.append(new_user)
    id_counter += 1
    return "User added successfully"


@app.delete("/delete_user/{id}")
def delete_user(id: int):
    for i, user in enumerate(users):
        if user.id == id:
            del users[i]
            return "User deleted successfully"
    raise HTTPException(status_code=404, detail="User does not exist")

if __name__ == '__main__':
    uvicorn.run("HW5:app", host='127.0.0.1', port=8000)
