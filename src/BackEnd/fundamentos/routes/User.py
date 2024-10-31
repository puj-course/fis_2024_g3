from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from bson import ObjectId
from twilio.rest import Client
from schema.User import UserCreate, UserInDB, UserUpdate, Role
from database.Database import db
from dependencies.Auth import is_admin, is_gerente_or_higher, get_current_user
from core.security import get_password_hash
from schema.User import PyObjectId
from core.config import settings

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

# Función para convertir ObjectId a str en las respuestas
def user_helper(user: dict) -> UserInDB:
    return UserInDB(
        id=str(user["_id"]),
        name=user["name"],
        lastname=user["lastname"],
        email=user["email"],
        role=user["role"],
        number =user["number"],
        projects=[str(project) for project in user.get("projects", [])],
        tasks=[str(task) for task in user.get("tasks", [])]
    )


def send_welcome_sms(phone_number: str, user_name: str):
    client = Client(settings.tw_Sid,settings.tw_token)
    try:
        message = client.messages.create(
            body=f"Bienvenido {user_name} a TeamConnect, tu cuenta ha sido creada exitosamente.",
            from_=settings.tw_number,
            to=phone_number
        )
        print(f"SMS enviado con éxito a {phone_number}. SID del mensaje: {message.sid}")
    except Exception as e:
        print(f"Error al enviar SMS: {str(e)}")


@router.post("/", response_model=UserInDB, status_code=status.HTTP_201_CREATED, dependencies=[Depends(is_admin)])
async def create_user(user: UserCreate):
    # Verificar si el email ya está registrado
    existing_user = await db.db.users.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El email ya está registrado"
        )
    
    # Hashear la contraseña
    hashed_password = get_password_hash(user.password)
    
    # Crear el usuario en la base de datos
    user_dict = user.dict()
    user_dict.pop("password")  # Eliminar la contraseña plana
    user_dict["password_hash"] = hashed_password
    user_dict["projects"] = []
    user_dict["tasks"] = []
    
    result = await db.db.users.insert_one(user_dict)
    created_user = await db.db.users.find_one({"_id": result.inserted_id})

    send_welcome_sms(user.number, user.name)
    
    return user_helper(created_user)

@router.get("/users", response_model=List[UserInDB], dependencies=[Depends(is_gerente_or_higher)])
async def get_users():
    users = []
    cursor = db.db.users.find()
    async for user in cursor:
        users.append(user_helper(user))
    return users

@router.get("/{user_id}", response_model=UserInDB, dependencies=[Depends(is_gerente_or_higher)])
async def get_user(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID de usuario inválido"
        )
    
    user = await db.db.users.find_one({"_id": ObjectId(user_id)})
    if user:
        return user_helper(user)
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado"
    )

@router.put("/{user_id}", response_model=UserInDB, dependencies=[Depends(is_gerente_or_higher)])
async def update_user(user_id: str, user: UserUpdate):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID de usuario inválido"
        )
    
    update_data = user.dict(exclude_unset=True)
    
    # Si se está actualizando la contraseña, hashearla
    if "password" in update_data:
        update_data["password_hash"] = get_password_hash(update_data.pop("password"))
    
    if update_data:
        update_result = await db.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": update_data})
        if update_result.modified_count == 1:
            updated_user = await db.db.users.find_one({"_id": ObjectId(user_id)})
            if updated_user:
                return user_helper(updated_user)
    
    existing_user = await db.db.users.find_one({"_id": ObjectId(user_id)})
    if existing_user:
        return user_helper(existing_user)
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado"
    )

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(is_admin)])
async def delete_user(user_id: str):
    if not ObjectId.is_valid(user_id):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="ID de usuario inválido"
        )
    
    delete_result = await db.db.users.delete_one({"_id": ObjectId(user_id)})
    if delete_result.deleted_count == 1:
        return
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Usuario no encontrado"
    )

@router.get("/users/me",response_model = UserInDB)
async def get_me(current_user:UserInDB = Depends(get_current_user)):
    return current_user



