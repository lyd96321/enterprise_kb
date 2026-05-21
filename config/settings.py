import os


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
    CHROMA_PATH = os.path.join(BASE_DIR, "storage", "chroma_db")
    BM25_CACHE_PATH = os.path.join(BASE_DIR, "storage", "bm25_cache.pkl")

    RETRIEVE_TOP_K = 8
    FINAL_TOP_N = 5

    WHISPER_MODEL = "base"
    FFMPEG_SAMPLE_RATE = 16000

    # ========== LANGFUSE 监控配置（直接改这里） ==========
    LANGFUSE_PUBLIC_KEY = "pk-lf-a44bc5ce-b22e-4dda-ad45-7daf1274c6af"
    LANGFUSE_SECRET_KEY = "sk-lf-dc389649-b394-42e5-b68b-5aa199e6c1f5"
    LANGFUSE_HOST = "http://172.21.0.185:3300"


settings = Settings()
