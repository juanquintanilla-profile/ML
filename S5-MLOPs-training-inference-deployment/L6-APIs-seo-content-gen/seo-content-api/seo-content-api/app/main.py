"""
Aplicación principal FastAPI.
Configura routers, middleware y documentación.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import get_settings
from app.routers import (
    keywords_router,
    articles_router,
    metadata_router,
    faqs_router,
    social_router
)

# Obtener configuración
settings = get_settings()

# Crear aplicación FastAPI
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="""
    API REST para generación de contenido SEO utilizando Azure OpenAI.
    
    ## Funcionalidades
    
    * **Keywords**: Genera keywords semilla, long-tail y preguntas relevantes
    * **Articles**: Crea artículos completos optimizados para SEO
    * **Metadata**: Genera meta titles y descriptions optimizados
    * **FAQs**: Extrae FAQs y genera esquemas JSON-LD
    * **Social**: Adapta contenido para diferentes redes sociales
    
    ## Documentación
    
    - Swagger UI: `/docs`
    - ReDoc: `/redoc`
    """,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, especificar dominios permitidos
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registrar routers
app.include_router(keywords_router)
app.include_router(articles_router)
app.include_router(metadata_router)
app.include_router(faqs_router)
app.include_router(social_router)


@app.get("/")
async def root():
    """
    Endpoint raíz que retorna información de la API.
    """
    return {
        "message": "SEO Content API",
        "version": settings.app_version,
        "docs": "/docs",
        "endpoints": {
            "keywords": "/api/keywords/generate",
            "articles": "/api/articles/generate",
            "metadata": "/api/metadata/generate",
            "faqs": "/api/faqs/extract",
            "social": "/api/social/summaries"
        }
    }


@app.get("/health")
async def health_check():
    """
    Endpoint de health check para monitoring.
    """
    return {"status": "healthy", "service": settings.app_name}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
