# Este archivo es la logica de negocio del proyecto aqui es donde se calculan las solicitudes 

from app.schemas.solicitud import Solicitud
from app.schemas.solicitud import ResultadoSistema
from app.schemas.solicitud import ResultadoSolicitud
import joblib
import pandas as pd


def calcular_ratio(datos: Solicitud) -> float: # calcula el ratio de endeudamiento de los usuarios y lo retorna como float
    ratio_endeudamiento = datos.gastos_mensuales / datos.salario
    return ratio_endeudamiento


def calcular_score(datos: Solicitud, ratio: float) -> float: # calcula el score apartir una formula y retorna un valor float 
    score_crediticio = (
        100
        - (ratio * 50)
        - (datos.retrasos_previos * 10)
        + ((datos.meses_cliente / 12) * 5)
        - (datos.creditos_activos * 5)
    )

    # Normalizar el score entre 0 y 100
    if score_crediticio < 0:
        score_crediticio = 0
    elif score_crediticio > 100:
        score_crediticio = 100

    return score_crediticio

# def evaluar_credito(datos: Solicitud):
    
#     ratio = calcular_ratio(datos)
#     score = calcular_score(datos, ratio)

#     resultado = {
#         "score": round(score,2),
#         "ratio": round(ratio,2)
#     }

#     return resultado

ml = joblib.load('app/ml/modelo_barbobank_creditosv2.pkl') # aqui leemos el modelo de machine learning 

def evaluar_credito(datos: Solicitud): # en esta funcion evaluamos la solicitud del usuario con el modelo de ml
    ratio = calcular_ratio(datos) 
    score = calcular_score(datos, ratio)

    df = pd.DataFrame([{
        "edad":                 datos.edad,
        "salario":              datos.salario,
        "gastos_mensuales":     datos.gastos_mensuales,
        "meses_cliente":        datos.meses_cliente,
        "creditos_activos":     datos.creditos_activos,
        "retrasos_previos":     datos.retrasos_previos,
        "score_crediticio":     score,
        "ratio_endeudamiento":  ratio
    }])

    probabilidad = ml.predict_proba(df)[:, 1][0]
    
    porcentaje_prob = round(probabilidad * 100, 1)
    
    return porcentaje_prob
# lo que hacemos aqui es traer los datos de la solicitud y cargarlos al modelo con pandas para que evalue 
# y esta funcion devuelve un porcentaje de default del 1 al 100

def decision_credito(probabilidad: float) -> object: # aqui tomamos las decision en base ael porcentaje dado por el modelo
    if probabilidad > 40:
        return "RECHAZADO"
    else:
        return "APROBADO"
    # si el porcentaje de defualt del usuario es mayor a 40 rechaza el credito 
    
# print(ml.feature_names_in_)

def Resultado_solicitud(datos: Solicitud) -> ResultadoSolicitud: # esta funcion le da a el usuario el resultado de la solicitudes
    ratio = calcular_ratio(datos)
    score = calcular_score(datos, ratio)
    probabilidad = evaluar_credito(datos)
    decision = decision_credito(probabilidad)

    resultado_solicitud = ResultadoSolicitud(
        solicitud=datos,
        resultado=ResultadoSistema(
            score_crediticio=score,
            ratio_endeudamiento=ratio,
            probabilidad_default=probabilidad,
            decision=decision,
            fecha_registro=pd.Timestamp.now()
        )
    )

    return resultado_solicitud
# Entonces esta funcion recolecta los datos de  la solicitud y los datos que el sistema calcula paara asi guardarlos en la BD



