import re
import hashlib

def md5_hash(text: str) -> str:
    return hashlib.md5(text.encode("utf-8")).hexdigest()

def clean_text(raw_text: str) -> str:
    text = re.sub(r"\n+", "\n", raw_text)
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[^\u4e00-\u9fa5a-zA-Z0-9\s\.,;:，。；：、]", "", text)
    return text.strip()

def get_file_suffix(file_path: str) -> str:
    return file_path.split(".")[-1].lower()
