# Importa APIRouter desde FastAPI
# APIRouter permite crear grupos de rutas (modularizar el backend)
from fastapi import APIRouter

# Importa el módulo de endpoints de créditos
# Aquí está definido "credirouter" con sus rutas
from app.api.v1.endpoints import credit

# Importa el módulo de endpoints del agente (IA/chat)
# Aquí está definido "agenterouter"
from app.api.v1.endpoints import agente


# Crea el router principal
# Este router actuará como contenedor de todos los sub-routers
router = APIRouter()


# Incluye el router de créditos dentro del router principal
router.include_router(
    
    credit.credirouter,   # Router definido en credit.py (contiene endpoints de crédito)
    
    prefix="/credit",     # Prefijo de ruta:
                          # todas las rutas de este router empezarán con /credit
    
    tags=["Credit"]       # Etiqueta para la documentación automática (Swagger)
                          # agrupa estos endpoints bajo "Credit"
)


# Incluye el router del agente (chat con IA)
router.include_router(
    
    agente.agenterouter,  # Router definido en agente.py (contiene endpoints del agente)
    
    prefix="/agente",     # Prefijo de ruta:
                          # todas las rutas de este router empezarán con /agente
    
    tags=["Agente"]       # Etiqueta en Swagger para agrupar estos endpoints
)