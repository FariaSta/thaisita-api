from fastapi import FastAPI
from config.database import engine, Base
from routers.article import article_router
# from models.article import Article
import uvicorn
import os

# For production:
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0",
    port=int(os.environ.get("PORT", 8000)))

app = FastAPI()
app.title = "Thaisita Api"
app.version = "0.0.1"

app.include_router(article_router)

Base.metadata.create_all(bind=engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}

