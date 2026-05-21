from langfuse import Langfuse
from functools import wraps
from config.settings import settings

class LangfuseTracer:
    def __init__(self):
        self.lf = Langfuse(
            public_key=settings.LANGFUSE_PUBLIC_KEY,
            secret_key=settings.LANGFUSE_SECRET_KEY,
            host=settings.LANGFUSE_HOST
        )

    def get_tracer(self):
        return self.lf

def rag_trace_decorator():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            lf = LangfuseTracer().get_tracer()
            trace = lf.trace(
                name="enterprise_rag_search",
                input=kwargs.get("query", "")
            )
            result = func(*args, **kwargs)
            if result.get("raw_list"):
                contexts = [item["chunk_content"] for item in result["raw_list"]]
                trace.update(contexts=contexts)
            if result.get("ai_answer"):
                trace.update(output=result["ai_answer"])
            return result
        return wrapper
    return decorator
