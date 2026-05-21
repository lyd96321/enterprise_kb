import uuid
from typing import List
from langchain_text_splitters import RecursiveCharacterTextSplitter
from entity.document_entity import DocumentEntity
from entity.chunk_entity import ParentChunk, ChildChunk
from config.settings import settings

class ChunkStrategy:
    @staticmethod
    def split_parent(doc: DocumentEntity) -> List[ParentChunk]:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.PARENT_CHUNK_SIZE,
            chunk_overlap=settings.PARENT_OVERLAP,
            separators=["\n\n", "\n", "。", "，"]
        )
        texts = splitter.split_text(doc.raw_content)
        parent_list = []
        for t in texts:
            pid = str(uuid.uuid4())
            parent_list.append(ParentChunk(
                parent_id=pid,
                content=t,
                file_id=doc.file_id,
                tags=doc.tags
            ))
        return parent_list

    @staticmethod
    def split_child(parent: ParentChunk) -> List[ChildChunk]:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHILD_CHUNK_SIZE,
            chunk_overlap=settings.CHILD_OVERLAP,
            separators=["。", "，", " "]
        )
        texts = splitter.split_text(parent.content)
        child_list = []
        for t in texts:
            cid = str(uuid.uuid4())
            child_list.append(ChildChunk(
                child_id=cid,
                parent_id=parent.parent_id,
                content=t,
                file_id=parent.file_id
            ))
        return child_list