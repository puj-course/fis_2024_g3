from motor.motor_asyncio import AsyncIOMotorClient
from core.config import settings

class Database:
    client: AsyncIOMotorClient = None
    db = None

    @classmethod
    async def connect(cls):
        cls.client = AsyncIOMotorClient(settings.mongodb_url)
        cls.db = cls.client[settings.mongodb_db]
        # Verificar la conexión
        try:
            await cls.db.command("ping")
            print("Conectado a MongoDB!")
        except Exception as e:
            print("No se pudo conectar a MongoDB", e)

    @classmethod
    async def disconnect(cls):
        cls.client.close()
        print("Desconectado de MongoDB")

# Instancia de la base de datos
db = Database()