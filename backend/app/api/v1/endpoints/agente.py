# para manejar los endpoints del agente
from fastapi import APIRouter
from app.services.agent_service import agente_sql_con_memoria
from app.schemas.agente_schemas import ChatInput, ChatOutput
from app.services.agent_service import _historiales
import traceback 
agenterouter = APIRouter()

# Define un endpoint POST en la ruta /chat_agente
# response_model=ChatOutput obliga a que la respuesta tenga esa estructura
@agenterouter.post("/chat_agente", response_model=ChatOutput)

# Función asíncrona (porque usa await)
# body: ChatInput → recibe los datos del cliente (mensaje + session_id)
async def chat(body: ChatInput):
    
    try:
        # Llama al agente de IA de forma asíncrona
        # ainvoke ejecuta el agente con entrada y configuración
        result = await agente_sql_con_memoria.ainvoke(
            
            # "input" es el mensaje que escribe el usuario
            {"input": body.mensaje},
            
            # config permite pasar configuraciones adicionales
            # aquí se usa session_id para mantener memoria de conversación
            config={"configurable": {"session_id": body.session_id}}
        )

        # Imprime en consola el resultado completo del agente (debug)
        print("RESULTADO:", result)

        # Procesa la respuesta:
        # - Si el resultado es un diccionario → intenta obtener "output"
        # - Si no lo es → convierte todo a string
        respuesta = result.get("output") if isinstance(result, dict) else str(result)

        # Validación: si la respuesta está vacía o es None
        if not respuesta:
            respuesta = "Sin respuesta del agente"

        # Retorna la respuesta usando el modelo ChatOutput
        # Esto asegura que el formato sea consistente
        return ChatOutput(
            respuesta=respuesta,          # texto generado por el agente
            session_id=body.session_id    # se devuelve el mismo session_id
        )

    # Captura cualquier error que ocurra durante la ejecución
    except Exception as e:
        
        # Imprime el error completo en consola (muy útil para debug)
        print("ERROR COMPLETO:")
        traceback.print_exc()

        # Retorna una respuesta controlada en caso de fallo
        return ChatOutput(
            respuesta="Error procesando la solicitud",  # mensaje genérico
            session_id=body.session_id                  # mantiene la sesión
        )
