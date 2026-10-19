from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.routers.tasks import router as tasks_router
from app.infrastructure.database.models import Base
from app.infrastructure.database.session import engine


@asynccontextmanager
async def lifespan(_: FastAPI):
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(title="Python Clean Architecture API", version="0.2.0", lifespan=lifespan)
app.include_router(tasks_router, prefix="/api/v1")


@app.get("/health", tags=["health"])
def health() -> dict[str, str]:
    return {"status": "ok"}
