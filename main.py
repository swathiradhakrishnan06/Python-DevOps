import uvicorn
from src.logic import wiki_search
from src.logic import wiki as wiki_summary
from src.logic import phrase as wiki_phrase
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"msg": "Wikipedia API"}


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


@app.get("/phrase/{name}")
async def phrase(name: str):
    """Wiki summary noun phrases"""
    phrases = wiki_phrase(name)
    return {"result": phrases}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
