from fastapi import APIRouter, Depends, HTTPException, status
from schema.Project import ProjectCreate, ProjectInDB, ProjectUpdate
from dependencies.Auth import is_admin, is_gerente_or_higher, get_current_user
from database.Database import db
from bson import ObjectId

router = APIRouter()

@router.post("/projects/", response_model=ProjectInDB, dependencies=[Depends(is_gerente_or_higher)])
async def create_project(project: ProjectCreate):
    """
    Gerentes o Admins pueden crear un proyecto dentro de un departamento.
    """
    existing_project = await db.db.projects.find_one({"name": project.name})
    if existing_project:
        raise HTTPException(status_code=400, detail="El proyecto ya existe.")
    
    project_dict = project.dict()
    result = await db.db.projects.insert_one(project_dict)
    
    return ProjectInDB(**project_dict)

@router.get("/projects/{project_id}", response_model=ProjectInDB)
async def get_project(project_id: str):
    """
    Cualquier usuario puede ver los detalles del proyecto.
    """
    if not ObjectId.is_valid(project_id):
        raise HTTPException(status_code=400, detail="ID del proyecto inválido.")
    
    project = await db.db.projects.find_one({"_id": ObjectId(project_id)})
    if not project:
        raise HTTPException(status_code=404, detail="Proyecto no encontrado.")
    
    return ProjectInDB(**project)

@router.delete("/projects/{project_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(is_admin)])
async def delete_project(project_id: str):
    """
    Solo los Admins pueden eliminar un proyecto y todas las tareas asociadas.
    """
    if not ObjectId.is_valid(project_id):
        raise HTTPException(status_code=400, detail="ID del proyecto inválido.")
    
    delete_result = await db.db.projects.delete_one({"_id": ObjectId(project_id)})
    if delete_result.deleted_count == 1:
        # Eliminar todas las tareas asociadas al proyecto
        await db.db.tasks.delete_many({"project": ObjectId(project_id)})
        return
    
    raise HTTPException(status_code=404, detail="Proyecto no encontrado.")
