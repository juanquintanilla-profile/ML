# Deep Learning

Proyectos de redes neuronales profundas con PyTorch y TensorFlow/Keras, cubriendo arquitecturas feedforward, CNNs para visión por computadora y RNNs para procesamiento de lenguaje natural.

## Redes Neuronales Feedforward

### Predicción de Diabetes (Pima Indians Dataset)

**Archivos**: `L2-e2-feed-forward-network-diabetesprediction/l2-e2-diabetespred.ipynb`

Clasificación binaria para predecir diabetes utilizando redes feedforward con PyTorch.

**Detalles técnicos**:
- **Arquitectura**: 3 capas (8→64→32→1), activación ReLU en capas ocultas, Sigmoid en salida
- **Preprocesamiento**: Reemplazo de valores 0 no realistas por medias, StandardScaler
- **Loss function**: Binary Cross-Entropy (BCELoss)
- **Optimizer**: Adam (lr=0.001)
- **Training**: 200 épocas, conversión de datos a tensores float32
- **Métricas**: Accuracy (0.7188), F1-score (0.5846), classification report completo
- **Dataset**: 768 registros, 8 features (Pregnancies, Glucose, BloodPressure, BMI, etc.)

### Predicción de Calificaciones Estudiantiles

**Archivos**: `L2-e1-feed-forward-scoresprediction/l2-e1-student-score.ipynb`

Red neuronal para predecir calificaciones de estudiantes basándose en horas de estudio y otras variables.

## Visión por Computadora (CNNs)

### Clasificación de Imágenes Intel (6 clases)

**Archivos**: `L4-e1-CNN-intel-classifcation-dataset/intel_cnn_pytorch.ipynb`

Clasificación de imágenes en 6 categorías (buildings, forest, glacier, mountain, sea, street) con CNNs en PyTorch.

**Detalles técnicos**:
- **Data Augmentation** (≥5 técnicas): RandomResizedCrop, RandomHorizontalFlip, RandomRotation (15°), ColorJitter, RandomGrayscale, GaussianBlur
- **Arquitectura CNN**:
  - 3 capas convolucionales (3→32→64→128)
  - MaxPool2d después de cada capa convolucional
  - AdaptiveAvgPool2d (4x4) para independencia de tamaño de entrada
  - Capas fully connected (128×16→256→6) con Dropout (0.3)
- **Training**: 30 épocas con imágenes aumentadas, evaluación en imágenes sin aumento
- **Normalización**: Mean=[0.485, 0.456, 0.406], Std=[0.229, 0.224, 0.225] (ImageNet stats)
- **Input size**: 150×150 píxeles
- **Visualización**: Comparación original vs aumentada, curvas de loss y accuracy

### Clasificación de Sign Language MNIST

**Archivos**: `L4-e2-CNN-sign-lenguage-MNIST/SignLanguageMNIST_Augment_CNN.ipynb`

Reconocimiento de lenguaje de señas utilizando CNNs con data augmentation.

**Detalles técnicos**:
- Dataset de imágenes de gestos de lenguaje de señas
- Arquitectura CNN optimizada para clasificación multiclase
- Data augmentation para mejorar generalización

### Clasificación CIFAR-10

**Archivos**: `L4-computer-vision/cifar10_classifier.ipynb`

Clasificador de imágenes del dataset CIFAR-10 (10 clases).

## Procesamiento de Lenguaje Natural

### Análisis de Sentimientos en Twitter

**Archivos**: `L5-NLP/analisis-de-sentimientos.ipynb`

Análisis completo de sentimientos en tweets comparando múltiples arquitecturas: FFNN, LSTM y BERT.

**Detalles técnicos**:
- **Dataset**: 74,682 tweets de entrenamiento, 1,000 de test
- **Preprocesamiento exhaustivo**:
  - Eliminación de URLs, menciones (@), hashtags (#), caracteres especiales
  - Expansión de contracciones (won't → would not, can't → can not)
  - Eliminación de stopwords con NLTK
  - Lowercase y normalización de espacios
- **Word Embeddings**:
  - Word2Vec entrenado desde cero (vector_size=100, window=5)
  - GloVe preentrenado (glove-twitter-25)
  - Análisis de similitud semántica entre palabras
- **Modelo 1 - FFNN**: Embedding layer + Flatten + Dense, accuracy 0.747
- **Modelo 2 - LSTM**: Embedding layer + LSTM(128) + Dense, accuracy 0.830
- **Modelo 3 - BERT**: RoBERTa preentrenado (cardiffnlp/twitter-roberta-base-sentiment-latest)
- **Visualización**: WordClouds por clase de sentimiento, matrices de confusión
- **Métricas**: Accuracy, precision, recall, F1-score

### Clasificador de Spam

**Archivos**: `L5-spam-classifier/nlp-spam-class.ipynb`

Detección de mensajes spam utilizando redes neuronales.

### Clasificador de Películas

**Archivos**: `L5-Film-Classifier/nlp-film-classifier.ipynb`

Clasificación de reseñas de películas por sentimiento.

## Optimización y Arquitecturas Avanzadas

### Optimización de Hiperparámetros

**Archivos**: `L6-optimizacion/optimizacion-hiperparametros.ipynb`

Exploración sistemática de hiperparámetros para mejorar rendimiento de modelos.

### TMDB con LSTM y GloVe

**Archivos**: `L6-e1-optimizacion-NLP/tmdb_lstm_glove.ipynb`

Análisis de sentimientos en reseñas de TMDB utilizando LSTM con embeddings GloVe preentrenados.

## Herramientas y Frameworks

- **PyTorch**: Definición de modelos, nn.Module, optimizers, loss functions
- **TensorFlow/Keras**: Sequential models, Embedding layers, LSTM
- **Transformers (Hugging Face)**: BERT, RoBERTa para NLP
- **torchvision**: Transforms, data augmentation, ImageFolder
- **NLTK/spaCy**: Preprocesamiento de texto, stopwords
- **Gensim**: Word2Vec, GloVe embeddings
