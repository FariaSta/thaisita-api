from pydantic import BaseModel, Field
from typing import Optional

class Article(BaseModel):
    title: str
    descripton: str
    category: str
    poster: Optional[str]

    class Config:
        schema_extra = {
            "title": "Post",
            "descripton": "Descripcion del post",
            "category": "salud",
            "poster": "www.google.com",
        }
