from fastapi import FastAPI
from .routers import audit

app = FastAPI()

app.include_router(audit.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Ethics Sentinel API"}
