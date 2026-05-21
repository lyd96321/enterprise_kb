from adapter.base_adapter import BaseAdapter
from entity.document_entity import DocumentEntity
from common.utils import clean_text, md5_hash

class MdAdapter(BaseAdapter):
    def parse(self, file_path: str) -> DocumentEntity:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        clean_content = clean_text(content)
        file_id = md5_hash(file_path)
        return DocumentEntity(
            file_id=file_id,
            title=file_path.split("/")[-1],
            raw_content=clean_content,
            file_type="md",
            file_path=file_path
        )