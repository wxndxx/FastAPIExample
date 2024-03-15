from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from netaddr import IPAddress

app = FastAPI()


@app.get("/",
         include_in_schema=False)
async def root():
    return RedirectResponse("/docs")


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get('/ip')
async def get_user_ip(request: Request):
    ip_version = IPAddress(request.client.host).version
    return {"message": f'Your IPv{ip_version} is {request.client.host}'}
