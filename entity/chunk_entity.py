from dataclasses import dataclass, field
from typing import List

@dataclass
class ParentChunk:
    parent_id: str
    content: str
    file_id: str
    tags: List[str]

@dataclass
class ChildChunk:
    child_id: str
    parent_id: str
    content: str
    file_id: str