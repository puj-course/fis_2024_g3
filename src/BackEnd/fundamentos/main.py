from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.Database import db
from routes import Auth, Task, User, Area, Project  # Importa otros routers según tu proyecto

app = FastAPI(
    title="API TEAMCONNECT",
    description="API para gestionar proyecto TeamConnect",
    version="1.0.0"
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Cambia esto a la URL de tu frontend en producción si es necesario
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los headers
)

# Incluir routers
app.include_router(Auth.router)
app.include_router(User.router)  # Asegúrate de tener un router de usuarios
app.include_router(Task.router)
app.include_router(Project.router)
app.include_router(Area.router)

@app.on_event("startup")
async def startup_db_client():
    await db.connect()

@app.on_event("shutdown")
async def shutdown_db_client():
    await db.disconnect()

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de Gestión de Proyectos"}
