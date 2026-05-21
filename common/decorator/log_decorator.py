from functools import wraps
import time
from common.log_config import kb_logger

def cost_log(func_name:str):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            try:
                res = func(*args, **kwargs)
                cost = round(time.time() - start, 4)
                kb_logger.info(f"【{func_name}】执行成功，耗时={cost}s")
                return res
            except Exception as e:
                kb_logger.error(f"【{func_name}】执行异常：{str(e)}", exc_info=True)
                raise e
        return wrapper
    return decorator

def parse_log():
    def decorator(func):
        @wraps(func)
        def wrapper(file_path:str):
            kb_logger.info(f"开始解析文件：{file_path}")
            doc = func(file_path)
            kb_logger.info(
                f"解析完成 | 文件类型={doc.file_type} | 原始字符数={len(doc.raw_content)} | tags={doc.tags}"
            )
            return doc
        return wrapper
    return decorator

def chunk_log():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            parents, children = func(*args, **kwargs)
            kb_logger.info(
                f"【文本分块】父块数量={len(parents)} | 子块数量={len(children)}"
            )
            for idx, p in enumerate(parents):
                kb_logger.debug(f"父块{idx+1} 字数：{len(p.content)}")
            return parents, children
        return wrapper
    return decorator

def search_log():
    def decorator(func):
        @wraps(func)
        def wrapper(query:str):
            kb_logger.info(f"【用户检索】query={query}")
            res = func(query)
            data_len = len(res.get("data", []))
            kb_logger.info(f"【检索结束】召回片段数量={data_len}")
            return res
        return wrapper
    return decorator

def llm_log():
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            ans = res.get("ai_answer", "")
            input_t = res.get("input_token", 0)
            output_t = res.get("output_token", 0)
            kb_logger.info(
                f"【LLM生成】输入token={input_t} | 输出token={output_t} | 回答长度={len(ans)}"
            )
            return res
        return wrapper

    return decorator