"""
Servicio para generación de metadatos SEO usando Azure OpenAI.
"""
from openai import AzureOpenAI
from app.config import get_settings
from app.models.metadata import MetadataRequest, MetadataResponse


class MetadataService:
    """
    Servicio que genera meta titles y meta descriptions optimizados.
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
    
    def generate_metadata(self, request: MetadataRequest) -> MetadataResponse:
        """
        Genera múltiples variantes de metadatos SEO.
        
        Args:
            request: MetadataRequest con información del artículo
            
        Returns:
            MetadataResponse con variantes de meta titles y descriptions
        """
        try:
            prompt = self._build_prompt(request)
            
            completion = self.client.beta.chat.completions.parse(
                model=self.deployment,
                messages=[
                    {
                        "role": "system",
                        "content": "Eres un experto en SEO especializado en metadatos. Generas meta titles y descriptions persuasivos que mejoran el CTR, respetando estrictamente los límites de caracteres."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                response_format=MetadataResponse,
                temperature=0.9  # Mayor creatividad para variantes
            )
            
            return completion.choices[0].message.parsed
            
        except Exception as e:
            raise Exception(f"Error generando metadata: {str(e)}")
    
    def _build_prompt(self, request: MetadataRequest) -> str:
        """
        Construye el prompt para generación de metadatos.
        """
        return f"""
Genera metadatos SEO optimizados para el siguiente artículo:

Título del artículo: {request.article_title}
Keyword principal: {request.main_keyword}
Extracto: {request.article_excerpt}

Genera:
1. meta_titles: Array de 3-5 variantes de meta title
   - Cada variante debe incluir:
     * text: El meta title (MÁXIMO 60 caracteres)
     * character_count: Número exacto de caracteres
   - Debe incluir la keyword principal
   - Usa lenguaje persuasivo y específico
   - Varía el estilo: algunos con año, otros con beneficios, otros con números

2. meta_descriptions: Array de 3-5 variantes de meta description
   - Cada variante debe incluir:
     * text: La meta description (MÁXIMO 160 caracteres)
     * character_count: Número exacto de caracteres
   - Debe incluir la keyword principal
   - Incluye un call-to-action
   - Comunica el valor o beneficio principal
   - Varía el enfoque y el tono

CRÍTICO: 
- Meta titles: MAX 60 caracteres
- Meta descriptions: MAX 160 caracteres
- Cuenta los caracteres con precisión
- Incluye siempre la keyword principal de forma natural
"""
