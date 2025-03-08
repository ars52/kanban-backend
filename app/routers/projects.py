from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def read_projects():
    return {"message": "Список проектов"}
