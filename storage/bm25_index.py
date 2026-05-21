import pickle
import jieba
from rank_bm25 import BM25Okapi
from config.settings import settings

class BM25Index:
    def __init__(self):
        self.corpus = []
        self.meta = []
        self.bm25 = None
        self.load_cache()

    def add_data(self, content: str, meta_info: dict):
        token = jieba.lcut(content)
        self.corpus.append(token)
        self.meta.append(meta_info)
        self.bm25 = BM25Okapi(self.corpus)
        self.save_cache()

    def search(self, query: str, top_k: int) -> list:
        if not self.bm25:
            return []
        tokens = jieba.lcut(query)
        scores = self.bm25.get_scores(tokens)
        ranked = sorted(zip(self.meta, scores), key=lambda x:x[1], reverse=True)
        return ranked[:top_k]

    def save_cache(self):
        with open(settings.BM25_CACHE_PATH, "wb") as f:
            pickle.dump((self.corpus, self.meta), f)

    def load_cache(self):
        try:
            with open(settings.BM25_CACHE_PATH, "rb") as f:
                self.corpus, self.meta = pickle.load(f)
                self.bm25 = BM25Okapi(self.corpus)
        except:
            pass