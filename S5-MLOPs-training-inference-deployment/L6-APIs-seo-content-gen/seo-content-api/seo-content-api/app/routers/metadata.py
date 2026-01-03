"""
Router para el endpoint de generación de metadatos SEO.
"""
from fastapi import APIRouter, HTTPException
from app.models.metadata import MetadataRequest, MetadataResponse
from app.services.metadata_service import MetadataService

router = APIRouter(prefix="/api/metadata", tags=["Metadata"])
service = MetadataService()


@router.post("/generate", response_model=MetadataResponse)
async def generate_metadata(request: MetadataRequest):
    """
    Genera múltiples variantes de meta titles y meta descriptions.
    
    - **article_title**: Título del artículo
    - **main_keyword**: Keyword principal
    - **article_excerpt**: Extracto o resumen del artículo
    
    Returns:
        MetadataResponse con 3-5 variantes de cada metadato
        
    Note:
        - Meta titles: máximo 60 caracteres
        - Meta descriptions: máximo 160 caracteres
    """
    try:
        return service.generate_metadata(request)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
