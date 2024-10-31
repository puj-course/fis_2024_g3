from fastapi import APIRouter, Depends, HTTPException, status
from schema.Task import TaskCreate, TaskInDB, TaskUpdate
from dependencies.Auth import is_lider_or_higher, get_current_user
from database.Database import db
from bson import ObjectId

router = APIRouter()

@router.post("/tasks/", response_model=TaskInDB, dependencies=[Depends(is_lider_or_higher)])
async def create_task(task: TaskCreate):
    """
    Líderes o Gerentes pueden crear tareas dentro de proyectos específicos.
    """
    task_dict = task.dict()
    result = await db.db.tasks.insert_one(task_dict)
    
    return TaskInDB(**task_dict)

@router.get("/tasks/{task_id}", response_model=TaskInDB)
async def get_task(task_id: str):
    """
    Cualquier usuario puede ver una tarea, pero solo puede actualizar las asignadas a ellos.
    """
    if not ObjectId.is_valid(task_id):
        raise HTTPException(status_code=400, detail="ID de la tarea inválido.")
    
    task = await db.db.tasks.find_one({"_id": ObjectId(task_id)})
    if not task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada.")
    
    return TaskInDB(**task)

@router.put("/tasks/{task_id}", response_model=TaskInDB, dependencies=[Depends(get_current_user)])
async def update_task(task_id: str, task: TaskUpdate, current_user: dict = Depends(get_current_user)):
    """
    Los usuarios pueden actualizar el estado de las tareas asignadas, y los Líderes o Gerentes pueden modificar cualquier tarea.
    """
    if not ObjectId.is_valid(task_id):
        raise HTTPException(status_code=400, detail="ID de la tarea inválido.")
    
    # Verificar si el usuario tiene permiso para actualizar esta tarea
    existing_task = await db.db.tasks.find_one({"_id": ObjectId(task_id)})
    if not existing_task:
        raise HTTPException(status_code=404, detail="Tarea no encontrada.")
    
    # Si el usuario es Empleado, verifica que solo puede actualizar su estado
    if current_user["role"] == "Empleado" and ObjectId(current_user["_id"]) not in existing_task["users"]:
        raise HTTPException(status_code=403, detail="No tienes permisos para modificar esta tarea.")

    # Actualizar la tarea
    update_data = task.dict(exclude_unset=True)
    update_result = await db.db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": update_data})
    
    if update_result.modified_count == 1:
        updated_task = await db.db.tasks.find_one({"_id": ObjectId(task_id)})
        return TaskInDB(**updated_task)

    raise HTTPException(status_code=400, detail="No se pudo actualizar la tarea.")
