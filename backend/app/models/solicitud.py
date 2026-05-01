# Importa SQLModel (base de los modelos) y Field (para definir columnas)
from sqlmodel import SQLModel, Field

# Optional permite que un campo pueda ser None (opcional)
from typing import Optional

# datetime para manejar fechas
from datetime import datetime


# Define la tabla "SolicitudesCredito" en la base de datos
# table=True indica que este modelo se convierte en tabla real
class SolicitudesCredito(SQLModel, table=True):
    
    # ID único de la solicitud (clave primaria)
    # Optional porque al inicio es None y la BD lo genera automáticamente
    id: Optional[int] = Field(default=None, primary_key=True)
    
    # Nombre del cliente
    nombre: str
    
    # Email del cliente
    email: str
    
    # Fecha de registro automática
    # default_factory ejecuta datetime.utcnow al crear el objeto
    fecha_registro: datetime = Field(default_factory=datetime.utcnow)
    
    # Salario mensual del cliente
    salario: float
    
    # Gastos mensuales del cliente
    gastos_mensuales: float
    
    # Tiempo que lleva como cliente (en meses)
    meses_cliente: int
    
    # Número de créditos activos actuales
    creditos_activos: int
    
    # Cantidad de retrasos en pagos anteriores
    retrasos_previos: int
    
    # Score crediticio (valor numérico que mide riesgo)
    score_crediticio: float
    
    # Ratio de endeudamiento (ej: gastos / salario)
    ratio_endeudamiento: float
    
    # Probabilidad de que el cliente entre en default (modelo ML)
    probabilidad_default: float
    
    # Decisión final del sistema (Aprobado / Rechazado)
    decision: str
    
    # Edad del cliente
    edad: int
    
    # Cédula del cliente (identificación)
    cedula: int