# routers/auth.py
from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from schema.User import UserCreate, UserInDB, UserLogin
from schema.Token import Token
from twilio.rest import Client
from database.Database import db
from models.User import User
from core.security import verify_password, get_password_hash, create_access_token
from core.config import settings
from bson import ObjectId

router = APIRouter(
    tags=["auth"]
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


@router.post("/register", response_model=UserInDB)
async def register(user: UserCreate):
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
    
    result = await db.db.users.insert_one(user_dict)
    created_user = await db.db.users.find_one({"_id": result.inserted_id})

    send_welcome_sms(user.number,user.name)

    return created_user


@router.post("/login", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Buscar el usuario por email
    user = await db.db.users.find_one({"email": form_data.username})
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Verificar la contraseña
    if not verify_password(form_data.password, user["password_hash"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Crear el token de acceso
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    access_token = create_access_token(
        data={"sub": str(user["_id"])},
        expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}
