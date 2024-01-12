import uvicorn

from fastapi import FastAPI, Depends, Request
from typing import Annotated

from db.session import Session
from db import get_db
from crud import get_all
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def get_flats(request: Request, db: Annotated[Session, Depends(get_db)]):
    flats = get_all(db=db)
    return templates.TemplateResponse(
        request=request, name="flats.html", context={"flats": flats}
    )


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8080, reload=True, proxy_headers=True)
