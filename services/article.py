from models.article import Article as ArticleModel
from schemas.article import Article


class ArticleService():

    def __init__(self, db) -> None:
        self.db = db

    def create_article(self, article: Article):
        new_article = ArticleModel(**article.dict())
        self.db.add(new_article)
        self.db.commit()
        return