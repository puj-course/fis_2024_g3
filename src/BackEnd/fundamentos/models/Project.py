
from pydantic import BaseModel
from models.Department import Department
from typing import List
class Project(BaseModel):
    id:str
    name: str
    description: str
    deparment:Department 
    users: List[str]