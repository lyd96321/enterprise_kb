from langchain_community.vectorstores import Qdrant
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from factory.embedding_factory import EmbeddingFactory
from config.settings import settings
import logging

logger = logging.getLogger(__name__)

class VectorFactory:
    _qdrant_client = None
    _vector_db = None
    
    def __init__(self):
        self.embedding = EmbeddingFactory.get_embedding()
    
    @staticmethod
    def get_qdrant_client():
        """获取 Qdrant 客户端（单例模式）"""
        if VectorFactory._qdrant_client is None:
            try:
                if settings.QDRANT_MODE == "local":
                    # 本地模式：使用文件存储
                    VectorFactory._qdrant_client = QdrantClient(
                        path=settings.QDRANT_PATH
                    )
                    logger.info(f"✓ 本地 Qdrant 客户端已初始化 (路径: {settings.QDRANT_PATH})")
                else:
                    # 远程模式：连接到 Qdrant 服务器
                    VectorFactory._qdrant_client = QdrantClient(
                        host=settings.QDRANT_HOST,
                        port=settings.QDRANT_PORT,
                        api_key=settings.QDRANT_API_KEY
                    )
                    logger.info(f"✓ 远程 Qdrant 客户端已初始化 ({settings.QDRANT_HOST}:{settings.QDRANT_PORT})")
            except Exception as e:
                logger.error(f"✗ Qdrant 客户端初始化失败: {str(e)}")
                raise
        
        return VectorFactory._qdrant_client
    
    @staticmethod
    def ensure_collection_exists(client, collection_name, vector_size):
        """确保集合存在，如果不存在则创建"""
        try:
            # 检查集合是否存在
            client.get_collection(collection_name)
            logger.info(f"✓ 集合 '{collection_name}' 已存在")
        except Exception:
            # 集合不存在，创建新集合
            try:
                client.create_collection(
                    collection_name=collection_name,
                    vectors_config=VectorParams(
                        size=vector_size,
                        distance=Distance.COSINE
                    )
                )
                logger.info(f"✓ 集合 '{collection_name}' 创建成功")
            except Exception as e:
                logger.error(f"✗ 创建集合 '{collection_name}' 失败: {str(e)}")
                raise
    
    def get_qdrant_vector(self):
        """获取 LangChain Qdrant 向量库实例"""
        if VectorFactory._vector_db is None:
            try:
                client = self.get_qdrant_client()
                
                # 确保集合存在
                self.ensure_collection_exists(
                    client,
                    settings.QDRANT_COLLECTION_NAME,
                    settings.QDRANT_VECTOR_SIZE
                )
                
                # 创建 LangChain 包装的 Qdrant 实例
                VectorFactory._vector_db = Qdrant(
                    client=client,
                    collection_name=settings.QDRANT_COLLECTION_NAME,
                    embeddings=self.embedding
                )
                logger.info(f"✓ Qdrant 向量库已加载")
            except Exception as e:
                logger.error(f"✗ Qdrant 向量库加载失败: {str(e)}")
                raise
        
        return VectorFactory._vector_db
    
    # 保留兼容性方法
    def get_chroma_vector(self):
        """兼容旧代码的方法（实际使用 Qdrant）"""
        return self.get_qdrant_vector()
