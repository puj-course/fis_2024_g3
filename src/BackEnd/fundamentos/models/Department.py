from pydantic import BaseModel
from typing import List

class Department(BaseModel):
    id:str
    name:str
    description:str
    users:List[str]
    projects:List[str]