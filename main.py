from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI()


@app.get('/')
def index(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {
            'data': f'{limit} published blogs from DB'
        }
    else:
        return {
            'data': f'{limit} all blogs from DB'
        }


@app.get('/blog/unpublished')
def unpublished():
    return {
        'data': 'all unpublished blogs'
    }


@app.get('/blog/{id}')
def about(id: int):
    return {
        'data': id
    }


@app.get('/blog/{id}/comments')
def comments(id: int, limit=10):
    return limit
    return {
        'data': {'comments': {'comment1', 'comment2', 'comment3'}}
    }


class Blog(BaseModel):
    title: str
    body: str
    published_at: Optional[bool]


@app.post('/blog/{id}/')
def create_blog(blog: Blog):
    return {
        'data': f'blog is created with title as {blog.title}'
    }


if __name__ == '__main__':
    uvicorn.run(
        app,
        host='172.0.0.1',
        port='8000'
    )
