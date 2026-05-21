from docx import Document
from adapter.base_adapter import BaseAdapter
from entity.document_entity import DocumentEntity
from common.utils import clean_text, md5_hash

class WordAdapter(BaseAdapter):
    def parse(self, file_path: str) -> DocumentEntity:
        doc = Document(file_path)
        content = "\n".join([p.text for p in doc.paragraphs])
        clean_content = clean_text(content)
        file_id = md5_hash(file_path)
        return DocumentEntity(
            file_id=file_id,
            title=file_path.split("/")[-1],
            raw_content=clean_content,
            file_type="docx",
            file_path=file_path
        )