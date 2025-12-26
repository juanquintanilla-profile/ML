# Data Cleaning

Conjunto de laboratorios prácticos centrados en técnicas de limpieza, transformación y análisis exploratorio de datos utilizando pandas, numpy y visualización con matplotlib/seaborn.

## Lab 1: Análisis de Dataset Médico

**Archivos**: `analisis-dataset-tfg.ipynb`, `calculadora_notas.ipynb`

Análisis exploratorio de un dataset médico sobre enfermedades respiratorias (EPOC, cáncer de pulmón, sarcoidosis, neumonía). Se trabaja con datos de pacientes incluyendo edad, sexo, tipo de enfermedad y número de muestras de tos.

**Técnicas aplicadas**:
- Manipulación de DataFrames con pandas
- Visualizaciones: histogramas de distribución, gráficos de barras agrupados, scatter plots bidimensionales y tridimensionales
- Heatmaps con seaborn para visualizar distribución por sexo y rango de edad
- Agregaciones y análisis de frecuencias por enfermedad

## Lab 2: Análisis de Red de Ventas

**Archivos**: `analisis_red_ventas.ipynb`

Análisis integral de una red de ventas multi-tienda trabajando con tres datasets: ventas, inventarios y satisfacción del cliente.

**Técnicas aplicadas**:
- Combinación de DataFrames con pd.merge
- Cálculo de indicadores de negocio: ventas totales por tienda, rotación de inventario
- Identificación de tiendas con niveles críticos de stock
- Operaciones con numpy: cálculo de mediana, desviación estándar
- Generación de proyecciones de ventas con números aleatorios controlados (semilla para reproducibilidad)

## Lab 3: Análisis de Eventos Deportivos

**Archivos**: `analisis_eventos.ipynb`

Análisis de datos de eventos deportivos integrando información de eventos, aficionados y promociones publicitarias mediante merges de múltiples datasets.

**Técnicas aplicadas**:
- Merges con validación (many-to-many) para garantizar integridad
- Análisis demográfico: segmentación por rangos de edad con pd.cut
- Cálculo de métricas de impacto: ratio asistencia/presupuesto promocional
- Identificación de medios publicitarios más efectivos
- Exportación de reportes agregados a CSV

## Lab 4: Análisis de Ventas de Películas

**Archivos**: `analisis_ventas_peliculas.ipynb`

Análisis predictivo de ventas de boletos de películas incorporando variables de calificación, eventos promocionales y participación en promociones.

**Técnicas aplicadas**:
- Detección de valores nulos y tratamiento de datos faltantes
- Identificación de outliers mediante boxplots
- Matriz de correlación de Pearson para análisis de dependencias entre variables
- Regresión lineal múltiple con statsmodels.OLS
- Visualización de residuales y comparación de valores reales vs predicciones

## Herramientas y Librerías

- **pandas**: Manipulación y análisis de datos estructurados
- **numpy**: Operaciones numéricas y estadísticas
- **matplotlib**: Visualizaciones básicas
- **seaborn**: Visualizaciones estadísticas avanzadas
- **statsmodels**: Modelos estadísticos y regresión lineal
