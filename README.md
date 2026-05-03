# 🏦 BarboBank — Simulador de Aprobaciones de Crédito con IA

> Proyecto exploratorio, investigativo y explicativo sobre lógica de decisión crediticia, consumo de modelos de Machine Learning en backend y la integración de un agente de IA en un sistema financiero simulado.

---

## 📌 ¿Qué es BarboBank?

BarboBank es un sistema que simula el proceso de aprobación de créditos bancarios. El usuario completa una solicitud ingresando sus datos financieros y personales; el sistema evalúa internamente esa información y toma una decisión de aprobación o rechazo basada en un modelo de Machine Learning.

Al finalizar la solicitud, el usuario puede interactuar con un **agente de IA consultor** que accede a su información mediante su cédula y puede responder todo tipo de preguntas sobre su solicitud y estado crediticio.

---

## 🎯 Objetivos del proyecto

- Demostrar cómo un modelo de ML puede integrarse al backend como parte central de la lógica de negocio.
- Mostrar la lógica de evaluación de riesgo crediticio en un entorno controlado y educativo.
- Implementar un agente de IA con acceso a base de datos dentro de un sistema funcional.

> ⚠️ Este es un proyecto educativo. En un entorno bancario real los parámetros de evaluación son considerablemente más complejos. Campos como "retrasos previos" no formarían parte de una solicitud directa al usuario en producción real.

---

## ⚙️ ¿Cómo funciona?

### Solicitud de crédito
El usuario ingresa:
- Salario mensual
- Deudas actuales
- Edad
- Meses como cliente
- Si ha tenido retrasos previos en pagos

El sistema calcula internamente:
- **Score crediticio**
- **Ratio de endeudamiento**

### Decisión crediticia (Modelo ML)
Todos los parámetros son enviados a un modelo de Machine Learning que estima la **probabilidad de default** (incumplimiento de pago).
Si probabilidad de default > 40% → Crédito RECHAZADO
Si probabilidad de default ≤ 40% → Crédito APROBADO

### Agente de IA consultor
Tras finalizar la solicitud, el usuario puede abrir un chat con un agente que:
- Solo necesita la **cédula del cliente** para consultar su información.
- Tiene acceso directo a la base de datos del sistema.
- Puede responder preguntas sobre la solicitud, el historial y el estado crediticio.

---

## 🛠️ Stack tecnológico

| Categoría | Tecnología |
|---|---|
| Framework web | FastAPI |
| ORM / Base de datos | SQLModel + PyMySQL + MySQL |
| Agente IA | LangChain + LangChain-OpenAI |
| Modelo ML | scikit-learn + joblib |
| Validación | Pydantic + pydantic-settings |
| Contenerización | Docker |
| Despliegue | AWS |
| Seguridad | cryptography |

### Dependencias principales
fastapi==0.136.1
uvicorn[standard]==0.45.0
sqlmodel==0.0.38
PyMySQL==1.1.2
pydantic==2.13.3
pydantic-settings==2.14.0
email-validator==2.3.0
python-dotenv==1.2.2
langchain-openai==1.2.1
langchain-community==0.4.1
langchain-core==1.3.2
pandas==3.0.2
joblib==1.5.3
scikit-learn==1.8.0
cryptography==47.0.0

---

## 🌿 Ramas del repositorio

| Rama | Descripción |
|---|---|
| `main` | Versión local — para desarrollo y pruebas |
| `cloud-deploy` | Versión configurada para despliegue en AWS |

---

## 🚀 Cómo correr el proyecto localmente

### 1. Clonar el repositorio
```bash
git clone https://github.com/AlejandroBarboza19/Barbobank/
cd barbobank
git checkout main
```

### 2. Configurar variables de entorno
Crea un archivo `.env` en la raíz con las siguientes variables:
```env
DB_HOST=
DB_PORT=
DB_USER=
DB_PASSWORD=
DB_NAME=
IA_API_KEY=

```

### 3. Levantar con Docker
```bash
docker-compose up --build
```

### 4. Acceder a la API

---

## ☁️ Despliegue en AWS

> 📹 *Próximamente: video tutorial paso a paso del despliegue en AWS.*

Para desplegar en la nube, cambia a la rama `cloud-deploy`:
```bash
git checkout cloud-deploy
```

Esta rama contiene las configuraciones adaptadas para el entorno de AWS (variables de entorno, puertos, ajustes de seguridad).

---

## 🤖 Modelo de Machine Learning

> 📹 *Próximamente: video explicando el modelo, las variables, el entrenamiento y la lógica de decisión.*

El modelo fue entrenado con variables estándar de evaluación crediticia y exportado con `joblib` para ser consumido directamente por el backend en cada solicitud.

---

## 📬 Contacto

Si tienes preguntas sobre el proyecto o quieres conectar:

**LinkedIn:** https://www.linkedin.com/in/alejandro-barboza-439303288/ 
**GitHub:** https://github.com/AlejandroBarboza19/

---

> *Proyecto desarrollado con fines educativos e investigativos.*