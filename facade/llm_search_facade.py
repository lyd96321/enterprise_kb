from facade.search_facade import SearchFacade
from llm.llm_decorator import llm_answer_decorator
from llm.langfuse_trace import rag_trace_decorator
from common.decorator.log_decorator import llm_log

class LLMSearchFacade:
    @staticmethod
    @llm_log()
    @rag_trace_decorator()
    @llm_answer_decorator
    def search(query:str):
        return SearchFacade.search(query)
