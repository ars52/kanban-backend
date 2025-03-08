from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_tasks():
    return {"message": "Список задач"}
