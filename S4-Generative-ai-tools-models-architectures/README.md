# Generative AI: Tools, Models & Architectures

Proyectos prácticos sobre herramientas, arquitecturas y patrones de diseño para aplicaciones de IA generativa, desde integración de APIs hasta implementación de sistemas RAG y agentes autónomos.

## Lab 1: Plataformas de IA Generativa

**Archivos**: `1-ai-generative-platforms/lab_proveedores_IA.ipynb`

Exploración y comparación de proveedores de modelos de IA generativa comerciales.

**Proveedores evaluados**:
- **OpenAI**: GPT-4, GPT-3.5-turbo (API key, pricing, rate limits)
- **Anthropic**: Claude 3 (Opus, Sonnet, Haiku)
- **Google**: Gemini, PaLM 2

**Aspectos técnicos**:
- Integración de APIs mediante SDKs oficiales
- Comparación de capacidades: ventana de contexto, multimodalidad, latencia
- Patrones de prompting efectivos por proveedor
- Gestión de tokens y optimización de costos

## Lab 2: Plataformas Open Source para Chatbots

**Archivos**: `2-opensource-platforms-chatbot/lab_opensource_IA.ipynb`

Implementación de chatbots con modelos de lenguaje open source.

**Modelos utilizados**:
- **LLaMA** (Meta): Modelos de 7B a 70B parámetros
- **Mistral**: Mixtral 8x7B, optimización de inferencia
- **Falcon**: Modelos optimizados para uso comercial

**Infraestructura**:
- Despliegue local vs cloud (costos, latencia, privacidad)
- Optimización de memoria: quantization (int8, int4)
- Frameworks: llama.cpp, vLLM, Text Generation Inference
- Interfaces: Gradio, Streamlit

## Lab 3: Structured Outputs

**Archivos**: `3-structured-outputs/lab_salida_estructurada_IA.ipynb`

Generación de salidas estructuradas y validadas desde LLMs.

**Técnicas implementadas**:
- **JSON Schema enforcement**: Definición de esquemas estrictos
- **Pydantic models**: Validación de tipos y constraints
- **Function calling**: Uso de herramientas definidas
- **Output parsers**: Extracción robusta de información estructurada
- **Casos de uso**: Extracción de entidades, generación de datos sintéticos, form filling

## Lab 4: Retrieval Augmented Generation (RAG)

**Archivos**: `4-retrieval-augmented-generation/FicherosPasoaPasoLab04/lab04_rag.ipynb`

Implementación completa de sistemas RAG para Q&A sobre documentos.

**Arquitectura RAG**:
- **Embeddings**: Transformación de documentos a vectores (OpenAI embeddings, sentence-transformers)
- **Vector Store**: Almacenamiento y búsqueda de similitud (FAISS, Chroma, Pinecone)
- **Chunking strategies**: División óptima de documentos (tamaño, overlap)
- **Retrieval**: Top-k similarity search con métricas de distancia
- **Re-ranking**: Mejora de relevancia de resultados recuperados
- **Generation**: Augmented prompts con contexto recuperado

**Pipeline completo**:
1. Document loading (PDF, TXT, Markdown)
2. Text splitting y chunking
3. Embedding generation
4. Vector indexing
5. Query embedding
6. Semantic search
7. Context injection en prompt
8. Response generation

## Lab 5 y 6: Model Context Protocol (MCP)

**Archivos**: `5-model-context-protocol/RecursosLab05Pasoapaso/lab05_tools_mcp.ipynb`, `6-model-context-protocol-final/`

Implementación del protocolo MCP para integración de herramientas con LLMs.

**Conceptos MCP**:
- **Tool definition**: Especificación de funciones con JSON Schema
- **Context management**: Mantenimiento de estado entre llamadas
- **Error handling**: Validación y recuperación de errores
- **Multi-tool orchestration**: Combinación de múltiples herramientas

**Herramientas implementadas**:
- APIs externas (weather, stock prices, web search)
- Database queries
- File system operations
- Computation tools (calculator, unit converter)

## Lab 7: Agentes Autónomos - LinkedIn Poster

**Archivos**: `7-agents-linkedIn-poster/`

Desarrollo de agente autónomo para automatización de posts en LinkedIn.

**Arquitectura de Agente**:
- **Planning**: Descomposición de tarea en subtareas
- **Tool use**: LinkedIn API, content generation, image creation
- **Memory**: Tracking de posts previos, engagement metrics
- **Reflection**: Auto-evaluación de calidad de contenido
- **Error recovery**: Reintentos y estrategias fallback

**Componentes**:
- Content generation (LLM-based)
- Scheduling y timing óptimo
- Hashtag recommendation
- Image/media attachment
- Engagement analysis

## Herramientas y Frameworks

- **LangChain**: Orquestación de pipelines con LLMs
- **LlamaIndex**: Framework RAG y data indexing
- **Pydantic**: Validación de datos estructurados
- **FAISS/Chroma**: Vector databases
- **APIs**: OpenAI, Anthropic, LinkedIn, weather services
- **Gradio/Streamlit**: Interfaces de usuario
