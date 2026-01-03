"""
Servicio para extracción de FAQs y generación de JSON-LD usando Azure OpenAI.
"""
from openai import AzureOpenAI
from app.config import get_settings
from app.models.faqs import FAQRequest, FAQResponse


class FAQsService:
    """
    Servicio que extrae FAQs de un artículo y genera el esquema JSON-LD.
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
    
    def extract_faqs(self, request: FAQRequest) -> FAQResponse:
        """
        Extrae FAQs del contenido y genera el esquema JSON-LD.
        
        Args:
            request: FAQRequest con contenido del artículo
            
        Returns:
            FAQResponse con FAQs y esquema JSON-LD
        """
        try:
            prompt = self._build_prompt(request)
            
            completion = self.client.beta.chat.completions.parse(
                model=self.deployment,
                messages=[
                    {
                        "role": "system",
                        "content": "Eres un experto en SEO y structured data. Extraes preguntas frecuentes relevantes y generas esquemas JSON-LD válidos para rich snippets."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                response_format=FAQResponse,
                temperature=0.7
            )
            
            return completion.choices[0].message.parsed
            
        except Exception as e:
            raise Exception(f"Error extrayendo FAQs: {str(e)}")
    
    def _build_prompt(self, request: FAQRequest) -> str:
        """
        Construye el prompt para extracción de FAQs.
        """
        return f"""
Analiza el siguiente contenido y extrae preguntas frecuentes (FAQs) relevantes:

Contenido del artículo:
{request.article_content[:2000]}

Número máximo de preguntas: {request.max_questions}

Genera:
1. faqs: Array de {request.max_questions} FAQs donde cada FAQ tiene:
   - question: Pregunta clara y natural que los usuarios harían
   - answer: Respuesta concisa y útil (50-150 palabras)
   
   Las preguntas deben:
   - Ser relevantes al contenido
   - Empezar con qué, cómo, cuándo, dónde, por qué, cuál
   - Ser específicas y naturales
   - Cubrir diferentes aspectos del tema

2. json_ld_schema: Objeto con el esquema JSON-LD FAQPage válido
   Estructura exacta:
   {{
     "@context": "https://schema.org",
     "@type": "FAQPage",
     "mainEntity": [
       {{
         "@type": "Question",
         "name": "pregunta aquí",
         "acceptedAnswer": {{
           "@type": "Answer",
           "text": "respuesta aquí"
         }}
       }}
     ]
   }}

IMPORTANTE:
- Las respuestas deben ser informativas y completas
- El JSON-LD debe ser válido y seguir exactamente el formato de Schema.org
- Incluye todas las FAQs en mainEntity
"""
