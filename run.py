from app.main import create_app
from app.main.routes.books_controller import api


app = create_app()
app.include_router(api, prefix="/books", tags=["Books CRUD"])
