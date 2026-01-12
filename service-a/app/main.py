from fastapi import FastAPI
from app.routes.ip_route import ip_router

app = FastAPI

app.include_router(ip_router)