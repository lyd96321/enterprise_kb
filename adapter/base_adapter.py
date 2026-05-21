from abc import ABC, abstractmethod
from entity.document_entity import DocumentEntity

class BaseAdapter(ABC):
    @abstractmethod
    def parse(self, file_path: str) -> DocumentEntity:
        pass