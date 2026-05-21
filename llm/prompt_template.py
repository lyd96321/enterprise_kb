def build_rag_prompt(question:str, context:str) -> str:
    prompt = f"""你是企业内部知识库助手，只能根据参考资料回答。严禁编造、没有就回答暂无相关资料。
【参考资料】{context}
【用户问题】{question}
简洁专业回答："""
    return prompt
