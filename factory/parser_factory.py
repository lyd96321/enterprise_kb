from common.utils import get_file_suffix
from adapter.pdf_adapter import PdfAdapter
from adapter.word_adapter import WordAdapter
from adapter.excel_adapter import ExcelAdapter
from adapter.md_adapter import MdAdapter
from adapter.video_adapter import VideoAdapter

class ParserFactory:
    _MAP = {
        "pdf": PdfAdapter,
        "docx": WordAdapter,
        "doc": WordAdapter,
        "xlsx": ExcelAdapter,
        "md": MdAdapter,
        "mp4": VideoAdapter
    }

    @staticmethod
    def get_parser(file_path: str):
        suffix = get_file_suffix(file_path)
        if suffix not in ParserFactory._MAP:
            raise Exception(f"不支持的文件格式：{suffix}")
        return ParserFactory._MAP[suffix]()