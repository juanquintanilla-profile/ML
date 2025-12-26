# UNIR Bootcamp - Especialidad IA

Proyectos del bootcamp de especialización en Inteligencia Artificial de UNIR, cubriendo fundamentos de machine learning supervisado y no supervisado.

## Sprint 1: Machine Learning Supervisado

### Lab 3: Supervised Learning Foundations

**Archivos**: `Especialidad/Sprint1_lab04/sprint1_lab3-supervised-learning.ipynb`

Introducción a algoritmos de aprendizaje supervisado y conceptos fundamentales.

**Temas cubiertos**:
- Diferencia entre clasificación y regresión
- Train/test split y validación cruzada
- Overfitting vs underfitting
- Evaluación de modelos con métricas apropiadas

### Lab 4: Análisis Supervisado - Proyectos Prácticos

#### Regresión: Housing Prices

**Archivos**: `Especialidad/Sprint1_lab04/s1-lab4-analisis_supervisado/housing.ipynb`

Predicción de precios de viviendas usando regresión lineal.

**Implementación**:
- Análisis exploratorio con pairplots
- Codificación de variables categóricas (one-hot encoding)
- Normalización con StandardScaler
- LinearRegression de scikit-learn
- Métricas: MSE, MAE, R²

#### Clasificación Binaria: Titanic Survival

**Archivos**: `Especialidad/Sprint1_lab04/s1-lab4-analisis_supervisado2/titanic.ipynb`

Predicción de supervivencia en el Titanic comparando múltiples algoritmos.

**Modelos comparados**:
- Logistic Regression
- K-Nearest Neighbors
- Support Vector Classifier
- Decision Tree
- Random Forest

**Pipeline completo**:
- Manejo de valores nulos (SimpleImputer)
- ColumnTransformer para preprocesamiento diferenciado
- Evaluación con ROC-AUC, confusion matrix, classification report

#### Clasificación Multiclase: Diamonds

**Archivos**: `Especialidad/Sprint1_lab04/s1-lab4analisis_supervisado3/diamonds_multiclase_basico.ipynb`

Clasificación de calidad de diamantes en múltiples categorías.

## Sprint 1: Machine Learning No Supervisado

### Lab 5: Unsupervised Learning - Clustering

**Archivos**: `Especialidad/Sprint1_lab05/1736243792361-unsupervised-learning.ipynb`

Segmentación de clientes utilizando K-Means clustering.

**Técnicas implementadas**:
- Normalización de datos con StandardScaler
- Determinación del K óptimo mediante método del codo
- Coeficiente de Silhouette para validación
- Reducción dimensional con PCA (2D y 3D)
- Visualización de clusters por pares de variables
- Interpretación de segmentos con boxplots

**Métricas de evaluación**:
- Inercia (within-cluster sum of squares)
- Silhouette score
- Análisis visual de separación de clusters

## Estructura del Proyecto

```
UNIR-Bootcamp/
├── Especialidad/
│   ├── Sprint1_lab04/         # Aprendizaje supervisado
│   │   ├── s1-lab4-analisis_supervisado/      # Regresión
│   │   ├── s1-lab4-analisis_supervisado2/     # Clasificación binaria
│   │   └── s1-lab4analisis_supervisado3/      # Clasificación multiclase
│   └── Sprint1_lab05/         # Aprendizaje no supervisado
└── .venv/                      # Entorno virtual Python
```

## Herramientas y Tecnologías

- **scikit-learn**: Algoritmos de ML, preprocesamiento, métricas
- **pandas**: Análisis y manipulación de datos
- **numpy**: Operaciones numéricas
- **matplotlib/seaborn**: Visualización de datos y resultados
- **StandardScaler**: Normalización de features
- **Pipelines**: Automatización del flujo de preprocesamiento
