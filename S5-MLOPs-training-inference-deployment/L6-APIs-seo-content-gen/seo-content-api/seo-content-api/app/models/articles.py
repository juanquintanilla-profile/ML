"""
Modelos para el endpoint de generación de artículos.
"""
from pydantic import BaseModel, Field
from typing import List


class ArticleSection(BaseModel):
    """
    Sección individual de un artículo con encabezado y contenido.
    """
    heading: str = Field(..., description="Encabezado (H2 o H3)")
    heading_level: int = Field(..., ge=2, le=3, description="Nivel de encabezado (2 o 3)")
    content: str = Field(..., min_length=50, description="Contenido de la sección")
    
    class Config:
        json_schema_extra = {
            "example": {
                "heading": "¿Qué es el SEO?",
                "heading_level": 2,
                "content": "El SEO es la optimización..."
            }
        }


class ArticleRequest(BaseModel):
    """
    Request para generar un artículo completo.
    """
    main_keyword: str = Field(..., min_length=2, description="Keyword principal")
    secondary_keywords: List[str] = Field(default=[], description="Keywords secundarias")
    word_count: int = Field(default=1000, ge=300, le=5000, description="Número de palabras objetivo")
    tone: str = Field(default="profesional", description="Tono del artículo")
    
    class Config:
        json_schema_extra = {
            "example": {
                "main_keyword": "marketing digital",
                "secondary_keywords": ["SEO", "redes sociales"],
                "word_count": 1500,
                "tone": "profesional"
            }
        }


class ArticleResponse(BaseModel):
    """
    Response con el artículo generado.
    """
    title: str = Field(..., description="Título del artículo (H1)")
    sections: List[ArticleSection] = Field(..., description="Secciones del artículo")
    keyword_density: dict = Field(..., description="Densidad de keywords principales")
    call_to_actions: List[str] = Field(..., description="CTAs incluidos en el artículo")
    
    class Config:
        json_schema_extra = {
            "example": {
                "title": "Guía Completa de Marketing Digital 2024",
                "sections": [],
                "keyword_density": {"marketing digital": 2.5},
                "call_to_actions": ["Contacta con nuestro equipo"]
            }
        }
