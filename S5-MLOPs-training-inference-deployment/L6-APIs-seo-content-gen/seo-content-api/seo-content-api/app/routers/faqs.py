"""
Router para el endpoint de extracción de FAQs.
"""
from fastapi import APIRouter, HTTPException
from app.models.faqs import FAQRequest, FAQResponse
from app.services.faqs_service import FAQsService

router = APIRouter(prefix="/api/faqs", tags=["FAQs"])
service = FAQsService()


@router.post("/extract", response_model=FAQResponse)
async def extract_faqs(request: FAQRequest):
    """
    Extrae FAQs de un artículo y genera el esquema JSON-LD.
    
    - **article_content**: Contenido completo del artículo
    - **max_questions**: Máximo de preguntas a extraer (3-10)
    
    Returns:
        FAQResponse con FAQs y esquema JSON-LD FAQPage para rich snippets
    """
    try:
        return service.extract_faqs(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
