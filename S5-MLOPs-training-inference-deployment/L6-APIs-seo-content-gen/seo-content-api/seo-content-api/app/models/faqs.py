"""
Modelos para el endpoint de extracción de FAQs.
"""
from pydantic import BaseModel, Field
from typing import List


class FAQ(BaseModel):
    """
    Pregunta y respuesta individual.
    """
    question: str = Field(..., min_length=10, description="Pregunta")
    answer: str = Field(..., min_length=50, max_length=500, description="Respuesta (50-150 palabras)")
    
    class Config:
        json_schema_extra = {
            "example": {
                "question": "¿Qué es el SEO?",
                "answer": "El SEO es la optimización para motores de búsqueda..."
            }
        }


class FAQRequest(BaseModel):
    """
    Request para extraer FAQs de un artículo.
    """
    article_content: str = Field(..., min_length=100, description="Contenido del artículo")
    max_questions: int = Field(default=5, ge=3, le=10, description="Máximo de preguntas a generar")
    
    class Config:
        json_schema_extra = {
            "example": {
                "article_content": "El SEO es fundamental para...",
                "max_questions": 5
            }
        }


class FAQResponse(BaseModel):
    """
    Response con FAQs y esquema JSON-LD.
    """
    faqs: List[FAQ] = Field(..., description="Lista de FAQs extraídas")
    json_ld_schema: dict = Field(..., description="Esquema JSON-LD FAQPage")
    
    class Config:
        json_schema_extra = {
            "example": {
                "faqs": [
                    {"question": "¿Qué es el SEO?", "answer": "El SEO es..."}
                ],
                "json_ld_schema": {
                    "@context": "https://schema.org",
                    "@type": "FAQPage"
                }
            }
        }
