from pydantic import BaseModel, Field
from typing import List

class DepartmentBase(BaseModel):
    name: str = Field(..., example="Departamento de Desarrollo")
    description: str = Field(..., example="Responsable del desarrollo de software.")
    users: List[str] = Field(..., example=["user_id_1", "user_id_2"])
    projects: List[str] = Field(..., example=["project_id_1", "project_id_2"])

class DepartmentCreate(DepartmentBase):
    """
    Schema para la creación de un nuevo departamento.
    """
    pass

class DepartmentUpdate(BaseModel):
    """
    Schema para la actualización de un departamento.
    """
    name: str = Field(None, example="Departamento de Marketing")
    description: str = Field(None, example="Responsable de las campañas de marketing.")
    users: List[str] = Field(None, example=["user_id_3", "user_id_4"])
    projects: List[str] = Field(None, example=["project_id_3", "project_id_4"])

class DepartmentInDB(DepartmentBase):
    """
    Representación de un departamento en la base de datos.
    """
    id: str = Field(..., example="64f9a8b2c8f8b23d1a21a9")

    class Config:
        orm_mode = True
