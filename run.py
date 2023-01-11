from app.main import create_app
from app.main.routes.manipulate_object_controller import api


app = create_app()
app.include_router(api)
