from fastapi import FastAPI
from . import schema

app = FastAPI()


@app.post('/blog')
def create(blog: schema.Blog):
    return {
        'title': blog.title,
        'body': blog.body
    }
