# Foundation Models y Modelos Generativos

Proyectos enfocados en modelos generativos de última generación, incluyendo GANs y modelos de difusión para generación de imágenes.

## Lab 1: Generative Adversarial Networks (GANs)

**Archivos**: `L1/Foundation_Models_y_Modelos_Generativos_Laboratorio_de_GANs.ipynb`

Implementación y entrenamiento de GANs para generación de imágenes sintéticas.

**Detalles técnicos**:
- **Arquitectura GAN**: Red generadora y discriminadora en competencia
- **Proceso de entrenamiento adversarial**: Optimización alternada de generador y discriminador
- **Generación de imágenes sintéticas** a partir de ruido aleatorio
- **Evaluación de calidad**: Análisis visual de imágenes generadas a lo largo del entrenamiento

## Lab 2: Modelos de Difusión

### Stable Diffusion para Generación de Imágenes

**Archivos**: `L2/Foundation_Models_y_Modelos_Generativos-StableDiffusion_Inference.ipynb`, `L2/diffusion_models_image_gen.ipynb`

Inferencia con Stable Diffusion para generación de imágenes a partir de descripciones textuales.

**Detalles técnicos**:
- **Modelo**: Stable Diffusion (diffusion-based text-to-image)
- **Pipeline de inferencia**: Uso de diffusers de Hugging Face
- **Text-to-image generation**: Generación de imágenes a partir de prompts textuales
- **Control de parámetros**: Steps de difusión, guidance scale, scheduler
- **Aplicaciones**: Generación creativa de imágenes, exploración del espacio latente

### Entrenamiento de Diffusion Models

**Archivos**: `L2/lab2-e3/diffusion_models_image_gen.ipynb`

Entrenamiento de modelos de difusión desde cero para comprender el proceso de denoising iterativo.

## Lab 3: Generación de Imágenes de Gatos

**Archivos**: `L3/dataset-fotos-gatos/diffusers_cat_images_generation.ipynb`

Proyecto especializado en generación de imágenes de gatos utilizando diffusion models.

**Detalles técnicos**:
- **Dataset**: Colección de imágenes de gatos para fine-tuning
- **Fine-tuning de diffusion models**: Adaptación del modelo a un dominio específico
- **Generación condicional**: Control de características específicas de las imágenes generadas
- **Evaluación**: Calidad visual y diversidad de las imágenes sintéticas generadas

## Lab 4: Transformers y Embeddings

**Archivos**: Laboratorios sobre arquitecturas Transformer y representación de embeddings.

**Conceptos cubiertos**:
- Mecanismos de atención (self-attention, multi-head attention)
- Arquitectura Transformer completa
- Embeddings contextuales vs estáticos
- Position encoding

## Lab 5: Fine-tuning de Foundation Models

**Archivos**: Proyectos de adaptación de modelos preentrenados.

**Técnicas aplicadas**:
- Transfer learning con modelos foundation
- Fine-tuning en tareas específicas de dominio
- Estrategias de optimización (learning rate scheduling, gradient accumulation)

## Herramientas y Frameworks

- **Diffusers (Hugging Face)**: Pipelines de modelos de difusión
- **Transformers (Hugging Face)**: Acceso a modelos preentrenados
- **PyTorch**: Framework de deep learning
- **Stable Diffusion**: Modelo estado del arte para text-to-image
- **GANs**: Implementación de arquitecturas adversariales
