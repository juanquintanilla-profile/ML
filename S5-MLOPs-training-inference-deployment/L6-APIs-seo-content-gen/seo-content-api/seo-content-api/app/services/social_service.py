"""
Servicio para generación de contenido social usando Azure OpenAI.
"""
from openai import AzureOpenAI
from app.config import get_settings
from app.models.social import SocialRequest, SocialResponse


class SocialService:
    """
    Servicio que genera contenido adaptado para diferentes redes sociales.
    """
    
    def __init__(self):
        """Inicializa el cliente de Azure OpenAI"""
        settings = get_settings()
        self.client = AzureOpenAI(
            api_key=settings.azure_openai_api_key,
            api_version=settings.openai_api_version,
            azure_endpoint=settings.azure_openai_endpoint
        )
        self.deployment = settings.deployment_name
    
    def generate_social_content(self, request: SocialRequest) -> SocialResponse:
        """
        Genera contenido optimizado para múltiples plataformas sociales.
        
        Args:
            request: SocialRequest con contenido y plataformas objetivo
            
        Returns:
            SocialResponse con contenido para cada plataforma solicitada
        """
        try:
            prompt = self._build_prompt(request)
            
            completion = self.client.beta.chat.completions.parse(
                model=self.deployment,
                messages=[
                    {
                        "role": "system",
                        "content": "Eres un experto en marketing de contenidos y redes sociales. Adaptas contenido al tono, formato y mejores prácticas de cada plataforma social."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                response_format=SocialResponse,
                temperature=0.85
            )
            
            return completion.choices[0].message.parsed
            
        except Exception as e:
            raise Exception(f"Error generando contenido social: {str(e)}")
    
    def _build_prompt(self, request: SocialRequest) -> str:
        """
        Construye el prompt para generación de contenido social.
        """
        platforms = ", ".join(request.target_platforms)
        
        return f"""
Genera contenido optimizado para redes sociales basándote en:

Título del artículo: {request.article_title}
Contenido: {request.article_content[:1500]}
Plataformas objetivo: {platforms}

Genera contenido SOLO para las plataformas solicitadas. Deja en null las no solicitadas.

Para TWITTER (si está en target_platforms):
- text: Tweet de máximo 280 caracteres, directo e impactante
- hashtags: 2-3 hashtags relevantes (sin # en el array)
- character_count: Cuenta exacta de caracteres

Para LINKEDIN (si está en target_platforms):
- text: Post profesional de 150-300 palabras
- hashtags: 3-5 hashtags profesionales del sector
- call_to_action: CTA profesional (ej: "Comparte tu experiencia en los comentarios")

Para INSTAGRAM (si está en target_platforms):
- caption: Caption atractivo de 100-200 palabras
- hashtags: 15-25 hashtags relevantes (máx 30)
- call_to_action: CTA visual (ej: "Guarda este post", "Etiqueta a alguien")

Para FACEBOOK (si está en target_platforms):
- text: Post conversacional de 100-250 palabras
- hashtags: 2-4 hashtags
- call_to_action: CTA comunitario (ej: "¿Qué opinas?", "Comparte con tu red")

IMPORTANTE:
- Adapta el tono a cada plataforma (Twitter: breve, LinkedIn: profesional, Instagram: visual, Facebook: conversacional)
- Respeta estrictamente el límite de 280 caracteres en Twitter
- Los hashtags deben ser relevantes y específicos
- Incluye emojis apropiados para cada plataforma
- Cada plataforma debe tener un CTA único y relevante
"""
