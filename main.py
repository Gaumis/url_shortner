from fastapi import FastAPI
from controllers.url_controller import router
from db.init_db import init_db

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(router)