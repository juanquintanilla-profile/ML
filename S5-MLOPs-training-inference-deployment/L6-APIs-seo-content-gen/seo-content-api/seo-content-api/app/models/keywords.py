"""
Modelos para el endpoint de generación de keywords.
"""
from pydantic import BaseModel, Field
from typing import List


class KeywordRequest(BaseModel):
    """
    Request para generar keywords.
    """
    topic: str = Field(..., min_length=3, description="Tema principal")
    industry: str = Field(..., min_length=2, description="Industria o nicho")
    language: str = Field(default="es", description="Idioma (es, en, etc.)")
    
    class Config:
        json_schema_extra = {
            "example": {
                "topic": "marketing digital",
                "industry": "tecnología",
                "language": "es"
            }
        }


class KeywordResponse(BaseModel):
    """
    Response con keywords generadas.
    """
    seed_keywords: List[str] = Field(..., description="Keywords principales/semilla")
    long_tail_keywords: List[str] = Field(..., description="Keywords de cola larga")
    questions: List[str] = Field(..., description="Preguntas relacionadas")
    intent_classification: dict = Field(..., description="Clasificación por intención de búsqueda")
    
    class Config:
        json_schema_extra = {
            "example": {
                "seed_keywords": ["marketing digital", "SEO", "redes sociales"],
                "long_tail_keywords": ["cómo hacer marketing digital para pymes"],
                "questions": ["¿Qué es el marketing digital?"],
                "intent_classification": {
                    "informational": ["SEO", "marketing digital"],
                    "transactional": ["contratar agencia SEO"]
                }
            }
        }
