import fitz
from adapter.base_adapter import BaseAdapter
from entity.document_entity import DocumentEntity
from common.utils import clean_text, md5_hash

class PdfAdapter(BaseAdapter):
    def parse(self, file_path: str) -> DocumentEntity:
        doc = fitz.open(file_path)
        content = ""
        for page in doc:
            content += page.get_text()
        clean_content = clean_text(content)
        file_id = md5_hash(file_path)
        return DocumentEntity(
            file_id=file_id,
            title=file_path.split("/")[-1],
            raw_content=clean_content,
            file_type="pdf",
            file_path=file_path
        )