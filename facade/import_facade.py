from service.parse_service import ParseService
from service.chunk_service import ChunkService
from service.tag_service import TagService
from service.vector_service import VectorService
from storage.bm25_index import BM25Index
from storage.db import SqliteDB

class ImportFacade:
    @staticmethod
    def import_file(file_path: str):
        doc = ParseService.parse_file(file_path)
        doc.tags = TagService.generate_tags(doc.raw_content)
        parents, children = ChunkService.do_chunk(doc)
        VectorService().insert_child_chunk(children)
        for c in children:
            BM25Index().add_data(c.content, {"file_id":c.file_id})
        db = SqliteDB()
        tag_str = ",".join(doc.tags)
        db.insert(
            "INSERT INTO document VALUES (?,?,?,?,?)",
            (doc.file_id, doc.title, doc.file_type, doc.file_path, tag_str)
        )
        return {"code":200, "msg":"入库成功", "file_id":doc.file_id}