from fastapi import FastAPI
from app.dependencies import mongo
from app.routers import activity, healthcheck

try:
    app = FastAPI()
    app.include_router(activity.router)
    app.include_router(healthcheck.router)
finally:
    mongo().close()
