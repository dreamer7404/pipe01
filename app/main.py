from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/favicon.ico", response_class=HTMLResponse)
async def favicon():
    return Response(content="", media_type="image/x-icon")

@app.get("/")
async def welcome() -> dict:
    return {"message": "Hello World!!!"}