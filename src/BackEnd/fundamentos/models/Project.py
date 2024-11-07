from pydantic import BaseModel
from models.Department import Department
from typing import List
from models.Status import Status

class Project(BaseModel):
    id:str
    name: str
    description: str
    deparment:Department 
    users: List[str]
    status: Status