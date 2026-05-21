from typing import List
from entity.document_entity import DocumentEntity
from entity.chunk_entity import ParentChunk, ChildChunk
from strategy.chunk_strategy import ChunkStrategy
from common.decorator.log_decorator import chunk_log,cost_log

class ChunkService:
    @staticmethod
    @cost_log("文本分块")
    @chunk_log()
    def do_chunk(doc: DocumentEntity) -> tuple[List[ParentChunk], List[ChildChunk]]:
        parents = ChunkStrategy.split_parent(doc)
        all_child = []
        for p in parents:
            children = ChunkStrategy.split_child(p)
            all_child.extend(children)
        return parents, all_child
