from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from schemas.article import Article
from config.database import Session
from services.article import ArticleService

article_router = APIRouter()

@article_router.post('/create-article', tags=['article'], response_model=dict, status_code=201)
def create_article(article: Article) -> dict:
    db = Session()
    ArticleService(db).create_article(article)
    return JSONResponse(content={"message": "Se ha registrado"})

@article_router.get('/get-articles', tags=['article'], response_model=dict, status_code=200)
def get_article() -> dict:
    db = Session()
    articles = ArticleService(db).get_articles()
    return JSONResponse(content=jsonable_encoder(articles))