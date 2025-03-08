from fastapi import FastAPI  # Подключение к базе данных и настройки SessionLocal
from app.database import engine
# Базовый класс для моделей SQLAlchemy # Импорт роутеров для эндпоинтов
from app.models import Base
from app.routers import users, projects, tasks, logs

app = FastAPI(
    title="Kanban Board API",
    description="Демо-проект для практикума: управление канбан-доской",
    version="1.0.0"
)

# Создаем все таблицы в базе данных (для разработки; в продакшене обычно применяются миграции)
Base.metadata.create_all(bind=engine)

# Подключаем роутеры для группировки эндпоинтов
app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(projects.router, prefix="/projects", tags=["Projects"])
app.include_router(tasks.router, prefix="/projects", tags=["Tasks"])
app.include_router(logs.router, prefix="/projects", tags=["Logs"])


@app.get("/")
def read_root():
    return "message good Kanban Board!"
