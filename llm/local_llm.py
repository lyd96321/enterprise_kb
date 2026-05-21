import requests
from llm.llm_base import BaseLLM
class LocalLLM(BaseLLM):
    def __init__(self):
        self.url = "http://localhost:11434/api/generate"
        self.model_name = "qwen3:4b"
    def generate(self, prompt: str) -> str:
        res = requests.post(self.url, json={"model":self.model_name,"prompt":prompt,"stream":False})
        return res.json()["response"]
