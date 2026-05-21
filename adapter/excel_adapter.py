import pandas as pd
from adapter.base_adapter import BaseAdapter
from entity.document_entity import DocumentEntity
from common.utils import clean_text, md5_hash

class ExcelAdapter(BaseAdapter):
    def parse(self, file_path: str) -> DocumentEntity:
        df_list = pd.read_excel(file_path, sheet_name=None)
        content = ""
        for sheet_name, df in df_list.items():
            content += f"【工作表：{sheet_name}】\n" + df.to_string()
        clean_content = clean_text(content)
        file_id = md5_hash(file_path)
        return DocumentEntity(
            file_id=file_id,
            title=file_path.split("/")[-1],
            raw_content=clean_content,
            file_type="xlsx",
            file_path=file_path
        )