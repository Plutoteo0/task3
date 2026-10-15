from lcm import lcm
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/plutoteo0_gmail_com", response_class=PlainTextResponse)
def lcm_route(x: str | None = None, y: str | None = None):
    return lcm(x, y)