from datetime import datetime

from pydantic import BaseModel, EmailStr, Field, field_validator


class User(BaseModel):
    id:int
    name: str = Field(title="name", max_length=32)
    last_name: str = Field(title="last_name", max_length=32)
    bday: datetime = Field(title="bday", default='YYYY-MM-DD')
    email: EmailStr = Field(title="email", max_length=50)
    address: str = Field(title="address", max_length=32)


class Userin(BaseModel):
    name: str = Field(title="name", max_length=32)
    last_name: str = Field(title="last_name", max_length=32)
    bday: datetime = Field(title="bday", default='YYYY-MM-DD')
    email: EmailStr = Field(title="email", max_length=50)
    address: str = Field(title="address", max_length=32)

