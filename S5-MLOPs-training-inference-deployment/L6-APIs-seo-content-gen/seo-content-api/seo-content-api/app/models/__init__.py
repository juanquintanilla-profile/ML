"""
Exporta todos los modelos para facilitar imports.
"""
from .keywords import KeywordRequest, KeywordResponse
from .articles import ArticleRequest, ArticleResponse, ArticleSection
from .metadata import MetadataRequest, MetadataResponse, MetaTitle, MetaDescription
from .faqs import FAQRequest, FAQResponse, FAQ
from .social import (
    SocialRequest, 
    SocialResponse, 
    TwitterContent, 
    LinkedInContent, 
    InstagramContent, 
    FacebookContent
)

__all__ = [
    "KeywordRequest",
    "KeywordResponse",
    "ArticleRequest",
    "ArticleResponse",
    "ArticleSection",
    "MetadataRequest",
    "MetadataResponse",
    "MetaTitle",
    "MetaDescription",
    "FAQRequest",
    "FAQResponse",
    "FAQ",
    "SocialRequest",
    "SocialResponse",
    "TwitterContent",
    "LinkedInContent",
    "InstagramContent",
    "FacebookContent",
]
