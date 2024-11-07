from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional  # Asegúrate de que el modelo Department esté importado correctamente
from database import db
from dependencies.Auth import is_admin, is_gerente_or_higher, get_current_user
from schema.Department import DepartmentInDB


router = APIRouter()

@router.get("/departments/assigned", response_model=Optional[DepartmentInDB])
async def get_assigned_department(current_user: dict = Depends(get_current_user)):
    # Verificar si el usuario tiene el rol de "Líder"
    if current_user["role"] != "Líder":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Access forbidden: only leaders can access their department."
        )

    # Buscar el departamento asignado al líder
    department = await db.db.departments.find_one({"users": current_user["id"]})
    
    if not department:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No department assigned to this leader."
        )

    return department
