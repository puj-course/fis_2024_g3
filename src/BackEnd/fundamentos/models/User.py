from pydantic import BaseModel, EmailStr
from typing import List
from models.Role import Role

class User(BaseModel):
    id: str
    name: str
    lastname: str
    email: EmailStr
    password_hash: str
    role: Role
    projects: List[str]
    tasks: List[str]
