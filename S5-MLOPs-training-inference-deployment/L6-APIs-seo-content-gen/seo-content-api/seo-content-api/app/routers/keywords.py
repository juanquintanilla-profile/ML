"""
Router para el endpoint de generación de keywords.
"""
from fastapi import APIRouter, HTTPException
from app.models.keywords import KeywordRequest, KeywordResponse
from app.services.keywords_service import KeywordsService

router = APIRouter(prefix="/api/keywords", tags=["Keywords"])
service = KeywordsService()


@router.post("/generate", response_model=KeywordResponse)
async def generate_keywords(request: KeywordRequest):
    """
    Genera keywords semilla, long-tail, preguntas e intención de búsqueda.
    
    - **topic**: Tema principal para generar keywords
    - **industry**: Industria o nicho del negocio
    - **language**: Idioma de las keywords (por defecto: es)
    
    Returns:
        KeywordResponse con keywords clasificadas
    """
    try:
        return service.generate_keywords(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
