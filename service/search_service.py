from typing import List
from factory.vector_factory import VectorFactory
from storage.bm25_index import BM25Index
from strategy.rank_strategy import RankStrategy
from common.decorator.cache_decorator import search_cache
from config.settings import settings

class SearchService:
    def __init__(self):
        self.vector_db = VectorFactory().get_chroma_vector()
        self.bm25 = BM25Index()

    @search_cache()
    def search(self, query: str) -> list:
        keywords = RankStrategy.extract_keyword(query)
        vec_res = self.vector_db.similarity_search_with_score(query, k=settings.RETRIEVE_TOP_K)
        bm25_res = self.bm25.search(query, settings.RETRIEVE_TOP_K)
        merge = []
        for doc, score in vec_res:
            merge.append({
                "content": doc.page_content,
                "meta": doc.metadata,
                "vec_score": 1 - score
            })
        for item in merge:
            s = RankStrategy.fusion_score(item["vec_score"], item["content"], keywords)
            item["total_score"] = s
        merge.sort(key=lambda x:x["total_score"], reverse=True)
        return merge[:settings.FINAL_TOP_N]