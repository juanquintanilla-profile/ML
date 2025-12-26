# MLOps: Training, Inference & Deployment

Material teórico y recursos sobre prácticas de MLOps para entrenamiento, despliegue y operación de modelos de machine learning en producción.

## Contenido

### Teoría

Documentación y guías sobre los pilares fundamentales de MLOps:

**Training Pipeline**:
- Gestión de experimentos (MLflow, Weights & Biases)
- Versionado de datos y modelos (DVC, Git LFS)
- Reproducibilidad y trazabilidad
- Automatización del entrenamiento
- Hyperparameter tuning distribuido

**Model Serving & Inference**:
- Estrategias de despliegue (batch, real-time, streaming)
- Optimización de inferencia (quantization, pruning, distillation)
- Model serving frameworks (TorchServe, TensorFlow Serving, FastAPI)
- Containerización con Docker
- Orquestación con Kubernetes

**Deployment & Monitoring**:
- CI/CD para modelos de ML
- A/B testing y canary deployments
- Monitoreo de rendimiento y drift detection
- Logging y observabilidad
- Escalabilidad y auto-scaling

**Infrastructure & Tools**:
- Plataformas cloud (AWS SageMaker, Azure ML, Google Vertex AI)
- Gestión de recursos computacionales (GPUs, distributed training)
- Data pipelines (Apache Airflow, Prefect, Kubeflow)
- Feature stores (Feast, Tecton)

## Recursos Complementarios

- Best practices de MLOps según el nivel de madurez
- Arquitecturas de referencia para diferentes casos de uso
- Checklists para despliegue seguro en producción
- Estrategias de debugging y troubleshooting

## Herramientas Mencionadas

- **MLflow**: Tracking de experimentos, registro de modelos
- **DVC**: Versionado de datos y pipelines
- **Docker/Kubernetes**: Containerización y orquestación
- **FastAPI**: Servicio de modelos vía API REST
- **Prometheus/Grafana**: Monitoring y visualización
- **Apache Airflow**: Orquestación de workflows
