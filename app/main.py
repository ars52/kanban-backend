from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routers import users, projects, tasks, logs  # сущности

app = FastAPI(
    title="Kanban Board API",
    description="Управление канбан-доской",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

# роутеры для группировки эндпоинтов
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(projects.router, prefix="/projects", tags=["Projects"])
app.include_router(tasks.router, prefix="/projects", tags=["Tasks"])
app.include_router(logs.router, prefix="/projects", tags=["Logs"])


@app.get("/")
def read_root():
    return "message good Kanban Board!"
