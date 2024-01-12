import uvicorn

from fastapi import FastAPI, Depends
from typing import Annotated
from db.session import Session
from db import get_db
from crud import get_all

app = FastAPI()


@app.get("/")
async def get_flats(db: Annotated[Session, Depends(get_db)]):
    return get_all(db=db)


if __name__ == "__main__":
    uvicorn.run("server:app", host="localhost", port=8080, reload=True)
