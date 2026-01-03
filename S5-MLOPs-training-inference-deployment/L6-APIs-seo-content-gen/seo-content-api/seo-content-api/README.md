# SEO Content API

API REST para generación de contenido SEO optimizado utilizando Azure OpenAI (GPT-4o).

## 🚀 Características

- **Generación de Keywords**: Keywords semilla, long-tail, preguntas y clasificación por intención
- **Artículos SEO**: Contenido estructurado con H1/H2/H3, densidad de keywords y CTAs
- **Metadatos**: Meta titles y descriptions optimizados para CTR
- **FAQs**: Extracción de preguntas frecuentes con esquemas JSON-LD
- **Contenido Social**: Adaptación automática para Twitter, LinkedIn, Instagram y Facebook

## 📋 Requisitos

- Python ≥ 3.12
- Azure OpenAI API Key y Endpoint
- Modelos disponibles: gpt-4o, gpt-4o-mini

## 🛠️ Instalación

1. **Clonar el repositorio**
```bash
git clone <tu-repositorio>
cd seo-content-api
```

2. **Crear entorno virtual**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno**

Editar archivo `.env` en la raíz del proyecto con tus credenciales de Azure:
```env
AZURE_OPENAI_API_KEY=tu-api-key
AZURE_OPENAI_ENDPOINT=https://tu-recurso.openai.azure.com/
OPENAI_API_VERSION=2024-02-15-preview
DEPLOYMENT_NAME=gpt-4o
```

## 🚀 Ejecución

```bash
uvicorn app.main:app --reload
```

La API estará disponible en: `http://localhost:8000`

## 📚 Documentación

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔗 Endpoints

### 1. POST /api/keywords/generate
Genera keywords SEO clasificadas.

**Request:**
```json
{
  "topic": "marketing digital",
  "industry": "tecnología",
  "language": "es"
}
```

### 2. POST /api/articles/generate
Crea artículos SEO completos.

**Request:**
```json
{
  "main_keyword": "marketing digital",
  "secondary_keywords": ["SEO", "redes sociales"],
  "word_count": 1500,
  "tone": "profesional"
}
```

### 3. POST /api/metadata/generate
Genera metadatos optimizados.

**Request:**
```json
{
  "article_title": "Guía de Marketing Digital",
  "main_keyword": "marketing digital",
  "article_excerpt": "Descubre las mejores estrategias..."
}
```

### 4. POST /api/faqs/extract
Extrae FAQs con JSON-LD.

**Request:**
```json
{
  "article_content": "El marketing digital es...",
  "max_questions": 5
}
```

### 5. POST /api/social/summaries
Genera contenido para redes sociales.

**Request:**
```json
{
  "article_title": "Guía de Marketing",
  "article_content": "El marketing digital...",
  "target_platforms": ["twitter", "linkedin"]
}
```

## 🏗️ Estructura del Proyecto

```
seo-content-api/
├── app/
│   ├── main.py              # Aplicación FastAPI
│   ├── config.py            # Configuración
│   ├── models/              # Modelos Pydantic
│   │   ├── keywords.py
│   │   ├── articles.py
│   │   ├── metadata.py
│   │   ├── faqs.py
│   │   └── social.py
│   ├── services/            # Lógica de negocio + OpenAI
│   │   ├── keywords_service.py
│   │   ├── articles_service.py
│   │   ├── metadata_service.py
│   │   ├── faqs_service.py
│   │   └── social_service.py
│   └── routers/             # Endpoints
│       ├── keywords.py
│       ├── articles.py
│       ├── metadata.py
│       ├── faqs.py
│       └── social.py
├── .env                     # Variables de entorno
├── requirements.txt         # Dependencias
└── README.md
```

## 💡 Uso de Azure OpenAI

Este proyecto utiliza Azure OpenAI con el SDK oficial:

```python
from openai import AzureOpenAI

client = AzureOpenAI(
    api_key=settings.azure_openai_api_key,
    api_version=settings.openai_api_version,
    azure_endpoint=settings.azure_openai_endpoint
)
```

### Structured Outputs

Utilizamos `beta.chat.completions.parse` para obtener respuestas estructuradas:

```python
completion = client.beta.chat.completions.parse(
    model="gpt-4o",
    messages=[...],
    response_format=KeywordResponse,  # Modelo Pydantic
    temperature=0.7
)

result = completion.choices[0].message.parsed  # Objeto Pydantic
```

## ⚠️ Limitaciones de Azure for Students

- Crédito: $100
- Modelos disponibles: **gpt-4o** y **gpt-4o-mini**
- NO disponibles: gpt-4.1, gpt-5
- Ver [quotas y límites](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/quotas-limits)

## 🧪 Testing

Puedes probar los endpoints usando:

1. **Swagger UI**: http://localhost:8000/docs
2. **cURL**:
```bash
curl -X POST "http://localhost:8000/api/keywords/generate" \
  -H "Content-Type: application/json" \
  -d '{"topic":"IA","industry":"tecnología","language":"es"}'
```

3. **Python**:
```python
import requests

response = requests.post(
    "http://localhost:8000/api/keywords/generate",
    json={
        "topic": "inteligencia artificial",
        "industry": "tecnología",
        "language": "es"
    }
)
print(response.json())
```

## 📝 Licencia

MIT

## 👤 Autor

Juan
