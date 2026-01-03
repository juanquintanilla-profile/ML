"""
Modelos para el endpoint de generación de metadatos SEO.
"""
from pydantic import BaseModel, Field, field_validator
from typing import List


class MetaTitle(BaseModel):
    """
    Meta título individual con validación de longitud.
    """
    text: str = Field(..., description="Texto del meta title")
    character_count: int = Field(..., description="Número de caracteres")
    
    @field_validator('text')
    @classmethod
    def validate_length(cls, v):
        """Valida que el meta title no exceda 60 caracteres"""
        if len(v) > 60:
            raise ValueError('Meta title debe tener máximo 60 caracteres')
        return v


class MetaDescription(BaseModel):
    """
    Meta descripción individual con validación de longitud.
    """
    text: str = Field(..., description="Texto de la meta description")
    character_count: int = Field(..., description="Número de caracteres")
    
    @field_validator('text')
    @classmethod
    def validate_length(cls, v):
        """Valida que la meta description no exceda 160 caracteres"""
        if len(v) > 160:
            raise ValueError('Meta description debe tener máximo 160 caracteres')
        return v


class MetadataRequest(BaseModel):
    """
    Request para generar metadatos.
    """
    article_title: str = Field(..., min_length=5, description="Título del artículo")
    main_keyword: str = Field(..., min_length=2, description="Keyword principal")
    article_excerpt: str = Field(..., min_length=50, description="Extracto del artículo")
    
    class Config:
        json_schema_extra = {
            "example": {
                "article_title": "Guía de Marketing Digital",
                "main_keyword": "marketing digital",
                "article_excerpt": "Descubre las mejores estrategias..."
            }
        }


class MetadataResponse(BaseModel):
    """
    Response con variantes de metadatos.
    """
    meta_titles: List[MetaTitle] = Field(..., min_length=3, max_length=5)
    meta_descriptions: List[MetaDescription] = Field(..., min_length=3, max_length=5)
    
    class Config:
        json_schema_extra = {
            "example": {
                "meta_titles": [
                    {"text": "Marketing Digital 2024 | Guía Completa", "character_count": 38}
                ],
                "meta_descriptions": [
                    {"text": "Aprende marketing digital con nuestra guía...", "character_count": 120}
                ]
            }
        }
