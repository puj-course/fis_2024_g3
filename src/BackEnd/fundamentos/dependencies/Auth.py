# dependencies/auth.py

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from bson import ObjectId
from typing import Optional
from core.config import settings
from core.security import verify_password, get_password_hash, create_access_token
from database.Database import db
from schema.User import UserInDB, Role

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")  # Ajusta el tokenUrl según tus rutas

async def get_current_user(token: str = Depends(oauth2_scheme)) -> UserInDB:
    """
    Obtiene el usuario actual a partir del token JWT.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="No se pudo validar las credenciales",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        user_id: str = payload.get("sub")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    user_data = await db.db.users.find_one({"_id": ObjectId(user_id)})
    if user_data is None:
        raise credentials_exception

    return UserInDB(**user_data)

async def get_current_user_role(current_user: UserInDB = Depends(get_current_user)) -> Role:
    """
    Obtiene el rol del usuario actual.
    """
    return current_user.role

async def is_admin(role: Role = Depends(get_current_user_role)):
    """
    Verifica si el usuario tiene rol de admin.
    """
    if role != Role.admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos para realizar esta operación"
        )

async def is_gerente_or_higher(role: Role = Depends(get_current_user_role)):
    """
    Verifica si el usuario tiene rol de gerente o superior.
    """
    if role not in [Role.admin, Role.gerente]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos para realizar esta operación"
        )

async def is_lider_or_higher(role: Role = Depends(get_current_user_role)):
    """
    Verifica si el usuario tiene rol de líder o superior.
    """
    if role not in [Role.admin, Role.gerente, Role.lider]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="No tienes permisos para realizar esta operación"
        )
