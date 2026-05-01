# Importa Depends desde FastAPI
# Depends se usa para crear dependencias (inyección automática)
from fastapi import Depends 

# Importa Annotated para tipado moderno con dependencias
from typing import Annotated

# Importa herramientas de SQLModel:
# - Field → definir columnas
# - SQLModel → base para modelos
# - create_engine → conexión a la BD
# - Session → manejo de sesiones
# - select → consultas SQL
from sqlmodel import Field, SQLModel, create_engine, Session, select

# Importa la configuración del proyecto (donde está la URL de la BD)
from app.core.config import settings


# Obtiene la URL de conexión a la base de datos desde settings
# Ejemplo: mysql://user:pass@localhost/db
url_connection = settings.DATABASE_URL


# Crea el engine (motor de conexión a la base de datos)
# echo=True → imprime todas las consultas SQL en consola (debug)
engine = create_engine(url_connection, echo=True)


# Función para crear las tablas en la base de datos
def crate_db_and_tables():
    # Toma todos los modelos definidos con SQLModel
    # y crea sus tablas en la base de datos
    SQLModel.metadata.create_all(engine)
    

# Función generadora que crea una sesión de base de datos
def get_session():  
    # Abre una sesión conectada al engine
    with Session(engine) as session:
        
        # Entrega la sesión al endpoint que la necesite
        yield session
        
        # Al terminar (automático), la sesión se cierra


# Crea una dependencia reutilizable llamada session_dep
# Annotated combina:
# - el tipo (Session)
# - la dependencia (Depends(get_session))
session_dep = Annotated[Session, Depends(get_session)]