from fastapi import APIRouter
from app.main.schemas.books_schema import Books
from app.main.redis_client.crud import save_hash, delete_hash, get_hash
from app.main.redis_client.connection import connection_redis
import json

api = APIRouter()
fake_db = [{
  "id": "bf37f289-8006-4951-95c1-617d9ecb2000",
  "name": "El Sueño",
  "author": "Ricardo Casic",
  "date": "2023-01-13 16:19:46.318739"
}]
r = connection_redis()


@api.get("/")
async def root():
    return {"messaje ": "Bienvenidos para visualizar la documentacion api ir a /docs"}


@api.post("/create", response_model=Books)
def create(books: Books):
    try:
        fake_db.append(books.dict())
        r.set(books.dict()["id"], json.dumps(books.dict()))
        # save_hash(key=books.dict()["id"], data=books.dict())
        return books
    except Exception as e:
        return e


@api.get("/get/{id}")
def get_all(id: str):
    try:
        response = json.loads(r.get(id))

        # The next work with redis external server
        """data = get_hash(key=id)
        if len(data) == 0:
            book = list(filter(lambda field: field["id"] == id, fake_db))[0]
            print(book)
            save_hash(key=id, data=book)
            return book"""

        return response
    except Exception as e:
        return e


@api.get("/get_all")
def get_all():
    try:
        keys_iter = (json.loads(r.get(key)) for key in r.keys())
        response = keys_iter

        return response
    except Exception as e:
        return e


@api.delete("/delete/{id}")
def delete_bykey(id: str):
    try:
        r.delete(id)
        book = list(filter(lambda field: field["id"] == id, fake_db))[0]
        if len(book) != 0:
            fake_db.remove(book)
        return {
            "data": fake_db,
            "messaje": "succes"
        }
    except Exception as e:
        return e
