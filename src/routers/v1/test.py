from fastapi import APIRouter

testrouter = APIRouter(prefix="/test")


@testrouter.get(path="my_test_path",
                )
