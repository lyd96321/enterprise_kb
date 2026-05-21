from typing import List
from factory.vector_factory import VectorFactory
from entity.chunk_entity import ChildChunk
from storage.db import SqliteDB
from common.decorator.log_decorator import cost_log

class VectorService:
    def __init__(self):
        self.vector_db = VectorFactory().get_chroma_vector()
        self.db = SqliteDB()

    @cost_log("向量入库")
    def insert_child_chunk(self, child_list: List[ChildChunk]):
        texts = []
        metas = []
        for child in child_list:
            texts.append(child.content)
            metas.append({
                "child_id": child.child_id,
                "parent_id": child.parent_id,
                "file_id": child.file_id
            })
            self.db.insert(
                "INSERT INTO chunk_relation VALUES (?,?,?,?)",
                (child.child_id, child.parent_id, child.file_id, child.content)
            )
        self.vector_db.add_texts(texts=texts, metadatas=metas)
        self.vector_db.persist()
