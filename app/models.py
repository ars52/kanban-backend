from sqlalchemy import Column, Integer, String
from app.database import Base

# Пример простой модели Project


class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
