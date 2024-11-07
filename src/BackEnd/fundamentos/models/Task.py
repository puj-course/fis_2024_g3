from typing import List
from pydantic import BaseModel
from models.Status import Status

class Task(BaseModel):
    id: str
    name: str
    description: str
    project: str
    users: List[str]
    status: Status
