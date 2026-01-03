"""
Servicio para generación de keywords usando Azure OpenAI.
"""
from openai import AzureOpenAI
from app.config import get_settings
from app.models.keywords import KeywordRequest, KeywordResponse


class KeywordsService:
    """
    Servicio que genera keywords semilla, long-tail y preguntas relevantes.
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
    
    def generate_keywords(self, request: KeywordRequest) -> KeywordResponse:
        """
        Genera keywords utilizando GPT-4o.
        
        Args:
            request: KeywordRequest con topic, industry y language
            
        Returns:
            KeywordResponse con keywords generadas y clasificadas
        """
        try:
            # Construir el prompt estructurado
            prompt = self._build_prompt(request)
            
            # Llamada a Azure OpenAI con structured outputs
            completion = self.client.beta.chat.completions.parse(
                model=self.deployment,
                messages=[
                    {
                        "role": "system",
                        "content": "Eres un experto en SEO y generación de keywords. Respondes en formato JSON estructurado."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                response_format=KeywordResponse,
                temperature=0.7
            )
            
            # Parsear la respuesta estructurada
            return completion.choices[0].message.parsed
            
        except Exception as e:
            raise Exception(f"Error generando keywords: {str(e)}")
    
    def _build_prompt(self, request: KeywordRequest) -> str:
        """
        Construye el prompt para la generación de keywords.
        """
        return f"""
Genera una lista completa de keywords para SEO basándote en la siguiente información:

Tema principal: {request.topic}
Industria: {request.industry}
Idioma: {request.language}

Debes generar:
1. seed_keywords: 5-7 keywords principales/semilla relacionadas directamente con el tema
2. long_tail_keywords: 8-10 keywords de cola larga (frases de 3-5 palabras)
3. questions: 5-7 preguntas que los usuarios podrían buscar
4. intent_classification: Clasifica las keywords en dos categorías:
   - informational: keywords con intención informativa (aprender, entender)
   - transactional: keywords con intención transaccional (comprar, contratar, descargar)

Las keywords deben ser relevantes, específicas y optimizadas para motores de búsqueda.
"""
