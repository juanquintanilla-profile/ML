# Machine Learning

Proyectos de machine learning clásico abarcando aprendizaje supervisado (clasificación y regresión) y no supervisado (clustering). Implementaciones con scikit-learn enfocadas en pipelines completos de preprocesamiento, entrenamiento y evaluación.

## Aprendizaje Supervisado

### Clasificación Binaria: Supervivencia del Titanic

**Archivos**: `s1-lab4-analisis_supervisado2/titanic.ipynb`

Predicción de supervivencia de pasajeros del Titanic utilizando múltiples algoritmos de clasificación.

**Detalles técnicos**:
- **Preprocesamiento**: Imputación de valores nulos (mediana para numéricas, moda para categóricas), one-hot encoding, StandardScaler
- **Pipeline completo con ColumnTransformer**: Diferenciación automática de features numéricas y categóricas
- **Modelos evaluados**: Logistic Regression, KNN (k=5), SVC con probabilidades, Decision Tree, Random Forest (200 estimadores)
- **Métricas**: Accuracy, matriz de confusión, classification report (precision, recall, F1), curvas ROC con AUC
- **Train/Test split**: 80/20 con análisis de balance de clases

### Regresión: Predicción de Precios de Viviendas

**Archivos**: `L4-e1/regression_housing_prices.ipynb`, `s1-lab4-analisis_supervisado/housing.ipynb`

Predicción del precio de viviendas utilizando regresión lineal con features numéricas y categóricas.

**Detalles técnicos**:
- **Análisis exploratorio**: Pairplots para visualización de relaciones entre variables, boxplots de distribución de precios
- **One-Hot Encoding** de variables categóricas con pd.get_dummies
- **Normalización** con StandardScaler para acelerar convergencia
- **Modelo**: LinearRegression de scikit-learn
- **Métricas**: MSE (Mean Squared Error), MAE (Mean Absolute Error), R² (coeficiente de determinación)
- **Visualizaciones**: Scatter plot de valores reales vs predicciones, distribución de residuales

### Clasificación Multiclase: Dataset Diamonds

**Archivos**: `s1-lab4-analisis_supervisado3/diamonds_multiclase_basico.ipynb`

Clasificación de calidad de diamantes en múltiples categorías.

**Detalles técnicos**:
- Preprocesamiento de variables categóricas y numéricas
- Pipelines de transformación con scikit-learn
- Evaluación con métricas multiclase

## Aprendizaje No Supervisado

### Segmentación de Clientes con K-Means

**Archivos**: `s1-lab5-analisis_no_supervisado/lab05_01.ipynb`

Clustering de clientes del dataset Wholesale basado en patrones de gasto en diferentes categorías de productos.

**Detalles técnicos**:
- **Dataset**: 440 clientes con features (Fresh, Milk, Grocery, Frozen, Detergents_Paper, Delicassen)
- **Preprocesamiento**: StandardScaler para normalización de todas las variables
- **Método del codo**: Evaluación de K desde 2 hasta 10, análisis de inercia
- **Coeficiente de Silhouette**: Validación de la calidad del clustering
- **Número óptimo de clusters**: K=6 determinado por análisis del codo
- **Visualización**:
  - Reducción dimensional con PCA (2D y 3D)
  - Boxplots por variable y cluster para interpretación
  - Scatter plots por pares de variables coloreados por cluster

## Herramientas y Librerías

- **scikit-learn**: Modelos de ML, preprocesamiento, métricas, pipelines
- **pandas**: Manipulación de datos
- **numpy**: Operaciones numéricas
- **matplotlib/seaborn**: Visualización de resultados
- **Pipelines**: ColumnTransformer para preprocesamiento automatizado
