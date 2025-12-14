#!/usr/bin/env python3
import os, sys
from dotenv import load_dotenv
from core.rag_system import RAGSystem
from core.chatbot import Chatbot
from pathlib import Path

load_dotenv()

DOCS_DIR = Path(__file__).parent / 'documents'

def load_documents():
    docs = []
    for p in sorted(DOCS_DIR.glob('*.md')):
        text = p.read_text(encoding='utf-8')
        docs.append((text, {'source': p.name}))
    return docs

def main():
    print('Iniciando Chatbot RAG - CLI')
    print('Cargando documentos...')
    docs = load_documents()
    if not docs:
        print('No se encontraron documentos en la carpeta documents/. Añade .md y vuelve a intentarlo.')
        sys.exit(1)

    rag = RAGSystem(embedding_model_name=os.getenv('EMBEDDING_MODEL'))
    print(f'Indexando {len(docs)} documento(s)... Esto requiere llamadas a la API de OpenAI para generar embeddings.')
    rag.index_documents(docs, chunk_size=800)
    print('Indexación completada.')
    model = os.getenv('DEFAULT_MODEL', 'gpt-4o')
    bot = Chatbot(model_name=model)
    print('Escribe tu pregunta. Salir: /salir o quit')

    while True:
        q = input('> ').strip()
        if not q:
            continue
        if q.lower() in ['/salir','quit','/exit']:
            print('Saliendo. ¡Hasta luego!')
            break
        try:
            retrieved = rag.retrieve(q, k=4)
            print(f'-> Recuperadas {len(retrieved)} fragmentos. Generando respuesta...')
            answer = bot.ask(q, retrieved)
            print('\n---\nRespuesta:\n')
            print(answer)
            print('\n---\n')
        except Exception as e:
            print('Error durante la consulta:', str(e))

if __name__ == '__main__':
    main()
