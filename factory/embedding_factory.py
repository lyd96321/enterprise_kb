from langchain_community.embeddings import HuggingFaceEmbeddings
from config.settings import settings

class EmbeddingFactory:
    @staticmethod
    def get_embedding():
        return HuggingFaceEmbeddings(
            model_name=settings.EMBEDDING_MODEL,
            model_kwargs={"device": settings.DEVICE}
        )