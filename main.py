from fastapi import FastAPI
import uvicorn
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from facade.import_facade import ImportFacade
from facade.search_facade import SearchFacade
from facade.llm_search_facade import LLMSearchFacade

app = FastAPI(docs_url=None, redoc_url=None)

@app.get("/docs")
async def custom_docs():
    return get_swagger_ui_html(
        openapi_url="/openapi.json",
        title="知识库接口文档",
        swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@4/swagger-ui-bundle.min.js",
        swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@4/swagger-ui.min.css"
    )

@app.get("/openapi.json")
async def openapi_json():
    return get_openapi(title="企业私有化知识库", version="1.0.0", routes=app.routes)

@app.post("/import")
def import_api(file_path: str):
    return ImportFacade.import_file(file_path)

@app.get("/search")
def search_api(query: str):
    return SearchFacade.search(query)

@app.get("/ai_search")
def ai_search_api(query: str):
    return LLMSearchFacade.search(query)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=False)
