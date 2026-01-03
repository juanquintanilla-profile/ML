"""
Servicio para generación de artículos SEO usando Azure OpenAI.
"""
from openai import AzureOpenAI
from app.config import get_settings
from app.models.articles import ArticleRequest, ArticleResponse


class ArticlesService:
    """
    Servicio que genera artículos completos optimizados para SEO.
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
    
    def generate_article(self, request: ArticleRequest) -> ArticleResponse:
        """
        Genera un artículo completo con estructura SEO.
        
        Args:
            request: ArticleRequest con keywords y configuración
            
        Returns:
            ArticleResponse con artículo estructurado
        """
        try:
            prompt = self._build_prompt(request)
            
            completion = self.client.beta.chat.completions.parse(
                model=self.deployment,
                messages=[
                    {
                        "role": "system",
                        "content": "Eres un redactor experto en contenido SEO. Creas artículos bien estructurados con jerarquía de encabezados H1/H2/H3, densidad natural de keywords y CTAs efectivos."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                response_format=ArticleResponse,
                temperature=0.8
            )
            
            return completion.choices[0].message.parsed
            
        except Exception as e:
            raise Exception(f"Error generando artículo: {str(e)}")
    
    def _build_prompt(self, request: ArticleRequest) -> str:
        """
        Construye el prompt para generación de artículos.
        """
        secondary = ", ".join(request.secondary_keywords) if request.secondary_keywords else "ninguna"
        
        return f"""
Genera un artículo SEO completo con la siguiente configuración:

Keyword principal: {request.main_keyword}
Keywords secundarias: {secondary}
Número de palabras objetivo: {request.word_count}
Tono: {request.tone}

Estructura requerida:
1. title: Un título H1 atractivo que incluya la keyword principal
2. sections: Array de secciones con:
   - heading: Título de la sección
   - heading_level: 2 para H2, 3 para H3
   - content: Contenido de la sección (mínimo 50 palabras)
   
   Crea una estructura jerárquica lógica:
   - Introducción (H2)
   - 3-5 secciones principales (H2)
   - Cada H2 puede tener 1-3 subsecciones H3
   - Conclusión (H2)

3. keyword_density: Objeto con el % de densidad de cada keyword
   Ejemplo: {{"marketing digital": 2.5, "SEO": 1.8}}

4. call_to_actions: Array de 2-3 CTAs naturales incluidos en el contenido
   Ejemplo: ["Solicita una consulta gratuita", "Descarga nuestra guía"]

IMPORTANTE:
- Integra las keywords de forma natural, sin keyword stuffing
- La densidad ideal es 1-3% para la keyword principal
- Usa sinónimos y variaciones
- Los CTAs deben ser relevantes y coherentes con el contenido
"""
