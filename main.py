from fastapi import FastAPI
import uvicorn
from mylib.logic import search_wiki
from mylib.logic import wiki as wikipage
from mylib.logic import phrases as wikiphrases

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API. Call /search or /wiki"}


@app.get("/search/{value}")
async def search(value: str):
    """Page to search in Wikipedia"""

    results = search_wiki(value)
    return {"Search Results": results}


@app.get("/wiki/{name}")
async def wiki(name: str):
    """Retrieve Wikipedia page"""

    results = wikipage(name)
    return {"Wikipedia Page": results}


@app.get("/wiki/phrases/{name}")
async def phrases(name: str):
    results = wikiphrases(name)
    return {"Wikipedia Phrases": results}


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
