from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.router import router as api_router
from app.core.database import  crate_db_and_tables
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI()

# Configuración vital para que el frontend pueda hablar con el backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite cualquier origen (ideal para desarrollo local)
    allow_credentials=True,
    allow_methods=["*"],  # Esto arreglará el error 405 en las peticiones OPTIONS
    allow_headers=["*"],
)

app.include_router(api_router)

@app.get("/prueba")
def obtener_estado(): # es una mini funcion para ver que fastpi esta corriendo correctamente
    return {"hola, Fast api esta funcionando correctamente!"}

@app.get("/formulario")
def formulario_solicitud():
    html = Path("templates/formulario_solicitud.html").read_text(encoding="utf-8")
    return HTMLResponse(content=html)

@app.get("/chat")
def formulario_chat_agente():
    html = Path("templates/chat_agente.html").read_text(encoding="utf-8")
    return HTMLResponse(content=html)

@app.get("/")
def home():
    html = Path("templates/home.html").read_text(encoding="utf-8")
    return HTMLResponse(content=html)


#voy a crear una funcion para que al arrancar la app se creen las tablas de las base de datos 
@app.on_event('startup')
def on_startup():
    crate_db_and_tables()
