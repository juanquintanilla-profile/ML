# 🧠 Chatbot RAG con LangChain y OpenAI  
### Proyecto – Desarrollo de Soluciones IA · Zona de Entrenamiento

Este proyecto consiste en desarrollar un **chatbot inteligente** que utiliza la técnica **RAG (Retrieval-Augmented Generation)** para responder preguntas basándose únicamente en documentos internos de una empresa ficticia.  
El sistema utiliza **LangChain**, **OpenAI**, un **vector store en memoria**, y una **interfaz de línea de comandos (CLI)**.

---

## 📁 Estructura del proyecto
├── main.py # Punto de entrada de la aplicación (CLI)
├── documents/
│ ├── documento1.md # Información general de la empresa
│ └── documento2.md # Políticas internas y procedimientos
├── core/
│ ├── init.py
│ ├── rag_system.py # Implementación del sistema RAG
│ └── chatbot.py # Lógica de conversación del chatbot
├── requirements.txt
├── .env # Variables de entorno (API Key)
└── README.md


---

## 🎯 Objetivo del proyecto

Construir un chatbot capaz de:

- Procesar documentos markdown.
- Indexarlos en un vector store usando **OpenAIEmbeddings**.
- Recuperar fragmentos relevantes ante una consulta.
- Generar respuestas coherentes y contextualizadas utilizando un modelo de OpenAI.
- Mantener contexto conversacional.
- Proporcionar interacción completa mediante CLI.

Este proyecto forma parte del apartado **Entrenamiento**, suponiendo un **40% de la nota final**. La corrección es automática mediante IA.

---

## 📝 Requisitos del reto

### 🔹 1. Sistema de embeddings (25%)
Debes:

- Usar `OpenAIEmbeddings` con el modelo **text-embedding-3-small**.
- Procesar documentos markdown.
- Generar y almacenar embeddings en `InMemoryVectorStore`.

### 🔹 2. Sistema de retrieval (25%)
Debe ser capaz de:

- Recuperar fragmentos relevantes usando similitud.
- Devolver información que responda a la consulta del usuario.

### 🔹 3. Chatbot conversacional (25%)
El chatbot debe:

- Mantener el contexto durante la conversación.
- Utilizar modelos de OpenAI (**gpt-4o**, **gpt-4.1**, **gpt-5**).
- Generar respuestas *solo* basadas en información recuperada.
- Integrarse correctamente con el sistema RAG.

### 🔹 4. Interfaz CLI (25%)
Debe permitir:

- Iniciar conversación.
- Mostrar mensajes informativos.
- Salir con `/salir` o `quit`.
- Manejar errores básicos (conexión, modelo, recuperación, etc.).

---

## 📚 Documentos markdown

Debes crear **dos documentos ficticios** de al menos **500 palabras cada uno**:

### `documento1.md`
Incluye:

- Historia de la empresa.
- Misión y visión.
- Servicios ofrecidos.
- Información general corporativa.

### `documento2.md`
Incluye:

- Políticas internas.
- Horarios.
- Beneficios para empleados.
- Código de conducta.
- Procedimientos internos.

---

## 🧩 Tecnologías utilizadas

- **Python 3.10+**
- **LangChain**
- **LangChain OpenAI**
- **OpenAI API**
- **InMemoryVectorStore**
- **python-dotenv**

---

## ⚙️ Configuración del entorno

### 1️. Instalar dependencias


