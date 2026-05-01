# schemas funcionan para tener un estandar de como se manejan los datos en los endpoints, actuan como un molde
# para asegurar que la informacion cumpla con un formato especifico 
from pydantic import BaseModel, Field, EmailStr
from datetime import datetime

class Solicitud(BaseModel): # esta es la solicitud que manda el usuario 
    nombre: str = Field(..., min_length=3)
    edad: int = Field(..., ge=18, le=100)
    cedula: int 
    email: EmailStr = Field(..., description="Correo del solicitante")
    
    salario: float = Field(...)
    gastos_mensuales: float = Field(..., ge=0)
    
    meses_cliente: int = Field(..., ge=0)
    creditos_activos: int = Field(..., ge=0)
    retrasos_previos: int = Field(..., ge=0)    
    

class ResultadoSistema(BaseModel): # esta es la respuesta que calcula el sistema
    score_crediticio: float 
    ratio_endeudamiento: float 
    probabilidad_default: float = Field(ge=0, le=100)
    # prediccion: int #0 no default, 1 default
    decision: str
    fecha_registro: datetime
    

class ResultadoSolicitud(BaseModel): #Este es el objeto que une todo La solicitud y la respuesta para guardarlo en la base de datos 
    solicitud: Solicitud
    resultado: ResultadoSistema
    # fecha_registro: datetime, la dehca ya la va a manejar la base de datos 
    

    