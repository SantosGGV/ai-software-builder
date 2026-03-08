from fastapi import FastAPI

# Creamos la instancia principal de la aplicación
app = FastAPI(
    title="AI Software Builder",
    description="API principal del sistema de generación automática de software basado en IA",
    version="0.1"
)

# Endpoint básico de comprobación
@app.get("/health")
def health_check():
    """
    Endpoint utilizado para comprobar que la API está funcionando correctamente.
    """
    return {
        "status": "ok",
        "service": "ai-software-builder"
    }
