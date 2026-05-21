from langchain_community.vectorstores import Chroma
from factory.embedding_factory import EmbeddingFactory
from config.settings import settings

class VectorFactory:
    def __init__(self):
        self.embedding = EmbeddingFactory.get_embedding()

    def get_chroma_vector(self):
        db = Chroma(
            persist_directory=settings.CHROMA_PATH,
            embedding_function=self.embedding
        )
        return db