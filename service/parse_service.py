from factory.parser_factory import ParserFactory
from entity.document_entity import DocumentEntity
from common.decorator.log_decorator import parse_log,cost_log

class ParseService:
    @staticmethod
    @cost_log("文件解析")
    @parse_log()
    def parse_file(file_path: str) -> DocumentEntity:
        parser = ParserFactory.get_parser(file_path)
        return parser.parse(file_path)
