from fastapi import FastAPI
from .database.Database import db
from routes import Auth, User  # Importa otros routers según tu proyecto

app = FastAPI(
    title="API TEAMCONNECT",
    description="API para gestionar proyecto TeamConnect",
    version="1.0.0"
)

# Incluir routers
app.include_router(Auth.router)
app.include_router(User.router)  # Asegúrate de tener un router de usuarios

@app.on_event("startup")
async def startup_db_client():
    await db.connect()

@app.on_event("shutdown")
async def shutdown_db_client():
    await db.disconnect()

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de Gestión de Proyectos"}
