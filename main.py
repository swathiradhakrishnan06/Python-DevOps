import uvicorn
from src.logic import wiki_search
from src.logic import wiki as wiki_summary
from fastapi import FastAPI

app = FastAPI()

@app.get("/search/{term}")
async def search(term: str):
    """Wiki search suggestions"""
    results = wiki_search(term)
    return {"result": results}

@app.get("/wiki/{name}")
async def wiki(name: str):
    """Wiki summary"""
    results = wiki_summary(name)
    return {"result": results}

if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
