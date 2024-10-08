from pydantic import BaseModel, Field
from typing import List
from schema.Department import DepartmentInDB  # Importar el schema del department
from typing import Optional

class ProjectBase(BaseModel):
    name: str = Field(..., example="Proyecto Alpha")
    description: str = Field(..., example="Proyecto de desarrollo de software")
    department: DepartmentInDB = Field(..., example={
        "id": "64f9a8b2c8f8b23d1a21a9", 
        "name": "Departamento de Desarrollo",
        "description": "Responsable del desarrollo de software",
        "users": ["user_id_1", "user_id_2"],
        "projects": ["project_id_1", "project_id_2"]
    })
    users: List[str] = Field(..., example=["user_id_1", "user_id_2"])

class ProjectCreate(ProjectBase):
    """
    Schema para la creación de un nuevo proyecto.
    """
    pass

class ProjectUpdate(BaseModel):
    """
    Schema para la actualización de un proyecto.
    """
    name: Optional[str] = Field(None, example="Proyecto Beta")
    description: Optional[str] = Field(None, example="Descripción actualizada del proyecto")
    department: Optional[DepartmentInDB] = Field(None, example={
        "id": "64f9a8b2c8f8b23d1a21a9",
        "name": "Departamento de Marketing",
        "description": "Responsable de las campañas de marketing"
    })
    users: Optional[List[str]] = Field(None, example=["user_id_3", "user_id_4"])

class ProjectInDB(ProjectBase):
    """
    Representación de un proyecto en la base de datos.
    """
    id: str = Field(..., example="64f9a8b2c8f8b23d1a24b9")

    class Config:
        orm_mode = True
