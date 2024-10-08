from pydantic import BaseModel, Field
from typing import List, Optional
from schema.Status import Status  # Asegúrate de tener un esquema de Status

class TaskBase(BaseModel):
    name: str = Field(..., example="Desarrollo de Módulo de Login")
    description: str = Field(..., example="Implementar el sistema de autenticación para la aplicación.")
    project: str = Field(..., example="64f9a8b2c8f8b23d1a24b9")
    users: List[str] = Field(..., example=["user_id_1", "user_id_2"])
    status: Status = Field(..., example="onGoing")

class TaskCreate(TaskBase):
    """
    Schema para la creación de una nueva tarea.
    """
    pass

class TaskUpdate(BaseModel):
    """
    Schema para la actualización de una tarea.
    """
    name: Optional[str]
    description: Optional[str]
    project: Optional[str]
    users: Optional[List[str]]
    status: Optional[Status]

class TaskInDB(TaskBase):
    """
    Representación de una tarea en la base de datos.
    """
    id: str = Field(..., example="64f9a8b2c8f8b23d1a25c9")

    class Config:
        orm_mode = True
