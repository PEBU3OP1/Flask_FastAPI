"""
Задание №2
Создать API для получения списка фильмов по жанру. Приложение должно
иметь возможность получать список фильмов по заданному жанру.
Создайте модуль приложения и настройте сервер и маршрутизацию.
Создайте класс Movie с полями id, title, description и genre.
Создайте список movies для хранения фильмов.
Создайте маршрут для получения списка фильмов по жанру (метод GET).
Реализуйте валидацию данных запроса и ответа.
"""
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from typing import Optional

app2 = FastAPI()


class Movie(BaseModel):
    movie_id: int
    title: str
    description: Optional[str] = None
    genre: str


movies = [
    Movie(movie_id=0, title="Один", description="aaa", genre="Drama"),
    Movie(movie_id=1, title="Два", description="bbb", genre="Action"),
    Movie(movie_id=2, title="Три", description="ccc", genre="Comedy"),
    Movie(movie_id=3, title="Четыре", description="ddd", genre="Action")
]


if __name__ == '__main__':
    uvicorn.run("Sem5.2:app2", host="127.0.0.1", port=8000)