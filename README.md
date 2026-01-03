# AI & Machine Learning Portfolio

Repositorio completo de proyectos prácticos cubriendo el espectro completo de IA y Machine Learning: desde limpieza de datos hasta modelos generativos de última generación, MLOps y agentes autónomos.

---

## Índice de Contenidos

1. [Metodologías Ágiles](#metodologías-ágiles)
2. [S0: Data Cleaning](#s0-data-cleaning)
3. [S1: Machine Learning](#s1-machine-learning)
4. [S2: Deep Learning](#s2-deep-learning)
5. [S3: Foundation Models](#s3-foundation-models)
6. [S4: Generative AI Tools & Architectures](#s4-generative-ai-tools--architectures)
7. [S5: MLOps](#s5-mlops)
8. [UNIR Bootcamp](#unir-bootcamp)
9. [Stack Tecnológico](#stack-tecnológico)
10. [Instalación y Requisitos](#instalación-y-requisitos)

---

## Metodologías Ágiles

Material de estudio sobre metodologías ágiles de desarrollo de software

**Contenido**:
- 9 Fastbooks sobre Scrum, Kanban y frameworks ágiles
- Proyecto chatbot (archivo comprimido)
- Teoría y casos prácticos

[Ver más →](./Metodologias-agiles)

---

## S0: Data Cleaning

Laboratorios prácticos de limpieza, transformación y análisis exploratorio de datos con pandas, numpy y visualización avanzada.

**Proyectos destacados**:
- **Lab 1**: Análisis de dataset médico (EPOC, cáncer de pulmón, neumonía)
  - Visualizaciones: histogramas, scatter plots 3D, heatmaps
- **Lab 2**: Análisis de red de ventas multi-tienda
  - Merge de datasets, rotación de inventario, proyecciones con numpy
- **Lab 3**: Análisis de eventos deportivos
  - Segmentación demográfica, métricas de impacto publicitario
- **Lab 4**: Predicción de ventas de películas
  - Detección de outliers, matriz de correlación, regresión lineal múltiple (statsmodels)

**Herramientas**: pandas · numpy · matplotlib · seaborn · statsmodels

[Ver más →](./S0-Data-Cleaning)

---

## S1: Machine Learning

Proyectos de machine learning clásico: aprendizaje supervisado (clasificación y regresión) y no supervisado (clustering) con scikit-learn.

### Aprendizaje Supervisado

**Clasificación Binaria - Titanic**:
- Pipeline completo con ColumnTransformer
- 5 modelos comparados (Logistic Regression, KNN, SVC, Decision Tree, Random Forest)
- Métricas: accuracy, ROC-AUC, confusion matrix

**Regresión - Housing Prices**:
- One-hot encoding y normalización
- Visualización: pairplots, scatter de predicciones vs reales
- Métricas: MSE, MAE, R²

**Clasificación Multiclase - Diamonds**:
- Evaluación con métricas multiclase

### Aprendizaje No Supervisado

**Segmentación de Clientes - Wholesale (K-Means)**:
- 440 clientes, 6 features de gasto
- Método del codo + Silhouette coefficient
- K óptimo: 6 clusters
- Reducción dimensional con PCA (2D y 3D)

**Herramientas**: scikit-learn · pandas · numpy · matplotlib · seaborn

[Ver más →](./S1-Machine-Learning)

---

## S2: Deep Learning

Redes neuronales profundas con PyTorch y TensorFlow/Keras: feedforward, CNNs para visión y RNNs para NLP.

### Redes Feedforward

**Predicción de Diabetes (Pima Indians)**:
- Arquitectura: 8→64→32→1, ReLU + Sigmoid
- PyTorch: BCELoss, Adam optimizer, 200 épocas
- Accuracy: 0.7188, F1-score: 0.5846

### Visión por Computadora

**Clasificación Intel (6 clases: buildings, forest, glacier, mountain, sea, street)**:
- Data augmentation: 6+ técnicas (RandomRotation, ColorJitter, GaussianBlur)
- CNN: 3 conv layers (3→32→64→128) + MaxPool + Dropout(0.3)
- 30 épocas, input 150×150px

**Sign Language MNIST**:
- Reconocimiento de lenguaje de señas con CNNs

**CIFAR-10**:
- Clasificador de 10 clases

### Procesamiento de Lenguaje Natural

**Análisis de Sentimientos - Twitter (74,682 tweets)**:
- Preprocesamiento exhaustivo: eliminación de URLs, menciones, stopwords, expansión de contracciones
- **3 modelos comparados**:
  - FFNN: accuracy 0.747
  - LSTM: accuracy 0.830
  - BERT (RoBERTa): state-of-the-art
- Word embeddings: Word2Vec (entrenado) + GloVe (preentrenado)
- WordClouds por sentimiento

**Otros proyectos**:
- Clasificador de spam
- Clasificador de reseñas de películas

### Optimización

**TMDB con LSTM + GloVe**:
- Análisis de sentimientos con embeddings preentrenados
- Optimización de hiperparámetros

**Herramientas**: PyTorch · TensorFlow/Keras · Transformers (Hugging Face) · torchvision · NLTK · Gensim

[Ver más →](./S2-Deep-Learning)

---

## S3: Foundation Models

Modelos generativos de última generación: GANs y diffusion models para generación de imágenes.

### Lab 1: Generative Adversarial Networks (GANs)
- Entrenamiento adversarial de generador y discriminador
- Generación de imágenes sintéticas desde ruido

### Lab 2: Modelos de Difusión

**Stable Diffusion - Inferencia**:
- Text-to-image generation con diffusers (Hugging Face)
- Control de parámetros: steps, guidance scale, scheduler

**Entrenamiento de Diffusion Models**:
- Proceso de denoising iterativo desde cero

### Lab 3: Generación de Gatos
- Fine-tuning de diffusion models en dataset especializado
- Generación condicional de imágenes de gatos

### Lab 4: Transformers y Embeddings
- Mecanismos de atención (self-attention, multi-head)
- Position encoding
- Embeddings contextuales vs estáticos

### Lab 5: Fine-tuning
- Transfer learning con foundation models
- Learning rate scheduling, gradient accumulation

**Herramientas**: Diffusers · Transformers · PyTorch · Stable Diffusion

[Ver más →](./S3-Foundation-Models)

---

## S4: Generative AI Tools & Architectures

Herramientas, arquitecturas y patrones para aplicaciones de IA generativa: APIs, RAG, agentes autónomos.

### Lab 1: Plataformas de IA Generativa
- **Proveedores**: OpenAI (GPT-4), Anthropic (Claude 3), Google (Gemini)
- Comparación de capacidades, pricing, rate limits
- Patrones de prompting efectivos

### Lab 2: Plataformas Open Source
- **Modelos**: LLaMA (7B-70B), Mistral (Mixtral 8x7B), Falcon
- Despliegue local vs cloud
- Optimización: quantization (int8, int4)
- Frameworks: llama.cpp, vLLM, TGI
- Interfaces: Gradio, Streamlit

### Lab 3: Structured Outputs
- JSON Schema enforcement
- Pydantic models para validación
- Function calling
- Casos de uso: extracción de entidades, datos sintéticos

### Lab 4: Retrieval Augmented Generation (RAG)

**Pipeline completo**:
1. Document loading (PDF, TXT, Markdown)
2. Text splitting y chunking
3. Embedding generation (OpenAI, sentence-transformers)
4. Vector indexing (FAISS, Chroma, Pinecone)
5. Semantic search (top-k similarity)
6. Re-ranking de resultados
7. Context injection en prompt
8. Response generation

**Técnicas**:
- Chunking strategies (tamaño, overlap)
- Métricas de similitud
- Optimización de relevancia

### Lab 5 y 6: Model Context Protocol (MCP)
- Tool definition con JSON Schema
- Context management y estado
- Multi-tool orchestration
- Herramientas: APIs externas, databases, file system, cálculos

### Lab 7: Agentes Autónomos - LinkedIn Poster

**Arquitectura**:
- **Planning**: Descomposición de tareas
- **Tool use**: LinkedIn API, content generation, image creation
- **Memory**: Tracking de posts y engagement
- **Reflection**: Auto-evaluación de calidad
- **Error recovery**: Reintentos y fallbacks

**Componentes**:
- Content generation (LLM-based)
- Scheduling óptimo
- Hashtag recommendation
- Análisis de engagement

**Herramientas**: LangChain · LlamaIndex · Pydantic · FAISS/Chroma · OpenAI/Anthropic APIs

[Ver más →](./S4-Generative-ai-tools-models-architectures)

---

## S5: MLOps

Material teórico sobre prácticas de MLOps para entrenamiento, despliegue y operación de modelos en producción.

### Training Pipeline
- Gestión de experimentos (MLflow, Weights & Biases)
- Versionado de datos y modelos (DVC, Git LFS)
- Reproducibilidad y trazabilidad
- Hyperparameter tuning distribuido

### Model Serving & Inference
- Estrategias: batch, real-time, streaming
- Optimización: quantization, pruning, distillation
- Frameworks: TorchServe, TensorFlow Serving, FastAPI
- Containerización: Docker
- Orquestación: Kubernetes

### Deployment & Monitoring
- CI/CD para modelos
- A/B testing, canary deployments
- Drift detection
- Logging y observabilidad
- Auto-scaling

### Infrastructure
- Plataformas cloud (AWS SageMaker, Azure ML, Google Vertex AI)
- Distributed training con GPUs
- Data pipelines (Apache Airflow, Prefect, Kubeflow)
- Feature stores (Feast, Tecton)

**Herramientas**: MLflow · DVC · Docker/Kubernetes · FastAPI · Prometheus/Grafana · Airflow

[Ver más →](./S5-MLOPs-training-inference-deployment)

---

## UNIR Bootcamp

Proyectos del bootcamp de especialización en IA de UNIR: fundamentos de ML supervisado y no supervisado.

### Sprint 1: ML Supervisado

**Proyectos**:
- **Regresión**: Housing Prices (MSE, MAE, R²)
- **Clasificación Binaria**: Titanic Survival (5 modelos con ROC-AUC)
- **Clasificación Multiclase**: Diamonds quality

**Pipeline completo**:
- SimpleImputer para valores nulos
- ColumnTransformer para preprocesamiento
- StandardScaler para normalización

### Sprint 1: ML No Supervisado

**Clustering con K-Means**:
- Método del codo + Silhouette score
- PCA para reducción dimensional (2D/3D)
- Interpretación con boxplots

**Herramientas**: scikit-learn · pandas · numpy · matplotlib · seaborn

[Ver más →](./UNIR-Bootcamp)

---

## Stack Tecnológico

### Machine Learning & Deep Learning
- **Frameworks**: PyTorch · TensorFlow/Keras · scikit-learn
- **Procesamiento de datos**: pandas · numpy · statsmodels
- **Visualización**: matplotlib · seaborn

### Generative AI
- **APIs**: OpenAI · Anthropic (Claude) · Google (Gemini)
- **Open Source LLMs**: LLaMA · Mistral · Falcon
- **Frameworks**: LangChain · LlamaIndex · Transformers (Hugging Face) · Diffusers
- **Embeddings**: sentence-transformers · Word2Vec · GloVe

### Vector Databases & RAG
- FAISS · Chroma · Pinecone

### Computer Vision
- torchvision · OpenCV · PIL

### NLP
- NLTK · spaCy · Gensim · Transformers (BERT, RoBERTa)

### MLOps & Deployment
- **Experiment Tracking**: MLflow · Weights & Biases
- **Versionado**: DVC · Git LFS
- **Containerización**: Docker · Kubernetes
- **Serving**: TorchServe · TensorFlow Serving · FastAPI
- **Orchestration**: Apache Airflow · Prefect · Kubeflow
- **Monitoring**: Prometheus · Grafana

### Interfaces & Deployment
- Gradio · Streamlit · FastAPI

---

## Instalación y Requisitos

### Requisitos previos
- Python 3.8+
- pip o conda
- Git

### Instalación

```bash
# Clonar el repositorio
git clone <repository-url>
cd repo

# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### Dependencias principales

Las dependencias están organizadas en `requirements.txt` e incluyen:

- **Data Science**: pandas, numpy, scipy, statsmodels
- **Machine Learning**: scikit-learn
- **Deep Learning**: torch, torchvision, tensorflow, keras
- **NLP**: transformers, nltk, spacy, gensim
- **Generative AI**: openai, anthropic, langchain, llama-index, diffusers
- **Visualización**: matplotlib, seaborn, plotly
- **Vector Stores**: faiss-cpu, chromadb
- **MLOps**: mlflow, dvc
- **Deployment**: fastapi, uvicorn, gradio, streamlit

---

## Estructura del Repositorio

```
repo/
├── Metodologias-agiles/           # Scrum, Kanban, metodologías ágiles
├── S0-Data-Cleaning/              # Limpieza y análisis exploratorio
├── S1-Machine-Learning/           # ML supervisado y no supervisado
├── S2-Deep-Learning/              # Redes neuronales (CNNs, RNNs, LSTM)
├── S3-Foundation-Models/          # GANs, Diffusion Models, Transformers
├── S4-Generative-ai-tools-models-architectures/  # RAG, Agentes, MCP
├── S5-MLOPs-training-inference-deployment/       # Teoría MLOps
├── UNIR-Bootcamp/                 # Proyectos bootcamp UNIR
├── .venv/                         # Entorno virtual Python
├── requirements.txt               # Dependencias del proyecto
└── README.md                      # Este archivo
```

---

## Licencia

Este repositorio contiene proyectos educativos y de práctica personal.

---

**Última actualización**: Diciembre 2024
