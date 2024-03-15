import netaddr.core

from fastapi import FastAPI
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
async def check_ip_version(ip: str):
    try:
        ip_version = IPAddress(ip).version
        return {"message": f'IP {ip} is IPv{ip_version}'}
    except netaddr.core.AddrFormatError:
        return {"message": f'{ip} is not a valid IP address.'}
