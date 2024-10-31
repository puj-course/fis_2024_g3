from fastapi import APIRouter, Depends, HTTPException, status
from schema.Area import AreaCreate, AreaUpdate, AreaInDB
from database.Database import db
from typing import List
from bson import ObjectId
from dependencies.Auth import is_admin

router = APIRouter()

@router.post("/areas/", response_model=AreaInDB, dependencies=[Depends(is_admin)])
async def create_area(area: AreaCreate):
    """
    Admins pueden crear un área.
    """
    existing_area = await db.db.areas.find_one({"name": area.name})
    if existing_area:
        raise HTTPException(status_code=400, detail="El área ya existe.")
    
    area_dict = area.dict()
    result = await db.db.areas.insert_one(area_dict)
    
    return AreaInDB(**area_dict)

@router.get("/areas/{area_id}", response_model=AreaInDB)
async def get_area(area_id: str):
    """
    Cualquier usuario puede obtener información sobre un área.
    """
    if not ObjectId.is_valid(area_id):
        raise HTTPException(status_code=400, detail="ID del área inválido.")
    
    area = await db.db.areas.find_one({"_id": ObjectId(area_id)})
    if not area:
        raise HTTPException(status_code=404, detail="Área no encontrada.")
    
    return AreaInDB(**area)

@router.put("/areas/{area_id}", response_model=AreaInDB, dependencies=[Depends(is_admin)])
async def update_area(area_id: str, area: AreaUpdate):
    """
    Admins pueden actualizar un área.
    """
    if not ObjectId.is_valid(area_id):
        raise HTTPException(status_code=400, detail="ID del área inválido.")
    
    update_data = area.dict(exclude_unset=True)
    update_result = await db.db.areas.update_one({"_id": ObjectId(area_id)}, {"$set": update_data})
    
    if update_result.modified_count == 1:
        updated_area = await db.db.areas.find_one({"_id": ObjectId(area_id)})
        return AreaInDB(**updated_area)

    raise HTTPException(status_code=404, detail="Área no encontrada.")

@router.delete("/areas/{area_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(is_admin)])
async def delete_area(area_id: str):
    """
    Admins pueden eliminar un área.
    """
    if not ObjectId.is_valid(area_id):
        raise HTTPException(status_code=400, detail="ID del área inválido.")
    
    delete_result = await db.db.areas.delete_one({"_id": ObjectId(area_id)})
    if delete_result.deleted_count == 1:
        return
    
    raise HTTPException(status_code=404, detail="Área no encontrada.")
