from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class DocumentEntity:
    file_id: str
    title: str
    raw_content: str
    file_type: str
    file_path: str
    tags: List[str] = field(default_factory=list)
    meta: Dict = field(default_factory=dict)