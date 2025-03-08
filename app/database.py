# app/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Пропиши здесь реальные данные подключения к PostgreSQL
DATABASE_URL = "postgresql://postgres:123@localhost:5432/postgres"


# Создаём объект engine
engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Объявляем базовый класс для всех моделей
Base = declarative_base()
