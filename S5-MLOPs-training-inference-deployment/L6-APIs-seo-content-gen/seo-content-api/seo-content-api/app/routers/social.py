"""
Router para el endpoint de generación de contenido social.
"""
from fastapi import APIRouter, HTTPException
from app.models.social import SocialRequest, SocialResponse
from app.services.social_service import SocialService

router = APIRouter(prefix="/api/social", tags=["Social Media"])
service = SocialService()


@router.post("/summaries", response_model=SocialResponse)
async def generate_social_summaries(request: SocialRequest):
    """
    Genera contenido optimizado para múltiples redes sociales.
    
    - **article_title**: Título del artículo
    - **article_content**: Contenido del artículo a adaptar
    - **target_platforms**: Lista de plataformas (twitter, linkedin, instagram, facebook)
    
    Returns:
        SocialResponse con contenido adaptado para cada plataforma solicitada
        
    Note:
        - Twitter: máximo 280 caracteres
        - LinkedIn: tono profesional
        - Instagram: máximo 30 hashtags
        - Facebook: tono conversacional
    """
    try:
        return service.generate_social_content(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
