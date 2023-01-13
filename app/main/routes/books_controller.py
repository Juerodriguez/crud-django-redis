from fastapi import APIRouter
from app.main.schemas.books_schema import Books

api = APIRouter()
fake_db = [{
  "id": "bf37f289-8006-4951-95c1-617d9ecb2000",
  "name": "El Sueño",
  "author": "Ricardo Casic",
  "date": "2023-01-13 16:19:46.318739"
}]


@api.post("/create", response_model=Books)
def create(books: Books):
    try:
        fake_db.append(books.dict())
        return books
    except Exception as e:
        return e


@api.get("/get/{id}")
def get(id: str):
    try:
        return list(filter(lambda field: field["id"] == id, fake_db))[0]
    except Exception as e:
        return e


@api.delete("/delete/{id}")
def get(id: str):
    try:
        book = list(filter(lambda field: field["id"] == id, fake_db))[0]
        if len(book) != 0:
            fake_db.remove(book)
        return {
            "data": fake_db,
            "messaje": "succes"
        }
    except Exception as e:
        return e