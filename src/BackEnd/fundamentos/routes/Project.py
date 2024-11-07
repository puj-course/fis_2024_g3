from fastapi import APIRouter, Depends, HTTPException, status
from schema.Project import ProjectCreate, ProjectInDB, ProjectUpdate
from dependencies.Auth import is_admin, is_gerente_or_higher, get_current_user
from database.Database import db
from bson import ObjectId
from typing import List


router = APIRouter(
    tags=["project"]
)

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


@router.get("/projects/assigned", response_model=List[ProjectInDB])
async def get_assigned_projects(current_user: dict = Depends(get_current_user)):
    if current_user["role"] != "Gerente":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access forbidden: only managers can access assigned projects."
        )

    # Obtener proyectos asignados al gerente
    projects = await db.db.projects.find({"users": current_user["id"]}).to_list(length=100)

    # Enriquecer cada proyecto con sus tareas y los usuarios de cada tarea
    for project in projects:
        project["tasks"] = await db.db.tasks.find({"project": project["_id"]}).to_list(length=100)
        
        # Enriquecer cada tarea con la información de los usuarios asignados
        for task in project["tasks"]:
            task_users = await db.db.users.find({"_id": {"$in": task["users"]}}).to_list(length=100)
            task["user_names"] = [user["name"] for user in task_users]  # Agrega los nombres de los usuarios

    return projects

@router.patch("/projects/{project_id}/status")
async def update_project_status(project_id: str, status: str, current_user: dict = Depends(get_current_user)):
    if current_user["role"] != "Gerente":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access forbidden: only managers can update project statuses."
        )

    project = await db.db.projects.find_one({"_id": project_id, "users": current_user["id"]})
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Project not found")

    await db.db.projects.update_one({"_id": project_id}, {"$set": {"status": status}})
    return {"status": "updated"}

