import jieba
from typing import List, Dict
from config.settings import settings

class RankStrategy:
    @staticmethod
    def extract_keyword(query: str) -> List[str]:
        stop_words = {"的","了","是","在","和","有","我","你","它"}
        words = jieba.lcut(query)
        return [w for w in words if w not in stop_words and len(w)>=2]

    @staticmethod
    def keyword_score(text: str, keywords: List[str]) -> float:
        if not keywords:
            return 0.0
        hit = sum(1 for w in keywords if w in text)
        return hit / len(keywords)

    @staticmethod
    def density_score(text: str) -> float:
        words = jieba.lcut(text)
        unique = len(set(words))
        total = len(words)
        return unique / total if total > 0 else 0.0

    @staticmethod
    def fusion_score(vec_score: float, text: str, keywords: List[str]) -> float:
        bm25_s = RankStrategy.keyword_score(text, keywords)
        den_s = RankStrategy.density_score(text)
        total = (bm25_s * settings.BM25_WEIGHT) + (vec_score * settings.VECTOR_WEIGHT) + (den_s * settings.DENSITY_WEIGHT)
        return round(total, 4)