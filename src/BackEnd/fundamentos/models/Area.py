from pydantic import BaseModel
from typing import List

class Area(BaseModel):
    id:str
    name:str
    deparments:List[str]
    