from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    
    # Base de datos 
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    
    @property
    def DATABASE_URL(self) -> str:
        return (
            f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"   

settings = Settings()

# En este archivo se define la clase Settings que hereda de BaseSettings de Pydantic. Esta clase se encarga de cargar 
# las variables de entorno necesarias para la configuración de la base de datos. 
# La propiedad DATABASE_URL construye la URL de conexión a la base de datos utilizando las variables de entorno. 
# La clase Config especifica que las variables de entorno se deben cargar desde un archivo 
# .env y que se deben ignorar las variables adicionales que no estén definidas en la clase. Finalmente, 
# se crea una instancia de Settings llamada settings que se puede usar en otras partes del código para acceder a la configuración.