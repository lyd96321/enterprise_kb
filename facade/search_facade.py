from service.search_service import SearchService
from storage.db import SqliteDB

class SearchFacade:
    @staticmethod
    def search(query: str):
        raw_list = SearchService().search(query)
        db = SqliteDB()
        result = []
        for item in raw_list:
            meta = item["meta"]
            file_id = meta["file_id"]
            res = db.query("SELECT title,file_path,file_type,tags FROM document WHERE file_id=?", (file_id,))
            if not res:
                continue
            title, path, f_type, tags = res[0]
            result.append({
                "file_name": title,
                "file_path": path,
                "file_type": f_type,
                "tags": tags.split(","),
                "chunk_content": item["content"],
                "score": item["total_score"]
            })
        return {"code":200, "data":result}