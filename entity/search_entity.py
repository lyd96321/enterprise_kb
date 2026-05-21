from dataclasses import dataclass, field
from typing import List

@dataclass
class SearchResult:
    file_name: str
    file_path: str
    chunk_content: str
    tags: List[str]
    score: float
    file_type: str