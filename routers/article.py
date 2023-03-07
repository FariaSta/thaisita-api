from fastapi import APIRouter
from fastapi.responses import JSONResponse
from schemas.article import Article
from config.database import Session
from services.article import ArticleService

article_router = APIRouter()

@article_router.post('/create-article', tags=['article'], response_model=dict, status_code=201)
def create_post(article: Article) -> dict:
    db = Session()
    ArticleService(db).create_article(article)
    return JSONResponse(content={"message": "Se ha registrado"})