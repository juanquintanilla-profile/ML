"""
Router para el endpoint de generación de artículos.
"""
from fastapi import APIRouter, HTTPException
from app.models.articles import ArticleRequest, ArticleResponse
from app.services.articles_service import ArticlesService

router = APIRouter(prefix="/api/articles", tags=["Articles"])
service = ArticlesService()


@router.post("/generate", response_model=ArticleResponse)
async def generate_article(request: ArticleRequest):
    """
    Genera un artículo completo optimizado para SEO.
    
    - **main_keyword**: Keyword principal del artículo
    - **secondary_keywords**: Lista de keywords secundarias
    - **word_count**: Número objetivo de palabras (300-5000)
    - **tone**: Tono del artículo (profesional, casual, técnico, etc.)
    
    Returns:
        ArticleResponse con artículo estructurado, densidad de keywords y CTAs
    """
    try:
        return service.generate_article(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
