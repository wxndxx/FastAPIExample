import netaddr.core

from fastapi import FastAPI
from netaddr import IPAddress


app = FastAPI()


@app.get("/",
         include_in_schema=False)
async def root():
    return {"message": "Timeweb Cloud + FastAPI = ❤"}


@app.get('/ip')
async def check_ip_version(ip: str):
    try:
        ip_version = IPAddress(ip).version
        return {"message": f'IP {ip} is IPv{ip_version}'}
    except netaddr.core.AddrFormatError:
        return {"message": f'{ip} is not a valid IP address.'}
