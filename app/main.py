from fastapi import FastAPI

from app.config import get_settings
from app.routes.chat import router as chat_router

settings = get_settings()
app = FastAPI(title=settings.app_name)

app.include_router(chat_router)


@app.get("/health")
def health():
    return {"status": "ok"}