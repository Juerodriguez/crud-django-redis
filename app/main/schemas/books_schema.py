from datetime import datetime
from pydantic import BaseModel, Field
from uuid import uuid4


def generate_uuid():
    return str(uuid4())


def generate_date():
    return str(datetime.now())


class Books(BaseModel):
    id: str = Field(default_factory=generate_uuid)
    name: str
    author: str
    date: str = Field(default_factory=generate_date)
