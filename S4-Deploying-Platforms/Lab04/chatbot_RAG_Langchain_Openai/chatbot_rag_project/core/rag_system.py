import os
from typing import List, Dict, Any, Tuple
import numpy as np
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

class InMemoryVectorStore:
    """Simple in-memory vector store: stores (text, embedding, metadata).
    Uses cosine similarity for retrieval."""
    def __init__(self, embedding_model_name: str = None):
        model = embedding_model_name or os.getenv('EMBEDDING_MODEL', 'text-embedding-3-small')
        self._embedder = OpenAIEmbeddings(model=model)
        self.items = []  # list of dicts: {'text':..., 'vec': np.array, 'meta': {...}}

    def add_texts(self, texts: List[str], metadatas: List[Dict[str,Any]] = None):
        metadatas = metadatas or [None]*len(texts)
        # generate embeddings in batches via embedder
        embs = self._embedder.embed_documents(texts)
        for t, e, m in zip(texts, embs, metadatas):
            vec = np.array(e, dtype=float)
            self.items.append({'text': t, 'vec': vec, 'meta': m or {}})

    def _cosine_sim(self, a: np.ndarray, b: np.ndarray) -> float:
        if np.linalg.norm(a)==0 or np.linalg.norm(b)==0:
            return 0.0
        return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

    def retrieve(self, query: str, k: int = 4) -> List[Dict[str,Any]]:
        q_emb = np.array(self._embedder.embed_query(query), dtype=float)
        scored = []
        for it in self.items:
            score = self._cosine_sim(q_emb, it['vec'])
            scored.append((score, it))
        scored.sort(key=lambda x: x[0], reverse=True)
        results = [item for score, item in scored[:k]]
        return results

class RAGSystem:
    def __init__(self, embedding_model_name: str = None):
        self.store = InMemoryVectorStore(embedding_model_name=embedding_model_name)

    def index_documents(self, docs: List[Tuple[str, Dict[str,Any]]], chunk_size: int = 800):
        """docs: list of tuples (text, metadata). We'll chunk by approximate characters to create retrievable passages."""
        texts = []
        metas = []
        for text, meta in docs:
            # simple chunking by characters to keep chunks <= chunk_size
            start = 0
            while start < len(text):
                chunk = text[start:start+chunk_size]
                texts.append(chunk)
                metas.append(meta or {})
                start += chunk_size
        self.store.add_texts(texts, metas)

    def retrieve(self, query: str, k: int = 4):
        return self.store.retrieve(query, k=k)
