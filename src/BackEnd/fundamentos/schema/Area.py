from pydantic import BaseModel, Field
from typing import List

class AreaBase(BaseModel):
    name: str = Field(..., example="Área de Tecnología")
    departments: List[str] = Field(..., example=["department_id_1", "department_id_2"])

class AreaCreate(AreaBase):
    """
    Schema para la creación de un área.
    """
    pass

class AreaUpdate(BaseModel):
    """
    Schema para la actualización de un área.
    """
    name: str = Field(None, example="Área de Marketing")
    departments: List[str] = Field(None, example=["department_id_3", "department_id_4"])

class AreaInDB(AreaBase):
    """
    Representación de un área en la base de datos.
    """
    id: str = Field(..., example="64f9a8b2c8f8b23d1a24b9")

    class Config:
        orm_mode = True
