import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME = "Enterprise-Knowledge-Base"
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    LOG_DIR = os.path.join(BASE_DIR, "logs")
    os.makedirs(LOG_DIR, exist_ok=True)

    PARENT_CHUNK_SIZE = 850
    PARENT_OVERLAP = 120
    CHILD_CHUNK_SIZE = 350
    CHILD_OVERLAP = 80

    BM25_WEIGHT = 0.45
    VECTOR_WEIGHT = 0.35
    DENSITY_WEIGHT = 0.20

    EMBEDDING_MODEL = "BAAI/bge-small-zh-v1.5"
    DEVICE = "cpu"

    DB_PATH = os.path.join(BASE_DIR, "storage", "knowledge.db")
    BM25_CACHE_PATH = os.path.join(BASE_DIR, "storage", "bm25_cache.pkl")

    # ========== Qdrant 向量库配置 ==========
    # 本地模式：使用内存+磁盘存储
    QDRANT_MODE = os.getenv("QDRANT_MODE", "local")  # "local" 或 "remote"
    QDRANT_PATH = os.path.join(BASE_DIR, "storage", "qdrant")  # 本地存储路径
    
    # 远程模式：连接到 Qdrant 服务器
    QDRANT_HOST = os.getenv("QDRANT_HOST", "localhost")
    QDRANT_PORT = int(os.getenv("QDRANT_PORT", "6333"))
    QDRANT_API_KEY = os.getenv("QDRANT_API_KEY", None)
    
    # 集合配置
    QDRANT_COLLECTION_NAME = "enterprise_knowledge_base"
    QDRANT_VECTOR_SIZE = 384  # BAAI/bge-small-zh-v1.5 的向量维度
    
    RETRIEVE_TOP_K = 8
    FINAL_TOP_N = 5

    WHISPER_MODEL = "base"
    FFMPEG_SAMPLE_RATE = 16000

    # ========== LANGFUSE 监控配置（使用环境变量） ==========
    LANGFUSE_PUBLIC_KEY = os.getenv("LANGFUSE_PUBLIC_KEY", "")
    LANGFUSE_SECRET_KEY = os.getenv("LANGFUSE_SECRET_KEY", "")
    LANGFUSE_HOST = os.getenv("LANGFUSE_HOST", "http://localhost:3300")


settings = Settings()
