import uvicorn

from fastapi import FastAPI

from app.core.config import settings
from app.api.routers import router


app = FastAPI(
    title=settings.app_title,
    description=settings.desc,
)


app.include_router(router)


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
