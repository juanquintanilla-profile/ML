"""
Modelos para el endpoint de generación de contenido social.
"""
from pydantic import BaseModel, Field, field_validator
from typing import List, Optional


class TwitterContent(BaseModel):
    """
    Contenido optimizado para Twitter/X.
    """
    text: str = Field(..., description="Texto del tweet")
    hashtags: List[str] = Field(..., description="Hashtags sugeridos")
    character_count: int = Field(..., description="Conteo de caracteres")
    
    @field_validator('text')
    @classmethod
    def validate_length(cls, v):
        """Valida límite de 280 caracteres de Twitter"""
        if len(v) > 280:
            raise ValueError('Tweet debe tener máximo 280 caracteres')
        return v


class LinkedInContent(BaseModel):
    """
    Contenido optimizado para LinkedIn.
    """
    text: str = Field(..., description="Texto del post")
    hashtags: List[str] = Field(..., description="Hashtags profesionales")
    call_to_action: str = Field(..., description="CTA específico")


class InstagramContent(BaseModel):
    """
    Contenido optimizado para Instagram.
    """
    caption: str = Field(..., description="Caption del post")
    hashtags: List[str] = Field(..., max_length=30, description="Hashtags (máx 30)")
    call_to_action: str = Field(..., description="CTA para Instagram")


class FacebookContent(BaseModel):
    """
    Contenido optimizado para Facebook.
    """
    text: str = Field(..., description="Texto del post")
    hashtags: List[str] = Field(..., description="Hashtags sugeridos")
    call_to_action: str = Field(..., description="CTA específico")


class SocialRequest(BaseModel):
    """
    Request para generar contenido social.
    """
    article_title: str = Field(..., min_length=5, description="Título del artículo")
    article_content: str = Field(..., min_length=100, description="Contenido del artículo")
    target_platforms: List[str] = Field(
        ..., 
        description="Plataformas objetivo (twitter, linkedin, instagram, facebook)"
    )
    
    @field_validator('target_platforms')
    @classmethod
    def validate_platforms(cls, v):
        """Valida que las plataformas sean válidas"""
        valid_platforms = {'twitter', 'linkedin', 'instagram', 'facebook'}
        for platform in v:
            if platform.lower() not in valid_platforms:
                raise ValueError(f'Plataforma inválida: {platform}')
        return [p.lower() for p in v]
    
    class Config:
        json_schema_extra = {
            "example": {
                "article_title": "Guía de Marketing Digital",
                "article_content": "El marketing digital es esencial...",
                "target_platforms": ["twitter", "linkedin"]
            }
        }


class SocialResponse(BaseModel):
    """
    Response con contenido para múltiples plataformas.
    """
    twitter: Optional[TwitterContent] = None
    linkedin: Optional[LinkedInContent] = None
    instagram: Optional[InstagramContent] = None
    facebook: Optional[FacebookContent] = None
