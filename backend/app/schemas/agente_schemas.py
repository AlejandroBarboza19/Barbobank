# Este arcivo es el esquema del agente maneja es el esquema que dice que datos y como se van a manejar
# para tener la conversacion con el agente

from pydantic import BaseModel

class ChatInput(BaseModel): # esta clase es el mensaje que entra del usuario 
    mensaje: str
    session_id: str = "default"

class ChatOutput(BaseModel): # esta clase es el mensaje que saca el agente
    respuesta: str
    session_id: str