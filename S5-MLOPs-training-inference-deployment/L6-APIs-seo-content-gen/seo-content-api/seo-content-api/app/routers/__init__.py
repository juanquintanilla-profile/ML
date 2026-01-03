"""
Exporta todos los routers.
"""
from .keywords import router as keywords_router
from .articles import router as articles_router
from .metadata import router as metadata_router
from .faqs import router as faqs_router
from .social import router as social_router

__all__ = [
    "keywords_router",
    "articles_router",
    "metadata_router",
    "faqs_router",
    "social_router",
]
