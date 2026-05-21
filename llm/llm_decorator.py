from functools import wraps
from llm.local_llm import LocalLLM
from llm.prompt_template import build_rag_prompt
import tiktoken

def count_token(text:str) -> int:
    enc = tiktoken.get_encoding("cl100k_base")
    return len(enc.encode(text))

def llm_answer_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result["code"] != 200 or len(result["data"]) == 0:
            return {"code":200, "ai_answer":"暂无相关资料", "raw_list":[]}
        context = ""
        for item in result["data"]:
            context += item["chunk_content"] + "\n"
        llm = LocalLLM()
        prompt = build_rag_prompt(kwargs["query"], context)
        ai_text = llm.generate(prompt)
        return {
            "code":200,
            "ai_answer": ai_text,
            "raw_list": result["data"],
            "input_token":count_token(prompt),
            "output_token":count_token(ai_text)
        }
    return wrapper
