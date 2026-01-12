from fastapi import FastAPI
from routes.ip_route import ip_router

app = FastAPI()

app.include_router(ip_router)