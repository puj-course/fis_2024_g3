# app/schemas/user.py
from enum import Enum
from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from bson import ObjectId
from models.Role import Role

# Función para manejar ObjectId en Pydantic
class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid ObjectId')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')


class UserBase(BaseModel):
    name: str = Field(..., example="Juan")
    lastname: str = Field(..., example="Perez")
    email: EmailStr = Field(..., example="juan.perez@example.com")
    role: Role = Field(..., example=Role.empleado)
    projects: List[PyObjectId] = []
    tasks: List[PyObjectId] = []


class UserCreate(UserBase):
    password: str = Field(..., min_length=6, example="strongpassword")


class UserInDB(UserBase):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}


class UserLogin(BaseModel):
    email: EmailStr = Field(..., example="juan.perez@example.com")
    password: str = Field(..., min_length=6, example="strongpassword")


class UserUpdate(UserBase):
    name: str = Field(..., example="Juan")
    lastname: str = Field(..., example="Perez")
    email: EmailStr = Field(..., example="juan.perez@example.com")
    role: Role = Field(..., example=Role.empleado)
    projects: List[PyObjectId] = []
    tasks: List[PyObjectId] = []
