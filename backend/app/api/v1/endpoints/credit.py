from fastapi import APIRouter
from app.schemas.solicitud import Solicitud
from app.core.database import session_dep
from sqlmodel import Session
from app.models.solicitud import SolicitudesCredito
from app.services.credit_service import Resultado_solicitud
from app.schemas.solicitud import ResultadoSolicitud

credirouter = APIRouter() # creamos la "direccion" para poder importarla en router que asu vez lo importa en main

def guardar_solicitud(ResultadoSolicitud: ResultadoSolicitud, session: Session): # Creamos la funcion para guardar las solicitudes en la base de datos 
        entrada = SolicitudesCredito(
            nombre=ResultadoSolicitud.solicitud.nombre,
            edad=ResultadoSolicitud.solicitud.edad,
            cedula=ResultadoSolicitud.solicitud.cedula,
            email=ResultadoSolicitud.solicitud.email,
            salario=ResultadoSolicitud.solicitud.salario,
            gastos_mensuales=ResultadoSolicitud.solicitud.gastos_mensuales,
            meses_cliente=ResultadoSolicitud.solicitud.meses_cliente,
            creditos_activos=ResultadoSolicitud.solicitud.creditos_activos,
            retrasos_previos=ResultadoSolicitud.solicitud.retrasos_previos,
            score_crediticio=ResultadoSolicitud.resultado.score_crediticio,
            ratio_endeudamiento=ResultadoSolicitud.resultado.ratio_endeudamiento,
            probabilidad_default=ResultadoSolicitud.resultado.probabilidad_default,
            decision=ResultadoSolicitud.resultado.decision
        )
        # Entonces entrada ya es todo los datos de la solicitud y el resultado del sistema 
   
    
       
        session.add(entrada)
        session.commit()
        session.refresh(entrada)
        #para guardar en la base de datos 


@credirouter.post("/solicitud")
def recibir_solicitud(datos: Solicitud, session: session_dep):
    
    resultado = Resultado_solicitud(datos)  # ← ya hace todo el cálculo
    guardar_solicitud(resultado, session)
    
    return {"status": "enviado", "data": resultado}

# esta funcion con una sesion para guardar los datos en l bd recibe la solicitud calcula el resultado con la funcion
# resultado solicitud guarda el resultado en la base de datos y devuelve un diccionario con el resultaado adentro 


