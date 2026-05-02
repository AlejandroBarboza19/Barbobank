from langchain_community.utilities import SQLDatabase
from app.core.config import settings

# Configuración de la base de datos 
db_url = settings.DATABASE_URL

db_agent = SQLDatabase.from_uri(db_url)

# db_agent es el objeto que representa la conexión a la base de datos y que el agente 
# va a usar para hacer consultas SQL.

print("Tablas que ve el agente:", db_agent.get_usable_table_names())