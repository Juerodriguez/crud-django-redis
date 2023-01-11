from fastapi import APIRouter


api = APIRouter()


@api.get("/")
def read_root():
    return {"message": "Welcome from the API"}
